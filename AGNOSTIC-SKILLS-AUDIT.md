# Agnostic Software-Development Skills Audit

Date: 2026-09-19

Last remediation update: 2026-09-22

## Purpose

This report audits the reusable Agent Skills in
`skills/agnostic-software-development/` for structural validity, routing
consistency, workflow compatibility, portability, progressive disclosure,
dependency metadata, supporting-file integrity, and validation readiness.

The intended readers are maintainers of the skill catalog. The report records
evidence, remediation updates, and prioritized follow-up work.

## Scope

The audit covered:

- all 32 canonical `SKILL.md` files in
  `skills/agnostic-software-development/`
- all 32 supporting files under those skill directories, for 64 canonical files
  in total
- the collection catalog in
  `using-agnostic-software-development-skills/SKILL.md`
- metadata dependencies and references between skills
- supporting files under `assets/`, `references/`, and `scripts/`
- installed copies under `.agents/skills/`
- generated catalog coverage in `ritebook-index.json`
- repository validation and maintenance entry points

The initial audit did not modify skill behavior, metadata, generated indexes, or
installed copies. Later remediation updates revise this report as findings are
addressed.

## Method

The review used the repository's `author-agent-skill` guidance as the governing
checklist and examined the collection across these dimensions:

1. Frontmatter, naming, versioning, dependencies, and top-level structure.
2. Catalog coverage and routing consistency.
3. Compatibility between workflows that are commonly composed.
4. Portability across languages, frameworks, tools, and repositories.
5. Supporting-file existence, references, and installed-target parity.
6. Validation commands and reproducibility of the quality gate.
7. Current authoritative sources for mutable or specification-backed claims.

Findings are ranked as:

- **High:** likely to cause unsafe or materially incorrect work.
- **Medium:** likely to route agents incorrectly, create contradictory execution,
  or weaken portability in common use.
- **Low:** maintainability, precision, or validation weakness with a narrower or
  less immediate effect.

## Executive assessment

The collection is structurally healthy and broadly useful. Ritebook accepts all
skill headers, the catalog covers every constituent skill, supporting resources
resolve, and canonical files match their installed copies. No high-severity issue
was found.

The main remaining weakness is the collection boundary rather than individual skill
quality. Two agnostic validation skills contain a Python-specific tool preference
that belongs in the separate Python collection. This issue is fixable without
redesigning the collection.

**Verdict:** pass with follow-up. Address the remaining medium finding before
treating the catalog as fully technology-agnostic.

## Findings

### F-04 — Medium: Python-specific tool policy leaks into the agnostic collection

**Locations**

- `skills/agnostic-software-development/ci-cd-and-automation/SKILL.md`
  lines 66-90
- `skills/agnostic-software-development/run-local-quality-gate/SKILL.md`
  lines 22-42

**Evidence**

Both skills instruct maintainers to prefer `ty` over `mypy` when a Python project
requires a newly selected type checker. This is a prescriptive technology choice,
not merely a portable example. The repository already has a separate
`python-software-development` collection that can own Python tool selection.

Other language-specific examples in the agnostic collection are generally labeled
as examples and do not prescribe repository tooling. These two passages directly
choose between competing Python tools.

**Impact**

The collection is less technology-agnostic than advertised, and its general CI and
quality-gate workflows can override a decision that belongs to a language-specific
catalog or target project.

**Recommendation**

- Keep the agnostic rule at "use the project's configured type or contract
  checker."
- If no tool is configured, require an explicit project or technology-specific
  selection rather than choosing one in the generic workflow.
- Move any `ty` versus `mypy` recommendation to the Python collection and declare
  the applicable Python versions, project constraints, and verification source
  there.

### F-09 — Low: Skill validation is not a first-class reproducible repository gate

**Locations**

- `Makefile`
- repository root validation configuration

**Evidence**

Ritebook provides a working header validator, and both collection-only and
full-repository runs passed. The Makefile does not expose that validator as a
dedicated target. It also defaults to `uvx ritebook@latest`, so validation behavior
can change when a new Ritebook version is released.

The repository has no single documented check covering header lint, generated
index coverage, relative supporting-file links, and canonical-to-installed drift.

**Impact**

Contributors must discover validation commands independently, and identical source
changes can be checked by different Ritebook versions at different times.

**Recommendation**

- Add a `lint-skills` or equivalent target.
- Pin the Ritebook version used by automated validation.
- Add checks for canonical skill lint, index coverage, supporting-file links, and
  installed-target drift.
- Run the aggregate gate in CI if this repository is published from CI.

## Positive findings

- Ritebook validated all 32 skills in the agnostic collection.
- Ritebook validated all 47 canonical skills under `skills/`.
- All 64 canonical collection files have byte-identical installed counterparts
  under `.agents/skills/`.
- `ritebook-index.json` includes every one of the 32 canonical agnostic skills and
  contains no unexpected skill for that collection.
