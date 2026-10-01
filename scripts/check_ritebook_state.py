"""Verify Ritebook source, index, installed targets, and lock provenance."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any

GIT_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
INDEX_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


@dataclass(frozen=True)
class ExpectedInstallation:
    """One installation resolved from ritebook.toml and ritebook-index.json."""

    requirement: str
    index_name: str
    skill_name: str
    target: str
    target_ref: str | None
    skill_path: str
    skill_file: str


def normalize_index(document: dict[str, Any]) -> dict[str, Any]:
    """Return the semantic publisher document without its generation timestamp."""
    normalized = copy.deepcopy(document)
    normalized.pop("generated_at", None)
    return normalized


def normalize_lock(document: dict[str, Any]) -> dict[str, Any]:
    """Return lock semantics while ignoring per-run lock timestamps."""
    normalized = copy.deepcopy(document)
    skills = normalized.get("skills", [])
    if not isinstance(skills, list):
        return normalized
    for entry in skills:
        if isinstance(entry, dict):
            entry.pop("locked_at", None)
    normalized["skills"] = sorted(
        skills,
        key=_lock_sort_key,
    )
    return normalized


def fingerprint(value: Any) -> str:
    """Return a stable SHA-256 fingerprint for a JSON-compatible value."""
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def resolve_expected_installations(
    requirements: dict[str, Any],
    index: dict[str, Any],
) -> list[ExpectedInstallation]:
    """Resolve exact skills and immediate collection children from requirements."""
    targets = requirements.get("targets", {})
    index_skills = index.get("skills", [])
    skills_by_path = {skill["path"]: skill for skill in index_skills}
    skills_root = PurePosixPath(index["skills_root"])
    resolved: list[ExpectedInstallation] = []

    for requirement in requirements.get("skills", []):
        reference = requirement["name"]
        if "/" not in reference:
            raise ValueError(f"unqualified Ritebook requirement: {reference}")
        index_name, selector = reference.split("/", maxsplit=1)
        exact = skills_by_path.get(selector)
        if exact is not None:
            selected = [exact]
            expands_collection = False
        else:
            prefix = f"{selector}/"
            selected = sorted(
                (
                    skill
                    for skill in index_skills
                    if skill["path"].startswith(prefix)
                    and "/" not in skill["path"][len(prefix) :]
                ),
                key=lambda skill: skill["path"],
            )
            expands_collection = True
        if not selected:
            raise ValueError(f"unknown Ritebook skill or collection: {reference}")

        target_ref = requirement.get("target")
        target_path = requirement.get("target_path")
        if (target_ref is None) == (target_path is None):
            raise ValueError(
                f"requirement must define exactly one target or target_path: {reference}"
            )
        if target_ref is not None:
            if target_ref not in targets:
                raise ValueError(
                    f"undefined Ritebook target {target_ref!r}: {reference}"
                )
            target_base = PurePosixPath(targets[target_ref])
        else:
            target_base = PurePosixPath(target_path)

        for skill in selected:
            skill_name = skill["name"]
            if target_ref is not None or expands_collection:
                install_target = target_base / skill_name
            else:
                install_target = target_base
            resolved.append(
                ExpectedInstallation(
                    requirement=f"{index_name}/{skill['path']}",
                    index_name=index_name,
                    skill_name=skill_name,
                    target=str(install_target),
                    target_ref=target_ref,
                    skill_path=str(skills_root / skill["path"]),
                    skill_file=str(skills_root / skill["skill_file"]),
                )
            )

    duplicate_targets = _duplicates(item.target for item in resolved)
    if duplicate_targets:
        raise ValueError(
            "duplicate resolved Ritebook targets: " + ", ".join(duplicate_targets)
        )
    duplicate_requirements = _duplicates(item.requirement for item in resolved)
    if duplicate_requirements:
        raise ValueError(
            "duplicate resolved Ritebook requirements: "
            + ", ".join(duplicate_requirements)
        )
    return sorted(resolved, key=lambda item: (item.index_name, item.skill_path))


def validate_lock_document(
    lock: dict[str, Any],
    expected: list[ExpectedInstallation],
    *,
    requirements_file: str = "ritebook.toml",
) -> list[str]:
    """Validate complete lock coverage and internally consistent provenance."""
    errors: list[str] = []
    if lock.get("schema_version") != 1:
        errors.append("ritebook.lock schema_version must be 1")
    if lock.get("requirements_file") != requirements_file:
        errors.append(
            "ritebook.lock requirements_file does not match " + requirements_file
        )
    entries = lock.get("skills")
    if not isinstance(entries, list):
        return [*errors, "ritebook.lock skills must be a list"]

    entries_by_requirement: dict[str, dict[str, Any]] = {}
    valid_entries: list[dict[str, Any]] = []
    for position, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"lock entry {position} must be an object")
            continue
        valid_entries.append(entry)
        requirement = entry.get("requirement")
        if requirement in entries_by_requirement:
            errors.append(f"duplicate lock requirement: {requirement}")
        elif isinstance(requirement, str):
            entries_by_requirement[requirement] = entry
        else:
            errors.append("lock entry has a missing or invalid requirement")

    expected_by_requirement = {item.requirement: item for item in expected}
    for requirement in sorted(entries_by_requirement.keys() - expected_by_requirement):
        errors.append(f"unexpected lock requirement: {requirement}")
    for requirement in sorted(expected_by_requirement.keys() - entries_by_requirement):
        errors.append(f"missing lock requirement: {requirement}")

    for requirement in sorted(expected_by_requirement.keys() & entries_by_requirement):
        item = expected_by_requirement[requirement]
        entry = entries_by_requirement[requirement]
        expected_fields: dict[str, Any] = {
            "index_name": item.index_name,
            "skill_name": item.skill_name,
            "target": item.target,
            "skill_path": item.skill_path,
            "skill_file": item.skill_file,
            "index_schema_version": 1,
            "source_type": "git_url",
        }
        if item.target_ref is not None:
            expected_fields["target_ref"] = item.target_ref
        for field, expected_value in expected_fields.items():
            if entry.get(field) != expected_value:
                errors.append(
                    f"{requirement}: {field} is {entry.get(field)!r}; "
                    f"expected {expected_value!r}"
                )
        if item.target_ref is None and entry.get("target_ref") is not None:
            errors.append(f"{requirement}: unexpected target_ref")
        source = entry.get("source")
        if not isinstance(source, str) or not source:
            errors.append(f"{requirement}: invalid Git source")
        revision = entry.get("source_revision", "")
        if not isinstance(revision, str) or not GIT_OBJECT_ID.fullmatch(revision):
            errors.append(f"{requirement}: invalid full Git source_revision")
        digest = entry.get("index_digest", "")
        if not isinstance(digest, str) or not INDEX_DIGEST.fullmatch(digest):
            errors.append(f"{requirement}: invalid index_digest")
        if not _is_timestamp(entry.get("locked_at")):
            errors.append(f"{requirement}: invalid locked_at timestamp")

    revisions = {entry.get("source_revision") for entry in valid_entries}
    digests = {entry.get("index_digest") for entry in valid_entries}
    timestamps = {entry.get("locked_at") for entry in valid_entries}
    sources = {entry.get("source") for entry in valid_entries}
    if len(revisions) > 1:
        errors.append("ritebook.lock contains multiple source revisions")
    if len(digests) > 1:
        errors.append("ritebook.lock contains multiple index digests")
    if len(timestamps) > 1:
        errors.append("ritebook.lock contains multiple locked_at timestamps")
    if len(sources) > 1:
        errors.append("ritebook.lock contains multiple Git sources")
    return errors


def validate_provenance_binding(
    lock_entries: list[dict[str, Any]],
    *,
    current_index_bytes: bytes,
    bound_index_bytes: bytes,
    canonical_matches_bound: bool,
) -> list[str]:
    """Validate the exact index digest and current source binding."""
    if not lock_entries:
        return ["ritebook.lock has no skill entries"]
    errors: list[str] = []
    expected_digest = lock_entries[0].get("index_digest")
    actual_digest = "sha256:" + hashlib.sha256(bound_index_bytes).hexdigest()
    if expected_digest != actual_digest:
        errors.append(
            "lock index_digest does not match ritebook-index.json at source_revision"
        )
    if current_index_bytes != bound_index_bytes:
        errors.append(
            "current ritebook-index.json differs from the lock-bound source revision"
        )
    if not canonical_matches_bound:
        errors.append(
            "current canonical skill bytes differ from the lock-bound source revision"
        )
    return errors


def snapshot_directory(path: Path) -> dict[str, dict[str, Any]]:
    """Snapshot regular files and symlinks below a directory."""
    if not path.is_dir():
        raise FileNotFoundError(path)
    snapshot: dict[str, dict[str, Any]] = {}
    for candidate in sorted(path.rglob("*")):
        relative = candidate.relative_to(path).as_posix()
        if candidate.is_symlink():
            snapshot[relative] = {"kind": "symlink", "target": os.readlink(candidate)}
        elif candidate.is_file():
            mode = candidate.stat().st_mode
            snapshot[relative] = {
                "kind": "file",
                "sha256": hashlib.sha256(candidate.read_bytes()).hexdigest(),
                "executable": bool(mode & stat.S_IXUSR),
            }
    return snapshot


def compare_directory_snapshots(
    source: dict[str, dict[str, Any]],
    target: dict[str, dict[str, Any]],
    *,
    source_label: str,
    target_label: str,
) -> list[str]:
    """Describe file-set, content, symlink, and executable-bit differences."""
    differences: list[str] = []
    for relative in sorted(source.keys() - target.keys()):
        differences.append(
            f"{relative}: present in {source_label}, missing from {target_label}"
        )
    for relative in sorted(target.keys() - source.keys()):
        differences.append(f"{relative}: unexpected in {target_label}")
    for relative in sorted(source.keys() & target.keys()):
        if source[relative] != target[relative]:
            differences.append(
                f"{relative}: differs between {source_label} and {target_label}"
            )
    return differences


def git_snapshot(
    repo: Path, revision: str, tree_path: str
) -> dict[str, dict[str, Any]]:
    """Snapshot one tracked directory exactly as stored at a Git revision."""
    output = _run_git_bytes(
        repo,
        ["ls-tree", "-r", "-z", revision, "--", tree_path],
    )
    prefix = tree_path.rstrip("/") + "/"
    snapshot: dict[str, dict[str, Any]] = {}
    for raw_entry in output.split(b"\0"):
        if not raw_entry:
            continue
        metadata, raw_path = raw_entry.split(b"\t", maxsplit=1)
        mode, object_type, _object_id = metadata.decode().split()
        path = raw_path.decode()
        if object_type != "blob" or not path.startswith(prefix):
            continue
        relative = path[len(prefix) :]
        content = _run_git_bytes(repo, ["show", f"{revision}:{path}"])
        if mode == "120000":
            snapshot[relative] = {"kind": "symlink", "target": content.decode()}
        else:
            snapshot[relative] = {
                "kind": "file",
                "sha256": hashlib.sha256(content).hexdigest(),
                "executable": mode == "100755",
            }
    return snapshot


def run_check(
    repo: Path,
    *,
    ritebook_command: str,
) -> dict[str, Any]:
    """Run all read-only consistency checks and return a structured result."""
    errors: list[str] = []
    try:
        requirements = tomllib.loads(
            (repo / "ritebook.toml").read_text(encoding="utf-8")
        )
        index = _load_json(repo / "ritebook-index.json")
        lock = _load_json(repo / "ritebook.lock")
        expected = resolve_expected_installations(requirements, index)
    except (KeyError, OSError, TypeError, ValueError) as error:
        return {"ok": False, "errors": [str(error)]}

    generated_index, publish_error = _generate_index(repo, ritebook_command)
    if publish_error is not None:
        errors.append(publish_error)
    elif normalize_index(generated_index) != normalize_index(index):
        errors.append(
            "ritebook-index.json has semantic drift from the canonical skills tree"
        )

    errors.extend(validate_lock_document(lock, expected))
    raw_entries = lock.get("skills", [])
    entries = (
        [entry for entry in raw_entries if isinstance(entry, dict)]
        if isinstance(raw_entries, list)
        else []
    )
    revisions = {entry.get("source_revision") for entry in entries}
    revision = next(iter(revisions)) if len(revisions) == 1 else None
    bound_index_bytes = b""
    canonical_matches_bound = False
    if isinstance(revision, str) and GIT_OBJECT_ID.fullmatch(revision):
        if _git_result(repo, ["cat-file", "-e", f"{revision}^{{commit}}"]).returncode:
            errors.append(f"lock source_revision is unavailable locally: {revision}")
        else:
            if _git_result(
                repo, ["merge-base", "--is-ancestor", revision, "HEAD"]
            ).returncode:
                errors.append(
                    f"lock source_revision is not an ancestor of HEAD: {revision}"
                )
            try:
                bound_index_bytes = _run_git_bytes(
                    repo, ["show", f"{revision}:ritebook-index.json"]
                )
            except RuntimeError as error:
                errors.append(str(error))
            canonical_matches_bound = True
            for item in expected:
                current_path = repo / item.skill_path
                try:
                    current_snapshot = snapshot_directory(current_path)
                    bound_snapshot = git_snapshot(repo, revision, item.skill_path)
                except (FileNotFoundError, RuntimeError) as error:
                    errors.append(f"{item.requirement}: {error}")
                    canonical_matches_bound = False
                    continue
                differences = compare_directory_snapshots(
                    bound_snapshot,
                    current_snapshot,
                    source_label=f"Git {revision}",
                    target_label="current canonical source",
                )
                if differences:
                    canonical_matches_bound = False
                    errors.extend(
                        f"{item.requirement}: {difference}"
                        for difference in differences
                    )
            if bound_index_bytes:
                errors.extend(
                    validate_provenance_binding(
                        entries,
                        current_index_bytes=(repo / "ritebook-index.json").read_bytes(),
                        bound_index_bytes=bound_index_bytes,
                        canonical_matches_bound=canonical_matches_bound,
                    )
                )

    installed_state: dict[str, Any] = {}
    for item in expected:
        canonical_path = repo / item.skill_path
        target_path = repo / item.target
        try:
            canonical_snapshot = snapshot_directory(canonical_path)
            target_snapshot = snapshot_directory(target_path)
        except FileNotFoundError as error:
            errors.append(f"{item.requirement}: missing directory {error.filename}")
            continue
        differences = compare_directory_snapshots(
            canonical_snapshot,
            target_snapshot,
            source_label="canonical source",
            target_label="installed target",
        )
        errors.extend(f"{item.requirement}: {difference}" for difference in differences)
        installed_state[item.requirement] = target_snapshot

    current_index_bytes = (repo / "ritebook-index.json").read_bytes()
    return {
        "ok": not errors,
        "errors": errors,
        "resolved_installations": len(expected),
        "source_revision": revision,
        "index_digest": "sha256:" + hashlib.sha256(current_index_bytes).hexdigest(),
        "normalized_index_fingerprint": fingerprint(normalize_index(index)),
        "normalized_lock_fingerprint": fingerprint(normalize_lock(lock)),
        "installed_tree_fingerprint": fingerprint(installed_state),
    }


def main(argv: list[str] | None = None) -> int:
    """Run the consistency gate."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--ritebook-command",
        default="uvx ritebook@0.1.48",
        help="Command prefix used to regenerate the index in a temporary directory.",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args(argv)
    result = run_check(args.root.resolve(), ritebook_command=args.ritebook_command)
    if args.json_output:
        print(json.dumps(result, indent=2, sort_keys=True))
    elif result["ok"]:
        print(
            "Ritebook state is consistent: "
            f"{result['resolved_installations']} installation(s), "
            f"revision {result['source_revision']}, {result['index_digest']}"
        )
    else:
        print("Ritebook state is inconsistent:", file=sys.stderr)
        for error in result["errors"]:
            print(f"- {error}", file=sys.stderr)
    return 0 if result["ok"] else 1


