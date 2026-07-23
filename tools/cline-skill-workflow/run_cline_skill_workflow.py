"""Run a Cline-powered maintenance workflow across skill folders in parallel."""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import datetime as dt
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SKILL_ROOTS = (
    REPO_ROOT / 'skills',
)
DEFAULT_LOG_ROOT = REPO_ROOT / '.cline-logs' / 'skill-runs'
SKILL_NAME_PATTERN = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


DEFAULT_PROMPT_TEMPLATE = """Maintain this Agent Skill directory: {skill_path}

Goal:
- Review the skill for format, clarity, portability, references, validation readiness, and usefulness.
- Improve or update the skill in place only when the change is safe, narrow, and directly supported by the existing content.
- Validate the result against the repository's skill and markdown rules when practical.
- Report what changed, what was reviewed, validation performed, and any remaining issues.

Required skill guidance:
- Use the `author-agent-skill` Agent Skill as the governing guidance for this task.
- Prefer an `author-agent-skill/SKILL.md` found under the repository's `skills/` tree.
- Otherwise report that the governing skill is unavailable rather than assuming a different repository layout.
- Apply its guidance for frontmatter, naming, metadata versioning, body structure, progressive disclosure, portability, plain formatting, validation, and handoff notes.

Required scope control:
- Work only in this skill directory unless a referenced supporting file in the same skill directory needs a directly related update.
- Do not edit synced targets directly when the source-of-truth rule indicates a shared source should be edited instead.
- Do not change unrelated skills or repository files.
- Keep reusable content portable and free of repository-local paths unless a section is explicitly repository-specific.
- Keep markdown plain: no emojis, decorative separators, banners, or ornamental formatting.

Review checklist:
- `author-agent-skill` guidance was read or explicitly considered before reviewing or editing.
- SKILL.md starts with YAML frontmatter.
- Frontmatter includes name, description, and metadata.version when this repository convention expects it.
- Frontmatter name matches the parent directory and is valid kebab-case.
- The body has a clear top-level heading and actionable instructions.
- Metadata versioning is preserved or incremented when skill behavior changes.
- Local references to scripts, references, assets, or other skills are valid.
- Optional scripts, references, and assets are necessary and referenced clearly when relevant.

Before finishing:
- Run the narrowest relevant validation command for this skill when practical.
- If validation is skipped, explain why.
- Provide a concise per-skill handoff summary.
"""


@dataclasses.dataclass(frozen=True)
class SkillTask:
    """A single skill directory and its derived execution metadata."""

    path: Path
    relative_path: str
    log_path: Path
    data_dir: Path


@dataclasses.dataclass(frozen=True)
class TaskResult:
    """Result from one Cline CLI invocation."""

    task: SkillTask
    returncode: int
    command: list[str]


def repo_relative(path: Path) -> str:
    """Return a POSIX-style repository-relative path."""

    return path.relative_to(REPO_ROOT).as_posix()


def display_path(path: Path) -> str:
    """Return a repository-relative path, or an absolute path when external."""

    try:
        return repo_relative(path)
    except ValueError:
        return path.resolve().as_posix()


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            'Run the same Cline maintenance prompt across Agent Skill folders '
            'with bounded parallelism.'
        )
    )
    parser.add_argument(
        '--root',
        action='append',
        type=Path,
        help=(
            'Skill root to scan. May be repeated. Defaults to all repository '
            'skill roots.'
        ),
    )
    parser.add_argument(
        '--skill',
        action='append',
        help=(
            'Skill directory name or repository-relative path to include. May be '
            'repeated. Defaults to every skill under selected roots.'
        ),
    )
    parser.add_argument(
        '--concurrency',
        type=int,
        default=10,
        help='Maximum number of Cline tasks to run at once. Default: 10.',
    )
    parser.add_argument(
        '--prompt-file',
        type=Path,
        help='Optional file containing a custom prompt template.',
    )
    parser.add_argument(
        '--review-only',
        action='store_true',
        help='Ask Cline to review and report only, without editing files.',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print planned Cline commands without running them.',
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=0,
        help='Per-skill Cline timeout in seconds. Default: 0, no timeout.',
    )
    parser.add_argument(
        '--thinking',
        default='medium',
        choices=('none', 'low', 'medium', 'high', 'xhigh'),
        help='Cline reasoning effort level. Default: medium.',
    )
    parser.add_argument(
        '--provider',
        help='Optional Cline provider id passed through to --provider.',
    )
    parser.add_argument(
        '--model',
        help='Optional model id passed through to --model.',
    )
    parser.add_argument(
        '--cline-bin',
        default='cline',
        help='Cline executable to invoke. Default: cline.',
    )
    parser.add_argument(
        '--log-root',
        type=Path,
        default=DEFAULT_LOG_ROOT,
        help='Directory for run logs. Default: .cline-logs/skill-runs.',
    )
    parser.add_argument(
        '--isolated-data-dir',
        action='store_true',
        help=(
            'Use one isolated Cline --data-dir per skill. By default the runner '
            'uses your normal Cline configuration and auth state.'
        ),
    )
    parser.add_argument(
        '--auto-approve',
        choices=('true', 'false'),
        default='true',
        help='Pass-through value for Cline --auto-approve. Default: true.',
    )
    return parser.parse_args()


