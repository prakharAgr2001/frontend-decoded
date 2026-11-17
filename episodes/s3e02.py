from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E02', tag='S3 · E02', short='CORE WEB VITALS')

VITALS = [('LCP', 'Largest Contentful Paint', 'loading', BLUE), ('INP', 'Interaction to Next Paint', 'responsiveness', PURPLE),
          ('CLS', 'Cumulative Layout Shift', 'visual stability', ORANGE)]

def hook(c):
    tl = c.T('looks')
    browser(c, 110, 360, 970, 760, url='your-site.com', dy=(1 - c.P(0, 0.45)) * 900)
    if c.on(tl):
        for k in range(3): c.pen.rr(160 + k * 270, 480, 380 + k * 270, 700, 14, fill=[LIGHT, (255, 235, 200), (220, 230, 250)][k])
        cross(c.pen, 540, 590, 2.4, RED, 14, c.P(c.T('grades'), 0.4))
    tn = c.T('three')
    if c.on(tn):
        card(c.pen, 200, 860, 880, 1180, 26, WHITE, 12, 5)
        c.pen.text(540, 910, 'REPORT CARD', 'osw', 44, INK)
        for k, (ab, *_r) in enumerate(VITALS):
            t = tn + 0.2 + k * 0.25
            if c.on(t): c.sfx(t, 'pop'); pill(c.pen, 330 + k * 210, 1030, ab + '  ?', c.B(t, 0.3), YEL, INK, 36)
    tr = c.T('real')
    if c.on(tr): txt(c, 540, 1120, 'from real Chrome users', tr, 'ints', 32, MUTE)

def three(c):
    title(c, 'CORE WEB VITALS', 330, c.T('called'), 104, hlcol=YEL)
    kws = ['Largest', 'Interaction', 'Cumulative']; subs = ['how fast the main content appears', 'how fast the page responds', 'how much things jump around']
    for k, (ab, full, kind, col) in enumerate(VITALS):
        t = c.T(kws[k]); y = 540 + k * 260
        if not c.on(t - 0.01): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        card(c.pen, 90, y - 100 * s, 990, y + 100 * s, 24, WHITE, 10, 5)
        c.pen.rr(120, y - 70 * s, 330, y + 70 * s, 18, fill=col, outline=INK, w=4)
        c.pen.text(225, y, ab, 'osw', 70 * s, WHITE)
        c.pen.text(370, y - 36, full, 'intx', 36 * s, INK, 'lm')
        c.pen.text(370, y + 14, kind, 'ints', 30 * s, col, 'lm')
        c.pen.text(370, y + 56, subs[k], 'intm', 26 * s, MUTE, 'lm')

def dash(c):
    title(c, 'A DASHBOARD, NOT 50 GAUGES', 330, c.T('dashboard'), 70)
    for k, (kw, nm, f) in enumerate((('speed', 'SPEED', 0.3), ('fuel', 'FUEL', 0.55), ('temperature', 'TEMP', 0.85))):
        gauge(c, 210 + k * 330, 700, 130, f, c.T(kw), nm, '')
    tt = c.T('three', 1)
    if c.on(tt):
        for k, (ab, *_r, col) in enumerate(VITALS): pill(c.pen, 210 + k * 330, 960, ab, c.B(tt + k * 0.15, 0.35), col, WHITE, 44)
        txt(c, 540, 1080, 'three dials that tell you something is wrong', tt + 0.6, 'ints', 34, INK)

def marks(c):
    title(c, 'THE PASS MARKS', 330, c.T('pass'), 100)
    for k, (kw, ab, th, col) in enumerate((('two', 'LCP', '≤ 2.5 s', BLUE), ('hundred', 'INP', '≤ 200 ms', PURPLE), ('zero', 'CLS', '≤ 0.1', ORANGE))):
        t = c.T(kw); y = 530 + k * 220
        if not c.on(t - 0.01): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        card(c.pen, 140, y - 85 * s, 940, y + 85 * s, 24, WHITE, 10, 5)
        c.pen.text(200, y, ab, 'osw', 80 * s, col, 'lm')
        c.pen.text(880, y, th, 'intx', 72 * s, INK, 'rm')
    tb = c.T('below')
    if c.on(tb): label(c, 540, 1230, 'green = good · orange = needs improvement · red = poor', tb + 0.6, WHITE, INK, 26)

def p75(c):
    title(c, 'GRADED AT p75', 330, c.T('seventy'), 104, hlcol=YEL)
    tt = c.T('three', 1)
    for k in range(4):
        x = 210 + k * 220; ok = k < 3
        if not c.on(tt + k * 0.2): continue
        s = c.B(tt + k * 0.2, 0.35); c.sfx(tt + k * 0.2, 'pop')
        person(c.pen, x, 820, 1.4 * s, GRN if ok else RED)
        (check if ok else cross)(c.pen, x, 900, 1.0, GRN if ok else RED, 9, c.P(tt + k * 0.2 + 0.2, 0.3))
    td = c.T('separately')
    if c.on(td):
        icon(c.pen, 'phone', 380, 1100, 1.0 * c.B(td, 0.4)); icon(c.pen, 'laptop', 700, 1100, 1.0 * c.B(td + 0.15, 0.4))
        txt(c, 540, 1220, 'mobile and desktop graded separately', td + 0.3, 'ints', 32, INK)

