from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E05', tag='S3 · E05', short='INP', hook='the tap that takes forever')

def hook(c):
    phone(c, 540, 760, 460, 860, url='shop.example.com', dy=(1 - c.P(0, 0.45)) * 900)
    c.pen.rect(360, 460, 720, 760, fill=(230, 220, 205)); c.pen.text(540, 610, 'sneakers', 'intx', 40, MUTE)
    c.pen.rr(360, 800, 720, 900, 24, fill=YEL, outline=INK, w=4); c.pen.text(540, 850, 'Add to cart', 'intx', 36, INK)
    for n, kw in ((1, 'tap'), (2, 'tap')):
        t = c.T(kw, n)
        if c.on(t) and c.t < t + 0.5:
            r = 20 + 60 * lin(c.t, t, t + 0.5); c.pen.circ(600, 850, r, outline=INK, w=5); c.sfx(t, 'click')
    tr = c.T('react')
    if c.on(tr): txt(c, 540, 960, '...nothing', tr, 'intx', 38, RED)
    tt = c.T('two')
    if c.on(tt):
        c.pen.circ(700, 300, 50 * c.B(tt, 0.4), fill=RED, outline=INK, w=4); c.pen.text(700, 300, '2', 'osw', 60 * c.B(tt, 0.4), WHITE)
        c.sfx(tt, 'ding'); stamp(c.cv, 540, 1270, 'ORDERED TWICE', 66, c.P(tt + 0.3, 0.35), -3, RED)

def define(c):
    title(c, 'INTERACTION TO NEXT PAINT', 330, c.T('Interaction'), 72, hlcol=YEL)
    tt = c.T('tap')
    axis(c, 140, 940, 620, tt, [(0.0, 'tap', tt, BLUE), (1.0, 'next paint', c.T('visibly'), GRN)])
    if c.on(c.T('visibly')):
        p = c.P(c.T('visibly'), 0.5); c.pen.rect(140, 650, 140 + 800 * p, 690, fill=PURPLE); txt(c, 540, 740, 'INP', c.T('visibly') + 0.3, 'osw', 60, PURPLE)
    gauge(c, 540, 1080, 170, 0.3, c.T('Good'), '', 'good ≤ 200 ms')

def parts(c):
    title(c, '3 PARTS', 330, c.T('three'), 110)
    segs = [('Input delay', 0.35, RED, 'Input', 'main thread busy'), ('Processing', 0.4, YEL, 'Processing', 'your handlers run'),
            ('Presentation', 0.25, CYAN, 'Presentation', 'style · layout · paint')]
    x = 90
    for k, (nm, w, col, kw, sub) in enumerate(segs):
        t = c.T(kw); ww = 900 * w
        if c.on(t):
            p = c.P(t, 0.4); c.sfx(t, 'pop')
            c.pen.rect(x + 6, 520 + 8, x + ww * p + 6, 640 + 8, fill=INK)
            c.pen.rect(x, 520, x + ww * p, 640, fill=col, outline=INK, w=4)
            c.pen.text(x + ww / 2, 580, nm, 'intx', 30, INK)
            y = 760 + k * 150
            card(c.pen, 140, y - 55, 940, y + 55, 18, WHITE, 8, 4)
            c.pen.circ(200, y, 22, fill=col, outline=INK, w=4)
            c.pen.text(250, y, nm + ': ' + sub, 'ints', 34, INK, 'lm')
        x += ww

def doorbell(c):
    card(c.pen, 300, 420, 780, 1150, 20, (170, 110, 60), 12, 5)
    td = c.T('door', 1)
    op = c.P(td, 0.6) if c.on(td) else 0
    c.pen.rect(340, 470, 740, 1110, fill=(255, 240, 200), outline=INK, w=4)
    if op > 0.5: person(c.pen, 560, 1110, 1.8, BLUE)
    c.pen.rect(340, 470, 740 - 360 * op, 1110, fill=(140, 85, 45), outline=INK, w=4)
    c.pen.circ(700 - 360 * op, 800, 14, fill=YEL, outline=INK, w=3)
    tr = c.T('ringing')
    if c.on(tr):
        c.pen.circ(870, 760, 34, fill=WHITE, outline=INK, w=5); c.pen.circ(870, 760, 14, fill=YEL)
        for k in range(2):
            r = 50 + 20 * k + 12 * math.sin(c.t * 8)
            c.pen.arc(870 - r, 760 - r, 870 + r, 760 + r, -40, 40, INK, 4)
    th = c.T('hears')
    if c.on(th): pill(c.pen, 540, 360, 'heard ≠ done', c.B(th, 0.35), WHITE, INK, 32)
    tn = c.T('next')
    if c.on(tn): stamp(c.cv, 540, 1270, 'DOOR OPENS = NEXT PAINT', 54, c.P(tn, 0.35), -3, GRN); c.sfx(tn, 'thud')

