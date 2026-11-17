from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E15', tag='S3 · E15', short='BUNDLE DIET')

def hook(c):
    tb = c.T('two')
    if c.on(tb):
        card(c.pen, 160, 380, 920, 600, 26, (255, 225, 190), 12, 5)
        c.pen.text(540, 460, 'bundle.js', 'monob', 44, INK); bignum(c, 540, 540, '2.0 MB', tb, 80, RED)
    tp = c.T('phone')
    if c.on(tp):
        icon(c.pen, 'phone', 260, 860, 2.0 * c.B(tp, 0.4))
        counter(c, 680, 860, 0, 3.4, c.T('parsing'), c.T('parsing') + 1.5, '{:.1f}', 100, RED, ' s')
        txt(c, 680, 960, 'parse + compile + run', c.T('parsing'), 'ints', 32, INK)
    tt = c.T('tap')
    if c.on(tt): stamp(c.cv, 540, 1160, 'NO TAPS UNTIL THEN', 62, c.P(tt, 0.35), -3, RED); c.sfx(tt, 'thud')

def cost(c):
    title(c, '100 KB ≠ 100 KB', 330, c.T('catch'), 110, hlcol=YEL)
    for j, (nm, kw, steps, col) in enumerate((('image', 'image', ['download', 'decode'], (120, 170, 210)),
                                               ('JavaScript', 'JavaScript', ['download', 'parse', 'compile', 'execute'], YEL))):
        t = c.T(kw, 2); y = 560 + j * 330
        if not c.on(t): continue
        c.pen.text(110, y - 70, f'100 KB of {nm}', 'intx', 38, INK, 'lm')
        x = 110
        for k, st in enumerate(steps):
            tk = t + 0.3 + k * 0.3
            if not c.on(tk): continue
            w = 190 if j else (200 if k == 0 else 120)
            c.pen.rect(x, y - 30, x + w * c.P(tk, 0.3), y + 50, fill=col if k else (200, 200, 205), outline=INK, w=3)
            c.pen.text(x + w / 2, y + 10, st, 'int', 26, INK)
            x += w + 10
    tm = c.T('main')
    if c.on(tm): label(c, 540, 1180, 'all on the main thread', tm, (255, 210, 210), INK, 34)

def trek(c):
    title(c, 'UPHILL WITH A BACKPACK', 330, 0.1, 80)
    tu = c.T('uphill')
    c.pen.poly([(90, 1150), (990, 520), (990, 1150)], fill=(200, 190, 170), outline=INK, w=4)
    q = c.P(tu, 3.0, lambda x: x) if c.on(tu) else 0
    x = 200 + 600 * q; y = 1150 - (x - 90) * 630 / 900
    person(c.pen, x, y + 10, 1.1, BLUE)
    c.pen.rr(x - 70, y - 120, x - 20, y - 40, 10, fill=ORANGE, outline=INK, w=4)
    tp = c.T('phones')
    if c.on(tp): label(c, 540, 1250, 'phones are always on the steep part', tp, YEL, INK, 34)

def measure(c):
    title(c, 'MEASURE FIRST', 330, c.T('measuring'), 100)
    ta = c.T('analyzer')
    boxes = [(110, 450, 620, 900, 'moment + locales', RED), (630, 450, 970, 700, 'chart.js', ORANGE), (630, 710, 970, 900, 'lodash', ORANGE),
             (110, 910, 400, 1120, 'react-dom', BLUE), (410, 910, 650, 1120, 'app code', GRN), (660, 910, 820, 1120, 'axios', PURPLE), (830, 910, 970, 1120, '…', GREY)]
    for k, (x0, y0, x1, y1, nm, col) in enumerate(boxes):
        t = ta + k * 0.12
        if not c.on(t): continue
        s = c.P(t, 0.3)
        c.pen.rect(x0, y0, x0 + (x1 - x0) * s, y1, fill=col, outline=INK, w=4)
        c.pen.text((x0 + x1) / 2, (y0 + y1) / 2, nm, 'intx', 30 if (x1 - x0) > 200 else 24, WHITE)
    tb = c.T('biggest')
    if c.on(tb): c.pen.rect(100, 440, 630, 910, outline=YEL, w=10)

