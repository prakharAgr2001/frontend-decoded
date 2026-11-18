from engine.lib import *

EP = dict(id='S2E07', tag='S2 · E07', short='IQ: CSR · SSR · SSG · ISR', hook='CSR · SSR · SSG · ISR')

SCENES = [
    (scene_iq_intro('CSR · SSR · SSG · ISR'),
     "Four interview questions on rendering strategies. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'View Source shows only an empty root div. Which strategy is this, and what is one SEO risk?',
              [('client', 'client-side rendering (CSR)'), ('crawlers', 'crawlers / link previews without JS'), ('page', 'see an empty page')]),
     "Question one. View Source shows only an empty root div. Which strategy is this, and what's one SEO risk? [[3]] Answer: client side rendering. Crawlers and link previews that don't run JavaScript see an empty page."),
    (scene_iq(2, 'Users get a 404 when they refresh /products/42 in your SPA. Why, and what is the fix?',
              [('file', 'the server has no file at that path'), ('rewrite', 'fix: rewrite every route to index.html')]),
     "Question two. Users get a 404 when they refresh slash products slash forty two in your single page app. Why, and what's the fix? [[3]] Answer: the server has no file at that path. The router only exists in the browser. Fix: rewrite every unknown route to index dot html."),
    (scene_iq(3, 'After moving to SSR, TTFB got worse, but the page appears sooner. How?',
              [('builds', 'HTML is built before byte one → TTFB ↑'), ('content', 'but that HTML already has content'),
               ('wait', 'first paint no longer waits for JS')]),
     "Question three. After moving to server side rendering, Time To First Byte got worse, but the page appears sooner. How? [[3]] Answer: the server builds the HTML before sending the first byte, so that number goes up. But the HTML already has content, so the first paint no longer waits for JavaScript."),
    (scene_iq(4, 'Pick a strategy: a blog, a product page with hourly prices, a logged-in dashboard.',
              [('static', 'blog → SSG'), ('incremental', 'product page → ISR (or SSR)'), ('client', 'dashboard → CSR (no SEO needed)')]),
     "Question four. Pick a strategy for each: a blog, a product page with hourly prices, and a logged in dashboard. [[3]] Answer: the blog, static generation. The product page, incremental regeneration, or server rendering. The dashboard, client rendering, because it's behind a login and needs no SEO."),
    (scene_next('S2 · E08', 'HYDRATION', 'just add hot water', 'hydration', 'water'),
     "Got all four? Tell me your score below. Next: hydration. Just add hot water. Comment NOTES for the cheat sheet."),
]