def _generate_index(
    repo: Path,
    ritebook_command: str,
) -> tuple[dict[str, Any], str | None]:
    with tempfile.TemporaryDirectory(prefix="ritebook-state-") as temp_dir:
        root = Path(temp_dir)
        shutil.copytree(repo / "skills", root / "skills", symlinks=True)
        command = [
            *shlex.split(ritebook_command),
            "indexes",
            "publish",
            "--skills-root",
            "skills",
            "--name",
            _load_json(repo / "ritebook-index.json")["index"]["name"],
        ]
        completed = subprocess.run(
            command,
            cwd=root,
            capture_output=True,
            check=False,
            text=True,
        )
        if completed.returncode:
            detail = completed.stderr.strip() or completed.stdout.strip()
            return {}, f"temporary Ritebook publication failed: {detail}"
        return _load_json(root / "ritebook-index.json"), None


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise TypeError(f"expected a JSON object: {path}")
    return value


def _is_timestamp(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def _lock_sort_key(entry: Any) -> tuple[str, str, str]:
    if not isinstance(entry, dict):
        return ("", "", json.dumps(entry, sort_keys=True))
    return (
        str(entry.get("index_name", "")),
        str(entry.get("skill_path", "")),
        str(entry.get("target", "")),
    )


def _duplicates(values: Any) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)


def _git_result(repo: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *arguments],
        cwd=repo,
        capture_output=True,
        check=False,
    )


def _run_git_bytes(repo: Path, arguments: list[str]) -> bytes:
    completed = _git_result(repo, arguments)
    if completed.returncode:
        detail = completed.stderr.decode(errors="replace").strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed: {detail}")
    return completed.stdout


def _run_git_text(repo: Path, arguments: list[str]) -> str:
    return _run_git_bytes(repo, arguments).decode()


if __name__ == "__main__":
    raise SystemExit(main())
