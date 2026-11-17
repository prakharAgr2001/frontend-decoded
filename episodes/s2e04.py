from engine.s2_extra import *

EP = dict(id='S2E04', tag='S2 · E04', short='SERVER-SIDE RENDERING')

def hook(c):
    tv = c.T('View')
    htmlcard(c, 40, 330, 1040, ['<span id="productTitle">', '  Wireless Headphones…', '</span>', '<span class="a-price-whole">',
                                 '  2,499', '</span>', '<img src="…/I/71abc.jpg">'], tv, 'view-source:amazon.in', 30,
             marks=[(1, c.T('right', 2), YEL), (4, c.T('Prices'), YEL)])
    tb = c.T('Before')
    if c.on(tb): stamp(c.cv, 540, 1150, 'BEFORE ANY JS', 84, c.P(tb, 0.4), -4, RED)

def define(c):
    title(c, 'SERVER-SIDE RENDERING', 340, c.T('server'), 84, hlcol=YEL)
    txt(c, 540, 420, 'SSR = full HTML built on every request', c.T('server') + 0.4, 'ints', 34, MUTE)
    u = node(c, 170, 700, 200, 180, 'request', c.T('every'), 'laptop', size=30)
    s = node(c, 540, 700, 260, 220, 'server', c.T('runs'), 'server')
    d = node(c, 540, 1000, 220, 140, 'database', c.T('fetches'), 'db', size=28)
    link(c, s, d, c.T('fetches'), dash=True)
    tf = c.T('full')
    if c.on(tf): link(c, u, s, c.T('every'))
    b = node(c, 910, 700, 200, 180, 'browser', c.T('receives'), 'laptop', size=30)
    if c.on(c.T('receives')): packet(c, s, b, c.T('receives'), c.T('receives') + 0.9, YEL, 'full HTML')
    tp = c.T('paints')
    if c.on(tp): label(c, 910, 880, 'paints immediately', tp, GRN, WHITE, 26)

def cup(pen, cx, cy, s=1.0, fill=(205, 150, 95)):
    pen.poly([(cx - 70 * s, cy - 80 * s), (cx + 70 * s, cy - 80 * s), (cx + 50 * s, cy + 80 * s), (cx - 50 * s, cy + 80 * s)], WHITE, INK, 5)
    pen.poly([(cx - 64 * s, cy - 56 * s), (cx + 64 * s, cy - 56 * s), (cx + 50 * s, cy + 70 * s), (cx - 50 * s, cy + 70 * s)], fill)
    for k in range(3):
        x = cx - 30 * s + k * 30 * s
        pen.arc(x - 12 * s, cy - 150 * s, x + 12 * s, cy - 100 * s, 90, 270, MUTE, 4)

def analogy(c):
    tc = c.T('chai')
    if c.on(tc):
        card(c.pen, 120, 360, 960, 820, 26, WHITE, 12, 5)
        c.pen.text(540, 430, 'THE CHAI STALL', 'osw', 60, INK)
        cup(c.pen, 540, 640, 1.2 * c.B(tc, 0.4))
    tf = c.T('fresh')
    if c.on(tf): label(c, 540, 900, 'fresh for every customer', tf, GRN, WHITE, 32)
    tw = c.T('wait')
    if c.on(tw): label(c, 540, 990, 'but you wait while it’s made', tw, ORANGE, WHITE, 32)
    tr = c.T('crowd')
    if c.on(tr):
        for k in range(7):
            at = tr + k * 0.08
            if c.on(at): person(c.pen, 200 + k * 115, 1250, 0.9 * c.B(at, 0.3), [BLUE, RED, GRN, PURPLE, ORANGE, TEAL, PINK][k])

CODE = ["app.get('/product/:id', async (req, res) => {", '  const p = await db.product(req.params.id);', '  res.send(`<html><body>',
        '    <h1>${p.name}</h1>', '    <p>Rs ${p.price}</p>', '    <script src="/app.js"></script>', '  </body></html>`);', '});']

def how(c):
    code(c, 30, 340, 1050, 340 + 72 + 8 * 54 + 40, CODE, c.T('Express'), 0.12, 28, 'server.js',
         marks=[(1, c.T('database'), YEL), (3, c.T('HTML'), YEL), (4, c.T('HTML'), YEL), (5, c.T('script'), YEL)])
    ts = c.T('script')
    if c.on(ts): txt(c, 540, 1000, 'JS still loads — to make it interactive', ts, 'ints', 34, INK)

