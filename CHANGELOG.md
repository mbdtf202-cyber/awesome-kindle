# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
