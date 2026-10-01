# Agnostic Software Development Skills Audit

Date: 2026-09-29

Audited revision: `6796d13c92bc2616de7913eec680755d3d151550`

## Purpose

This report audits the reusable Agent Skills under
`skills/agnostic-software-development/`. It evaluates structural validity,
portable Agent Skills compatibility, catalog routing, dependency metadata,
client-compatibility guidance, supporting resources, generated catalog state,
installed-copy parity, and repository validation readiness.

The audit is evidence-only. It does not modify the audited skill collection.

## Scope

The audit covered:

- 32 canonical `SKILL.md` files
- 32 supporting files: 25 references, 5 assets, 1 script, and 1 package README
- the collection catalog in
  `using-agnostic-software-development-skills/SKILL.md`
- skill-to-skill relationships and declared runtime capabilities
- supporting-file paths and references
- installed copies under `.agents/skills/`
- generated coverage in `ritebook-index.json`
- provenance in `ritebook.lock`
- repository validation and maintenance entry points
- current official Agent Skills, Claude Code, Cline, and GitHub Copilot
  documentation where the collection makes mutable compatibility claims

## Method

The review used the collection's `author-agent-skill` checklist as the local
contract, then checked that contract against the open Agent Skills specification
and its reference validator.

The audit included:

1. Ritebook header validation.
2. Agent Skills reference validation with `agentskills` 0.1.1 from the
   `skills-ref` package.
3. Manual and scripted checks for names, descriptions, versions, frontmatter,
   headings, dependency relationships, cross-skill references, and support paths.
4. Source-to-installed byte comparison for every collection file.
5. Source, generated-index, and lock coverage comparison.
6. Review of workflow composition and capability declarations.
7. Verification of mutable compatibility claims against current official
   documentation.
8. Comparison with the previous audit committed on 2026-09-21 to distinguish
   resolved findings from current ones.

Severity meanings:

- **High:** prevents a stated primary outcome or causes broad incompatibility.
- **Medium:** can misroute execution, misrepresent reproducibility, or produce
  incorrect integration behavior in common use.
- **Low:** maintenance, precision, or process weakness with narrower impact.

## Executive assessment

The collection is structurally healthy inside its native Ritebook workflow. All
32 skill headers pass Ritebook validation; names, descriptions, versions,
headings, support references, and dependency names are coherent; the generated
index covers every skill; and all 64 canonical files have byte-identical installed
copies under `.agents/skills/`.

The main problem is the gap between **Ritebook-local validity** and the
collection's broader portability claims. The open Agent Skills reference validator
accepts only 4 of 32 skills. Twenty-eight fail on inline empty sequence syntax,
and all 32 use a nested `metadata.dependencies` object even though the open
specification defines `metadata` as a map from string keys to string values. The
local `author-agent-skill` currently requires this repository-specific extension
without labeling the resulting compatibility boundary.

Three additional issues weaken operational reliability: client-adapter guidance
has already drifted from current official documentation, runtime capabilities are
still under-declared in execution-heavy workflows, and `ritebook.lock` no longer
describes the checked-in installed skill state.

**Verdict:** pass for the repository's current Ritebook consumer path, but not for
unqualified portable Agent Skills distribution. Resolve F-01 and F-02 before
claiming conformance with the open format, and resolve F-03 through F-05 before
treating the catalog metadata and client integration guidance as a dependable
orchestration contract.

**Post-audit update (2026-10-01):** F-01 through F-05 and F-08 are resolved. The
verdict above is retained as the conclusion for the audited revision; the
resolution notes under each finding describe the later remediation and its
evidence.

## Findings

### F-01 — High: 28 of 32 skills fail the Agent Skills reference validator

**Resolution status — resolved after the audited revision on 2026-09-30.** The
skill headers were migrated to string-valued metadata without inline empty
sequences or nested dependency objects. `skills-ref` 0.1.1 now accepts all 32
agnostic skills and all 47 canonical skills. Ritebook 0.1.48 also accepts all 47
canonical skills. The original finding and evidence below are retained because
they accurately describe audited revision
`6796d13c92bc2616de7913eec680755d3d151550`.

