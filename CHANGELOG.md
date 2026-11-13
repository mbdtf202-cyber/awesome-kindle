# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.2.0] - 2026-11-13

### Added
- 🔎 Search UX: URL-shareable state (`?q=&s=&lang=&theme=`), fuzzy matching, `/` shortcut, Esc to clear.
- 🌐 SEO/quality: `sitemap.xml`, `robots.txt`, `404.html`, per-page description + OpenGraph/Twitter tags, skip-link.
- ⬇️ **Export & API** page + `resources.csv` / `resources.md` exports (JSON already existed).
- ✅ **Verified setups** page + `data/verified.json` + “Report your working setup” issue form.
- 📚 3 new guides: USBNetLite + Tailscale, Android (overview), Customize (fonts/screensavers/ads/collections).
- 💬 **Community** page (top needs + how to contribute); GitHub **Discussions** enabled; “Request a guide” form.
- 🔄 **Upstream sync** workflow: weekly diff of `kindlemodding.org/jailbreaks.json` → auto-issue + snapshot.
- 🩺 Link-health summary in CI; guide “Last reviewed” stamps.
- 🧪 `scripts/audit.py` + `AUDIT.md`: internal links/anchors, HTML basics, parity, data, sitemap.
- 🏷️ README CI/last-commit badges.

## [2.1.0] - 2026-11-12

### Added — community-driven
- 📊 **Jailbreak status board** (`docs/status.html`): max supported firmware, per-method status, and a **"not supported yet" watchlist** (Scribe 3, Scribe Colorsoft, 2026 Kindle/Paperwhite).
- 🧭 Wizard now warns "no public jailbreak yet — don't flash" and links the status board when nothing matches.
- 🧯 **Troubleshooting v2**: real error codes (`UPDATE ERROR 2/4`, `007`), per-device pitfalls (PW3 Hotfix crash, K4/DX unsupported, PW1/PW5 HTTPS, Colorsoft persistence, MTP fill), KPM `add-repo` workaround.
- 📝 New guide **KOReader — export highlights & notes** (My Clippings / built-in export / `.sdr` script).
- 🇨🇳 New guide **Kindle 退出中国后的生存指南** (防删书 / 微信读书 / Android / 本地阅读).
- 🛒 Buying guide upgraded with a **used-unit checklist** (firmware screenshot, account, ads, screen, battery, USB, return window).
- 🇯🇵🇰🇷 Expanded 日本語 / 한국어 digests (status + full section map).

## [2.0.0] - 2026-11-12

### Added — "make it a real one-stop product"
- 🔓 **12 step-by-step jailbreak pages** (`docs/jailbreaks/`) generated from the compatibility matrix.
- 🧰 **8 mini-guides** (`docs/guides/`): Starter Pack, KOReader, KPM, KCC, Calibre, SSH/terminal, Troubleshooting & brick rescue, Buying guide — each with an English walkthrough + 中文速览.
- 🧭 **Jailbreak Wizard** (`docs/wizard.html`): pick model + firmware → matching methods.
- 🖥️ **Site UX**: EN/中文 toggle, light/dark theme, card **detail modal** + copy link, nav bar.
- ⬇️ **Offline single-file export** (`docs/offline.html`) + **PWA** (manifest + service worker + icon).
- 🇯🇵🇰🇷 Condensed **日本語 / 한국어** READMEs.
- 🤖 Bilingual machine-readable index (137 items) + **JSON Schema** + `scripts/validate_data.py`.
- ⚙️ **Automation**: `build-data` workflow auto-regenerates `resources.json`; **Quality** CI (data + generated-docs reproducibility); broken-link **auto-issue**; **Dependabot**.
- 🔐 Repo hygiene: `SECURITY.md`, `CODEOWNERS`, `FUNDING.yml`, richer PR checklist.

