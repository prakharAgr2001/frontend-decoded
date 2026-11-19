from engine.lib import *
from engine.shorts import hook, fox_cta

EP = dict(id='SH05', tag='SHORT', short='Captcha secret', tail=1.0,
          hook='Does the pole count?',
          caption=("\"Select all images with traffic lights\" 🚦\nBhai, pole bhi count hota hai kya? 😭\n\n"
                   "Plot twist: that checkbox was watching HOW you moved your mouse. And those old wavy words? "
                   "Google used them to digitize old books.\n\n"
                   "Tumne kitni baar fail kiya hai? 👇\n📩 Send this to the friend who fails CAPTCHA 3 times."))

def tl(c, cx, cy, s, on=True):
    """tiny traffic light"""
    c.pen.rect(cx - 3 * s, cy + 30 * s, cx + 3 * s, cy + 90 * s, fill=INK)
    c.pen.rr(cx - 18 * s, cy - 45 * s, cx + 18 * s, cy + 35 * s, 8 * s, fill=INK)
    for i, col in enumerate([RED, YEL, GRN]):
        c.pen.circ(cx, cy - 25 * s + i * 25 * s, 8 * s, fill=col if on else (80, 80, 80))

GRID = [1, 0, 0, 1, 1, 0, 0, 2, 0]   # 1 = traffic light, 2 = only the pole (the classic doubt)

