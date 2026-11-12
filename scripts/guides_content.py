# Bilingual guide content for docs/guides/*. Each entry: slug, title, subtitle, body (Markdown).
GUIDES = []

GUIDES.append(dict(
slug="starter-pack", title="Starter Pack — first 20 minutes after jailbreak",
subtitle="The must-install set so your jailbreak is safe and actually useful.",
body=r"""# Starter Pack — first 20 minutes after jailbreak

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
"""))

GUIDES.append(dict(
slug="koreader", title="KOReader — install & first setup",
subtitle="The single best upgrade for any jailbroken Kindle.",
body=r"""# KOReader — install & first setup

KOReader is a cross-platform reader with PDF/CBZ reflow, dictionaries, gestures and
fine typography. It is the #1 reason to jailbreak.

## Install (pick one)
1. **Via KPM** (easiest): open KPM → search `koreader` → install.
2. **Manual**: download the `koreader-kindle-*.zip` release, unzip so `koreader/`
   and `extensions/koreader.sh` land in the USB root, then eject.

## First run
1. Launch from **KUAL** or the **KPM/Jobman** menu (or the `koreader.sh` entry).
2. Set your language, then open a book from `documents/`.
3. Tap the top/bottom edges for menus; long-press for quick actions.

## Recommended settings
- **PDF/DjVu**: enable *Reflow* for text PDFs; use *Page crop* for scans.
- **Dictionaries**: Settings → Dictionary → add StarDict `.dict`/`.idx` files.
- **Gestures**: configure corner taps (brightness, full refresh, rotation).
- **Fonts**: drop `.ttf` into `koreader/fonts/`.

## Where to put books
Copy files into `documents/` over USB, or use Calibre. KOReader reads EPUB, PDF,
CBZ/CBR, FB2, DJVU, MOBI/AZW3 (basic) and more.

---

## 中文速览

- **安装**：KPM 搜 `koreader` 安装；或下载 release 解压到根目录（`koreader/` + `extensions/koreader.sh`）。
- **启动**：KUAL / Jobman 菜单进入。
- **优化**：PDF 开 Reflow 与裁边；装 StarDict 词典；配置角落手势；字体放 `koreader/fonts/`。
- **放书**：USB 拷进 `documents/`，或用 Calibre。
"""))

GUIDES.append(dict(
slug="kpm", title="KPM — Kindle Package Manager",
subtitle="Install, update and remove Kindle apps like a package manager.",
body=r"""# KPM — Kindle Package Manager

KPM is `apt` for the Kindle: it installs **scriptlets** and apps from repositories,
handles updates, and keeps things clean.

## Install KPM
1. Download the KPM release from https://github.com/KindleModding/KPM
2. Copy it to the USB root and run the installer as described in its README.
3. Reboot; KPM appears in your launcher / KUAL.

## Use it
- Browse or search for a package, then install.
- Add third-party repositories to get more packages.
- Update packages from the KPM menu; remove what you don't use.

## Build your own (optional)
- A KPM package is a folder + a manifest; scriptlets are just `.sh` apps.
- Docs: https://kindlemodding.org/kindle-dev/kpm/creating-a-package.html

---

## 中文速览

- **安装**：下载 KPM release → 拷到根目录 → 按其 README 安装 → 重启。
- **使用**：搜索/浏览包 → 安装；可添加第三方源；菜单里可更新/卸载。
- **自定义**：KPM 包 = 目录 + manifest；scriptlet 就是 `.sh` 应用。文档见官方。
"""))

GUIDES.append(dict(
slug="kcc", title="KCC — Kindle Comic Converter",
subtitle="Turn comics, manga and PDFs into Kindle-perfect files.",
body=r"""# KCC — Kindle Comic Converter

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
"""))

