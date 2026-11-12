(function () {
  const $ = (id) => document.getElementById(id);
  const MODELS = ["PW","PW2","PW3","PW4","PW5","PW6","KV","KT","KT2","KT3","KT4","KT5","KT6","KOA","KOA2","KOA3","KS","KS2","CS","K2","DX","K3","K4"];
  let methods = [];
  const vt = (s) => {
    if (!s) return null;
    const p = String(s).trim().toLowerCase().split(/[^0-9x]+/).filter(Boolean).map(x => x === "x" ? 999 : parseInt(x, 10));
    while (p.length < 6) p.push(0);
    return p;
  };
  const cmp = (a, b) => { for (let i = 0; i < 6; i++) { if (a[i] !== b[i]) return a[i] - b[i]; } return 0; };
  const inRange = (v, r) => cmp(v, r[0]) >= 0 && cmp(v, r[1]) <= 0;
  function matchesModel(m, model) {
    if (!model) return true;
    if (m.models_all) return true;
    if (!m.models || !m.models.length) return true;
    return m.models.some((x) => x.toUpperCase() === model.toUpperCase());
  }
  function matchFw(m, v) {
    if (m.legacy) {
      if (!v) return { ok: true, unknown: true };
      const major = v[0];
      return { ok: major === 2 || major === 4 || (major === 5 && v[1] === 0), unknown: false };
    }
    if (!m.ranges || !m.ranges.length) return { ok: !!v, unknown: true };
    if (!v) return { ok: true, unknown: true };
    if ((m.exclude || []).some(e => cmp(v, e) === 0)) return { ok: false, denied: true };
    return { ok: m.ranges.some(r => inRange(v, r)), unknown: false };
  }
  function render(list, v) {
    const box = $("res");
    if (!list.length) { box.innerHTML = '<p class="meta">No match — double-check the exact firmware. If it is newer than every method, there is <strong>no public jailbreak yet</strong>: wait and do <em>not</em> flash. See the <a href="status.html">status board</a> or the <a href="jailbreaks/index.html">guides</a>.</p>'; return; }
    box.innerHTML = list.map(({ m, fw }) => {
      const badge = fw.unknown ? '<span class="meta">⚠️ check official</span>' : (fw.ok ? '<span class="ok">✓ likely works</span>' : '<span class="no">✗ not this range</span>');
      return `<div class="item"><h3><a href="jailbreaks/${m.slug}.html">${m.name}</a></h3>
        <div class="meta">Firmware: ${m.firmware}</div>
        <div class="meta">Status: ${m.status} · Account: ${m.account} · Ads: ${m.ads} · ${badge}</div></div>`;
    }).join("");
  }
  function run() {
    const model = $("model").value, fwRaw = $("fw").value.trim();
    const v = vt(fwRaw);
    $("hint").textContent = fwRaw ? "" : "Tip: leave firmware empty to list methods that support your model.";
    const scored = methods.map(m => ({ m, fw: matchFw(m, v) }))
      .filter(({ m, fw }) => matchesModel(m, model) && (fw.ok || (!v && matchesModel(m, model))));
    // sort: likely first
    scored.sort((a, b) => (b.fw.ok ? 1 : 0) - (a.fw.ok ? 1 : 0));
    render(scored, v);
  }
  fetch("jailbreaks.json").then(r => r.json()).then(data => {
    methods = data;
    const sel = $("model");
    MODELS.forEach(code => { const o = document.createElement("option"); o.value = code; o.textContent = code; sel.appendChild(o); });
    $("go").addEventListener("click", run);
    $("fw").addEventListener("keydown", e => { if (e.key === "Enter") run(); });
  }).catch(() => { $("res").innerHTML = '<p class="meta">Failed to load jailbreaks.json</p>'; });
})();
