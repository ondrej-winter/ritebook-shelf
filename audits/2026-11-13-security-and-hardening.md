# Skill security audit — 2026-11-13

Reviewed each skill and its bundled resources individually in tracker order,
using `security-and-hardening`. These are instruction packages and templates;
the audit addresses their concrete trust, data, execution and verification
boundaries. No-change entries mean no actionable defect was established in this
scope, not a certification of downstream applications.

Every completed entry passed focused Ritebook 0.1.63 lint (temporary parent scan
root), skills-ref 0.1.0 validation, and configured mirror parity. Instruction
walkthroughs are paper review evidence, not target-host execution. External
integrations, automatic discovery, downstream applications and production
security remain runtime-unverified unless execution evidence is recorded.
No index refresh, install, provenance update, commit, push or publication is
part of this audit. Catalog and lock state are inspected without regeneration.

Audit completed: **43 of 43** entries reviewed in order; **25** improved and
**18** retained. Only security-and-hardening goals changed in the tracker.

The material executable/template fixes are a dotenv validation traceback leak
and automatic release publication without an effective opt-in. Other changes
strengthen the instruction contracts for input/authorization boundaries,
untrusted code and content, private evidence, safe migration and test coverage.
No known vulnerability was deferred or accepted by this review; downstream
runtime behavior remains outside the observed evidence below.

Changed versions:

| Skill | Before | After |
| --- | --- | --- |
| api-and-interface-design | 1.3.4 | 1.4.0 |
| author-agent-skill | 2.1.1 | 2.2.0 |
| code-review-and-quality | 1.4.0 | 1.5.0 |
| context-engineering | 1.1.6 | 1.2.0 |
| debugging-and-error-recovery | 1.2.4 | 1.3.0 |
| deprecation-and-migration | 1.3.0 | 1.4.0 |
| doubt-driven-development | 1.2.3 | 1.3.0 |
| frontend-ui-engineering | 1.3.4 | 1.4.0 |
| incremental-implementation | 2.2.0 | 2.3.0 |
| interview-me | 2.0.1 | 2.1.0 |
| performance-optimization | 1.5.0 | 1.6.0 |
| run-local-quality-gate | 1.4.3 | 1.5.0 |
| security-and-hardening | 1.1.9 | 1.2.0 |
| source-driven-development | 1.2.3 | 1.3.0 |
| test-driven-development | 1.3.4 | 1.4.0 |
| update-project-docs | 1.3.3 | 1.4.0 |
| add-hexagonal-feature | 1.1.3 | 1.2.0 |
| bootstrap-python-app | 1.6.0 | 2.0.0 |
| python-add-adapter | 1.0.5 | 1.1.0 |
| python-add-env-settings-adapter | 1.0.5 | 1.1.0 |
| python-add-port | 1.0.4 | 1.1.0 |
| python-build-extensible-cli | 1.1.4 | 1.2.0 |
| split-python-module | 1.1.3 | 1.2.0 |
| write-pytest-tests | 1.1.4 | 1.2.0 |
| condensed-prose-refactor | 1.2.0 | 1.3.0 |

Final verification:

- Focused Ritebook 0.1.63 lint and skills-ref 0.1.0 validation passed for each
  skill before advancing. Lint used an isolated temporary parent scan root;
  this Ritebook version cannot lint a skill at catalog path `.` directly.
- Broad `ritebook skills lint --root skills` passed for 43 canonical skills;
  `ritebook skills lint --root .agents/skills` passed for 33 installed skills.
  Validators ran from existing cached uv environments without a package refresh.
- All 33 configured mirrors and all three Cline scaffold copies have byte parity.
  The 10 Python skills are not selected in `ritebook.toml`; none were installed.
