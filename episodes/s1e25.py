from engine.lib import *

EP = dict(id='S1E25', tag='S1 · E25', short='FINALE: ONE CLICK', tail=3.0)

def chaps(c, items, y0=820, gap=95):
    for i, (tag, name, kw) in enumerate(items):
        at = c.T(kw) if isinstance(kw, str) else kw
        chapter(c, 540, y0 + i * gap, tag, name, at)

def intro(c):
    stamp(c.cv, 540, 420, 'SEASON 1 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'ONE VISIT.', 640, c.T('One', 2), 120)
    title(c, 'EVERY MILLISECOND.', 790, c.T('followed'), 96, hlcol=YEL)
    tg = c.T('go')
    if c.on(tg): icon(c.pen, 'bolt', 540, 1020, 1.6 * c.B(tg, 0.4))

def network(c):
    browser(c, 90, 290, 990, 560, url='')
    addressbar(c, 130, 395, 950, typed_text(c, 'youtube.com', c.T('type'), 0.08), True, 44)
    chaps(c, [('E02', 'DNS', 'DNS'), ('E03', 'TCP', 'TCP'), ('E04', 'TLS', 'TLS'), ('E05', 'HTTP/3', 'three'), ('E06', 'CDN edge', 'CDN')], 660, 108)

def render(c):
    steps = [('DOM', 'DOM'), ('CSSOM', 'CSSOM'), ('Render tree', 'render'), ('Layout', 'layout'), ('Paint', 'paints'), ('Composite', 'composites')]
    for i, (nm, kw) in enumerate(steps):
        at = c.T(kw); x = 115 + (i % 3) * 290; y = 380 + (i // 3) * 150
        if not c.on(at - 0.01):
            c.pen.rr(x, y - 50, x + 270, y + 50, 16, outline=GREY, w=3); continue
        c.sfx(at, 'pop'); s = c.B(at, 0.3)
        col = STAGE_COL.get(nm, YEL if i < 2 else (255, 246, 214))
        c.pen.rr(x + 5, y - 50 * s + 6, x + 275, y + 50 * s + 6, 16, fill=INK)
        c.pen.rr(x, y - 50 * s, x + 270, y + 50 * s, 16, fill=col, outline=INK, w=4)
        c.pen.text(x + 135, y, nm, 'intx', 34 * s, WHITE if nm == 'Layout' else INK)
    chaps(c, [('E08', 'DOM & CSSOM', 'DOM'), ('E09', 'Layout → Paint', 'layout'), ('E09', 'Composite', 'composites')], 820, 110)

def hover(c):
    for i in range(6):
        x = 120 + (i % 3) * 290; y = 330 + (i // 3) * 220
        grow = i == 1 and c.on(c.T('zooms'))
        s = 1 + 0.12 * c.P(c.T('zooms'), 0.4) if i == 1 else 1
        cx, cy = x + 130, y + 90
        w, h = 130 * s, 90 * s
        c.pen.rr(cx - w + 6, cy - h + 8, cx + w + 6, cy + h + 8, 14, fill=INK) if grow else None
        c.pen.rr(cx - w, cy - h, cx + w, cy + h, 14, fill=(60, 64, 72) if i != 1 else (40, 90, 160), outline=YEL if grow else INK, w=5 if grow else 3)
        c.pen.poly([(cx - 18, cy - 24), (cx - 18, cy + 24), (cx + 22, cy)], fill=WHITE)
    th = c.T('hover')
    if c.on(th): c.pen.circ(560, 470, 18, fill=YEL, outline=INK, w=3)
    chaps(c, [('E12', 'transform → compositor', 'transform'), ('E10', 'no reflow · no repaint', 'reflow')], 860, 110)

def click(c):
    chaps(c, [('E20', 'capture ↓ bubble ↑', 'captures'), ('E21', 'one delegated listener', 'delegated'),
              ('E14', 'the one chef (main thread)', 'chef'), ('E15', 'Web APIs → queue', 'web')], 420, 120)
    tc = c.T('click')
    if c.on(tc): stamp(c.cv, 540, 330, 'CLICK', 60, c.P(tc, 0.3), -4, BLUE)
    tr = c.T('request')
    if c.on(tr): packet(c, (300, 960, 500, 1060), (600, 960, 900, 1060), tr, tr + 1.4, YEL, 'GET /video')

def frames(c):
    chaps(c, [('E16', 'tasks + microtasks', 'microtasks'), ('E17', 'requestAnimationFrame', 'requestAnimationFrame'), ('E18', 'no long tasks', 'long')], 420, 120)
    td = c.T('drains')
    if c.on(td):
        for k in range(10):
            x = 120 + k * 86
            col = [CYAN, YEL, YEL, GRN][k % 4]
            if c.on(td + k * 0.08): c.pen.rr(x, 860, x + 76, 940, 10, fill=col, outline=INK, w=3)
        txt(c, 540, 990, 'every frame inside its budget', td + 0.6, 'intx', 36, GRN)

def scroll(c):
    card(c.pen, 290, 330, 790, 1020, 36, WHITE, 12, 5)
    ts = c.T('scroll')
    off = ((c.t - ts) * 160) % 120 if c.on(ts) else 0
    for k in range(6):
        y = 380 + k * 110 - off
        if 350 < y < 960: c.pen.rect(330, y, 750, y + 80, fill=LIGHT)
    if c.on(c.T('IntersectionObserver')): c.pen.line([(292, 930), (788, 930)], YEL, 5, False); c.pen.text(540, 990, 'load next batch', 'int', 26, INK)
    chaps(c, [('E23', 'IntersectionObserver', 'IntersectionObserver'), ('E22', 'cleans up → no leaks', 'cleans')], 1100, 100)

SEASON = ['URL→PIXELS', 'DNS', 'TCP', 'HTTPS', 'HTTP 1·2·3', 'CDNs', 'IQ', 'DOM/CSSOM', 'LAYOUT', 'REFLOW', 'THRASHING', 'TRANSFORM', 'IQ',
          'ONE CHEF', 'CALL STACK', 'MICROTASKS', '16 ms', 'LONG TASKS', 'IQ', 'BUBBLING', 'DELEGATION', 'LEAKS', 'OBSERVERS', 'IQ', 'FINALE']

def wrap(c):
    tt = c.T('Twenty')
    for i, nm in enumerate(SEASON):
        x = 130 + (i % 5) * 205; y = 360 + (i // 5) * 120
        at = tt + i * 0.06
        if not c.on(at): continue
        c.sfx(at, 'tick'); s = c.B(at, 0.3)
        c.pen.rr(x - 92 * s, y - 46 * s, x + 92 * s, y + 46 * s, 12, fill=YEL if nm == 'FINALE' else WHITE, outline=INK, w=3)
        c.pen.text(x, y - 14 * s, f'E{i + 1:02d}', 'int', 20 * s, MUTE)
        c.pen.text(x, y + 14 * s, nm, 'int', 22 * s, INK)
    tn = c.T('Next')
    if c.on(tn):
        darkcard(c.pen, 90, 1000, 990, 1240)
        c.pen.text(540, 1050, 'NEXT · SEASON 2', 'int', 32, YEL)
        c.pen.text(540, 1130, 'RENDERING STRATEGIES', 'osw', 74 * c.B(tn, 0.4), WHITE)
        c.pen.text(540, 1200, 'CSR → SSR → SSG → Server Components', 'int', 30, (180, 186, 196))
    tc = c.T('Comment')
    if c.on(tc): pill(c.pen, 540, 1330, 'Comment NOTES for the full season cheat sheet', c.B(tc, 0.35), YEL, INK, 30)

SCENES = [
    (intro, "Season one finale. One visit to YouTube, followed through everything we've learned. Let's go."),
    (network, "You type youtube dot com and press Enter. DNS finds the address, probably from cache. TCP opens a connection, and TLS locks it. On YouTube, all of this likely rides on HTTP three. And the files arrive from a CDN edge near you."),
    (render, "The browser parses HTML into the DOM, and CSS into the CSSOM. It builds the render tree, runs layout, paints, and composites the layers onto your screen."),
    (hover, "You hover over a thumbnail. The preview zooms with transform, so it stays on the compositor and glides. No reflow. No repaint of the page."),
    (click, "You click. The event captures down and bubbles up, and one delegated listener on the grid catches it. The handler runs on the main thread, the one chef, while the video request goes out through the browser's web APIs."),
    (frames, "Responses come back as tasks and promise microtasks. The event loop drains them, visual updates land in requestAnimationFrame, and the work is split, so no long task blocks your next tap."),
    (scroll, "As you scroll the comments, an IntersectionObserver loads the next batch, and the app cleans up after itself, so the tab doesn't leak."),
    (wrap, "Twenty five episodes. One visit, explained down to the millisecond. Next season: rendering strategies, from client side rendering to server components. Comment NOTES for the full season cheat sheet."),
]
