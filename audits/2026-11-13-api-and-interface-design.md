# Skill interface audit — 2026-11-13

Reviewed in `AUDIT_TRACKING.md` order with `api-and-interface-design`.
The public boundary is each skill's activation, required inputs, workflow,
resources, side effects, and handoff to its calling agent or adjacent skills.
Canonical instructions and bundled resources are the contract source; routing
catalogs and cross-references are consumer evidence. Classification below is
based on these documented consumers; automatic discovery and target-host runtime
behavior are unverified. Entries include paper walkthroughs, with actual helper and
rendered-template execution identified separately. No automatic agent-discovery
claim is made. Changes clarify existing obligations without renaming skills,
resources, or required output formats. No migration is required unless noted.

Every entry passed focused Ritebook 0.1.63 lint and skills-ref 0.1.0 validation.
Existing configured mirrors were synchronized and checked byte for byte; Python
skills are not selected by `ritebook.toml` and have no installed mirror.
Catalog and lock state are inspected separately without regenerating provenance.

## add-observability

- Version: 1.4.1.
- Finding and change: Telemetry schema changes lacked an explicit consumer migration decision. Added query and alert compatibility review, transition ownership, and double-counting avoidance.
- Consumer walkthrough: A label rename now requires checking dependent queries and naming a transition; unchanged local logging retains its existing path.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## api-and-interface-design

- Version: 1.3.4.
- Finding and change: Cancellation could be mistaken for provider rollback; stream resource ownership was implicit. Clarified cancellation versus waiting, outcome reconciliation, backpressure, and cleanup.
- Consumer walkthrough: A timed-out write must reconcile its final outcome before retry; a subscription consumer must know who closes the stream.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## author-agent-skill

- Version: 2.1.1.
- Finding and change: Versioning rules did not explicitly connect workflow changes to skill consumers. Added review of activation, inputs, resource paths, helper arguments, outputs, and migration obligations.
- Consumer walkthrough: Renaming a bundled helper now requires checking invocations and examples; a prose clarification keeps the existing activation and output contract.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## author-agents-config

- Version: 1.3.0.
- Finding and change: No interface defect found. Mode table, canonical ownership, client capability checks, scoped loading, idempotent reconciliation, and explicit verification levels already cover the boundary. Reviewed README, references, and every scaffold asset; retained dated compatibility qualifications.
- Consumer walkthrough: An audit remains read-only; sync with a missing canonical source reports the dependency; a partly configured Cline project does not trigger fresh-scaffold replacement.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## browser-runtime-verification

- Version: 1.2.0.
- Finding and change: No interface defect found. Scenario inputs, tool capabilities, side-effect limits, replay safety, sanitized evidence, and aggregate result rules already make the verification contract explicit.
- Consumer walkthrough: With network inspection unavailable, a successful visual check yields incomplete overall verification; a relevant observed failure yields failed even if other checks pass.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## ci-cd-and-automation

- Version: 1.7.0.
- Finding and change: No interface defect found. Required-check consumers, workflow inputs, permissions, artifact identity, skip semantics, stale deployments, replay recovery, and execution evidence are already explicit.
- Consumer walkthrough: A renamed check requires coordinating branch-policy consumers; an unexpected skipped upstream job cannot become aggregate success; interrupted writes require reconciliation before replay.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## code-review-and-quality

- Version: 1.4.0.
- Finding and change: No interface defect found. Review target and baseline, read-only scope, finding severity, requested schema precedence, optional Markdown template, evidence attribution, and verdict semantics agree across instructions and references.
- Consumer walkthrough: A findings-only caller keeps its schema; absent material verification defers judgment; an authorized fix is re-reviewed before a verdict.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## code-simplification

- Version: 1.1.6.
- Finding and change: Unused-code guidance could miss indirect consumers. Added export, registry, serialization, reflection, and configuration checks before renames or removals.
- Consumer walkthrough: A class with no direct calls but a serialized name is retained or migrated explicitly; purely private guard-clause refactoring keeps its existing verification path.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## context-engineering

- Version: 1.1.6.
- Finding and change: Context packets omitted workspace identity and evidence freshness, risking stale handoffs. Added repository/revision/worktree state, planned-versus-run checks, and source-backed constraint provenance.
- Consumer walkthrough: A receiving agent can distinguish an old passing check from a current planned check and locate the workspace before editing.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## conventional-commits