### Changed
- `docs/` is now a small multi-page site (index + jailbreaks + guides + wizard + offline) sharing `style.css` / `page.css`.
- `scripts/build_resources.py` merges **both** READMEs for bilingual fields; added `scripts/mdmini.py`, `scripts/build_docs.py`, `scripts/build_offline.py`, `scripts/guides_content.py`.

## [1.5.0] - 2026-11-12

### Added
- 📚 **Library borrowing & official subscriptions** — Libby / OverDrive / Hoopla / cloudLibrary / Everand (free legal borrowing with a library card).
- 📰 **RSS / news / magazines / web fiction** — Reabble, Inoreader, Feedly, NewsBlur, Wattpad, Scribble Hub (schedule onto the device with Calibre Recipes / KindleEar).
- 🎨 **Fonts / wallpapers / public-domain art / offline dictionaries** — Google Fonts, Font Squirrel, WikiArt, Met Open Access, Rijksmuseum, Wikimedia Commons, Wiktionary, GoldenDict.
- 🤖 Machine-readable index grows to **137 items** (12 jailbreak + 125 tools/sites); generator re-run, `docs/resources.json` synced.

## [1.4.0] - 2026-11-12

### Added
- 🌐 **Live searchable site** on GitHub Pages (served from `docs/`): https://mbdtf202-cyber.github.io/awesome-kindle/
- 🖼️ `assets/site-preview.png` — screenshot of the searchable index, embedded in both READMEs.
- 🔗 Site entry points in both READMEs (header + "What is this"); the repo homepage now points to the live site.

### Changed
- The docs build is a single static page with **no build step**; regenerate the index with `python3 scripts/build_resources.py`.

## [1.3.0] - 2026-11-12

### Added
- 🧭 **One-stop roadmap** section (bilingual): buy → check firmware → jailbreak → harden → apps → content → convert → transfer.
- 🔎 **Searchable static site** in `docs/` (vanilla HTML/CSS/JS, no build step) — deployable on GitHub Pages.
- 🤖 **Machine-readable index** `data/resources.json` (118 items) + reproducible generator `scripts/build_resources.py`.
- 🗺️ `ROADMAP.md` and `SUPPORT.md`.
- 📝 Renamed the project to **awesome-kindle** (fixed the missing "e"); updated LICENSE holder.

## [1.2.0] - 2026-11-12

### Added
- 🗂️ **Content sources** section (bilingual): public-domain / free ebooks (EN + 中文 + classics),
  free comics, audiobooks, open-access papers, sheet music, offline Wikipedia, web fiction.
- 🧰 Find → convert → transfer pipeline (Calibre, FanFicFare, EpubMerge, KCC, Send to Kindle).
- ⚖️ A clear **legal-only policy**: no pirate / shadow-library links, to keep the repo compliant and DMCA-safe.

## [1.1.0] - 2026-11-12

### Added
- 🇬🇧 **English edition** ([README_EN.md](README_EN.md)) fully mirroring the Chinese README.
- 🎨 Hand-drawn SVG banner (`assets/banner.svg`) shown in both READMEs.
- 🖼️ `assets/social-preview.svg` + generated **1280×640 `social-preview.png`** for GitHub's repo social preview.
- ⚙️ `.editorconfig` for consistent formatting.
- ⚡ **Quick start (5 minutes)** and **Identify your device & firmware** sections.
- ⚖️ **Why jailbreak (pros & cons)** section.
- 🧭 **Glossary** of Kindle modding terms.
- 🤝 `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.
- 🗂️ GitHub issue forms (add-resource, broken-link) and a PR template.
- 🔗 **Link-check CI** (`lychee`) running on push / PR / weekly schedule.

### Changed
- Wording now frames the project as an **open index for everyone**, not for a single language group.
- Unified the brand title to **Awesome Kindle** across both languages.

## [1.0.0] - 2026-11-12

### Added
- Initial release: Chinese README with the full jailbreak compatibility matrix, device table,
  post-jailbreak ecosystem, app/game lists, firmware & recovery guide, and FAQ.
- MIT `LICENSE`, `.gitignore`.
