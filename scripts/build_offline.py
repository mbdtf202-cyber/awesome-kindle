#!/usr/bin/env python3
"""Build a single self-contained offline HTML (docs/offline.html) from resources.json.

Everything (data + CSS + JS) is inlined so the file works with no server — handy to
copy onto a Kindle and read the index locally.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "data" / "resources.json", encoding="utf-8"))
items = data["items"]
payload = json.dumps(items, ensure_ascii=False)

html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Awesome Kindle — offline index</title>
<style>
:root{--bg:#0b1220;--card:#111a2b;--line:#22304a;--fg:#e8eef7;--muted:#94a3b8;--accent:#38bdf8}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(160deg,#0b1220,#111c31);color:var(--fg);font-family:-apple-system,Segoe UI,Roboto,"PingFang SC","Microsoft YaHei",sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:24px 18px 60px}
h1{font-size:34px;margin:8px 0 4px}.muted{color:var(--muted)}
#q{width:100%;padding:14px 16px;border-radius:12px;border:1px solid var(--line);background:#0d1524;color:var(--fg);font-size:16px;margin:14px 0}
.item{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:8px 0}
.item h3{margin:0 0 4px;font-size:16px}.item a{color:#eaf2ff;text-decoration:none}.item p{margin:0;color:#a9b7cb;font-size:13px}
.tag{font-size:11px;color:#8fb4e8;background:#0f1d33;border:1px solid #21375a;border-radius:999px;padding:2px 8px;margin-right:6px}
.go{color:var(--muted);font-size:12px}
</style></head>
<body><div class="wrap">
<h1>Awesome Kindle — offline index</h1>
<p class="muted">Self-contained copy of the index. Works offline and on-device. <span id="n"></span></p>
<input id="q" placeholder="Search…"/>
<div id="list"></div>
</div>
<script>
const DATA = __DATA__;
const $ = id => document.getElementById(id);
function esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function render(q){
  q=(q||"").toLowerCase();
  const list = DATA.filter(it => !q || [it.name,it.name_zh,it.description,it.description_zh,it.section,it.section_zh].join(" ").toLowerCase().includes(q));
  $("n").textContent = "(" + list.length + " / " + DATA.length + " items)";
  $("list").innerHTML = list.map(it => {
    let h=""; try{h=new URL(it.url).hostname.replace(/^www\\./,"")}catch(e){}
    return `<div class="item"><h3><a href="${esc(it.url)}">${esc(it.name)}</a></h3>
      <p><span class="tag">${esc((it.section||"").replace(/^[^\\p{L}\\p{N}]+/u,""))}</span>${esc(it.description)}</p>
      <span class="go">${esc(h)}</span></div>`;
  }).join("");
}
$("q").addEventListener("input",e=>render(e.target.value));
render("");
</script></body></html>
"""
html = html.replace("__DATA__", payload)
out = ROOT / "docs" / "offline.html"
out.write_text(html, encoding="utf-8")
print(f"Wrote {out.relative_to(ROOT)} ({len(items)} items)")