def worst(c):
    title(c, 'NOT THE AVERAGE', 330, c.T('average'), 100)
    ts = c.T('slowest')
    vals = [60, 90, 40, 120, 80, 640, 70, 100]
    for k, v in enumerate(vals):
        x = 140 + k * 100; t = ts - 0.8 + k * 0.1
        if not c.on(t): continue
        h = v * 0.9 * c.P(t, 0.3)
        col = RED if v > 500 else GRN
        c.pen.rect(x, 1060 - h, x + 70, 1060, fill=col, outline=INK, w=3)
    c.pen.line([(120, 1064), (960, 1064)], INK, 5)
    if c.on(ts): pill(c.pen, 690, 410, '640 ms = your INP', c.B(ts, 0.35), RED, WHITE, 30, outline=None)
    tf = c.T('dropdown')
    if c.on(tf): txt(c, 540, 1140, 'one sluggish filter dropdown fails the page', tf, 'intx', 34, INK)

def fix(c):
    code(c, 50, 330, 1030, 760, ["button.addEventListener('click', async () => {", '  showSpinner();          // feedback first',
                                 '  await scheduler.yield(); // let it paint', '  recalculateCart();      // heavy work after', '});'],
         c.T('feedback') - 0.5, 0.15, 28, 'cart.js', marks=[(1, c.T('feedback'), YEL), (2, c.T('yield'), YEL), (3, c.T('heavy'), (60, 110, 70))])
    rows(c, 100, 880, [('small', 'keep handlers small', None, 'ok'), ('break', 'break long tasks (S1 · E18)', None, 'ok'),
                      ('waits', 'input never waits for the chef', None, 'ok')], 120, 880, 96, 34)

def proof(c):
    panel(c, 60, 330, 1020, 1220, tabs=('Performance', 'Live metrics'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tl = c.T('live')
    if c.on(tl):
        c.pen.text(110, 480, 'Interaction to Next Paint', 'ints', 32, WHITE, 'lm')
        counter(c, 900, 480, 0, 312, tl, tl + 1.0, '{:.0f}', 60, ORANGE, ' ms')
    ti = c.T('lists')
    items = [('pointer  button.add-to-cart', '312 ms', ORANGE), ('keyboard input#search', '96 ms', GRN), ('pointer  a.filter', '184 ms', GRN)]
    for k, (nm, v, col) in enumerate(items):
        t = ti + k * 0.3
        if not c.on(t): continue
        y = 600 + k * 90; c.sfx(t, 'tick')
        c.pen.text(110, y, nm, 'mono', 28, WHITE, 'lm'); c.pen.text(970, y, v, 'monob', 30, col, 'rm')
    tp = c.T('parts')
    if c.on(tp):
        c.pen.text(110, 900, 'button.add-to-cart', 'monob', 28, YEL, 'lm')
        x = 110
        for nm, w, col in (('input delay 180', 0.55, RED), ('processing 90', 0.27, YEL), ('presentation 42', 0.18, CYAN)):
            ww = 860 * w * c.P(tp, 0.5); c.pen.rect(x, 950, x + ww, 1010, fill=col)
            if c.P(tp, 0.5) > 0.9: c.pen.text(x + 12, 1050, nm, 'mono', 22, (200, 205, 215), 'lm')
            x += 860 * w

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Does scrolling count toward INP?', c.T('scrolling'), 'intx', 46, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 610, tn, 120, RED)
    for k, (nm, ok, kw) in enumerate((('click', True, 'clicks'), ('tap', True, 'taps'), ('key press', True, 'key'), ('scroll', False, 'Scrolling'), ('hover', False, 'hovering'))):
        t = c.T(kw) if kw != 'Scrolling' else c.T('Scrolling', 1)
        if kw == 'Scrolling': t = c.T('scrolling', 2)
        y = 740 + k * 105
        if not c.on(t): continue
        pill(c.pen, 420, y, nm, c.B(t, 0.3), (215, 240, 215) if ok else (255, 225, 225), INK, 34)
        (check if ok else cross)(c.pen, 650, y, 1.0, GRN if ok else RED, 9, c.P(t + 0.1, 0.3))

SCENES = [
    (hook, "You tap Add to cart. The button doesn't react. So you tap again. Now there are two pairs in your cart."),
    (define, "Interaction to Next Paint, or INP, measures the time from your tap, click or key press until the screen visibly updates. Good is two hundred milliseconds or less."),
    (parts, "Every interaction has three parts. Input delay: waiting for the main thread to be free. Processing: your event handlers running. Presentation delay: style, layout and paint before the next frame."),
    (doorbell, "Think of ringing a doorbell. What matters isn't when someone inside hears it. It's when the door opens. INP waits for the door to open: the next paint."),
    (worst, "And INP isn't an average. It's roughly your slowest interaction in the whole visit. One sluggish filter dropdown can fail the entire page."),
    (fix, "So show feedback first, yield so the browser can paint, then do the heavy work. Keep handlers small, and break up long tasks, so input never waits for the one chef."),
    (proof, "In DevTools, the Performance panel shows live INP as you click around. It lists every interaction, and splits the slow ones into their three parts."),
    (gotcha, "Interview trap: does scrolling count toward INP? No. Only clicks, taps and key presses. Scrolling and hovering aren't measured."),
    (scene_next('S3 · E06', 'TTFB · FCP · TBT', 'the supporting cast of metrics', 'TTFB', 'supporting'),
     "Next: TTFB, FCP and TBT, the supporting cast of metrics. Comment NOTES for the cheat sheet."),
]
