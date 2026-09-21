# Agnostic Software-Development Skills Audit

Date: 2026-09-19

## Purpose

This report audits the reusable Agent Skills in
`skills/agnostic-software-development/` for structural validity, routing
consistency, workflow compatibility, portability, progressive disclosure,
dependency metadata, supporting-file integrity, and validation readiness.

The intended readers are maintainers of the skill catalog. The report records
evidence and prioritized follow-up work without changing the audited skills.

## Scope

The audit covered:

- all 32 canonical `SKILL.md` files in
  `skills/agnostic-software-development/`
- all 25 supporting files under those skill directories, for 57 canonical files
  in total
- the collection catalog in
  `using-agnostic-software-development-skills/SKILL.md`
- metadata dependencies and references between skills
- supporting files under `assets/`, `references/`, and `scripts/`
- installed copies under `.agents/skills/`
- generated catalog coverage in `ritebook-index.json`
- repository validation and maintenance entry points

The audit did not modify skill behavior, metadata, generated indexes, or installed
copies.

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

The main weakness is cross-skill coherence rather than individual skill quality.
The catalog and implementation workflows sometimes describe incompatible order of
operations, capability dependencies are not modeled consistently enough to support
availability checks, and two agnostic validation skills contain a Python-specific
tool preference. These issues are fixable without redesigning the collection.

**Verdict:** pass with follow-up. Address the medium findings before treating the
catalog as a fully coherent orchestration contract.

## Findings

### F-01 — Medium: Catalog routing conflicts with the workflows it routes

**Locations**

- `skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md`
  lines 128-162 and 251-281
- `skills/agnostic-software-development/spec-driven-development/SKILL.md`
  lines 25-39
- `skills/agnostic-software-development/test-driven-development/SKILL.md`
  lines 16-58

**Evidence**

The catalog routes every "new project, feature, or change" to
`spec-driven-development` and says to start with a spec whenever a non-trivial task
has none. The specification skill is more selective: it says a precise fix or
small edit with clear acceptance criteria should work directly from the request.

The catalog's typical lifecycle also places `incremental-implementation` before
`test-driven-development`. The TDD skill requires a failing test before the code
that makes it pass. Read as an ordered sequence, the catalog therefore tells an
agent to start implementation before applying the test-first workflow.

The catalog correctly notes that not every task needs every skill, but the primary
routing tree and numbered lifecycle remain more absolute than the routed skills.

**Impact**

Agents following the catalog literally can create unnecessary specifications or
implement behavior before writing the failing test required by the selected TDD
workflow.

**Recommendation**

- Qualify the specification route to exclude small changes with clear acceptance
  criteria.
- Describe TDD as an execution discipline applied inside implementation slices,
  not as a later lifecycle phase.
- Replace the numbered universal lifecycle with a conditional graph or label it
  explicitly as one possible composition.
- Keep each routed skill's activation rules authoritative when they are narrower
  than the catalog summary.

### F-03 — Medium: Capability metadata does not consistently expose required capabilities

**Locations**

- `skills/agnostic-software-development/source-driven-development/SKILL.md`
- `skills/agnostic-software-development/doubt-driven-development/SKILL.md`
- `skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md`
- dependency metadata throughout the collection

**Evidence**

The catalog instructs agents to confirm that selected skills are available before
using them. The metadata cannot consistently support that check:

- `source-driven-development` declares no tools even though its workflow may need
  access to official web documentation, local dependency source, command help, or
  another authoritative source.
- `doubt-driven-development` declares no capability for the fresh-context or
  independent review that defines its preferred workflow. It documents a degraded
  self-review fallback, but the metadata does not expose when degradation is
  necessary.
- Similar capabilities use different levels of abstraction, including `shell`,
  `sh`, `web access`, and `browser runtime`.
- Optional skill dependencies can mean routing, escalation, awareness, or an
  executable handoff; metadata does not distinguish those relationships.

Ritebook validates the metadata's shape, but shape validity does not prove that the
declared capabilities are complete or semantically consistent.

**Impact**

An orchestrator cannot reliably determine whether a skill can run as written,
whether it must use a degraded fallback, or whether a referenced skill should be
activated automatically.

**Recommendation**

- Define and document a small capability vocabulary for shell execution, version
  control, browser runtime, source retrieval, and independent review.
- Declare optional capabilities when a documented fallback exists and required
  capabilities when the stated outcome cannot otherwise be produced.
- Define dependency relationship semantics, such as `route`, `handoff`,
  `verification`, or `awareness`, if the skill format permits it.
- State explicitly that optional related skills are not recursively activated
  unless their trigger is present.

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

### F-05 — Medium: Deprecation requires proof of zero active usage before removal

**Location**

- `skills/agnostic-software-development/deprecation-and-migration/SKILL.md`
  lines 149-172

**Evidence**

The workflow says to remove an old path only after zero active usage and treats
removal before metrics, logs, or dependency checks show zero usage as a red flag.
Zero usage can be demonstrated for fully controlled and observable consumers, but
not always for public APIs, offline clients, externally owned integrations,
distributed installations, or systems without complete telemetry.

The same skill supports compulsory deprecation with deadlines and exception
processes, but its removal gate does not provide an evidence-based alternative
when complete usage measurement is impossible.

**Impact**

Legitimate removals can become impossible to complete, or maintainers may claim
stronger usage evidence than they actually possess.

**Recommendation**

- Require zero measured usage when the consumer population is controlled and
  measurement is sufficiently complete.