- Version: 1.1.3.
- Finding and change: Drafting input and output scope were implicit. Clarified staged-diff ownership, missing-evidence handling, ready-to-copy output, and separation from committing and release-tool behavior.
- Consumer walkthrough: A staged-only request excludes an unrelated unstaged fix; a supplied message can be reviewed without Git access or creating a commit.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## debugging-and-error-recovery

- Version: 1.2.4.
- Finding and change: Reproduction advice allowed repeated scenarios without first reconciling write outcomes. Added partial-state inspection and safe replay requirements for timed-out writes and jobs.
- Consumer walkthrough: A payment-like job with a lost response is inspected or reproduced in a fixture before replay; a pure failing unit test can still be rerun directly.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## deprecation-and-migration

- Version: 1.2.4.
- Finding and change: Parallel migration guidance left write ownership and rollback data compatibility implicit. Clarified mixed-version consumers, resumability, duplicate effects, and old-reader compatibility.
- Consumer walkthrough: A new writer that changes stored data prevents an unconditional rollback promise; a shadow run must suppress duplicate external writes.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## documentation-and-adrs

- Version: 1.3.3.
- Finding and change: Specialized routing lacked an explicit handoff and unavailable-dependency result. Added handoff inputs, scope preservation, and a writing-brief fallback without claiming completion.
- Consumer walkthrough: An unavailable ADR writer produces a destination and evidence brief; a documentation-advice request remains advisory rather than creating files.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## doubt-driven-development

- Version: 1.2.3.
- Finding and change: Reviewer handoff omitted snapshot identity and write ownership. Added revision/access context and stale-finding reconciliation without changing the review response format.
- Consumer walkthrough: A reviewer returns findings for its supplied snapshot; later edits require refreshed evidence, and the coordinator retains write ownership.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## frontend-ui-engineering

- Version: 1.3.4.
- Finding and change: Component responsibilities did not define caller-facing state and event contracts or asynchronous outcome ownership. Added input/default/callback semantics and stale-response, disposal, and mutation-retry handling.
- Consumer walkthrough: A controlled component reports intent without silently taking state ownership; a timed-out form mutation reconciles its outcome before retry.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## git-workflow-and-versioning

- Version: 1.3.3.
- Finding and change: Handoff output omitted the final Git-state boundary. Added repository/branch identity and explicit unstaged, staged, committed, pushed, and observed remote status.
- Consumer walkthrough: A local commit is reported by ID without implying a push or passing remote CI; uncommitted staged user work remains identifiable.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## hexagonal-vertical-slices

- Version: 1.2.1.
- Finding and change: No interface defect found. Slice ownership, published ports, adapter translation, caller compatibility, consistency, failure semantics, incremental migration, and consumer-facing checks already form a complete contract.
- Consumer walkthrough: A vendor error is translated at the adapter; a cross-slice mutation uses the owning published boundary; review-only work returns planned checks without claiming runtime compliance.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## idea-refine

- Version: 2.0.0.
- Finding and change: Helper emitted invalid JSON for control characters and left invocation/failure semantics implicit. Used standard-library JSON encoding, validated argument count, retained empty/default behavior, and documented paths, repeat runs, exits, partial creation, and Python 3 fallback. Helper compatibility is conditional on Python 3 and at most one argument; major version marks that requirement.
- Consumer walkthrough: Executed isolated default/empty/leading-dash/quoted/backslash/newline/tab/Unicode paths, repeat runs, extra arguments, and file collisions; decoded success JSON and verified no false success or overwritten file. Refinement itself remains usable without the helper.
- Compatibility: breaking for shell-only helper callers or callers passing extra arguments. Version 2.0.0 documents the Python 3 prerequisite, one-argument grammar, and manual fallback. Success JSON keys are preserved; arbitrary agent-host execution remains unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## incremental-implementation

- Version: 2.1.4.
- Finding and change: Rollback advice assumed additive safety and required splitting replacement/removal even when that breaks an intermediate contract. Corrected both and clarified mixed producer/consumer versions and feature-flag limits.
- Consumer walkthrough: A strict decoder must be checked before adding a field; a public symbol replacement stays atomic or uses a compatibility adapter rather than an intentionally broken intermediate increment.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## interview-me

