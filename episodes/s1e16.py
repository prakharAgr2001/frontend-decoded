from engine.lib import *

EP = dict(id='S1E16', tag='S1 · E16', short='MICROTASKS vs TASKS')

def hook(c):
    node(c, 280, 600, 380, 220, 'Promise.then', 0.2, None, fill=(255, 246, 214), size=40)
    node(c, 800, 600, 380, 220, 'setTimeout 0', 0.6, None, fill=(225, 240, 255), size=40)
    c.pen.text(540, 600, 'vs', 'osw', 70, INK)
    tw = c.T('first')
    if c.on(tw):
        c.sfx(tw, 'thud'); s = c.B(tw, 0.4)
        c.pen.circ(540, 900, 90 * s, fill=YEL, outline=INK, w=5); c.pen.text(540, 900, '?', 'osw', 120 * s, INK)
    tg = c.T('wrong')
    if c.on(tg): txt(c, 540, 1080, 'most people guess wrong', tg, 'intx', 40, RED)

def queues(c):
    for j, (lab, items, kw, col) in enumerate([('TASK QUEUE', ['setTimeout', 'click', 'message'], 'task', CYAN),
                                              ('MICROTASK QUEUE', ['promise.then', 'queueMicrotask'], 'microtask', YEL)]):
        at = c.T(kw); y = 470 + j * 380
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        c.pen.text(110, y, lab, 'osw', 54, INK, 'lm')
        c.pen.rr(100, y + 50, 980, y + 220, 20, outline=INK, w=5)
        for i, s_ in enumerate(items):
            a2 = at + 0.4 + i * 0.25
            if c.on(a2):
                w = c.pen.tw(s_, 'monob', 28) + 40
                x = 130 + sum(c.pen.tw(t, 'monob', 28) + 70 for t in items[:i])
                c.pen.rr(x, y + 95, x + w, y + 175, 14, fill=col, outline=INK, w=3)
                c.pen.text(x + w / 2, y + 135, s_, 'monob', 28, INK)

def club(c):
    title(c, 'THE VIP LINE', 330, c.T('VIP'), 100, hlcol=YEL)
    tb = c.T('bouncer')
    person(c.pen, 540, 820, 1.2 * c.B(tb, 0.4) if c.on(tb) else 0.01, INK)
    if c.on(tb): c.pen.text(540, 860, 'event loop', 'int', 28, INK)
    te = c.T('entire')
    for i in range(4):
        q = c.P(te + i * 0.35, 0.5) if c.on(te) else 0
        x = 200 + i * 80 + q * (440 - i * 80 + 200)
        y = 560 - q * 140
        if q < 1: person(c.pen, 260 - i * 0, 640 - 0, 0, YEL)
        person(c.pen, 100 + i * 90 + q * 600, 620 - q * 60, 0.7, YEL)
    for i in range(4):
        person(c.pen, 100 + i * 90, 1060, 0.7, CYAN)
    c.pen.text(110, 450, 'VIP · microtasks', 'int', 30, INK, 'lm')
    c.pen.text(110, 1110, 'regular · tasks', 'int', 30, INK, 'lm')
    tr = c.T('regular')
    if c.on(tr): label(c, 760, 1100, 'waits until VIP is empty', tr, RED, WHITE, 26)

def rule(c):
    title(c, 'THE RULE', 330, 0.1, 100, hlcol=YEL)
    seq = [('task', CYAN, 'task', 170), ('micro', YEL, 'drains', 90), ('micro', YEL, 'drains', 90), ('micro', YEL, 'new', 90),
           ('render', GRN, 'render', 140), ('task', CYAN, 'next', 170)]
    x = 100
    for i, (lab, col, kw, w) in enumerate(seq):
        at = c.T(kw) + (0.25 * (i - 1) if kw == 'drains' else 0)
        if c.on(at):
            c.sfx(at, 'tick'); p = c.P(at, 0.3)
            c.pen.rr(x, 560, x + (w - 10) * p, 680, 14, fill=col, outline=INK, w=4)
            if p > 0.8: c.pen.text(x + (w - 10) / 2, 620, lab, 'int', 24, INK)
        x += w
    tn = c.T('new')
    if c.on(tn): txt(c, 540, 780, '…including microtasks added along the way', tn, 'int', 34, INK)
    tr = c.T('render')
    if c.on(tr): txt(c, 540, 860, 'rendering waits for the microtask queue to empty', tr, 'int', 34, MUTE)

PUZ = ["console.log(1);", "setTimeout(() => console.log(2));", "Promise.resolve().then(() => console.log(3));", "console.log(4);"]

def puzzle(c):
    code(c, 40, 320, 1040, 640, PUZ, c.T('one') - 0.3, 0.35, 26, 'puzzle.js')
    tg = c.T('guess')
    ta = c.T('answer')
    if c.on(tg) and not c.on(ta):
        frac = lin(c.t, tg, ta)
        ring(c, 540, 860, 90, frac, YEL, 18)
        c.pen.text(540, 860, '?', 'osw', 90, INK)
    if c.on(ta):
        darkcard(c.pen, 200, 760, 880, 940)
        out = [str(n) for n, kw, k in ((1, 'one', 3), (4, 'four', 2), (3, 'three', 2), (2, 'two', 2)) if c.on(c.T(kw, k))]
        c.pen.text(540, 850, '   '.join(out), 'monob', 80, (120, 220, 150))
        txt(c, 540, 1040, 'promise (micro) beats timer (task)', ta + 2.5, 'intx', 38, INK)

def starve(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    title(c, 'MICROTASK STARVATION', 470, c.T('starvation'), 70)
    te = c.T('each')
    if c.on(te):
        cx, cy, r = 540, 780, 150
        ang = (c.t - te) * 5
        c.pen.circ(cx, cy, r, outline=LIGHT, w=18)
        c.pen.arc(cx - r, cy - r, cx + r, cy + r, math.degrees(ang) % 360, math.degrees(ang) % 360 + 90, YEL, 18)
        c.pen.text(cx, cy, 'micro → micro', 'monob', 32, INK)
    tf = c.T('freezes')
    if c.on(tf):
        node(c, 260, 1060, 300, 120, 'tasks', tf, None, fill=(255, 225, 225), sub='never reached', size=34)
        node(c, 820, 1060, 300, 120, 'render', tf + 0.2, None, fill=(255, 225, 225), sub='never happens', size=34)

SCENES = [
    (hook, "A promise callback, or a setTimeout with zero delay. Which runs first? Most people guess wrong."),
    (queues, "There are actually two queues. The task queue, for things like timers and events. And the microtask queue, for promise callbacks and queueMicrotask."),
    (club, "Think of a club with a VIP line. Every time the bouncer is free, he lets the entire VIP line in, before a single person from the regular line."),
    (rule, "That's the rule. After each task finishes, the event loop drains every microtask, including new ones added along the way. Only then can the browser render, and pick the next task."),
    (puzzle, "Try this one. Log one. A timeout logs two. A promise logs three. Log four. Pause and guess. [[3]] The answer: one, four, three, two."),
    (starve, "Interview trap: microtask starvation. If each microtask queues another one, the loop never gets back to tasks or rendering, and the page freezes, even though no single function is slow."),
    (scene_next('S1 · E17', '16 ms', 'the frame budget you can not miss', 'sixteen', 'budget'),
     "Next: the sixteen millisecond frame budget. Comment NOTES for the cheat sheet."),
]
