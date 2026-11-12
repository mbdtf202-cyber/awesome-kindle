#!/usr/bin/env python3
"""Build a bilingual machine-readable index (data/resources.json) from the READMEs.

Parses the 3-column resource tables and the 7-column jailbreak matrix from both
README_EN.md and README.md, merges them by URL, and writes a deterministic JSON
index used by the static site and any tooling. Run from the repo root:

    python3 scripts/build_resources.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "resources.json"
OUT_SITE = ROOT / "docs" / "resources.json"

LINK_RE = re.compile(r"https?://[^\s)<>\"'|]+")


def strip_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").replace("<br/>", " ").replace("<br>", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip(" ·")


def parse(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    items, h2, h3, i = [], None, None, 0
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
        if line.lstrip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i]); i += 1
            if len(block) < 3:
                continue
            header = [c.strip() for c in block[0].strip().strip("|").split("|")]
            rows = block[2:]
            for r in rows:
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                # 7-col jailbreak matrix
                if len(header) == 7 and len(cells) == 7:
                    urls = LINK_RE.findall(cells[6])
                    if not urls:
                        continue
                    items.append({
                        "name": strip_md(cells[0]), "url": urls[0].rstrip(".,"),
                        "links": [u.rstrip(".,") for u in urls],
                        "description": (f"Firmware: {strip_md(cells[1])} · Models: {strip_md(cells[2])}"
                                        f" · Account: {strip_md(cells[3])} · Ads: {strip_md(cells[4])}"
                                        f" · Status: {strip_md(cells[5])}"),
                        "section": h2, "subsection": h3, "kind": "jailbreak",
                    })
                    continue
                # standard 3-col: Name | Description | Link
                if len(header) == 3 and len(cells) == 3:
                    urls = LINK_RE.findall(cells[2])
                    if not urls:
                        continue
                    items.append({
                        "name": strip_md(cells[0]), "url": urls[0].rstrip(".,"),
                        "links": [u.rstrip(".,") for u in urls],
                        "description": strip_md(cells[1]),
                        "section": h2, "subsection": h3, "kind": "resource",
                    })
            continue
        i += 1
    return items


def build():
    en = parse(ROOT / "README_EN.md")
    zh = parse(ROOT / "README.md")
    zh_by_url = {}
    for it in zh:
        zh_by_url.setdefault(it["url"], it)
    merged = []
    for it in en:
        z = zh_by_url.get(it["url"], {})
        merged.append({
            "name": it["name"],
            "name_zh": z.get("name", ""),
            "url": it["url"],
            "links": it["links"],
            "description": it["description"],
            "description_zh": z.get("description", ""),
            "section": it["section"],
            "section_zh": z.get("section", ""),
            "subsection": it["subsection"],
            "subsection_zh": z.get("subsection", ""),
            "kind": it["kind"],
        })
    payload = {
        "repo": "awesome-kindle",
        "generated": "2026-11-12",
        "source": "README_EN.md + README.md",
        "note": "Bilingual machine-readable index derived from the README tables. See data/README.md.",
        "count": len(merged),
        "items": merged,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    OUT.write_text(text, encoding="utf-8")
    if (ROOT / "docs").is_dir():
        OUT_SITE.write_text(text, encoding="utf-8")
    matched = sum(1 for it in merged if it["description_zh"])
    print(f"Wrote {len(merged)} items to {OUT.relative_to(ROOT)} (zh matched {matched})")


if __name__ == "__main__":
    build()