- Version: 2.0.1.
- Finding and change: No interface defect found. Activation exclusions, light/full selection, ordinal readiness, one-question interaction, explicit confirmation, noninteractive draft fallback, and downstream handoff agree with the scenario reference.
- Consumer walkthrough: A precise edit bypasses interviewing; an unanswered full interview returns an unconfirmed draft; a confirmed intent hands off without treating hypotheses as requirements.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## performance-optimization

- Version: 1.4.5.
- Finding and change: Optimization patterns could be copied as externally visible truncation or shape changes. Added consumer review and preservation of completeness, order, freshness, failures, and side effects.
- Consumer walkthrough: Paginating internal work can preserve a full-result API; returning only page one requires an explicit contract migration rather than a performance-only claim.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## planning-and-task-breakdown

- Version: 2.2.2.
- Finding and change: No interface defect found. Requirements-to-task mapping, stable progress IDs, canonical checkbox ownership, confirmed-versus-proposed commands, blocked prerequisites, readiness, and parallel integration contracts match the plan template.
- Consumer walkthrough: An unknown verification command stays unresolved; a summary references canonical task IDs without duplicating status; invalidated evidence reopens the affected item.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## review-implementation-plan

- Version: 1.3.3.
- Finding and change: Readiness labels could freeze independent tasks and differed from the planning skill. Aligned blocked semantics and clarified inline input, explicit review-only output, and readiness versus authorization.
- Consumer walkthrough: A blocked later migration does not prevent an independent discovery task; a supplied inline no-edit review returns findings without demanding a file.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## run-local-quality-gate

- Version: 1.4.3.
- Finding and change: Validation output lacked aggregate status semantics and check-only ownership. Added no-edit command handling, aggregate side-effect inspection, tested-state context, and passed/failed/incomplete rules.
- Consumer walkthrough: A review-only formatter uses check mode; a passing subset with an unavailable required build reports incomplete rather than passed.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## security-and-hardening

- Version: 1.1.9.
- Finding and change: Validation guidance did not require classifying tighter validation for existing callers. Added caller impact, stable rejection categories, effect timing, denied-state guarantees, and intentional-break migration handling.
- Consumer walkthrough: A newly rejected legacy input receives a documented error and migration path; denied requests are checked for unintended mutation without retaining an unsafe bypass.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## shipping-and-launch

- Version: 1.6.4.
- Finding and change: Readiness evidence was not bound to an artifact or mixed consumer versions, and the performance reference assumed rollback despite alternative recovery contracts. Added release identity and compatibility checks; aligned the reference with chosen recovery.
- Consumer walkthrough: A canary serving old and new clients needs verified combinations; a data-changing release cannot treat flag disablement as schema rollback.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## source-driven-development

- Version: 1.2.3.
- Finding and change: Source-backed guidance could be read as runtime proof, and latest docs could silently shift the target version. Added evidence status, detected-version discipline, unavailable-source handling, and separate execution claims.
- Consumer walkthrough: A current example requiring a newer library is not copied into the pinned target without migration; official documentation support is reported separately from an executed test.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## spec-driven-development

- Version: 2.1.2.
- Finding and change: No interface defect found. Canonical revision, requirement basis, stable IDs, observable acceptance, draft/accepted/superseded states, delegated authority, and derived-plan handoff match the bundled template.
- Consumer walkthrough: An accepted requirement can coexist with blocked implementation access; an unaccepted amendment preserves the accepted baseline; a precise fix does not require a new specification.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## test-driven-development

- Version: 1.3.4.
- Finding and change: Contract-test guidance did not address fake/provider drift or older supported consumers. Added shared observable contracts for adapters and fakes plus compatibility fixtures and real-integration limits.
- Consumer walkthrough: A fake that silently uses different retry or error semantics is checked against the provider contract; a new response field is verified with supported consumer fixtures.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## update-project-docs

- Version: 1.3.3.
- Finding and change: Configuration documentation omitted precedence, empty/null distinctions, validation failures, and reload behavior. Added these observable contract checks with implementation evidence.
- Consumer walkthrough: An empty environment override is documented according to actual precedence and parsing; an unsupported key is not assigned an invented default.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## using-agnostic-software-development-skills

