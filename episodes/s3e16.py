from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E16', tag='S3 · E16', short='MINIFY + BROTLI')

def hook(c):
    tl = c.T('laptop')
    if c.on(tl):
        node(c, 280, 560, 360, 220, 'your laptop', tl, 'laptop', sub='app.js · 400 KB')
    tu = c.T('downloads')
    if c.on(tu):
        node(c, 800, 560, 360, 220, "user's browser", tu, 'phone', sub='transferred · ~60 KB')
        arrow(c.pen, 470, 560, 610, 560, c.P(tu, 0.3), INK, 7)
    ts = c.T('Same')
    if c.on(ts): title(c, 'SAME FILE', 820, ts, 110, RED)
    tt = c.T('tricks')
    if c.on(tt):
        pill(c.pen, 360, 1000, '1 · minify', c.B(tt, 0.35), YEL, INK, 40); pill(c.pen, 720, 1000, '2 · compress', c.B(tt + 0.2, 0.35), YEL, INK, 40)

def minify(c):
    title(c, 'MINIFICATION', 330, c.T('minification'), 110, hlcol=YEL)
    code(c, 50, 440, 1030, 780, ['// add up the prices in the cart', 'function calculateTotal(cartItems) {', '  let runningTotal = 0;',
                                 '  for (const item of cartItems) runningTotal += item.price;', '  return runningTotal;', '}'], c.T('strips') - 0.5, 0.1, 23, 'cart.js',
         marks=[(0, c.T('comments'), (120, 60, 60))])
    tr = c.T('renames')
    code(c, 50, 830, 1030, 990, ['function c(t){let n=0;for(const o of t)n+=o.price;return n}'], tr, 0.1, 23, 'cart.min.js', marks=[(0, c.T('same'), (60, 110, 70))])
    ts = c.T('same')
    if c.on(ts): label(c, 540, 1080, 'runs exactly the same', ts, (200, 240, 200), INK, 34)

def compress(c):
    title(c, 'COMPRESSION', 330, c.T('compression'), 110, hlcol=YEL)
    a = node(c, 220, 560, 280, 170, 'server', c.T('server'), 'server')
    b = node(c, 860, 560, 280, 170, 'browser', c.T('unpacks'), 'laptop')
    tq = c.T('squeezes')
    if c.on(tq): packet(c, a, b, tq, tq + 1.4, YEL, 'app.js.br')
    bars(c, 90, 760, [('original', 400, GREY, c.T('Gzip') - 0.4), ('gzip', 80, BLUE, c.T('Gzip')), ('brotli', 66, GRN, c.T('Brotli'))], 400, 560, 80, 120, '{} KB', 200, 32)
    tf = c.T('fifteen')
    if c.on(tf): label(c, 540, 1180, 'brotli ≈ 15–20% smaller than gzip on text', tf, YEL, INK, 30)

def duvet(c):
    title(c, 'VACUUM-PACKED', 330, c.T('vacuum'), 110)
    q = c.P(c.T('fraction'), 0.8) if c.on(c.T('fraction')) else 0
    fl = c.P(c.T('fluffs'), 0.6) if c.on(c.T('fluffs')) else 0
    sz = 1 - 0.6 * q + 0.6 * fl
    w, h = 420 * sz, 300 * sz; cy = 720 + 360 * q * (1 - fl)
    card(c.pen, 540 - w / 2, cy - h / 2, 540 + w / 2, cy + h / 2, 40 * sz, (230, 235, 255), 10, 5)
    for k in range(3): c.pen.line([(540 - w / 2 + 30, cy - h / 2 + (k + 1) * h / 4), (540 + w / 2 - 30, cy - h / 2 + (k + 1) * h / 4)], (180, 190, 230), 4)
    tb = c.T('box')
    if c.on(tb): c.pen.rect(270, 980, 810, 1180, outline=(150, 110, 70), w=8); c.pen.text(540, 1220, 'moving box', 'ints', 28, MUTE)

