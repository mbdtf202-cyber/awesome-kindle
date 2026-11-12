# KCC — Kindle Comic Converter

KCC converts CBZ/CBR/images/PDF into EPUB/MOBI/KFX tuned for e-ink: correct size,
contrast, margins and panel handling.

## Install
- Download from https://github.com/ciromattia/kcc (Windows/macOS/Linux builds).

## Basic workflow
1. Drag your `.cbz`/`.cbr`/images/PDF into KCC.
2. Pick your **device profile** (e.g. Paperwhite 5, Scribe) — this sets resolution.
3. Choose output: **EPUB** (new firmware) or **MOBI/AZW3** (older); enable *manga mode* for right-to-left.
4. Convert, then copy the output to `documents/` or send via Calibre.

## Tips
- For scanned PDFs, enable *cropping* and *auto-contrast*.
- Use **manga mode** for Japanese order; use *spread splitting* for double pages.
- Large books: convert per-volume, then merge with **EpubMerge** if needed.

---

## 中文速览

- **安装**：GitHub 下载对应系统版本。
- **流程**：拖入 CBZ/CBR/图片/PDF → 选机型（自动分辨率）→ 输出 EPUB（新固件）或 MOBI/AZW3（老固件）→ 拷进 `documents/`。
- **技巧**：扫描 PDF 开裁边+自动对比度；日漫开 manga 模式；双页拆分；分卷转换后用 EpubMerge 合并。