- The environment adapter was rendered into an isolated temporary package with
  its bundled DTO/adapter tests. A new regression failed before the fix because
  formatted exception output contained a synthetic dotenv secret; afterward all
  **17 tests passed** on Python 3.14.10, Pydantic 2.13.5 and pydantic-settings
  2.15.0. Inherited alias contamination and local dotenv lookup were isolated.
  This does not establish behavior on every supported dependency version or
  in a complete generated application. Explicit error/context/local capture
  still needs the documented redaction controls.
- Rendered bootstrap YAML passed checks for release opt-in, push/ref/bot and
  quality prerequisites, read-only quality permissions, no persisted quality
  checkout token, and all action references pinned to 40-character commits.
  The opt-in check failed before the edit. Pins were resolved from the existing
  upstream refs with read-only `git ls-remote`, including the peeled setup-uv
  tag; no action version family was intentionally upgraded. These are parse and
  policy checks, not hosted Actions execution or an action-source security audit.
- The idea-refinement helper passed isolated default-path, hostile literal path,
  extra-argument rejection and repeated-run preservation checks. No helper code
  change was needed.
- Tracker/report order and 43 anchors, local links, unchanged other audit goals,
  metadata/diff review and `git diff --check` passed. The final illustrative
  authoring timestamp was preserved rather than refreshed with package metadata.
- Catalog inspection found 43 matching canonical paths and descriptions. The
  schema contains no package versions or hashes; regeneration was unnecessary.
  `ritebook-index.json`, `ritebook.lock` and `.ritebook/` provenance are unchanged.
- No automated secret or advisory scan was run: no shelf secret scanner or
  resolved downstream application lock is available. Changed diffs were manually
  inspected for sensitive literals and unsafe defaults. No clean vulnerability
  scan or full-history secret-scan result is claimed. Templates remain subject
  to their target project's dependency and release scans.
- Automatic discovery, downstream app builds, full scaffold quality gates,
  browser/provider execution, production behavior and publication were not
  exercised. Instruction scenarios are paper walkthroughs and package checks,
  not proof that all future agents obey the guidance.
- All changes are unstaged and uncommitted. No index refresh, install, provenance
  rewrite, commit, push, publication or remote configuration change occurred.

Primary sources consulted for added security/API guidance (2026-11-13):

- [OWASP prompt-injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use)
  and [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)
- [Pydantic error input hiding](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.hide_input_in_errors)
  and [Python exception chaining](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)

## add-observability

- Version: 1.4.1.
- Review: Retained. Reviewed telemetry contracts and the full signal checklist: early allowlisting/redaction, bounded fields and labels, protected profiles, untrusted incoming context, restricted outgoing baggage, export-failure isolation and test alert destinations are already explicit. Paper scenarios for sensitive URLs, forged trace context and unavailable collectors preserve data and workflow boundaries.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## api-and-interface-design

- Version: 1.4.0.
- Review: Fixed a gap between shape validation and authorization: protected operations now require actor/action/resource/tenant checks, including batch items, and scope caches, cursors and idempotency records against cross-actor reuse. Paper scenarios cover a valid foreign resource ID, a mixed-tenant batch and replay after permission loss; consumer denial tests are required. Existing caller fields and handoff remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## author-agent-skill

- Version: 2.2.0.
- Review: Fixed unsafe review execution assumptions: imported instructions and tool output cannot expand authority, helpers/dependencies must be inspected before execution, and unfamiliar packages use disposable workspaces without real credentials or sensitive files. Paper scenarios reject an embedded permission override and avoid running a credential-reading helper merely because package validation passes. Activation, resource paths and outputs remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## author-agents-config

- Version: 1.3.0.
- Review: Retained after reviewing the main workflow, README, three references, templates and Cline files. Existing controls preserve workspace/symlink boundaries, prevent permission/hook/secret changes, separate configuration text from enforced restrictions and require safe fresh-session checks. Paper cases for an external symlink, existing policy owner and review-only request keep writes within scope. Dated client compatibility claims were not refreshed or asserted as observed runtime behavior.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## browser-runtime-verification

