# Condensed prose audit — 2026-11-14

Reviewed skills individually in `AUDIT_TRACKING.md` order using
`condensed-prose-refactor` 1.3.0: balanced refactoring and condensation, with
meaning, uncertainty, obligations, exceptions, and protected literals preserved.
Each review covers the skill and its bundled files; executable examples and
machine-significant template content remain unchanged. Clear prose is retained
when an edit would be cosmetic. Editorial changes receive patch versions;
no-change reviews retain lifecycle metadata.

Each completed entry passed `skills-ref validate <canonical-directory>`
(skills-ref 0.1.0), Ritebook 0.1.63 `skills lint --root <temporary-scan-root>`
with an unchanged package copy below that root, protected-literal comparison for
edited prose, and `git diff --check`. Configured installed copies are synchronized
and checked byte for byte; Python skills have no configured installed mirror.
These are editorial and package checks, not target-host discovery, runtime, or
generated-application verification.

Final result: all 43 reviews completed in order; 20 skills received editorial
patch updates and 23 required no changes. Full-shelf Ritebook lint passed for
43 canonical and 33 installed skills. All 43 reference validations, 33 mirror
comparisons, 58 local resource links, Cline scaffold parity, protected-literal
checks against the original Git snapshot, and tracker/report coverage passed.
No executable, reference, or template file changed. Runtime workflows and
automatic skill discovery were not exercised.

The generated catalog was reviewed against all canonical names, paths, and
descriptions and still matches; its schema stores no skill version or content
digest. The catalog and lock remain byte-identical to the original Git snapshot.
The lock records published provenance and does not attest these local mirror
edits. No index refresh, install, push, or publication was performed. The final
worktree diff check passed. The user subsequently requested a local commit of
the completed audit; the commit includes canonical edits, installed mirrors,
the tracker, and this report.

## add-observability

- Version: 1.4.2 (patch editorial update).
- Findings and action: Compressed the opening and signal-selection instruction by removing setup phrases. Retained diagnostic and operational scope, the smallest safe signal set, all verification states, and the reference's counting and data-handling distinctions.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## api-and-interface-design

- Version: 1.4.2 (patch editorial update).
- Findings and action: Replaced indirect output wording with a direct instruction. Preserved every required review element, compatibility classification, consumer check, and boundary-specific prompt.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## author-agent-skill

- Version: 2.2.1 (patch editorial update).
- Findings and action: Tightened two indirect phrases in the scope and packaging steps. Retained format limits, shelf conventions, version rules, authorization boundaries, conditional references, and distinctions between package, paper, and runtime evidence.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## author-agents-config

- Version: 1.3.1 (patch editorial update).
- Findings and action: Simplified the canonical-authoring instruction without dropping its importance or ownership tests. Retained repeated fresh-setup conditions where they protect separate entry points; preserved dated client qualifications and exact Cline scaffolds.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## browser-runtime-verification

- Version: 1.2.0 (unchanged).
- Findings and action: No necessary prose change found. Scenario setup, visible interaction, partial accessibility evidence, and pass/fail/incomplete rules use direct language. Repeated runtime qualifications constrain different evidence types and remain useful.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## ci-cd-and-automation

- Version: 1.7.0 (unchanged).
- Findings and action: No necessary edit found. Ordered steps and the verification matrix already compress the CI workflow effectively. Preserved distinctions between local validation, provider execution, enforcement, stale deployments, and intentional rollback.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## code-review-and-quality

- Version: 1.5.0 (unchanged).
- Findings and action: No necessary edit found. The workflow separates actionable findings, unresolved concerns, severity, and blocking status clearly. Supporting checklists and report template are concise and retain the limits of static and measured evidence.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## code-simplification

- Version: 1.1.7 (patch editorial update).
- Findings and action: Removed a redundant incremental-application sentence immediately beneath the one-change-at-a-time heading and before its concrete sequence. Preserved all behavior checks, blocked-execution rules, examples, and validation steps.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## context-engineering

- Version: 1.2.1 (patch editorial update).
- Findings and action: Made the context-packet deliverable a direct instruction and removed an empty introduction to trust classification. Kept provenance, scope, stale-evidence, redaction, and unresolved-decision requirements intact.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## conventional-commits

- Version: 1.1.4 (unchanged).
- Findings and action: No necessary edit found. Syntax requirements, optional components, project-specific conventions, and conditional release effects are stated distinctly. Repeated syntax in examples and the final checklist supports writing and review without changing normative force.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## debugging-and-error-recovery

