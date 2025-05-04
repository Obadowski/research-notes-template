# Research Notes Template

A template repository for creating structured, version-controlled summaries of scientific articles using [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

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
    │   ├── notes/
    │   │   └── en/
    │   │       └── note-template.md
    │   └── templates/
    │       └── note-template.md

---

## 📄 License

See: https://obad.mit-license.org/
