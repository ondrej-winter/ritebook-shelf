RITEBOOK ?= uvx ritebook@latest
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf
INDEX_ALIAS ?= $(INDEX_NAME)
FABRICA ?= uvx fabrica@latest

.PHONY: publish-index update-indexes sync-skills check-ritebook-state commit

publish-index:
	$(RITEBOOK) indexes publish --skills-root $(SKILLS_ROOT) --name $(INDEX_NAME)

update-indexes:
	$(RITEBOOK) indexes update --all

sync-skills:
	$(RITEBOOK) skills sync --force

commit:
	$(FABRICA) commit \
		--skill conventional-commits \
		--skill-root .agents/skills \
		--model gpt-6-luna \
		--reasoning-effort low
