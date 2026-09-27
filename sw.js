// Fokus Spiel — 오프라인 지원 (같은 사이트 파일만 캐시, 온라인이면 항상 최신 먼저)
const CACHE = 'fokus-spiel-20260927052108';
const CORE = ["./", "./index.html", "./manifest.webmanifest", "./shared/fokus.css", "./shared/core.js", "./shared/guide.js", "./shared/sync.js", "./shared/fonts.js", "./icons/icon-192.png", "./icons/favicon.svg", "./crimson-desert/guide.html", "./dark-souls/guide.html", "./dont-starve-together/guide.html", "./street-fighter-5/guide.html", "./total-war-three-kingdoms/guide.html", "./uncharted-waters-2/guide.html", "./baldurs-gate-3/guide.html", "./crimson-desert/cover.jpg", "./dark-souls/cover.jpg", "./dont-starve-together/cover.jpg", "./street-fighter-5/cover.jpg", "./total-war-three-kingdoms/cover.jpg"];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).catch(() => {}).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('fokus-spiel-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return; // Firebase·폰트는 건드리지 않음
  if (!url.pathname.startsWith(new URL(self.registration.scope).pathname)) return;
  e.respondWith(
    fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req, { ignoreSearch: true }).then(r => r || caches.match('./index.html')))
  );
});
