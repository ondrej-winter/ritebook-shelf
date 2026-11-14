# Condensed prose audit, second pass — 2026-11-14

Fresh review of all 43 skills in tracker order, starting from `d33b093`, using
`condensed-prose-refactor` 1.3.0 and the lifecycle conventions in
`author-agent-skill` 2.2.1. Scope includes every bundled file. Edit for clearer
structure, direct instructions, and useful compression while preserving claims,
conditions, uncertainty, obligations, examples, commands, and protected literals.
Retain clear prose and existing metadata when no edit is needed.

Each entry passes focused Ritebook 0.1.63 lint through a temporary parent scan
root, `skills-ref` 0.1.0 validation, diff checks, and configured mirror parity.
Edited prose also passes literal comparison against its pre-edit text; lifecycle
changes are confined to the real frontmatter. These are editorial/package checks,
not automatic discovery or runtime verification. Python skills have no configured
installed mirror. Previous review links and checked audit goals remain intact.

All 43 second-pass reviews completed in order: 18 skills received editorial
patch updates and 25 required no further changes. Changes remove duplicated
instructions, compress evidence and fallback descriptions, separate completion
states, and clarify mandatory versus recommended CLI requirements.

Final checks passed: Ritebook lint for 43 canonical and 33 installed skills,
43 reference validations, 33 complete mirror comparisons, 58 local resource
links, Cline scaffold parity, preserved literals, lifecycle metadata, and
43 ordered tracker/report entries. The tracker retains all original audit marks
and first-pass links. No executable or template asset changed.

The generated catalog still matches canonical names, paths, and descriptions;
it stores no skill version or content digest. The catalog, lock, and first-pass
report remain byte-identical to `d33b093`. Published provenance does not attest
local mirror edits. The user subsequently requested a local commit of this pass.
No index refresh, install, push, or publication was performed. Runtime workflows
and automatic discovery remain unverified.

## add-observability

Condensed the missing-access outcome and consumer-migration instructions. Retained grounded local implementation, the incomplete-verification label, backend-delivery limits, migration ownership/timing/removal checks, and the prohibition on double-counting old and new signals. The telemetry reference needs no edit. Version 1.4.3 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## api-and-interface-design

Tightened value-ownership guidance while retaining all four representations, the condition for separating them, protected provider-owned fields, and the targeting/concurrency exception. Boundary-specific prompts remain clear. Version 1.4.3 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## author-agent-skill

Compressed the interface-change review and verification-date explanation. Retained the public-interface inventory, caller migration check, exact metadata rules, real review time, and the limit that a timestamp cannot certify host runtime behavior. Version 2.2.2 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## author-agents-config

No further edit needed. The workflow, README, three references, and six scaffolds keep ownership, fresh-setup eligibility, scope, and client-loading evidence explicit. Repeated preservation rules protect independently read sections; shortening them would hide material conditions. Version 1.3.1 (unchanged). Focused checks passed; installed mirror matches.

## browser-runtime-verification

Compressed the unavailable-browser branch and warning-analysis paragraph. Preserved useful scenario planning, partial checks, runtime-unverified labels, established sign-in, and the distinction between expected diagnostics and unexplained warnings. Version 1.2.1 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## ci-cd-and-automation

No further edit needed. Each CI/CD section addresses a distinct concern: gate enforcement, privilege, reproducibility, promotion, interruption, bounded writes, and evidence. The local/provider distinction and failure-path matrix are already direct; additional compression would mostly change style. Version 1.7.0 (unchanged). Focused checks passed; installed mirror matches.

## code-review-and-quality

Compressed evidence attribution and the no-findings handoff. Preserved the four evidence sources, failure attribution, unavailable-tool outcome, scope/risk limits, and owner-only risk acceptance. Supporting checklists and report template remain unchanged. Version 1.5.1 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## code-simplification

Compressed the execution boundary without relaxing it. A useful review or proposed diff remains the only fallback when checks cannot run, retains both unverified labels, and cannot be applied or reported as behavior-preserving. Code examples and staged refactoring steps are unchanged. Version 1.1.8 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## context-engineering

No further edit needed. Context layers, trust provenance, source-backed constraints, stale verification, and redaction are concise. Repeated focus guidance appears at distinct loading and file-selection decisions and still earns its place. Version 1.2.1 (unchanged). Focused checks passed; installed mirror matches.

## conventional-commits

No further edit needed. Repeated syntax rules support drafting, examples, and final validation rather than add empty emphasis. Preserved optional sections, exact separators, breaking-change alternatives, and conditional release implications. Version 1.1.4 (unchanged). Focused checks passed; installed mirror matches.

## debugging-and-error-recovery

Separated completed recovery from the missing-reproduction-access fallback and repaired the awkward semicolon break left by the first pass. Preserved every completion requirement, useful-only triage, evidence capture, unresolved/runtime-unverified labels, and blocked-fix condition. Version 1.3.3 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## deprecation-and-migration

