from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E04', tag='S3 · E04', short='CLS', hook='why buttons jump under your tap')

def hook(c):
    box = phone(c, 540, 760, 460, 860, url='tickets.example.com', dy=(1 - c.P(0, 0.45)) * 900)
    ta = c.T('ad')
    push = 220 * c.P(ta, 0.25) if c.on(ta) else 0
    if c.on(ta):
        c.pen.rect(330, 460, 330 + 420, 460 + push, fill=(255, 225, 190)); c.pen.text(540, 460 + push / 2, 'AD', 'osw', 60 * c.P(ta, 0.25), ORANGE)
    c.pen.text(540, 520 + push, 'Confirm booking?', 'intx', 34, INK)
    c.pen.rr(360, 590 + push, 720, 680 + push, 20, fill=GRN, outline=INK, w=4); c.pen.text(540, 635 + push, 'Buy · ₹2,400', 'intx', 32, WHITE)
    c.pen.rr(360, 810 + push, 720, 900 + push, 20, fill=WHITE, outline=INK, w=4); c.pen.text(540, 855 + push, 'Cancel', 'intx', 32, INK)
    tt = c.T('tap', 2)
    fy = 855
    c.pen.circ(600, fy, 26, fill=None, outline=RED if c.on(tt) else INK, w=6)
    if c.on(tt): stamp(c.cv, 540, 1260, 'LAYOUT SHIFT', 70, c.P(c.T('jump'), 0.35), -3, RED); c.sfx(c.T('jump'), 'thud')

def define(c):
    title(c, 'CUMULATIVE LAYOUT SHIFT', 330, c.T('Cumulative'), 76, hlcol=YEL)
    tv = c.T('moves')
    for k in range(3):
        y = 470 + k * 120; dx = 0
        if c.on(tv) and k == 1: dx = 140 * math.sin(min(1, (c.t - tv) / 0.4) * math.pi / 2)
        c.pen.rr(200 + dx, y, 880 + dx, y + 90, 14, fill=WHITE, outline=RED if dx else INK, w=5)
    gauge(c, 540, 1080, 170, 0.18, c.T('Good'), '', 'good ≤ 0.1')

def score(c):
    title(c, 'SCORING A SHIFT', 330, 0.1, 96)
    ti = c.T('screen')
    if c.on(ti):
        card(c.pen, 110, 440, 520, 1000, 20, WHITE, 8, 5)
        c.pen.rect(150, 540, 480, 740, fill=(220, 230, 250), outline=INK, w=3)
        q = c.P(c.T('far'), 0.5)
        c.pen.rect(150, 540 + 160 * q, 480, 740 + 160 * q, fill=(255, 210, 210), outline=RED, w=4)
        txt(c, 315, 1050, 'how much area', ti, 'intx', 32, INK)
    tf = c.T('far')
    if c.on(tf):
        arrow(c.pen, 760, 560, 760, 900, c.P(tf, 0.5), RED, 8)
        txt(c, 760, 1050, 'how far it moved', tf, 'intx', 32, INK)
    tb = c.T('burst')
    if c.on(tb):
        for k, (x, w) in enumerate([(160, 40), (220, 30), (270, 50), (560, 30), (620, 40)]):
            c.pen.rect(x, 1200 - w * 1.6, x + 28, 1200, fill=RED if k < 3 else ORANGE, outline=INK, w=3)
        c.pen.line([(130, 1205), (950, 1205)], INK, 5)
        c.pen.rr(140, 1100, 340, 1215, 10, outline=RED, w=5)
        txt(c, 540, 1290, 'worst burst = CLS', c.T('worst'), 'intx', 36, RED)