- Version: 1.3.2 (patch editorial update).
- Findings and action: Compressed the unavailable-reproduction fallback by replacing a repeated environment/access enumeration and indirect artifact wording. Preserved useful-only triage, missing-access reporting, unresolved status, and the prohibition on claiming recovery without evidence.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## deprecation-and-migration

- Version: 1.4.1 (patch editorial update).
- Findings and action: Removed a generic exhortation before the concrete usage-evidence sources. Retained the evidence requirement, source list, observation limits, mixed-version safeguards, and all removal gates.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## documentation-and-adrs

- Version: 1.3.4 (patch editorial update).
- Findings and action: Condensed the opening's repeated description of its routing role. Preserved the choice of no documentation, reader/purpose/surface decisions, conditional specialized handoffs, and missing-skill fallback.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## doubt-driven-development

- Version: 1.3.1 (unchanged).
- Findings and action: No necessary prose edit found. The compact review loop and orchestration reference distinguish artifact, contract, findings, uncertainty, reconciliation, and stopping conditions. Preserved the prompt examples and degraded self-review label.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## frontend-ui-engineering

- Version: 1.4.2 (patch editorial update).
- Findings and action: Compressed framework-neutral scope wording. Preserved the frontend focus, all listed concerns, framework/library/tool exclusions, browser evidence requirement, and accessibility reference.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## git-workflow-and-versioning

- Version: 1.3.3 (unchanged).
- Findings and action: No necessary edit found. Commands and examples are compact, and atomicity, authorization, conflict handling, and local-versus-remote state remain explicit. Retained the handoff template unchanged as protected example content.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## hexagonal-vertical-slices

- Version: 1.2.2 (patch editorial update).
- Findings and action: Replaced indirect deliverable wording with a direct instruction. Retained ownership, contracts, dependency direction, consistency/failure semantics, conditional refactoring steps, and verification evidence; detailed architectural distinctions need no condensation.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## idea-refine

- Version: 2.0.2 (patch editorial update).
- Findings and action: Replaced an awkward nominal phrase with a direct request for specific reasons. Retained the collaborative sequence, numerical ranges, confirmation conditions, helper contract, and calibration examples.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## incremental-implementation

- Version: 2.3.1 (patch editorial update).
- Findings and action: Split the dense overview into two paragraphs at the transition from test-first execution to alternative increment types. Tightened the paragraph's setup while preserving every step, conditional, classification, and working-state obligation.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## interview-me

- Version: 2.1.1 (unchanged).
- Findings and action: No necessary prose edit found. Repetition across path selection, turn structures, loop, and examples serves separate execution and calibration needs. Preserved readiness levels, single-question rules, explicit confirmation, and distinctions between evidence, guesses, and assumptions.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## performance-optimization

- Version: 1.6.2 (patch editorial update).
- Findings and action: Condensed the circular opening about guessing into one causal sentence. Retained its warning about premature complexity, the full measurement loop, all evidence requirements, and dated web-metric qualifications.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## planning-and-task-breakdown

- Version: 2.2.2 (unchanged).
- Findings and action: No necessary prose edit found. The workflow and template distinguish requirements, acceptance, verification, dependencies, readiness, and progress ownership precisely. Retained repeated canonical-checkbox rules because they guard separate authoring and maintenance steps.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## review-implementation-plan

- Version: 1.3.4 (patch editorial update).
- Findings and action: Simplified the nested availability/selection wording for prerequisite skills. Preserved optional availability, distinct requirement-versus-decomposition triggers, in-place/review-only behavior, readiness labels, and the boundary against implementation.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## run-local-quality-gate

- Version: 1.5.0 (unchanged).
- Findings and action: No necessary prose edit found. The short workflow makes discovery, check order, auto-fix scope, failure handling, and partial-versus-complete gate outcomes explicit without expendable explanation.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## security-and-hardening

- Version: 1.2.1 (unchanged).
- Findings and action: No necessary prose edit found. Boundary controls, approval scope, examples, and verification obligations are concrete. Repeated controls in the main workflow and focused checklist support different review depths; retained their qualifications and normative strength.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## shipping-and-launch

- Version: 1.6.6 (patch editorial update).
- Findings and action: Replaced motivational and contrastive opening language with the concrete launch conditions it introduced. Preserved safety, monitoring, recovery readiness, success criteria, staged exposure, and irreversible-change qualifications across the workflow and references.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## source-driven-development

- Version: 1.3.1 (patch editorial update).
- Findings and action: Made the source-traceable deliverable instruction direct. Preserved current/relevant/verifiable source conditions, version detection, authority hierarchy, conflict handling, and separate runtime evidence.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## spec-driven-development

