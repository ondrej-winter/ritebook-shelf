# Repository instructions

## Repository orientation

This repository publishes a Ritebook catalog of reusable Agent Skills.

- `skills/` is the canonical authored skill source.
- `.agents/skills/` is the installed mirror selected by `ritebook.toml`. Edit the
  canonical source first and synchronize the installed copy; do not maintain the
  two trees independently.
- `ritebook-index.json` is generated catalog state. Regenerate it through the
  repository's Ritebook workflow instead of editing it by hand.
- `ritebook.lock` records installed provenance. Change it only through an
  explicitly authorized Ritebook install or update workflow.
- The root `.clinerules/` directory is the canonical reusable Cline bootstrap.
  Its packaged copies under `author-agents-config/assets/clinerules/` must remain
  byte-identical.

## Working rules

- Inspect the working tree and relevant source files before editing. Preserve
  unrelated user changes and existing project ownership decisions.
- Follow the relevant task procedure under `.agents/skills/` when its trigger
  matches. Keep durable repository policy here and Cline-only mechanics in
  `.clinerules/`.
- When a canonical skill changes, update its version as required by
  `author-agent-skill`, synchronize its installed copy, and review generated
  catalog state.
- Do not address unrelated audit findings or perform opportunistic migrations.

## Validation and completion

- Run focused checks for the affected skill or documentation before broader
  repository validation.
- For skill changes, run Ritebook lint and the open Agent Skills reference
  validator when available.
- Verify canonical-to-installed parity and any declared template parity before
  handoff.
- Report checks actually run, distinguish documented compatibility from observed
  runtime behavior, and identify any unverified or deferred work.

## Git and external actions

Local inspection, editing, and validation are allowed in Act mode. Creating a
commit, pushing, publishing or refreshing Ritebook indexes, mutating another
local repository or any remote system, and running destructive commands require
an explicit user request. Approval for one named operation does not authorize
other Git, publication, remote, or destructive actions.