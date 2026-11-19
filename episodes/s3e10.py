from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E10', tag='S3 · E10', short='ASYNC vs DEFER', hook='two words that change load order')

def lanes(c, at, mode, y0=520):
    """three lanes: HTML parsing / script fetch / script run"""
    lab = [('HTML parsing', GRN), ('fetch', BLUE), ('execute', YEL)]
    for k, (nm, col) in enumerate(lab):
        c.pen.text(110, y0 + k * 150, nm, 'int', 30, INK, 'lm')
        c.pen.line([(110, y0 + k * 150 + 50), (970, y0 + k * 150 + 50)], GREY, 3)
    T = lambda f: at + f * 3.0
    def bar(row, a, b, col):
        if not c.on(T(a)): return
        p = lin(c.t, T(a), T(b)); xa = 110 + 860 * a; xb = xa + 860 * (b - a) * p
        y = y0 + row * 150 + 25
        c.pen.rect(xa, y, xb, y + 50, fill=col, outline=INK, w=3)
    if mode == 'plain':
        bar(0, 0, 0.25, GRN); bar(1, 0.25, 0.55, BLUE); bar(2, 0.55, 0.75, YEL); bar(0, 0.75, 1.0, GRN)
    elif mode == 'async':
        bar(0, 0, 0.45, GRN); bar(1, 0.15, 0.45, BLUE); bar(2, 0.45, 0.62, YEL); bar(0, 0.62, 1.0, GRN)
    else:
        bar(0, 0, 0.7, GRN); bar(1, 0.15, 0.45, BLUE); bar(2, 0.7, 0.88, YEL)
        if c.on(T(0.88)): c.pen.line([(110 + 860 * 0.9, y0 - 30), (110 + 860 * 0.9, y0 + 360)], RED, 4); c.pen.text(110 + 860 * 0.9, y0 + 400, 'DOMContentLoaded', 'int', 24, RED)

def hook(c):
    code(c, 70, 400, 1010, 640, ['<script async src="a.js"></script>', '<script defer src="b.js"></script>'], max(0.05, c.T('Two') - 0.3), 0.2, 30, 'index.html', lang='html',
         circles=[(0, c.T('async'), 'async'), (1, c.T('defer'), 'defer')])
    tb = c.T('break')
    if c.on(tb): stamp(c.cv, 300, 820, 'APP BREAKS', 58, c.P(tb, 0.35), -6, RED); c.sfx(tb, 'thud')
    tf = c.T('faster')
    if c.on(tf): stamp(c.cv, 780, 960, '1 s FASTER', 58, c.P(tf, 0.35), 5, GRN); c.sfx(tf, 'thud')

def plain(c):
    title(c, '<script>', 330, c.T('plain'), 100, k='monob')
    lanes(c, c.T('stops'), 'plain')
    tw = c.T('waits')
    if c.on(tw): label(c, 540, 1080, 'parsing waits for download + run', tw, (255, 225, 225), INK, 32)

def async_(c):
    title(c, '<script async>', 330, c.T('Async'), 84, k='monob', hlcol=(200, 220, 255))
    lanes(c, c.T('parallel'), 'async')
    tm = c.T('moment')
    if c.on(tm): label(c, 540, 1080, 'runs the moment it arrives', tm, (200, 220, 255), INK, 32)
    to = c.T('order')
    if c.on(to): txt(c, 540, 1180, 'order = whoever finishes first', to, 'intx', 36, RED)

def defer(c):
    title(c, '<script defer>', 330, c.T('Defer'), 84, k='monob', hlcol=(200, 240, 200))
    lanes(c, c.T('parallel'), 'defer')
    to = c.T('order')
    if c.on(to): label(c, 540, 1080, 'after parsing · in document order', to, (200, 240, 200), INK, 32)

def wedding(c):
    title(c, 'THE WEDDING', 330, 0.1, 100)
    for j, (nm, kw, col, desc) in enumerate((('ASYNC GUESTS', 'Async', BLUE, 'grab the mic on arrival'), ('DEFER GUESTS', 'Defer', GRN, 'speak after the vows, in order'))):
        t = c.T(kw); y = 560 + j * 380
        if not c.on(t): continue
        s = c.B(t, 0.4); c.sfx(t, 'pop')
        card(c.pen, 110, y - 150 * s, 970, y + 150 * s, 26, WHITE, 10, 5)
        c.pen.text(150, y - 95, nm, 'osw', 50 * s, col, 'lm')
        c.pen.text(150, y - 35, desc, 'ints', 32 * s, INK, 'lm')
        for k in range(4):
            x = 200 + k * 150
            person(c.pen, x, y + 135, 0.6, col if (j == 1 or k != 2) else RED)
            if j == 1 and c.on(c.T('program')): c.pen.text(x, y + 15, str(k + 1), 'osw', 36, INK)
        if j == 0 and c.on(c.T('ceremony')):
            c.pen.rr(560, y - 10, 700, y + 50, 10, fill=RED); c.pen.text(630, y + 20, 'MIC!', 'osw', 32, WHITE)

