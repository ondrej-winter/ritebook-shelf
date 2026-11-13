---
name: using-python-software-development-skills
description: Discover and invoke Python software development skills. Use when starting Python work or deciding which Python-specific implementation, validation, testing, or documentation skill applies.
metadata:
  version: "3.0.1"
  last-verified: "2026-11-13T17:53:04+00:00"
---

# Using Python Software Development Skills

Use this collection catalog when starting Python software development work or
when you need to discover Python-specific skills. It complements
`using-agnostic-software-development-skills`, which routes technology-independent
engineering workflows.

## Steps

1. Load this skill at session start when working on a Python project.
2. Use `using-agnostic-software-development-skills` alongside this skill for
   shared workflow routing.
3. Check the Python routing guide below before choosing implementation,
   validation, or documentation skills.
4. Prefer the most specific matching skill. Use shared skills for general
   workflow guidance and this collection for Python mechanics.
5. Confirm the selected skill is available and read its execution requirements.
   If unavailable, report the missing capability and continue only independent
   work supported by the request and available instructions; do not invent the
   missing procedure or count skipped execution as complete.

Routes select workflows whose own triggers match; they do not activate every
listed skill. Preserve the request's edit/review scope and pass canonical paths,
settled port contracts, unresolved decisions, and validation evidence through
feature-to-port-to-adapter handoffs. A complete feature needs integration evidence
beyond the completion of its individual port and adapter procedures.

Use this Python routing guide:

```text
Python task arrives
- Starting a new Python application: bootstrap-python-app
- Adding an end-to-end hexagonal feature: add-hexagonal-feature
- Adding an application boundary: python-add-port
- Adding infrastructure, HTTP, CLI, event, or persistence integration: python-add-adapter
- Building or refactoring an extensible multi-feature product CLI: python-build-extensible-cli
- Adding environment-backed configuration: python-add-env-settings-adapter
- Splitting a growing Python module or package: split-python-module
- Writing or refactoring Python tests: write-pytest-tests
- Adding Python docstrings or useful comments: write-python-docstrings
```

## Skill selection notes

- Use `add-hexagonal-feature` when the change spans domain, application,
  adapters, and tests for one feature slice.
- Use `python-add-port` before `python-add-adapter` when the application-layer
  boundary does not already exist.
- Use `python-build-extensible-cli` when a shared product CLI shell needs
  multiple feature-owned command contributions; use `python-add-adapter` for an
  individual CLI adapter.
- Use `python-add-env-settings-adapter` for configuration sourced from
  environment variables, `.env` files, or runtime settings objects.
- Use `write-pytest-tests` for test design and structure.

## Project validation

Read the target project's `AGENTS.md` and executable task definitions for its
formatting, linting, type-checking, test, and complete quality-gate commands.
Run focused checks during development and the required project gate before
handoff. Keep command details in those project-owned sources rather than loading
separate skills to invoke tools. Preserve the configured tools, targets, and
options; report unavailable checks without claiming they passed.
If a required command or tool is undefined, report the gap rather than selecting
or installing tooling as part of validation.
