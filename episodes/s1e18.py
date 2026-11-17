from engine.lib import *

EP = dict(id='S1E18', tag='S1 · E18', short='LONG TASKS')

def hook(c):
    tt = c.T('tap')
    card(c.pen, 290, 380, 790, 900, 40, WHITE, 12, 6)
    c.pen.rr(380, 600, 700, 700, 50, fill=YEL, outline=INK, w=5); c.pen.text(540, 650, 'Add to cart', 'intx', 38, INK)
    if c.on(tt):
        r = 30 + 60 * lin(c.t, tt, tt + 0.4)
        c.pen.circ(600, 660, r, outline=mix(INK, PAPER, lin(c.t, tt, tt + 0.4)), w=5)
    tn = c.T('Nothing')
    if c.on(tn): counter(c, 540, 1020, 0, 500, tn, c.T('responds'), '{:.0f}', 110, RED, ' ms')
    tl = c.T('long')
    if c.on(tl): stamp(c.cv, 540, 1180, 'A LONG TASK', 62, c.P(tl, 0.35), -3, RED)

def define(c):
    title(c, 'LONG TASK = > 50 ms', 330, c.T('fifty'), 96, hlcol=YEL)
    tasks = [(0.00, 0.05), (0.06, 0.04), (0.11, 0.30), (0.42, 0.05), (0.48, 0.38), (0.88, 0.06)]
    ta = c.T('Any')
    for i, (s, d) in enumerate(tasks):
        at = ta + i * 0.2
        if not c.on(at): continue
        xa = 110 + 860 * s; xb = xa + 860 * d * c.P(at, 0.3)
        long_ = d > 0.1
        c.pen.rect(xa, 560, xb, 660, fill=(150, 150, 160) if not long_ else (200, 200, 205), outline=INK, w=3)
        if long_ and c.on(c.T('fifty') + 0.3):
            x50 = xa + 860 * 0.06
            for k in range(int((xb - x50) // 18)): c.pen.line([(x50 + k * 18, 660), (x50 + k * 18 + 14, 560)], RED, 4, False)
            c.pen.poly([(xb - 22, 560), (xb, 560), (xb, 582)], fill=RED)
    tr = c.T('respond')
    if c.on(tr):
        for i, nm in enumerate(['tap', 'click', 'key']):
            pill(c.pen, 300 + i * 240, 820, nm + ' → waits', c.B(tr + i * 0.15, 0.3), (255, 225, 225), INK, 28)

def why50(c):
    title(c, 'WHY 50 ms?', 330, 0.1, 100)
    ti = c.T('instant')
    if c.on(ti):
        c.pen.rect(110, 560, 110 + 860 * c.P(ti, 0.5), 680, fill=WHITE, outline=INK, w=4)
        c.pen.text(540, 520, '100 ms feels instant', 'intx', 40, INK)
    tf = c.T('task')
    if c.on(tf):
        c.pen.rect(110, 560, 110 + 430 * c.P(tf, 0.3), 680, fill=YEL, outline=INK, w=4); c.pen.text(325, 620, '50 · your task', 'int', 30, INK)
    th = c.T('handle')
    if c.on(th):
        c.pen.rect(540, 560, 540 + 430 * c.P(th, 0.3), 680, fill=GRN, outline=INK, w=4); c.pen.text(755, 620, '50 · input + paint', 'int', 30, WHITE)

def bank(c):
    node(c, 540, 470, 360, 170, 'Bank counter', c.T('bank'), 'server')
    tc = c.T('hundred')
    for i in range(5):
        x = 540 if i == 0 else 540 - 0
        person(c.pen, 540, 800 + i * 0, 0, INK)
    if c.on(tc):
        person(c.pen, 540, 760, 1.1, ORANGE)
        for k in range(6): c.pen.rect(600 + k * 10, 640 - k * 10, 680 + k * 10, 700 - k * 10, fill=WHITE, outline=INK, w=2)
        c.pen.text(700, 590, '×100 cheques', 'int', 28, INK, 'lm')
    tw = c.T('waits')
    if c.on(tw):
        for k in range(4): person(c.pen, 180 + k * 100, 1050, 0.7, BLUE)
        txt(c, 330, 1100, 'everyone behind waits', tw, 'int', 28, RED)
    ts = c.T('Split')
    if c.on(ts): label(c, 760, 1000, 'split into smaller visits', ts, GRN, WHITE, 28)

def fix(c):
    code(c, 60, 320, 1020, 640, ['for (const item of items) {', '  process(item);', '  await scheduler.yield(); // let input in', '}'],
         c.T('chunks') - 0.5, 0.15, 30, 'work.js', marks=[(2, c.T('yield'), YEL)])
    ty = c.T('gaps')
    if c.on(ty):
        x = 110
        for k in range(6):
            c.pen.rect(x, 780, x + 110, 860, fill=YEL, outline=INK, w=3); x += 110
            if k == 2: c.pen.rect(x, 780, x + 30, 860, fill=GRN, outline=INK, w=3); c.pen.text(x + 15, 900, 'tap!', 'int', 26, GRN)
            x += 30
        txt(c, 540, 980, 'input handled in the gaps', ty, 'intx', 38, GRN)
    ts = c.T('setTimeout')
    if c.on(ts): txt(c, 540, 1060, 'older browsers: await new Promise(r => setTimeout(r))', ts, 'mono', 26, MUTE)

def proof(c):
    panel(c, 60, 330, 1020, 900, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    blocks = [(0.0, 0.08, 0, 'JS'), (0.1, 0.5, 0, 'JS', True), (0.62, 0.08, 0, 'Layout'), (0.72, 0.06, 0, 'Paint')]
    flame(c, 100, 500, 980, blocks, c.T('Performance'), 80)
    th = c.T('Hover')
    if c.on(th):
        c.sfx(th, 'pop'); card(c.pen, 260, 640, 900, 800, 14, WHITE, 6, 3)
        c.pen.text(290, 690, 'Long task · 412 ms', 'intx', 34, RED, 'lm')
        c.pen.text(290, 750, 'Function call  ·  app.js:128', 'mono', 26, INK, 'lm')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Which metric measures this?', c.T('metric'), 'intx', 48, INK)
    title(c, 'INP', 680, c.T('Interaction'), 220, RED)
    txt(c, 540, 840, 'Interaction to Next Paint', c.T('Interaction') + 0.3, 'intx', 44, INK)
    txt(c, 540, 920, 'how long the page takes to respond to input', c.T('tracks'), 'int', 32, MUTE)
    ty = c.T('twenty')
    if c.on(ty): label(c, 540, 1060, 'Core Web Vital since 2024 (replaced FID)', ty, YEL, INK, 30)

SCENES = [
    (hook, "You tap a button. Nothing happens. Half a second later, it finally responds. Somewhere, a long task was hogging the main thread."),
    (define, "Any task that runs longer than fifty milliseconds is a long task. While it runs, the browser can't respond to taps, clicks or key presses."),
    (why50, "Why fifty? To feel instant, a response should land within about a hundred milliseconds. Fifty for your task. Fifty to handle the input and paint."),
    (bank, "It's like one customer at a bank counter with a hundred cheques. Everyone behind them waits. Split the job into smaller visits, and others can squeeze in."),
    (fix, "So break the work into chunks, and yield back to the browser between them. With await scheduler dot yield, or a simple setTimeout, the browser handles input in the gaps."),
    (proof, "In the Performance panel, long tasks get a red triangle in the corner. Hover one to see exactly what caused it."),
    (gotcha, "Interview question: which metric measures this? Interaction to Next Paint, or INP. It tracks how long the page takes to respond to input, and it became a Core Web Vital in twenty twenty four."),
    (scene_next('S1 · E19', 'PREDICT THE OUTPUT', 'event loop interview puzzles', 'predict', 'puzzles'),
     "Next: predict the output, event loop puzzles from real interviews. Comment NOTES for the cheat sheet."),
]
