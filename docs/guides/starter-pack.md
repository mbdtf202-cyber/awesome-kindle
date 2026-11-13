# Starter Pack — first 20 minutes after jailbreak

> Last reviewed: 2026-11-13

Do these in order. Skip nothing in step 1-2 — they protect the jailbreak itself.

## 1. Lock it in (do first)
1. **Hotfix** — install it immediately. It blocks OTA updates from wiping the jailbreak and prevents bricks. → https://github.com/KindleModding/Hotfix
2. **Delete leftover `.bin` files** from the USB root so a reboot can't auto-install an update.
3. Reboot once and confirm the jailbreak is still active.

## 2. Get a package manager
1. **KPM** (Kindle Package Manager) — like `apt` for the Kindle; installs scriptlets/apps. → https://github.com/KindleModding/KPM
2. **Jobman** — a GUI to manage the jailbreak and installed apps. → https://github.com/KindleTweaks/jobman

## 3. The essentials
- **KOReader** — the best reader (PDF/CBZ/EPUB reflow, dictionaries, gestures). → https://github.com/koreader/koreader
- **kterm** — a terminal, and the base for SSH. → https://github.com/bfabiszewski/kterm
- **USBNetLite** — enable SSH over USB/Wi-Fi. → https://github.com/notmarek/kindle-usbnetlite
- **fonts & dictionaries** — copy `.ttf` into the fonts folder; add StarDict/GoldenDict dictionaries.
- **screensaver / ads tweaks** — optional KUAL/KPM packages.

## 4. Quality of life
- Set up **Calibre** on your PC and connect over USB, or use **Send to Kindle**.
- Install **KCC** if you read comics/manga.
- Make a **backup** of your `documents/` and jailbreak config.

## Checklist
- [ ] Hotfix installed & rebooted
- [ ] KPM + Jobman installed
- [ ] KOReader working
- [ ] SSH/terminal working (optional)
- [ ] Fonts/dictionaries added
- [ ] Calibre or Send to Kindle set up

---

## 中文速览：越狱后 20 分钟 Starter Pack

1. **先装 Hotfix**（阻断 OTA、防变砖）→ 删除根目录 `.bin` → 重启确认越狱还在。
2. 装 **KPM**（应用商店）+ **Jobman**（管理 GUI）。
3. 必备：**KOReader**（阅读神器）、**kterm**（终端）、**USBNetLite**（SSH）、字体与词典。
4. 电脑端装 **Calibre** 或直接用 **Send to Kindle**；看漫画装 **KCC**；最后做个备份。
