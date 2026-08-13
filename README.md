# ritebook-shelf

This repository is a [Ritebook](https://github.com/ondrej-winter/ritebook)
publisher catalog of reusable Agent Skills for software-development workflows.
Ritebook is a Python CLI for validating, publishing, registering, browsing, and
installing Agent Skill indexes.

The skills live under `skills/`. The generated `ritebook-index.json` file is the
reviewable catalog that lets Ritebook consumers register this Git-backed index,
browse available skills, and install selected skills into their own projects.

## Repository tools

- [Cline skill workflow](tools/cline-skill-workflow/README.md) recursively reviews
  or maintains every Agent Skill under `skills/`.