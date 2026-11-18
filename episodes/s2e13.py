from engine.s2_extra import *

EP = dict(id='S2E13', tag='S2 · E13', short='STREAMING SSR', hook='send the page before it’s done')

def hook(c):
    box = phone(c, 540, 780, 460, 860)
    x0, y0, x1, y1 = box
    c.pen.rect(x0, y0, x1, y1, fill=WHITE)
    th = c.T('header')
    if c.on(th):
        c.pen.rect(x0, y0, x1, y0 + 70, fill=INK); c.pen.rect(x0 + 20, y0 + 22, x0 + 130, y0 + 48, fill=YEL)
        c.pen.rr(x0 + 24, y0 + 100, x1 - 24, y0 + 330, 12, fill=mix(WHITE, BLUE, 0.6))
    tr = c.T('rest')
    for k in range(3):
        y = y0 + 370 + k * 140
        if c.on(tr + 0.6 * k + 0.6):
            c.pen.rr(x0 + 24, y, x1 - 24, y + 120, 10, fill=(236, 240, 248)); c.pen.rr(x0 + 44, y + 20, x0 + 220, y + 44, 6, fill=INK)
        elif c.on(th):
            c.pen.rr(x0 + 24, y, x1 - 24, y + 120, 10, fill=LIGHT)
    tn = c.T('without')
    if c.on(tn): label(c, 540, 330, 'no client-side fetch', tn, INK, WHITE, 30)

def bottleneck(c):
    title(c, 'THE BOTTLENECK', 340, c.T('bottleneck'), 100, hlcol=YEL)
    x0, x1 = 100, 980
    rows = [('header data', 0.12, GRN), ('product data', 0.2, GRN), ('reviews query', 0.85, RED)]
    tq = c.T('slowest')
    for i, (n, w, col) in enumerate(rows):
        y = 500 + i * 110; at = tq + i * 0.2
        if not c.on(at): continue
        c.pen.text(x0, y - 30, n, 'int', 28, INK, 'lm')
        c.pen.rect(x0, y, x0 + (x1 - x0) * w * c.P(at, 0.6 * w / 0.3 + 0.1), y + 46, fill=col, outline=INK, w=3)
    tw = c.T('waits')
    if c.on(tw):
        marker(c, x0 + (x1 - x0) * 0.85, 920, 450, 'first byte', tw, RED)
        stamp(c.cv, 540, 1080, 'WHOLE PAGE WAITS', 70, c.P(tw, 0.4), -4, RED)

def thali(c):
    tt = c.T('thali')
    if c.on(tt):
        c.pen.text(540, 350, 'THE THALI', 'osw', 80, INK)
        c.pen.circ(540, 720, 300, fill=(220, 224, 230), outline=INK, w=6)
    dishes = [('rice', 540, 820, 120, WHITE, 'Rice'), ('dal', 380, 610, 80, (240, 200, 80), 'dal'),
              ('sabzi', 700, 610, 80, (120, 170, 80), 'rest'), ('paneer', 380, 830, 70, (240, 140, 80), 'rest'), ('raita', 700, 830, 70, (240, 240, 230), 'rest')]
    for k, (n, x, y, r, col, kw) in enumerate(dishes):
        at = c.T(kw) + (0.5 * (k - 2) if kw == 'rest' else 0)
        if not c.on(at): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.35)
        c.pen.circ(x, y, r * s, fill=col, outline=INK, w=4); c.pen.text(x, y, n, 'int', 26 * s, INK)
    tf = c.T('first')
    if c.on(tf): label(c, 540, 1100, 'eat what’s ready · the rest follows', tf, YEL, INK, 32)

CODE = ["import { renderToPipeableStream } from 'react-dom/server';", '', 'const stream = renderToPipeableStream(<App />, {',
        '  onShellReady() {', "    res.setHeader('Content-Type', 'text/html');", '    stream.pipe(res);', '  },', '});']

def how(c):
    tc = c.T('chunks')
    if c.on(tc):
        for k, (lab, col, kw) in enumerate([('shell + fallbacks', CYAN, 'shell'), ('reviews HTML', YEL, 'ready'), ('tiny script → swap in', PINK, 'script')]):
            at = c.T(kw); x = 100 + k * 300
            if c.on(at):
                c.sfx(at, 'pop')
                c.pen.rr(x, 380, x + 270, 470, 14, fill=col, outline=INK, w=4)
                c.pen.text(x + 135, 425, lab, 'int', 24, INK)
                if k: arrow(c.pen, x - 28, 425, x - 4, 425, 1, INK, 4, 12)
    code(c, 20, 540, 1060, 540 + 72 + 8 * 50 + 40, CODE, c.T('React'), 0.1, 25, 'server.js', marks=[(3, c.T('onShellReady'), YEL), (5, c.T('pipe'), YEL)])