Recast the dense completion-state paragraph as three parallel state definitions followed by the execution blocker. Kept the plan's qualified completion rule, every required field, per-consumer migration verification, removal approvals/cleanup, and the distinction between planned and executed work. Version 1.4.2 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## documentation-and-adrs

No further edit needed. Reader/purpose selection, artifact ownership, conditional handoffs, and missing-skill writing briefs remain compact. Contract, rationale, usage, and runbook responsibilities stay distinct; the first pass already removed the redundant opening. Version 1.3.4 (unchanged). Focused checks passed; installed mirror matches.

## doubt-driven-development

No further edit needed. The short workflow and orchestration reference distinguish claim, artifact, contract, review data, accepted trade-offs, and bounded iteration. Preserved the prompt and stopping conditions; no reviewer was invoked for this editorial audit. Version 1.3.1 (unchanged). Focused checks passed; installed mirror matches.

## frontend-ui-engineering

Condensed the browser-evidence boundary and split the fallback into its own paragraph. Retained repository access, manual/automated evidence for every changed UI concern, useful-only design/review, both outcome labels, and the prohibition on applying or completing unverified implementation. Version 1.4.3 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## git-workflow-and-versioning

No further edit needed. Scope, atomicity, local conventions, conflict handling, authorization, and observed remote state are already concise. Kept command examples and the distinction between committed, published, and CI-verified work. Version 1.3.3 (unchanged). Focused checks passed; installed mirror matches.

## hexagonal-vertical-slices

No further edit needed. Vocabulary, allowed/forbidden dependencies, responsibility assignment, and the review checklist serve different decisions. Preserved optional interfaces, small-slice exceptions, application authorization/atomicity, cross-slice consistency, and migration safeguards. Version 1.2.2 (unchanged). Focused checks passed; installed mirror matches.

## idea-refine

No further edit needed. The main workflow, three references, and helper retain concrete variation counts, convergence criteria, assumption tests, confirmation conditions, and exact helper outcomes. Examples carry domain reasoning; trimming them would turn condensation into summary. Version 2.0.2 (unchanged). Focused checks passed; installed mirror matches.

## incremental-implementation

Removed a repeated green-baseline sentence already specified in step 2 and corrected subject–verb agreement in the simplicity rule. Preserved the non-behavioral RED exception, evidence requirement, slice classifications, numerical guidance, and all examples. Version 2.3.2 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## interview-me

Condensed the full-path presentation rule while retaining every expansion trigger and the exception for expected readiness changes. Kept the operating model, all output templates, confirmation rules, and calibration examples intact. Version 2.1.2 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## performance-optimization

No further edit needed. Measurement conditions, noisy-result summaries, load-generator limits, failed-optimization disposition, and cache/consumer contracts are already precise. Retained all three references, literal examples, and the dated Web Vitals qualifications without asserting a new compatibility review. Version 1.6.2 (unchanged). Focused checks passed; installed mirror matches.

## planning-and-task-breakdown

No further edit needed. The plan workflow and template distinguish acceptance from verification, known commands from execution, readiness from permission, and canonical progress from summaries. Repetition protects those boundaries across creation and maintenance; all examples and template fields remain useful. Version 2.2.2 (unchanged). Focused checks passed; installed mirror matches.

## review-implementation-plan

Consolidated the repeated handoff list into the existing Expected output format, retaining the step-specific owner/audience, blockers, and nonblocking backlog details. Requirements, preserved progress, readiness, and review-only boundaries are unchanged. Version 1.3.5 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## run-local-quality-gate

No further edit needed. The workflow is compact and separates command discovery, authorized auto-fixes, review-only execution, failure handling, and partial gate evidence. Repeated unavailable-check wording constrains distinct steps rather than repeat empty setup. Version 1.5.0 (unchanged). Focused checks passed; installed mirror matches.

## security-and-hardening

No further edit needed. Main instructions and the focused checklist preserve specific controls, exceptions, authorization scope, and required evidence. Repeated security verbs carry normative force; shortening them would risk weakening requirements rather than improve clarity. Version 1.2.1 (unchanged). Focused checks passed; installed mirror matches.

## shipping-and-launch

Separated plan completion from executed launch and removed repeated outcome setup. Preserved every plan field, planning-only/not-deployed labels, authorization/access/post-launch evidence, and all blocked-deployment conditions. Five references and their templates remain unchanged. Version 1.6.7 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## source-driven-development

No further edit needed. Source selection, version scope, authority, conflict handling, and citations are already direct. The hierarchy, concrete records, and runtime-evidence distinction preserve useful detail without padding. Version 1.3.1 (unchanged). Focused checks passed; installed mirror matches.

## spec-driven-development

No further edit needed. Specification and template keep accepted authority, proposed requirements, bounded assumptions, validation pass conditions, readiness, and execution permission separate. The existing prose is dense with necessary distinctions rather than repetition to remove. Version 2.1.2 (unchanged). Focused checks passed; installed mirror matches.