- Version: 2.5.4.
- Finding and change: Relationship vocabulary lacked the state transferred at a handoff. Added scope, authorization, canonical revision, decisions, blockers, prior evidence, and expected deliverable; aligned launch summary with its recovery alternatives.
- Consumer walkthrough: A documentation review routed to a writer retains no-edit scope; a planning handoff does not acquire publication authority or lose unresolved blockers.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## write-adr

- Version: 1.2.3.
- Finding and change: Sequential creation did not address competing slugs or partial retries, and index instructions imposed tables over existing navigation. Added number-wide collision checks, retry reconciliation, and index-format preservation.
- Consumer walkthrough: An existing same-number different-slug ADR causes renumbering; a retry repairs the missing index entry instead of duplicating the decision; a list index stays a list.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## add-hexagonal-feature

- Version: 1.1.3.
- Finding and change: A claimed complete slice could stop after fake-backed application tests. Added use-case contract semantics, caller compatibility checks, composition-root/inbound wiring, and explicit partial-increment labeling.
- Consumer walkthrough: A passing fake-repository test does not complete a CLI-facing slice until the real entry point is wired and its result/failure mapping is checked.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## bootstrap-python-app

- Version: 1.5.1.
- Finding and change: Bootstrap input validation and retry ownership were implicit, and CLI stream/exit semantics were scattered across tests. Clarified package/version/coverage inputs, destination preservation, partial resumption, and the existing CLI result contract. Reviewed all six assets; no template behavior changed.
- Consumer walkthrough: A keyword package name or inconsistent Python/Ruff target is rejected before generation; rerunning after partial setup preserves edits; the existing CLI tests agree on no-argument/help/version/invalid-argument streams and statuses.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## python-add-adapter

- Version: 1.0.5.
- Finding and change: Method matching was insufficient for semantic conformance, and resource/retry ownership was absent. Added caller/implementation contract inspection, client cleanup, async behavior, bounded retries, and unknown-write reconciliation.
- Consumer walkthrough: A driver timeout maps to the promised application failure without blindly repeating a committed write; a client session has a defined cleanup owner.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## python-add-env-settings-adapter

- Version: 1.0.5.
- Finding and change: Rendered templates exposed secrets in adapter/DTO representations and test isolation missed case-insensitive or field-name environment inputs. Fixed repr fields and isolation, added precedence/blank-override/redaction regression checks and verified dotenv-only and mixed-case field-name inputs, and documented path, source, alias, snapshot, and exception semantics. Conditional runtime evidence: Python 3.14, pydantic-settings 2.15.0, Pydantic 2.13.5.
- Consumer walkthrough: Rendered all Python assets into an isolated package: 16 pytest cases passed after observing ambient-environment failures and two secret-repr failures before fixes. Existing typed settings and exception contracts remain; callers must not parse repr text. Full generated-project quality gates and other dependency versions were not exercised.
- Compatibility: typed field values, constructors, and ConfigurationError remain compatible. Representations intentionally omit secrets; consumers parsing repr text must migrate to typed access without logging secrets. Observed only with the dependency versions above; automatic agent-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## python-add-port

- Version: 1.0.4.
- Finding and change: Port guidance focused on signatures without complete operation semantics or conformance evidence. Added ownership, failures, effects, collection/retry/lifecycle contracts, existing-consumer migration, and type-versus-runtime verification limits.
- Consumer walkthrough: Two repository adapters must agree on missing-result and ordering semantics; a structural Protocol is checked at actual typed use sites and does not itself prove runtime behavior.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## python-build-extensible-cli

- Version: 1.1.4.
- Finding and change: The entrypoint sketch omitted the console-compatible default and did not distinguish empty argv from process argv. Clarified that contract, borrowed stream/resource ownership, effect-free registration/decoding, and invocation isolation.
- Consumer walkthrough: An embedding caller passing an empty list parses no arguments; the console calls main without parameters; a runner does not close the caller stdout or execute after decode failure.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## split-python-module

- Version: 1.1.3.
- Finding and change: Public re-exports were treated as sufficient without persisted module identity, resource lookup, or actual monkeypatch behavior. Added these consumers and upgrade/downgrade compatibility checks.
- Consumer walkthrough: An old import can succeed while new pickle data points to an unavailable module or a patch no longer intercepts calls; saved fixtures and patch behavior are checked before claiming preservation.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## using-python-software-development-skills