def resolve_repo_path(path: Path) -> Path:
    """Resolve a path relative to the repository root when needed."""

    if path.is_absolute():
        return path.resolve()
    return (REPO_ROOT / path).resolve()


def selected_roots(args: argparse.Namespace) -> list[Path]:
    """Return validated skill roots selected by arguments."""

    roots = args.root or list(DEFAULT_SKILL_ROOTS)
    resolved = [resolve_repo_path(root) for root in roots]
    missing = [root for root in resolved if not root.exists()]
    if missing:
        raise ValueError(
            'skill root does not exist: ' + ', '.join(path.as_posix() for path in missing)
        )
    non_directories = [root for root in resolved if not root.is_dir()]
    if non_directories:
        raise ValueError(
            'skill root is not a directory: '
            + ', '.join(path.as_posix() for path in non_directories)
        )
    return list(dict.fromkeys(resolved))


def discover_skill_dirs(roots: list[Path]) -> list[Path]:
    """Find skill directories containing SKILL.md under the selected roots."""

    skill_dirs: set[Path] = set()
    for root in roots:
        for skill_file in root.rglob('SKILL.md'):
            skill_dirs.add(skill_file.parent.resolve())
    return sorted(skill_dirs, key=lambda path: path.as_posix())


def filter_skill_dirs(skill_dirs: list[Path], selections: list[str] | None) -> list[Path]:
    """Filter discovered skills by name or repository-relative path."""

    if not selections:
        return skill_dirs

    selected = set(selections)
    filtered: list[Path] = []
    for skill_dir in skill_dirs:
        relative = repo_relative(skill_dir)
        if skill_dir.name in selected or relative in selected:
            filtered.append(skill_dir)
    matched = {skill_dir.name for skill_dir in filtered}
    matched.update(repo_relative(skill_dir) for skill_dir in filtered)
    unmatched = sorted(selected - matched)
    if unmatched:
        raise ValueError('skill selection did not match: ' + ', '.join(unmatched))
    return filtered


def safe_log_name(relative_path: str) -> str:
    """Convert a repository-relative path into a stable log filename stem."""

    return re.sub(r'[^A-Za-z0-9._-]+', '__', relative_path)


def load_prompt_template(path: Path | None) -> str:
    """Load a custom prompt template or return the default prompt."""

    if path is None:
        return DEFAULT_PROMPT_TEMPLATE
    return resolve_repo_path(path).read_text(encoding='utf-8')


def build_prompt(template: str, skill_dir: Path, review_only: bool) -> str:
    """Render the prompt for one skill directory."""

    prompt = template.format(
        skill_path=repo_relative(skill_dir),
        skill_name=skill_dir.name,
        repo_root=REPO_ROOT.as_posix(),
    )
    if review_only:
        prompt += (
            '\n\nReview-only constraint: do not edit files. Report findings, suggested '
            'changes, and validation guidance only.\n'
        )
    return prompt


def build_command(args: argparse.Namespace, task: SkillTask, prompt: str) -> list[str]:
    """Build a Cline CLI command for one skill task."""

    command = [
        args.cline_bin,
        '--json',
        '--cwd',
        REPO_ROOT.as_posix(),
        '--auto-approve',
        args.auto_approve,
        '--thinking',
        args.thinking,
        '--compaction',
        'basic',
    ]
    if args.isolated_data_dir:
        command.extend(['--data-dir', task.data_dir.as_posix()])
    if args.timeout:
        command.extend(['--timeout', str(args.timeout)])
    if args.provider:
        command.extend(['--provider', args.provider])
    if args.model:
        command.extend(['--model', args.model])
    command.append(prompt)
    return command


