# Agnostic Software-Development Skills Audit

Date: 2026-09-22

Status: Open remediation backlog

## Purpose

This report audits `skills/agnostic-software-development/` for structural
validity, semantic metadata accuracy, Agent Skills portability, current client
compatibility, and repository integration defects.

The intended readers are maintainers of this shelf. Findings are recorded here
so they can be reviewed and addressed separately from the audit itself. This
document does not authorize or apply the recommended skill, adapter, index, or
repository changes.

Line references identify the repository state inspected on 2026-09-22. Recheck
them after edits.

## Scope

The audit covered:

- all 32 canonical `SKILL.md` files under
  `skills/agnostic-software-development/`
- all 32 supporting files under those skill directories, for 64 collection
  files in total
- the collection router and dependency contract in
  `using-agnostic-software-development-skills/`
- skill-to-skill references and declared runtime capabilities
- supporting files under `assets/`, `references/`, and `scripts/`
- generated catalog coverage in `ritebook-index.json`
- repository-level documentation and maintenance integration
- current official Agent Skills, Claude Code, Cline, VS Code, GitHub Copilot,
  Core Web Vitals, and Conventional Commits documentation where claims depend
  on mutable external behavior

The audit did not change any target skill, supporting resource, generated index,
or repository integration file.

## Severity model

- **Critical:** likely to cause security exposure, data loss, or severe broken
  behavior.
- **High:** invalidates a collection-wide contract or a central portability
  claim and can cause materially incorrect activation or execution.
- **Medium:** creates stale compatibility guidance, incomplete runtime gating,
  or a broken repository integration path.
- **Low:** maintainability or verification weakness with limited immediate
  behavioral impact.

## Executive assessment

The collection is structurally healthy, internally well linked, and accepted by
Ritebook lint. No critical issue was found. However, the collection is not yet
semantically accurate or fully portable as currently described.

The two highest-priority problems are:

1. Several execution-oriented skills declare no runtime capabilities even though
   their stated outcomes require command or browser execution. The collection
   router treats those declarations as activation gates.
2. Every skill uses nested dependency objects under `metadata`, while the Agent
   Skills specification defines metadata as a string-to-string map. Ritebook
   accepts the extension, but generic Agent Skills consumers are not required to
   preserve its structure or semantics.

The client-adapter reference also contains stale Claude Code and Cline guidance,
and the root README links to a missing repository tool.

**Verdict:** request changes before claiming complete dependency metadata,
cross-client portability, or current adapter guidance.

## Findings summary

| ID   | Severity | Category                 | Summary                                                                                 | Status |
| ---- | -------- | ------------------------ | --------------------------------------------------------------------------------------- | ------ |
| F-01 | High     | Collection-internal      | Mandatory execution capabilities are absent from several skill declarations             | Open   |
| F-02 | High     | Agent Skills portability | Nested dependency metadata is not portable as structured Agent Skills metadata          | Open   |
| F-03 | Medium   | Collection-internal      | The five-name capability vocabulary cannot represent important operational access       | Open   |
| F-04 | Medium   | External-client guidance | Claude Code guidance presents `AGENTS.md` as import-only rather than natively supported | Open   |
| F-05 | Medium   | External-client guidance | Cline's two documented rule directories are described as a documentation discrepancy    | Open   |
| F-06 | Medium   | Repository integration   | The root README links to a missing repository tool                                      | Open   |

## Collection-internal defects

### F-01 — High: Mandatory execution capabilities are absent from metadata

#### Contract evidence

The collection router makes dependency declarations behaviorally significant:

- `skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md:153-160`
  requires checking selected skills' capabilities before activation, stopping
  when a required capability is unavailable, and labeling optional fallbacks as
  degraded.
- The canonical capability names are defined in the same file at lines 201-209.
- Required-versus-optional semantics are defined at lines 211-213.
- `skills/agnostic-software-development/author-agent-skill/SKILL.md:100-107`
  says runtime assumptions must be declared.
- The same file says `tools: []` is appropriate only when no known tool,
  command, permission, service, or runtime dependency exists at lines 128-133.

At least four skills conflict with that contract.

#### F-01a: `test-driven-development` requires shell execution

Evidence:

- It declares `tools: []` at
  `skills/agnostic-software-development/test-driven-development/SKILL.md:4-12`.
