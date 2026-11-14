# Agent Skill authoring audit — 2026-11-14

Reviewed each of the 43 entries in `AUDIT_TRACKING.md` order using
`author-agent-skill` 2.2.0. Scope: activation, inputs, executable instructions,
portable packaging, progressive disclosure, resource/caller consistency, lifecycle
metadata, validation readiness, and completion evidence. Each entry includes all
bundled files; no-change results retain existing versions and verification dates.

Format and authoring baseline: [Agent Skills specification](https://agentskills.io/specification)
and [authoring guidance](https://agentskills.io/skill-creation/best-practices),
consulted on the review date. Existing callers and catalog routes were inspected;
unchanged public names, resource paths, and output contracts require no migration.

Every completed entry passed `skills-ref validate <canonical-directory>`
(skills-ref 0.1.0) and Ritebook 0.1.63 `skills lint --root <temporary-scan-root>`
with an unchanged copy of that skill below the scan root. Cached executables were
used directly because uv's default cache is outside writable roots. Each entry
also passed `git diff --check` and configured mirror parity. Walkthroughs below
are paper review evidence, not automatic discovery or target-host runtime tests.
Actual helper/template execution is identified separately. External services,
production workflows, and complete generated Python applications were not run.
Final aggregate checks: Ritebook lint across all 43 canonical skills, reference
validation for all 43, ordered tracker/report coverage, local resource links,
33 installed mirrors, Cline scaffold parity, and diff checks passed. Eighteen
skills changed with lifecycle updates; 25 required no edits.

The checked-in catalog still matches all canonical names, paths, and descriptions;
its schema contains no skill version or content digest. It was not regenerated.
The lock retains its recorded published revision and does not attest these local
mirror edits. Publication and reinstall/provenance refresh remain separate,
unrequested operations. No index, lock, publication, install, or push changes are
included; the user requested a local commit after the reviews.

## add-observability

- Version: 1.4.1.
- Findings and action: No authoring defect found. Discoverable operational scope, missing-access fallback, optional signal-specific reference, and evidence labels are consistent; retained instructions and metadata.
- Paper walkthrough: A local retry metric follows attempt versus operation semantics; a missing backend yields verification incomplete; a measured bottleneck routes to performance-optimization.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## api-and-interface-design

- Version: 1.4.1.
- Findings and action: The conditional boundary checklist was named only as code. Added a relative Markdown link at its existing read point so hosts can resolve the resource directly; patch version 1.4.1, no interface migration.
- Paper walkthrough: A CLI contract review loads only the CLI checklist; a private helper refactor stays outside the trigger; design-only work returns a verification plan.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## author-agent-skill

- Version: 2.2.0.
- Findings and action: No defect found against the current primary specification and authoring guidance. Portable fields, shelf-only conventions, safe helper review, conditional handoffs, validation limits, and copy ownership are explicit; retained 2.2.0.
- Paper walkthrough: A review-only request returns findings without edits; missing validators require named manual checks; an unavailable optional skill does not trigger invented instructions.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## author-agents-config

- Version: 1.3.0.
- Findings and action: No authoring defect found across the workflow, README, three references, and six scaffold files. Conditional loading, init/update/sync/audit boundaries, fresh-setup eligibility, and client verification levels agree. Retained dated compatibility notes without claiming a new runtime compatibility review; Cline scaffold parity passed.
- Paper walkthrough: An existing AGENTS.md prevents fresh scaffold replacement; an audit stays read-only; unavailable client loading yields static evidence and an explicit runtime gap.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## browser-runtime-verification

- Version: 1.2.0.
- Findings and action: No authoring defect found. Scenario inputs, capability checks, bounded waits, safe setup, scope-preserving replay, evidence capture, and pass/fail/incomplete rules form a self-contained workflow.
- Paper walkthrough: A changed dialog needs visual and keyboard checks; missing network capture leaves an applicable check unverified; a backend-only change does not activate this skill.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## ci-cd-and-automation

- Version: 1.7.0.
- Findings and action: No authoring defect found. Portable provider-neutral steps, version-sensitive documentation checks, missing-access outcomes, bounded mutations, and execution-versus-enforcement evidence are explicit; no packaged helper dependency.
- Paper walkthrough: A local workflow edit can finish with provider execution unverified; an unexpected skipped required job cannot pass; audit scope does not authorize deployment.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## code-review-and-quality

- Version: 1.5.0.
- Findings and action: No authoring defect found. Three conditionally linked references agree with scope, severity, requested-format precedence, attribution, and verdict rules. Optional template does not force file creation or override a caller schema.
- Paper walkthrough: A findings-only request retains its format; missing evidence about material risk defers judgment; a confirmed blocker requests changes; a check-only request routes to the local gate.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## code-simplification

- Version: 1.1.6.
- Findings and action: No authoring defect found. Narrow refactor trigger, preservation contract, validation prerequisite/fallback, and examples are consistent and self-contained; no external resource prerequisites.
- Paper walkthrough: Guard-clause conversion preserves validation order and exceptions; an untested dynamic registration name is retained; unavailable checks yield an explicitly unapplied proposal.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## context-engineering

- Version: 1.2.0.
- Findings and action: No authoring defect found. Context packet makes workspace state, source provenance, verification currency, and open questions explicit; templates use generic placeholders and require no bundled tooling.
- Paper walkthrough: A task switch refreshes only relevant sources; a stale passing log stays attributed to its revision; conflicting requirements are surfaced without granting authority to external text.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## conventional-commits

- Version: 1.1.4.
- Findings and action: The named v1.0.0 standard lacked a resolvable source. Linked the official versioned specification and checked the documented syntax against it; patch 1.1.4 preserves input and message output contracts.
- Paper walkthrough: A staged-message request excludes unstaged changes; missing diff evidence produces a provisional draft; a valid breaking footer is accepted without creating a commit.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## debugging-and-error-recovery

- Version: 1.3.1.
- Findings and action: Blanket confirmation for every diagnostic command or URL could stall already-authorized inspection. Replaced it with independent destination/action review against diagnostic scope and existing authorization; patch 1.3.1 retains the untrusted-data boundary.
- Paper walkthrough: An error-linked documentation page can be inspected within scope; an embedded upload command gains no authority; a missing runtime still yields unresolved triage rather than a recovery claim.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## deprecation-and-migration

- Version: 1.4.0.
- Findings and action: No authoring defect found. Planning, execution, and removal outcomes are separated; usage evidence classifications, bounded transitions, and the notice template supply executable decision points without hidden tools.
- Paper walkthrough: An offline public consumer prevents proven-zero claims; a plan remains planning-only; a shadow migration cannot duplicate writes; missing execution access blocks only the affected phase.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## documentation-and-adrs

- Version: 1.3.3.
- Findings and action: No authoring defect found. Routing-only purpose, concrete handoff inputs, unavailable-skill fallback, canonical artifact ownership, and no-file advice outcome are explicit; direct specialized routes remain available.
- Paper walkthrough: A documentation-choice request returns the smallest justified artifact; missing write-adr yields a bounded brief; an already-clear README update routes directly to update-project-docs.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## doubt-driven-development

- Version: 1.3.1.
- Findings and action: Orchestration guidance had only a code-form path. Added a relative link and concrete read condition; patch 1.3.1 preserves the optional reviewer capability, degraded fallback, bounded cycles, and artifact/contract handoff.
- Paper walkthrough: A non-trivial migration decision receives bounded issues-first review; a mechanical rename skips it; missing independent review is disclosed as degraded self-review.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## frontend-ui-engineering

- Version: 1.4.1.
- Findings and action: The accessibility reference was named only as code. Added a relative link and interactive-change read condition; patch 1.4.1 preserves the browser-evidence requirement, review-only fallback, and existing component contracts.
- Paper walkthrough: An interactive form loads the focused accessibility reference; missing browser execution remains disclosed; backend-only work stays outside the trigger.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## git-workflow-and-versioning

- Version: 1.3.3.
- Findings and action: No authoring defect found. Provider-neutral commands, scoped Git authorization, staged-state inspection, conflict decisions, optional worktree examples, and repository-state handoff are explicit; placeholders are clearly examples.
- Paper walkthrough: A handoff-only request reports the unstaged diff without committing; an authorized conflict repair inspects both sides; an ambiguous shared-history rewrite stops for the missing scope decision.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## hexagonal-vertical-slices

- Version: 1.2.1.
- Findings and action: No authoring defect found. Standalone architecture workflow stays below recommended size limits, labels folder shapes as examples, defines scope/ownership/outputs, and keeps implementation mechanics in conditional related workflows.
- Paper walkthrough: A boundary review uses actual imports rather than folder names; a small slice can omit interfaces and empty layers; design-only output contains a concrete verification plan.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## idea-refine

- Version: 2.0.1.
- Findings and action: References and helper were only code-form paths; examples had no concrete read condition. Added direct resource links and conditional guidance, patch 2.0.1. Executed the inspected unchanged helper in a disposable workspace: default/empty path, spaces/Unicode, JSON escaping, repeat preservation, collision failure, and excess arguments all passed.
- Paper walkthrough: A vague concept explores alternatives and retains excluded scope; clear implementation requests skip refinement; missing Python uses the documented manual directory fallback without blocking the interview.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## incremental-implementation

- Version: 2.3.0.
- Findings and action: No authoring defect found. Slice types, TDD applicability, non-behavioral validation, optional skill use, checkpoint alternatives, and incomplete-execution outcomes are explicit; the standalone workflow is within size recommendations.
- Paper walkthrough: A prose-only change skips RED and uses focused review; a storage-only increment is contract-first rather than vertical; an unavailable required runtime leaves that increment incomplete.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## interview-me

- Version: 2.1.1.
- Findings and action: The medium example started light despite omitting the underlying outcome, which the main high-risk rule requires to start full. Made its daily-triage outcome explicit and narrowed the first question to triage priority; preserved escalation when a second audience appears. Added the conditional examples link; patch 2.1.1.
- Paper walkthrough: An outcome-free dashboard request starts full; a known daily-triage outcome with one priority gap can start light; adding product-manager reporting escalates to full. Explicit interview and confirmation behavior remain unchanged.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## performance-optimization

- Version: 1.6.1.
- Findings and action: Three supporting references were named only as code. Converted their existing conditional read points to relative Markdown links; patch 1.6.1 retains measured-workload scope and dated web-threshold qualifications without asserting newly verified browser policy.
- Paper walkthrough: A batch bottleneck loads neutral patterns; browser latency loads web guidance only when relevant; missing measurements produce a labeled proposal without an improvement claim.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## planning-and-task-breakdown

- Version: 2.2.2.
- Findings and action: No authoring defect found. Linked plan asset matches canonical-checkbox ownership, requirement coverage, dependencies, readiness, unknown validation, and continuation rules. Template placeholders and optional sections are clearly marked.
- Paper walkthrough: A small clear change uses an inline list; an unknown check creates bounded discovery and prevents verified completion; ready independent tasks continue under existing authorization.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## review-implementation-plan

- Version: 1.3.3.
- Findings and action: No authoring defect found. Existing-file and inline inputs, review-only precedence, readiness semantics, optional upstream skills, and bounded plan-editing output are explicit; no invented filename or implementation permission.
- Paper walkthrough: An inline plan stays inline; missing plan input is requested; downstream blocking questions prevent recommending affected tasks while independent readiness remains visible.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## run-local-quality-gate

- Version: 1.5.0.
- Findings and action: No authoring defect found. Discovery-first commands, installed-tool execution, safe setup, check-only review mode, failure handling, and partial versus full gate evidence are self-contained and portable.
- Paper walkthrough: A review-only aggregate that writes files requires a check-only alternative; unavailable setup leaves the gate incomplete; unrelated failures are reported without opportunistic repair.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## security-and-hardening

- Version: 1.2.1.
- Findings and action: The focused companion checklist had only a code-form path. Added a direct relative link, patch 1.2.1; retained portable scope, per-boundary guidance, rejected-path verification, and explicit design/review/implementation outcomes.
- Paper walkthrough: A protected mutation includes denied-path checks; unavailable scanners remain skipped evidence; an existing authorization permits scoped hardening without granting unrelated integration changes.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## shipping-and-launch

- Version: 1.6.5.
- Findings and action: Five conditional readiness/example references were named only as code. Added direct relative links at existing read points, patch 1.6.5; all reference checklists and illustrative rollout/recovery templates remain consistent with risk-based selection.
- Paper walkthrough: A planning-only request does not deploy; a small irreversible release can choose documented containment rather than a flag; a missed recovery threshold stops rollout instead of waiting out the window.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## source-driven-development

- Version: 1.3.0.
- Findings and action: No authoring defect found. Narrow source-sensitive trigger, version discovery, source hierarchy, precise rule/citation templates, unavailable-source fallback, and documented-versus-observed distinction are coherent and self-contained.
- Paper walkthrough: An installed-version API question uses matching primary evidence; a newer example does not silently upgrade the project; absent official guidance leaves the detail explicitly unverified.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## spec-driven-development

- Version: 2.1.2.
- Findings and action: No authoring defect found. Linked specification asset matches acceptance status, requirement/plan separation, stable IDs, explicit unknowns, prior authorization, and next-step semantics. No generic approval gate is introduced.
- Paper walkthrough: A precise bug fix skips a new spec; accepted requirements can coexist with an unresolved implementation dependency; a material unaccepted proposal preserves the accepted baseline.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## test-driven-development

- Version: 1.4.1.
- Findings and action: Browser guidance required approval for all extracted links, conflicting with the linked verification workflow allowing authorized ordinary navigation. Aligned destination checks with the test scenario and existing authorization, preserving secret-access restrictions; linked the testing-patterns resource. Patch 1.4.1.
- Paper walkthrough: A local page navigation needed for the authorized test can proceed after inspection; hostile page commands remain data; a documentation-only change skips TDD and receives relevant validation.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## update-project-docs

- Version: 1.4.0.
- Findings and action: No authoring defect found. Reader-visible trigger, canonical source ownership, scoped sections, real configuration semantics, safe example execution, and release-note fallback define a portable standalone workflow.
- Paper walkthrough: A generated configuration page is updated at its source; unknown defaults are checked rather than invented; a non-reader-visible edit can justify no durable documentation change.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## using-agnostic-software-development-skills

- Version: 2.5.5.
- Findings and action: The assumption prompt treated lack of correction as permission to proceed, conflicting with routed requirement workflows. Replaced it with basis/impact/resolution fields, distinguished bounded working assumptions from required decisions, and limited pauses to dependent work. Scoped operating guidance to current authority and linked the catalog reference; patch 2.5.5.
- Paper walkthrough: A precise authorized fix stays direct; a material unresolved product decision cannot be accepted by silence; an unrelated ready task can continue; listed destinations do not activate recursively.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## write-adr

- Version: 1.2.3.
- Findings and action: No authoring defect found. Local directory/template conventions, sequential numbering, collision and retry handling, status selection, index preservation, and final link checks are explicit; examples use portable placeholders.
- Paper walkthrough: A concurrent number claim triggers renumbering rather than overwrite; an agreed decision can be accepted; unspecified status stays proposed; an existing non-table index keeps its format.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.

## add-hexagonal-feature

- Version: 1.3.0.
- Findings and action: The workflow assumed a standard layout without an initial source/working-tree inspection or missing-specialist path. Added package/path discovery, explicit prerequisite and handoff gaps, and clarified that a selected TDD workflow governs ordering inside each behavior increment. Compatible guidance addition, version 1.3.0.
- Paper walkthrough: An existing differently named import package is discovered before writing paths; a missing port skill leaves that procedure incomplete; a selected TDD cycle starts before the corresponding service implementation.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## bootstrap-python-app

- Version: 2.1.0.
- Findings and action: Six bundled templates lacked direct resource links, and commands changed into the target project without explicitly locating skill assets. Added asset links, skill-relative resolution, and missing-tool/runtime/dependency evidence limits; compatible guidance version 2.1.0. Rendered all six assets with safe fixture values: token check, TOML/YAML/Python parsing, and Make quality dry run passed.
- Paper walkthrough: A fresh project resolves templates from the installed skill root after changing into the project; missing dependency access leaves validation unverified; an existing project requires explicit safe reconciliation. Full scaffold execution and provider release behavior were not exercised.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## python-add-adapter

- Version: 1.2.0.
- Findings and action: Added explicit repository/package inspection and missing-port/library/capability handling before branch execution. The previous instructions assumed prerequisites but did not define an incomplete outcome; compatible workflow guidance version 1.2.0. Inbound/outbound contracts and test locations remain unchanged.
- Paper walkthrough: An existing adapter pattern determines module placement; a missing port is reported before implementation; unit-tested mapping without runtime wiring is labeled incomplete integration.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## python-add-env-settings-adapter

- Version: 1.2.0.
- Findings and action: Templates import AppSettings through the DTO package, but the instructions made that export conditional without an alternative. Documented concrete-module imports when the package does not re-export DTOs, added ten direct asset links and installed-root resolution; compatible guidance version 1.2.0. All seven Python assets parse. The inspected validation environment lacks pydantic-settings, so the template test suite was not run.
- Paper walkthrough: A project without DTO re-exports adjusts both adapter and test imports; an existing configuration slice keeps ownership; missing runtime dependencies leave execution unverified rather than a settings-integration pass.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## python-add-port

- Version: 1.2.0.
- Findings and action: The interface workflow lacked an explicit initial project inspection and completion handoff. Added package/convention discovery, prerequisite handling, configured-check reporting, and missing-follow-up-skill limits; compatible guidance version 1.2.0. Port signatures and example paths are unchanged.
- Paper walkthrough: A project using ABC retains its established choice; unavailable type checks remain unverified; a new declaration with an unwritten adapter is reported as a boundary contract rather than an integrated use case.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## python-build-extensible-cli

- Version: 1.2.1.
- Findings and action: The conditional shell-pattern resource was unlinked and its sketch used Python 3.12 generic/type-alias syntax without naming that requirement. Linked it, declared the example version boundary and older-runtime adaptation without requiring upgrades; patch 1.2.1. AST checks confirmed the sketch accepts 3.12 syntax and rejects 3.11.
- Paper walkthrough: A one-feature script stays an ordinary adapter; a pre-3.12 project adapts typing syntax while retaining contracts; missing provider/runtime checks remain explicit verification gaps.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## split-python-module

- Version: 1.2.0.
- Findings and action: No authoring defect found. Narrow split trigger, preserved imports/dynamic references/serialization identity, safe fixtures, incremental moves, focused compatibility checks, and exact-results handoff are self-contained; no bundled resources.
- Paper walkthrough: A cohesive long file is retained; a re-export is not assumed to preserve monkeypatch behavior; untrusted pickle/plugin execution is excluded from compatibility checks.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## using-python-software-development-skills

- Version: 3.0.1.
- Findings and action: No authoring defect found. All nine destinations exist, matching triggers preserve complete-feature versus boundary/adapter scope, missing skills have a bounded path, and validation commands stay project-owned.
- Paper walkthrough: A single CLI adapter does not require the extensible shell; absent selected skills are reported; an undefined checker is a project gap rather than permission to install a new tool.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## write-pytest-tests

- Version: 1.2.0.
- Findings and action: No authoring defect found. Pytest prerequisite, convention discovery, deterministic setup, scenario examples, optional plugin boundary, stable exception assertions, and unavailable-validation reporting are explicit; no helper or resource dependency.
- Paper walkthrough: A text error assertion is used only for promised wording; inherited environment aliases and local dotenv are isolated; missing test execution is reported without claiming pass.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## write-python-docstrings

- Version: 1.1.3.
- Findings and action: No authoring defect found. Contract-driven trigger, implementation/caller inspection, conditional Google-style sections, lifecycle semantics, noise removal, and manual-check fallback are coherent without extra resources.
- Paper walkthrough: A trivial helper needs no ceremonial docstring; a borrowed iterator documents cleanup timing; absent automated documentation checks yield explicitly reported manual review.
- Checks: package validators, full resource and caller review, diff check; no configured installed mirror (Python collection).

## condensed-prose-refactor

- Version: 1.3.0.
- Findings and action: No authoring defect found. Distinct editing operations, source/input boundary, fidelity rules, protected literals, missing-source clarification, conditional rhetorical reference, and rewrite-only output are internally consistent. Calibration examples retain uncertainty and distinguish condensation from summary.
- Paper walkthrough: A request without source asks for the passage; a technical rewrite preserves commands and caveats; routine editing does not load author associations; a hard limit cannot silently erase required meaning.
- Checks: package validators, full resource and caller review, diff check; installed mirror byte parity.