- Every supporting file under `assets/`, `references/`, and `scripts/` is mentioned
  by its owning `SKILL.md`.
- No broken supporting-file path was found. Links such as
  `./<NNNN>-<slug>.md` in `write-adr` are intentional template placeholders rather
  than repository links.
- Skill names match their directory names and use valid kebab-case.
- Required descriptions, semantic versions, dependency sections, and top-level
  headings are present and accepted by Ritebook.
- No metadata dependency names point to missing skills.
- The catalog declares all 31 other skills as optional dependencies and mentions
  every constituent skill in its body.
- Capability dependencies use the canonical `shell-execution`, `version-control`,
  `browser-runtime`, `source-retrieval`, and `independent-review` vocabulary.
- Required capabilities stop activation when unavailable; optional capabilities
  are reserved for conditional use or documented degraded fallbacks.
- Every agnostic skill dependency is classified as `route`, `handoff`,
  `verification`, or `awareness`, and optional dependencies are explicitly
  non-recursive unless their own trigger or an explicit handoff is present.
- Security, performance, and accessibility references are tailored to review,
  implementation, or release audiences rather than being accidental duplicate
  files.
- `idea-refine/scripts/idea-refine.sh` passes shell syntax validation.
- The Conventional Commits skill is consistent with the pinned official 1.0.0
  specification for message shape, `feat`, `fix`, scope, `!`, footer syntax,
  breaking-change tokens, and case handling.

## Recommended remediation order

1. **Restore the collection boundary.** Move the Python tool preference described
   in F-04 to the Python collection.
2. **Strengthen maintenance controls.** Add the validation target from F-09.

Each behavioral skill change should increment that skill's semantic version and
be synchronized through the repository's normal Ritebook workflow rather than by
editing `.agents/skills/` directly.

## Validation evidence

The following checks were run during the audit:

```text
uvx ritebook@latest skills lint --root skills/agnostic-software-development
Validated 32 skill(s)

uvx ritebook@latest skills lint --root skills
Validated 47 skill(s)
```

Additional read-only checks confirmed:

- 32 canonical agnostic `SKILL.md` files
- 64 total canonical files in the collection
- no missing or changed installed counterpart among those 64 files
- no missing or extra agnostic skill in `ritebook-index.json`
- no unmentioned supporting file
- no broken supporting-file reference
- valid shell syntax for `idea-refine/scripts/idea-refine.sh`

The F-01 remediation on 2026-09-22 additionally confirmed:

- `using-agnostic-software-development-skills` version 2.5.0 routes
  `spec-driven-development` only when requirements need clarification,
  consolidation, or durable agreement, and explicitly bypasses a separate spec for
  precise fixes or small edits with clear acceptance criteria
- the numbered universal lifecycle was replaced with a conditional composition
  graph whose routed skills retain authority over their narrower activation rules
- `test-driven-development` is applied inside each behavior change that automated tests can verify
  before implementation rather than after `incremental-implementation`
- minimal behavior changes can invoke TDD directly without forcing the incremental
  workflow outside its own activation rules
- canonical and installed catalog skill files remain byte-identical

The F-03 remediation on 2026-09-22 additionally confirmed:

- every declared agnostic capability uses the documented five-name vocabulary
- `source-driven-development` requires `source-retrieval`
- `doubt-driven-development` declares optional `independent-review` and its
  degraded fallback
- every non-empty agnostic skill dependency has a valid relationship
- all catalog dependencies use `relationship: route`

The F-06 remediation on 2026-09-22 additionally confirmed:

- `performance-optimization` version 1.4.1 qualifies the embedded Core Web Vitals
  thresholds with the 75th-percentile assessment and mobile/desktop segmentation
- the focused web-performance reference links the official Web Vitals guidance,
  records both the verification date and source-page update date, and requires
  reverification before the thresholds are presented as current policy
- the current official thresholds remain LCP at 2.5/4.0 seconds, INP at 200/500
  milliseconds, and CLS at 0.1/0.25 for good/poor boundaries
- canonical and installed `performance-optimization` files remain byte-identical

The F-07 remediation on 2026-09-22 additionally confirmed:

- `shipping-and-launch` version 1.6.0 makes runtime release controls conditional
  on release risk, safe isolation, and net operational value
- rollout and recovery examples use project-derived placeholders instead of fixed
  numeric defaults
- recovery guidance allows rollback, disablement, roll-forward, compensation, or
  documented irreversibility with explicit risk acceptance and containment
- canonical and installed `shipping-and-launch` files remain byte-identical

## Limitations

- Ritebook lint validates headers and metadata shape; it does not establish
  workflow coherence or metadata completeness.
- The audit did not execute every skill against a representative project. Findings
  about orchestration are based on the written contracts and their composition.
- External source verification was limited to mutable or specification-backed
  claims identified during review, specifically Core Web Vitals and Conventional
  Commits v1.0.0.
- Installed-target parity was checked against the current repository state; the
  audit did not test a fresh remote install into a separate repository.
