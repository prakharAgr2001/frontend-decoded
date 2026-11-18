from engine.s2_extra import *

EP = dict(id='S2E05', tag='S2 · E05', short='STATIC SITE GENERATION', hook='cook once, serve millions')

def hook(c):
    icon(c.pen, 'globe', 540, 640, 3.4 * c.B(0.1, 0.5))
    for k, (x, y, city) in enumerate([(240, 440, 'Delhi'), (860, 470, 'London'), (200, 860, 'Sydney'), (880, 880, 'New York')]):
        at = c.T('anywhere') + k * 0.15
        if c.on(at): label(c, x, y, city + ' · fast', at, GRN, WHITE, 28)
    tb = c.T('blink')
    if c.on(tb): stamp(c.cv, 540, 1130, 'HOW?', 100, c.P(tb, 0.4), -5, RED)

def define(c):
    title(c, 'STATIC SITE GENERATION', 340, c.T('static'), 80, hlcol=YEL)
    txt(c, 540, 420, 'SSG = HTML built once, at build time', c.T('static') + 0.4, 'ints', 34, MUTE)
    tb = c.T('build')
    if c.on(tb):
        node(c, 200, 640, 220, 150, 'build', tb, 'cpu', size=30)
        for i in range(4):
            at = tb + 0.3 + i * 0.15
            if c.on(at): icon(c.pen, 'doc', 430 + i * 95, 640, 0.9 * c.B(at, 0.3))
    tbf = c.T('before')
    if c.on(tbf): label(c, 540, 780, 'before any user visits', tbf, YEL, INK, 30)
    tc = c.T('copied')
    if c.on(tc):
        cdn = [(200, 1040), (430, 1100), (660, 1040), (890, 1100)]
        for i, (x, y) in enumerate(cdn):
            at = tc + i * 0.15
            if c.on(at):
                node(c, x, y, 170, 130, 'edge', at, 'server', size=26, sound=None)
                arrow(c.pen, 540, 830, x, y - 75, c.P(at, 0.4), INK, 4, 14, dash=True)
    ta = c.T('served')
    if c.on(ta): label(c, 540, 1260, 'served as is — no work per request', ta, GRN, WHITE, 30)

def bottle(pen, cx, cy, s=1.0):
    pen.rr(cx - 20 * s, cy - 120 * s, cx + 20 * s, cy - 80 * s, 6, fill=INK)
    pen.poly([(cx - 22 * s, cy - 80 * s), (cx + 22 * s, cy - 80 * s), (cx + 44 * s, cy - 40 * s), (cx + 44 * s, cy + 100 * s),
              (cx - 44 * s, cy + 100 * s), (cx - 44 * s, cy - 40 * s)], (250, 245, 230), INK, 4)
    pen.rect(cx - 44 * s, cy - 6 * s, cx + 44 * s, cy + 50 * s, fill=YEL, outline=INK, w=3)

def analogy(c):
    tb = c.T('bottled')
    if c.on(tb):
        c.pen.text(540, 360, 'BOTTLED LASSI', 'osw', 70, INK)
        for k in range(6):
            at = tb + k * 0.1
            if c.on(at): bottle(c.pen, 170 + k * 148, 590, c.B(at, 0.3))
    tm = c.T('once')
    if c.on(tm): label(c, 540, 770, 'made once, in bulk', tm, YEL, INK, 32)
    tg = c.T('Grab')
    if c.on(tg): label(c, 540, 860, 'grab and go: zero waiting', tg, GRN, WHITE, 32)
    ti = c.T('identical')
    if c.on(ti): label(c, 540, 990, 'every bottle identical', ti, ORANGE, WHITE, 32)
    tr = c.T('recipe')
    if c.on(tr): label(c, 540, 1080, 'new recipe = new production run', tr, RED, WHITE, 32)

CODE = ['// runs at BUILD time, not per request', 'for (const post of await getPosts()) {', '  const html = renderPage(post);',
        '  await writeFile(`dist/${post.slug}.html`, html);', '}']

def how(c):
    code(c, 30, 360, 1050, 360 + 72 + 5 * 56 + 40, CODE, c.T('build'), 0.15, 29, 'build.js', marks=[(0, c.T('build'), YEL), (3, c.T('file'), YEL)])
    tf = c.T('frameworks')
    if c.on(tf): chips(c, 110, 920, [('Next.js', WHITE), ('Astro', WHITE), ('Hugo', WHITE), ('Gatsby', WHITE), ('Eleventy', WHITE)], tf, 0.2, 32)
    tn = c.T('next')
    if c.on(tn): txt(c, 540, 1130, 'output = plain .html files', tn, 'intx', 40, INK)

def proof(c):
    tk = c.T('kirana')
    if c.on(tk): chapter(c, 540, 340, 'S1 · E06', 'the kirana store (CDN)', tk)
    p = panel(c, 60, 420, 1020, 1100, ('Headers',), 0, (1 - c.P(0, 0.45)) * 900)
    rows = [('cache-control', 'public, max-age=0', 'headers'), ('x-cache', 'HIT', 'hit'), ('age', '86400', 'age')]
    for i, (k, v, kw) in enumerate(rows):
        at = c.T(kw); y = 590 + i * 110
        if not c.on(at): continue
        c.sfx(at, 'tick')
        c.pen.text(110, y, k + ':', 'monob', 30, CYAN, 'lm'); c.pen.text(110 + c.pen.tw(k + ': ', 'monob', 30), y, v, 'mono', 30, WHITE, 'lm')
        if kw != 'headers': c.pen.rr(96, y - 34, 980, y + 34, 10, outline=YEL, w=3)
    tl = c.T('long')
    if c.on(tl): label(c, 540, 1000, 'built long before you asked', tl, YEL, INK, 30)

def gotcha(c):
    trap(c)
    qtext(c, '50,000 products. Prices change every hour. SSG?', 460, c.T('fifty'), 48)
    items = [(False, 'build takes ages for 50k pages', c.T('Builds')), (False, 'prices stale until the next deploy', c.T('stale'))]
    proscons(c, 110, 740, 980, items, 36, 110)
    tg = c.T('gap')
    if c.on(tg): stamp(c.cv, 540, 1060, 'NOT ALONE', 90, c.P(tg, 0.4), -4, RED)

SCENES = [
    (hook, "Why does a documentation page load in a blink, even on a slow connection, from almost anywhere in the world?"),
    (define, "Often it's static site generation. The HTML is built once, at build time, before any user visits. Then the same files are copied to CDN edges and served as is."),
    (analogy, "Think of bottled lassi. Made once, in bulk, then stocked in every shop. Grab and go, zero waiting. But every bottle is identical, and changing the recipe means a new production run."),
    (how, "At build time, a script loops over your content, renders each page, and writes it to a file. Most frameworks do this for you, from Next to Astro to Hugo. What gets deployed is just plain HTML."),
    (proof, "Remember the kirana store from season one? That's the CDN. In DevTools, check the document's response headers. A cache hit, and a large age value. This HTML was built long before you asked."),
    (gotcha, "Interview trap: you have fifty thousand products, and prices change every hour. Is static generation a good fit? Not on its own. Builds get slow, and pages stay stale until the next deploy. That gap is exactly what the next technique fills."),
    (scene_next('S2 · E06', 'INCREMENTAL STATIC REGEN', 'static pages that update themselves', 'incremental', 'update'),
     "Next: incremental static regeneration. Static pages that update themselves. Comment NOTES for the cheat sheet."),
]