- Version: 1.2.0.
- Review: Retained. The workflow already treats page/console/network content as untrusted, preserves authenticated user state, bounds retries, limits side effects, uses test accounts and forbids moving browser secrets to other tools. Paper cases for malicious page instructions, a destructive retry and secret-bearing HAR/screenshot evidence follow explicit scope and sanitization rules. Browser execution is outside this package audit.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## ci-cd-and-automation

- Version: 1.7.0.
- Review: Retained. Reviewed event-to-job trust, effective downstream permissions, safe input transport, immutable dependencies, cache/artifact poisoning boundaries, trusted producer checks and fail-closed aggregate gates. Paper cases for an untrusted artifact producer, missing gate result and stale deployment are already covered. No provider policy or workflow dispatch was changed or exercised.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## code-review-and-quality

- Version: 1.5.0.
- Review: Fixed the reviewer execution boundary: patch comments/logs cannot grant authority, and executing tests or build hooks from untrusted contributions requires inspection and a disposable environment without production credentials or sensitive files. Paper cases for a malicious test hook and a comment requesting secret disclosure now stop before unsafe execution. Reviewed all three supporting checklists/templates; review format and verdict contract remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## code-simplification

- Version: 1.1.6.
- Review: Retained. Reviewed guard-clause and notification examples plus the refactor workflow. Validation and authorization ordering is preserved, security checks cannot be removed for neatness, and unsupported behavior preservation blocks edits. Paper cases for consolidating permission checks or removing apparently unused policy code require evidence and tests first; no executable helper or new trust boundary exists.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## context-engineering

- Version: 1.2.0.
- Review: Fixed context laundering and data minimization gaps: provenance/scope determine trust, summaries retain trust labels, documentation cannot expand user authorization, and evidence packets redact credentials and unnecessary personal data. Paper cases cover a log claiming to be system policy and an environment dump proposed for handoff. Packet format and routing remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## conventional-commits

- Version: 1.1.3.
- Review: Retained. This package drafts or reviews message text from an explicit diff scope and does not execute Git or infer release authorization. Examples contain placeholders and no live credentials. Paper review of a staged-message request excludes unstaged work and cannot create a commit; no actionable security defect was established in the syntax-only workflow.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## debugging-and-error-recovery

- Version: 1.3.0.
- Review: Fixed evidence preservation that could copy live secrets into transcripts or regression fixtures. Captures now require sanitization, synthetic reproducers and restricted storage for necessary raw evidence. Paper cases for a credential-bearing URL and an environment dump preserve diagnostic structure without secret values. Existing safeguards for untrusted error text, uncertain writes and idempotent retries remain intact.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## deprecation-and-migration

- Version: 1.4.0.
- Review: Fixed migration security continuity: parallel paths, backfills, copies and rollback must preserve authorization, tenant isolation, redaction and retention, and cannot restore revoked access or deleted sensitive data. Paper cases for a permissive legacy shim and rollback after revocation now require denial checks. Existing phased migration/removal outputs and load controls remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## documentation-and-adrs

- Version: 1.3.3.
- Review: Retained. The routing workflow passes evidence, edit/review scope and verification to an explicitly read specialized skill, and unavailable dependencies yield a bounded brief. Interface documentation includes authorization constraints. Paper review of a security-decision documentation request does not grant runtime or publication authority; no executable assets or sensitive example values are bundled.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## doubt-driven-development

- Version: 1.3.0.
- Review: Fixed external-review data exposure: authorization to invoke a reviewer now also requires an approved destination for the artifact classification and removal of credentials and unnecessary sensitive content. Paper cases distinguish permission to run review from permission to export confidential material. Read the orchestration reference; read-only reviewer scope, safe artifact transport and untrusted-output reconciliation remain intact. No external reviewer was invoked.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## frontend-ui-engineering

