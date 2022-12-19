const staticAssets = [
    '/',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/bootstrap5/main.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/main.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/message.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/mobile.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/nav-sidebar.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/css/sidebar.css',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/axios0.21,js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/main.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/message.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/move_top.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/nav_sidebar_menu.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/search_modal.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/js/select_redirect.js',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/chant.png',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/daily_mass.png',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/logo.png',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/mobile_logo_black.png',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/mobile_logo_white.png',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/check-circle-dill.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/check-circel.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/flower.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/picture.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/schedule.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/school.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/video.svg',
    'https://daechi4.s3.ap-northeast-2.amazonaws.com/static/icon/weekly.svg',
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