def when(c):
    title(c, 'WHICH ONE?', 330, 0.1, 100)
    versus(c, ('DEFER', GRN, c.T('defer'), [('DOM', 'your app code'), ('order', 'needs the DOM + order')]),
           ('ASYNC', BLUE, c.T('async'), [('analytics', 'analytics, ads, widgets'), ('either', 'independent of everything')]), 440, 940)
    tm = c.T('module')
    if c.on(tm): label(c, 540, 1060, '<script type="module"> = deferred by default', tm, YEL, INK, 32)

def proof(c):
    box = browser(c, 70, 330, 1010, 900, url='view-source:shop.example.com', dy=(1 - c.P(0, 0.45)) * 900)
    lines = ['<script defer src=".../vendors.js"></script>', '<script defer src=".../behaviors.js"></script>', '<script type="module" src=".../app.js"></script>']
    tv = c.T('View')
    for k, ln in enumerate(lines):
        if c.on(tv + k * 0.2): c.pen.text(110, 470 + k * 70, ln, 'mono', 24, INK, 'lm')
    ts = c.T('search')
    if c.on(ts):
        for k in range(2): hl(c.pen, 222, 452 + k * 70, 300, 490 + k * 70, c.P(ts + k * 0.2, 0.3))
        for k, ln in enumerate(lines[:2]): c.pen.text(110, 470 + k * 70, ln, 'mono', 24, INK, 'lm')
    tp = c.T('Performance')
    if c.on(tp):
        panel(c, 70, 960, 1010, 1300, tabs=('Performance',))
        c.pen.rect(110, 1110, 700, 1160, fill=GRN); c.pen.text(120, 1135, 'Parse HTML', 'int', 24, INK, 'lm')
        c.pen.rect(710, 1110, 900, 1160, fill=YEL); c.pen.text(720, 1135, 'Evaluate script', 'int', 22, INK, 'lm')

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 60, 450, 1020, 690, ['<script async src="lib.js"></script>', '<script async src="uses-lib.js"></script>'], c.T('two') - 0.3, 0.2, 28, 'index.html', lang='html')
    tw = c.T('machine')
    if c.on(tw):
        pill(c.pen, 300, 790, 'your laptop: works', c.B(tw, 0.35), (200, 240, 200), INK, 30)
    tp = c.T('production')
    if c.on(tp):
        pill(c.pen, 760, 790, 'production: breaks', c.B(tp, 0.35), (255, 210, 210), INK, 30)
        console(c, 60, 860, 1020, 1060, [(tp + 0.3, 'ReferenceError: lib is not defined', RED)])
    to = c.T('first', 2)
    if c.on(to): label(c, 540, 1160, 'async has no order · use defer', to, YEL, INK, 34)
    ti = c.T('inline')
    if c.on(ti): txt(c, 540, 1250, 'and defer does nothing on inline scripts', ti, 'ints', 30, MUTE)

SCENES = [
    (hook, "Two script tags. One says async. The other says defer. Mix them up, and your app can break. Get them right, and your page can load a second faster."),
    (plain, "A plain script tag stops the HTML parser. The browser downloads the script, runs it, and parsing waits the whole time."),
    (async_, "Async downloads the script in parallel, without stopping the parser. But the moment it arrives, it runs, interrupting parsing, in whatever order the files happen to finish."),
    (defer, "Defer also downloads in parallel. But it waits until the HTML is fully parsed, then runs every deferred script in document order, just before DOMContentLoaded."),
    (wedding, "Think of a wedding. Async guests grab the mic the moment they walk in, even mid ceremony. Defer guests wait until the vows are done, then speak in the order printed on the program."),
    (when, "So use defer for your app code, which needs the DOM, and needs order. Use async for independent scripts like analytics, that don't care about either. And scripts with type module are deferred by default."),
    (proof, "View Source on almost any big site, and search for defer. Then in the Performance panel, deferred scripts only evaluate after parsing ends."),
    (gotcha, "Interview trap: two async scripts, and the second uses a library from the first. It works on your machine, and breaks in production. Async has no order: whichever arrives first runs first. And remember, defer does nothing on inline scripts."),
    (scene_next('S3 · E11', 'RESOURCE HINTS', 'tell the browser what is coming', 'resource', 'coming'),
     "Next: resource hints, telling the browser what's coming before it asks. Comment NOTES for the cheat sheet."),
]