- Version: 2.1.2 (unchanged).
- Findings and action: No necessary prose edit found. Requirements, proposals, accepted authority, implementation readiness, and completion are carefully separated. The workflow and template retain useful conditions and examples without disposable prose.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## test-driven-development

- Version: 1.4.1 (unchanged).
- Findings and action: No necessary prose edit found. RED/GREEN evidence, behavior-focused assertions, test scope, browser verification, and isolated side effects are stated directly. Retained calibration examples and the optional independent-review condition.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## update-project-docs

- Version: 1.4.0 (unchanged).
- Findings and action: No necessary prose edit found. The reader-centered sequence is concise, and configuration semantics, canonical ownership, conditional release notes, and safe example validation remain explicit.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## using-agnostic-software-development-skills

- Version: 2.5.6 (patch editorial update).
- Findings and action: Removed repeated step setup and a scope metaphor that restated an existing instruction. Kept the routing tree, lifecycle table, concrete operating rules, examples, authorization transfer, and conditional activation unchanged.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## write-adr

- Version: 1.2.3 (unchanged).
- Findings and action: No necessary prose edit found. Numbering, naming, collision checks, local conventions, default status, and index maintenance are concise and actionable. Kept literal templates and the distinctions between proposed, accepted, deprecated, and superseded decisions.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.

## add-hexagonal-feature

- Version: 1.3.1 (patch editorial update).
- Findings and action: Condensed the port-selection handoff paragraph by removing repeated scope setup. Preserved when to use the specialized procedure, boundary-selection responsibility, and inbound/application/outbound dependency rules.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## bootstrap-python-app

- Version: 2.1.0 (unchanged).
- Findings and action: No necessary prose edit found. The detailed instructions explain non-obvious input, layout, CLI, coverage, release opt-in, and installed-wheel constraints. Reviewed all six assets and retained commands, pinned values, template tokens, comments, and CI behavior unchanged.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## python-add-adapter

- Version: 1.2.1 (patch editorial update).
- Findings and action: Shortened the branch-selection instruction. Preserved adapter direction, prerequisite routing, inbound and outbound responsibilities, semantic conformance, resource lifecycle, and real enforcement verification.
- Scope: all bundled files reviewed; edited SKILL.md.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## python-add-env-settings-adapter

- Version: 1.2.0 (unchanged).
- Findings and action: No necessary prose edit found. Main instructions and ten assets clearly distinguish parsing, application defaults, precedence, blank rejection, representation redaction, and explicit serialization risks. Preserved executable templates and synthetic values exactly.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## python-add-port

- Version: 1.2.0 (unchanged).
- Findings and action: No necessary prose edit found. Port direction, call flow versus imports, structural typing versus runtime semantics, optional direct tests, and related handoffs are explicit. Kept literal examples and path conventions unchanged.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## python-build-extensible-cli

- Version: 1.2.1 (unchanged).
- Findings and action: No necessary prose edit found. Ownership, parser lifecycle, namespace isolation, mandatory version behavior, stream borrowing, and entrypoint equivalence are precise. Main and reference material serve workflow and implementation roles; retained examples and strength distinctions.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## split-python-module

- Version: 1.2.0 (unchanged).
- Findings and action: No necessary prose edit found. The short sequence gives concrete split criteria and protects public imports, dynamic names, serialization, monkeypatching, and trusted-fixture boundaries without redundant setup.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## using-python-software-development-skills

- Version: 3.0.1 (unchanged).
- Findings and action: No necessary prose edit found. The compact catalog distinguishes general workflow routing from Python mechanics and carries scope, contracts, decisions, and integration evidence across handoffs. Validation ownership and missing-tool limits are clear.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## write-pytest-tests

- Version: 1.2.0 (unchanged).
- Findings and action: No necessary prose edit found. Short instructions and examples cover pytest-native structure, contract-level assertions, deterministic isolation, optional plugins, and meaningful doubles. Preserved all examples and practical qualifications.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## write-python-docstrings

- Version: 1.1.3 (unchanged).
- Findings and action: No necessary prose edit found. The workflow already favors concise summaries, useful Google-style sections, non-obvious contracts, and validation beside implementation. Resource lifetime, cancellation, omission, and exception distinctions remain precise.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; no configured mirror.

## condensed-prose-refactor

- Version: 1.3.0 (unchanged).
- Findings and action: No necessary prose edit found. Priorities, silent constraint ledger, bidirectional fidelity comparison, protected literals, uncertainty, relational tone, and no-change option are precise. Reviewed the rhetorical reference without applying its author associations; retained calibration examples and the Kafka exclusion.
- Scope: all bundled files reviewed; no edits required.
- Checks: reference validator, focused Ritebook lint, protected literals and diff; installed mirror parity.