def chair(c):
    ts = c.T('sit')
    q = c.P(ts, 0.6) if c.on(ts) else 0
    cx = 560 + 260 * q
    c.pen.rect(cx - 90, 860, cx + 90, 890, fill=(170, 110, 60), outline=INK, w=4)
    c.pen.rect(cx + 60, 640, cx + 90, 860, fill=(170, 110, 60), outline=INK, w=4)
    for dx in (-80, 70): c.pen.rect(cx + dx, 890, cx + dx + 16, 1050, fill=(170, 110, 60), outline=INK, w=3)
    person(c.pen, 460, 1050 + 40 * q, 1.6, BLUE)
    tf = c.T('fine')
    if c.on(tf): check(c.pen, cx, 560, 1.4, GRN, 10, c.P(tf, 0.3))
    tw = c.T('worst')
    if c.on(tw): stamp(c.cv, 540, 1240, 'WORST MOMENT', 72, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')

def causes(c):
    rows(c, 90, 360, [('width', 'images without width + height', None, 'no'), ('ads', 'ads & embeds with no space', None, 'no'),
                      ('banners', 'banners injected above content', None, 'no'), ('fonts', 'web fonts swapping in', None, 'no')], 125, 900, 100, 36)
    tr = c.T('reserve')
    code(c, 60, 880, 1020, 1240, ['<img src="hero.jpg" width="800" height="450">', '.ad-slot { min-height: 250px; }', 'img { aspect-ratio: 16 / 9; }'],
         tr, 0.25, 26, 'reserve space', lang='html', marks=[(0, tr + 0.2, (60, 110, 70)), (1, tr + 0.45, (60, 110, 70))])

def proof(c):
    box = phone(c, 540, 760, 460, 860, url='news.example.com', dy=(1 - c.P(0, 0.45)) * 900)
    for k in range(5): c.pen.rr(360, 470 + k * 120, 720, 560 + k * 120, 12, fill=LIGHT)
    tb = c.T('flashes')
    if c.on(tb):
        k = int((c.t - tb) / 0.6) % 4
        c.pen.rr(360, 470 + k * 120, 720, 560 + k * 120, 12, fill=(150, 190, 255), outline=BLUE, w=5)
    tr = c.T('Layout')
    if c.on(tr): label(c, 540, 1270, 'DevTools → Rendering → Layout Shift Regions', tr, YEL, INK, 30)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Does every movement count?', c.T('every'), 'intx', 48, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 600, tn, 120, RED)
    th = c.T('half')
    if c.on(th):
        axis(c, 140, 940, 820, th, [(0.0, 'tap', th, BLUE), (0.5, '+500 ms', th + 0.3, GRN)], labels_up=True)
        c.pen.rect(140, 840, 140 + 400 * c.P(th, 0.4), 880, fill=(200, 235, 200))
        txt(c, 340, 920, 'shifts here: expected, excluded', c.T('excluded'), 'ints', 30, GRN)
    tt = c.T('transform')
    if c.on(tt): label(c, 540, 1100, 'transform animations never shift layout', tt, YEL, INK, 34)

SCENES = [
    (hook, "You're about to tap Cancel. An ad loads above it, everything jumps, and your tap lands on Buy instead. That jump is a layout shift."),
    (define, "Cumulative Layout Shift, or CLS, adds up how much visible content moves unexpectedly while you're on the page. Good is zero point one or less."),
    (score, "Each shift scores how much of the screen was affected, times how far things moved. Shifts close together form a burst, and your worst burst becomes your CLS."),
    (chair, "It's like someone pulling your chair away just as you sit. The chair was fine. It just moved at the worst moment."),
    (causes, "The usual culprits: images without a width and height. Ads and embeds with no space saved for them. Banners injected above content. And web fonts swapping in. The fix is always the same idea: reserve the space before the content arrives."),
    (proof, "Watch shifts live. In DevTools, open Rendering and turn on Layout Shift Regions. Every shift flashes blue as it happens."),
    (gotcha, "Interview trap: does every movement count? No. Shifts within half a second of a tap or key press are expected, so they're excluded. And animations that use transform don't shift layout at all."),
    (scene_next('S3 · E05', 'INP', 'the tap that takes forever', 'INP', 'forever'),
     "Next: INP, and the tap that seems to take forever. Comment NOTES for the cheat sheet."),
]
