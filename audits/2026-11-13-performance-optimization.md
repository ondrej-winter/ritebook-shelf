# Skill performance audit — 2026-11-13

Reviewed one skill at a time in `AUDIT_TRACKING.md` order using
`performance-optimization`, including each skill’s bundled resources.
These packages primarily contain instructions and templates. Findings about
measurement quality and bounded work are workflow design reviews, not measured
runtime speedups. No application performance claim follows from a prose change.
No-change entries mean no actionable performance defect was established within
this review; they do not certify future applications or host runtimes.

Every completed entry passes focused Ritebook 0.1.63 lint, skills-ref 0.1.0
validation, and parity for its configured installed mirror. Walkthroughs are
paper review evidence unless execution is explicitly recorded. Runtime behavior,
automatic discovery, production workloads, and external integrations remain
unverified unless separately stated. No speculative runtime optimization is
implemented without comparable measurements. Catalog and lock are inspected
without regeneration or provenance changes.

Audit completed: **43 of 43** skills reviewed; **4** updated and **39** retained.
Only performance-optimization goals were checked in the tracker.

Changed versions:

| Skill | Before | After | Result |
| --- | --- | --- | --- |
| deprecation-and-migration | 1.2.4 | 1.3.0 | Bound migration load, checkpoint and resume work |
| incremental-implementation | 2.1.4 | 2.2.0 | Require measurement as well as correctness before optimization |
| performance-optimization | 1.4.5 | 1.5.0 | Validate offered load, bound cache capacity and discard ineffective changes |
| bootstrap-python-app | 1.5.1 | 1.6.0 | Default the initial test suite to serial execution; retain opt-in xdist |

Final verification:

- `ritebook skills lint --root skills`: 43 skills passed with Ritebook 0.1.63.
- `ritebook skills lint --root .agents/skills`: 33 mirrors passed.
- `skills-ref validate <skill-directory>`: all 43 canonical skills passed with
  skills-ref 0.1.0, individually before moving to the next entry.
- Focused Ritebook lint used an isolated temporary parent scan root containing
  one skill. Scanning the skill directory itself produces an invalid catalog
  path of `.` in this Ritebook version; no source changes were made to satisfy
  that tool limitation.
- Validators ran directly from existing local uv tool environments. No network
  install or dependency refresh was performed. The uv launcher could not write
  its cache under the sandbox, so existing cached executables were used instead.
- All 33 canonical/installed packages and all three Cline bootstrap copies are
  byte-identical. The 10 Python skills are not selected by `ritebook.toml`; no
  installed Python tree was created.
- Tracker order, 43 report anchors, local links, unchanged other audit goals,
  rendered bootstrap TOML and `git diff --check` passed.
- Catalog inspection found 43 entries agreeing with canonical paths and
  descriptions; its schema carries no skill versions or content hashes.
  `ritebook-index.json`, `ritebook.lock` and `.ritebook/` provenance were unchanged.
- Bootstrap runtime evidence includes one warmup and six timed runs in each
  comparison mode, followed by one warmup and six timed post-edit default runs.
  Every run passed all four tests with 100% coverage; the 93% floor and branch
  collection remained enabled. [Raw samples and fixture conditions](2026-11-13-bootstrap-performance.json)
  record commands and the local environment. Synthetic installed metadata and
  explicit cached plugin loading avoid a dependency install; this is not a
  complete scaffold build, wheel test, ordinary plugin-autoload comparison,
  or hosted CI observation.
- Changes are unstaged and uncommitted. No index refresh, Ritebook install,
  provenance update, commit, push or publication was performed. Installed mirror
  synchronization reflects local authored edits, not a new verified installation.
- Automatic agent discovery, model token/latency effects, external providers,
  production load and the full generated-application gate were not exercised.
  Workflow additions received paper walkthroughs and package checks; they do
  not establish application performance gains. No required review item remains.

## add-observability

- Version: 1.4.1.
- Review: No change. Source and telemetry checklist already bound buffering, retries, label cardinality, event volume and profile duration; they require representative-load overhead checks and comparable evidence for improvement claims. Walkthrough: exporter failure must preserve workflow behavior and expose dropped telemetry; per-item hot-loop logs are rejected.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## api-and-interface-design

