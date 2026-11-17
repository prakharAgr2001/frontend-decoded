from engine.s2_extra import *

EP = dict(id='S2E08', tag='S2 · E08', short='HYDRATION')

def hook(c):
    fill_page(c, phone(c, 540, 760, 460, 820), 'full')
    tb = c.T('Add')
    if c.on(tb):
        c.pen.rr(380, 1000, 700, 1080, 16, fill=YEL, outline=INK, w=4)
        c.pen.text(540, 1040, 'Add to cart', 'int', 32, INK)
    tt = c.T('tap')
    for k in range(3):
        at = tt + k * 0.6
        if c.on(at) and c.t < at + 0.4:
            c.sfx(at, 'click'); r = 20 + 50 * c.P(at, 0.4)
            c.pen.circ(600, 1050, r, outline=mix(INK, PAPER, c.P(at, 0.4)), w=5)
    tn = c.T('Nothing')
    if c.on(tn): stamp(c.cv, 540, 1280, 'NOTHING HAPPENS', 70, c.P(tn, 0.4), -4, RED)
    ta = c.T('alive')
    if c.on(ta): label(c, 540, 330, 'visible ≠ alive', ta, INK, WHITE, 32)

def define(c):
    title(c, 'HYDRATION', 330, c.T('hydration'), 120, hlcol=YEL)
    tp = c.T('picture')
    if c.on(tp):
        fill_page(c, (100, 460, 470, 900), 'full'); c.pen.rr(100, 460, 470, 900, 8, outline=INK, w=4)
        txt(c, 285, 950, 'server HTML: a picture', tp, 'ints', 30, INK)
    tr = c.T('runs')
    if c.on(tr):
        code(c, 520, 460, 1000, 460 + 72 + 4 * 50 + 30, ['<App />', '  <Header />', '  <Cart onClick={…} />', '  <Grid />'], tr, 0.15, 28, 'components', dy=0)
    tat = c.T('attaches')
    if c.on(tat):
        for k, (x, y) in enumerate([(200, 560), (380, 760), (220, 840)]):
            at = tat + k * 0.25
            if c.on(at):
                c.pen.circ(x, y, 22 * c.B(at, 0.3), fill=YEL, outline=INK, w=4); icon(c.pen, 'bolt', x, y, 0.35)
        label(c, 285, 1060, 'event handlers plugged in', tat, GRN, WHITE, 28)

def noodles(pen, cx, cy, s, wet):
    pen.poly([(cx - 150 * s, cy - 110 * s), (cx + 150 * s, cy - 110 * s), (cx + 110 * s, cy + 140 * s), (cx - 110 * s, cy + 140 * s)], WHITE, INK, 5)
    if wet > 0:
        lvl = cy + 130 * s - 220 * s * wet
        pen.poly([(cx - 145 * s + 35 * s * (1 - wet), lvl), (cx + 145 * s - 35 * s * (1 - wet), lvl), (cx + 110 * s, cy + 136 * s), (cx - 110 * s, cy + 136 * s)], (250, 220, 150))
    for k in range(5):
        y = cy - 70 * s + k * 26 * s
        pts = [(cx - 100 * s + i * 20 * s, y + (8 * s if i % 2 else -8 * s) * (1 - 0.6 * wet)) for i in range(11)]
        pen.line(pts, (220, 170, 60) if wet < 0.5 else (240, 200, 110), 6)

def analogy(c):
    tn = c.T('noodles')
    if c.on(tn):
        c.pen.text(540, 340, 'INSTANT NOODLES', 'osw', 72, INK)
        tw = c.T('water', 1)
        wet = c.P(tw, 2.2, lambda x: x) if c.on(tw) else 0
        noodles(c.pen, 540, 650, 1.3 * c.B(tn, 0.4), wet)
        if c.on(tw) and wet < 1:
            for k in range(6): c.pen.line([(540 - 10 + k * 4, 380 + k * 20), (540 - 10 + k * 4, 420 + k * 20)], BLUE, 6)
    rows = [('noodle cake', 'server HTML', 'cake'), ('hot water', 'JavaScript', 'water'), ('3 minutes', 'hydration', 'minutes')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw, 2 if kw == 'water' else 1); y = 950 + i * 100
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        txt(c, 420, y, a, at, 'intx', 38, INK, 'rm', 'slide')
        arrow(c.pen, 450, y, 510, y, c.P(at, 0.3), INK, 5, 14)
        pill(c.pen, 690, y, b, c.B(at, 0.35), YEL, INK, 30)

CODE = ['// server', 'const html = renderToString(<App />);', '', '// browser', "import { hydrateRoot } from 'react-dom/client';",
        "hydrateRoot(document.getElementById('root'), <App />);"]

