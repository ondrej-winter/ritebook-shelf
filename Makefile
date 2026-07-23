RITEBOOK ?= uvx ritebook@latest
SKILLS_ROOT ?= skills
INDEX_NAME ?= ondrej-winter-ritebook-shelf

.PHONY: publish-index cline-skills cline-skills-dry-run
publish-index:
	$(RITEBOOK) publish-index --skills-root $(SKILLS_ROOT) --index-name $(INDEX_NAME)

cline-skills:
	uv run tools/cline-skill-workflow/run_cline_skill_workflow.py

cline-skills-dry-run:
	uv run tools/cline-skill-workflow/run_cline_skill_workflow.py --dry-run --review-only