**Locations**

- frontmatter in 28 `SKILL.md` files under
  `skills/agnostic-software-development/`
- representative examples:
  - `add-observability/SKILL.md:7`
  - `author-agent-skill/SKILL.md:7-8`
  - `run-local-quality-gate/SKILL.md:11`
  - `using-agnostic-software-development-skills/SKILL.md:7`

**Evidence**

Ritebook accepts all 32 skills:

```text
uvx ritebook@latest skills lint --skills-root skills/agnostic-software-development
Validated 32 skill(s)
```

The open format's reference validator does not:

```text
uvx --from skills-ref agentskills --version
agentskills, version 0.1.1
```

A validation run across every skill produced:

```text
passed: 4
failed: 28
```

The passing skills were:

- `author-agents-config`
- `browser-runtime-verification`
- `conventional-commits`
- `idea-refine`

The other 28 were rejected before deeper semantic validation because their
frontmatter contains inline empty sequences such as `tools: []` or `skills: []`.
The reference validator reports those JSON-like flow collections as disallowed.

This is not an isolated edge case: every failing skill has at least one inline
empty sequence in its actual frontmatter. The examples inside
`author-agent-skill/SKILL.md` also teach the same form.

**Impact**

- A consumer using the reference validator can reject most of the collection.
- The local authoring skill teaches syntax that the reference tool rejects.
- Ritebook-only validation gives maintainers a false sense of cross-client
  portability.
- New skills copied from the local required shape will reproduce the failure.

**Recommendation**

1. Decide explicitly whether the shelf targets Ritebook only or the open Agent
   Skills format plus Ritebook extensions.
2. If open-format portability is required, redesign the dependency representation
   so the reference validator accepts the skill headers. Do not merely replace one
   empty-list spelling without validating the result.
3. Update `author-agent-skill` examples and checklist rules to teach the accepted
   shape.
4. Add the reference validator to the repository gate alongside Ritebook lint.
5. If the collection intentionally remains Ritebook-specific, declare that
   compatibility boundary in repository and skill documentation instead of
   describing the directories as generally portable.

### F-02 — Medium: All skills use metadata that conflicts with the open specification

**Resolution status — resolved after the audited revision on 2026-09-30.** All
47 canonical skills now use string-valued `metadata.version` without nested
`metadata.dependencies`. Both Ritebook 0.1.48 and `skills-ref` 0.1.1 accept the
resulting headers. Detailed capability requirements and skill relationships were
moved to compatibility, workflow, or catalog prose where applicable. The
original finding and evidence below are retained for audit traceability.

**Locations**

- all 32 canonical `SKILL.md` files
- `author-agent-skill/SKILL.md:61-79` and `98-176`
- `author-agents-config/references/client-adapters.md:119-124`

**Evidence**

Every skill uses this conceptual structure:

```yaml
metadata:
  version: "..."
  dependencies:
    tools: ...
    skills: ...
```

The open Agent Skills specification defines optional `metadata` as a map from
string keys to string values. A nested `dependencies` mapping with sequences of
objects is therefore a Ritebook-local extension rather than portable metadata.

The local `author-agent-skill` goes further: it makes `metadata.version` and
`metadata.dependencies` mandatory and describes the resulting skill as copyable
into a compatible agent environment. The client-adapter reference acknowledges
that the shelf adds version and dependency metadata, but it does not explain that
the dependency shape exceeds the open specification.

The current reference validator does not report this semantic mismatch for the
four skills that avoid inline empty sequences, so validator success alone is not
enough to prove specification conformance.

**Impact**

- Clients that strictly type `metadata` values as strings may reject or ignore the
  dependency graph.
- The shelf's portability contract is stronger than the evidence supports.
- Maintainers cannot tell which requirements are open-format requirements and
  which are Ritebook repository policy.

**Recommendation**

- Separate open Agent Skills frontmatter from Ritebook-specific orchestration
  metadata. Viable approaches include a sidecar manifest, an index-owned graph, or
  namespaced string metadata with a documented encoding.