def proof(c):
    box = browser(c, 70, 320, 1010, 1260, url='pagespeed.web.dev', dy=(1 - c.P(0, 0.45)) * 900)
    tp = c.T('PageSpeed')
    if c.on(tp): addressbar(c, 110, 420, 970, typed_text(c, 'your-site.com', tp, 0.06), False, 36, 80)
    tu = c.T('Chrome')
    if c.on(tu):
        c.pen.text(120, 560, 'Discover what your real users are experiencing', 'intx', 30, INK, 'lm')
        txt(c, 120, 605, 'Chrome UX Report · last 28 days', tu, 'intm', 26, MUTE, 'lm')
    tg = c.T('marked')
    vals = [('Largest Contentful Paint (LCP)', '2.1 s', GRN), ('Interaction to Next Paint (INP)', '310 ms', ORANGE), ('Cumulative Layout Shift (CLS)', '0.04', GRN)]
    for k, (nm, v, col) in enumerate(vals):
        t = tg + k * 0.35
        if not c.on(t): continue
        y = 700 + k * 130; c.sfx(t, 'tick'); p = c.P(t, 0.3)
        c.pen.circ(140, y, 14, fill=col)
        c.pen.text(170, y, nm, 'ints', 30, mix(WHITE, INK, p), 'lm')
        c.pen.text(950, y, v, 'intx', 44, mix(WHITE, col, p), 'rm')
        c.pen.rect(170, y + 40, 950, y + 52, fill=LIGHT)
        c.pen.rect(170, y + 40, 170 + 780 * (0.72 if col == GRN else 0.5), y + 52, fill=col)
    tpoor = c.T('poor')
    if c.on(tg + 1.3): stamp(c.cv, 540, 1150, 'ASSESSMENT: FAILED', 52, c.P(tg + 1.3, 0.35), -3, RED); c.sfx(tg + 1.3, 'thud')

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, 'What happened to First Input Delay?', c.T('happened'), 'intx', 44, INK)
    tm = c.T('March')
    if c.on(tm):
        card(c.pen, 90, 580, 510, 960, 24, LIGHT, 10, 5)
        c.pen.text(300, 660, 'FID', 'osw', 110, GREY)
        c.pen.text(300, 760, 'delay before the first', 'ints', 28, INK); c.pen.text(300, 800, "handler starts", 'ints', 28, INK)
        cross(c.pen, 300, 880, 1.6, RED, 12, c.P(c.T('replaced'), 0.4))
        card(c.pen, 570, 580, 990, 960, 24, (255, 246, 214), 10, 5)
        c.pen.text(780, 660, 'INP', 'osw', 110 * c.B(c.T('replaced'), 0.4), PURPLE)
    ti = c.T('whole')
    if c.on(ti):
        c.pen.text(780, 760, 'input → handler → paint', 'ints', 28, INK); c.pen.text(780, 800, 'for every interaction', 'ints', 28, INK)
        check(c.pen, 780, 880, 1.6, GRN, 12, c.P(c.T('every'), 0.4))
    label(c, 540, 1080, 'since March 2024', tm + 0.3, YEL, INK, 32)

SCENES = [
    (hook, "Google doesn't grade your website on how it looks. It grades it on three numbers, collected from real Chrome users visiting your pages."),
    (three, "They're called Core Web Vitals. Largest Contentful Paint, or LCP: how fast the main content appears. Interaction to Next Paint, or INP: how fast the page responds. And Cumulative Layout Shift, or CLS: how much things jump around."),
    (dash, "Think of a car's dashboard. One dial for speed, one for fuel, one for engine temperature. You don't need fifty gauges. Just three that tell you something is wrong."),
    (marks, "Each one has a pass mark. LCP within two point five seconds. INP within two hundred milliseconds. CLS at or below zero point one."),
    (p75, "And they're graded at the seventy fifth percentile. Your page passes only if three out of four visits hit the mark, with mobile and desktop judged separately."),
    (proof, "Check your own site. Paste a URL into PageSpeed Insights. The top section shows real user data from the Chrome UX Report, with each vital marked good, needs improvement, or poor."),
    (gotcha, "Interview question: what happened to First Input Delay? In March twenty twenty four, INP replaced it. FID only measured the wait before the first handler started. INP measures the whole response, input to paint, for every interaction."),
    (scene_next('S3 · E03', 'LCP', 'when does the page feel loaded?', 'LCP', 'loaded'),
     "Next: LCP, the moment your page actually feels loaded. Comment NOTES for the cheat sheet."),
]
