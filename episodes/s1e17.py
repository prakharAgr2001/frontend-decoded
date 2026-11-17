from engine.lib import *

EP = dict(id='S1E17', tag='S1 · E17', short='16 ms FRAME BUDGET')

def strip(c, y, n, at, miss=None, w=110):
    for i in range(n):
        x = 110 + i * (w + 14)
        if not c.on(at + i * 0.1): continue
        missed = miss is not None and i == miss and c.on(at + 1.5)
        c.pen.rr(x, y, x + w, y + 150, 10, fill=(255, 225, 225) if missed else WHITE, outline=RED if missed else INK, w=4)
        if missed: cross(c.pen, x + w / 2, y + 75, 1.0, RED, 9)
        else: c.pen.rect(x + 14, y + 20, x + w - 14, y + 130, fill=YEL if i % 2 else (255, 230, 150))

def hook(c):
    title(c, '60 FRAMES / SECOND', 340, c.T('sixty'), 100, hlcol=YEL)
    strip(c, 500, 7, c.T('sixty') + 0.2, miss=4 if c.on(c.T('Miss')) else None)
    tm = c.T('sixteen')
    bignum(c, 540, 860, '≈16.7 ms', tm, 130, RED)
    txt(c, 540, 980, 'per frame', tm + 0.2, 'intx', 40, INK)
    tmi = c.T('drop')
    if c.on(tmi): stamp(c.cv, 540, 1110, 'DROPPED FRAME = JANK', 52, c.P(tmi, 0.35), -3, RED)

def budget(c):
    title(c, 'WHAT FITS IN 16 ms', 330, 0.1, 96)
    segs = [('JS', 0.30, YEL, 'JavaScript'), ('Style', 0.12, (150, 120, 230), 'style'), ('Layout', 0.18, PURPLE, 'layout'),
            ('Paint', 0.16, GRN, 'paint'), ('Comp', 0.10, CYAN, 'composite')]
    x = 110
    for lab, d, col, kw in segs:
        at = c.T(kw); w = 860 * d
        if c.on(at):
            c.sfx(at, 'tick'); c.pen.rect(x, 560, x + w * c.P(at, 0.3), 680, fill=col, outline=INK, w=3)
            c.pen.text(x + w / 2, 620, lab, 'int', 26, INK if lab not in ('Layout',) else WHITE)
        x += w
    c.pen.line([(110, 720), (970, 720)], INK, 4); c.pen.text(970, 760, '16.7 ms', 'monob', 30, INK, 'rm')
    tt = c.T('ten')
    if c.on(tt):
        c.pen.rect(110, 800, 110 + 516 * c.P(tt, 0.4), 860, fill=YEL, outline=INK, w=3)
        c.pen.text(110, 900, 'your JS: keep it under ~10 ms', 'intx', 38, INK, 'lm')

def interval(c):
    title(c, 'setInterval: A GAMBLE', 330, 0.1, 90)
    c.pen.text(110, 500, 'frames', 'int', 30, INK, 'lm')
    for i in range(8): c.pen.rect(240 + i * 95, 470, 250 + i * 95, 540, fill=INK)
    tr = c.T('random')
    c.pen.text(110, 640, 'interval', 'int', 30, RED, 'lm')
    for k, x in enumerate([270, 330, 455, 590, 600, 760, 880]):
        at = tr + k * 0.12
        if c.on(at): c.pen.circ(x, 640, 16, fill=RED, outline=INK, w=3)
    tt = c.T('twice')
    if c.on(tt): c.pen.rr(570, 600, 630, 680, 10, outline=RED, w=4); txt(c, 600, 730, 'twice in one frame', tt, 'int', 28, RED)
    tn = c.T('not')
    if c.on(tn): c.pen.rr(620, 600, 720, 680, 10, outline=ORANGE, w=4); txt(c, 760, 790, 'none in this one', tn, 'int', 28, ORANGE)