- Version: 1.3.4.
- Review: No change. Main workflow and boundary checklist already define collection limits, streaming backpressure, cancellation, deadlines, freshness and consumer compatibility. Walkthrough: paginating a complete-result API requires a consumer migration; a timeout does not justify blindly retrying provider work.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## author-agent-skill

- Version: 2.1.1.
- Review: No change. Conditional resource loading, minimal supporting material, focused-before-broad checks and nonrecursive skill routing already limit unnecessary work. Walkthrough: an optional reference loads only for its relevant branch; a structural pass cannot establish runtime efficiency or discovery.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## author-agents-config

- Version: 1.3.0.
- Review: No change. Conditional references, scoped policy, minimal adapters, metadata-only capability discovery and idempotent reconciliation avoid redundant loading and regeneration. Assets contain no execution loop. Walkthrough: adding a supported native client creates no duplicate adapter; repeating reconciliation preserves unchanged bytes. Dated host compatibility was retained without a runtime claim.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## browser-runtime-verification

- Version: 1.2.0.
- Review: No change. The workflow selects minimal risk-covering scenarios, reuses suitable running builds, uses bounded condition waits, checks request counts and timing, and restores throttling. Walkthrough: persistent background traffic does not force an endless network-idle wait; a screenshot alone cannot substantiate responsiveness.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## ci-cd-and-automation

- Version: 1.7.0.
- Review: No change. Optimization already starts from measured queue/job durations; independent jobs may run concurrently, cold caches must work, selective checks retain dependency coverage, and retries/timeouts are bounded. Walkthrough: a faster path filter cannot skip a required gate; deployment writes remain serialized and interruption-safe.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## code-review-and-quality

- Version: 1.4.0.
- Review: No change. The performance reference already distinguishes static cost from measured impact, requires representative scale and comparable revisions/cache states, and checks fan-out, cache misses and resource tradeoffs. Walkthrough: a faster average cannot establish tail-latency improvement; missing runtime evidence yields a concrete measurement follow-up rather than fabricated timings.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## code-simplification

- Version: 1.1.6.
- Review: No change. Existing rules preserve required performance and timing assumptions, inspect historical performance reasons and consumers, and validate one small refactor at a time. Walkthrough: replacing streaming with an eager collection is not justified by shorter syntax; no speedup can be inferred from fewer lines.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## context-engineering

- Version: 1.1.6.
- Review: No change. Focused file selection, compact packets, minimal failure excerpts and evidence freshness already constrain context volume and repeated investigation. Walkthrough: a module switch refreshes relevant evidence rather than loading every repository file; old validation cannot certify a new revision.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## conventional-commits

- Version: 1.1.3.
- Review: No change. This package formats a scoped message and has no helper, dependency scan or runtime hot path. It reads only the requested diff and does not create commits. Walkthrough: a staged-message task excludes unstaged changes and returns a message without running application checks or release automation.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## debugging-and-error-recovery

- Version: 1.2.4.
- Review: No change. Reproduction, localization, narrow guards and widening validation avoid speculative fixes and repeated full suites; performance tuning is explicitly routed to measured diagnosis. Walkthrough: a slow timeout is first reproduced and its partial side effects reconciled; broad retries cannot hide it.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## deprecation-and-migration

- Version: 1.3.0.
- Review: Workflow design gap: staged and parallel migration guidance did not bound backfill work or combined transitional load. Added batch/concurrency/rate/retry limits, durable checkpoints, pause/resume, and representative throughput/live-budget checks before scaling. Walkthrough: an interrupted backfill resumes from durable progress; shadow load is included in the capacity budget. Guidance only; no backfill executed and no runtime speedup claimed. Existing skill routing and inputs remain compatible.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## documentation-and-adrs

- Version: 1.3.3.
- Review: No change. The routing workflow selects the smallest durable artifact and specialized owner, passes a bounded brief, and avoids duplicate policy or unnecessary file creation. Walkthrough: an already-known README task goes directly to project-doc maintenance; no recursive catalog loading or runtime tuning is required.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## doubt-driven-development

