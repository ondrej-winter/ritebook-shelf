# ritebook-shelf

This repository is a [Ritebook](https://github.com/ondrej-winter/ritebook)
publisher catalog of reusable Agent Skills for software-development workflows.
Ritebook is a Python CLI for validating, publishing, registering, browsing, and
installing Agent Skill indexes.

The skills live under `skills/`. The generated `ritebook-index.json` file is the
reviewable catalog that lets Ritebook consumers register this Git-backed index,
browse available skills, and install selected skills into their own projects.

## Repository state

The repository tracks four related forms of skill state:

- `skills/` is the canonical authored source. Make skill changes there first.
- `ritebook-index.json` is generated publisher state. Regenerate it with Ritebook,
  review it, and commit it; do not edit it by hand.
- `.agents/skills/` is the checked-in installed mirror selected by
  `ritebook.toml`. Keep it byte-identical to the configured canonical skills and
  do not maintain it as an independent source.
- `ritebook.lock` is generated consumer provenance. It records the exact Git
  revision and index digest used to install `.agents/skills/`; regenerate it only
  through `skills sync`.

Run the read-only local consistency gate with:

```bash
make check-ritebook-state
```

The gate uses Ritebook 0.1.48 by default. It regenerates an index in a temporary
directory, compares it with the checked-in index while ignoring only
`generated_at`, expands every requirement in `ritebook.toml`, verifies canonical
and installed directory contents, and checks the lock against its exact Git
revision and index digest. It does not rewrite tracked repository files.

## Maintenance workflow

Ritebook installs only from the immutable revision bound by the registered index.
`skills sync` does not publish local changes or advance that binding. This makes
catalog publication and consumer synchronization two explicit phases.

### When canonical skill or catalog metadata changed

1. Edit `skills/` and update the corresponding `.agents/skills/` mirror in the
   same change. Do not run consumer sync against the old registered revision,
   because that would restore the previously published bytes.
2. Generate and review the publisher index:

   ```bash
   make publish-index
   ```

3. Commit and push the canonical skills, installed mirror, and generated index.
   The lock cannot attest uncommitted skill bytes.
4. Refresh the registered Git-backed index to the published commit:

   ```bash
   make update-index
   ```

5. Reinstall every requirement and regenerate the lock:

   ```bash
   make sync-skills
   ```

6. Verify the resulting state:

   ```bash
   make check-ritebook-state
   ```

Review and commit the regenerated `ritebook.lock` separately from the publication
commit when the publication commit must already be reachable by the registered
Git source.

### When the committed index already matches canonical skills

Do not republish merely to refresh `generated_at`. Update the registered index,
run the full sync, and run the consistency gate:

```bash
make update-index
make sync-skills
make check-ritebook-state
```

Ritebook 0.1.48 assigns a new `locked_at` timestamp and rewrites `ritebook.lock`
on every successful sync. A repeated sync is therefore expected to preserve all
installed bytes and all other lock fields while changing only `locked_at`.