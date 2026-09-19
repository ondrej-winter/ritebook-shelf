RITEBOOK ?= uvx ritebook@latest
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf
FABRICA ?= uvx fabrica@latest

.PHONY: publish-index cline-skills cline-skills-dry-run
publish-index:
	$(RITEBOOK) indexes publish --skills-root $(SKILLS_ROOT) --index-name $(INDEX_NAME)

cline-skills:
	uv run tools/cline-skill-workflow/run_cline_skill_workflow.py

cline-skills-dry-run:
	uv run tools/cline-skill-workflow/run_cline_skill_workflow.py --dry-run --review-only

update-indexes:
	$(RITEBOOK) indexes update --all

commit:
	$(FABRICA) commit \
		--skill conventional-commits \
		--skill-root .agents/skills \
		--model gpt-5.6-luna \
		--reasoning-effort low