def swaps(c):
    title(c, 'THE DIET', 330, c.T('diet'), 110, hlcol=YEL)
    rows(c, 90, 520, [('moment', 'moment → date-fns or Intl', '~70 KB → a few KB', 'ok'), ('polyfills', "drop polyfills you don't need", 'modern browsers have them', 'ok'),
                      ('duplicate', 'dedupe package versions', 'two copies of the same library', 'ok')], 190, 900, 150, 40, 30)

def check_(c):
    title(c, 'BEFORE YOU npm install', 330, c.T('Before'), 80)
    tb = c.T('bundlephobia')
    if c.on(tb): label(c, 540, 470, 'check its cost: bundlephobia.com', tb, WHITE, INK, 34)
    tp = c.T('platform')
    if c.on(tp): txt(c, 540, 580, 'can the platform do it already?', tp, 'intx', 42, INK)
    for k, (a, b, kw) in enumerate((('axios', 'fetch()', 'fetch'), ('modal library', '<dialog>', 'dialog'))):
        t = c.T(kw); y = 740 + k * 190
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        pill(c.pen, 300, y, a, s, (255, 210, 210), INK, 38); arrow(c.pen, 470, y, 600, y, c.P(t, 0.3), INK, 6)
        pill(c.pen, 780, y, b, s, (200, 240, 200), INK, 38)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    ty = c.T('yellow')
    if c.on(ty):
        blocks = [(0.0, 0.08, 0, 'Compile'), (0.09, 0.45, 0, 'JS', True), (0.55, 0.06, 0, 'Layout'), (0.62, 0.2, 0, 'JS', True), (0.83, 0.05, 0, 'Paint')]
        flame(c, 90, 520, 990, blocks, ty, 80)
        txt(c, 540, 700, 'Evaluate script · Compile code', ty + 0.5, 'mono', 30, YEL)
    tp = c.T('paid')
    if c.on(tp): txt(c, 540, 900, 'your bundle, being paid for', tp, 'intx', 40, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, '"200 KB gzipped." Is that the real cost?', c.T('gzipped'), 'intx', 42, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 600, tn, 110, RED)
    tu = c.T('uncompressed')
    if c.on(tu):
        bars(c, 90, 720, [('network', 200, BLUE, tu), ('parsed', 700, RED, tu + 0.5)], 700, 560, 80, 130, '{} KB', 200, 32)
    tc = c.T('CPU')
    if c.on(tc): label(c, 540, 1080, 'compression saves the network, not the CPU', tc, YEL, INK, 32)

SCENES = [
    (hook, "Your JavaScript bundle is two megabytes. On a mid range phone, parsing and running it can take seconds, and until it's done, the page can't respond to a single tap."),
    (cost, "Here's the catch: a hundred kilobytes of JavaScript costs far more than a hundred kilobytes of image. An image just downloads and decodes. JavaScript has to be downloaded, parsed, compiled and executed, all on the main thread."),
    (trek, "It's like trekking uphill with a backpack. Every gram counts more on the steep part, and cheap phones are always on the steep part."),
    (measure, "So start by measuring. A bundle analyzer shows every package as a box, sized by its weight. The biggest boxes are where you start."),
    (swaps, "Then the diet. Swap heavy libraries for lighter ones, like moment for date fns, or the built in Intl API. Drop polyfills that modern browsers don't need. And remove duplicate versions of the same package."),
    (check_, "Before adding a dependency, check its cost on bundlephobia, and ask: can the platform do this already? Use fetch instead of axios. A native dialog instead of a modal library."),
    (proof, "In DevTools, the Performance panel shows the bill: long yellow blocks of script compile and evaluation on load. That's your bundle being paid for."),
    (gotcha, "Interview question: our bundle is two hundred kilobytes gzipped. Is that the real cost? No. The browser parses the uncompressed size, maybe seven hundred kilobytes. Compression saves the network, not the CPU."),
    (scene_next('S3 · E16', 'MINIFY + BROTLI', 'same code, a fraction of the bytes', 'minification', 'fraction'),
     "Next: minification and Brotli, the same code in a fraction of the bytes. Comment NOTES for the cheat sheet."),
]
