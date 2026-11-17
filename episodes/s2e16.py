from engine.s2_extra import *

EP = dict(id='S2E16', tag='S2 · E16', short='ISLANDS ARCHITECTURE')

def hook(c):
    p = panel(c, 50, 330, 1030, 1100, ('Elements',), 0, (1 - c.P(0, 0.45)) * 900)
    ts = c.T('search')
    lines = [('<main>', WHITE), ('  <h1>Build the web you want</h1>', WHITE), ('  <p>…static text…</p>', (150, 156, 166)),
             ('  <astro-island component-url=…', YEL), ('    client="visible">', YEL), ('  </astro-island>', YEL), ('  <footer>…</footer>', WHITE), ('</main>', WHITE)]
    for i, (ln, col) in enumerate(lines):
        at = 0.4 + i * 0.12
        if c.on(at): c.pen.text(100, 470 + i * 70, ln, 'mono', 28, col, 'lm')
    if c.on(ts): c.pen.rr(84, 640, 1000, 840, 12, outline=YEL, w=5)
    tw = c.T('What')
    if c.on(tw): stamp(c.cv, 540, 1230, 'WHAT IS THAT TAG?', 66, c.P(tw, 0.4), -4, RED)

def sea(c):
    title(c, 'ISLANDS ARCHITECTURE', 340, c.T('Islands'), 84, hlcol=YEL)
    ts = c.T('sea')
    if c.on(ts):
        c.pen.rr(90, 450, 990, 1200, 30, fill=mix(WHITE, BLUE, 0.25 * c.P(ts, 0.6)), outline=INK, w=5)
        for k in range(6):
            y = 500 + k * 120
            pts = [(120 + i * 30, y + 10 * math.sin(i * 0.8 + c.t * 2)) for i in range(29)]
            c.pen.line(pts, (180, 200, 235), 3)
        c.pen.text(540, 1160, 'static HTML · zero JS', 'int', 30, BLUE)
    isl = [('search', 300, 640, 'Only'), ('carousel', 760, 760, 'Only'), ('comments', 400, 1000, 'Only')]
    for k, (n, x, y, kw) in enumerate(isl):
        at = c.T(kw) + k * 0.3
        if not c.on(at): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.35)
        c.pen.ell(x - 140 * s, y - 70 * s, x + 140 * s, y + 70 * s, fill=(240, 210, 120), outline=INK, w=5)
        c.pen.text(x, y, n, 'intx', 34 * s, INK)
    to = c.T('own')
    if c.on(to): label(c, 540, 1270, 'each island hydrates on its own', to, YEL, INK, 30)

CODE = ['---', "import Header from './Header.astro';", "import Search from './Search.jsx';", "import Comments from './Comments.jsx';", '---',
        '<Header />', '<Search client:load />', '<Comments client:visible />']

def how(c):
    code(c, 60, 340, 1020, 340 + 72 + 8 * 52 + 40, CODE, c.T('Astro'), 0.12, 29, 'index.astro',
         marks=[(5, c.T('plain'), YEL), (6, c.T('load'), YEL), (7, c.T('visible'), YEL)])
    rows = [('client:load', 'hydrate now', 'load'), ('client:visible', 'when scrolled into view', 'visible'), ('client:idle', 'when the browser is free', 'idle')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw); y = 940 + i * 80
        if not c.on(at - 0.01): continue
        pill(c.pen, 260, y, a, c.B(at, 0.35), YEL, INK, 30)
        txt(c, 440, y, b, at, 'ints', 32, INK, 'lm', 'slide')
    ti = c.T('IntersectionObserver')
    if c.on(ti): chapter(c, 540, 1220, 'S1 · E23', 'IntersectionObserver', ti)

def compare(c):
    tf = c.T('full')
    if c.on(tf):
        c.pen.text(290, 360, 'full hydration', 'intx', 38, INK)
        fill_page(c, (90, 410, 490, 1000), 'full'); c.pen.rr(90, 410, 490, 1000, 10, outline=INK, w=4)
        c.pen.rr(90, 410, 490, 1000, 10, fill=None, outline=RED, w=10)
        label(c, 290, 1060, 'whole page hydrated', tf, RED, WHITE, 26)
    ti = c.T('islands')
    if c.on(ti):
        c.pen.text(790, 360, 'islands', 'intx', 38, INK)
        fill_page(c, (590, 410, 990, 1000), 'full'); c.pen.rr(590, 410, 990, 1000, 10, outline=INK, w=4)
        for (a, b, cc, d) in [(610, 760, 970, 820), (610, 960, 970, 990)]:
            c.pen.rr(a, b, cc, d, 8, fill=None, outline=GRN, w=8)
        label(c, 790, 1060, 'only the widgets', ti, GRN, WHITE, 26)
    tk = c.T('kilobytes')
    if c.on(tk):
        timerbar(c, 120, 1180, 480, 0.95, tk, None, RED, 44); timerbar(c, 620, 1180, 980, 0.18, tk, None, GRN, 44)
        c.pen.text(540, 1270, 'JS shipped (illustrative)', 'int', 26, MUTE)

def gotcha(c):
    trap(c)
    qtext(c, 'Header cart count + an Add button lower down. Two islands. How do they share state?', 450, c.T('share'), 44)
    ts = c.T('separate')
    if c.on(ts):
        node(c, 260, 780, 320, 160, 'CartCount', ts, None, fill=(240, 210, 120), size=34)
        node(c, 820, 780, 320, 160, 'AddButton', ts + 0.2, None, fill=(240, 210, 120), size=34)
        c.pen.text(540, 780, 'no props', 'intx', 40, RED)
    tu = c.T('shared')
    if c.on(tu):
        chips(c, 120, 1000, [('shared store (nanostores)', YEL), ('custom events', CYAN), ('rethink the boundary', WHITE)], tu, 0.5, 30)

SCENES = [
    (hook, "Open a site built with Astro, and search the Elements panel. Most of the page is plain HTML. But a few parts are wrapped in a strange tag: astro island. What is that?"),
    (sea, "That's islands architecture. The page is static HTML by default, a sea with zero JavaScript. Only the interactive widgets become islands, and each island hydrates on its own."),
    (how, "In Astro, components are plain HTML unless you opt in. Each island chooses when to wake up. Client load, right away. Client visible, when it scrolls into view, using an IntersectionObserver. Client idle, when the browser is free."),
    (compare, "Compare that to full hydration, where the whole page becomes one big app. With islands, only the widgets ship code. A content site might send a few kilobytes, instead of hundreds."),
    (gotcha, "Interview trap: a cart count in the header, and an add button lower down. Two islands. How do they share state? They're separate apps, so props can't cross between them. Use a shared store, or custom events, or rethink the boundary."),
    (scene_next('S2 · E17', 'RESUMABILITY', 'skip hydration entirely', 'resumability', 'skip'),
     "Next: resumability. What if you could skip hydration entirely? Comment NOTES for the cheat sheet."),
]