- It requires confirming that a new test fails at lines 55-58.
- It requires running the focused test command at lines 88-89.
- It requires running relevant tests after meaningful refactors at lines
  103-104.
- Completion requires focused and broader tests to pass at lines 226-237.

Impact:

The router can activate the skill where local commands cannot be run even though
the skill cannot complete its RED-GREEN-REFACTOR outcome in that environment.

Recommended fix:

```yaml
tools:
  - name: shell-execution
    purpose: Run focused and broader tests and confirm RED-GREEN-REFACTOR evidence.
    required: true
```

The instruction to use an independent reviewer or subagent for complex bug fixes
at lines 195-199 should also be declared as optional `independent-review`, or
softened to an explicitly optional recommendation.

#### F-01b: `incremental-implementation` requires shell execution

Evidence:

- It declares `tools: []` at
  `skills/agnostic-software-development/incremental-implementation/SKILL.md:4-12`.
- It requires running an initial green baseline at lines 43-49.
- It requires focused tests and affected builds, type checks, static analysis,
  integration checks, or runtime verification at lines 53-55.
- It requires affected checks after every increment at lines 181-185.
- Its final checklist requires tests, build, type checking, and linting at lines
  241-259.

Impact:

The core outcome of independently verified increments cannot normally be
completed without command execution.

Recommended fix:

```yaml
tools:
  - name: shell-execution
    purpose: Run focused tests and affected build, type, lint, and integration checks for each increment.
    required: true
  - name: version-control
    purpose: Create a descriptive checkpoint when the repository workflow uses commits.
    required: false
```

Version control remains optional because the skill provides an explicit progress
note as a checkpoint fallback at lines 56-58.

#### F-01c: `frontend-ui-engineering` requires browser runtime access

Evidence:

- It declares `tools: []` at
  `skills/agnostic-software-development/frontend-ui-engineering/SKILL.md:4-12`.
- It says real-browser verification is required when behavior or visual state
  matters at lines 39-46.
- It requires runtime verification at lines 157-170.
- It treats shipping visual behavior without browser verification as a red flag
  at lines 188-198.
- Its output checklist requires browser verification to be run or skipped with a
  reason at lines 200-210.

The optional reference to `browser-runtime-verification` does not replace a
direct tool declaration. The router states that optional related skills are not
recursively activated merely because they are listed at
`using-agnostic-software-development-skills/SKILL.md:222-224`.

Impact:

The skill can be activated without the capability needed to substantiate its
production-quality UI outcome.

Recommended fix:

```yaml
tools:
  - name: browser-runtime
    purpose: Verify rendering, interaction, focus, accessibility, network behavior, and responsive layout.
    required: true
```

An alternative is to narrow this skill to design and static implementation
guidance, then delegate all runtime claims. That would materially change its
current outcome and should be versioned accordingly.

#### F-01d: `code-simplification` requires executable validation or a fallback

Evidence:

- It declares `tools: []` at
  `skills/agnostic-software-development/code-simplification/SKILL.md:4-8`.
- Every simplification must run the narrowest relevant check at lines 123-132.
- Risky simplification should have tests at lines 138-145.
- The completed result must have validation covering the affected behavior at
  lines 147-158.

Impact:

The skill can claim behavior preservation without declaring the execution
capability its workflow normally requires.

Recommended fix:

Declare `shell-execution` as required, or document a constrained no-shell mode
that reports a review-only result and does not claim behavior preservation was
verified.

#### Acceptance criteria

- The four skills no longer declare `tools: []` while requiring unavailable
  execution capabilities.
- Each `required` value follows the contract at
  `using-agnostic-software-development-skills/SKILL.md:211-213`.
- Conditional independent review and checkpoint behavior is either declared or
  worded as optional with a usable fallback.
- A regression check detects imperative execution requirements paired with an
  empty tool list where practical.
- Changed skill versions and generated index data are updated as required.

### F-03 — Medium: The capability vocabulary cannot represent operational access

The router currently defines only these capabilities at
`skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md:201-209`:

- `shell-execution`
- `version-control`
- `browser-runtime`
- `source-retrieval`
- `independent-review`

That vocabulary is insufficient for several operational workflows.

#### `performance-optimization`

