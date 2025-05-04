from pathlib import Path
import re
import requests
import urllib3

# Disable SSL warnings (only use in trusted environments)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
docs_root = Path("docs")                 # Traverse all subfolders
output_bib = Path("references.bib")      # Output .bib file

# Regex to extract DOI from markdown
doi_regex = re.compile(
    r"\*\*DOI\s*/\s*Link:\*\*\s*\[.*?\]\((https?://doi\.org/[^)]+)\)",
    re.IGNORECASE
)

# Headers for CrossRef API
headers = {
    "Accept": "application/x-bibtex",
    "User-Agent": "ResearchNotesBot/1.0 (mailto:you@example.com)"
}

entries = []

# --- Process each Markdown file ---
for note_file in sorted(docs_root.rglob("*.md")):
    if "templates" in note_file.parts:
        continue

    content = note_file.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Extract title from first markdown heading
    title_line = next((l for l in lines if l.startswith("# ")), note_file.stem)
    title = title_line.lstrip("# ").strip()

    # Try to find DOI
    match = doi_regex.search(content)

    if match:
        doi_url = match.group(1)
        doi_id = doi_url.split("doi.org/")[-1]

        try:
            response = requests.get(doi_url, headers=headers, timeout=10, verify=False)
            response.raise_for_status()
            bibtex = response.text.strip()
            entries.append(bibtex)
            print(f"✓ Fetched BibTeX for {note_file}")
        except Exception as e:
            print(f"⚠️  Failed to fetch DOI for {note_file.name}: {e}")
            fallback = f"""@article{{{note_file.stem},
  title = {{{title}}},
  doi = {{{doi_id}}},
  note = {{DOI fetch failed. From {note_file.name}}}
}}"""
            entries.append(fallback)
    else:
        print(f"⨯ No DOI found in {note_file}")
        fallback = f"""@misc{{{note_file.stem},
  title = {{{title}}},
  note = {{No DOI found. Source: {note_file.name}}}
}}"""
        entries.append(fallback)

# --- Write output .bib ---
output_bib.write_text("\n\n".join(entries), encoding="utf-8")
print(f"\n✔ Done. {len(entries)} entries written to {output_bib}")
