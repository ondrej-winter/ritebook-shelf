from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "check_ritebook_state.py"
SPEC = importlib.util.spec_from_file_location("check_ritebook_state", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load checker module from {MODULE_PATH}")
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


class NormalizeIndexTests(unittest.TestCase):
    def test_normalize_index_ignores_only_generated_at(self) -> None:
        first = {
            "schema_version": 1,
            "generated_at": "2026-10-01T08:00:00Z",
            "skills": [{"name": "example", "description": "First"}],
        }
        second = copy.deepcopy(first)
        second["generated_at"] = "2026-10-01T09:00:00Z"

        self.assertEqual(
            checker.normalize_index(first), checker.normalize_index(second)
        )

        second["skills"][0]["description"] = "Changed"
        self.assertNotEqual(
            checker.normalize_index(first),
            checker.normalize_index(second),
        )


class NormalizeLockTests(unittest.TestCase):
    def test_normalize_lock_ignores_only_locked_at(self) -> None:
        first = {
            "schema_version": 1,
            "requirements_file": "ritebook.toml",
            "skills": [
                {
                    "requirement": "catalog/collection/example",
                    "source_revision": "a" * 40,
                    "locked_at": "2026-10-01T08:00:00Z",
                }
            ],
        }
        second = copy.deepcopy(first)
        second["skills"][0]["locked_at"] = "2026-10-01T09:00:00Z"

        self.assertEqual(checker.normalize_lock(first), checker.normalize_lock(second))

        second["skills"][0]["source_revision"] = "b" * 40
        self.assertNotEqual(
            checker.normalize_lock(first), checker.normalize_lock(second)
        )

    def test_normalize_lock_preserves_malformed_entries_for_diagnostics(self) -> None:
        document = {
            "schema_version": 1,
            "requirements_file": "ritebook.toml",
            "skills": ["not-an-object"],
        }

        self.assertEqual(checker.normalize_lock(document)["skills"], ["not-an-object"])


class RequirementResolutionTests(unittest.TestCase):
    def test_resolve_expected_installations_expands_collection_children(self) -> None:
        requirements = {
            "targets": {"agents": ".agents/skills"},
            "skills": [
                {
                    "name": "catalog/agnostic-software-development",
                    "target": "agents",
                }
            ],
        }
        index = {
            "schema_version": 1,
            "index": {"name": "catalog"},
            "skills_root": "skills",
            "skills": [
                {
                    "name": "alpha",
                    "path": "agnostic-software-development/alpha",
                    "skill_file": "agnostic-software-development/alpha/SKILL.md",
                    "description": "Alpha",
                },
                {
                    "name": "beta",
                    "path": "agnostic-software-development/beta",
                    "skill_file": "agnostic-software-development/beta/SKILL.md",
                    "description": "Beta",
                },
                {
                    "name": "other",
                    "path": "another-collection/other",
                    "skill_file": "another-collection/other/SKILL.md",
                    "description": "Other",
                },
            ],
        }

        resolved = checker.resolve_expected_installations(requirements, index)

        self.assertEqual(
            [item.requirement for item in resolved],
            [
                "catalog/agnostic-software-development/alpha",
                "catalog/agnostic-software-development/beta",
            ],
        )
        self.assertEqual(
            [item.target for item in resolved],
            [".agents/skills/alpha", ".agents/skills/beta"],
        )
        self.assertEqual([item.target_ref for item in resolved], ["agents", "agents"])
        self.assertEqual(
            [item.skill_path for item in resolved],
            [
                "skills/agnostic-software-development/alpha",
                "skills/agnostic-software-development/beta",
            ],
        )


class LockValidationTests(unittest.TestCase):
    def test_validate_lock_reports_non_object_entry_without_crashing(self) -> None:
        lock = {
            "schema_version": 1,
            "requirements_file": "ritebook.toml",
            "skills": ["not-an-object"],
        }

        errors = checker.validate_lock_document(
            lock,
            [],
        )

        self.assertIn("lock entry 1 must be an object", errors)

    def test_validate_lock_reports_inconsistent_provenance(self) -> None:
        expected = [
            checker.ExpectedInstallation(
                requirement="catalog/collection/example",
                index_name="catalog",
                skill_name="example",
                target=".agents/skills/example",
                target_ref="agents",
                skill_path="skills/collection/example",
                skill_file="skills/collection/example/SKILL.md",
            )
        ]
        lock = {
            "schema_version": 1,
            "requirements_file": "ritebook.toml",
            "skills": [
                {
                    "requirement": "catalog/collection/example",
                    "index_name": "catalog",
                    "skill_name": "example",
                    "target": ".agents/skills/example",
                    "source": "git@github.com:example/catalog.git",
                    "source_type": "git_url",
                    "source_revision": "a" * 40,
                    "index_digest": "sha256:" + "1" * 64,
                    "index_schema_version": 1,
                    "skill_path": "skills/collection/example",
                    "skill_file": "skills/collection/example/SKILL.md",
                    "locked_at": "2026-10-01T08:00:00Z",
                    "target_ref": "agents",
                },
                {
                    "requirement": "catalog/collection/extra",
                    "index_name": "catalog",
                    "skill_name": "extra",
                    "target": ".agents/skills/extra",
                    "source": "git@github.com:example/catalog.git",
                    "source_type": "git_url",
                    "source_revision": "b" * 40,
                    "index_digest": "sha256:" + "2" * 64,
                    "index_schema_version": 1,
                    "skill_path": "skills/collection/extra",
                    "skill_file": "skills/collection/extra/SKILL.md",
                    "locked_at": "2026-10-01T08:00:00Z",
                    "target_ref": "agents",
                },
            ],
        }

        errors = checker.validate_lock_document(
            lock,
            expected,
        )

        self.assertTrue(any("unexpected lock requirement" in error for error in errors))
        self.assertTrue(any("multiple source revisions" in error for error in errors))
        self.assertTrue(any("multiple index digests" in error for error in errors))

    def test_validate_lock_reports_multiple_git_sources(self) -> None:
        entries = []
        for position, source in enumerate(
            [
                "git@github.com:example/catalog.git",
                "https://github.com/example/catalog.git",
            ],
            start=1,
        ):
            entries.append(
                {
                    "requirement": f"catalog/collection/example-{position}",
                    "index_name": "catalog",
                    "skill_name": f"example-{position}",
                    "target": f".agents/skills/example-{position}",
                    "source": source,
                    "source_type": "git_url",
                    "source_revision": "a" * 40,
                    "index_digest": "sha256:" + "1" * 64,
                    "index_schema_version": 1,
                    "skill_path": f"skills/collection/example-{position}",
                    "skill_file": f"skills/collection/example-{position}/SKILL.md",
                    "locked_at": "2026-10-01T08:00:00Z",
                    "target_ref": "agents",
                }
            )
        lock = {
            "schema_version": 1,
            "requirements_file": "ritebook.toml",
            "skills": entries,
        }

        errors = checker.validate_lock_document(lock, [])

        self.assertTrue(any("multiple Git sources" in error for error in errors))

    def test_validate_provenance_binding_reports_stale_current_index(self) -> None:
        bound_index = b'{"schema_version": 1}\n'
        lock_entries = [
            {
                "source_revision": "a" * 40,
                "index_digest": "sha256:" + hashlib.sha256(bound_index).hexdigest(),
            }
        ]

        errors = checker.validate_provenance_binding(
            lock_entries,
            current_index_bytes=b'{"schema_version": 2}\n',
            bound_index_bytes=bound_index,
            canonical_matches_bound=False,
        )

        self.assertTrue(any("current ritebook-index.json" in error for error in errors))
        self.assertTrue(any("canonical skill bytes" in error for error in errors))


class DirectorySnapshotTests(unittest.TestCase):
    def test_compare_directory_snapshots_reports_target_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            canonical = root / "canonical"
            installed = root / "installed"
            canonical.mkdir()
            installed.mkdir()
            (canonical / "SKILL.md").write_text("canonical\n", encoding="utf-8")
            (installed / "SKILL.md").write_text("changed\n", encoding="utf-8")
            (installed / "unexpected.txt").write_text("extra\n", encoding="utf-8")

            differences = checker.compare_directory_snapshots(
                checker.snapshot_directory(canonical),
                checker.snapshot_directory(installed),
                source_label="canonical",
                target_label="installed",
            )

        rendered = json.dumps(differences)
        self.assertIn("SKILL.md", rendered)
        self.assertIn("unexpected.txt", rendered)


if __name__ == "__main__":
    unittest.main()
