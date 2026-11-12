#!/usr/bin/env python3
"""Build data/resources.json from README_EN.md.

Parses the Markdown tables in the English README into a machine-readable
resource index. Run from the repo root:

    python3 scripts/build_resources.py

The output is deterministic and committed so the site / tooling can consume it.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README_EN.md"
OUT = ROOT / "data" / "resources.json"
OUT_SITE = ROOT / "docs" / "resources.json"

LINK_RE = re.compile(r"https?://[^\s)<>\"']+")


def strip_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)  # [text](url) -> text
    s = s.replace("**", "").replace("`", "").replace("<br/>", " ")
    return s.strip()


def parse_tables(lines):
    items = []
    h2 = h3 = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            h2, h3 = strip_md(line[3:]), None
            i += 1
            continue
        if line.startswith("### "):
            h3 = strip_md(line[4:])
            i += 1
            continue
        if line.strip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            if len(block) < 3:
                continue
            header = strip_md(block[0]).lower()
            rows = block[2:]
            for r in rows:
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                # 7-col jailbreak matrix: Method | Firmware | Models | Account | Ads | Status | Links
                if "method" in header and len(cells) == 7:
                    urls = LINK_RE.findall(cells[6])
                    if not urls:
                        continue
                    items.append({
                        "name": strip_md(cells[0]),
                        "url": urls[0].rstrip(".,"),
                        "links": [u.rstrip(".,") for u in urls],
                        "description": (
                            f"Firmware: {strip_md(cells[1])} · Models: {strip_md(cells[2])}"
                            f" · Account: {strip_md(cells[3])} · Ads: {strip_md(cells[4])}"
                            f" · Status: {strip_md(cells[5])}"
                        ),
                        "section": h2,
                        "subsection": h3,
                        "kind": "jailbreak",
                    })
                    continue
                # standard 3-col: Name | Description | Link
                if len(cells) != 3:
                    continue
                urls = LINK_RE.findall(cells[2])
                if not urls:
                    continue
                items.append({
                    "name": strip_md(cells[0]),
                    "url": urls[0].rstrip(".,"),
                    "links": [u.rstrip(".,") for u in urls],
                    "description": strip_md(cells[1]),
                    "section": h2,
                    "subsection": h3,
                    "kind": "resource",
                })
            continue
        i += 1
    return items


def main():
    items = parse_tables(README.read_text(encoding="utf-8").splitlines())
    payload = {
        "repo": "awesome-kindle",
        "generated": "2026-11-12",
        "source": "README_EN.md",
        "note": "Machine-readable index derived from README_EN.md tables. See data/README.md.",
        "count": len(items),
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    OUT.write_text(text, encoding="utf-8")
    # keep a copy next to the static site so it works on GitHub Pages (/docs)
    if (ROOT / "docs").is_dir():
        OUT_SITE.write_text(text, encoding="utf-8")
    print(f"Wrote {len(items)} items to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
