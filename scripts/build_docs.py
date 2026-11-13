#!/usr/bin/env python3
"""Generate static docs pages (jailbreaks + guides) for GitHub Pages.

Reads data/jailbreaks.json and the bilingual guide content below, and writes
plain HTML (styled by docs/page.css) plus a Markdown copy for GitHub browsing.
No third-party dependencies.
"""
import json, re, sys, html
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdmini

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
JB_DIR = DOCS / "jailbreaks"
GUIDE_DIR = DOCS / "guides"

SLUG = {
    "WinterBreak2": "winterbreak2", "WinterBreak": "winterbreak",
    "SpiderCat": "spidercat", "Véra": "vera", "Nosebleed": "nosebleed",
    "Sanctuary": "sanctuary", "SpringBreak (WinterBreak3)": "springbreak",
    "Shadow": "shadow", "AdBreak": "adbreak", "LanguageBreak": "languagebreak",
    "NiLuJe K2/K4/K5": "niluje", "Android flash": "android-flash",
}
NOTES = {
    "WinterBreak2": ("The classic no-account path for ≤ 5.16.3 (and 5.16.5). The first choice when your firmware is old enough.",
        "≤ 5.16.3（含 5.16.5）的经典免账号方案，固件够老时首选。"),
    "WinterBreak": ("Requires an Amazon login and covers 5.16.2.1.1 – 5.17.x. The most widely used method in this range.",
        "需要登录 Amazon 账号，覆盖 5.16.2.1.1 – 5.17.x，该区间最主流的方案。"),
    "SpiderCat": ("No account required; broad model coverage and works up to 5.19.5.",
        "无需账号，机型覆盖广，支持到 5.19.5。"),
    "Véra": ("No account required; the newest range up to 5.20.2 on 2023+ models.",
        "无需账号，覆盖到 5.20.2，2023+ 新机型。"),
    "Nosebleed": ("No account required; two firmware branches depending on model (see the table).",
        "无需账号，按机型分两条固件分支（见能力表）。"),
    "Sanctuary": ("No account required; note that this method denies 5.16.5.",
        "无需账号，注意该方法不支持 5.16.5。"),
    "SpringBreak (WinterBreak3)": ("Requires an Amazon login; targets 5.18.1 – 5.19.2.0.1.",
        "需要登录 Amazon 账号，面向 5.18.1 – 5.19.2.0.1。"),
    "Shadow": ("No account required; covers 5.19.4 – 5.19.6.",
        "无需账号，覆盖 5.19.4 – 5.19.6。"),
    "AdBreak": ("Experimental; requires a login and only works on ad-supported (Special Offers) devices.",
        "实验性方案；需登录账号，且仅适用于带广告（Special Offers）的设备。"),
    "LanguageBreak": ("Archived legacy method for very old firmware (≤ 5.16.2.1.1).",
        "已归档的旧方案，仅用于极老固件（≤ 5.16.2.1.1）。"),
    "NiLuJe K2/K4/K5": ("Classic legacy jailbreak for 2.x / 4.x / 5.0.x devices.",
        "面向 2.x / 4.x / 5.0.x 老机型的经典越狱。"),
    "Android flash": ("Hardcore: replace the OS with Android on supported models. High risk.",
        "硬核玩法：在支持机型上把系统整体换成 Android，风险高。"),
}

GEN_STEPS_EN = [
 "**Identify your exact device + firmware** — Settings → Device Options → Device Info. Note the full version (e.g. `5.16.2.1.1`) and the model code.",
 "**Back up and block OTA** — fill the storage or follow “Prevent Automatic Updates”, so a background update can't kill the process mid-way.",
 "**Charge fully and use a reliable USB cable** — never lose power during the process.",
 "**Read the official page for this method first** — steps change over time; the official wiki always wins.",
]
RUN_STEPS_EN = [
 "On the Kindle, open the browser and go to the official page for this method (link below).",
 "Download the jailbreak package for your exact model / firmware.",
 "Run it exactly as the official page says (tap the link / run the script / trigger the exploit).",
 "Wait patiently — do **not** unplug or power off while it runs.",
 "When it finishes the device usually reboots; confirm if prompted.",
 "Verify success with the method's own check (e.g. the jailbreak marker or the provided test).",
]
AFTER_EN = [
 "Install **Hotfix** — blocks OTA from wiping the jailbreak and prevents bricks.",
 "Install **KPM** (Kindle Package Manager) and **Jobman** — your app store and manager.",
 "Delete any leftover `.bin` update files from the USB root.",
 "Reboot once and confirm the jailbreak survives.",
]
ROLL_EN = [
 "Jailbreaking does not flash firmware; a factory reset typically returns to a clean state.",
 "**Without a jailbreak you cannot downgrade** — never flash a mismatched firmware.",
 "If the device won't boot, follow the official recovery / serial-flash guide for your model.",
 "If a step fails, stop, re-check model + firmware, and re-read the official page.",
]

