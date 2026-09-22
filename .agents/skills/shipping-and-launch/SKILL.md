---
name: shipping-and-launch
description: Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy.
metadata:
  version: "1.4.0"
  dependencies:
    tools: []
    skills:
      - name: add-observability
        purpose: Ensure launch, rollout, and rollback plans include meaningful operational signals.
        required: false
      - name: performance-optimization
        purpose: Address launch risks involving latency, throughput, resource usage, or scalability.
        required: false
      - name: debugging-and-error-recovery
        purpose: Prepare recovery steps for known failure modes, incidents, or rollback scenarios.
        required: false
---

# Shipping and Launch

## Overview

Ship with confidence. The goal is not just to deploy, but to deploy safely, with
monitoring in place, a recovery plan ready, and a clear understanding of what
success looks like. Make each launch observable and incremental when the system
allows it. Define a rollback, disablement, roll-forward, or compensation path for
changes that cannot be directly reversed.

## When to Use

- Deploying a feature to production for the first time
- Releasing a significant change to users
- Migrating data or infrastructure
- Opening a beta or early access program
- Any deployment that carries risk (all of them)

Use `add-observability` when launch readiness requires new logs, metrics, traces,
dashboards, alerts, or troubleshooting notes. Use `performance-optimization` when
launch readiness depends on diagnosing and fixing a performance bottleneck. Use
`debugging-and-error-recovery` when a launch, rollout, or rollback exposes an
active failure that needs root-cause repair.

## Steps

1. Identify the release scope, production risk, owners, target users, and planned
   launch window.
2. Complete the pre-launch checklist sections that apply to the release.
3. Use the supporting reference checklists for deeper security, performance, or
   accessibility verification when those risks apply.
4. Define the rollout sequence, monitoring thresholds, recovery triggers, and
   recovery path
   before changing production state.
5. Deploy incrementally, verify post-launch signals, and hold or execute the
   recovery plan when thresholds are missed.
6. Record launch evidence, accepted residual risks, cleanup owners, and any
   follow-up work after the release.

## Pre-launch readiness

Before changing production state, confirm that:

- required tests, builds, static checks, artifact generation, and review pass
- temporary code, debug output, sensitive logging, and known blocking failures are resolved
- configuration, secrets, migrations, infrastructure, networking, and artifacts are ready
- health checks, telemetry, dashboards, alerts, and ownership are in place
- user, operator, API, integration, runbook, changelog, and decision documentation is current where relevant
- security, performance, and accessibility checks are complete when those risks apply

Use `references/launch-readiness-checklist.md` for the full cross-cutting
checklist and monitoring categories. Use the focused security, performance, and
accessibility references when those risks apply. Record skipped checks, reasons,
accepted risk, and owners.

## Feature Flag Strategy

When the change can be controlled safely at runtime, ship behind a feature flag
or equivalent release control to decouple deployment from release:

### Feature Flag Lifecycle

1. Deploy with flag off: code is in production but inactive.
2. Enable for team or beta users: internal testing happens in the production environment.
3. Gradually roll out: increase exposure through risk-appropriate stages.
4. Monitor at each stage: watch error rates, performance, and user feedback.
5. Clean up: remove the flag and dead code path after full rollout.

### Feature Flag Rules

- Every feature flag has an owner and an expiration date
- Clean up flags within the agreed post-rollout cleanup window
- Do not nest feature flags because doing so creates exponential combinations
- Test both flag states (on and off) in CI

## Staged rollout

Define release-specific cohorts, observation windows, and advance, hold, or
recovery thresholds before launch. A common sequence is staging, production with
release control off, internal exposure, a small canary, increasing cohorts, and
full rollout. Advance only when representative evidence satisfies the defined
thresholds, and retain the ability to stop or reduce exposure at every stage.

Execute the recovery plan when a release-specific threshold is missed or a new
severe failure, data-integrity risk, or security issue appears. For a worked rollout
sequence and example decision table, see
`references/launch-planning-examples.md`.

## Monitoring and Observability

### What to monitor

Monitor signals that show user outcomes and system health: release-specific
business or workflow measures, errors, latency, traffic, resource saturation,
queue or dependency health, and client-side failures where relevant. Compare them
with the pre-launch baseline and the rollout thresholds.

### Error Reporting

When an error reaches a release boundary:

1. Record the exception type, operation, correlation ID, release version, and safe context.
2. Exclude secrets, credentials, raw personal data, and sensitive internals.
3. Return or display a safe recovery message to the user or caller.
4. Emit a metric or alert signal when the failure affects launch thresholds.
5. Preserve enough detail for operators to diagnose the issue from logs or traces.

### Post-Launch Verification

During the initial post-launch observation window:

1. Check the system's health, readiness, smoke, or equivalent operational signal.
2. Check the error monitoring dashboard for new error types.
3. Check the latency dashboard for regressions.
4. Test the critical user flow manually.
5. Verify logs are flowing and readable.
6. Confirm the recovery mechanism works, using a dry run if possible.

## Recovery strategy

Every deployment needs a recovery plan before it happens. Use rollback or
disablement when safe; otherwise define roll-forward or compensation steps.
Document triggers, decision ownership, commands or runbooks, data and state
handling, verification, communication, and recovery-time targets. Dry-run the
mechanism when practical. For a reusable example, see
`references/launch-planning-examples.md`.

## See Also

- For the detailed cross-cutting readiness checklist, see
  `references/launch-readiness-checklist.md`
- For security pre-launch checks, see `references/security-checklist.md`
- For performance pre-launch checklist, see `references/performance-checklist.md`
- For accessibility verification before launch, see `references/accessibility-checklist.md`
- For worked rollout and recovery examples, see `references/launch-planning-examples.md`

## Common Rationalizations

| Rationalization                                   | Reality                                                                                       |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| "It works in staging, it will work in production" | Production has different data, traffic patterns, and edge cases. Monitor after deploy.        |
| "We do not need feature flags for this"           | Every feature benefits from a kill switch. Even "simple" changes can break things.            |
| "Monitoring is overhead"                          | Not having monitoring means you discover problems from user complaints instead of dashboards. |
| "We will add monitoring later"                    | Add it before launch. You cannot debug what you cannot see.                                   |
| "Rolling back is admitting failure"               | Rolling back is responsible engineering. Shipping a broken feature is the failure.            |

## Red Flags

- Deploying without a rollback plan
- No monitoring or error reporting in production
- Big-bang releases (everything at once, no staging)
- Feature flags with no expiration or owner
- No one monitoring the deploy during the initial observation window
- Production environment configuration done by memory, not code
- "It is Friday afternoon, let us ship it"

## Verification

Before deploying:

- [ ] Applicable pre-launch checklist sections completed
- [ ] Feature flag configured (if applicable)
- [ ] Recovery plan documented
- [ ] Monitoring views and alerts set up
- [ ] Team notified of deployment

After deploying:

- [ ] Health, readiness, smoke, or equivalent operational check passes
- [ ] Error rate is normal
- [ ] Latency is normal
- [ ] Critical user flow works
- [ ] Logs are flowing
- [ ] Recovery mechanism tested or verified ready
