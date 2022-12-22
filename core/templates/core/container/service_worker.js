const staticAssets = [
    '/',
    '{{ static }}css/bootstrap5/main.css',
    '{{ static }}css/main.css',
    '{{ static }}css/message.css',
    '{{ static }}css/mobile.css',
    '{{ static }}css/nav-sidebar.css',
    '{{ static }}css/sidebar.css',
    '{{ static }}js/axios0.21,js',
    '{{ static }}js/main.js',
    '{{ static }}js/message.js',
    '{{ static }}js/move_top.js',
    '{{ static }}js/nav_sidebar_menu.js',
    '{{ static }}js/search_modal.js',
    '{{ static }}js/select_redirect.js',
    '{{ static }}img/chant.png',
    '{{ static }}img/daily_mass.png',
    '{{ static }}img/logo.png',
    '{{ static }}img/mobile_logo_black.png',
    '{{ static }}img/mobile_logo_white.png',
    '{{ static }}icon/check-circle-dill.svg',
    '{{ static }}icon/check-circel.svg',
    '{{ static }}icon/flower.svg',
    '{{ static }}icon/picture.svg',
    '{{ static }}icon/schedule.svg',
    '{{ static }}icon/school.svg',
    '{{ static }}icon/video.svg',
    '{{ static }}icon/weekly.svg',
];

self.addEventListener('install', async event => {
    const cache = await caches.open('static-cache');
    cache.addAll(staticAssets);
});

self.addEventListener('fetch', event => {
    const req = event.request;
    const url = new URL(req.url);

    if(url.origin === location.url){
        event.respondWith(cacheFirst(req));
    } else {
        event.respondWith(newtorkFirst(req));
    }
});

async function cacheFirst(req) {
    const cachedResponse = caches.match(req);
    return cachedResponse || fetch(req);
}

async function newtorkFirst(req) {
    const cache = await caches.open('dynamic-cache');

    try {
        const res = await fetch(req);
        cache.put(req, res.clone());
        return res;
    } catch (error) {
        return await cache.match(req);
    }
}