from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E07', tag='S3 · E07', short='LAB vs FIELD', hook='why Lighthouse 100 still fails')

def hook(c):
    tl = c.T('Lighthouse')
    if c.on(tl):
        card(c.pen, 90, 360, 510, 820, 26, DARK, 10, 5)
        ring(c, 300, 560, 120, c.P(tl, 0.8), GRN, 20, (60, 66, 76))
        c.pen.text(300, 560, str(int(100 * c.P(tl, 0.8))), 'osw', 100, GRN)
        c.pen.text(300, 760, 'Lighthouse', 'int', 32, WHITE)
    ts = c.T('Search')
    if c.on(ts):
        card(c.pen, 570, 360, 990, 820, 26, WHITE, 10, 5)
        c.pen.text(780, 430, 'Core Web Vitals', 'intx', 34, INK)
        for k, (nm, col) in enumerate((('Poor URLs  · 412', RED), ('Need improvement · 96', ORANGE), ('Good · 18', GRN))):
            y = 500 + k * 80; p = c.P(ts + 0.2 + k * 0.15, 0.3)
            c.pen.rect(610, y, 610 + 340 * p * (1 - k * 0.3), y + 50, fill=col)
            c.pen.text(620, y + 25, nm, 'int', 24, WHITE, 'lm')
        c.pen.text(780, 760, 'Search Console', 'int', 30, INK)
    tt = c.T('truth')
    if c.on(tt): stamp(c.cv, 540, 1000, 'BOTH ARE RIGHT', 76, c.P(tt, 0.35), -3, RED); c.sfx(tt, 'thud')

def lab(c):
    title(c, 'LAB DATA', 330, c.T('lab'), 120, hlcol=(200, 220, 255))
    rows(c, 110, 500, [('One', 'one run', None, BLUE), ('simulated', 'simulated mid-range phone', None, BLUE),
                      ('throttled', 'throttled network', None, BLUE), ('clean', 'clean browser, no extensions', None, BLUE)], 130, 860, 100, 38)
    td = c.T('debugging')
    if c.on(td): label(c, 540, 1100, 'repeatable · perfect for debugging', td, YEL, INK, 34)