GUIDES.append(dict(
slug="calibre", title="Calibre — manage, convert & send",
subtitle="The desktop hub for your whole library.",
body=r"""# Calibre — manage, convert & send

Calibre is the all-in-one ebook manager: library, metadata, conversion, news recipes
and one-click send-to-device.

## Setup
1. Install from https://calibre-ebook.com/.
2. Add your books; Calibre fetches covers/metadata.
3. Connect the Kindle over USB — Calibre detects it as a device.

## Convert & send
- **Convert**: pick output **AZW3** (older firmware) or **EPUB** (new firmware).
- **Send to device**: select books → *Send to device*; or use *Send to Kindle* (email/app).
- **News**: *Fetch news* → pick a recipe → schedule to your device.

## Power tips
- **FanFicFare** plugin: download web fiction / AO3 / Royal Road as ebooks.
- **EpubMerge**: merge serials into one omnibus.
- **WordDumb**: generate Word Wise / X-Ray files.
- **Calibre-Web**: self-host your library and read from a browser.

---

## 中文速览

- **安装**：calibre-ebook.com；导入书籍自动抓元数据；USB 连接识别设备。
- **转换/推送**：输出 AZW3（老固件）或 EPUB（新固件）；*发送到设备* 或 *Send to Kindle*；*抓取新闻* 定时推送。
- **插件**：FanFicFare（网文/AO3 下载）、EpubMerge（合并）、WordDumb（生词/X-Ray）、Calibre-Web（自建书库）。
"""))

GUIDES.append(dict(
slug="ssh-terminal", title="SSH & terminal on Kindle",
subtitle="Get a real shell and remote access.",
body=r"""# SSH & terminal on Kindle

With a jailbreak you can get a shell — locally with **kterm**, remotely over **SSH**.

## Local terminal
1. Install **kterm** via KPM (or manually).
2. Launch it from KUAL/Jobman — you get a shell on the device.

## Enable SSH (USBNetLite)
1. Install **USBNetLite** → https://github.com/notmarek/kindle-usbnetlite
2. Choose USB or Wi-Fi mode; note the device IP.
3. Set a root password (per its README) before exposing it on Wi-Fi.

## Connect from your computer
```bash
ssh root@<kindle-ip>
# or over USB (usbnet): ssh root@192.168.15.244
```
- Copy files: `scp book.epub root@<kindle-ip>:/mnt/us/documents/`
- Be careful: you can break the system as root. Keep a backup and Hotfix installed.

---

## 中文速览

- **本地终端**：KPM 装 **kterm**，从 KUAL/Jobman 启动即得 shell。
- **开 SSH**：装 **USBNetLite**，选 USB/Wi-Fi 模式，记下 IP，先设 root 密码再对外。
- **连接**：`ssh root@<ip>`；传文件 `scp book.epub root@<ip>:/mnt/us/documents/`。
- **注意**：root 能把系统搞坏；务必装 Hotfix 并备份。
"""))


GUIDES.append(dict(
slug="buying-guide", title="Buying guide — which Kindle to get (2024–2026)",
subtitle="Buy for jailbreak-ability, not just specs.",
body=r"""# Buying guide — which Kindle to get (2024–2026)

If jailbreaking matters to you, **firmware version on the box matters more than the model**.
Amazon ships whatever firmware is current, and a newer firmware can close the door.

## Quick rules
1. **Older firmware = easier.** A unit on ≤ 5.16.3 is the easiest to jailbreak (WinterBreak2, no account).
2. **Newer models may already be patched.** 2025–2026 models (Scribe 3, Colorsoft, 2026 Kindle/Paperwhite) may have no public jailbreak yet — check the matrix first.
3. **Ask the seller for the exact firmware** (Settings → Device Options → Device Info) before buying used.
4. **Buy used/refurb with a return window** so you can verify firmware and return if it's too new.

## By goal
- **Just read + KOReader** → any Paperwhite (PW4/PW5) on older firmware is the sweet spot.
- **Notes / Scribe** → Scribe is great for writing, but confirm jailbreak status first.
- **Color comics** → Colorsoft / color devices; verify firmware support.
- **Cheapest tinkering** → a used PW3/PW4 or even an old K4/K5 for legacy jailbreaks.

## Avoid
- Units advertised with "latest firmware" if you plan to jailbreak.
- Marketplace listings without a firmware screenshot.
- 2025–2026 flagships unless the matrix confirms support.

## Check before you pay
- Exact model code + firmware version.
- Region (some features/ads differ).
- Return policy.

> Always cross-check the [compatibility matrix](https://kindlemodding.org/jailbreaks.json) and the [Jailbreak Wizard](../wizard.html).

---

## 中文速览：买前选购

- **越狱看固件，不只看机型**：≤ 5.16.3 最好越（WinterBreak2 免账号）；2025–2026 新机可能已被封。
- 二手务必让卖家提供**确切固件版本**（设置 → 设备选项 → 设备信息）。
- 只阅读+KOReader：老固件的 PW4/PW5 最香；记笔记看 Scribe；彩漫看 Coloresoft（先确认可越狱）。
- 避开"最新固件"机、无固件截图、未确认支持的新旗舰；保留退货窗口。
- 下单前对照官方兼容矩阵与越狱向导。
"""))