def transport(c):
    tr = c.T('road')
    if c.on(tr): chapter(c, 540, 340, 'S1 · E05', 'the multi-lane road', tr)
    b = node(c, 220, 700, 260, 220, 'server', c.T('pieces'), 'server')
    br = node(c, 860, 700, 260, 220, 'browser', c.T('pieces'), 'laptop')
    tp = c.T('pieces')
    if c.on(tp):
        for k in range(4):
            t0 = tp + k * 0.7
            packet(c, b, br, t0, t0 + 0.9, [CYAN, YEL, YEL, PINK][k], ['<head>…', '<header>…', '<main>…', '<script>'][k])
    tc = c.T('Chunked')
    if c.on(tc): label(c, 540, 930, 'HTTP/1.1: Transfer-Encoding: chunked', tc, WHITE, INK, 28)
    td = c.T('frames')
    if c.on(td): label(c, 540, 1010, 'HTTP/2 & 3: DATA frames', td, WHITE, INK, 28)
    tpa = c.T('parsing')
    if c.on(tpa): label(c, 540, 1120, 'browser parses chunk 1 while the rest is in flight', tpa, GRN, WHITE, 28)

def proof(c):
    p = panel(c, 50, 330, 1030, 760, ('Headers', 'Timing'), 1, (1 - c.P(0, 0.45)) * 900)
    tt = c.T('Timing')
    rows = [('Waiting for server response', 0.12, GRN), ('Content Download', 0.75, BLUE)]
    for i, (n, w, col) in enumerate(rows):
        at = tt + i * 0.3; y = 500 + i * 110
        if not c.on(at): continue
        c.pen.text(100, y, n, 'int', 28, WHITE, 'lm')
        c.pen.rect(560, y - 20, 560 + 420 * w * c.P(at, 0.5), y + 20, fill=col)
    tl = c.T('long')
    if c.on(tl): c.pen.rr(80, 580, 1000, 640, 10, outline=YEL, w=4)
    tv = c.T('View')
    if c.on(tv):
        htmlcard(c, 50, 820, 1030, ['<div hidden id="S:0">', '  <section>…reviews…</section>', '</div>', '<script>$RC("B:0","S:0")</script>'], tv, 'view-source (bottom)', 28,
                 marks=[(0, c.T('hidden'), YEL), (3, c.T('template'), YEL)])

def gotcha(c):
    trap(c)
    qtext(c, 'Streaming started. Can you still send a 404 or a redirect?', 450, c.T('status'), 46)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 650, 'NO', 110, c.P(tn, 0.35), -6, RED)
    th = c.T('Headers')
    if c.on(th):
        seg_row(c, 100, 800, 980, [('200 + headers + shell', 0, 0.45, CYAN, th), ('more chunks…', 0.45, 0.9, YEL, th + 0.5)])
        label(c, 300, 920, 'status locked here', th + 0.3, RED, WHITE, 28)
    tb = c.T('before')
    if c.on(tb): label(c, 540, 1060, 'check it before the shell · or render an error in-page', tb, GRN, WHITE, 28)

SCENES = [
    (hook, "Some server rendered pages show the header instantly, then fill in the rest a moment later. Without a single fetch from the browser. How?"),
    (bottleneck, "Classic server rendering has a bottleneck. The server can't send a single byte until the slowest data is ready. One slow reviews query, and the whole page waits."),
    (thali, "Think of a thali. The restaurant doesn't wait for every dish. Rice and dal arrive first, and the rest come as they're cooked."),
    (how, "Streaming SSR sends HTML in chunks, over the same response. The shell goes first, with fallbacks for the slow parts. When the slow data is ready, the server sends that HTML, plus a tiny script that swaps it into place. In React, it's renderToPipeableStream, and onShellReady starts the pipe."),
    (transport, "Remember the multi-lane road from season one? An HTTP response can arrive in pieces. Chunked transfer in HTTP one point one, or data frames in HTTP two and three. The browser starts parsing the first chunk while the rest is still in flight."),
    (proof, "Click the document request and open Timing. With streaming, Content Download stays open for a long time, because chunks keep coming. View Source shows hidden divs near the bottom, and a script that moves them into place, like a template."),
    (gotcha, "Interview trap: once streaming starts, can you still change the status code, or redirect? No. Headers go out with the first chunk. So check for missing data before the shell, or render an error inside the page."),
    (scene_next('S2 · E14', 'SERVER COMPONENTS', 'components that never ship', 'server', 'never'),
     "Next: React Server Components. Components whose code never ships to the browser. Comment NOTES for the cheat sheet."),
]
