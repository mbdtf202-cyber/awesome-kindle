#!/usr/bin/env python3
"""Deep project audit (offline, no network): internal links, anchors, HTML basics,
placeholder leaks, bilingual parity, data consistency, sitemap coverage.

Writes AUDIT.md and exits non-zero on hard failures.
"""
import json, re, sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
fails, warns, passes = [], [], []

def ok(msg): passes.append(msg)
def warn(msg): warns.append(msg)
def fail(msg): fails.append(msg)

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set(); self.has_title = False; self.html_close = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "link") and a.get("href"): self.links.append(a["href"])
        if tag in ("script", "img") and a.get("src"): self.links.append(a["src"])
        if a.get("id"): self.ids.add(a["id"])
        if tag == "a" and a.get("name"): self.ids.add(a["name"])
        if tag == "title": self.has_title = True
    def handle_endtag(self, tag):
        if tag == "html": self.html_close = True

pages = {}
for p in DOCS.rglob("*.html"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    par = P(); par.feed(txt)
    pages[p] = (par, txt)
    if not par.has_title: fail(f"missing <title>: {p.relative_to(ROOT)}")
    if "</html>" not in txt: fail(f"missing </html>: {p.relative_to(ROOT)}")
if pages: ok(f"parsed {len(pages)} html pages (title + </html>)")

def resolve(base: Path, href: str):
    href = href.split("#", 1)
    path = href[0]; anchor = href[1] if len(href) > 1 else None
    if path == "": return base, anchor
    if re.match(r"^(https?:|mailto:|tel:|javascript:)", path): return None, None
    target = (base.parent / path).resolve()
    return target, anchor

broken = 0; anchors = 0
for p, (par, txt) in pages.items():
    for href in par.links:
        if href.startswith("data:"): continue
        target, anchor = resolve(p, href)
        if target is None: continue
        if target.is_dir(): continue
        if not target.exists():
            broken += 1; fail(f"broken link: {p.relative_to(ROOT)} → {href}")
            continue
        if anchor and target.suffix == ".html":
            tpar = pages.get(target)
            if tpar and anchor not in tpar[0].ids:
                anchors += 1; fail(f"missing anchor: {p.relative_to(ROOT)} → {href}")
if not broken and not anchors: ok("all internal HTML links & anchors resolve")

# Markdown internal links
md_bad = 0
for md in [ROOT / "README.md", ROOT / "README_EN.md", ROOT / "README_JA.md", ROOT / "README_KO.md",
           ROOT / "CONTRIBUTING.md", ROOT / "ROADMAP.md", ROOT / "SUPPORT.md", ROOT / "SECURITY.md"]:
    if not md.exists(): continue
    for m in re.finditer(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8", errors="ignore")):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#)", href): continue
        path = href.split("#")[0]
        if not path: continue
        if not (ROOT / path).exists():
            md_bad += 1; fail(f"broken md link: {md.name} → {href}")
if not md_bad: ok("all Markdown relative links resolve")

# Placeholder leaks ({{...}} or unreplaced tokens)
leak = 0
SKIP = {".git", "__pycache__", "node_modules"}
for p in ROOT.rglob("*"):
    if p.is_dir() or any(s in p.parts for s in SKIP): continue
    if p.name in ("audit.py", "AUDIT.md") or ".github/workflows" in p.as_posix(): continue
    if p.suffix.lower() not in (".md", ".html", ".js", ".css", ".py", ".yml", ".yaml", ".json", ".txt", ".toml"): continue
    try: t = p.read_text(encoding="utf-8", errors="ignore")
    except Exception: continue
    if "{{" in t or "}}" in t:
        leak += 1; fail(f"placeholder leak: {p.relative_to(ROOT)}")
if not leak: ok("no unreplaced template tokens")

# Bilingual parity
def h2(p): return sum(1 for l in p.read_text(encoding="utf-8").splitlines() if l.startswith("## "))
zh, en = ROOT / "README.md", ROOT / "README_EN.md"
lz, le = len(zh.read_text(encoding="utf-8").splitlines()), len(en.read_text(encoding="utf-8").splitlines())
if lz == le and h2(zh) == h2(en): ok(f"README zh/en parity: {lz} lines, {h2(zh)} H2")
else: fail(f"README parity mismatch: zh {lz}/{h2(zh)} vs en {le}/{h2(en)}")
ja, ko = ROOT / "README_JA.md", ROOT / "README_KO.md"
if ja.exists() and ko.exists():
    if len(ja.read_text(encoding='utf-8').splitlines()) == len(ko.read_text(encoding='utf-8').splitlines()):
        ok("README JA/KO line parity")
    else: warn("README JA/KO line counts differ")

# Data consistency
res = json.load(open(ROOT / "data" / "resources.json", encoding="utf-8"))
items = res["items"]
assert res["count"] == len(items)
zh_matched = sum(1 for it in items if it.get("description_zh"))
if zh_matched == len(items): ok(f"resources bilingual complete: {len(items)}/{len(items)}")
else: fail(f"resources zh descriptions incomplete: {zh_matched}/{len(items)}")
if (ROOT / "docs" / "resources.json").read_text(encoding="utf-8") == (ROOT / "data" / "resources.json").read_text(encoding="utf-8"):
    ok("data/resources.json == docs/resources.json")
else: fail("docs/resources.json out of sync")

# sitemap coverage
sm = (DOCS / "sitemap.xml").read_text(encoding="utf-8") if (DOCS / "sitemap.xml").exists() else ""
locs = re.findall(r"<loc>(.*?)</loc>", sm)
missing = 0
for loc in locs:
    rel = re.sub(r"^https?://[^/]+/awesome-kindle/", "", loc)
    rel = "" if rel == "" else rel
    target = DOCS / ("index.html" if rel in ("",) else rel)
    if not target.exists(): missing += 1; fail(f"sitemap points to missing: {loc}")
if locs and not missing: ok(f"sitemap: {len(locs)} urls all resolve")

# File size sanity (soft)
big = [p for p in DOCS.rglob("*") if p.is_file() and p.stat().st_size > 1_500_000 and p.suffix in (".html",".js",".css")]
if big: warn(f"large files: {[str(p.relative_to(ROOT)) for p in big]}")

# Write report
lines = ["# Deep audit report", "", f"Status: {'✅ PASS' if not fails else '❌ FAIL'}", ""]
lines += ["## Passed", *[f"- ✅ {x}" for x in passes], ""]
if warns: lines += ["## Warnings", *[f"- ⚠️ {x}" for x in warns], ""]
if fails: lines += ["## Failures", *[f"- ❌ {x}" for x in fails], ""]
(ROOT / "AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
sys.exit(1 if fails else 0)