- Version: 1.2.3.
- Review: No change. The three-cycle stop condition, smallest reviewable artifact, nonrecursive orchestration and explicit external-review cost/latency tradeoff already bound work. Walkthrough: substantive findings after cycle three escalate instead of triggering an unbounded reviewer tree; trivial mechanical edits bypass this workflow.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## frontend-ui-engineering

- Version: 1.3.4.
- Review: No change. Dedicated performance guidance already checks redundant requests/renders, asset size, layout shifts, input-blocking work and bounded rendering; claims require before/after evidence and browser verification. Walkthrough: a long-list change uses project budgets and representative measurements, while keyboard/focus and error states remain required.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## git-workflow-and-versioning

- Version: 1.3.3.
- Review: No change. The workflow uses scoped diffs, bounded log examples and atomic validation without adding history scans or automatic worktree creation. Walkthrough: a handoff inspects current state and reports local/remote evidence separately; no benchmark or Git optimization is justified by this static package.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## hexagonal-vertical-slices

- Version: 1.2.1.
- Review: No change. Guidance avoids chatty slice boundaries, unnecessary interfaces and rich domain hydration for read-only queries; ports follow use-case operations instead of driver CRUD. Walkthrough: a projection can serve query-heavy work without bypassing ownership, and adding a seam does not justify a repository-wide abstraction. No implementation bottleneck was established.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## idea-refine

- Version: 2.0.0.
- Review: No change. Reviewed all three references and executed the optional directory helper in an isolated local fixture: 20 fresh-directory subprocess runs median 42.16 ms (35.50–48.26), 20 existing-directory runs median 46.36 ms (41.81–55.77). Every run returned correct JSON/status. This is local shell/Python startup plus filesystem cost, not agent-session latency. No user latency target or bottleneck justifies replacing its JSON-safe implementation; no after-measurement or new benchmark guard is needed because no optimization was made. The workflow already bounds variations and loads frameworks selectively.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## incremental-implementation

- Version: 2.2.0.
- Review: Workflow design gap: simplicity guidance allowed optimization after correctness tests alone and unconditionally recommended a naive implementation. It now respects known workload/resource limits and requires a representative baseline, identified bottleneck, comparable remeasurement and regression guard. Walkthrough: a correct but unbounded prototype does not satisfy a known resource budget; green unit tests do not prove speed. Instruction change only, with existing activation and outputs preserved; runtime-unverified.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## interview-me

- Version: 2.0.1.
- Review: No change. Reviewed full workflow and examples. Adaptive depth, one high-value unknown per turn, compact unchanged turns and an explicit stop condition avoid unnecessary exploration. Walkthrough: a precise request bypasses the interview; a stable full-mode model uses a compact update rather than repeating the complete history. No runtime helper or measured latency problem exists.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## performance-optimization

- Version: 1.5.0.
- Review: Workflow design findings: successful-request latency could hide reduced offered load and overload failures; cache guidance allowed TTL as the sole capacity bound; failed experiments had no explicit discard decision. Added load-generator validity and offered/achieved/error accounting, entry/byte and in-flight fill bounds, and discard/revise guidance; aligned the checklist. Walkthrough: low latency with increasing timeout counts is not a win; expiring entries do not establish a memory cap during a traffic burst; a neutral patch is not retained as a speedup. Reviewed all three references and preserved qualified historical web thresholds. No load test or runtime cache change was made; guidance remains runtime-unverified.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## planning-and-task-breakdown

- Version: 2.2.2.
- Review: No change. Reviewed workflow and plan asset. Reused canonical plans, bounded spikes, focused iteration checks and meaningful shared checkpoints already avoid redundant planning and broad-suite repetition. Walkthrough: independent branches need genuine write/environment independence and a join; an unknown performance check stays unresolved rather than becoming a passing placeholder.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## review-implementation-plan

- Version: 1.3.3.
- Review: No change. The review keeps the existing plan, scopes depth to risk, separates focused/final checks and flags expensive or flaky validation without starting implementation. Walkthrough: an unknown required check prevents affected work being called ready; completed evidence and stable task IDs survive revision. No measurement-driven optimization of this instruction-only workflow is established.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## run-local-quality-gate