GUIDES.append(dict(
slug="troubleshooting", title="Troubleshooting & brick rescue",
subtitle="Common errors, what they mean, and how to recover.",
body=r"""# Troubleshooting & brick rescue

> Always cross-check with the official wiki: https://kindlemodding.org/

## Common issues
| Symptom / error | Likely cause | Fix |
| --- | --- | --- |
| Jailbreak "not supported" | Firmware/model mismatch | Re-check exact version; use the matching method |
| Update wipes jailbreak | OTA installed | Install **Hotfix**; delete `.bin`; block updates |
| `UPDATE ERROR 2` | Wrong model/firmware update file | Download the exact `.bin` for your device |
| `UPDATE ERROR 4` | Corrupted download | Re-download, verify size, retry |
| Stuck on "Updating" | Interrupted / bad file | Wait, then force-restart; re-flash correct file |
| KUAL won't open | Missing Hotfix / wrong install | Reinstall Hotfix + KUAL per wiki |
| No Wi-Fi after tweak | Network service broken | Revert the tweak; reboot; factory reset last resort |

## Brick rescue decision tree
1. **Does it boot to the UI?** → Yes: reinstall Hotfix, delete `.bin`, reboot.
2. **Boot loop / stuck logo?** → Try a **forced restart** (hold power ~20s). Then a **factory reset** from recovery.
3. **Still dead?** → **Serial/Downgrade recovery** per your model (see wiki). Without a jailbreak you cannot simply downgrade.
4. **Hardware-level** → last resort: serial flash / recovery image per the official guide.

## Golden rules
- Model + firmware must match **exactly**.
- Never flash a mismatched `.bin`.
- Keep **Hotfix** installed and OTA blocked.
- When unsure, stop and read the official page.

---

## 中文速览

- 任何操作先对照官方 Wiki。
- 常见：`UPDATE ERROR 2` = 机型/固件包不匹配；`ERROR 4` = 文件损坏；越狱被 OTA 覆盖 = 没装 Hotfix。
- 救砖顺序：能进系统→重装 Hotfix/删 `.bin`；卡 logo→强制重启/恢复出厂；仍不行→按机型串口/降级恢复；最后才是硬件级。
- 铁律：机型固件必须完全匹配，绝不乱刷 `.bin`，始终装 Hotfix + 阻断 OTA。
"""))

