"""Tiny dependency-free Markdown -> HTML converter for the docs pages.

Supports the subset used by this repo: h1-h3, paragraphs, ordered/unordered
lists, blockquotes, fenced code, horizontal rules, simple pipe tables, and
inline **bold**, `code`, [text](url). Intentionally small and predictable.
"""
import html
import re

def _inline(s):
    s = html.escape(s, quote=False)
    s = s.replace("&lt;br/&gt;", "<br/>").replace("&lt;br&gt;", "<br/>")
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def convert(md: str) -> str:
    lines = md.splitlines()
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i])); i += 1
            i += 1
            out.append(f'<pre><code class="lang-{html.escape(lang)}">' + "\n".join(buf) + "</code></pre>")
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if line.strip() == "---":
            out.append("<hr/>"); i += 1; continue
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(_inline(lines[i][1:].lstrip())); i += 1
            out.append("<blockquote><p>" + "<br/>".join(buf) + "</p></blockquote>"); continue
        if line.lstrip().startswith("|"):
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i]); i += 1
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block]
            if len(rows) >= 2 and re.match(r"^:?-+:?$", rows[1][0]):
                head, body = rows[0], rows[2:]
                h = "".join(f"<th>{_inline(c)}</th>" for c in head)
                b = "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in row) + "</tr>" for row in body)
                out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")
            continue
        mo = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if mo:
            items = []
            while i < n:
                mm = re.match(r"^\s*(\d+)\.\s+(.*)$", lines[i])
                if not mm: break
                items.append(_inline(mm.group(2))); i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"); continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(_inline(re.sub(r"^\s*[-*]\s+", "", lines[i]))); i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"); continue
        if line.strip() == "":
            i += 1; continue
        para = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,3}\s|>\s?|\s*[-*]\s|\s*\d+\.\s|\||```|---$)", lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append("<p>" + _inline(" ".join(para)) + "</p>")
    return "\n".join(out)