- Version: 1.4.0.
- Review: Fixed missing content and authority controls in an otherwise detailed UI workflow: context-aware rendering, reviewed rich-content sanitization, allowed URL schemes, client secret exclusion and server-side authorization are now explicit. Paper cases cover scriptable links, raw user markup and a hidden control called directly. Relevant malicious-content/denial verification is required; accessibility reference and existing browser evidence contract are preserved.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## git-workflow-and-versioning

- Version: 1.3.3.
- Review: Retained. Reviewed noninteractive inspection, staged/unstaged ownership, precommit secret checks, authorization for history changes and explicit worktree targets. Paper cases for mixed user/agent changes, a secret-bearing staged file and a shared-branch rewrite follow existing preservation and approval rules. The package has illustrative commands only and does not itself execute or publish.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## hexagonal-vertical-slices

- Version: 1.2.1.
- Review: Retained. Architecture responsibilities already keep transport authentication/shape validation at inbound adapters, enforce business authorization consistently in the application/domain, and isolate secret loading and infrastructure details. Paper cases for an alternate inbound adapter and a cross-slice direct storage write remain constrained by published use cases and state ownership. Folder shape alone is explicitly insufficient evidence.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## idea-refine

- Version: 2.0.0.
- Review: Retained after reviewing all three references and the shell/Python helper. The helper passes arguments as data, JSON-encodes paths, rejects extra arguments and only creates a caller-selected directory within prior persistence authorization. Executed isolated cases for defaults, a quoted shell-like path, extra arguments and repeated-run content preservation; all passed without command execution. Product/research decisions and saving remain explicitly separate.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## incremental-implementation

- Version: 2.3.0.
- Review: Fixed a slicing gap that could defer controls until a later hardening phase: every exposed protected operation now includes authentication, authorization, validation, secret handling and negative checks in the same increment. Paper cases for an active endpoint behind a hidden UI and a background write demonstrate why feature flags are insufficient. Increment classifications and checkpoint outputs remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## interview-me

- Version: 2.1.0.
- Review: Fixed sensitive-data collection in open-ended interviews: questions now minimize data, never request credentials or raw personal records, and avoid repeating supplied secrets in summaries or handoffs. Paper scenarios use roles and redacted examples to resolve access requirements without collecting tokens. Reviewed the normative examples; presentation, confirmation and downstream intent contracts remain unchanged.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## performance-optimization

- Version: 1.6.0.
- Review: Fixed two concrete optimization risks: authorized bounded load tests and protected/redacted profiling data; cache/batch reuse must also preserve tenant scope and current authorization, including revocation and deletion. Paper cases cover cross-tenant cache hits and production load generation. Reviewed all three references. Existing measurement requirements remain intact; no performance or production-security result is claimed from these guidance changes.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## planning-and-task-breakdown

- Version: 2.2.2.
- Review: Retained after reviewing the workflow and plan template. Scope/permission prerequisites, failure acceptance criteria, data recovery, shared-state serialization and unverified-check blockers are already explicit. Paper cases for a security-sensitive dependency, an unavailable check and an external rollout keep readiness separate from execution authorization. No commands or sensitive values are embedded in the template.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## review-implementation-plan

- Version: 1.3.3.
- Review: Retained. The review explicitly checks security/privacy implications, dependency and rollback impact, failure coverage and execution permissions while prohibiting task implementation. Paper cases for an unresolved security policy, an unavailable validation command and a review-only plan preserve blockers rather than manufacturing readiness. No executable helpers or external mutations are part of this package.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## run-local-quality-gate

- Version: 1.5.0.
- Review: Fixed the assumption that a named local gate is safe to execute: commands/hooks must be inspected, untrusted code uses isolated disposable environments without production credentials or sensitive files, and sandbox bypass is forbidden. Paper cases cover a credential-reading build backend and a gate needing unavailable privileges; independent safe checks continue with incomplete status. Existing project commands and check-only behavior remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## security-and-hardening

