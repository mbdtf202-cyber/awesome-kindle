# KOReader — export highlights & notes

KOReader keeps annotations **per book** in a sidecar folder next to the file:
`<book>.sdr/metadata.<ext>.lua`. There are three practical ways to get them out.

## 1. Native Kindle highlights
Highlights made in the **stock Kindle reader** go to `documents/My Clippings.txt`
(over USB). That file is plain text and easy to parse.

## 2. KOReader built-in export
In KOReader, open the book → reader menu → **Export highlights** → choose **HTML** or
**Markdown**. It writes a file you can copy off over USB or with `scp`.

## 3. Parse the sidecar yourself (script)
The `.sdr/metadata.*.lua` file contains an `annotations` table. A minimal extractor:

```python
import re, sys, json
path = sys.argv[1]
src = open(path, encoding="utf-8", errors="ignore").read()
notes = []
for m in re.finditer(r'\{\s*chapter\s*=\s*"([^"]*)".*?text\s*=\s*"((?:[^"\\]|\\.)*)"', src, re.S):
    chapter, text = m.group(1), m.group(2).encode().decode("unicode_escape")
    notes.append({"chapter": chapter, "text": text})
print(json.dumps(notes, ensure_ascii=False, indent=2))
```
Then convert JSON → Markdown/Notion/Readwise as you like.

## 4. Calibre / sync
- **Calibre** can collect KOReader metadata via plugins; search "KOReader" in Calibre's plugin list.
- Cloud sync: KOReader's *Progress sync* keeps positions; annotations live in the sidecar above.

## Tips
- Export **per book** after finishing it — sidecars travel with the file.
- Keep a git/Dropbox folder of exported Markdown for a permanent notes archive.

---

## 中文速览

- KOReader 的标注存在每本书旁边的 `.sdr/metadata.<ext>.lua` 里。
- 三种导出：① 原生 Kindle 阅读器的高亮在 `documents/My Clippings.txt`；② KOReader 阅读菜单 → **导出高亮** → HTML/Markdown；③ 用脚本解析 `.sdr` 里的 `annotations` 表（见上方 Python）。
- Calibre 有 KOReader 相关插件可汇总；每本书读完就导出，sidecar 随书走，导出的 Markdown 存进网盘/仓库做长期笔记库。