def field(c):
    title(c, 'FIELD DATA', 330, c.T('Field'), 120, hlcol=(200, 240, 200))
    tr = c.T('real')
    if c.on(tr):
        for k in range(12):
            t = tr + k * 0.06
            if c.on(t):
                x = 150 + (k % 6) * 155; y = 640 + (k // 6) * 230
                icon(c.pen, ['phone', 'laptop', 'phone'][k % 3], x, y, 0.9 * c.B(t, 0.3), INK, [WHITE, (255, 230, 200), (220, 230, 250)][k % 3])
    tc = c.T('Chrome', 1)
    if c.on(tc): label(c, 540, 470, 'Chrome UX Report (CrUX)', tc, YEL, INK, 34)
    for k, (kw, s) in enumerate((('twenty', 'last 28 days'), ('seventy', 'at p75'), ('everything', 'cheap phones · busy networks · extensions'))):
        t = c.T(kw)
        if c.on(t): pill(c.pen, 540, 1060 + k * 80, s, c.B(t, 0.35), WHITE, INK, 30)

def drive(c):
    for j, (lab_, kw, sub) in enumerate((('TEST DRIVE', 'track', 'empty track'), ('REAL COMMUTE', 'commutes', 'traffic · potholes'))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 520 + j * 400; s = c.B(t, 0.4); c.sfx(t, 'pop')
        card(c.pen, 110, y - 150 * s, 970, y + 150 * s, 26, WHITE, 10, 5)
        c.pen.text(150, y - 100, lab_, 'osw', 54 * s, INK, 'lm')
        c.pen.rect(150, y - 20, 930, y + 80, fill=(90, 90, 96))
        for k in range(8): c.pen.rect(170 + k * 100, y + 26, 220 + k * 100, y + 34, fill=WHITE)
        cx = 200 + ((c.t - t) * 220) % 700 if j == 0 else 200 + ((c.t - t) * 80) % 700
        c.pen.rr(cx, y - 10, cx + 110, y + 50, 14, fill=BLUE if j == 0 else ORANGE, outline=INK, w=3)
        if j:
            for k in range(3): c.pen.rr(360 + k * 200, y - 10, 460 + k * 200, y + 50, 14, fill=GREY, outline=INK, w=3)
            c.pen.ell(300, y + 52, 360, y + 72, fill=INK)
        c.pen.text(930, y - 100, sub, 'ints', 30 * s, MUTE, 'rm')
    tu = c.T('users')
    if c.on(tu): txt(c, 540, 1230, 'your users drive on the real roads', tu, 'intx', 38, INK)

def differ(c):
    title(c, 'WHY THEY DISAGREE', 330, c.T('disagree'), 96)
    rows(c, 90, 500, [('click', "lab can't click", 'so no INP', 'no'), ('first', 'loads only the first screen', 'misses shifts while scrolling', 'no'),
                      ('device', 'one device', 'your users have hundreds', 'no')], 190, 900, 150, 40, 30)

def rum(c):
    title(c, 'MEASURE REAL USERS', 330, c.T('real'), 90, hlcol=YEL)
    code(c, 50, 450, 1030, 900, ["import { onLCP, onINP, onCLS } from 'web-vitals';", '', 'function send(m) {',
                                 "  navigator.sendBeacon('/rum', JSON.stringify(m));", '}', 'onLCP(send); onINP(send); onCLS(send);'],
         c.T('library') - 0.4, 0.15, 25, 'rum.js', marks=[(0, c.T('library'), YEL), (5, c.T('few'), YEL)])
    tr = c.T('reports')
    if c.on(tr): label(c, 540, 1000, 'RUM = real user monitoring', tr, WHITE, INK, 34)

def proof(c):
    box = browser(c, 70, 320, 1010, 1250, url='pagespeed.web.dev', dy=(1 - c.P(0, 0.45)) * 900)
    tt = c.T('top')
    if c.on(tt):
        c.pen.rect(100, 410, 980, 760, fill=(225, 245, 225), outline=GRN, w=4)
        c.pen.text(130, 450, 'Discover what your real users are experiencing', 'intx', 28, INK, 'lm')
        c.pen.text(130, 500, 'FIELD · CrUX · 28 days', 'monob', 26, GRN, 'lm')
        for k, (ab, v, col) in enumerate((('LCP', '3.4 s', ORANGE), ('INP', '280 ms', ORANGE), ('CLS', '0.21', RED))):
            c.pen.text(200 + k * 290, 620, ab, 'osw', 50, INK); c.pen.text(200 + k * 290, 690, v, 'intx', 40, col)
    tb = c.T('bottom')
    if c.on(tb):
        c.pen.rect(100, 800, 980, 1200, fill=(225, 235, 255), outline=BLUE, w=4)
        c.pen.text(130, 840, 'Diagnose performance issues', 'intx', 28, INK, 'lm')
        c.pen.text(130, 890, 'LAB · Lighthouse · one run', 'monob', 26, BLUE, 'lm')
        ring(c, 540, 1050, 90, 0.97 * c.P(tb, 0.6), GRN, 16); c.pen.text(540, 1050, str(int(97 * c.P(tb, 0.6))), 'osw', 70, GRN)
    tf = c.T('trust')
    if c.on(tf): label(c, 540, 1300, 'trust the field · debug in the lab', tf, YEL, INK, 34)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Fix shipped today. Why is field data still red?', c.T('shipped'), 'intx', 38, INK)
    tw = c.T('rolling')
    if c.on(tw):
        for d in range(28):
            x = 110 + (d % 14) * 62; y = 620 + (d // 14) * 90
            fixed = d >= 26
            c.pen.rr(x, y, x + 52, y + 70, 8, fill=GRN if fixed else (240, 170, 170), outline=INK, w=3)
        txt(c, 540, 860, '28-day window: 2 good days, 26 old ones', tw + 0.3, 'ints', 32, INK)
    tf = c.T('weeks')
    if c.on(tf): stamp(c.cv, 540, 1020, 'FADES IN OVER WEEKS', 64, c.P(tf, 0.35), -3, GRN); c.sfx(tf, 'thud')

SCENES = [
    (hook, "Your Lighthouse score is a perfect one hundred. Then Search Console says your pages fail Core Web Vitals. They're both telling the truth."),
    (lab, "Lighthouse is lab data. One run, on a simulated mid range phone, with a throttled network, in a clean browser. It's repeatable, and perfect for debugging."),
    (field, "Field data comes from real users. The Chrome UX Report collects it from Chrome users who opt in, over the last twenty eight days, at the seventy fifth percentile. Cheap phones, busy networks, extensions, everything."),
    (drive, "Lab data is a test drive on an empty track. Field data is a month of real commutes, in traffic, over potholes. Your users drive on the real roads."),
    (differ, "So they disagree, for good reasons. The lab can't click, so it has no INP. It loads only the first screen, so it misses shifts while you scroll. And it tests one device, while your users have hundreds."),
    (rum, "To see your own real user data, add monitoring. Google's web vitals library reports each metric from real visits, in a few lines."),
    (proof, "PageSpeed Insights shows both on one page. The top is field data from real users. The bottom is a Lighthouse lab run. When they disagree, trust the field, and debug in the lab."),
    (gotcha, "Interview trap: you shipped a fix today, so why is the field data still red? Because CrUX is a twenty eight day rolling window. Your fix fades in over weeks, not hours."),
    (scene_next('S3 · E08', 'IQ: METRICS', 'four questions on web vitals', 'questions', 'vitals'),
     "Next: four interview questions on web vitals. Pause and answer each one. Comment NOTES for the cheat sheet."),
]
