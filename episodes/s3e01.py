from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E01', tag='S3 · E01', short='100 ms = MONEY', hook='why 100 ms costs real money')

def hook(c):
    box = phone(c, 360, 700, 440, 760, url='shop.example.com', dy=(1 - c.P(0, 0.45)) * 900)
    tl = c.T('One')
    if c.on(tl):
        spinner(c, 360, 680, 50)
        counter(c, 360, 820, 0, 3.0, tl, c.T('Three'), '{:.1f}', 90, RED, ' s')
    tg = c.T('gone')
    if c.on(tg):
        for k in range(5):
            x = 140 + k * 200; q = c.P(tg + k * 0.12, 0.6)
            person(c.pen, x + q * 60, 1260, 0.8, mix(BLUE, GREY, q))
            if q > 0.3: cross(c.pen, x + 60, 1100, 0.7, RED, 7, c.P(tg + k * 0.12 + 0.2, 0.3))
    tf = c.T('fifty')
    if c.on(tf):
        card(c.pen, 630, 400, 1000, 640, 24, YEL, 10, 5)
        bignum(c, 815, 490, '53%', tf, 110, INK)
        txt(c, 815, 590, 'leave after 3 s', tf + 0.3, 'int', 28, INK)

def money(c):
    title(c, 'SPEED IS MONEY', 340, c.T('Speed'), 110, hlcol=YEL)
    ta = c.T('Amazon')
    if c.on(ta):
        card(c.pen, 110, 470, 970, 820, 28, WHITE, 12, 5)
        bignum(c, 330, 640, '+100 ms', c.T('hundred'), 96, INK, sound='pop')
        arrow(c.pen, 520, 640, 600, 640, c.P(c.T('cost'), 0.3), INK, 7)
        bignum(c, 780, 640, '−1%', c.T('one'), 120, RED)
        txt(c, 540, 770, 'of sales, in an often-quoted Amazon finding', c.T('sales'), 'intm', 30, MUTE)
    tb = c.T('blink')
    if c.on(tb):
        icon(c.pen, 'eye', 540, 1000, 1.6 * c.B(tb, 0.4))
        txt(c, 540, 1110, 'a blink ≈ 100–150 ms', tb + 0.2, 'int', 34, INK)

def thresholds(c):
    title(c, 'HOW TIME FEELS', 340, 0.1, 100)
    axis(c, 110, 970, 700, c.T('perceive'), [(0.06, '0.1 s', 'hundred', GRN), (0.42, '1 s', c.T('second', 2), YEL), (0.94, '10 s', 'ten', RED)])
    for kw, x, s1, col in (('instant', 160, 'instant', GRN), ('flow', 470, 'still in flow', ORANGE), ('attention', 920, 'attention gone', RED)):
        t = c.T(kw)
        if c.on(t): pill(c.pen, x if x < 900 else 860, 820, s1, c.B(t, 0.35), WHITE, col, 30)
    txt(c, 540, 980, 'response-time limits, Jakob Nielsen', c.T('attention') + 0.6, 'intm', 30, MUTE)

def lift(c):
    for j, (lbl, kw, disp) in enumerate((('no floor display', 'lift', False), ('shows progress', 'Show', True))):
        t = c.T(kw)
        if not c.on(t - 0.01): continue
        x0 = 100 + j * 460; s = c.B(t, 0.4); c.sfx(t, 'pop')
        card(c.pen, x0, 420, x0 + 420, 980, 24, LIGHT, 10, 5)
        c.pen.rect(x0 + 60, 560, x0 + 205, 940, fill=(205, 200, 190), outline=INK, w=4)
        c.pen.rect(x0 + 215, 560, x0 + 360, 940, fill=(205, 200, 190), outline=INK, w=4)
        c.pen.rr(x0 + 120, 450, x0 + 300, 530, 12, fill=DARK)
        if disp:
            fl = 1 + int((c.t - t) * 2) % 9
            c.pen.text(x0 + 210, 490, f'↓ {10 - fl}', 'intx', 40, YEL)
        else:
            c.pen.text(x0 + 210, 490, '—', 'intx', 40, (90, 90, 90))
        c.pen.text(x0 + 210, 1040, lbl, 'intx', 36 * s, INK)
    tf = c.T('forever')
    if c.on(tf): stamp(c.cv, 310, 760, 'FOREVER', 52, c.P(tf, 0.35), -8, RED)
    ts = c.T('shorter')
    if c.on(ts): stamp(c.cv, 770, 760, 'SHORTER', 52, c.P(ts, 0.35), 6, GRN)
    tp = c.T('perceived')
    if c.on(tp): title(c, 'PERCEIVED PERFORMANCE', 1200, tp, 76, hlcol=YEL)