def tradeoff(c):
    tp = c.T('parcel')
    if c.on(tp): chapter(c, 540, 340, 'S1 · E01', 'the parcel journey', tp)
    x0, x1 = 100, 980
    txt(c, x0, 480, 'Static file', c.T('Time'), 'intx', 38, INK, 'lm')
    seg_row(c, x0, 520, x1, [('wait', 0, 0.12, GREY, c.T('Time')), ('HTML', 0.12, 0.25, CYAN, c.T('Time') + 0.3), ('JS → paint', 0.25, 0.8, YEL, c.T('Time') + 0.6)])
    marker(c, x0 + (x1 - x0) * 0.8, 640, 510, 'FIRST PAINT', c.T('Time') + 0.9, RED)
    txt(c, x0, 830, 'SSR', c.T('grows'), 'intx', 38, BLUE, 'lm')
    seg_row(c, x0, 870, x1, [('server cooking', 0, 0.32, ORANGE, c.T('grows')), ('HTML', 0.32, 0.48, CYAN, c.T('paint'))])
    marker(c, x0 + (x1 - x0) * 0.32, 990, 860, 'TTFB ↑', c.T('grows'), ORANGE)
    marker(c, x0 + (x1 - x0) * 0.48, 1080, 860, 'FIRST PAINT', c.T('sooner'), GRN)

def proof(c):
    p = panel(c, 60, 330, 1020, 1150, ('Headers', 'Preview', 'Timing'), 2, (1 - c.P(0, 0.45)) * 900)
    rows = [('Queueing', 0.02, GREY), ('Initial connection', 0.12, ORANGE), ('Request sent', 0.02, GREY),
            ('Waiting for server response', 0.5, GRN), ('Content Download', 0.1, BLUE)]
    tt = c.T('Timing')
    for i, (n, w, col) in enumerate(rows):
        at = tt + i * 0.2; y = 500 + i * 100
        if not c.on(at): continue
        c.pen.text(110, y, n, 'int', 28, WHITE, 'lm')
        c.pen.rect(600, y - 18, 600 + 380 * w * c.P(at, 0.4) / 0.5, y + 18, fill=col)
    tw = c.T('Waiting')
    if c.on(tw):
        c.pen.rr(90, 770, 990, 830, 12, outline=YEL, w=4)
        label(c, 540, 1050, '= your server’s render time', c.T('render'), YEL, INK, 32)

def gotcha(c):
    trap(c)
    qtext(c, 'Is SSR always faster?', 460, c.T('always'), 60)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 600, 'NO', 110, c.P(tn, 0.35), -6, RED)
    items = [(False, 'slow database → huge TTFB', c.T('database')), (False, 'far-away server → huge TTFB', c.T('far')),
             (False, 'still not interactive until JS loads', c.T('interactive'))]
    proscons(c, 110, 760, 980, items, 36, 100)
    tm = c.T('moves')
    if c.on(tm): label(c, 540, 1150, 'SSR moves work. It doesn’t delete it.', tm, INK, WHITE, 34)

SCENES = [
    (hook, "Open Amazon, right click, and View Page Source. Search for a product name you can see on screen. It's right there in the HTML. Prices, titles, images. Before any JavaScript runs."),
    (define, "That's server side rendering. On every request, the server runs your code, fetches the data, and builds the full HTML. The browser receives a finished page, and paints it immediately."),
    (analogy, "It's like a chai stall. You order, the chaiwala makes it fresh, and hands you a cup that's ready to drink. Fresh for every customer. But you wait while it's made, and the stall gets slow when a crowd arrives."),
    (how, "Here it is in Express. Read from the database, put the values straight into the HTML, and send it. A script tag still loads JavaScript afterwards, to make the page interactive."),
    (tradeoff, "Remember the parcel journey from season one? Server rendering adds work before the first byte. Time To First Byte grows, because the server is cooking. But the first paint comes much sooner."),
    (proof, "In DevTools, click the document request and open Timing. Waiting for server response is mostly your server's render time."),
    (gotcha, "Interview trap: is SSR always faster? No. A slow database, or a server far from the user, makes Time To First Byte huge. And the page still isn't interactive until the JavaScript loads. SSR moves work. It doesn't delete it."),
    (scene_next('S2 · E05', 'STATIC SITE GENERATION', 'cook once, serve a million times', 'static', 'million'),
     "Next: static site generation. Cook it once, serve it a million times. Comment NOTES for the cheat sheet."),
]
