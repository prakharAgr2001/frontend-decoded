from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E25', tag='S3 · E25', short='VIRTUALIZATION')

def hook(c):
    tt = c.T('ten')
    if c.on(tt): counter(c, 540, 420, 0, 10000, tt, tt + 0.8, '{:,.0f}', 110, INK, ' rows')
    tn = c.T('nodes')
    if c.on(tn):
        for k in range(120):
            t = tn + k * 0.01
            if c.on(t): c.pen.rect(110 + (k % 20) * 43, 560 + (k // 20) * 50, 145 + (k % 20) * 43, 600 + (k // 20) * 50, fill=(255, 210, 210), outline=INK, w=2)
        txt(c, 540, 900, '100,000+ DOM nodes', tn, 'intx', 48, RED)
    ts = c.T('stutters')
    if c.on(ts): stamp(c.cv, 540, 1080, 'SCROLL STUTTERS', 70, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')

def define(c):
    title(c, 'VIRTUALIZATION', 330, c.T('Virtualization'), 100, hlcol=YEL)
    ts = c.T('see')
    off = ((c.t - c.T('scroll')) * 120) if c.on(c.T('scroll')) else 0
    for k in range(12):
        y = 470 + k * 60 - (off % 60)
        inview = 650 <= y <= 950
        buffer = 590 <= y < 650 or 950 < y <= 1010
        if not c.on(ts):
            col = WHITE
        else:
            col = (200, 240, 200) if inview else ((255, 238, 170) if buffer else None)
        if col is None:
            c.pen.rect(240, y, 840, y + 50, outline=GREY, w=2)
        else:
            c.pen.rect(240, y, 840, y + 50, fill=col, outline=INK, w=3)
        c.pen.text(270, y + 25, f'row {k + int(off // 60) + 1}', 'mono', 24, INK if col else GREY, 'lm')
    if c.on(ts):
        c.pen.rect(220, 640, 860, 1010, outline=BLUE, w=6); c.pen.text(880, 820, 'viewport', 'intx', 28, BLUE, 'lm')
    tr = c.T('reused')
    if c.on(tr): label(c, 540, 1300, 'rows leaving the screen are reused', tr, YEL, INK, 30)

def window_(c):
    title(c, 'THE TRAIN WINDOW', 330, 0.1, 100)
    tl = c.T('landscape')
    off = (c.t * 200) % 300
    for k in range(8):
        x = 100 + k * 300 - off
        c.pen.poly([(x, 900), (x + 150, 650), (x + 300, 900)], fill=(120, 170, 120), outline=INK, w=3)
    c.pen.rect(0, 900, 1080, 960, fill=(140, 110, 80))
    WALL = (120, 45, 55)
    c.pen.rect(0, 440, 340, 1010, fill=WALL); c.pen.rect(740, 440, 1080, 1010, fill=WALL)
    c.pen.rect(340, 440, 740, 560, fill=WALL); c.pen.rect(340, 960, 740, 1010, fill=WALL)
    c.pen.line([(0, 440), (1080, 440)], INK, 6); c.pen.line([(0, 1010), (1080, 1010)], INK, 6)
    c.pen.rect(340, 560, 740, 960, outline=INK, w=10)
    tw = c.T('glass')
    if c.on(tw): label(c, 540, 1100, 'only render what passes the glass', tw, YEL, INK, 34)

def how(c):
    title(c, 'UNDER THE HOOD', 330, 0.1, 100)
    code(c, 30, 450, 1050, 820, ['const start = Math.floor(scrollTop / ROW_HEIGHT);', 'const end = start + Math.ceil(viewport / ROW_HEIGHT) + OVERSCAN;',
                                 'const visible = rows.slice(start, end);', '// spacer height = rows.length * ROW_HEIGHT'],
         c.T('spacer') - 0.5, 0.15, 22, 'virtual.js', marks=[(3, c.T('spacer'), YEL), (0, c.T('compute'), YEL), (2, c.T('position'), (60, 110, 70))])
    tp = c.T('scrollbar')
    if c.on(tp):
        c.pen.rect(900, 900, 940, 1250, fill=LIGHT, outline=INK, w=3); c.pen.rr(903, 920, 937, 980, 10, fill=INK)
        c.pen.text(860, 1080, 'spacer: 10,000 × 48 px', 'ints', 28, INK, 'rm')
        c.pen.text(860, 1130, 'only ~20 real rows inside', 'ints', 28, GRN, 'rm')

def libs(c):
    title(c, 'USE A LIBRARY', 330, c.T('library'), 110, hlcol=YEL)
    for k, (nm, kw) in enumerate((('TanStack Virtual', 'TanStack'), ('react-window', 'react'))):
        node(c, 540, 540 + k * 200, 700, 150, nm, c.T(kw), size=44)
    chips(c, 140, 1000, [('variable heights', WHITE), ('overscan', WHITE), ('scroll restoration', WHITE)], c.T('variable'), 0.3, 30)

def cv(c):
    title(c, 'THE CSS SHORTCUT', 330, c.T('shortcut'), 100)
    code(c, 60, 450, 1020, 800, ['.section {', '  content-visibility: auto;', '  contain-intrinsic-size: auto 500px;', '}'], c.T('content') - 0.4, 0.12, 30, 'feed.css',
         lang='css', marks=[(1, c.T('content'), YEL)])
    ts = c.T('skips')
    if c.on(ts):
        for k in range(4):
            y = 850 + k * 105; on = k == 0
            c.pen.rect(140, y, 940, y + 90, fill=(200, 240, 200) if on else LIGHT, outline=INK if on else GREY, w=3)
            c.pen.text(180, y + 45, 'on screen · rendered' if on else 'off screen · skipped', 'ints', 30, INK if on else MUTE, 'lm')
    td = c.T('DOM')
    if c.on(td): label(c, 540, 1325, 'still in the DOM · still findable', td, YEL, INK, 32)

def proof(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Performance monitor',), dy=(1 - c.P(0, 0.45)) * 900)
    tw = c.T('watch')
    if c.on(tw):
        c.pen.text(100, 480, 'DOM Nodes', 'int', 30, WHITE, 'lm')
        c.pen.text(980, 480, '1,412', 'monob', 34, GRN, 'rm')
        pts = [(100 + k * 22, 820 - 120 - 6 * math.sin(k * 0.7)) for k in range(int(40 * c.P(tw, 2.0, lambda x: x)) + 1)]
        if len(pts) > 1: c.pen.line(pts, GRN, 5)
        c.pen.line([(100, 820), (980, 820)], (90, 96, 106), 2)
    tf = c.T('flat')
    if c.on(tf): txt(c, 540, 940, 'stays flat while you scroll', tf, 'intx', 38, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'What breaks with virtualization?', c.T('breaks'), 'intx', 46, INK)
    rows(c, 90, 620, [('Control', 'Ctrl+F misses unrendered rows', None, 'no'), ('readers', "screen readers can't see the full list", None, 'no'),
                      ('heights', 'unknown heights → jumpy scrollbar', None, 'no')], 140, 900, 110, 36)
    tt = c.T('trade')
    if c.on(tt): label(c, 540, 1080, 'know the trade-offs first', tt, YEL, INK, 34)

SCENES = [
    (hook, "Your admin table has ten thousand rows. Render them all, and you create over a hundred thousand DOM nodes. The page takes seconds to appear, and every scroll stutters."),
    (define, "Virtualization, also called windowing, renders only the rows you can see, plus a few extra above and below. As you scroll, rows leaving the screen get reused for the ones coming in."),
    (window_, "It's like a train window. The landscape runs for hundreds of kilometers, but the window only shows one view at a time. You only need what's passing the glass."),
    (how, "Under the hood, one tall spacer gives the scrollbar the right height. On scroll, you compute which rows fall inside the viewport, and position just those."),
    (libs, "In practice, use a library, like TanStack Virtual or react window. They handle variable row heights, overscan, and scroll restoration."),
    (cv, "For long pages of content, there's a CSS shortcut: content visibility auto. The browser skips rendering work for off screen sections, while keeping them in the DOM."),
    (proof, "Open the Performance monitor in DevTools, and watch DOM nodes while you scroll a virtualized list. The count stays flat, no matter how far you go."),
    (gotcha, "Interview trap: what breaks with virtualization? Control F can't find rows that aren't rendered. Screen readers may not know the full list size. And rows with unknown heights make the scrollbar jump. Know the trade offs first."),
    (scene_next('S3 · E26', 'WEB WORKERS', 'a second chef for heavy work', 'web', 'chef'),
     "Next: Web Workers, a second chef for your heavy work. Comment NOTES for the cheat sheet."),
]