def li(items): return "\n".join(f"{i+1}. {s}" for i, s in enumerate(items))
def ul(items): return "\n".join(f"- {s}" for s in items)

def jailbreak_md(m):
    name = m["name"]; en_note, zh_note = NOTES.get(name, ("", ""))
    links = m["links"]
    official = next((l["url"] for l in links if "kindlemodding.org" in l["url"]), links[0]["url"] if links else "")
    repo = next((l["url"] for l in links if "github.com" in l["url"]), "")
    md = f"""# {name}

> **Status:** {m['status']}  ·  **Firmware:** {m['firmware']}  ·  **Models:** {m['models']}

{en_note}

## Compatibility

| Item | Value |
| --- | --- |
| Firmware | {m['firmware']} |
| Models | {m['models']} |
| Amazon account | {m['account']} |
| Ads / Special Offers | {m['ads']} |
| Status | {m['status']} |

## Before you start
{li(GEN_STEPS_EN)}

## Steps
{li(RUN_STEPS_EN)}

## After jailbreak — do this immediately
{li(AFTER_EN)}

## Rollback & troubleshooting
{ul(ROLL_EN)}

## Official links
{ul([f"[{l['label']}]({l['url']})" for l in links] or [f"[Official page]({official})"])}

---

## 中文速览

{zh_note}

- **适用固件：** {m['firmware']}
- **适用机型：** {m['models']}
- **需要 Amazon 账号：** {m['account']}　**仅限广告版：** {m['ads']}
- **步骤：** 识别机型固件 → 备份并阻断 OTA → 下载并执行（全程勿断电）→ 成功后**先装 Hotfix** → 再装 KPM / Jobman → 删除根目录 `.bin` → 重启验证。
- **风险：** 没有越狱不能降级，乱刷会变砖；**一切以官方 Wiki 为准**。
"""
    return md

def page_html(title, subtitle, body, back_href="../index.html", asset_prefix="../", extra_head=""):
    desc = html.escape(re.sub(r"<[^>]+>", "", str(subtitle)))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{html.escape(title)} — Awesome Kindle</title>
