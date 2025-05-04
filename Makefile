
.PHONY: help newnote serve deploy activate

help:
	@echo "Usage:"
	@echo "  make newnote TITLE='My New Note'"
	@echo "  make serve         # Run mkdocs server (background)"
	@echo "  make deploy        # Deploy to GitHub Pages"
	@echo "  make activate      # Activate the virtual environment (uv)"
	@echo "  make bib           # Generate references.bib from notes"

newnote:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: You must provide a TITLE variable."; \
		exit 1; \
	fi
	@slug=$$(echo "$(TITLE)" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g'); \
	file=docs/notes/$${slug}.md; \
	if [ -f "$$file" ]; then \
		echo "Note already exists: $$file"; \
		exit 1; \
	fi; \
	cp docs/notes/note-template.md $$file; \
	sed -i "1s/.*/# $(TITLE)/" $$file; \
	echo "  - $(TITLE): notes/$${slug}.md" >> mkdocs.yml; \
	echo "Created $$file and updated mkdocs.yml"

serve:
	@mkdocs serve

deploy:
	@mkdocs gh-deploy

activate:
	@echo "Run: source .venv/bin/activate"

bib:
	@python generate_bib.py
	@echo "✔ references.bib updated."