- If nested dependencies remain, mark them as a Ritebook extension and add a
  `compatibility` statement where appropriate.
- Split `author-agent-skill` validation into two explicit profiles:
  `open-agent-skills` and `ritebook-shelf`.
- Do not claim general portability unless both the open specification and target
  client validators accept the emitted format.

External source:

- [Agent Skills specification](https://agentskills.io/specification)

### F-03 — Medium: Client-adapter guidance has drifted from current official behavior

**Resolution status — resolved after the audited revision on 2026-09-30.**
`author-agents-config` 1.2.0 now makes conditional native Claude Code
`AGENTS.md` loading the first candidate and keeps `@AGENTS.md` as a fallback;
records both supported Cline rule layouts; lists current documented Cline and
Copilot skill roots; and records Cline's source-backed `.agents/skills/` scan at
revision `457be3d2fdc7bea65ac2a0dea883ec355d890ace` without claiming it as
documented or runtime-observed behavior.

The remediation also adds an event-driven freshness rule, exact fresh-project
Cline bootstrap assets, duplicate-prevention and existing-project preservation
cases, and this shelf's own root `AGENTS.md` plus `.tmp/cline/` ignore coverage.
The packaged Cline rules are byte-identical to the root `.clinerules/` source and
the full package is byte-identical to its installed `.agents/skills/` copy.

Validation performed after the change:

- Ritebook 0.1.48 accepted all 32 agnostic skills and all 47 canonical skills.
- `skills-ref` 0.1.1 accepted all 47 canonical skills.
- The generated index covered all 47 canonical skills with no missing or extra
  entries; `ritebook.lock` remained unchanged.
- Package parity, three-way Cline scaffold parity, relative-link checks, stale
  compatibility-text checks, and `git diff --check` passed.

No live target-client session was run, so Claude, Cline, Copilot, and Codex
runtime discovery remains documented or source-backed rather than runtime
observed. The original finding and evidence below are retained because they
accurately describe audited revision
`6796d13c92bc2616de7913eec680755d3d151550`.

**Location**

- `author-agents-config/references/client-adapters.md:3-98`

**Evidence**

The reference says its documentation was checked on 2026-09-16 and correctly asks
agents to reverify version-sensitive facts. By 2026-09-29, several material facts
need updating:

1. **Claude Code:** the reference presents `CLAUDE.md` importing `AGENTS.md` as the
   standard adapter. Current Claude Code documentation says version 2.1.277 and
   later can read `AGENTS.md` directly. The default is conditional: direct loading
   occurs when no applicable project or local `CLAUDE.md` is present, and settings
   can select one or both instruction families. Importing remains a fallback for
   older or unsupported sessions, not the universal first choice.
2. **Cline rules:** the reference describes `.clinerules/` versus `.cline/rules/`
   as a documentation discrepancy. Current Cline documentation explicitly says
   both workspace layouts are supported by VS Code, Desktop, and CLI, and both are
   searched when present.
3. **Cline skills:** the reference names `.cline/skills/` as the documented client
   location. Current Cline documentation also lists `.clinerules/skills/` and
   `.claude/skills/` as project skill locations.
4. **GitHub Copilot:** the reference defers skill location entirely to the selected
   surface. Current GitHub documentation lists `.github/skills/`,
   `.claude/skills/`, and `.agents/skills/` as project skill roots across its
   documented agent-skill support.

**Impact**

- `author-agents-config` can create an unnecessary Claude adapter instead of using
  current native discovery.
- It can preserve Cline uncertainty that official documentation has resolved.
- It can add duplicate projections for clients that now consume the existing
  canonical skill root.
- The skill's core objective—smallest evidence-backed configuration—can be
  undermined by its own stale compatibility reference.

**Recommendation**

- Refresh the dated compatibility matrix and source notes.
- For Claude Code, make direct `AGENTS.md` loading the first candidate when the
  version, session, settings, and absence of conflicting `CLAUDE.md` files permit
  it; retain the import adapter as a documented fallback.
- Replace the Cline "documentation discrepancy" warning with the current
  both-layouts-supported behavior, while still preserving existing project choice.
- Record all currently documented Cline and Copilot skill roots and keep the
  no-duplicate-projection rule.
- Add a lightweight freshness policy, such as review on every related skill change
  or after a defined interval, without rewriting dates during no-op syncs.

External sources:

- [Claude Code project memory and AGENTS.md](https://code.claude.com/docs/en/memory)
- [Cline rules](https://docs.cline.bot/customization/cline-rules)
- [Cline skills](https://docs.cline.bot/customization/skills)
- [GitHub Copilot customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)

### F-04 — Medium: Execution-heavy workflows under-declare runtime capabilities

**Resolution status — resolved after the audited revision on 2026-10-01.** A
review of all 32 agnostic skills found no current Ritebook or client consumer for
machine-readable capability negotiation. The remediation therefore removed the
catalog's unsupported instruction to inspect declared capabilities instead of
introducing another repository-specific metadata format after F-01 and F-02.

The catalog now requires agents to read execution requirements in the selected
workflow, confirm needed access before execution-dependent steps, and choose one
truthful status: fully executed and verified; a documented, independently useful
design- or review-only artifact labeled runtime-unverified; or blocked. Missing
required execution never counts as successful verification.

The same completion boundary was made explicit in the 11 workflows where the
32-skill review found a real ambiguity:

- `add-observability`
- `ci-cd-and-automation`
- `code-simplification`
- `debugging-and-error-recovery`
- `deprecation-and-migration`
- `frontend-ui-engineering`
- `incremental-implementation`
- `performance-optimization`
- `security-and-hardening`
- `shipping-and-launch`
- `test-driven-development`

The other 20 skills did not need F-04 edits because their output is a reasoning
or documentation artifact, their runtime contract is inherent and already
bounded, or their unavailable-evidence behavior was already explicit.
`author-agent-skill` already directs authors to keep mandatory execution,
conditional enhancements, and fallbacks near the workflow step that needs them.
No capability sidecar, encoded metadata, custom frontmatter, index schema, or
Ritebook orchestration feature was added. The original finding and evidence below
are retained because they accurately describe audited revision
`6796d13c92bc2616de7913eec680755d3d151550`.

Post-remediation validation on 2026-10-01 confirmed:

```text
uvx ritebook@latest skills lint --root skills/agnostic-software-development
Checked 32 skill(s)

uvx ritebook@latest skills lint --root skills
Checked 47 skill(s)

uvx --from skills-ref agentskills validate <each-canonical-skill-directory>
passed: 47
failed: 0
```

Focused checks also confirmed byte-identical canonical and installed copies for
all 32 agnostic skills, no F-04 change to `ritebook-index.json` or `ritebook.lock`,
and no remaining current-workflow instruction to inspect declared capabilities.

**Locations**

- `using-agnostic-software-development-skills/SKILL.md:145-160` and `201-224`
- `test-driven-development/SKILL.md:55-104`, `182-199`, and `226-237`
- `incremental-implementation/SKILL.md:39-67` and `245-309`
- `debugging-and-error-recovery/SKILL.md:47-91` and `148-157`
- `performance-optimization/SKILL.md:64-72`, `74-199`, and `256-267`
- `security-and-hardening/SKILL.md:21-31` and `266-275`
- `ci-cd-and-automation/SKILL.md:50-223`
- `author-agent-skill/SKILL.md:253-262`

**Evidence**

The catalog requires agents to inspect declared capabilities before activation,
stop when a required capability is absent, and label documented optional fallbacks
as degraded. Its canonical vocabulary includes `shell-execution`,
`version-control`, `browser-runtime`, `source-retrieval`, and
`independent-review`.

Only eight skills declare any tool capability, with nine declarations total.
Twenty-four skills declare `tools: []`.

Several of those empty declarations belong to workflows whose stated outcome
requires commands or other external execution:

- TDD requires observing a focused test fail and pass, and recommends an
  independent reviewer for complex reproduction tests.
- Incremental implementation requires focused tests, builds, type checks, lint,
  runtime checks, and checkpoints.
- Debugging requires reproduction commands and widening validation.
- Performance optimization requires measurement, profiling, benchmarks, or load
  tests.
- Security hardening requires dependency, secret, static-analysis, test, and build
  checks.
- CI/CD work requires provider or project validation to move beyond a design-only
  artifact.
- Agent-skill authoring tells agents to run repository or target validators when
  available.

These actions may be conditional, but the metadata does not expose the condition,
requiredness, or fallback. `test-driven-development` also names independent review
without declaring `independent-review`.

**Impact**

- The catalog cannot perform the preflight check it mandates.
- An orchestrator may activate a skill that cannot produce its stated verified
  outcome.
- Missing capabilities are discovered late, after following workflow steps.
- Degraded design-only or manual paths are not consistently labeled.

**Recommendation**

- Audit every skill against the canonical capability vocabulary.
- Declare `shell-execution` where command execution is required or conditionally
  needed, and document a design-only or manual fallback where one is valid.
- Declare `independent-review` in TDD if that path remains part of the workflow.
- Distinguish skills that can produce a useful design artifact without execution
  from skills whose completion contract requires runtime evidence.
- Add a validation check that flags strong execution verbs and command
  placeholders in skills declaring no relevant capability, with manual review to
  avoid false positives.

### F-05 — Medium: `ritebook.lock` does not describe the checked-in installed state

**Resolution status — resolved after the audited revision on 2026-10-01.** The
registered Git-backed index was refreshed to repository revision
`b0e69e5282ffe84ed0c4dbe9d31dc9c3616bba2d`, whose exact root index digest is
`sha256:fb7521783128d4ece9b4e354bf261ee5b2be0462c52649df4233d30bbb3708b2`.
Ritebook 0.1.48 then synchronized the complete `ritebook.toml` installation and
regenerated `ritebook.lock` with 33 entries: all 32 agnostic skills plus the
configured writing-and-editing skill. Every entry now records that revision,
digest, Git URL source, and one synchronization timestamp.

The repository now pins the Ritebook version used by its Make targets and
provides `make check-ritebook-state`. The read-only checker regenerates the index
in a temporary directory, compares publisher state while ignoring only
`generated_at`, expands the complete requirements file, checks canonical and
installed directory contents, and verifies the lock against the exact index and
skill bytes at its bound Git revision. The README documents ownership of the
canonical, generated, installed, and provenance artifacts and distinguishes
conditional publication from required registry refresh and synchronization.

Post-remediation validation confirmed:

```text
resolved installations: 33
source revision: b0e69e5282ffe84ed0c4dbe9d31dc9c3616bba2d
index digest: sha256:fb7521783128d4ece9b4e354bf261ee5b2be0462c52649df4233d30bbb3708b2
checker errors: 0
canonical-to-installed differences: 0
```

A second forced synchronization preserved the normalized lock fingerprint and
the complete installed-tree fingerprint. As documented behavior for Ritebook
0.1.48, only `locked_at` changed between the two lockfiles; all other lock fields
and all installed bytes remained identical. The original finding and evidence
below are retained because they accurately describe audited revision
`6796d13c92bc2616de7913eec680755d3d151550`.

**Locations**

- `ritebook.lock`
- `.agents/skills/`
- `skills/agnostic-software-development/`
- `ritebook-index.json`

**Evidence**

All 64 canonical collection files currently have byte-identical counterparts
under `.agents/skills/`, so the checked-in source and installed trees agree.

However, all 32 agnostic entries in `ritebook.lock` still record:

```text
source_revision: 66b7de82750b12534e0bce0dd8bc20d248502a4a
locked_at: 2026-09-19T18:23:42.657480Z
index_digest: sha256:1d71d6b6680a69588e30d0e7aad00db37b85e91f3b0efdbefe68a46f51d1a6d1
```

The canonical and installed skills changed substantially after that revision. The
generated index was refreshed on 2026-09-22, and the audited repository revision is
`6796d13c92bc2616de7913eec680755d3d151550` from 2026-09-29.

The lock therefore attests an older source revision even though the installed
files are current and identical to the canonical tree.

**Impact**

- The lock cannot reproduce or verify the checked-in `.agents/skills` contents.
- A future sync or forced install can have ambiguous behavior: the lock points to
  old provenance while the working tree contains newer installed files.
- Reviewers cannot use the lock to establish which source revision produced the
  installed skills.

**Recommendation**

- Refresh the lock through the normal Ritebook installation/synchronization
  workflow after publishing the current index.
- Add a gate that compares lock revision/digest, generated index, canonical files,
  and installed targets.
- Document whether `.agents/skills` is generated, vendored, or intentionally edited
  in the same commits as canonical skills.
- Avoid manual lock editing; regenerate and then verify a no-op repeat sync.

### F-06 — Low: Validation is not a pinned, aggregate repository gate

**Locations**

- `Makefile:1-11`
- repository root

**Evidence**

The Makefile exposes index publication and update commands but no dedicated skill
lint or audit target. It defaults to:

```make
RITEBOOK ?= uvx ritebook@latest
```

The repository has no single documented command that verifies:

- Ritebook headers
- open Agent Skills reference compatibility
- supporting-file references
- script syntax
- dependency names and relationship values
- source-to-index coverage
- source-to-installed parity
- lock freshness

The README says Ritebook validates and publishes skills but does not document the
local validation command.

**Impact**

- Contributors can run different validator versions at different times.
- The native validator passes while the open reference validator fails most
  skills.
- Index, installed-copy, and lock drift can survive a successful lint run.

**Recommendation**

- Pin the Ritebook and reference-validator versions used by the repository gate.
- Add a `lint-skills` or `audit-skills` Make target that performs the aggregate
  read-only checks.
- Run the same target in CI if publishing or installation is automated.
- Keep publication separate from validation so the gate itself does not rewrite
  generated files.

### F-07 — Low: The README advertises a missing maintenance workflow

**Location**

- `README.md:12-15`

**Evidence**

The README links to:

```text
tools/cline-skill-workflow/README.md
```

The repository has no `tools/` directory at the audited revision, so the documented
maintenance entry point is broken.

**Impact**

- Maintainers following the repository documentation cannot find the promised
  recursive skill-review workflow.
- The missing link obscures the actual validation process, which is already not
  exposed as a first-class command under F-06.

**Recommendation**

- Restore the documented workflow or remove/replace the link with the current
  maintenance command and source of truth.
- Include link existence in documentation validation.

### F-08 — Low: `interview-me` encourages false precision and excessive ceremony

**Resolution status — resolved after the audited revision on 2026-10-01.**
`interview-me` 2.0.0 replaces numeric confidence and the 90% completion threshold
with the ordinal states `exploring`, `narrowing`, and `ready-for-confirmation`.
The skill now defaults to a light path for one or two ordinary ambiguities and
uses the full operating model for explicit interview requests, high XY-risk, or
interacting material unknowns. Completion depends on decision sufficiency,
explicit disposition of material unknowns, and direct user confirmation.

The supporting examples now define normative short-, medium-, and high-ambiguity
scenarios. Manual dry-runs confirmed that the short scenario remains light, the
medium scenario escalates when a second user and outcome emerge, and an explicit
interview starts in full mode with ordinal readiness. Ritebook 0.1.48 accepts all
32 agnostic skills, `skills-ref` 0.1.1 accepts the revised skill, and the canonical
and installed `interview-me` directories are byte-identical. This is documented
scenario validation, not an automated agent-behavior evaluation.

**Location**

- `interview-me/SKILL.md:90-115`
- `interview-me/SKILL.md:228-280`

**Evidence**

The skill requires a numeric `CONFIDENCE: <0-100%>`, assigns detailed meaning to
numeric bands, requires confidence of at least 90% before stopping, and verifies
that the first turn included a falsifiable hypothesis, numeric confidence,
evidence, unknowns, the stated solution, the underlying outcome, and an XY-risk
level.

The skill correctly says confidence is not psychological certainty and requires
user confirmation. Even so, no calibration method supports the difference between,
for example, 88% and 90%. The threshold can turn a useful uncertainty model into a
compliance ritual and can prolong interviews even when all material decisions are
resolved.

**Impact**

- Agents can manufacture precise-looking numbers unsupported by evidence.
- Users with a straightforward ambiguity can receive an overly formal first turn.
- The numeric threshold can conflict with the stronger behavioral stop condition:
  no unresolved unknown materially changes the next decision.

**Recommendation**

- Replace numeric confidence with a small ordinal state such as `low`, `medium`,
  `ready-for-confirmation`, or make the number explicitly optional.
- Make material unresolved decisions and explicit user confirmation the normative
  stop criteria.
- Keep the full operating model for high-risk or explicitly requested interviews,
  but define a lighter path for one or two ordinary clarifications.
- Test the skill against representative short, medium, and high-ambiguity prompts
  to verify that ceremony scales with uncertainty.

## Resolved or substantially improved findings from the previous audit

The previous audit, committed on 2026-09-21, identified nine findings. Most were
addressed on 2026-09-22.

### Resolved: catalog routing versus specification and TDD

The catalog now makes specification conditional, routes precise small changes
directly from the request, and places TDD inside each behavior-changing
implementation slice.
`using-agnostic-software-development-skills/references/catalog-reference.md`
explains that there is no universal ordered lifecycle.

### Resolved: incremental implementation order and vertical slicing

`incremental-implementation` now uses `Define outcome -> Red when applicable ->
Implement -> Verify -> Checkpoint`, distinguishes non-behavioral work, and labels
contract-first and risk-first increments instead of describing incomplete layers
as vertical slices.

### Resolved after this audit: runtime execution and fallback semantics

The collection retains `route`, `handoff`, `verification`, and `awareness` as
prose relationship terms. On 2026-10-01, F-04 was resolved without a capability
metadata protocol: the catalog stopped promising automatic declared-capability
preflight, and ambiguous execution-heavy workflows gained explicit full,
runtime-unverified bounded-artifact, and blocked outcomes.

### Resolved: Python-specific type-checker policy in agnostic workflows

`ci-cd-and-automation` and `run-local-quality-gate` now defer to project-configured
tools or require an explicit technology-specific decision instead of preferring a
Python checker in the agnostic collection.

### Resolved: proof-of-zero requirement for deprecation removal

`deprecation-and-migration` now distinguishes proven zero usage, no known active
consumers, and remaining usage that cannot be observed. Removal gates account for
support windows, notice, approval, and residual-risk acceptance.

### Resolved: mutable Core Web Vitals context

`performance-optimization/references/web-performance.md` now identifies the
official source, records verification and source-update dates, explains the 75th
percentile assessment context, and requires reverification before presenting the
thresholds as current policy.

### Resolved: unqualified launch defaults

`shipping-and-launch` now derives controls from release risk, accepts rollback,
disablement, roll-forward, compensation, or documented irreversibility, and uses
project-derived triggers instead of universal numeric targets.

### Still open: reproducible repository validation

The prior validation-gate finding remains and is expanded in F-06 because the
reference-validator incompatibility and stale lock demonstrate the practical gap.

### Improved: progressive disclosure

The catalog now moves lifecycle detail into a reference, and multiple long skills
use focused supporting files. All main skill files remain below the open
specification's 500-line recommendation. Further splitting should be driven by
activation cost and cohesion, not a mechanical line limit.

## Positive findings

- Ritebook validates all 32 canonical skill headers.
- All skill names match their parent directories and use valid kebab-case.
- All descriptions are non-empty, specific, and under 1024 characters.
- All versions use quoted three-part semantic versions.
- All dependency objects include purpose and requiredness; all skill dependencies
  use one of the collection's declared relationship values.
- No dependency references a missing skill.
- The catalog declares and routes all 31 constituent workflow skills.
- Every main skill has exactly one top-level heading outside fenced examples.
- No heading-level jumps or duplicate structural headings were found outside code
  examples.
- Every supporting file referenced from a `SKILL.md` exists.
- Every file under `references/`, `assets/`, and `scripts/` is referenced by its
  owning skill.
- `idea-refine/scripts/idea-refine.sh` is executable and passes `sh -n`.
- `ritebook-index.json` contains exactly the 32 canonical agnostic skills, with no
  missing or extra entry.
- `ritebook.lock` contains the same 32 skill names, despite its stale provenance.
- All 64 canonical collection files have byte-identical installed counterparts
  under `.agents/skills/`.
- No local absolute user paths or private project names were found in portable
  skill content.
- Existing security guidance consistently treats browser content, logs, errors,
  and external output as untrusted data.
- The collection's earlier routing, TDD, migration, web-performance, and launch
  coherence issues were materially improved.

## Recommended remediation order

1. **Choose and enforce the portability profile.** Resolve F-01 and F-02 together;
   update the authoring skill and validate every skill with both intended
   validators.
2. **Refresh client compatibility.** Resolve F-03 before using
   `author-agents-config` for new multi-client setup or migration work.
3. **Clarify runtime completion contracts.** Resolve F-04 without speculative
   orchestration metadata: remove unsupported preflight claims and distinguish
   verified execution, bounded runtime-unverified artifacts, and blocked work.
4. **Restore reproducible provenance.** Refresh and verify `ritebook.lock` under
   F-05.
5. **Create a pinned aggregate gate.** Address F-06, then use that gate to prevent
   recurrence of F-01 through F-05 and F-07.
6. **Repair repository documentation.** Resolve F-07 by restoring or replacing the
   missing maintenance workflow link.
7. **Calibrate interaction overhead.** Evaluate and simplify `interview-me` under
   F-08 using representative conversations.

Behavioral, metadata, asset, script, or reference changes should increment the
owning skill's version according to `author-agent-skill`. Canonical skill changes
should then be propagated through the repository's documented Ritebook workflow,
with installed-copy and lock parity verified rather than edited blindly.

## Validation evidence

Commands and checks run during this audit included:

```text
uvx ritebook@latest skills lint --skills-root skills/agnostic-software-development
Validated 32 skill(s)
```

```text
uvx --from skills-ref agentskills --version
agentskills, version 0.1.1
```

```text
uvx --from skills-ref agentskills validate <each-skill-directory>
passed: 4
failed: 28
```

```text
sh -n skills/agnostic-software-development/idea-refine/scripts/idea-refine.sh
idea-refine.sh syntax: PASS
```

Additional read-only checks confirmed:

- 32 canonical skills and 64 total collection files
- valid local metadata scalar constraints, names, descriptions, and versions
- valid dependency names, required flags, and relationship values
- one real top-level heading per skill
- no missing supporting-file path
- no unreferenced `references/`, `assets/`, or `scripts/` file
- exact 32-skill coverage in `ritebook-index.json`
- exact 32-skill name coverage in `ritebook.lock`
- byte-identical canonical and `.agents/skills` copies for all 64 files
- valid shell syntax for the only bundled executable script
- current official compatibility facts for Claude Code, Cline, and GitHub Copilot

## Limitations

- The audit did not execute every workflow against representative target projects.
  Workflow findings are based on written contracts, composition, and the runtime
  evidence each workflow requires.
- The audit did not run `ritebook install --force` or regenerate the lock because
  those commands can change repository state; F-05 is based on direct provenance
  comparison.
- The reference-validator failures were tested with `agentskills` 0.1.1. Future
  validator releases may change parsing behavior, which is why the repository
  should pin and intentionally update the selected version.
- Client support can change quickly. The compatibility findings reflect official
  documentation checked on 2026-09-29 and should be reverified before future
  migrations.
- The audit evaluates portability against the published open specification. A
  Ritebook-only extension can be valid for this repository if it is explicitly
  documented and validated as such.
