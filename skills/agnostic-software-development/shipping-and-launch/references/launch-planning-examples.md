# Launch Planning Examples

Use these examples to draft release-specific rollout and recovery plans. Replace
all cohorts, windows, thresholds, commands, and time targets with values justified
by the release risk and operating environment.

## Example Rollout Sequence

Tailor cohort sizes and observation windows to traffic volume, release risk,
time-to-detection, and how quickly recovery can complete. Do not advance merely
because an example time window elapsed; advance when the defined evidence is
sufficient.

1. Deploy to staging.
   - Run the full test suite in the staging environment.
   - Manually smoke test critical flows.
2. Deploy to production with the feature flag off.
   - Verify deployment succeeded with a health check.
   - Check error monitoring for new errors.
3. Enable for the team with the flag on for internal users.
   - Have the team use the feature in production.
   - Observe for a risk-appropriate period.
4. Start a canary rollout with the flag on for 5% of users.
   - Monitor error rates, latency, and user behavior.
   - Compare canary metrics against baseline metrics.
   - Observe long enough to collect representative evidence.
   - Advance only if all thresholds pass.
5. Gradually increase from 25% to 50% to 100%.
   - Repeat the same monitoring at each step.
   - Keep the ability to roll back to the previous percentage at any point.
6. Complete the full rollout with the flag on for all users.
   - Continue monitoring through the agreed stabilization period.
   - Clean up the feature flag after the stabilization period succeeds.

## Example Rollout Decision Thresholds

Replace these example values with release-specific thresholds, then use them to
decide whether to advance, hold, or execute the recovery plan at each stage:

| Metric                      | Advance (green)        | Hold and investigate (yellow) | Roll back (red)     |
| --------------------------- | ---------------------- | ----------------------------- | ------------------- |
| Error rate                  | Within 10% of baseline | 10-100% above baseline        | >2x baseline        |
| P95 latency                 | Within 20% of baseline | 20-50% above baseline         | >50% above baseline |
| New failure modes           | No new severe types    | Low-volume non-severe types   | Severe or growing   |
| Product or business metrics | Neutral or positive    | Decline <5% or unclear signal | Decline >5%         |

## When to Roll Back

Roll back immediately if:

- Error rate increases by more than 2x baseline
- P95 latency increases by more than 50%
- User-reported issues spike
- Data integrity issues detected
- Security vulnerability discovered

## Recovery plan example

Every deployment needs a recovery plan before it happens. Use rollback or
disablement when safe; otherwise define roll-forward or compensation steps:

```markdown
## Recovery Plan for [Feature/Release]

### Trigger Conditions

- Error rate > 2x baseline
- P95 latency > [X]ms
- User reports of [specific issue]

### Rollback Steps

1. Disable feature flag (if applicable)
   OR
1. Deploy or restore the previous known-good version: `<rollback_command>`
1. Verify rollback: health check, error monitoring
1. Communicate: notify team of rollback

### Alternative Recovery Steps

- If rollback is unsafe or impossible, disable exposure, roll forward, or execute
  the tested compensation procedure: `<recovery_command_or_runbook>`

### Data and State Considerations

- Migration, schema change, configuration change, or state transition [X] has a tested rollback or compensation plan
- Data written by the release is [preserved / migrated back / cleaned up / reconciled]

### Recovery Time Targets

- Feature flag: < 1 minute
- Redeploy previous version: < 5 minutes
- Database rollback: < 15 minutes
```
