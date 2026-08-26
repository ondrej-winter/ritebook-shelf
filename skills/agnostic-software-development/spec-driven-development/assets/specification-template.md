# Specification: [Project or Feature Name]

## Objective

[Describe what is being built, for whom, and why it matters.]

## Current Context

[Describe relevant existing behavior, files, systems, workflows, constraints,
and dependencies.]

## Assumptions

- [State an unconfirmed belief that affects requirements or implementation, and
  explain how it will be confirmed or tested.]

## Desired Behavior

[Define the required functional, operational, data, interface, or workflow
behavior. Include observable outcomes and important failure behavior.]

## Commands and Validation

- Build: `<confirmed_build_command>`
- Test: `<confirmed_test_command>`
- Lint or static checks: `<confirmed_lint_or_check_command>`
- Manual verification: [Describe the manual check when applicable.]

Use `Not applicable` when a validation category genuinely does not apply. Keep an
unknown command visible as an open question rather than inventing one.

## Project Structure

- Specification: `docs/specs/<name>-spec.md`
- `<source_location>`: [Implementation responsibility.]
- `<test_location>`: [Test responsibility.]
- `<docs_location>`: [Documentation responsibility.]

## Conventions and Constraints

[Describe relevant naming, formatting, error-handling, logging, API,
accessibility, security, privacy, compatibility, platform, or operational
requirements. Mark individual concerns as not applicable only when supported by
project evidence or user confirmation.]

## Testing Strategy

[Describe the test levels, fixtures, edge cases, failure cases, and acceptance
checks that will demonstrate conformance with this specification.]

## Boundaries

- Always: [Required practices or invariants.]
- Ask first: [Scope-expanding, destructive, costly, or risky actions.]
- Never: [Explicitly prohibited behavior or changes.]

## Success Criteria

- [State a specific, observable, and verifiable outcome.]

## Open Questions

- [Record an unresolved decision, its impact, and the person or evidence needed
  to resolve it when known.]