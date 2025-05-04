from pathlib import Path
import re

# Path to notes and output
notes_dir = Path("docs/notes")
output_bib = Path("references.bib")

# Matches: **DOI / Link:** [Text](https://doi.org/xxx)
doi_regex = re.compile(r"\*\*DOI\s*/\s*Link:\*\*\s*\[.*?\]\((https?://doi\.org/[^)]+)\)", re.IGNORECASE)

# Stores .bib entries
entries = []

# Iterate over all .md files in docs/notes/
for note_file in sorted(notes_dir.glob("*.md")):
    lines = note_file.read_text(encoding="utf-8").splitlines()

    # Try to extract title from first line
    title_line = next((l for l in lines if l.startswith("# ")), note_file.stem)
    title = title_line.lstrip("# ").strip()

    # Search for DOI link
    doi_match = next((doi_regex.search(l) for l in lines if "DOI" in l), None)

    if doi_match:
        doi_url = doi_match.group(1)
        doi_id = doi_url.split("doi.org/")[-1]
        entry = f"""@article{{{note_file.stem},
  title = {{{title}}},
  doi = {{{doi_id}}},
  note = {{From {note_file.name}}}
}}"""
    else:
        entry = f"""@misc{{{note_file.stem},
  title = {{{title}}},
  note = {{No DOI found. Source: {note_file.name}}}
}}"""

    entries.append(entry)

# Write to .bib file
output_bib.write_text("\n\n".join(entries), encoding="utf-8")
print(f"✓ Wrote {len(entries)} entries to {output_bib}")