- Version: 1.4.3.
- Review: No change. The skill discovers aggregate and narrow commands, sequences fast feedback first, avoids broad cleanup and unsupported setup, and explicitly reports partial gates. Walkthrough: a missing integration prerequisite does not become a pass; a scoped lint precedes the full scan. No extra cache, parallel runner or redundant test framework is warranted.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## security-and-hardening

- Version: 1.1.9.
- Review: No change. Workflow and checklist already constrain input/file/archive resource use, rate limits, quotas and retries while preserving per-operation authorization and safe password hashing. Walkthrough: faster access cannot bypass tenant checks; oversized input is rejected at the boundary. This performance review does not re-certify algorithm choices or current security advisories.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## shipping-and-launch

- Version: 1.6.4.
- Review: No change. Main workflow and all five references already use release-specific budgets, production-scale checks, latency/error/saturation monitoring and evidence-based advance/hold/recover thresholds. Walkthrough: a low-traffic canary cannot advance simply because its window elapsed; a faster release must still preserve supported data and recovery combinations. No deployment or load test was run.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## source-driven-development

- Version: 1.2.3.
- Review: No change. Exact source-sensitive decisions, locally detected versions and narrow official sections avoid whole-site research; documentation and runtime evidence remain distinct. Walkthrough: a current API question first resolves its installed version and relevant source, while an unrelated local rename does not trigger research. No executable path or measured research bottleneck exists.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## spec-driven-development

- Version: 2.1.2.
- Review: No change. Workflow and template already replace vague speed goals with measurable outcomes, units, workload/environment conditions and sourced targets; small precise work avoids a separate spec. Walkthrough: an invented p95 threshold remains a proposal, while an agreed quantitative limit maps to a concrete acceptance measurement. No application is generated by this package.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## test-driven-development

- Version: 1.3.4.
- Review: No change. Reviewed workflow and test patterns. Narrow behavior tests, fast majority coverage, selective expensive boundary tests and avoidance of unchanged reassurance runs already constrain feedback cost. Walkthrough: an integration risk cannot be hidden by fast mocks; performance claims still require the separate measurement workflow rather than a green correctness test. Noise characterization is purposeful measurement, not reassurance rerunning.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## update-project-docs

- Version: 1.3.3.
- Review: No change. Existing canonical-surface selection, affected-section edits, short examples and generated-source ownership avoid documentation duplication and unnecessary rewrites. Walkthrough: a changed configuration default updates its existing reference with verified semantics; unrelated prose is preserved. No executable or measured performance bottleneck was found.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## using-agnostic-software-development-skills

- Version: 2.5.4.
- Review: No change. Main routing and catalog reference explicitly avoid a universal lifecycle and recursive optional activation; each handoff carries existing evidence and scope. Walkthrough: an explicit performance audit selects measurement-driven review without launching every catalog workflow. The conditional catalog reference remains deferred until composition detail is needed.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## write-adr

- Version: 1.2.3.
- Review: No change. Number selection scans filenames in the known ADR directory, rechecks allocation safely and updates one existing index. The template records one decision without duplicating implementation plans. Walkthrough: an occupied number is recomputed instead of overwritten; a partial retry inspects the existing index. No scalable runtime path or measured issue exists.
- Checks: focused lint and reference validator passed; installed mirror byte parity.

## add-hexagonal-feature

- Version: 1.1.3.
- Review: No change. The feature workflow creates only needed domain objects/ports/adapters, uses small fakes for unit feedback and checks the real wired entry point separately. Walkthrough: fake-only success cannot certify I/O latency or complete integration; a new feature does not trigger speculative caching or repository-wide abstraction. No measured runtime workload was supplied.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## bootstrap-python-app

