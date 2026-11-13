// Awesome Kindle — static searchable index (bilingual + theme + modal + URL state + fuzzy)
(function () {
  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  const state = {
    items: [], sectionOrder: [], activeSection: "All",
    query: params.get("q") || "",
    lang: params.get("lang") || localStorage.getItem("ak-lang") || "en",
    theme: params.get("theme") || localStorage.getItem("ak-theme") || "dark",
  };

  const host = location.hostname;
  let repoUrl = "";
  if (/\.github\.io$/i.test(host)) {
    const owner = host.split(".")[0];
    repoUrl = `https://github.com/${owner}/awesome-kindle`;
  }
  if (repoUrl) {
    ["repo-link", "repo-link-2"].forEach((id) => { const el = $(id); if (el) el.href = repoUrl; });
    const en = $("readme-en"), zh = $("readme-zh");
    if (en) en.href = `${repoUrl}/blob/main/README_EN.md`;
    if (zh) zh.href = `${repoUrl}/blob/main/README.md`;
  }

  const esc = (s) => String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const cleanSection = (s) => String(s || "").replace(/^[^\p{L}\p{N}]+/u, "").trim();

  const T = {
    en: { tagline: "Jailbreak · Flash · Play — the open-source index for Kindle tinkering.",
          search: "Search tools, sites, games…  ( / to focus )",
          count: (a, b) => `${a} of ${b} resources`, empty: "No matches. Try another keyword.",
          all: "All", open: "Open ↗", copy: "Copy link", copied: "Copied!" },
    zh: { tagline: "越狱 · 刷机 · 玩法 —— Kindle 折腾的一站式开源索引。",
          search: "搜索工具 / 站点 / 游戏…（按 / 聚焦）",
          count: (a, b) => `共 ${b} 条，当前 ${a} 条`, empty: "没有匹配项，换个关键词试试。",
          all: "全部", open: "打开 ↗", copy: "复制链接", copied: "已复制！" },
  };
  const t = () => T[state.lang];

  function syncURL() {
    const p = new URLSearchParams();
    if (state.query) p.set("q", state.query);
    if (state.activeSection && state.activeSection !== "All") p.set("s", state.activeSection);
    if (state.lang !== "en") p.set("lang", state.lang);
    if (state.theme !== "dark") p.set("theme", state.theme);
    const qs = p.toString();
    history.replaceState(null, "", qs ? "?" + qs : location.pathname);
  }

  function applyTheme() {
    document.body.dataset.theme = state.theme;
    const b = $("theme"); if (b) b.textContent = state.theme === "light" ? "☀️" : "🌙";
  }
  function applyLang() {
    document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
    const tag = $("tagline"); if (tag) tag.textContent = t().tagline;
    const s = $("search"); if (s) s.placeholder = t().search;
    document.querySelectorAll("#lang-seg button").forEach((b) => b.classList.toggle("on", b.dataset.lang === state.lang));
    document.querySelectorAll(".topnav a").forEach((a) => {
      const v = a.getAttribute(state.lang === "zh" ? "data-zh" : "data-en"); if (v) a.textContent = v;
    });
    buildChips(); render();
  }

  function label(item, field) {
    if (state.lang === "zh") { const v = item[field + "_zh"]; if (v) return v; }
    return item[field] || "";
  }

  function buildChips() {
    const box = $("chips"); if (!box) return;
    const all = ["All", ...state.sectionOrder];
    box.innerHTML = all.map((s) => {
      let labelText = s === "All" ? t().all : cleanSection(s);
      if (s !== "All" && state.lang === "zh") {
        const it = state.items.find((x) => x.section === s);
        if (it && it.section_zh) labelText = cleanSection(it.section_zh);
      }
      return `<button class="chip${s === state.activeSection ? " active" : ""}" data-sec="${esc(s)}">${esc(labelText)}</button>`;
    }).join("");
    box.querySelectorAll(".chip").forEach((b) =>
      b.addEventListener("click", () => { state.activeSection = b.dataset.sec; syncURL(); buildChips(); render(); }));
  }

  function subseq(hay, needle) {
    let i = 0;
    for (const ch of hay) { if (ch === needle[i]) i++; if (i === needle.length) return true; }
    return needle.length === 0;
  }
  function matches(it) {
    if (state.activeSection !== "All" && it.section !== state.activeSection) return false;
    if (!state.query) return true;
    const hay = [it.name, it.name_zh, it.description, it.description_zh, it.section, it.section_zh, it.subsection, it.subsection_zh]
      .join(" ").toLowerCase();
    const tokens = state.query.split(/\s+/).filter(Boolean);
    return tokens.every((tk) => hay.includes(tk) || subseq(hay, tk));
  }

  function render() {
    const grid = $("grid"); if (!grid) return;
    const list = state.items.filter(matches);
    $("count").textContent = t().count(list.length, state.items.length);
    $("empty").hidden = list.length !== 0;
    $("empty").textContent = t().empty;
    grid.innerHTML = list.map((it) => {
      let h = ""; try { h = new URL(it.url).hostname.replace(/^www\./, ""); } catch (e) {}
      return `<article class="card" data-i="${state.items.indexOf(it)}" tabindex="0" role="button" aria-label="${esc(label(it, "name"))}">
        <span class="tag">${esc(cleanSection(label(it, "section")))}</span>
        <h3>${esc(label(it, "name"))}</h3>
        <p>${esc(label(it, "description"))}</p>
        <span class="go">${esc(h)}</span></article>`;
    }).join("");
    grid.querySelectorAll(".card").forEach((c) => {
      const open = () => openModal(state.items[+c.dataset.i]);
      c.addEventListener("click", open);
      c.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
    });
  }

  let current = null;
  function openModal(it) {
    if (!it) return; current = it;
    $("m-tag").textContent = cleanSection(label(it, "section"));
    $("m-title").textContent = label(it, "name");
    $("m-desc").textContent = label(it, "description");
    $("m-link").href = it.url; $("m-link").textContent = t().open;
    $("m-copy").textContent = t().copy;
    $("modal").hidden = false;
    $("modal-close").focus();
  }
  function closeModal() { $("modal").hidden = true; }

  function boot() {
    applyTheme();
    const seg = $("lang-seg");
    if (seg) seg.addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      state.lang = b.dataset.lang; localStorage.setItem("ak-lang", state.lang); syncURL(); applyLang();
    });
    const th = $("theme");
    if (th) th.addEventListener("click", () => {
      state.theme = state.theme === "light" ? "dark" : "light";
      localStorage.setItem("ak-theme", state.theme); syncURL(); applyTheme();
    });
    const search = $("search");
    if (search) {
      search.value = state.query;
      search.addEventListener("input", (e) => { state.query = e.target.value.trim().toLowerCase(); syncURL(); render(); });
    }
    const mc = $("modal-close"); if (mc) mc.addEventListener("click", closeModal);
    const modal = $("modal");
    if (modal) modal.addEventListener("click", (e) => { if (e.target === modal) closeModal(); });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") { if (modal && !modal.hidden) closeModal(); else { state.query = ""; if (search) search.value = ""; syncURL(); render(); } }
      else if (e.key === "/" && document.activeElement !== search) { e.preventDefault(); if (search) search.focus(); }
    });
    const copy = $("m-copy");
    if (copy) copy.addEventListener("click", async () => {
      if (!current) return;
      try { await navigator.clipboard.writeText(current.url); copy.textContent = t().copied;
        setTimeout(() => copy.textContent = t().copy, 1200); } catch (e) {}
    });

    fetch("resources.json").then((r) => r.json()).then((data) => {
      state.items = data.items || [];
      for (const it of state.items) if (it.section && !state.sectionOrder.includes(it.section)) state.sectionOrder.push(it.section);
      const s = params.get("s"); if (s && state.sectionOrder.includes(s)) state.activeSection = s;
      applyLang();
      syncURL();
    }).catch(() => { $("count").textContent = "Failed to load resources.json"; });
  }
  boot();
  if ("serviceWorker" in navigator) { navigator.serviceWorker.register("sw.js").catch(function(){}); }
})();