- Version: 1.2.0.
- Review: Fixed missing agent prompt-injection and outbound-request/SSRF coverage in the main workflow and companion checklist. Reviewed OWASP primary guidance on 2026-11-13; tool actions must preserve authorization, and outbound destinations/redirects/DNS need controls beyond TLS. Paper cases cover retrieved secret-exfiltration instructions and an external URL redirecting to metadata. Existing review/implementation outputs remain compatible; no live attack was attempted.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## shipping-and-launch

- Version: 1.6.4.
- Review: Retained after reviewing all five references. Exact artifact identity, explicit deployment authorization, least exposure, denial/hostile-input checks, secret-safe evidence and recovery that cannot weaken security or expose stale sensitive data are already covered. Paper scenarios for missing monitoring, a security-triggered hold and unsafe rollback remain gated. No production action or notification was taken.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## source-driven-development

- Version: 1.3.0.
- Review: Fixed conflation of factual source authority with execution authority. Fetched pages/examples remain data, commands and installers require side-effect inspection, and research queries/URLs exclude credentials and private project data. Paper cases cover an official-looking installer snippet and a page requesting secret disclosure. Source hierarchy, citation format and version-evidence contract remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## spec-driven-development

- Version: 2.1.2.
- Review: Retained after reviewing the workflow and specification template. Actor/permission and failure invariants, data/privacy constraints, accepted-versus-proposed requirements and external-action boundaries are explicit. Paper cases for a speculative security requirement and an accepted spec with unresolved execution access preserve the distinction between agreement and permission. No runtime security claims or executable assets are present.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## test-driven-development

- Version: 1.4.0.
- Review: Fixed security-test guidance: the testing reference now calls for denial/cross-tenant cases at the real enforcement boundary, unchanged state on rejection, synthetic secrets/redaction assertions and isolated side effects. Paper cases expose a mock that merely returns denied and an integration test pointed at production. Main TDD order, resource path and outputs remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## update-project-docs

- Version: 1.4.0.
- Review: Fixed unsafe documentation examples and validation: credentials/private data require placeholders or sanitization, secret references replace live values, and runnable examples use inspected side effects and disposable write fixtures. Paper cases cover copying an authenticated URL into setup docs and executing a deployment example to validate it. Documentation surfaces and required output remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## using-agnostic-software-development-skills

- Version: 2.5.4.
- Review: Retained after reviewing the routing workflow and catalog reference. Handoffs preserve user scope, authorization, revision, blockers and prior verification; missing skills cannot be invented and optional mentions do not recursively activate workflows. Paper cases for review-to-implementation routing and local-validation-to-publication preserve permission boundaries. The reference table is navigation, not evidence of security enforcement.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## write-adr

- Version: 1.2.3.
- Review: Retained. File creation requires a repository-owned destination, collision rechecks and preservation of existing records; status defaults to Proposed rather than inventing acceptance. Paper cases for a concurrently claimed number and a new security decision preserve existing files and distinguish documentation from policy execution. The inline template contains no credentials or executable operations.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.

## add-hexagonal-feature

- Version: 1.2.0.
- Review: Fixed missing authorization ownership in the Python slice workflow: inbound identity establishment is separated from use-case actor/resource/tenant enforcement, DTO claims are untrusted, and denial/cross-tenant state-preservation checks include the real entry point. Paper scenarios cover a forged actor field and a background caller bypassing an HTTP-only guard. Existing slice layout and port contracts remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## bootstrap-python-app

- Version: 2.0.0.
- Review: Fixed active publication despite prose saying to defer it: release now defaults off and requires repository ENABLE_PYPI_RELEASE=true as well as existing event/ref/bot/quality gates. Documented migration and input serialization/workspace rules. Pinned every GitHub action to upstream commits resolved with read-only git ls-remote on 2026-11-13 (peeled setup-uv tag); quality checkout no longer persists credentials. Rendered YAML policy checks failed before and passed after. All six assets reviewed; full hosted CI, publishing and complete scaffold runtime were not exercised. Major version records the intentional release-default change.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## python-add-adapter

