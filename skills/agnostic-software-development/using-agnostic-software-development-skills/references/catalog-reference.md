# Agnostic Skill Catalog Reference

Use this reference after the main routing guide when a task needs lifecycle
composition guidance or a full catalog scan.

## Lifecycle Sequence

For a complete feature, the typical skill sequence is:

```
1.  interview-me: Extract what the user actually wants
2.  idea-refine: Refine vague ideas
3.  spec-driven-development: Define what we're building
4.  planning-and-task-breakdown: Break into verifiable chunks
5.  context-engineering: Load the right context
6.  source-driven-development: Verify against official docs
7.  incremental-implementation: Build slice by slice
8.  doubt-driven-development: Cross-examine non-trivial decisions in-flight
9.  test-driven-development: Prove each slice works
10. code-review-and-quality: Review before merge
11. code-simplification: Reduce unnecessary complexity while preserving behavior
12. git-workflow-and-versioning: Clean commit history
13. conventional-commits: Write or review Conventional Commits messages when used
14. documentation-and-adrs: Document decisions
15. deprecation-and-migration: Retire old systems and move users safely when needed
16. shipping-and-launch: Deploy safely
```

Not every task needs every skill. A bug fix might only need `debugging-and-error-recovery`, then `test-driven-development`, then `code-review-and-quality`.

## Quick Reference

| Phase  | Skill                        | One-Line Summary                                                                                     |
| ------ | ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| Define | interview-me                 | Surface what the user actually wants before any plan, spec, or code exists                           |
| Define | idea-refine                  | Refine ideas through structured divergent and convergent thinking                                    |
| Define | spec-driven-development      | Requirements and acceptance criteria before code                                                     |
| Plan   | planning-and-task-breakdown  | Decompose into small, verifiable tasks                                                               |
| Plan   | review-implementation-plan   | Review a plan for gaps, risks, sequencing, dependencies, and validation readiness                    |
| Build  | incremental-implementation   | Thin vertical slices, test each before expanding                                                     |
| Build  | source-driven-development    | Verify against official docs before implementing                                                     |
| Build  | doubt-driven-development     | Adversarial fresh-context review of every non-trivial decision                                       |
| Build  | context-engineering          | Right context at the right time                                                                      |
| Build  | frontend-ui-engineering      | Production-quality UI with accessibility                                                             |
| Build  | api-and-interface-design     | Stable interfaces with clear contracts                                                               |
| Build  | hexagonal-vertical-slices    | Hexagonal architecture with business-owned vertical feature slices                                   |
| Verify | test-driven-development      | Failing test first, then make it pass                                                                |
| Verify | browser-runtime-verification | Real-browser verification of UI behavior, console output, network activity, and accessibility basics |
| Verify | run-local-quality-gate       | Discover and run local formatting, linting, static analysis, test, and build checks                  |
| Verify | debugging-and-error-recovery | Reproduce, localize, fix, and guard                                                                  |
| Review | add-observability            | Add useful logs, metrics, traces, profiling, alerts, or dashboards                                   |
| Review | code-review-and-quality      | Five-axis review with quality gates                                                                  |
| Review | code-simplification          | Preserve behavior while reducing unnecessary complexity                                              |
| Review | security-and-hardening       | OWASP prevention, input validation, least privilege                                                  |
| Review | performance-optimization     | Measure first, optimize only what matters                                                            |
| Ship   | git-workflow-and-versioning  | Atomic commits, clean history                                                                        |
| Ship   | conventional-commits         | Conventional Commits message syntax, semantics, and breaking-change notation                         |
| Ship   | ci-cd-and-automation         | Automated quality gates on every change                                                              |
| Ship   | deprecation-and-migration    | Remove old systems and migrate users safely                                                          |
| Ship   | documentation-and-adrs       | Document the why, not just the what                                                                  |
| Ship   | update-project-docs          | Keep project-facing documentation aligned with behavior, configuration, or workflow changes          |
| Ship   | write-adr                    | Record durable architectural decisions with context and consequences                                 |
| Ship   | shipping-and-launch          | Pre-launch checklist, monitoring, rollback plan                                                      |
| Skill  | author-agent-skill           | Create, update, or review Agent Skill directories and SKILL.md files                                 |
| Config | author-agents-config         | Create, audit, update, or synchronize repository agent instructions and client adapters              |