- Declares `tools: []` at
  `skills/agnostic-software-development/performance-optimization/SKILL.md:4-20`.
- Requires measurement and remeasurement at lines 64-72.
- Uses telemetry, benchmarks, profiles, traces, and repeatable tests at lines
  74-108.
- Requires rerunning a comparable scenario at lines 155-178.

The full outcome needs runtime measurement access, though that access is not
always equivalent to local shell execution.

#### `add-observability`

- Declares `tools: []` at
  `skills/agnostic-software-development/add-observability/SKILL.md:4-28`.
- Requires exercising representative runtime paths and verifying exported
  telemetry at lines 188-208.

The full outcome needs runtime or telemetry access.

#### `ci-cd-and-automation`

- Declares `tools: []` at
  `skills/agnostic-software-development/ci-cd-and-automation/SKILL.md:4-8`.
- Requires safe exercise of mutating automation at lines 174-189.
- Requires verification in the intended environment at lines 207-223.

Execution can require shell access, source retrieval, and CI-provider access.

#### `shipping-and-launch`

- Declares `tools: []` at
  `skills/agnostic-software-development/shipping-and-launch/SKILL.md:4-20`.
- Directs incremental deployment at lines 48-60.
- Directs rollout and recovery execution at lines 87-113.
- Requires post-launch signals, user-flow testing, logs, and recovery verification
  at lines 134-155.

Execution can require deployment control, runtime observation, dashboards, and
external-service access. Those operations also require authorization boundaries,
not only technical availability.

Impact:

- Operational skills cannot accurately distinguish planning, local execution,
  provider access, runtime observation, and production mutation.
- A skill may pass the capability gate and then instruct an unavailable or
  unauthorized external operation.
- Marking everything as `shell-execution` would hide meaningful permission and
  environment differences.

Recommended fix:

Choose one of these approaches:

1. Add canonical capabilities such as `runtime-observation`, `telemetry-access`,
   `ci-provider-access`, `deployment-control`, and `external-service-access`.
2. Split affected skills into explicit planning and execution modes, with
   execution modes declaring the additional capabilities.
3. Combine both approaches where a single skill must support planning and
   authorized execution.

For every new capability, define:

- what access it represents
- when it is required versus optional
- whether user authorization is separately required
- the fallback when unavailable
- what outcome may still be claimed in degraded mode

#### Acceptance criteria

- Each operational skill distinguishes design-only, local verification, remote
  observation, and mutating execution.
- Production or provider mutation cannot follow solely from `tools: []`.
- The router and `author-agent-skill` document the expanded vocabulary or mode
  model.
- Capability availability and user authorization are treated as separate gates.

## Agent Skills portability issues

### F-02 — High: Nested dependency metadata is not portable as structured metadata

All 32 canonical skills place nested mappings and arrays under
`metadata.dependencies`. The collection also teaches this as a required shape in:

- `skills/agnostic-software-development/author-agent-skill/SKILL.md:61-79`
- `skills/agnostic-software-development/author-agent-skill/SKILL.md:98-133`
- `skills/agnostic-software-development/author-agent-skill/SKILL.md:264-285`

Representative live instances include:

- `skills/agnostic-software-development/test-driven-development/SKILL.md:4-12`
- `skills/agnostic-software-development/author-agents-config/SKILL.md:4-22`
- `skills/agnostic-software-development/using-agnostic-software-development-skills/SKILL.md:4-132`

The Agent Skills specification defines `metadata` as a string-to-string map. It
does not define arbitrarily nested dependency objects as portable structured
metadata.

Official `skills-ref` parser and validator source inspected during this audit
showed an important nuance: nested values are stringified by the parser and the
validator does not currently enforce metadata value types. Ritebook lint and the
current reference validator can therefore pass while `required`, `relationship`,
and `purpose` cease to exist as portable structured fields.

Impact:

- Ritebook understands the local extension, but a generic Agent Skills consumer
  may receive `dependencies` only as an opaque string.
- Generic clients are not required to preserve or act on the collection's
  capability gates and routing relationships.
- The authoring skill currently presents the Ritebook-specific structure as a
  generally portable required header.
- Validator success can be misinterpreted as proof that the structured dependency
  semantics are portable.

Recommended decision:

Choose and document one compatibility model.

#### Option A: Strictly portable metadata