def headers(c):
    title(c, 'WHO PICKS?', 330, 0.1, 110)
    panel(c, 50, 430, 1030, 700, tabs=('Request headers',))
    kv(c, 100, 590, 1000, [(c.T('Accept'), 'accept-encoding:', 'gzip, deflate, br, zstd', YEL)], 30)
    panel(c, 50, 760, 1030, 1030, tabs=('Response headers',))
    kv(c, 100, 920, 1000, [(c.T('Content'), 'content-encoding:', 'br', GRN)], 30)
    tb = c.T('best')
    if c.on(tb): txt(c, 540, 1120, 'server picks the best one both sides support', tb, 'ints', 32, INK)

def proof(c):
    panel(c, 50, 330, 1030, 1200, tabs=('Network', 'Headers'), dy=(1 - c.P(0, 0.45)) * 900)
    tc = c.T('encoding')
    if c.on(tc): kv(c, 100, 490, 1000, [(tc, 'content-encoding:', 'br', GRN)], 32)
    tb = c.T('big')
    if c.on(tb):
        c.pen.text(100, 640, 'Name', 'int', 26, (150, 156, 166), 'lm'); c.pen.text(760, 640, 'Size', 'int', 26, (150, 156, 166), 'lm')
        for k, (nm, a, b) in enumerate((('app.js', '61.2 kB', '402 kB'), ('styles.css', '18.4 kB', '121 kB'), ('index.html', '9.1 kB', '44 kB'))):
            y = 720 + k * 110
            c.pen.text(100, y, nm, 'mono', 30, WHITE, 'lm')
            c.pen.text(760, y - 18, a, 'monob', 28, WHITE, 'lm')
            if c.on(c.T('real')): c.pen.text(760, y + 22, b, 'mono', 26, (150, 156, 166), 'lm')
    tr = c.T('real')
    if c.on(tr): txt(c, 540, 1100, 'top: transferred  ·  bottom: real size', tr, 'ints', 30, YEL)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    title(c, 'COMPRESS EVERYTHING?', 480, c.T('everything'), 84)
    ta = c.T('already')
    for k, nm in enumerate(('.jpg', '.png', '.mp4', '.woff2')):
        if c.on(ta + k * 0.15): pill(c.pen, 210 + k * 220, 620, nm, c.B(ta + k * 0.15, 0.3), (255, 210, 210), INK, 36)
    tw = c.T('wastes')
    if c.on(tw): txt(c, 540, 720, 'already compressed → wasted CPU, ~0% saved', tw, 'ints', 32, RED)
    tt = c.T('text')
    for k, nm in enumerate(('HTML', 'CSS', 'JS', 'JSON', 'SVG')):
        if c.on(tt + k * 0.15): pill(c.pen, 170 + k * 185, 880, nm, c.B(tt + k * 0.15, 0.3), (200, 240, 200), INK, 36)
    if c.on(tt): txt(c, 540, 980, 'compress text', tt, 'intx', 44, GRN)

SCENES = [
    (hook, "Your JavaScript file is four hundred kilobytes on your laptop. The user's browser downloads about sixty. Same file. Two tricks made the difference."),
    (minify, "First, minification. A build tool strips whitespace and comments, and renames long local variables to single letters. The code runs exactly the same."),
    (compress, "Second, compression. The server squeezes the file before sending it, and the browser unpacks it. Gzip is the classic. Brotli usually saves another fifteen to twenty percent on text."),
    (duvet, "It's like vacuum packing a duvet before a move. Same duvet, a fraction of the space in the box, and it fluffs right back up when you open it."),
    (headers, "Who picks the format? The browser lists what it understands in the Accept Encoding header. The server picks the best one, and says so in Content Encoding."),
    (proof, "Check it in the Network panel. Click a JavaScript file, and look for content encoding in the response headers. Then turn on big request rows, and you'll see two sizes: transferred, and the real size."),
    (gotcha, "Interview trap: compress everything, including images. JPEGs, PNGs and videos are already compressed. Gzipping them wastes server CPU, and saves almost nothing. Compress text: HTML, CSS, JavaScript, JSON and SVG."),
    (scene_next('S3 · E17', 'IQ: LOADING', 'four questions on bundles + loading', 'questions', 'loading'),
     "Next: four interview questions on loading and bundles. Comment NOTES for the cheat sheet."),
]