<meta name="description" content="{desc}"/>
<meta property="og:title" content="{html.escape(title)} — Awesome Kindle"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="article"/>
<meta name="twitter:card" content="summary"/>
<link rel="stylesheet" href="{asset_prefix}style.css"/>
<link rel="stylesheet" href="{asset_prefix}page.css"/>{extra_head}
</head>
<body class="doc-body">
<a class="skip" href="#main">Skip to content</a>
<header class="doc-top"><div class="wrap"><a class="doc-back" href="{back_href}">← Awesome Kindle</a></div></header>
<main id="main" class="wrap doc-main">
<h1>{html.escape(title)}</h1>
<p class="doc-sub">{subtitle}</p>
<div class="prose">
{body}
</div>
<footer class="doc-foot">Defer to the <a href="https://kindlemodding.org/">official KindleModding wiki</a> · MIT</footer>
</main>
</body>
</html>
"""


def _vt(tok):
    out = []
    for part in re.split(r"[.\s]+", tok.strip().lower()):
        if not part:
            continue
        if part in ("x", "*"):
            out.append(999)
        elif part.isdigit():
            out.append(int(part))
        else:
            d = re.sub(r"\D", "", part)
            if d:
                out.append(int(d))
    return out + [0] * (6 - len(out))

def normalize_firmware(txt):
    t = txt.replace("<br/>", "\n").replace("<br>", "\n")
    if t.strip() in ("—", "", "-"):
        return [], [], True
    ranges, excl, legacy = [], [], False
    for seg in t.split("\n"):
        s = seg.lower()
        if any(k in s for k in ["2.x", "4.x", "5.0.x"]):
            legacy = True
            continue
        found = False
        for m in re.finditer(r"(≤|<=)\s*([0-9][0-9.]*[x0-9]*)", s):
            ranges.append([_vt("0"), _vt(m.group(2))]); found = True
        for m in re.finditer(r"([0-9][0-9.]*[x0-9]*)\s*[–\-]\s*([0-9][0-9.]*[x0-9]*)", s):
            ranges.append([_vt(m.group(1)), _vt(m.group(2))]); found = True
        for m in re.finditer(r"also\s+([0-9][0-9.]*)", s):
            v = _vt(m.group(1)); ranges.append([v, v]); found = True
        for m in re.finditer(r"denies\s+([0-9][0-9.]*)", s):
            excl.append(_vt(m.group(1)))
        if not found:
            bm = re.search(r"([0-9][0-9.]*(?:\.[0-9]+)+)", s)
            if bm:
                v = _vt(bm.group(1)); ranges.append([v, v])
    return ranges, excl, legacy

def _models(txt):
    s = txt.strip()
    if "—" in s or "Older" in s or "Select" in s or "Above" in s or "&" in s:
        return [], True
    parts = [x.strip() for x in re.split(r"[/,]", s) if x.strip()]
    return parts, False

def write_wizard_data(methods):
    out = []
    for m in methods:
        slug = SLUG.get(m["name"], re.sub(r"[^a-z0-9]+", "-", m["name"].lower()).strip("-"))
        ranges, excl, legacy = normalize_firmware(m["firmware"])
        models, allm = _models(m["models"])
        primary = next((l["url"] for l in m["links"] if "kindlemodding.org" in l["url"]), m["links"][0]["url"] if m["links"] else "")
        out.append({"slug": slug, "name": m["name"], "firmware": m["firmware"], "models": models,
                    "models_all": allm, "ranges": ranges, "exclude": excl, "legacy": legacy,
                    "status": m["status"], "account": m["account"], "ads": m["ads"], "url": primary})
    (DOCS / "jailbreaks.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def build_jailbreaks():
    JB_DIR.mkdir(parents=True, exist_ok=True)
    methods = json.load(open(ROOT / "data" / "jailbreaks.json", encoding="utf-8"))
    cards = []
    for m in methods:
        slug = SLUG.get(m["name"], re.sub(r"[^a-z0-9]+", "-", m["name"].lower()).strip("-"))
        md = jailbreak_md(m)
        (JB_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
        body = mdmini.convert(re.sub(r"^# .*\n", "", md, count=1))
        title = m["name"]
        sub = f"{m['status']} · Firmware {m['firmware']} · Account: {m['account']} · Ads: {m['ads']}"
        (JB_DIR / f"{slug}.html").write_text(page_html(title, html.escape(sub).replace("&lt;br/&gt;","<br/>"), body), encoding="utf-8")
        cards.append((slug, m))
    # index
    rows = "\n".join(
        f'<tr><td><a href="{slug}.html"><strong>{html.escape(m["name"])}</strong></a></td>'
        f'<td>{html.escape(m["firmware"])}</td><td>{html.escape(m["status"])}</td>'
        f'<td>{html.escape(m["account"])}</td></tr>' for slug, m in cards)
    body = f"""<p>Step-by-step pages for every method in the matrix. Pick your exact firmware + model,
