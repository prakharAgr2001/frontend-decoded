from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E31', tag='S3 · E31', short='PERFORMANCE BUDGETS', hook='stop regressions before ship')

def hook(c):
    tl = c.T('launch')
    if c.on(tl):
        pts = []
        n = int(52 * c.P(tl, 3.0, lambda x: x))
        for k in range(n + 1):
            pts.append((120 + k * 16, 950 - k * 7 - 20 * math.sin(k * 0.9)))
        c.pen.line([(110, 980), (980, 980)], INK, 4); c.pen.line([(110, 980), (110, 520)], INK, 4)
        if len(pts) > 1: c.pen.line(pts, RED, 6)
        c.pen.text(120, 1020, 'launch', 'ints', 28, INK, 'lm'); c.pen.text(980, 1020, '+1 year', 'ints', 28, INK, 'rm')
        c.pen.text(130, 500, 'load time', 'ints', 28, MUTE, 'lm')
    tt = c.T('twice')
    if c.on(tt): stamp(c.cv, 720, 620, '2X SLOWER', 64, c.P(tt, 0.35), -4, RED); c.sfx(tt, 'thud')
    tf = c.T('Fifty')
    if c.on(tf): label(c, 540, 1140, '50 small changes · a few KB each', tf, YEL, INK, 34)

def define(c):
    title(c, 'PERFORMANCE BUDGET', 330, c.T('budget'), 96, hlcol=YEL)
    tl = c.T('limit')
    if c.on(tl): txt(c, 540, 450, 'a limit your team agrees not to cross', tl, 'intx', 38, INK)
    for k, (kw, nm, v, frac) in enumerate((('JavaScript', 'JS (compressed)', '≤ 170 KB', 0.82), ('LCP', 'LCP', '≤ 2.5 s', 0.7), ('Total', 'TBT', '≤ 200 ms', 0.55))):
        t = c.T(kw); y = 600 + k * 170
        if not c.on(t): continue
        timerbar(c, 140, y, 940, frac, t, nm, GRN, 50, v)
        c.pen.line([(140 + 800 * 0.9, y - 10), (140 + 800 * 0.9, y + 60)], RED, 5)

def spend(c):
    title(c, 'A MONTHLY BUDGET', 330, 0.1, 100)
    tc = c.T('coffee')
    if c.on(tc):
        for k in range(18):
            t = tc + k * 0.12
            if c.on(t): c.pen.rr(140 + (k % 9) * 92, 480 + (k // 9) * 110, 210 + (k % 9) * 92, 570 + (k // 9) * 110, 10, fill=(170, 110, 60), outline=INK, w=3)
    ta = c.T('add')
    if c.on(ta):
        timerbar(c, 140, 820, 940, 1.0, ta, 'this month', RED, 60, 'over budget')
    te = c.T('end')
    if c.on(te): txt(c, 540, 1000, 'you only notice at the end of the month', te, 'intx', 36, INK)

def kinds(c):
    title(c, '3 KINDS OF BUDGET', 330, c.T('three'), 96)
    rows(c, 90, 520, [('Quantity', 'quantity', 'KB of JS · images · request count', BLUE), ('Milestone', 'milestone timings', 'LCP · TBT · INP', PURPLE),
                      ('rule', 'rule-based', 'e.g. Lighthouse score ≥ 90', ORANGE)], 190, 900, 150, 42, 30)

def enforce(c):
    title(c, 'ENFORCE IT IN CI', 330, c.T('enforced'), 100, hlcol=YEL)
    code(c, 40, 430, 1040, 910, ['"assertions": {', '  "largest-contentful-paint":', '      ["error", { "maxNumericValue": 2500 }],',
                                 '  "total-blocking-time":', '      ["error", { "maxNumericValue": 200 }],', '  "resource-summary:script:size":',
                                 '      ["error", { "maxNumericValue": 170000 }]', '}'], c.T('Lighthouse') - 0.4, 0.1, 24, 'lighthouserc.json', lang='json')
    tp = c.T('pull')
    if c.on(tp): chips(c, 140, 990, [('Lighthouse CI', (200, 220, 255)), ('size-limit', (255, 238, 170))], tp - 0.6, 0.3, 34)
    tf = c.T('fail')
    if c.on(tf): label(c, 540, 1120, 'budget crossed → build fails', tf, (255, 210, 210), INK, 34)

def proof(c):
    card(c.pen, 70, 340, 1010, 1060, 24, WHITE, 12, 5)
    c.pen.text(110, 400, 'Add product carousel  #482', 'intx', 36, INK, 'lm')
    tc = c.T('check')
    rows_ = [('size-limit · main.js', '172.4 KB / 170 KB', RED), ('lighthouse-ci · LCP', '2.31 s / 2.5 s', GRN), ('lighthouse-ci · TBT', '248 ms / 200 ms', RED)]
    for k, (nm, v, col) in enumerate(rows_):
        t = tc + k * 0.3
        if not c.on(t): continue
        y = 520 + k * 110; c.sfx(t, 'tick')
        (cross if col == RED else check)(c.pen, 140, y, 0.9, col, 8, c.P(t, 0.3))
        c.pen.text(190, y, nm, 'ints', 30, INK, 'lm'); c.pen.text(970, y, v, 'monob', 28, col, 'rm')
    te = c.T('exact')
    if c.on(te): pill(c.pen, 540, 900, 'All checks have failed', c.B(te, 0.35), (255, 210, 210), RED, 32)
    tu = c.T('before')
    if c.on(tu): txt(c, 540, 1140, 'fixed before a single user feels it', tu, 'intx', 38, GRN)

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, 'How do you pick the numbers?', c.T('pick'), 'intx', 48, INK)
    rows(c, 90, 620, [('current', 'start from current field data', None, 'ok'), ('slightly', 'set it slightly better than today', None, 'ok'),
                      ('ratchet', 'ratchet it down over time', None, 'ok'), ('phone', 'test on a real mid-range phone', None, 'ok')], 130, 900, 104, 36)

SCENES = [
    (hook, "Your app was fast at launch. A year later, it's twice as slow. No single change did it. Fifty small ones did, each adding just a few kilobytes."),
    (define, "A performance budget is a limit your team agrees not to cross. For example: JavaScript under a hundred and seventy kilobytes, compressed. LCP under two and a half seconds. Total Blocking Time under two hundred milliseconds."),
    (spend, "It's like a monthly spending budget. No single coffee breaks the bank. But small spends add up, and without a limit, you only notice at the end of the month."),
    (kinds, "Budgets come in three kinds. Quantity: kilobytes and request counts. Milestone timings, like LCP and TBT. And rule based ones, like a minimum Lighthouse score."),
    (enforce, "Budgets only work when they're enforced automatically. Run Lighthouse CI, or size limit, on every pull request, and fail the build when a budget is crossed."),
    (proof, "On the pull request, the check turns red, with the exact metric and how far over it went. It gets fixed before a single user feels it."),
    (gotcha, "Interview question: how do you pick the numbers? Not from thin air. Start from your current field data. Set budgets slightly better than today, and ratchet them down over time. And measure on a real mid range phone, not your laptop."),
    (scene_next('S3 · E32', 'IQ: RUNTIME', 'four questions on runtime performance', 'questions', 'runtime'),
     "Next: four interview questions on runtime performance. Comment NOTES for the cheat sheet."),
]