def write_dry_run(task: SkillTask, command: list[str]) -> None:
    """Write the planned command for a dry-run task."""

    task.log_path.parent.mkdir(parents=True, exist_ok=True)
    task.log_path.write_text(
        'Dry run command:\n' + shlex.join(command) + '\n',
        encoding='utf-8',
    )


def run_task(args: argparse.Namespace, task: SkillTask, prompt_template: str) -> TaskResult:
    """Run one Cline task and write stdout/stderr to its log file."""

    prompt = build_prompt(prompt_template, task.path, args.review_only)
    command = build_command(args, task, prompt)
    task.log_path.parent.mkdir(parents=True, exist_ok=True)
    if args.isolated_data_dir:
        task.data_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        write_dry_run(task, command)
        return TaskResult(task=task, returncode=0, command=command)

    with task.log_path.open('w', encoding='utf-8') as log_file:
        log_file.write(json.dumps({'command': command[:-1] + ['<prompt>']}) + '\n')
        log_file.flush()
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
    return TaskResult(task=task, returncode=completed.returncode, command=command)


def build_tasks(skill_dirs: list[Path], log_root: Path) -> tuple[Path, list[SkillTask]]:
    """Create task metadata and the timestamped run directory."""

    timestamp = dt.datetime.now(dt.UTC).strftime('%Y%m%dT%H%M%SZ')
    run_dir = resolve_repo_path(log_root) / timestamp
    tasks: list[SkillTask] = []
    for skill_dir in skill_dirs:
        relative = repo_relative(skill_dir)
        log_stem = safe_log_name(relative)
        tasks.append(
            SkillTask(
                path=skill_dir,
                relative_path=relative,
                log_path=run_dir / 'logs' / f'{log_stem}.log',
                data_dir=run_dir / 'data' / log_stem,
            )
        )
    return run_dir, tasks


def validate_args(args: argparse.Namespace) -> None:
    """Validate argument combinations before launching tasks."""

    if args.concurrency < 1:
        raise ValueError('--concurrency must be at least 1')
    if args.timeout < 0:
        raise ValueError('--timeout must be 0 or greater')
    if args.skill:
        invalid_names = [
            skill for skill in args.skill if '/' not in skill and not SKILL_NAME_PATTERN.fullmatch(skill)
        ]
        if invalid_names:
            raise ValueError(f'invalid skill name selection: {", ".join(invalid_names)}')


def write_summary(run_dir: Path, results: list[TaskResult]) -> Path:
    """Write a machine-readable and human-readable run summary."""

    summary_path = run_dir / 'summary.json'
    payload = [
        {
            'skill': result.task.relative_path,
            'returncode': result.returncode,
            'log': display_path(result.task.log_path),
        }
        for result in results
    ]
    summary_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return summary_path


def main() -> int:
    """Run Cline tasks for selected skills."""

    args = parse_args()
    try:
        validate_args(args)
        roots = selected_roots(args)
        skill_dirs = filter_skill_dirs(discover_skill_dirs(roots), args.skill)
        if not skill_dirs:
            print('No skill directories matched the selection.', file=sys.stderr)
            return 2

        prompt_template = load_prompt_template(args.prompt_file)
        run_dir, tasks = build_tasks(skill_dirs, args.log_root)
        run_dir.mkdir(parents=True, exist_ok=True)

        print(f'Run directory: {display_path(run_dir)}')
        print(f'Skills: {len(tasks)}')
        print(f'Concurrency: {args.concurrency}')

        results: list[TaskResult] = []
        workers = min(args.concurrency, len(tasks), os.cpu_count() or args.concurrency)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            future_by_task = {
                executor.submit(run_task, args, task, prompt_template): task for task in tasks
            }
            for future in concurrent.futures.as_completed(future_by_task):
                task = future_by_task[future]
                try:
                    result = future.result()
                except Exception as exc:
                    print(f'FAIL {task.relative_path}: {exc}', file=sys.stderr)
                    result = TaskResult(task=task, returncode=1, command=[])
                else:
                    status = 'OK' if result.returncode == 0 else f'FAIL {result.returncode}'
                    print(f'{status} {task.relative_path} -> {display_path(task.log_path)}')
                results.append(result)

        results.sort(key=lambda result: result.task.relative_path)
        summary_path = write_summary(run_dir, results)
        print(f'Summary: {display_path(summary_path)}')
        return 0 if all(result.returncode == 0 for result in results) else 1
    except ValueError as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