- Version: 1.6.0.
- Review: Measured defect: the four-test bootstrap default started automatic xdist workers on every local/CI/pre-commit run. Same rendered CLI/test fixture, coverage enabled, Python 3.14.10, pytest 9.1.1, xdist 3.8.0, coverage 7.15.4, macOS arm64/10 logical CPUs: six interleaved measured runs per mode after one warmup gave automatic median 4.096 s (3.733–4.628) and serial median 1.183 s (1.072–1.337). Removed only the automatic worker option; preserved xdist as explicit opt-in, coverage reporting, branch collection and 93% floor. Six fresh post-edit serial measurements gave median 1.078 s (1.033–1.213); every warmup/measured run passed four tests with 100% coverage. Target: avoid worker startup for the minimal suite while retaining checks; met in this fixture. Guard: serial default in the template and documented measurement before enabling parallel defaults. Rendered TOML parsed and policy assertions passed. Raw samples, output and reproduction conditions: [benchmark evidence](2026-11-13-bootstrap-performance.json). This fixture uses synthetic installed metadata and explicit cached plugins; it does not establish clean-wheel, full generated-project, hosted CI or larger-suite speedups. Existing projects are not migrated.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## python-add-adapter

- Version: 1.0.5.
- Review: No change. Adapters preserve port limits, bound technical timeouts/retries, own resource cleanup, and must not hide synchronous I/O behind async callers. Lightweight package initialization and focused boundary tests avoid unnecessary loading/testing. Walkthrough: a lost write response reconciles outcome before replay; a mock transport pass cannot prove real dependency latency.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## python-add-env-settings-adapter

- Version: 1.0.5.
- Review: No change. Reviewed all templates and docs. The composition root loads configuration once and shares an immutable slots DTO; repeated environment/dotenv reads are excluded from application hot paths. Walkthrough: service construction receives the already-loaded DTO instead of creating EnvSettings for every request. No global cache was added because it would change freshness and test isolation without a measured need; template runtime tests were not rerun for this unchanged package.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## python-add-port

- Version: 1.0.4.
- Review: No change. The port workflow already defines collection bounds, sync/async behavior and operation semantics, avoids full-driver mirrors, and directs verification to actual consumers rather than meaningless interface tests. Walkthrough: an adapter cannot silently choose unbounded collection behavior; declaring a Protocol alone neither proves conformance nor latency.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## python-build-extensible-cli

- Version: 1.1.4.
- Review: No change. Workflow and shell-pattern reference already parse once, keep registration/decoding free of expensive construction, lazily build only selected-command dependencies and keep help/version offline. Walkthrough: requesting version cannot open unselected clients; repeated invocations retain no parser state. No runtime implementation or representative startup regression was supplied to justify import machinery changes.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## split-python-module

- Version: 1.1.3.
- Review: No change. Responsibility-based splitting, lightweight package exports, import-time behavior inspection and focused smoke tests already avoid needless modules/eager side effects. Walkthrough: preserving a public re-export also requires checking initialization and dynamic consumers; a file split is not claimed to reduce startup time without a baseline.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## using-python-software-development-skills

- Version: 3.0.1.
- Review: No change. Routing selects only triggered Python mechanics and reads project-owned command definitions directly instead of invoking wrapper skills for every tool. Walkthrough: adding a single adapter does not activate bootstrap or module splitting; a completed port procedure does not substitute for full feature integration evidence.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## write-pytest-tests

- Version: 1.1.4.
- Review: No change. Minimal fixtures, parametrized distinct cases, isolated boundaries and narrow-first validation already limit test cost without assuming more workers are faster. Walkthrough: a large implicit fixture is replaced only for a real test need; existing project options remain authoritative rather than being bypassed to improve timing. No helper or test-runner implementation is bundled.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## write-python-docstrings

- Version: 1.1.3.
- Review: No change. The workflow limits documentation to useful contracts, avoids repeated type information, documents iterator/resource lifetime, and selects narrow validation. Walkthrough: a lazy iterator documents when work happens and who closes it; a trivial helper receives no boilerplate. No executable performance path exists.
- Checks: focused lint and reference validator passed; Python collection is not installed; no mirror created.

## condensed-prose-refactor

- Version: 1.2.0.
- Review: No change. Main instructions and rhetorical reference already defer optional author material, bound default variants, allow no-op edits, preserve protected content and require fidelity before compression. Walkthrough: a short technical edit avoids the author library and keeps qualified latency claims unchanged. Smaller prose alone is not reported as lower token cost, model latency or better task performance.
- Checks: focused lint and reference validator passed; installed mirror byte parity.