- Version: 3.0.1.
- Finding and change: Python routing omitted availability and handoff semantics present in the shared catalog. Added dependency checks, scoped fallback, transferred contracts/evidence, and full-feature integration requirements.
- Consumer walkthrough: A missing adapter skill is reported without inventing steps; completing separate port and adapter procedures does not imply the integrated feature works.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## write-pytest-tests

- Version: 1.1.4.
- Finding and change: Examples could freeze incidental error prose and under-isolate environment-backed boundaries. Clarified stable exception contracts, regex matching, consumer lookup patching, inherited aliases, and scoped state restoration.
- Consumer walkthrough: An exception with a stable code is tested by type/code rather than mutable prose; a lower-case inherited environment alias is cleared even when the test sets an uppercase variable.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## write-python-docstrings

- Version: 1.1.3.
- Finding and change: Callable documentation guidance did not make deferred execution or resource lifetime explicit. Added iterator/async/context lifetime, failure timing, cancellation effects, and absent/empty/default distinctions.
- Consumer walkthrough: A generator can raise during iteration rather than construction; a context-managed borrowed value documents when it becomes invalid; None does not silently mean the same as an empty collection.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; no configured mirror.

## condensed-prose-refactor

- Version: 1.2.0.
- Finding and change: No interface defect found. Source selection, operation/intensity defaults, literal protection, uncertainty, hard-limit conflict handling, missing-source clarification, variants, and rewrite-only output exceptions form an explicit contract. Rhetorical reference preserves the same fidelity limits.
- Consumer walkthrough: A missing source triggers clarification; an impossible length limit returns the shortest faithful rewrite with a brief conflict note; embedded commands and links remain literal; already effective prose can remain unchanged.
- Compatibility: compatible with documented callers; target-host execution unverified.
- Checks: focused lint, reference validator, resource review; mirror parity.

## Final verification and retained state

- All 43 tracker entries have this audit checked and linked in order; the other
  three audit goals remain unchecked. Thirty-four skills changed; nine needed
  no interface change.
- Full-shelf `ritebook skills lint --root skills` passed with cached Ritebook
  0.1.63. Focused lint used an isolated scan root containing the current skill
  because linting a skill directory as its own root produces a `.` catalog path.
- `skills-ref validate <skill-directory>` passed for all 43 canonical packages
  with skills-ref 0.1.0. Local resource links and all 33 installed mirror trees
  were checked; the three root and packaged Cline files remain byte-identical.
- The idea helper was invoked through `sh <absolute-skill-path>/scripts/idea-refine.sh`
  in a temporary workspace. JSON round-trip checks covered omitted/empty paths,
  leading dashes, quotes, backslashes, newlines, tabs, Unicode, repeated runs,
  extra arguments, and file collisions. Success/failure streams and exit codes
  were checked. Python-unavailable behavior was inspected, not executed.
- All seven Python settings assets were rendered into a temporary `example_app`
  package and tested using pytest 9.1.1 on Python 3.14.10 with pydantic-settings
  2.15.0 and Pydantic 2.13.5. Sixteen tests passed, with deliberately contaminated
  inherited environment variables. The original ambient-variable and secret-repr
  failures were observed before their fixes. This is fixture execution, not a
  complete generated-project quality gate or a dependency-version matrix.
- Existing catalog descriptions and paths agree for the 43 current skills. The
  catalog also contains four previously removed wrappers: `format-python-code`,
  `lint-python-code`, `run-python-quality-gate`, and `run-python-tests`. This is
  pre-existing drift, retained because index refresh requires an explicit request.
- `ritebook.lock` and `.ritebook/` provenance remain unchanged and describe their
  prior install; manually synchronized mirrors are local edits, not a new
  provenance-verified installation. No index refresh, install, publication,
  commit, or push was performed. The original staged tracker remains staged;
  this audit's tracker updates, source/mirror edits, and report are unstaged.
- Automatic skill discovery, external clients/providers, production behavior,
  and complete scaffold builds were not exercised. Dated compatibility references
  were reviewed as qualified documentation, not re-certified against current hosts.