then follow the page — and always defer to the official wiki.</p>
<table><thead><tr><th>Method</th><th>Firmware</th><th>Status</th><th>Account</th></tr></thead><tbody>
{rows}
</tbody></table>
<p><a href="../index.html">← Back to the searchable index</a></p>"""
    (JB_DIR / "index.html").write_text(page_html("Jailbreak guides", "Pick your method, follow the steps.", body, back_href="../index.html"), encoding="utf-8")
    md_lines = ["# Jailbreak guides", "", "Step-by-step pages for every method in the matrix. Always defer to the official wiki.", ""]
    md_lines += [f"- [{m['name']}]({slug}.md) — firmware {m['firmware']} · {m['status']}" for slug, m in cards]
    md_lines += ["", "Back to the [searchable index](../index.html).", ""]
    (JB_DIR / "README.md").write_text("\n".join(md_lines), encoding="utf-8")
    write_wizard_data(methods)
    print(f"jailbreaks: {len(methods)} pages")


def build_guides():
    from guides_content import GUIDES
    _seen = {}
    for _g in GUIDES:
        _seen[_g["slug"]] = _g  # last definition wins
    GUIDES = list(_seen.values())
    GUIDE_DIR.mkdir(parents=True, exist_ok=True)
    GUIDE_DATE = "2026-11-13"
    for g in GUIDES:
        _md = g["body"]
        _lines = _md.split("\n")
        if _lines and _lines[0].startswith("# "):
            _lines.insert(1, "")
            _lines.insert(2, f"> Last reviewed: {GUIDE_DATE}")
            _md = "\n".join(_lines)
        (GUIDE_DIR / f"{g['slug']}.md").write_text(_md, encoding="utf-8")
        body_html = mdmini.convert(re.sub(r"^# .*\n", "", _md, count=1))
        (GUIDE_DIR / f"{g['slug']}.html").write_text(
            page_html(g["title"], html.escape(g["subtitle"]), body_html, back_href="index.html"), encoding="utf-8")
    cards = "\n".join(
        f'<a class="gcard" href="{g["slug"]}.html"><h3>{html.escape(g["title"])}</h3>'
        f'<p>{html.escape(g["subtitle"])}</p></a>' for g in GUIDES)
    body = f'''<p>Practical, copy-paste guides. Each one has an English walkthrough and a 中文速览 at the bottom.</p>
<div class="gcards">{cards}</div>
<p><a href="../index.html">← Back to the searchable index</a></p>'''
    (GUIDE_DIR / "index.html").write_text(page_html("Guides", "Install, configure and recover your Kindle.", body, back_href="../index.html"), encoding="utf-8")
    md_lines = ["# Guides", "", "Practical walkthroughs (English + 中文速览).", ""]
    md_lines += [f"- [{g['title']}]({g['slug']}.md) — {g['subtitle']}" for g in GUIDES]
    md_lines += ["", "Back to the [searchable index](../index.html).", ""]
    (GUIDE_DIR / "README.md").write_text("\n".join(md_lines), encoding="utf-8")
    print(f"guides: {len(GUIDES)} pages")


def build_status():
    jb = json.load(open(DOCS / "jailbreaks.json", encoding="utf-8"))
    wl = json.load(open(ROOT / "data" / "watchlist.json", encoding="utf-8"))
    # compute max supported version across numeric ranges
    def maxv(m):
        best = [0]*6
        for r in m.get("ranges", []):
            if r[1] > best: best = r[1]
        return best
    def vtostr(v):
        parts=[("x" if x==999 else str(x)) for x in v]
        while len(parts) > 2 and parts[-1] == "0":
            parts.pop()
        return ".".join(parts) or "0"
    best=[0]*6; bestname=""
    for m in jb:
        mv=maxv(m)
        if mv>best: best=mv; bestname=m["name"]
    maxs=vtostr(best)
    rows="\n".join(
        f'<tr><td><a href="jailbreaks/{m["slug"]}.html"><strong>{html.escape(m["name"])}</strong></a></td>'
        f'<td>{html.escape(m["firmware"]).replace("&lt;br/&gt;","<br/>")}</td><td>{html.escape(m["status"])}</td>'
        f'<td>{html.escape(m["account"])}</td></tr>' for m in jb)
    wlrows="\n".join(f'<tr><td>{html.escape(x["model"])}</td><td>❌ {html.escape(x["note"])} / {html.escape(x["note_zh"])}</td></tr>' for x in wl["unsupported_models"])
    notes="\n".join(f'<li>{html.escape(n["note"])}<br/><span class="muted">{html.escape(n["note_zh"])}</span></li>' for n in wl["notes"])
    body=f"""<div class="prose">