def jobs(c):
    title(c, 'TWO JOBS', 340, c.T('two'), 110)
    versus(c, ('BE FAST', BLUE, c.T('actually'), [('less', 'send fewer bytes'), ('work', 'do less work on the main thread')]),
           ('FEEL FAST', GRN, c.T('feel'), [('early', 'show useful content early'), ('tap', 'respond to every tap right away')]), 460, 1040)

def proof(c):
    box = panel(c, 70, 330, 1010, 1150, tabs=('Network', 'Performance'), dy=(1 - c.P(0, 0.45)) * 900)
    tt = c.T('throttling')
    if c.on(tt):
        c.pen.rr(110, 470, 560, 540, 12, fill=(40, 46, 56), outline=(90, 96, 106), w=2)
        lab = 'Slow 4G' if c.on(c.T('Slow')) else 'No throttling'
        c.pen.text(140, 505, lab, 'int', 30, YEL if 'Slow' in lab else WHITE, 'lm')
    tr = c.T('Reload')
    if c.on(tr):
        slow = 1.0
        for k, (a, b, col) in enumerate([(0, 0.35, BLUE), (0.3, 0.7, PURPLE), (0.4, 0.8, ORANGE), (0.7, 1.0, GRN), (0.75, 0.98, TEAL)]):
            y = 600 + k * 90; t0 = tr + k * 0.2
            if not c.on(t0): continue
            p = c.P(t0, 1.6, lambda x: x)
            xa = 140 + 800 * a; xb = xa + 800 * (b - a) * p
            c.pen.rect(xa, y, xb, y + 50, fill=col)
        counter(c, 540, 1080, 0, 9.4, tr, tr + 2.5, '{:.1f}', 70, RED, ' s to load')
    tm = c.T('millions')
    if c.on(tm): label(c, 540, 1240, 'what many real users feel every day', tm, YEL, INK, 32)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"Average load: 1.2 s. We\'re fast."', c.T('average'), 'intx', 44, INK)
    ta = c.T('Averages')
    if c.on(ta):
        hs = [3, 8, 14, 18, 15, 10, 7, 5, 4, 3, 2, 2, 1, 1]
        for k, h in enumerate(hs):
            x = 120 + k * 60; p = c.P(ta + k * 0.04, 0.3)
            col = RED if k >= 9 else (GREY if k < 7 else ORANGE)
            c.pen.rect(x, 1000 - h * 18 * p, x + 50, 1000, fill=col, outline=INK, w=3)
        c.pen.line([(100, 1004), (980, 1004)], INK, 5)
        c.pen.line([(330, 600), (330, 1000)], BLUE, 5); c.pen.text(330, 580, 'average', 'int', 28, BLUE)
        txt(c, 820, 650, 'slowest users', ta + 0.4, 'intx', 32, RED)
    tp = c.T('percentiles')
    if c.on(tp):
        x = 120 + 7 * 60 + c.P(tp, 0.4) * 0
        c.pen.line([(x, 640), (x, 1000)], INK, 7); pill(c.pen, x, 1060, 'p75', c.B(tp, 0.35), YEL, INK, 32)
    tq = c.T('quarter')
    if c.on(tq): txt(c, 540, 1180, 'report p75: 75% of visits are at least this fast', tq, 'ints', 32, INK)

SCENES = [
    (hook, "You tap a product link. One second. Two. Three. Google's research found that fifty three percent of mobile visitors leave a page that takes longer than three seconds. They're already gone."),
    (money, "Speed is money. In an often quoted finding, Amazon saw every extra hundred milliseconds cost them about one percent in sales. A tenth of a second. Barely a blink."),
    (thresholds, "Why does a tenth of a second matter? It's how we perceive time. Under a hundred milliseconds feels instant. Under one second, you stay in flow. Past ten seconds, your attention is gone."),
    (lift, "Think of a lift with no floor display. Thirty seconds feels like forever. Show the floors counting down, and the same wait feels shorter. That's perceived performance."),
    (jobs, "So performance has two jobs. Be actually fast, by sending less and doing less work. And feel fast, by showing something useful early, and responding to every tap right away."),
    (proof, "See it yourself. In DevTools, open Network, and change throttling to Slow 4G. Reload a site you use daily. That's what millions of users on slower phones and networks feel."),
    (gotcha, "Interview trap: our average load time is one point two seconds, so we're fast. Not so fast. Averages hide your slowest users. We measure at percentiles, usually the seventy fifth, so the slow quarter can't hide behind the fast majority."),
    (scene_next('S3 · E02', 'CORE WEB VITALS', 'the three numbers Google grades you on', 'Core', 'three'),
     "Next: Core Web Vitals, the three numbers Google grades your site on. Comment NOTES for the cheat sheet."),
]