def how(c):
    code(c, 20, 340, 1060, 340 + 72 + 6 * 52 + 40, CODE, c.T('server'), 0.15, 26, 'entry.jsx',
         marks=[(1, c.T('renderToString'), YEL), (5, c.T('hydrateRoot'), YEL)])
    tw = c.T('walks')
    if c.on(tw):
        tree(c, [('a', '<App>', 540, 860, None, tw), ('h', '<Header>', 300, 980, 'a', tw + 0.2), ('c', '<Cart>', 540, 980, 'a', tw + 0.35),
                 ('g', '<Grid>', 780, 980, 'a', tw + 0.5)], tw, col=lambda k: YEL if k == 'c' and c.on(c.T('listeners')) else WHITE)
    tn = c.T('not')
    if c.on(tn): stamp(c.cv, 540, 1170, 'DOES NOT REBUILD THE DOM', 52, c.P(tn, 0.4), -3, BLUE)

def cost(c):
    tc = c.T('season')
    if c.on(tc): chapter(c, 540, 340, 'S1 · E14', 'the one-chef kitchen', tc)
    tm = c.T('main')
    if c.on(tm):
        flame(c, 80, 520, 1000, [(0, 0.08, 0, 'Paint'), (0.1, 0.7, 0, 'JS', True), (0.82, 0.08, 0, 'Paint')], tm, 90)
        c.pen.text(80, 470, 'main thread', 'int', 30, INK, 'lm')
    tl = c.T('long')
    if c.on(tl): label(c, 455, 660, 'hydrate()  ·  one long task', tl, RED, WHITE, 30)
    tw = c.T('wait')
    if c.on(tw):
        for k in range(3):
            at = tw + k * 0.25
            if c.on(at):
                c.pen.rr(220 + k * 230, 800, 400 + k * 230, 880, 12, fill=WHITE, outline=INK, w=4)
                c.pen.text(310 + k * 230, 840, 'tap', 'monob', 32, INK); c.pen.text(310 + k * 230, 920, 'waiting…', 'int', 26, RED)

def proof(c):
    p = panel(c, 50, 330, 1030, 1150, ('Performance',), 0, (1 - c.P(0, 0.45)) * 900)
    tr = c.T('record')
    filmstrip(c, 100, 470, 'Screenshots', ['white', 'full', 'full', 'full', 'full', 'full'], tr, 0.15, 128, 200, 22)
    tb = c.T('block')
    if c.on(tb):
        c.pen.text(100, 800, 'Main', 'int', 28, WHITE, 'lm')
        c.pen.rect(250, 840, 250 + 700 * c.P(tb, 0.6), 900, fill=YEL, outline=INK, w=2)
        c.pen.text(600, 870, 'Task · 820 ms', 'int', 26, INK)
        c.pen.poly([(934, 840), (950, 840), (950, 856)], fill=RED)
    th = c.T('hydration')
    if c.on(th):
        for k, nm in enumerate(['hydrateRoot', 'beginWork', 'completeWork']):
            c.pen.rect(250 + k * 20, 910 + k * 50, 900 - k * 120, 950 + k * 50, fill=(250, 220, 120), outline=INK, w=2)
            c.pen.text(270 + k * 20, 930 + k * 50, nm, 'mono', 22, INK, 'lm')
    if c.on(c.T('watered')): label(c, 540, 1240, 'your page being watered', c.T('watered'), YEL, INK, 30)

def gotcha(c):
    trap(c)
    qtext(c, 'Does hydration re-render the page from scratch?', 450, c.T('render'), 48)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 640, 'NO', 110, c.P(tn, 0.35), -6, RED)
    items = [(True, 'reuses the server’s DOM', c.T('reuses')), (True, 'only attaches listeners', c.T('attaches')),
             (False, 'but runs EVERY component again', c.T('every')), (False, '→ CPU cost, nothing visible changes', c.T('nothing'))]
    proscons(c, 110, 790, 980, items, 36, 100)

SCENES = [
    (hook, "Open a server rendered React page on a slow phone, and tap Add to cart the moment it appears. Nothing happens. The button is there. It just isn't alive yet."),
    (define, "The server sent HTML, a picture of the page. To make it interactive, React runs your components again in the browser, and attaches event handlers to the HTML that's already there. That step is called hydration."),
    (analogy, "Think of instant noodles. The dry noodle cake is the server HTML. The shape is all there, but you can't eat it until you add hot water. JavaScript is the water. Hydration is the three minutes you wait."),
    (how, "On the server, renderToString turns components into HTML. In the browser, hydrateRoot walks that same HTML, matches it to your components, and plugs in the listeners. It does not rebuild the DOM."),
    (cost, "And here's the catch from season one. Hydration runs on the main thread, the one chef. A big page means a long task. And while it runs, taps wait in line."),
    (proof, "In DevTools Performance, record a reload. After the first screenshot with content, look for a long scripting block on the main thread. Expand it, and you'll find React's hydration work. That's your page being watered."),
    (gotcha, "Interview trap: does hydration re render the page from scratch? No. It reuses the server's DOM, and only attaches listeners. But it does run every component again. That costs CPU, even though nothing visible changes."),
    (scene_next('S2 · E09', 'HYDRATION MISMATCH', 'the red error everyone hits', 'mismatch', 'red'),
     "Next: hydration mismatch. The red error everyone hits. Comment NOTES for the cheat sheet."),
]