<p><strong>Max firmware supported by any current public method: 🔺 {maxs}</strong> (via {html.escape(bestname)}). Newer than that? You have to wait.</p>
<blockquote>{html.escape(wl['rule'])}<br/><span class="muted">{html.escape(wl['rule_zh'])}</span></blockquote>
<h2>Jailbreak status by method</h2>
<table><thead><tr><th>Method</th><th>Firmware</th><th>Status</th><th>Account</th></tr></thead><tbody>
{rows}
</tbody></table>
<h2>Not supported yet — the watchlist</h2>
<table><thead><tr><th>Model</th><th>Status</th></tr></thead><tbody>
{wlrows}
</tbody></table>
<h2>Known caveats</h2>
<ul>{notes}</ul>
<p class="muted">Status reflects the README matrix at build time. Always confirm on the <a href="https://kindlemodding.org/">official wiki</a> / <a href="https://kindlemodding.org/jailbreaks.json">jailbreaks.json</a>.</p>
<p><a href="index.html">← Back to the searchable index</a></p>
</div>"""
    (DOCS / "status.html").write_text(page_html("Jailbreak status board", "What works, what doesn't, and what to wait for.", body, back_href="index.html", asset_prefix=""), encoding="utf-8")
    md=["# Jailbreak status board","", f"Max firmware supported by any current method: **{maxs}** ({bestname}).","", wl["rule"],"", "## Methods",""]
    md += [f'- {m["name"]} — {m["firmware"]} · {m["status"]}' for m in jb]
    md += ["", "## Not supported yet",""] + [f'- {x["model"]} — {x["note"]}' for x in wl["unsupported_models"]]
    (DOCS / "status.md").write_text("\n".join(md)+"\n", encoding="utf-8")
    print(f"status: max firmware {maxs}")


SW_TEMPLATE = """self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).catch(() => {})); self.skipWaiting(); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request).then((resp) => {
    const cp = resp.clone(); caches.open(CACHE).then((c) => c.put(e.request, cp)).catch(() => {}); return resp;
  }).catch(() => r)));
});
"""

def site_base():
    import os, subprocess
    env = os.environ.get("SITE_BASE")
    if env:
        return env.rstrip("/") + "/"
    try:
        url = subprocess.check_output(["git", "-C", str(ROOT), "remote", "get-url", "origin"], text=True).strip()
        m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", url)
        if m:
            return f"https://{m.group(1)}.github.io/{m.group(2)}/"
    except Exception:
        pass
    return "https://example.github.io/awesome-kindle/"

def build_extras():
    base = site_base()
    pages = []
    for pth in sorted(DOCS.rglob("*.html")):
        rel = pth.relative_to(DOCS).as_posix()
        if rel == "404.html":
            continue
        pages.append(rel)
    entries = []
    for r in pages:
        loc = base if r == "index.html" else base + r
        entries.append(f"  <url><loc>{loc}</loc></url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(entries) + "\n</urlset>\n")
    (DOCS / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n", encoding="utf-8")
    body = '<div class="prose"><h1>404 — page not found</h1><p>The page you were looking for does not exist.</p><p><a href="index.html">← Back to Awesome Kindle</a></p></div>'
    (DOCS / "404.html").write_text(page_html("Page not found", "404", body, back_href="index.html", asset_prefix=""), encoding="utf-8")
    assets = ["./", "index.html", "app.js", "style.css", "page.css", "resources.json", "jailbreaks.json",
              "offline.html", "wizard.html", "wizard.js", "status.html", "manifest.webmanifest", "icon.png"]
    assets += [pth.relative_to(DOCS).as_posix() for pth in sorted(DOCS.rglob("*.html")) if pth.name != "index.html"]
    assets = list(dict.fromkeys(assets))
    (DOCS / "sw.js").write_text("const CACHE='awesome-kindle-v2';\nconst ASSETS=" + json.dumps(assets) + ";\n" + SW_TEMPLATE, encoding="utf-8")
    print(f"extras: sitemap {len(pages)} urls, sw {len(assets)} files")




def clean_section(s):
    return re.sub(r"^[^\w\u4e00-\u9fff]+", "", s or "").strip()


def build_exports():
    import csv
    res = json.load(open(ROOT / "data" / "resources.json", encoding="utf-8"))
    items = res["items"]
    cols = ["name", "name_zh", "url", "section", "description", "description_zh", "kind"]
    for target in [ROOT / "data" / "resources.csv", DOCS / "resources.csv"]:
        with open(target, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: it.get(k, "") for k in cols})
    lines = ["# Awesome Kindle — resource index", "", f"{len(items)} items. Generated from the READMEs.", "",
             "| Name | Section | Link |", "| --- | --- | --- |"]
    lines += [f'| {it["name"]} | {clean_section(it.get("section", ""))} | {it["url"]} |' for it in items]
    (DOCS / "resources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    body = f"""<div class="prose"><h1>Export &amp; API</h1>
