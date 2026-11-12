const CACHE = "awesome-kindle-v1";
const ASSETS = ["./", "index.html", "app.js", "style.css", "page.css", "resources.json",
  "jailbreaks.json", "offline.html", "wizard.html", "wizard.js", "manifest.webmanifest", "icon.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).catch(() => {})); self.skipWaiting(); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request).then((resp) => {
    const cp = resp.clone(); caches.open(CACHE).then((c) => c.put(e.request, cp)).catch(() => {}); return resp;
  }).catch(() => r)));
});