## test-driven-development

Merged the testing reference's two overlapping introductory sentences. Retained its loading condition, before/during-implementation scope, narrowest-pattern rule, and focused/broader check reporting. Main workflow, examples, and execution requirements are unchanged. Version 1.4.2 (patch update). Edited references/testing-patterns.md. Focused checks passed; installed mirror matches.

## update-project-docs

No further edit needed. The seven-step workflow is already concise, with concrete reader-facing changes, canonical surfaces, configuration semantics, safe examples, release notes, and validation. Each repeated documentation category serves a different step. Version 1.4.0 (unchanged). Focused checks passed; installed mirror matches.

## using-agnostic-software-development-skills

Condensed the assumptions warning into a direct causal statement and action. Retained its claim about the most common failure mode, prohibition on silently filling requirements, and cost-of-rework rationale. Routing trees, examples, operating rules, and the catalog reference remain intact. Version 2.5.7 (patch update). Edited SKILL.md. Focused checks passed; installed mirror matches.

## write-adr

No further edit needed. Number allocation, last-moment collision checks, retry handling, local templates, status defaults, and index conventions are clear. Preserved every literal template and the difference between a proposed and already effective decision. Version 1.2.3 (unchanged). Focused checks passed; installed mirror matches.

## add-hexagonal-feature

No further edit needed. The feature workflow keeps the slice complete while delegating port and adapter mechanics. Conditional TDD, domain purity, boundary ownership, denied-path tests, and partial-increment labeling are explicit; the first-pass port paragraph reads clearly. Version 1.3.1 (unchanged). Focused checks passed; no configured mirror.

## bootstrap-python-app

Removed the smoke-test behavior summary duplicated by the immediately following, more precise CLI contract. Retained template instructions, metadata lookup, argv isolation, named-slice applicability, exact stdout/stderr/exit behavior, and all six executable assets unchanged. Version 2.1.1 (patch update). Edited SKILL.md. Focused checks passed; no configured mirror.

## python-add-adapter

Combined overlapping inbound result/exception mapping bullets. Retained the external-format mapping and caller-visible domain/application exception condition, with sensitive-output restrictions still adjacent. Ports, test boundaries, lifecycle, and outbound semantics are unchanged. Version 1.2.2 (patch update). Edited SKILL.md. Focused checks passed; no configured mirror.

## python-add-env-settings-adapter

No further edit needed. Reviewed the workflow and ten assets; precedence, aliases, blank values, working-directory lookup, representation versus serialization, safe tracebacks, and environment isolation each carry necessary distinctions. Kept template code, fixtures, and configuration prose unchanged. Version 1.2.0 (unchanged). Focused checks passed; no configured mirror.

## python-add-port

No further edit needed. Definitions, signature semantics, dependency direction, structural conformance, runtime limits, and related workflows are already direct. Preserved optional testing conditions and the distinction between a declaration and an integrated use case. Version 1.2.0 (unchanged). Focused checks passed; no configured mirror.

## python-build-extensible-cli

Separated mandatory version requirements from the recommended shell tasks, fixing the awkward 'should: Must' construction. Preserved the exact strength of both groups, both version-option literals, all other shell duties, and the implementation reference unchanged. Version 1.2.2 (patch update). Edited SKILL.md. Focused checks passed; no configured mirror.

## split-python-module

No further edit needed. Responsibility-based splitting, public imports, dynamic names, re-export limitations, monkeypatch targets, serialization direction, and safe fixtures are concise and distinct. Kept the step sequence and validation scope unchanged. Version 1.2.0 (unchanged). Focused checks passed; no configured mirror.

## using-python-software-development-skills

No further edit needed. The small catalog gives usable routes and explains which neighboring workflows differ. Conditional activation, handoff context, integration evidence, and project-owned validation commands remain explicit without excess prose. Version 3.0.1 (unchanged). Focused checks passed; no configured mirror.

## write-pytest-tests

No further edit needed. Test names, Arrange/Act/Assert, parametrization, fixtures, factories, patch targets, and behavioral assertions each have a focused example. Retained contract-sensitive exception matching, deterministic isolation, and synthetic-data cautions. Version 1.2.0 (unchanged). Focused checks passed; no configured mirror.

## write-python-docstrings

No further edit needed. The short workflow already removes noise while preserving caller contracts, intentional exceptions, resource lifetime, cancellation, and omission/default distinctions. Google-style sections and examples remain conditional and concise. Version 1.1.3 (unchanged). Focused checks passed; no configured mirror.

## condensed-prose-refactor

No further edit needed. The workflow, fidelity rules, output contract, calibration examples, and rhetorical reference agree. Preserved no-minimum-reduction/no-change guidance, protected literals, relational conditions, author-technique limits, and the Kafka exclusion. Version 1.3.0 (unchanged). Focused checks passed; installed mirror matches.