- Keep every value directly under `metadata` as a string.
- Move rich dependency data to a referenced file such as `dependencies.json` or
  another explicitly versioned manifest.
- Update Ritebook or shelf tooling to consume that manifest.
- Keep a concise portable metadata string when useful for discovery.

#### Option B: Explicit Ritebook extension

- Retain nested dependency objects.
- Document them as a Ritebook-specific extension.
- State that generic Agent Skills clients may discard their structure and cannot
  be assumed to enforce their semantics.
- Stop describing the nested shape as universally portable.

#### Option C: Dual-layer representation

- Use portable string metadata for generic consumers.
- Store the canonical structured dependency model in a separate manifest consumed
  by Ritebook and repository checks.
- Generate any derived summary rather than maintaining two independent sources.

Option C provides the clearest separation between Agent Skills portability and
Ritebook-specific routing semantics.

#### Acceptance criteria

- The repository explicitly records which metadata fields are portable and which
  are Ritebook extensions.
- `author-agent-skill` no longer teaches a non-portable nested shape as a generic
  Agent Skills requirement.
- The chosen representation preserves `required`, `purpose`, and `relationship`
  semantics for Ritebook consumers.
- Generic consumer behavior is not overstated.
- Ritebook lint, the official reference validator, and custom semantic checks are
  run after migration.

## Stale external-client claims

External behavior in this section was checked against official documentation on
2026-09-22. Reverify it when remediation is implemented.

### F-04 — Medium: Claude Code guidance presents `AGENTS.md` as import-only

Evidence:

- The adapter matrix says Claude Code uses `CLAUDE.md` to import adjacent
  `AGENTS.md` at
  `skills/agnostic-software-development/author-agents-config/references/client-adapters.md:13-18`.
- The Claude Code section describes `@AGENTS.md` import as the integration path at
  lines 41-60.
- `author-agents-config/SKILL.md:151-153` directs the bundled Claude adapter for
  confirmed support.
- The acceptance case at
  `author-agents-config/references/validation.md:86` expects a minimal adapter.

Current Claude Code documentation describes native `AGENTS.md` support in current
supported versions, with precedence, version, and fresh-session considerations.
A `CLAUDE.md` import remains relevant for coexistence and explicit composition,
but it is no longer accurate to present import as the only supported mechanism.

Impact:

- The workflow can create a redundant `CLAUDE.md` adapter even though its own
  preference order chooses native discovery before imports.
- A repository can acquire another configuration surface without client-specific
  content requiring it.
- Validation cases encode the stale default.

Recommended fix:

Update the matrix and workflow to distinguish:

1. native `AGENTS.md` discovery in supported Claude Code versions
2. precedence when both `CLAUDE.md` and `AGENTS.md` exist
3. `@AGENTS.md` import when coexistence or explicit composition requires it
4. scoped and nested instruction behavior, which must still be verified rather
   than assumed
5. installed-client version and fresh-session requirements

Make the bundled Claude adapter conditional rather than the default confirmed
support path.

Official source:

- <https://code.claude.com/docs/en/memory>

#### Acceptance criteria

- Native discovery is the first path for a supported current Claude Code client.
- The workflow preserves existing `CLAUDE.md` client-specific content.
- Imports are added only when they solve a verified coexistence or scope need.
- The adapter matrix, skill instructions, template guidance, and acceptance cases
  agree.
- The documentation check date is updated only after the content is reverified.

### F-05 — Medium: Cline rule directories are described as a discrepancy

Evidence:

- `skills/agnostic-software-development/author-agents-config/references/client-adapters.md:62-81`
  says the Rules and Config pages disagree between `.clinerules/` and
  `.cline/rules/`.
- `author-agents-config/SKILL.md:155-158` carries that uncertainty into migration
  guidance.
- `author-agents-config/references/validation.md:87-88` treats the newer path as
  version-uncertain.

Current Cline documentation explicitly documents both `.clinerules/` and
`.cline/rules/`. Preserving an existing working layout remains good guidance, but
the rationale should be support and migration stability rather than a supposed
documentation contradiction.

Impact:

- A supported directory can appear experimental or accidental.
- Fresh-setup guidance cannot clearly state the current preferred layout.
- Maintainers may defer a safe migration for the wrong reason or create duplicate
  paths as a speculative workaround.

Recommended fix:

- State that both locations are documented.
- Preserve an existing supported path unless migration is requested.
- Identify the preferred path for a fresh setup from current documentation.
- Do not duplicate rules across both locations without a verified need.
- Test actual loading in the installed client when scope or precedence matters.

Official sources:

- <https://docs.cline.bot/customization/cline-rules>
- <https://docs.cline.bot/getting-started/config>
- <https://docs.cline.bot/customization/skills>

#### Acceptance criteria

- The adapter reference no longer calls the two paths a documentation
  discrepancy.
- Existing supported layouts remain preserved by default.
- Fresh-setup, migration, precedence, and duplicate-loading guidance are explicit.
- Related validation cases match the updated support model.

## Repository integration defects

### F-06 — Medium: The root README links to a missing repository tool

Evidence:

- `README.md:12-15` links to `tools/cline-skill-workflow/README.md`.
- `tools/cline-skill-workflow/README.md` does not exist in the inspected tree.
- No replacement file was found under `tools/`.

Impact:

The repository's only documented tool entry leads to missing content and cannot
be followed by contributors.

Recommended fix:

Choose one:

- restore the tool and its README if it remains an owned repository feature
- remove the repository-tools section if the tool was retired
- update the link and description if the workflow moved

Do not create an empty placeholder solely to satisfy the link check.

#### Acceptance criteria

- Every repository-local README link resolves.
- The linked workflow exists and matches its description, or the stale entry is
  removed.
- The final validation includes a repository-local link check.

## Capability-declaration audit

This matrix distinguishes mandatory omissions from conditional or mode-specific
access. It excludes operations that appear only as examples and capabilities
fully delegated to a separately activated skill.

Legend:

- `R`: correctly declared required
- `O`: correctly declared optional
- `+R`: missing required declaration
- `+O`: missing conditional declaration or explicit fallback
- `delegated`: owned by a separately activated skill
- `—`: no direct declaration needed

| Skill                                        | Shell execution | Version control | Browser runtime | Source retrieval | Independent review |
| -------------------------------------------- | --------------- | --------------- | --------------- | ---------------- | ------------------ |
| `add-observability`                          | `+O`            | —               | —               | —                | —                  |
| `api-and-interface-design`                   | `+O`            | —               | —               | —                | —                  |
| `author-agent-skill`                         | `+O`            | —               | —               | `+O`             | —                  |
| `author-agents-config`                       | —               | `O`             | —               | `O`              | —                  |
| `browser-runtime-verification`               | `+O`            | —               | `R`             | —                | —                  |
| `ci-cd-and-automation`                       | `+O`            | —               | —               | `+O`             | —                  |
| `code-review-and-quality`                    | —               | `+O`            | —               | —                | —                  |
| `code-simplification`                        | `+R`            | —               | —               | —                | —                  |
| `context-engineering`                        | —               | —               | —               | —                | —                  |
| `conventional-commits`                       | —               | `O`             | —               | —                | —                  |
| `debugging-and-error-recovery`               | `+O`            | —               | —               | —                | —                  |
| `deprecation-and-migration`                  | `+O`            | —               | —               | —                | —                  |
| `documentation-and-adrs`                     | —               | —               | —               | —                | —                  |
| `doubt-driven-development`                   | —               | —               | —               | —                | `O`                |
| `frontend-ui-engineering`                    | `+O`            | —               | `+R`            | —                | —                  |
| `git-workflow-and-versioning`                | —               | `R`             | —               | —                | —                  |
| `hexagonal-vertical-slices`                  | `+O`            | —               | —               | —                | —                  |
| `idea-refine`                                | `O`             | —               | —               | —                | —                  |
| `incremental-implementation`                 | `+R`            | `+O`            | —               | —                | —                  |
| `interview-me`                               | —               | —               | —               | —                | —                  |
| `performance-optimization`                   | `+O`            | —               | `+O`            | —                | —                  |
| `planning-and-task-breakdown`                | —               | —               | —               | —                | —                  |
| `review-implementation-plan`                 | —               | —               | —               | —                | —                  |
| `run-local-quality-gate`                     | `R`             | —               | —               | —                | —                  |
| `security-and-hardening`                     | `+O`            | `+O`            | —               | —                | —                  |
| `shipping-and-launch`                        | `+O`            | —               | `+O`            | —                | —                  |
| `source-driven-development`                  | —               | —               | —               | `R`              | —                  |
| `spec-driven-development`                    | —               | —               | —               | —                | —                  |
| `test-driven-development`                    | `+R`            | —               | `delegated`     | —                | `+O`               |
| `update-project-docs`                        | `+O`            | —               | —               | —                | —                  |
| `using-agnostic-software-development-skills` | —               | —               | —               | —                | —                  |
| `write-adr`                                  | —               | —               | —               | —                | —                  |

