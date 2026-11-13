const CACHE='awesome-kindle-v2';
const ASSETS=["./", "index.html", "app.js", "style.css", "page.css", "resources.json", "jailbreaks.json", "offline.html", "wizard.html", "wizard.js", "status.html", "manifest.webmanifest", "icon.png", "404.html", "community.html", "export.html", "guides/android-flash.html", "guides/buying-guide.html", "guides/calibre.html", "guides/china-survival.html", "guides/customize.html", "guides/kcc.html", "guides/koreader-notes.html", "guides/koreader.html", "guides/kpm.html", "guides/ssh-terminal.html", "guides/starter-pack.html", "guides/troubleshooting.html", "guides/usbnet-tailscale.html", "jailbreaks/adbreak.html", "jailbreaks/android-flash.html", "jailbreaks/languagebreak.html", "jailbreaks/niluje.html", "jailbreaks/nosebleed.html", "jailbreaks/sanctuary.html", "jailbreaks/shadow.html", "jailbreaks/spidercat.html", "jailbreaks/springbreak.html", "jailbreaks/vera.html", "jailbreaks/winterbreak.html", "jailbreaks/winterbreak2.html", "verified.html"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).catch(() => {})); self.skipWaiting(); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request).then((resp) => {
    const cp = resp.clone(); caches.open(CACHE).then((c) => c.put(e.request, cp)).catch(() => {}); return resp;
  }).catch(() => r)));
});
