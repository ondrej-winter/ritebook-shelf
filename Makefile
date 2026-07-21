RITEBOOK ?= uvx ritebook@latest
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf

.PHONY: publish-index
publish-index:
	$(RITEBOOK) publish-index --skills-root $(SKILLS_ROOT) --index-name $(INDEX_NAME)