- Otherwise allow removal after a documented support window, migration notice,
  replacement readiness, owner approval, and explicit residual-risk acceptance.
- Distinguish `proven zero usage`, `no known active consumers`, and `remaining
  usage cannot be observed` in the removal decision.

### F-06 — Low: Mutable Core Web Vitals data lacks source context

**Location**

- `skills/agnostic-software-development/performance-optimization/SKILL.md`
  lines 275-286

**Evidence**

The embedded LCP, INP, and CLS thresholds matched the official Web Vitals guidance
checked on 2026-09-19. The official guidance evaluates Core Web Vitals at the 75th
percentile of page loads, segmented by mobile and desktop. The skill includes the
threshold values but omits that assessment context and does not link or date the
mutable external guidance.

Authoritative source:

- [Web Vitals](https://web.dev/articles/vitals), last updated 2024-10-31 when
  checked for this audit

**Impact**

Maintainers can apply correct numbers with incomplete semantics, and future metric
changes may leave the embedded table stale.

**Recommendation**

- Add the percentile and device-segmentation qualification.
- Link the authoritative reference and record a verification date.
- Consider moving mutable thresholds to a focused reference file that instructs
  agents to reverify them before making current-policy claims.

The separate Conventional Commits v1.0.0 guidance was checked against the official
specification and no substantive mismatch was found:

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

### F-07 — Low: Launch examples contain unqualified universal rules and numeric defaults

**Location**

- `skills/agnostic-software-development/shipping-and-launch/SKILL.md`
  lines 22-58 and 243-306

**Evidence**

The skill correctly requires a recovery strategy and allows rollback,
disablement, roll-forward, or compensation. Its example then supplies fixed
triggers and recovery-time targets, including twice-baseline error rate and
one-, five-, and fifteen-minute recovery targets, without labeling them as purely
illustrative project-specific values.

The rationalization table also says every feature benefits from a kill switch.
Feature flags and disablement are valuable when they reduce risk, but they also add
state, branching, cleanup, and operational complexity. Static, very small,
irreversible, or already compartmentalized changes may need another recovery
strategy instead.

**Impact**

Agents can copy arbitrary operational targets or add feature flags mechanically
rather than deriving controls from release risk and system capabilities.

**Recommendation**

- Replace example numbers with placeholders or label them prominently as examples
  that must be replaced.
- Make feature flags and kill switches risk-based rather than universal.
- Preserve the requirement for an explicit recovery strategy while allowing the
  project to choose rollback, roll-forward, compensation, disablement, or
  documented irreversibility.

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

### F-10 — Low: Progressive disclosure can be improved in the longest skills

**Locations**

- `skills/agnostic-software-development/code-review-and-quality/SKILL.md`
- `skills/agnostic-software-development/interview-me/SKILL.md`
- `skills/agnostic-software-development/performance-optimization/SKILL.md`
- `skills/agnostic-software-development/shipping-and-launch/SKILL.md`
- `skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md`

**Evidence**

Five main skill files exceed 300 lines. The collection catalog carries routing,
global behavioral policy, failure modes, lifecycle guidance, and a full reference
table in one always-loaded file. Several long skills already use supporting
references successfully, showing that the collection supports progressive
disclosure.

Length alone is not a defect, and some workflows need substantial context. The
maintenance concern is repeated or secondary material in the main activation
surface rather than a numeric line limit.

**Impact**

Long always-loaded skills consume more context and increase the chance that routing
summaries, detailed workflows, tables, and examples drift independently.

**Recommendation**

- Keep activation rules, the core workflow, red flags, and completion criteria in
  `SKILL.md`.
- Move long examples, domain-specific tables, and secondary checklists into
  referenced files when the main workflow remains self-contained.
- Start with the collection catalog because it combines the most distinct
  responsibilities.
- Do not split content mechanically or create supporting files that agents must
  always load to understand the basic workflow.

## Positive findings

- Ritebook validated all 32 skills in the agnostic collection.
- Ritebook validated all 47 canonical skills under `skills/`.
- All 57 canonical collection files have byte-identical installed counterparts
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
- Security, performance, and accessibility references are tailored to review,
  implementation, or release audiences rather than being accidental duplicate
  files.
- `idea-refine/scripts/idea-refine.sh` passes shell syntax validation.
- The Conventional Commits skill is consistent with the pinned official 1.0.0
  specification for message shape, `feat`, `fix`, scope, `!`, footer syntax,
  breaking-change tokens, and case handling.

## Recommended remediation order

1. **Reconcile catalog orchestration order.** Resolve F-01 so the catalog routes
   specification, incremental implementation, and TDD workflows through one
   compatible execution model.
2. **Normalize dependency semantics.** Address F-03 before adding more skills or
   building automation that relies on capability metadata.
3. **Restore the collection boundary.** Move the Python tool preference described
   in F-04 to the Python collection.
4. **Clarify lifecycle exits.** Fix the deprecation removal evidence model in F-05
   and risk-qualify launch examples in F-07.
5. **Strengthen maintenance controls.** Add the validation target from F-09.
6. **Reduce future drift.** Add source context for mutable guidance in F-06 and
   apply progressive disclosure selectively under F-10.

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
- 57 total canonical files in the collection
- no missing or changed installed counterpart among those 57 files
- no missing or extra agnostic skill in `ritebook-index.json`
- no unmentioned supporting file
- no broken supporting-file reference
- valid shell syntax for `idea-refine/scripts/idea-refine.sh`

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
