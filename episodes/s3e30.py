from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E30', tag='S3 · E30', short='CHUNKING LONG TASKS', hook='yield like you mean it')

def hook(c):
    tt = c.T('ten')
    if c.on(tt): counter(c, 540, 430, 0, 10000, tt, tt + 0.8, '{:,.0f}', 110, INK, ' records')
    ts = c.T('season')
    if c.on(ts): label(c, 540, 560, 'S1 · E18: split long tasks', ts, WHITE, INK, 32)
    tb = c.T('big')
    if c.on(tb): txt(c, 540, 720, 'how big should each chunk be?', tb, 'intx', 44, INK)
    th = c.T('hand')
    if c.on(th): txt(c, 540, 820, 'and how do you hand control back?', th, 'intx', 44, INK)
    if c.on(th):
        c.pen.rect(110, 960, 970, 1060, fill=(200, 200, 205), outline=INK, w=4)
        for k in range(int((c.t - th) * 4) % 9): c.pen.line([(110 + k * 100, 960), (110 + k * 100, 1060)], RED, 6)

def slices(c):
    title(c, 'SLICE BY TIME, NOT COUNT', 330, c.T('time'), 80, hlcol=YEL)
    code(c, 30, 440, 1050, 980, ['async function processAll(items) {', '  let deadline = performance.now() + 10;', '  for (const item of items) {', '    process(item);',
                                 '    if (performance.now() > deadline) {', '      await scheduler.yield();', '      deadline = performance.now() + 10;', '    }', '  }', '}'],
         c.T('milliseconds') - 0.6, 0.08, 25, 'process.js', marks=[(1, c.T('milliseconds'), YEL), (5, c.T('yield'), (60, 110, 70))])
    tf = c.T('Fast')
    if c.on(tf): label(c, 540, 1060, 'fast phones do more per slice · slow ones less', tf, WHITE, INK, 30)

def lawn(c):
    title(c, 'MOW IN STRIPS', 330, c.T('strips'), 110)
    tm = c.T('mowing')
    for k in range(6):
        x = 140 + k * 135
        done = c.on(tm + k * 0.6)
        c.pen.rect(x, 460, x + 130, 1000, fill=(120, 190, 100) if done else (70, 140, 60), outline=INK, w=3)
        if done:
            for j in range(8): c.pen.line([(x + 20, 490 + j * 65), (x + 110, 490 + j * 65)], (150, 210, 130), 4)
    td = c.T('door')
    if c.on(td):
        c.pen.rr(860, 1040, 960, 1200, 10, fill=(170, 110, 60), outline=INK, w=4); c.pen.circ(940, 1120, 8, fill=YEL)
        txt(c, 560, 1120, 'check the door after each strip', td, 'ints', 32, INK)

def yield_(c):
    title(c, 'scheduler.yield()', 330, c.T('yield'), 84, k='monob', hlcol=YEL)
    for j, (nm, kw, front) in enumerate((('scheduler.yield()', 'front', True), ('setTimeout(0)', 'back', False))):
        t = c.T(kw, 2 if kw == 'back' else 1); y = 560 + j * 330
        if not c.on(t): continue
        c.pen.text(110, y - 90, nm, 'monob', 34, INK, 'lm')
        q = ['input', 'other task', 'other task']
        order = (['input', 'your next chunk'] + q[1:]) if front else (q + ['your next chunk'])
        for k, nm2 in enumerate(order):
            x = 110 + k * 225; col = YEL if nm2 == 'your next chunk' else (RED if nm2 == 'input' else LIGHT)
            c.pen.rr(x, y - 40, x + 210, y + 40, 14, fill=col, outline=INK, w=3)
            c.pen.text(x + 105, y, nm2, 'int', 22, INK)
    tl = c.T('line')
    if c.on(tl): label(c, 540, 1170, 'yield keeps your place near the front of the line', tl, WHITE, INK, 28)

def posttask(c):
    title(c, 'scheduler.postTask()', 330, c.T('postTask'), 76, k='monob')
    for k, (nm, kw, col) in enumerate((("'user-blocking'", 'blocking', RED), ("'user-visible'", 'visible', ORANGE), ("'background'", 'background', GRN))):
        t = c.T(kw, 2 if kw == 'background' else 1); y = 520 + k * 150
        if c.on(t): pill(c.pen, 540, y, nm, c.B(t, 0.35), col, WHITE, 40)
    code(c, 30, 1000, 1050, 1150, ["scheduler.postTask(sendAnalytics, { priority: 'background' });"], c.T('background', 2) + 0.2, 0.1, 23, 'tasks.js')

def proof(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    tb = c.T('block')
    c.pen.text(100, 470, 'before', 'intx', 30, RED, 'lm')
    c.pen.rect(100, 500, 960, 570, fill=YEL, outline=INK, w=2); c.pen.poly([(936, 500), (960, 500), (960, 524)], fill=RED)
    tr = c.T('row')
    if c.on(tr):
        c.pen.text(100, 680, 'chunked', 'intx', 30, GRN, 'lm')
        for k in range(9):
            if c.on(tr + k * 0.08): c.pen.rect(100 + k * 96, 710, 180 + k * 96, 780, fill=YEL, outline=INK, w=2)
    tg = c.T('gaps')
    if c.on(tg):
        c.pen.rect(180 + 3 * 96, 700, 196 + 3 * 96, 790, fill=GRN)
        txt(c, 540, 880, 'taps land in the gaps', tg, 'intx', 40, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 40, 460, 1040, 620, ['await Promise.resolve(); // yields to the browser?'], c.T('resolve') - 0.4, 0.1, 30, 'process.js')
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 720, tn, 110, RED)
    tm = c.T('microtask')
    if c.on(tm): label(c, 540, 860, "it's a microtask: runs before render + input (S1 · E16)", tm, YEL, INK, 28)
    ts = c.T('still')
    if c.on(ts): stamp(c.cv, 540, 1010, 'STILL ONE LONG TASK', 64, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')

SCENES = [
    (hook, "You need to process ten thousand records on the main thread. Back in season one, you learned to split long tasks. But how big should each chunk be? And how do you hand control back?"),
    (slices, "Slice by time, not by item count. Process items until about ten milliseconds have passed, then yield, and reset the deadline. Fast phones do more per slice, slow ones do less, and input always gets a turn."),
    (lawn, "It's like mowing a lawn in strips. After each strip, you check if someone's at the door. You don't finish the whole lawn first."),
    (yield_, "Why scheduler dot yield? It hands control back, then your work continues near the front of the queue. setTimeout sends you to the back of the line, behind everything else."),
    (posttask, "For background jobs, scheduler dot postTask takes a priority: user blocking, user visible, or background."),
    (proof, "In the Performance panel, a chunked job is a row of small tasks with gaps, instead of one long block with a red corner. Taps land in the gaps."),
    (gotcha, "Interview trap: does await Promise dot resolve yield to the browser? No. It's a microtask, so it runs before the browser can render, or handle input. Your long task is still one long task."),
    (scene_next('S3 · E31', 'PERFORMANCE BUDGETS', 'stop regressions before they ship', 'budgets', 'regressions'),
     "Next: performance budgets, and how to stop regressions before they ship. Comment NOTES for the cheat sheet."),
]
