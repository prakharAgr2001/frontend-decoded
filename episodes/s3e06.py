from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E06', tag='S3 · E06', short='TTFB · FCP · TBT', hook='the metrics behind the vitals')

def hook(c):
    ts = c.T('spotlight')
    for k, (ab, col) in enumerate((('LCP', BLUE), ('INP', PURPLE), ('CLS', ORANGE))):
        t = ts + k * 0.15
        if not c.on(t): continue
        x = 220 + k * 320
        c.pen.poly([(x - 30, 330), (x + 30, 330), (x + 140, 700), (x - 140, 700)], fill=(255, 238, 170))
        pill(c.pen, x, 640, ab, c.B(t, 0.35), col, WHITE, 52, outline=INK)
    tw = c.T('why')
    for k, ab in enumerate(('TTFB', 'FCP', 'TBT')):
        t = c.T('three') + k * 0.2
        if c.on(t): pill(c.pen, 220 + k * 320, 900, ab, c.B(t, 0.35), WHITE, INK, 40)
    if c.on(tw): stamp(c.cv, 540, 1110, 'THE WHY', 80, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')

def timeline(c):
    title(c, 'FIRST BYTE TO FIRST PAINT', 330, 0.1, 76)
    tt = c.T('Time')
    axis(c, 110, 970, 700, tt, [(0.15, 'TTFB', c.T('byte'), BLUE), (0.48, 'FCP', c.T('anything'), TEAL), (0.85, 'LCP', c.T('main'), GRN)])
    for kw, x, s in (('byte', 110 + 860 * 0.15, 'good ≤ 0.8 s'), ('anything', 110 + 860 * 0.48, 'good ≤ 1.8 s'), ('main', 110 + 860 * 0.85, 'good ≤ 2.5 s')):
        txt(c, x, 790, s, c.T(kw) + 0.3, 'ints', 28, MUTE)
    ta = c.T('anything')
    if c.on(ta):
        card(c.pen, 380, 880, 700, 1180, 20, WHITE, 8, 4)
        c.pen.rr(410, 920, 560, 960, 8, fill=INK)
        if c.on(c.T('main')): c.pen.rect(410, 990, 670, 1150, fill=(120, 170, 210))

def cinema(c):
    title(c, 'A NIGHT AT THE MOVIES', 330, 0.1, 84)
    for k, (kw, lab, ab, col) in enumerate((('doors', 'doors open', 'TTFB', BLUE), ('trailers', 'trailers start', 'FCP', TEAL), ('film', 'your film starts', 'LCP', GRN))):
        t = c.T(kw); y = 520 + k * 250
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        card(c.pen, 110, y - 95 * s, 970, y + 95 * s, 22, WHITE, 10, 5)
        c.pen.rr(140, y - 65 * s, 340, y + 65 * s, 14, fill=DARK)
        if k: c.pen.rect(160, y - 45 * s, 320, y + 45 * s, fill=(255, 238, 170) if k == 1 else (120, 170, 210))
        else: c.pen.rect(230, y - 65 * s, 250, y + 65 * s, fill=YEL)
        c.pen.text(380, y, lab, 'intx', 44 * s, INK, 'lm')
        pill(c.pen, 860, y, ab, s, col, WHITE, 36, outline=INK)

def ttfb(c):
    title(c, 'SLOW TTFB DELAYS EVERYTHING', 330, c.T('slow'), 70, hlcol=(255, 180, 180))
    a = node(c, 200, 640, 220, 160, 'Browser', 0.0, 'laptop')
    b = node(c, 880, 640, 220, 160, 'Server', 0.0, 'server')
    for k, (kw, lab) in enumerate((('server', 'slow DB / render'), ('network', 'long distance'), ('redirects', '301 → 302 → 200'))):
        t = c.T(kw)
        if c.on(t): pill(c.pen, 540, 820 + k * 80, lab, c.B(t, 0.35), (255, 225, 225), INK, 30)
    packet(c, b, a, c.T('waits') - 0.5, c.T('waits') + 1.2, YEL, '1st byte')
    tf = c.T('CDNs')
    if c.on(tf): rows(c, 140, 1110, [(tf, 'CDN · caching · fewer redirects', None, 'ok')], 120, 800, 100, 36)

def tbt(c):
    title(c, 'TOTAL BLOCKING TIME', 330, c.T('Total'), 92, hlcol=YEL)
    tasks = [(0.0, 0.07), (0.1, 0.14), (0.3, 0.04), (0.38, 0.09), (0.55, 0.2), (0.8, 0.05)]
    tl = c.T('long')
    for k, (s, d) in enumerate(tasks):
        t = tl + k * 0.12
        if not c.on(t): continue
        xa = 110 + 860 * s; xb = xa + 860 * d * c.P(t, 0.3)
        c.pen.rect(xa, 520, xb, 620, fill=(200, 200, 205), outline=INK, w=3)
        if d > 0.05 and c.on(c.T('beyond')):
            x50 = xa + 860 * 0.05
            c.pen.rect(x50, 520, xb, 620, fill=RED, outline=INK, w=3)
    tb = c.T('beyond')
    if c.on(tb):
        txt(c, 540, 690, 'red = time past 50 ms per task', tb, 'ints', 32, RED)
        x = 300
        for k, d in enumerate([0.09, 0.04, 0.15]):
            w = 860 * d * c.P(tb + 0.6 + k * 0.2, 0.3); c.pen.rect(x, 800, x + w, 880, fill=RED, outline=INK, w=3); x += 860 * d
        c.pen.text(270, 840, 'TBT =', 'intx', 40, INK, 'rm')
    ti = c.T('interactive')
    if c.on(ti): axis(c, 110, 970, 1050, ti, [(0.0, 'FCP', ti, TEAL), (0.85, 'interactive', ti + 0.2, GRN)])

def standin(c):
    tl = c.T('Lighthouse')
    node(c, 300, 560, 300, 200, 'Lighthouse', tl, 'cpu')
    tt = c.T('tap')
    if c.on(tt): person(c.pen, 760, 660, 1.4, BLUE); cross(c.pen, 760, 470, 1.6, RED, 12, c.P(c.T('measure'), 0.35))
    ts = c.T('stand')
    if c.on(ts):
        card(c.pen, 140, 820, 940, 1000, 24, YEL, 10, 5)
        c.pen.text(540, 910, 'TBT  ≈  lab stand-in for INP', 'intx', 46 * c.B(ts, 0.35), INK)
    th = c.T('high')
    if c.on(th): txt(c, 540, 1100, 'high TBT usually means a bad INP', th, 'ints', 36, RED)

def proof(c):
    box = panel(c, 60, 330, 1020, 1200, tabs=('Elements', 'Lighthouse'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('report')
    if c.on(tr):
        ring(c, 540, 560, 100, 0.62 * c.P(tr, 0.8), ORANGE, 18, (60, 66, 76))
        c.pen.text(540, 560, str(int(62 * c.P(tr, 0.8))), 'osw', 80, ORANGE)
    items = [('First Contentful Paint', '1.4 s', 'FCP', '10%', GRN), ('Largest Contentful Paint', '3.2 s', 'LCP', '25%', ORANGE),
             ('Total Blocking Time', '640 ms', 'TBT', '30%', RED), ('Cumulative Layout Shift', '0.02', 'CLS', '25%', GRN), ('Speed Index', '2.9 s', 'Speed', '10%', ORANGE)]
    for k, (nm, v, kw, wt, col) in enumerate(items):
        t = c.T(kw)
        if not c.on(t): continue
        y = 740 + k * 80; c.sfx(t, 'tick')
        c.pen.circ(120, y, 12, fill=col)
        c.pen.text(150, y, nm, 'ints', 30, WHITE, 'lm'); c.pen.text(820, y, v, 'monob', 30, col, 'rm')
        if c.on(c.T('weight')): c.pen.text(960, y, wt, 'monob', 28, YEL if kw == 'TBT' else (150, 156, 166), 'rm')
    tw = c.T('weight')
    if c.on(tw): c.pen.rect(100, 900 - 34, 990, 900 + 34, outline=YEL, w=4)

def puzzle(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    tt = c.T('three')
    for k, (ms, kw) in enumerate(((70, 'seventy'), (140, 'hundred'), (40, 'forty'))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 520 + k * 130; w = ms * 4.5 * c.P(t, 0.4)
        c.pen.rect(140, y, 140 + w, y + 90, fill=(200, 200, 205), outline=INK, w=3)
        c.pen.text(140 + ms * 4.5 + 20, y + 45, f'{ms} ms', 'intx', 36, INK, 'lm')
        ta = c.T('Twenty')
        if c.on(ta) and ms > 50:
            c.pen.rect(140 + 50 * 4.5, y, 140 + ms * 4.5, y + 90, fill=RED, outline=INK, w=3)
            c.pen.text(140 + ms * 4.5 + 180, y + 45, f'+{ms - 50}', 'intx', 36, RED, 'lm')
    if c.on(tt): c.pen.line([(140 + 225, 490), (140 + 225, 920)], INK, 4)
    ta = c.T('Twenty')
    tq = c.T('TBT') + 0.6
    if tq <= c.t < ta:
        f = lin(c.t, tq, ta - 0.1); ring(c, 540, 1080, 80, f, YEL, 16)
        c.pen.text(540, 1080, str(max(1, 3 - int(f * 3))), 'osw', 80, INK)
        for k in range(3): c.sfx(tq + k * (ta - tq) / 3, 'tick')
    to = c.T('ten')
    if c.on(to):
        c.sfx(to, 'ding'); card(c.pen, 160, 1000, 920, 1160, 24, (255, 246, 214), 10, 5)
        c.pen.text(540, 1080, 'TBT = 20 + 90 + 0 = 110 ms', 'intx', 48 * c.B(to, 0.35), INK)

SCENES = [
    (hook, "LCP, INP and CLS get the spotlight. But when they're bad, three supporting metrics tell you why."),
    (timeline, "Time to First Byte, or TTFB: how long until the first byte of HTML arrives. First Contentful Paint, or FCP: when anything at all, text or an image, first appears. Then LCP, when the main content lands."),
    (cinema, "It's like a night at the movies. The doors open: that's TTFB. The trailers light up the screen: FCP. The film you came for starts: LCP."),
    (ttfb, "A slow TTFB means a slow server, a long network trip, or a chain of redirects, and every other metric waits for it. CDNs, caching and fewer redirects all help."),
    (tbt, "Total Blocking Time, or TBT, adds up the blocking part of every long task: the time beyond fifty milliseconds, between first paint and when the page is reliably interactive."),
    (standin, "Why does it exist? Lighthouse can't tap your page like a real person, so it can't measure INP. TBT is its stand in. A high TBT usually means a bad INP."),
    (proof, "Run Lighthouse in DevTools. The report shows FCP, LCP, TBT, CLS and Speed Index. And TBT carries the most weight in the score."),
    (puzzle, "Interview question. Three tasks run for seventy, a hundred and forty, and forty milliseconds. What's the TBT? [[3]] Twenty, plus ninety, plus zero: one hundred and ten milliseconds."),
    (scene_next('S3 · E07', 'LAB vs FIELD', 'why Lighthouse 100 can still fail', 'lab', 'fail'),
     "Next: lab versus field data, and why a Lighthouse score of one hundred can still fail. Comment NOTES for the cheat sheet."),
]