- Version: 1.1.0.
- Review: Fixed missing edge security controls: inbound validation/authentication and safe errors, application authorization ownership, safe outbound query/command/path handling, constrained destinations and least-privilege credentials. Negative tests must exercise real authorization rather than a stub-only path. Paper cases cover forged tenant IDs, secret-bearing driver errors and arbitrary outbound URLs. Existing port and package interfaces remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## python-add-env-settings-adapter

- Version: 1.1.0.
- Review: Fixed a reproduced leak: a missing required field chained a Pydantic ValidationError containing unrelated dotenv secrets into ConfigurationError tracebacks. Added input hiding, suppressed the validation chain, documented residual explicit serialization/context/local-capture risks and added a generated-template regression. Isolated template tests failed before on a synthetic secret in formatted traceback, then all 17 passed after; inherited case variants and dotenv lookup remained isolated. DTOs, aliases, precedence and safe application error text are preserved; internal validation causes are intentionally no longer displayed. Reviewed all ten assets.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## python-add-port

- Version: 1.1.0.
- Review: Fixed an implicit security contract: protected ports now specify authenticated context, authorization ownership and safe denial semantics, with application/adapter cross-tenant checks. Paper cases distinguish a structurally conforming implementation from one that enforces access and reject treating a typed actor field as permission. Existing Protocol/DTO shapes and paths remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## python-build-extensible-cli

- Version: 1.2.0.
- Review: Fixed extension and diagnostic trust gaps: registrar callbacks are trusted code rather than a sandbox, user-controlled dynamic loading needs a separate trust design, and protected commands require application authorization. Credentials stay out of argv/parser diagnostics and terminal output follows sanitization/disclosure policy. Paper cases cover an untrusted registrar path and verbose secret dumps. Reviewed the complete pattern reference; parser lifecycle, extension types and stream contracts remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## split-python-module

- Version: 1.2.0.
- Review: Fixed unsafe compatibility-check implications around persisted pickle names and dynamic imports: verification uses trusted synthetic fixtures, never unpickles untrusted objects or imports user-supplied plugins, and preserves public validation/authorization checks. Paper cases cover a supplied legacy pickle and a moved permission guard. Existing module-split scope and compatibility outputs remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## using-python-software-development-skills

- Version: 3.0.1.
- Review: Retained. The catalog preserves edit/review scope and canonical contracts through feature/port/adapter handoffs, requires integration evidence and cannot invent or install missing validation tools. Paper cases for an unavailable adapter skill and a port-only result preserve blockers and prevent false end-to-end/security claims. No executable helper or secret-bearing example is included.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## write-pytest-tests

- Version: 1.2.0.
- Review: Fixed security-coverage and fixture-exposure gaps: tests must include relevant denied/cross-tenant state-preservation checks without mocking enforcement, and fixture/parameter IDs, diffs, logs and tracebacks use synthetic data. Paper cases cover a mocked policy always returning denied and a live token used as a parametrized regression input. Pytest style, environment isolation and validation commands remain compatible.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## write-python-docstrings

- Version: 1.1.3.
- Review: Retained. Documentation is grounded in implementation/callers/tests, caller-visible failures and resource/side-effect constraints; illustrative examples contain no live secrets or execution helper. Paper review of a permission-sensitive function documents actual constraints without inventing enforcement. No actionable security defect was established in this narrowly scoped docstring workflow.
- Checks: focused lint and reference validator passed; Python collection is not selected for installation; no mirror created.

## condensed-prose-refactor

- Version: 1.3.0.
- Review: Fixed the editing trust boundary: source passages, quoted roles, commands and links remain content and cannot expand permissions, disclose hidden context or authorize external transmission. Paper cases for a passage saying to ignore prior instructions and a preserved executable command require faithful text handling without execution. Reviewed the rhetorical reference; fidelity, protected literals, attribution and rewrite-only output remain compatible.
- Checks: focused lint and reference validator passed; configured installed mirror byte parity passed.