Only the `+R` entries are unequivocal activation blockers. The `+O` entries are
conditional capabilities expected by some workflow modes. Under the collection's
own metadata contract, they should be declared or explicitly delegated with a
usable fallback.

This matrix should be reassessed after F-03 defines how runtime observation,
telemetry, CI-provider access, deployment control, and external services are
represented.

## Recommended remediation order

1. Decide the metadata compatibility model in F-02.
2. Correct the required capability declarations in F-01.
3. Define the operational capability or mode model in F-03.
4. Apply conditional declarations and explicit fallbacks from the capability
   matrix.
5. Update Claude Code guidance in F-04.
6. Update Cline guidance in F-05.
7. Fix or remove the broken README integration in F-06.
8. Increment affected skill versions according to the collection's versioning
   policy.
9. Regenerate or verify `ritebook-index.json` when descriptions or indexed fields
   change.
10. Run the complete validation plan below and record the results.

## Validation evidence from the audit

The read-only audit confirmed:

- 32 canonical skill directories
- 64 files in `skills/agnostic-software-development/`
- every canonical `SKILL.md` passed
  `uvx ritebook@latest skills lint --root skills/agnostic-software-development`
- frontmatter, dependency references, headings, fences, and relative links were
  checked
- supporting files, index coverage, shell syntax and mode, symlinks, and empty
  files were checked
- every current canonical skill is represented in `ritebook-index.json`
- no target skill or supporting file was modified by the audit

## Required validation after remediation

Run and record:

1. The official `skills-ref` validator against every canonical skill directory.
2. `uvx ritebook@latest skills lint --root skills/agnostic-software-development`
   or the repository's pinned equivalent.
3. A custom semantic dependency check covering:
   - canonical capability names
   - required and optional declarations
   - referenced skill existence
   - valid relationships
   - stop and fallback semantics
4. A metadata portability check for the representation selected in F-02.
5. Markdown heading, fence, and repository-local link checks.
6. Supporting-file reference and optional-directory checks.
7. Index coverage and description parity checks.
8. Shell syntax and executable-mode checks for scripts.
9. Fresh-session adapter verification for changed Claude Code and Cline guidance
   where the clients are available.
10. Final diff inspection to ensure unrelated files and changes are preserved.

Passing the reference validator is necessary but not sufficient for F-02 because
the current validator does not establish preservation of nested metadata
semantics.

## External sources

- Agent Skills specification: <https://agentskills.io/specification>
- Claude Code memory and instruction files:
  <https://code.claude.com/docs/en/memory>
- Claude Code skills: <https://code.claude.com/docs/en/skills>
- Cline Rules: <https://docs.cline.bot/customization/cline-rules>
- Cline Config: <https://docs.cline.bot/getting-started/config>
- Cline Skills: <https://docs.cline.bot/customization/skills>
- GitHub Copilot custom-instruction support:
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>
- VS Code custom instructions:
  <https://code.visualstudio.com/docs/agent-customization/custom-instructions>

## Limitations

- The official `skills-ref` validator was not executed during the read-only audit
  because doing so required temporary checkout or installation mutations that were
  outside that pass. Its specification and parser/validator source were inspected.
- Ritebook lint validates accepted repository structure; it does not prove semantic
  completeness or generic Agent Skills portability.
- The audit did not execute every skill against representative projects, clients,
  CI providers, telemetry systems, or production environments.
- Client compatibility claims reflect official documentation checked on
  2026-09-22, not every installed client version or configuration.
- Capability classifications marked `+O` may change after the collection defines
  planning-versus-execution modes and operational capability names.

## Resolution tracking

When addressing a finding, update its status only after its acceptance criteria
and the relevant validation steps pass. Record the resolving change or commit
beside the finding rather than deleting the historical evidence.
