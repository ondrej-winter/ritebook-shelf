RITEBOOK ?= uvx ritebook@latest
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf
FABRICA ?= uvx fabrica@latest

.PHONY: publish publish-index update-indexes commit
publish: publish-index

publish-index:
	$(RITEBOOK) indexes publish --skills-root $(SKILLS_ROOT) --name $(INDEX_NAME)

update-indexes:
	$(RITEBOOK) indexes update --all

commit:
	$(FABRICA) commit \
		--skill conventional-commits \
		--skill-root .agents/skills \
		--model gpt-6-luna \
		--reasoning-effort low
