from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E13', tag='S3 · E13', short='LAZY ROUTES')

def hook(c):
    tf = c.T('fifty')
    if c.on(tf):
        for k in range(50):
            t = tf + k * 0.02
            if not c.on(t): continue
            x = 130 + (k % 10) * 85; y = 380 + (k // 10) * 95
            home = k == 0
            c.pen.rr(x, y, x + 70, y + 80, 8, fill=YEL if home else WHITE, outline=INK, w=3)
            if c.on(c.T('history')) and not home:
                c.pen.rr(x, y, x + 70, y + 80, 8, fill=(255, 215, 215), outline=INK, w=3)
    tl = c.T('home')
    if c.on(tl): label(c, 540, 900, 'lands on: /home', tl, YEL, INK, 34)
    tq = c.T('download')
    if c.on(tq): txt(c, 540, 1000, 'download code for the other 49?', tq, 'intx', 40, INK)
    tc = c.T('course')
    if c.on(tc): stamp(c.cv, 540, 1150, 'OF COURSE NOT', 72, c.P(tc, 0.35), -3, RED); c.sfx(tc, 'thud')

def lazy(c):
    title(c, 'LAZY ROUTES', 330, c.T('Lazy'), 110, hlcol=YEL)
    code(c, 40, 450, 1040, 900, ["const Orders = lazy(() => import('./pages/Orders'));", '', '<Suspense fallback={<Spinner />}>', '  <Routes>',
                                 '    <Route path="/orders" element={<Orders />} />', '  </Routes>', '</Suspense>'],
         c.T('React') - 0.4, 0.12, 25, 'App.jsx', marks=[(0, c.T('lazy', 2), YEL), (2, c.T('Suspense'), YEL)])
    tn = c.T('navigates')
    if c.on(tn): label(c, 540, 1000, 'chunk loads on first visit to /orders', tn, WHITE, INK, 32)

def hotel(c):
    title(c, 'LIGHTS ON WHEN YOU ENTER', 330, 0.1, 76)
    tw = c.T('walk')
    for k in range(5):
        x = 140 + k * 170
        lit = c.on(tw) and k == 2
        c.pen.rect(x, 500, x + 150, 900, fill=(255, 238, 150) if lit else (70, 74, 84), outline=INK, w=4)
        c.pen.text(x + 75, 540, f'{201 + k}', 'intx', 30, INK if lit else (150, 150, 160))
        if lit: c.pen.circ(x + 75, 640, 30 * c.B(tw, 0.3), fill=YEL, outline=INK, w=3)
    if c.on(tw): person(c.pen, 140 + 2 * 170 + 75, 880, 1.1, BLUE)
    c.pen.rect(110, 900, 970, 930, fill=(150, 110, 70))
    te = c.T('empty')
    if c.on(te): txt(c, 540, 1040, 'no one pays for empty rooms', te, 'intx', 40, INK)

def cost(c):
    title(c, 'HIDE THE DELAY', 330, c.T('hide'), 100)
    tc = c.T('cost')
    if c.on(tc): timerbar(c, 140, 520, 940, c.P(tc + 0.3, 1.0), tc, 'first visit to /orders', ORANGE, 50, '+300 ms')
    code(c, 40, 660, 1040, 870, ["link.addEventListener('mouseenter', () =>", "  import('./pages/Orders'));  // prefetch on hover"], c.T('Prefetch') - 0.3, 0.15, 26, 'nav.js',
         marks=[(1, c.T('hovers'), YEL)])
    tv = c.T('view')
    if c.on(tv): label(c, 540, 980, 'or when the link scrolls into view', tv, WHITE, INK, 32)
    tn = c.T('Next')
    if c.on(tn): txt(c, 540, 1090, 'Next.js <Link> prefetches visible links in production', tn, 'ints', 30, MUTE)

def rules(c):
    title(c, 'TWO RULES', 330, c.T('rules'), 110)
    rows(c, 90, 540, [('land', "never lazy-load the landing route", 'it adds a round trip before LCP', 'no'),
                      ('fallback', 'give every boundary a fallback', 'that holds the layout · no CLS', 'ok')], 220, 900, 160, 38, 30)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Network', 'JS'), dy=(1 - c.P(0, 0.45)) * 900)
    tc = c.T('click')
    items = [(0, 'main.4f1a.js', ['142 KB']), (0, 'vendor.9c2e.js', ['88 KB']), (tc + 0.4, 'Orders.71bd.js', ['14 KB'], (40, 80, 50)),
             (tc + 1.2, 'Settings.a03f.js', ['9 KB'], (40, 80, 50)), (tc + 2.0, 'Wishlist.5e77.js', ['11 KB'], (40, 80, 50))]
    netrows(c, 100, 490, 1000, items, 28, 80, [820])
    te = c.T('navigate')
    if c.on(te): txt(c, 540, 1000, 'a new chunk per page, on navigation', te, 'intx', 36, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    td = c.T('deploy')
    if c.on(td):
        a = node(c, 280, 560, 380, 200, 'old tab', td, 'laptop', sub='expects Orders.71bd.js')
        b = node(c, 800, 560, 380, 200, 'server', td + 0.3, 'server', sub='now Orders.c9e0.js')
    tc = c.T('crashes')
    if c.on(tc): console(c, 60, 730, 1020, 910, [(tc, 'ChunkLoadError: Loading chunk 7 failed', RED)])
    tk = c.T('Keep')
    if c.on(tk):
        rows(c, 100, 1010, [(tk, 'keep old chunks for a while', None, 'ok'), (c.T('catch'), 'catch it → reload the page', None, 'ok')], 120, 880, 96, 36)

SCENES = [
    (hook, "A shopping app has fifty pages. A first time visitor lands on the home page. Should they download code for order history, settings, and the seller dashboard? Of course not."),
    (lazy, "Lazy routes load each page's code only when someone navigates there. In React, that's React dot lazy with a dynamic import, wrapped in Suspense."),
    (hotel, "It's like a hotel where the lights in a room switch on only when you walk in. Nobody pays for lighting empty rooms."),
    (cost, "The cost is a small delay on the first visit to each page, while its chunk downloads. So hide it. Prefetch the chunk when the user hovers the link, or when it scrolls into view. Next dot js does this for visible links automatically."),
    (rules, "Two rules. Never lazy load the route people land on: it just adds a round trip before LCP. And give every lazy boundary a fallback that holds the layout, so nothing jumps."),
    (proof, "Open the Network panel, filter by JS, and click around a single page app. Each page pulls in its own small chunk, the moment you navigate."),
    (gotcha, "Interview trap: you ship a new deploy. A user with the old version open clicks a link, and the app crashes with a chunk load error. The old file names no longer exist. Keep old chunks around for a while, and catch the error to reload the page."),
    (scene_next('S3 · E14', 'TREE SHAKING', 'how bundlers drop dead code', 'tree', 'dead'),
     "Next: tree shaking, and how bundlers drop dead code. Comment NOTES for the cheat sheet."),
]