# ---- v2 overrides & new guides (last definition wins) ----
GUIDES.append(dict(
slug="troubleshooting", title="Troubleshooting & brick rescue", subtitle="Real error codes, per-device pitfalls, and how to recover.",
body=r"""# Troubleshooting & brick rescue

> Always cross-check with the official wiki: https://kindlemodding.org/
> Rule #1: **model + firmware must match exactly**; never flash a mismatched `.bin`.

## By symptom (quick table)
| Symptom / error | Likely cause | Fix |
| --- | --- | --- |
| Jailbreak "not supported" | Firmware/model mismatch | Re-check exact version; use the matching method |
| Update wipes jailbreak | OTA installed | Reinstall **Hotfix**, delete `.bin`, block updates |
| `UPDATE ERROR 2` | Wrong model/firmware update file | Download the exact `.bin` for your device |
| `UPDATE ERROR 4` | Corrupted download | Re-download, verify size, retry |
| Error `007` on Hotfix | Hotfix package/model mismatch or partial download | Re-download the Universal Hotfix; try re-running it |
| Hotfix runs then **crash dump**, `;log` stops | Known on PW3 / 5.16.2.1.1 with some Hotfix builds | Reboot fully; retry Hotfix; if still failing, a full reboot usually restores `;log` |
| KUAL opens then returns to home | Hotfix/MRPI not installed in order | Install Hotfix → MRPI → KUAL; full reboot |
| `;log mrpi` does nothing | `mrpackages/` missing or MRPI not installed | Put the `.bin` in `mrpackages/`, install MRPI first |
| KUAL & Hotfix vanish after reset | Factory reset wiped booklets | Reinstall Hotfix, then MRPI, then KUAL |
| Can't write/delete over USB | Filesystem quirk after JB | Reboot; use a file manager app or `scp`; re-mount |

## By device
- **PW3 / 5.16.2.1.1** — many Hotfix 2.x crash reports. Try a full reboot after the booklet; `DISABLE_CORE_DUMP` empty file reduces crash dumps. WB2 recent builds may not need the Hotfix at all — check the method page.
- **K4 / DX / DXG** — modern Hotfix does **not** support these. Use NiLuJe's legacy K5 jailbreak + hotfix from MobileRead.
- **PW1 / old PW5 & HTTPS fails** — the built-in browser often can't load HTTPS. Host the jailbreak page locally over **http** (`node ./api/index.js` → `http://<your-ip>:3000`) or use an http mirror.
- **Colorsoft** — jailbreak works, but the "stay-jailbroken after reboot / Hotfix" step was unreliable; read the current method page.
- **MTP Kindles** — the disk-filler script may not work; fill storage manually with junk files (and remove `.partial.tmp.bin`).

## KPM not installing / add-repo fails
- The `;` search-bar commands are whitelisted by Amazon's `scriptExecutor` — arguments with `:` or `.` (e.g. a repo URL) are **silently dropped**.
- Workaround: install via **KPM scriptlet** or run `kpm install file:///...` from **kterm**; or use the repo's install scriptlet instead of a raw URL.

## Brick rescue decision tree
1. **Boots to UI?** → reinstall Hotfix, delete `.bin`, reboot.
2. **Boot loop / stuck logo?** → forced restart (hold power ~20s); then recovery factory reset.
3. **Still dead?** → serial / downgrade recovery per your model — **downgrade requires an existing jailbreak**.
4. **Hardware-level** → last resort: serial flash / recovery image.

---

## 中文速览

- 铁律：机型+固件必须完全匹配，绝不乱刷 `.bin`；始终装 Hotfix + 阻断 OTA。
- 错误码：`UPDATE ERROR 2`=包不匹配；`UPDATE ERROR 4`=文件损坏；`007`=Hotfix 包不匹配/没下全。
- PW3/5.16.2.1.1 Hotfix 崩溃：整机重启后再试；`DISABLE_CORE_DUMP` 可减少崩溃转储。
- K4/DX/DXG 新版 Hotfix 不支持，用 NiLuJe 旧版 K5 越狱。
- PW1/老 PW5 打不开 HTTPS：本地用 http 托管（`node ./api/index.js`）。
- KPM add-repo 带 URL 会被 `;` 命令白名单吞掉：改用 KPM scriptlet 或 `kterm` 里 `kpm install file://...`。
- 救砖顺序：进系统→重装 Hotfix/删 bin；卡 logo→强制重启/恢复出厂；仍不行→按机型串口/降级（需已越狱）；最后硬件级。
"""))