<p>The whole index is machine-readable ({len(items)} items):</p>
<ul>
<li><a href="resources.json">resources.json</a> — full bilingual JSON (name_zh, description_zh)</li>
<li><a href="resources.csv">resources.csv</a> — spreadsheet-friendly CSV</li>
<li><a href="resources.md">resources.md</a> — Markdown table</li>
<li><a href="jailbreaks.json">jailbreaks.json</a> — methods + firmware ranges (wizard data)</li>
<li>JSON Schema: <code>data/resources.schema.json</code></li>
</ul>
<p>Regenerate with <code>python3 scripts/build_resources.py</code>.</p>
<p><a href="index.html">← Back to the searchable index</a></p></div>"""
    (DOCS / "export.html").write_text(page_html("Export & API", "JSON / CSV / Markdown for tooling.", body, back_href="index.html", asset_prefix=""), encoding="utf-8")
    print(f"exports: {len(items)} items (json/csv/md)")


def build_verified():
    v = json.load(open(ROOT / "data" / "verified.json", encoding="utf-8"))
    entries = v.get("entries", [])
    if entries:
        rows = "\n".join(
            f'<tr><td>{html.escape(e.get("model",""))}</td><td>{html.escape(e.get("firmware",""))}</td>'
            f'<td>{html.escape(e.get("method",""))}</td><td>{html.escape(e.get("result",""))}</td>'
            f'<td>{html.escape(e.get("date",""))}</td></tr>' for e in entries)
        table = f'<table><thead><tr><th>Model</th><th>Firmware</th><th>Method</th><th>Result</th><th>Date</th></tr></thead><tbody>{rows}</tbody></table>'
    else:
        table = "<p><em>No community reports yet.</em> Be the first to add one.</p>"
    body = f"""<div class="prose"><h1>Verified setups (community)</h1>
<p>Real device + firmware + method reports from users. Updated {html.escape(v.get("updated",""))}.</p>
<blockquote>{html.escape(v.get("note",""))}</blockquote>
{table}
<p>👉 Submit via the repo: Issues → “Report your working setup” (template <code>report-setup.yml</code>).</p>
<p><a href="index.html">← Back to the searchable index</a></p></div>"""
    (DOCS / "verified.html").write_text(page_html("Verified setups", "Community-reported working device + firmware + method.", body, back_href="index.html", asset_prefix=""), encoding="utf-8")
    print(f"verified: {len(entries)} entries")




def gh_repo():
    import subprocess
    try:
        url = subprocess.check_output(["git", "-C", str(ROOT), "remote", "get-url", "origin"], text=True).strip()
        m = re.search(r"github\.com[:/]([^/]+/[^/.]+)", url)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "OWNER/awesome-kindle"


def build_community():
    repo = gh_repo()
    base = f"https://github.com/{repo}"
    needs = [
        ("固件能不能越 / 还要等多久", "Firmware support & waitlist", "status.html"),
        ("装不上 / 炸了怎么救", "Install reliability & brick rescue", "guides/troubleshooting.html"),
        ("越狱后到底能干嘛", "What jailbreak unlocks", "guides/starter-pack.html"),
        ("书和笔记怎么管", "Books, content & notes", "guides/koreader-notes.html"),
        ("买前 / 二手 / 残值", "Buying & used-market check", "guides/buying-guide.html"),
        ("Kindle 退出中国怎么活", "China survival (WeRead / Android)", "guides/china-survival.html"),
    ]
    items = "\n".join(f'<li>{html.escape(zh)} / <em>{html.escape(en)}</em> → <a href="{href}">guide</a></li>' for zh, en, href in needs)
    body = f"""<div class="prose"><h1>Community</h1>
<p>This is a community index. Here is how to contribute and what people ask for most.</p>
<h2>Top needs from our research</h2><ul>{items}</ul>
<h2>Get involved</h2>
<ul>
<li><a href="{base}/discussions">💬 Discussions</a> — ask questions, share setups</li>
<li><a href="{base}/issues/new?template=report-setup.yml">✅ Report your working setup</a> — feeds the <a href="verified.html">verified list</a></li>
<li><a href="{base}/issues/new?template=request-guide.yml">📝 Request a guide</a></li>
<li><a href="{base}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22">🌱 Good first issues</a></li>
<li><a href="{base}/graphs/contributors">🙌 Contributors</a></li>
</ul>
<p><a href="index.html">← Back to the searchable index</a></p></div>"""
    (DOCS / "community.html").write_text(page_html("Community", "Contribute, report setups, and see what people need.", body, back_href="index.html", asset_prefix=""), encoding="utf-8")
    md = ["# Community", "", "## Top needs from our research", ""] + [f"- {zh} / {en} → {href}" for zh, en, href in needs]
    (DOCS / "community.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("community page built")

if __name__ == "__main__":
    build_jailbreaks()
    build_guides()
    build_status()
    build_extras()
    build_exports()
    build_verified()
    build_community()
