# Research Notes Template

A template repository for creating structured, version-controlled summaries of scientific articles using [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## 📑 Table of Contents

- [How to Use](#-how-to-use)
- [Project Structure](#-structure)
- [Makefile Commands](#-makefile-commands)
- [Generating references.bib](#-generating-referencesbib)
- [License](#-license)

---

## 🔧 How to Use

### 1. Use This Template

Click the button below to create a new repository from this template:

[![Use this template](https://img.shields.io/badge/Use%20this-template-blue?style=for-the-badge)](https://github.com/Obadowski/research-notes-template/generate)

---

### 2. Clone and Set Up

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_NEW_REPO.git
cd YOUR_NEW_REPO

# Create environment (using uv)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```
---
### 3. Add Your Notes

- Create new files in `docs/notes/`
- Use the provided template: `docs/templates/note-template.md`
- Update the navigation in `mkdocs.yml` under the `nav:` section

---

### 4. Preview Locally

Run the local server:

    mkdocs serve

Then open your browser at:

    http://127.0.0.1:8000

---

### 5. Publish to GitHub Pages

Build and deploy:

    mkdocs gh-deploy

Then go to GitHub:

- Settings → Pages
- Source: `gh-pages` branch
- Click “Save”

Your site will be available at:

    https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/

---

## 📁 Structure

    .
    ├── mkdocs.yml
    ├── requirements.txt
    ├── docs/
    │   ├── index.md
    │   ├── examples/
    │   │  └── example-note.md
    │   ├── notes/
    │   │  └── note-template.md
    │   └── templates/
    │      └── note-template.md
---

## 🛠 Makefile Commands

This project includes a `Makefile` to simplify common tasks:

### ✅ Create a New Note

Generates a new Markdown file based on the template and appends it to `mkdocs.yml`.

```bash
make newnote TITLE="Your Note Title"
```

- Converts the title into a slug.
- Copies the note-template.md to docs/notes/.
- Replaces the # Title line.
- Adds entry to the nav: section of mkdocs.yml.

### ✅ Run MkDocs Server
Starts the MkDocs development server:
```bash
make serve
```

### ✅ Deploy to GitHub Pages
Builds and pushes to the gh-pages branch:
```bash
make deploy
```

### ✅ Environment Activation
Prints the command to activate your uv virtual environment:
```bash
make activate
```

### ✅ Help
List all available commands: (Nobody can remember everything all the time)
```bash
make help
```
---

## 🧾 Generating `references.bib`

The project includes a script to extract DOI links from all notes and automatically fetch full BibTeX entries using the CrossRef API.

### 🔁 How it works

- Recursively scans all `.md` files inside `docs/` (excluding `templates/`)
- Searches for lines like:

```markdown
**DOI / Link:** [Some Link](https://doi.org/10.XXXX/abc123)
```
- Fetches full BibTeX entries using CrossRef
- Writes output to references.bib

### ▶️ Usage
```bash
make bib
```
This runs generate_bib.py and updates references.bib in the project root.

---

## 📄 License

See: https://obad.mit-license.org/