def raf(c):
    title(c, 'requestAnimationFrame', 330, c.T('requestAnimationFrame'), 84, hlcol=YEL)
    c.pen.text(110, 500, 'frames', 'int', 30, INK, 'lm')
    for i in range(8): c.pen.rect(240 + i * 95, 470, 250 + i * 95, 540, fill=INK)
    tb = c.T('before')
    c.pen.text(110, 640, 'rAF', 'int', 30, GRN, 'lm')
    for i in range(8):
        if c.on(tb + i * 0.12): c.pen.circ(235 + i * 95, 640, 16, fill=GRN, outline=INK, w=3)
    to = c.T('One')
    if c.on(to): label(c, 540, 800, 'one update per frame, in sync', to, GRN, WHITE, 34)
    tp = c.T('background')
    if c.on(tp):
        node(c, 540, 1030, 460, 160, 'background tab → paused', tp, None, fill=(225, 245, 230), sub='saves battery + CPU', size=34)

def codeit(c):
    code(c, 40, 320, 1040, 700, ['function step(time) {', "  box.style.transform =", '    `translateX(${(time * 0.2) % 600}px)`;', '  requestAnimationFrame(step);', '}',
                                 'requestAnimationFrame(step);'], c.T('timestamp') - 0.6, 0.15, 26, 'animate.js',
         marks=[(0, c.T('timestamp'), YEL), (2, c.T('time'), YEL)])
    tt = c.T('time')
    if c.on(tt):
        node(c, 300, 960, 400, 180, 'motion uses time', tt, None, fill=(225, 245, 230), sub='same speed at 60 or 120 Hz', size=36)
        node(c, 780, 960, 400, 180, 'motion counts frames', tt + 0.3, None, fill=(255, 225, 225), sub='slows down when frames drop', size=36)

def proof(c):
    panel(c, 60, 330, 1020, 860, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    tf = c.T('Frames')
    c.pen.text(100, 490, 'Frames', 'mono', 28, WHITE, 'lm')
    for i in range(12):
        at = tf + i * 0.1
        if not c.on(at): continue
        bad = i in (5, 9) and c.on(c.T('red'))
        c.pen.rect(100 + i * 74, 520, 166 + i * 74, 620, fill=(220, 80, 80) if bad else (120, 200, 120), outline=INK, w=2)
    if c.on(c.T('green')): label(c, 320, 720, 'green = on time', c.T('green'), GRN, WHITE, 28)
    if c.on(c.T('red')): label(c, 760, 720, 'red = dropped', c.T('red'), RED, WHITE, 28)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Is it always 60 fps?', c.T('always'), 'intx', 50, INK)
    rows = [('60 Hz', '16.7 ms', 'sixty'), ('90 Hz', '11.1 ms', 'ninety'), ('120 Hz', '8.3 ms', 'hundred')]
    for i, (hz, ms, kw) in enumerate(rows):
        at = c.T(kw) if kw != 'sixty' else c.T('always') + 0.5
        y = 620 + i * 130
        if not c.on(at): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.3)
        card(c.pen, 200, y - 50 * s, 880, y + 50 * s, 16, WHITE if i < 2 else (255, 246, 214), 8, 4)
        c.pen.text(240, y, hz, 'osw', 52 * s, INK, 'lm'); c.pen.text(840, y, ms, 'monob', 44 * s, RED if i == 2 else INK, 'rm')
    ta = c.T('adapts')
    if c.on(ta): label(c, 540, 1060, 'rAF adapts automatically', ta, GRN, WHITE, 34)

SCENES = [
    (hook, "To look smooth, your screen redraws about sixty times a second. That gives the browser roughly sixteen milliseconds per frame. Miss it, and you drop a frame."),
    (budget, "Everything has to fit inside those sixteen milliseconds. Your JavaScript, style, layout, paint and composite. In practice, keep your own work under about ten."),
    (interval, "Animating with setInterval is a gamble. Its timer doesn't know when frames happen, so updates land at random points. Sometimes twice in one frame. Sometimes not at all."),
    (raf, "requestAnimationFrame fixes that. The browser calls your function right before it paints the next frame. One update per frame, perfectly in sync. And it pauses in background tabs, which saves battery."),
    (codeit, "Always use the timestamp it hands you, so motion depends on time, not on how many frames you happened to get."),
    (proof, "In the Performance panel, the Frames track shows green frames that arrived on time, and red frames that were dropped."),
    (gotcha, "Interview question: is it always sixty? No. Many phones and monitors run at ninety, or a hundred and twenty hertz, where the budget is just eight milliseconds. requestAnimationFrame adapts automatically."),
    (scene_next('S1 · E18', 'LONG TASKS', 'why pages freeze', 'long', 'freeze'),
     "Next: long tasks, and why pages freeze. Comment NOTES for the cheat sheet."),
]
