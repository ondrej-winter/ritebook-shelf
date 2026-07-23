# Cline skill workflow

Run a bounded-parallel Cline maintenance workflow for Agent Skills.

By default, the runner recursively discovers every `SKILL.md` below the
repository's `skills/` directory. Logs and a JSON summary are written below
`.cline-logs/skill-runs/`.

## Usage

Run Cline maintenance for all discovered skills:

```sh
make cline-skills
```

This invokes Cline with auto-approval enabled by default and may update skill
files. Preview the generated review-only tasks without invoking Cline:

```sh
make cline-skills-dry-run
```

Run selected skills by directory name or repository-relative path:

```sh
uv run tools/cline-skill-workflow/run_cline_skill_workflow.py \
  --skill author-agent-skill \
  --skill skills/python-software-development/run-python-tests
```

Use `--root` to replace the default `skills/` root. The option may be repeated;
overlapping roots are deduplicated.