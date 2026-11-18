from engine.lib import *
from engine.shorts import hook, fox_cta, paste

EP = dict(id='SH01', tag='SHORT', short='Nvidia CEO out', tail=1.6,
          hook='$4 trillion. And he is out.',
          caption=("33 years. A $4 trillion company. And the man who built it just stepped down. 😳\n\n"
                   "Jensen Huang is out as Nvidia CEO. The stock fell over 10% before the market even opened.\n\n"
                   "Can one person really be worth hundreds of billions? Comment 👇"))

def s0(c):
    pill(c.pen, 540, 290, 'BREAKING · NVIDIA', 1, RED, WHITE, 36, outline=None)
    hook(c, ['33 YEARS.'], 430, 170)
    t4 = c.T('Four')
    counter(c, 540, 760, 0, 4, t4, t4 + 0.6, '${:.0f} TRILLION', 120, INK)
    to = c.T('out')
    if c.on(to): c.sfx(to, 'thud'); stamp(c.cv, 540, 1080, "HE'S OUT", 150, c.P(to, 0.35), -6)

def s1(c):
    c.pen.circ(540, 600, 230, fill=LIGHT, outline=INK, w=6)
    person(c.pen, 540, 760, 2.2, INK)
    pill(c.pen, 540, 330, 'NVIDIA · CEO SINCE 1993', 1, INK, WHITE, 34, outline=None)
    title(c, 'JENSEN HUANG', 930, c.T('Jensen'), 110, INK, YEL)
    tl = c.T('leather')
    txt(c, 540, 1040, 'the leather-jacket boss', tl, 'ints', 44, MUTE)
    ts = c.T('stepped')
    if c.on(ts): c.sfx(ts, 'thud'); stamp(c.cv, 540, 1200, 'STEPPED DOWN', 110, c.P(ts, 0.35), 5)

def s2(c):
    tc = c.T('chips')
    s = c.B(0, 0.4)
    c.pen.circ(540, 640, 170 * s, fill=YEL, outline=INK, w=6)
    icon(c.pen, 'gpu', 540, 640, 1.6 * s)
    items = ['AI labs', 'cloud giants', 'data centers', 'self-driving', 'gaming', 'robots']
    ta = c.T('AI')
    for i, it in enumerate(items):
        a = -math.pi / 2 + i * 2 * math.pi / len(items)
        x, y = 540 + 360 * math.cos(a), 640 + 330 * math.sin(a)
        at = ta + i * 0.12
        if c.on(at): arrow(c.pen, 540 + 180 * math.cos(a), 640 + 175 * math.sin(a), x - 70 * math.cos(a), y - 50 * math.sin(a), c.P(at, 0.25), INK, 5, 16)
        label(c, x, y, it, at, WHITE, INK, 30)
    txt(c, 540, 1130, "the chips the AI boom runs on", tc, 'intx', 48, INK)

def s3(c):
    pill(c.pen, 540, 330, 'NVDA · PRE-MARKET', c.B(0, 0.3), INK, WHITE, 32, outline=None)
    x0, x1, y0 = 140, 940, 520
    tf = c.T('fell')
    pts = [(x0, y0 + 160), (x0 + 160, y0 + 110), (x0 + 300, y0 + 140), (x0 + 450, y0 + 60), (x0 + 560, y0 + 80)]
    drop = [(x0 + 560, y0 + 80), (x0 + 660, y0 + 330), (x1, y0 + 420)]
    c.pen.rr(x0 - 40, y0 - 60, x1 + 40, y0 + 500, 24, fill=WHITE, outline=INK, w=5)
    c.pen.line(pts, GRN, 10)
    if c.on(tf):
        p = c.P(tf, 0.6); n = drop[0]; k = drop[1] if p < 0.5 else drop[2]
        seg = [drop[0], (drop[0][0] + (drop[1][0] - drop[0][0]) * min(1, p * 2), drop[0][1] + (drop[1][1] - drop[0][1]) * min(1, p * 2))]
        if p > 0.5: seg.append((drop[1][0] + (drop[2][0] - drop[1][0]) * (p - 0.5) * 2, drop[1][1] + (drop[2][1] - drop[1][1]) * (p - 0.5) * 2))
        c.pen.line(seg, RED, 12)
    bignum(c, 540, 1170, '-10%', c.T('ten'), 230, RED)
    txt(c, 540, 1330, 'before the market even opened', c.T('opened'), 'ints', 40, MUTE)

def s4(c):
    t4 = c.T('four')
    counter(c, 540, 700, 0, 400, t4, t4 + 0.9, '${:.0f}B', 260, RED)
    txt(c, 540, 900, 'of value, on paper', c.T('paper'), 'ints', 46, MUTE)
    to = c.T('man')
    if c.on(to):
        person(c.pen, 540, 1300, 1.6 * c.B(to, 0.4), YEL)
        txt(c, 540, 1360, 'over ONE person', to + 0.1, 'intx', 50, INK)

def s5(c):
    tc = c.T('chips')
    node(c, 300, 560, 330, 240, 'its chips', tc, 'gpu')
    tp = c.T('person')
    node(c, 780, 560, 330, 240, 'one person', tp, None, YEL)
    if c.on(tp):
        cross(c.pen, 300, 560, 1.2, RED, 12, c.P(tp, 0.3))
    fox_cta(c, c.T('Follow'), 'FOLLOW FOR TECH NEWS, EXPLAINED', 1080)

SCENES = [
    (s0, "Thirty-three years. Four trillion dollars. And he's out."),
    (s1, "Jensen Huang, the leather-jacket boss who built Nvidia, just stepped down."),
    (s2, "Nvidia makes the chips most of the world's AI runs on."),
    (s3, "After a week of scandal reports, the stock fell over ten percent before the market even opened."),
    (s4, "That's around four hundred billion dollars, on paper, over one man."),
    (s5, "Sometimes a company isn't its chips. It's one person. Follow for tech news, explained."),
]
