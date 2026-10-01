RITEBOOK_VERSION ?= 0.1.48
RITEBOOK ?= uvx ritebook@$(RITEBOOK_VERSION)
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf
INDEX_ALIAS ?= $(INDEX_NAME)
PYTHON ?= python3
FABRICA ?= uvx fabrica@latest

.PHONY: publish publish-index update-index update-indexes sync-skills check-ritebook-state commit
publish: publish-index

publish-index:
	$(RITEBOOK) indexes publish --skills-root $(SKILLS_ROOT) --name $(INDEX_NAME)

update-index:
	$(RITEBOOK) indexes update $(INDEX_ALIAS)

update-indexes:
	$(RITEBOOK) indexes update --all

sync-skills:
	$(RITEBOOK) skills sync --file ritebook.toml --force --lockfile ritebook.lock

check-ritebook-state:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) scripts/check_ritebook_state.py \
		--ritebook-command '$(RITEBOOK)'

commit:
	$(FABRICA) commit \
		--skill conventional-commits \
		--skill-root .agents/skills \
		--model gpt-6-luna \
		--reasoning-effort low
