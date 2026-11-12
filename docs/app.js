// Awesome Kindle — static searchable index
(function () {
  const sectionOrder = [];
  let items = [];
  let activeSection = "All";
  let query = "";

  const $ = (id) => document.getElementById(id);

  // Derive the GitHub repo URL when hosted on GitHub Pages (<owner>.github.io/awesome-kindle)
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
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

  const cleanSection = (s) => String(s || "").replace(/^[^\p{L}\p{N}]+/u, "").trim();

  function buildChips() {
    const box = $("chips");
    const all = ["All", ...sectionOrder];
    box.innerHTML = all.map((s) =>
      `<button class="chip${s === activeSection ? " active" : ""}" data-sec="${esc(s)}">${esc(s === "All" ? "All" : cleanSection(s))}</button>`
    ).join("");
    box.querySelectorAll(".chip").forEach((b) =>
      b.addEventListener("click", () => { activeSection = b.dataset.sec; buildChips(); render(); })
    );
  }

  function matches(it) {
    if (activeSection !== "All" && it.section !== activeSection) return false;
    if (!query) return true;
    const hay = [it.name, it.description, it.section, it.subsection].join(" ").toLowerCase();
    return hay.includes(query);
  }

  function render() {
    const grid = $("grid");
    const list = items.filter(matches);
    $("count").textContent = `${list.length} of ${items.length} resources`;
    $("empty").hidden = list.length !== 0;
    grid.innerHTML = list.map((it) => {
      let host_ = "";
      try { host_ = new URL(it.url).hostname.replace(/^www\./, ""); } catch (e) {}
      return `<article class="card">
        <span class="tag">${esc(cleanSection(it.section))}</span>
        <h3><a href="${esc(it.url)}" target="_blank" rel="noopener">${esc(it.name)}</a></h3>
        <p>${esc(it.description)}</p>
        <span class="go">${esc(host_)}</span>
      </article>`;
    }).join("");
  }

  fetch("resources.json")
    .then((r) => r.json())
    .then((data) => {
      items = data.items || [];
      for (const it of items) {
        if (it.section && !sectionOrder.includes(it.section)) sectionOrder.push(it.section);
      }
      buildChips();
      render();
    })
    .catch(() => {
      $("count").textContent = "Failed to load resources.json";
    });

  const search = $("search");
  if (search) {
    search.addEventListener("input", (e) => {
      query = e.target.value.trim().toLowerCase();
      render();
    });
  }
})();
