from engine.lib import *

EP = dict(id='S1E15', tag='S1 · E15', short='CALL STACK & QUEUE')

CODE = ["console.log('A');", "setTimeout(() => console.log('B'), 0);", "console.log('C');"]

def board(c, stack, web=None, queue=(), out=(), hl_line=None, t_in=0.0):
    """shared layout: code top, stack left, web APIs right, queue bottom, console strip"""
    code(c, 60, 290, 1020, 560, CODE, -1, 0, 28, 'demo.js', marks=[(hl_line, 0, YEL)] if hl_line is not None else (), dy=0)
    c.pen.text(110, 620, 'CALL STACK', 'int', 28, INK, 'lm')
    c.pen.rr(100, 640, 470, 1040, 18, outline=INK, w=5)
    for i, s_ in enumerate(stack):
        y = 1000 - i * 80
        c.pen.rr(120, y - 34, 450, y + 34, 12, fill=YEL if i == len(stack) - 1 else WHITE, outline=INK, w=4)
        c.pen.text(285, y, s_, 'monob', 26, INK)
    c.pen.text(560, 620, 'WEB APIs', 'int', 28, INK, 'lm')
    c.pen.rr(550, 640, 980, 820, 18, fill=(225, 240, 255), outline=INK, w=5)
    if web: c.pen.text(765, 730, web, 'monob', 28, INK)
    c.pen.text(560, 870, 'TASK QUEUE', 'int', 28, INK, 'lm')
    c.pen.rr(550, 890, 980, 1040, 18, outline=INK, w=5)
    for i, s_ in enumerate(queue):
        c.pen.rr(570 + i * 200, 925, 750 + i * 200, 1005, 12, fill=CYAN, outline=INK, w=3); c.pen.text(660 + i * 200, 965, s_, 'monob', 26, INK)
    c.pen.rr(100, 1090, 980, 1180, 16, fill=DARK, outline=INK, w=4)
    c.pen.text(130, 1135, 'console:', 'monob', 28, (140, 146, 156), 'lm')
    c.pen.text(290, 1135, '  '.join(out), 'monob', 34, WHITE, 'lm')

def hook(c):
    code(c, 60, 330, 1020, 600, CODE, 0.1, 0.4, 28, 'demo.js')
    ta = c.T('A', 3)
    if c.on(ta):
        darkcard(c.pen, 200, 720, 880, 900)
        out = [s for s, at in (('A', ta), ('C', c.T('C', 2)), ('B', c.T('B', 2))) if c.on(at)]
        c.pen.text(540, 810, '   '.join(out), 'monob', 80, (120, 220, 150))
    te = c.T('Every')
    if c.on(te): stamp(c.cv, 540, 1030, 'EVERY. SINGLE. TIME.', 56, c.P(te, 0.35), -3, RED)

def stack(c):
    tp = c.T('plate')
    items = []
    if c.on(c.T('call')): items.append('main()')
    if c.on(tp): items.append("console.log('A')")
    if c.on(c.T('returns')): items = items[:1]
    board(c, items, hl_line=0 if c.on(tp) else None)
    if c.on(tp): label(c, 760, 1260, 'each call = a plate on top', tp, YEL, INK, 30)

def webapi(c):
    tw = c.T('hands')
    st = ['main()', 'setTimeout(…)'] if not c.on(c.T('returns')) else ['main()']
    if c.on(c.T('C')): st = ['main()', "console.log('C')"]
    board(c, st, web='timer: 0 ms → B' if c.on(tw) else None, out=['A'] + (['C'] if c.on(c.T('C')) else []), hl_line=2 if c.on(c.T('C')) else 1)
    if c.on(tw): arrow(c.pen, 460, 920, 560, 760, c.P(tw, 0.4), INK, 6, 20)

def queue(c):
    tj = c.T('joins')
    board(c, ['main()'] if not c.on(tj) else [], web=None if c.on(tj) else 'timer: 0 ms → B', queue=['B()'] if c.on(tj) else [], out=['A', 'C'])
    if c.on(tj): c.sfx(tj, 'pop'); arrow(c.pen, 765, 820, 765, 900, c.P(tj, 0.4), INK, 6, 20)
    tl = c.T('line')
    if c.on(tl): label(c, 760, 1260, 'jobs wait their turn', tl, CYAN, INK, 30)

def loop(c):
    te = c.T('empty')
    moved = c.on(c.T('pushes'))
    printed = c.on(c.T('print'))
    board(c, ['B()'] if moved and not printed else [], queue=[] if moved else ['B()'], out=['A', 'C'] + (['B'] if printed else []))
    if c.on(te):
        ang = (c.t - te) * 4
        cx, cy, r = 510, 940, 46
        c.pen.arc(cx - r, cy - r, cx + r, cy + r, math.degrees(ang) % 360, math.degrees(ang) % 360 + 280, ORANGE, 9)
        label(c, 540, 1260, 'event loop: stack empty? → next task', te, ORANGE, WHITE, 28)
    if printed: c.sfx(c.T('print'), 'ding')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, "What's the minimum setTimeout delay?", c.T('minimum'), 'intx', 46, INK)
    tr = c.T('request')
    if c.on(tr): label(c, 540, 600, '0 = a request, not a promise', tr, YEL, INK, 36)
    tw = c.T('waits')
    if c.on(tw):
        node(c, 300, 820, 380, 200, 'stack must be empty', tw, None, sub='then the callback runs', size=32)
    tc = c.T('clamped')
    if c.on(tc):
        node(c, 780, 820, 380, 200, 'nested timers', tc, None, fill=(255, 246, 214), sub='clamped to ≥ 4 ms', size=32)

SCENES = [
    (hook, "Log A. Set a timeout with zero delay, that logs B. Then log C. The output: A, C, B. Every single time. Here's why."),
    (stack, "JavaScript runs code on the call stack. Each function call is a plate stacked on top. The engine only works on the top plate, and when it returns, the plate comes off."),
    (webapi, "When setTimeout runs, it doesn't wait on the stack. It hands the timer to the browser, and returns immediately. So log C runs next."),
    (queue, "When the timer fires, its callback joins the task queue, a line of jobs waiting their turn."),
    (loop, "The event loop has one job. When the call stack is empty, it takes the next task from the queue and pushes it onto the stack. Only then does B print."),
    (gotcha, "Interview question: what's the minimum delay for setTimeout? Zero is a request, not a promise. The callback still waits for the stack to empty, and deeply nested timers get clamped to at least four milliseconds."),
    (scene_next('S1 · E16', 'MICROTASKS', 'the VIP lane of the event loop', 'microtasks', 'VIP'),
     "Next: microtasks versus macrotasks, the VIP lane of the event loop. Comment NOTES for the cheat sheet."),
]