def grid(c, y0=560, sel=(), pulse=None):
    c.pen.rr(110, y0 - 140, 970, y0 + 760, 18, fill=WHITE, outline=INK, w=5)
    c.pen.rect(110, y0 - 140, 970, y0 - 20, fill=BLUE)
    c.pen.text(140, y0 - 98, 'Select all images with', 'ints', 30, WHITE, 'lm')
    c.pen.text(140, y0 - 52, 'traffic lights', 'intx', 46, WHITE, 'lm')
    for i, k in enumerate(GRID):
        x = 140 + (i % 3) * 270; y = y0 + (i // 3) * 245
        c.pen.rect(x, y, x + 260, y + 235, fill=(205, 215, 200) if (i % 2) else (190, 205, 215))
        c.pen.rect(x, y + 170, x + 260, y + 235, fill=(150, 150, 150))
        if k == 1: tl(c, x + 130, y + 100, 1.2)
        if k == 2: c.pen.rect(x + 124, y, x + 136, y + 200, fill=INK)
        if i in sel:
            c.pen.rect(x, y, x + 260, y + 235, outline=BLUE, w=10)
            c.pen.circ(x + 34, y + 34, 22, fill=BLUE); check(c.pen, x + 34, y + 34, 0.28, WHITE, 5)
        if pulse is not None and i == 7:
            c.pen.rect(x - 4, y - 4, x + 264, y + 239, outline=RED, w=int(6 + 4 * math.sin(c.t * 12)))


def s0(c):
    grid(c, 520, [0, 3, 4], pulse=True)
    c.sfx(0.02, 'thud'); stamp(c.cv, 640, 1250, 'POLE BHI?!', 130, c.P(-0.3, 0.3), -7)

def s1(c):
    c.pen.rect(0, 250, 1080, 1450, fill=RED)
    c.pen.text(540, 760, 'PLOT', 'osw', 300 * c.B(-0.2, 0.25), WHITE)
    c.pen.text(540, 1060, 'TWIST', 'osw', 300 * c.B(-0.1, 0.25), YEL)

def s2(c):
    c.pen.rr(140, 420, 940, 620, 14, fill=WHITE, outline=GREY, w=4)
    c.pen.rr(190, 475, 280, 565, 8, fill=WHITE, outline=MUTE, w=5)
    c.pen.text(320, 520, "I'm not a robot", 'ints', 50, INK, 'lm')
    title(c, 'ASLI TEST:', 830, -0.3, 120, INK, None, d=0.2, sound=None)
    tm = c.T('mouse')
    title(c, 'TUMHARA MOUSE', 990, tm, 120, INK, YEL, d=0.2, sound='thud')

def s3(c):
    pill(c.pen, 540, 400, 'ROBOT', 1, INK, WHITE, 60, outline=None)
    p = c.P(0, 0.35)
    c.pen.line([(200, 1200), (200 + 680 * p, 1200 - 650 * p)], INK, 16)
    if p > 0.95: c.sfx(0.35, 'thud'); stamp(c.cv, 760, 1300, 'SUS', 140, c.P(0.4, 0.25), 6)

def s4(c):
    pill(c.pen, 540, 400, 'INSAAN', 1, YEL, INK, 60)
    p = c.P(0, 0.6, eio)
    pts = [(200 + 680 * u + 90 * math.sin(u * 11), 1200 - 650 * u + 60 * math.sin(u * 17)) for u in [k / 60 * p for k in range(61)]]
    c.pen.line(pts, RED, 16)
    if p > 0.95: check(c.pen, 860, 1250, 2.2 * c.B(0.6, 0.3), GRN, 22)

def s5(c):
    c.pen.rr(110, 520, 970, 860, 18, fill=WHITE, outline=INK, w=6)
    for i, ch in enumerate('ovemrn'):
        c.pen.text(220 + i * 128, 690 + 34 * math.sin(i * 1.7 + c.t * 8), ch, 'osw', 170, INK)
    title(c, 'YAAD HAI?', 1100, 0.25, 130, INK, YEL, d=0.2)

def s6(c):
    tb = c.T('books')
    for i in range(4):
        at = tb + i * 0.07
        if c.on(at):
            s = c.B(at, 0.2); x = 230 + i * 205
            c.pen.rr(x - 75 * s, 480, x + 75 * s, 480 + 250 * s, 10, fill=[YEL, RED, WHITE, YEL][i], outline=INK, w=6)
            icon(c.pen, 'book', x, 600, 0.9 * s)
    txt(c, 540, 860, 'you typed old books for Google', tb + 0.1, 'intx', 50, INK, anim='pop', d=0.2)
    tf = c.T('Free')
    if c.on(tf): c.sfx(tf, 'thud'); stamp(c.cv, 540, 1150, 'FOR FREE', 170, c.P(tf, 0.25), 5)

def s7(c):
    c.pen.rect(0, 250, 1080, 1450, fill=INK)
    c.pen.text(540, 640, "CONGRATS,", 'osw', 120 * c.B(-0.2, 0.2), WHITE)
    c.pen.text(540, 800, "YOU'RE GOOGLE'S", 'osw', 120 * c.B(-0.1, 0.2), WHITE)
    ti = c.T('intern')
    if c.on(ti): c.sfx(ti, 'thud'); stamp(c.cv, 540, 1060, 'UNPAID INTERN', 140, c.P(ti, 0.25), -6, YEL)

def s8(c):
    pill(c.pen, 540, 360, 'SEND THIS TO', 1, INK, WHITE, 46, outline=None)
    hook(c, ['THAT FRIEND', 'WHO FAILS 3X'], 500, 130)
    fox_cta(c, c.T('Follow') if 'Follow' in [w[0].strip('.,') for w in c.words] else 0.6, 'FOLLOW @tech.explained.dev', 1110)

SCENES = [
    (s0, "Bhai, pole bhi count hota hai kya?!"),
    (s1, "Plot twist."),
    (s2, "Asli test? Tumhara mouse."),
    (s3, "Robot: seedha."),
    (s4, "Insaan: ghoom ghoom ke."),
    (s5, "Aur yeh tedhe words, yaad hai?"),
    (s6, "Inse Google ne purani books type karwayi. Free mein."),
    (s7, "Congrats, tum Google ke unpaid intern ho."),
    (s8, "Bhejo us dost ko jo teen baar fail hota hai. Follow karo."),
]