GUIDES.append(dict(
slug="buying-guide", title="Buying guide — which Kindle to get (2024–2026)", subtitle="Buy for jailbreak-ability, and verify a used unit before you pay.",
body=r"""# Buying guide — which Kindle to get (2024–2026)

If jailbreaking matters, **the firmware on the box matters more than the model**. Amazon ships
whatever is current, and newer firmware can close the door.

## Quick rules
1. **Older firmware = easier.** A unit on ≤ 5.16.3 is easiest (WinterBreak2, no account).
2. **Newer models may already be patched.** 2025–2026 models (Scribe 3, Scribe Colorsoft, 2026 Kindle/Paperwhite) may have no public jailbreak yet — check the [status board](../status.html).
3. **Ask for the exact firmware** (Settings → Device Options → Device Info) before buying used.
4. **Buy used/refurb with a return window** so you can verify and return if it's too new.

## Used-unit checklist (do this before paying)
- [ ] Seller sends a photo of **Settings → Device Options → Device Info** (model code + full firmware).
- [ ] Firmware is **within a supported range** (see status board).
- [ ] Registered/account status: **deregistered** or you can register; note region.
- [ ] **Ads / Special Offers** status (affects AdBreak; some prefer ad-free).
- [ ] Screen: no dead pixels, even frontlight, no scratches; check a white page.
- [ ] Battery holds charge; charges over USB-C/micro-USB as applicable.
- [ ] Buttons/ touch, Wi-Fi connect, factory reset works.
- [ ] Return window + price sanity (compare eBay / 闲鱼 / local).

## By goal
- **Just read + KOReader** → Paperwhite PW4/PW5 on older firmware is the sweet spot.
- **Notes / Scribe** → Scribe is great, but confirm jailbreak status first.
- **Color comics** → Colorsoft; verify firmware support.
- **Cheapest tinkering** → a used PW3/PW4 or an old K4/K5 for legacy jailbreaks.

## Avoid
- "Latest firmware" units if you plan to jailbreak.
- Listings without a firmware screenshot.
- 2025–2026 flagships unless the matrix confirms support.

---

## 中文速览：买前与二手验机

- **越狱看固件不只看机型**：≤ 5.16.3 最好越；2025–2026 新机多半无解，先看[支持状态](../status.html)。
- **二手验机清单**：要卖家拍「设备信息」截图（机型+完整固件）；确认在支持范围内；账号是否已注销/可注册；是否广告版；屏幕/前光/坏点；电池；USB 充电；按键触控；Wi-Fi；能否恢复出厂；退货窗口与价格。
- 只阅读+KOReader：老固件 PW4/PW5 最香；记笔记看 Scribe（先确认可越）；彩漫看 Colorsoft；最便宜折腾用旧 PW3/PW4 或 K4/K5。
- 避开“最新固件”、无固件截图、未确认支持的新旗舰。
"""))

GUIDES.append(dict(
slug="koreader-notes", title="KOReader — export highlights & notes", subtitle="Get your annotations out to Markdown, Notion or Readwise.",
body=r"""# KOReader — export highlights & notes

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
"""))

GUIDES.append(dict(
slug="china-survival", title="Kindle 退出中国后的生存指南", subtitle="防删书 / 微信读书 / Android 与本地阅读的可行路径。", body=r"""# Kindle 退出中国后的生存指南

> Amazon 已于 2023 年停止 Kindle 中国电子书店运营、2024 年停止相关服务。很多用户反馈
> **联网后本地中文书会被清理**，账号/手机号也可能失效。下面是不踩坑的几条路。

## 先做：防删书（最重要）
1. 开 **飞行模式**，别让设备联网；需要传书时用 **USB**。
2. 把 `documents/` 整目录**备份到电脑**；删除前先导出。
3. 关闭自动更新 / 装 Hotfix 阻断 OTA（见越狱指南）。
4. 用 **Calibre** 管理并在本地转 EPUB/AZW3 再侧载，不依赖云端。

## 路线 A：越狱 + 本地阅读（推荐，风险低）
- 越狱后装 **KOReader**，直接读本地 EPUB/PDF/CBZ；配 **Calibre-Web** 可自建书库、浏览器推送。
- 不需要账号、不联网也能用；笔记用 KOReader 导出（见《KOReader 笔记导出》）。

## 路线 B：微信读书
- **网页版**体验一般（每章联网加载），但零风险：用内置浏览器开 `weread.qq.com`。
- **进阶**：越狱 → 装 KUAL/MRPI → 刷 **Android** → 安装**微信读书墨水屏版**。
  这是社区最常见做法，但**刷 Android 风险高**，务必先看官方/社区教程并备份。
  - 参考路径：越狱 → MRPI + KUAL → uboot → 刷 Android → 装微信读书墨水屏版。

## 路线 C：换区账号
- 把账号切到美亚/其他区可继续用商店（需对应支付/地址），但中文书资源有限。

## 风险与提醒
- 刷 Android / 改分区可能**变砖**；没有把握就先用路线 A（越狱+KOReader）。
- 任何固件/分区操作前，确认机型与固件、备份、留回滚方案。
- 一切以官方 Wiki 与成熟社区教程为准。

---

## English summary
After Kindle exited China (store closed 2023, services 2024), many users report **sideloaded
Chinese books being deleted when the device goes online**. Safest path: **airplane mode + USB
sideload + Calibre**, back up `documents/`, and jailbreak + **KOReader** for local reading.
For **WeRead**, either use the web version (low risk) or the advanced route: jailbreak →
KUAL/MRPI → flash **Android** → install the e-ink WeRead app (high risk — back up first).
Switching to a US/other-region account is another option but has limited Chinese catalog.
""")) 
