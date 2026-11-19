from engine.lib import *
from engine.shorts import hook, fox_cta

EP = dict(id='SH04', tag='SHORT', short='5 stages of prod down', tail=1.4,
          hook='5 stages of being a dev',
          caption=("5 stages of being a developer jab production down ho jaata hai 🔥\n\n"
                   "Denial → Panic → Bargaining → Blame → Acceptance\n\n"
                   "Stage 4 hurts the most 😭 Which stage are you in right now? 👇\n"
                   "📩 Send this to the friend who's on-call tonight."))

def stage(c, n, name, col=YEL):
    """stage header, visible from frame 1 of the scene"""
    pill(c.pen, 540, 300, f'STAGE {n} / 5', 1, INK, WHITE, 34, outline=None)
    hook(c, [name], 440, 150, hlcol=col)
    for i in range(5):  # progress dots
        c.pen.circ(420 + i * 60, 580, 14, fill=RED if i < n else LIGHT, outline=INK, w=3)

def s0(c):
    pill(c.pen, 540, 290, '2:07 AM', 1, RED, WHITE, 40, outline=None)
    hook(c, ['5 STAGES OF', 'BEING A DEV'], 460, 140)
    tp = c.T('production')
    if c.on(tp):
        c.sfx(tp, 'thud'); stamp(c.cv, 540, 900, 'WHEN PROD GOES DOWN', 84, c.P(tp, 0.35), -4)
    # alarm siren
    tl = c.T('jaata')
    if c.on(tl):
        r = 90 + 20 * math.sin(c.t * 20)
        c.pen.circ(540, 1200, r, fill=RED, outline=INK, w=6)
        c.pen.text(540, 1200, '500', 'osw', 80 * c.B(tl, 0.3), WHITE)

def s1(c):
    stage(c, 1, 'DENIAL')
    tm = c.T('local')
    card(c.pen, 120, 700, 960, 1180, 28, DARK, 12, 5)
    c.pen.text(170, 760, 'localhost:3000', 'monob', 36, (150, 155, 165), 'lm')
    if c.on(tm):
        check(c.pen, 540, 950, 2.2 * c.B(tm, 0.4), GRN, 22)
        txt(c, 540, 1110, '"mere local pe toh chal raha tha"', tm + 0.2, 'intx', 40, WHITE)

def s2(c):
    stage(c, 2, 'PANIC', RED)
    ts = c.T('Slack')
    counter(c, 540, 830, 0, 200, ts, ts + 1.2, '{:.0f}', 230, RED, '+')
    txt(c, 540, 990, 'unread messages', ts + 0.3, 'intx', 50, INK)
    tm = c.T('manager')
    if c.on(tm):
        s = c.B(tm, 0.35)
        card(c.pen, 150, 1100, 930, 1250, 40, WHITE, 8, 5)
        dots = '.' * (1 + int(c.t * 4) % 3)
        c.pen.text(540, 1175, 'Manager is typing' + dots, 'intx', 46 * s, INK)

def s3(c):
    stage(c, 3, 'BARGAINING')
    tb = c.T('console')
    lines = ['console.log("here")', 'console.log("here 2")', 'console.log("WHY")', 'console.log("pls")', 'console.log("!!!")']
    card(c.pen, 90, 680, 990, 1260, 24, DARK, 12, 5)
    for i, ln in enumerate(lines):
        at = tb + i * 0.32
        if c.on(at):
            c.sfx(at, 'pop')
            c.pen.text(140, 750 + i * 105, ln, 'monob', 46, [CYAN, CYAN, YEL, YEL, RED][i], 'lm')

def s4(c):
    stage(c, 4, 'BLAME')
    tg = c.T('git')
    card(c.pen, 90, 680, 990, 1130, 24, DARK, 12, 5)
    if c.on(tg):
        c.pen.text(140, 750, '$ git blame app.js', 'monob', 44, WHITE, 'lm')
    tn = c.T('naam')
    if c.on(tn):
        c.pen.text(140, 860, 'line 42:', 'monob', 44, (150, 155, 165), 'lm')
    tk = c.T('khud')
    if c.on(tk):
        c.sfx(tk, 'thud')
        c.pen.rr(130, 920, 950, 1040, 16, fill=YEL)
        c.pen.text(540, 980, 'YOU, 3 days ago', 'monob', 56 * c.B(tk, 0.35), INK)
        stamp(c.cv, 540, 1250, 'IT WAS ME', 110, c.P(tk + 0.25, 0.35), 5)

def s5(c):
    stage(c, 5, 'ACCEPTANCE', GRN)
    tf = c.T('fix')
    card(c.pen, 90, 680, 990, 960, 24, WHITE, 12, 5)
    if c.on(tf):
        c.pen.rr(110, 720, 970, 810, 10, fill=(255, 225, 225))
        c.pen.text(140, 765, '-  return user.name', 'monob', 44, RED, 'lm')
        c.pen.rr(110, 830, 970, 920, 10, fill=(220, 245, 225))
        c.pen.text(140, 875, '+  return user?.name', 'monob', 44, GRN, 'lm')
    tt = c.T('teen')
    if c.on(tt):
        c.sfx(tt, 'thud')
        c.pen.text(540, 1120, '3 HOURS.', 'osw', 120 * c.B(tt, 0.35), INK)
        c.pen.text(540, 1260, '2 CHARACTERS.', 'osw', 120 * c.B(tt + 0.5, 0.35), RED)

def s6(c):
    tb = c.T('bhejo')
    pill(c.pen, 540, 330, 'SEND THIS TO', 1, INK, WHITE, 40, outline=None)
    hook(c, ['YOUR ON-CALL', 'FRIEND'], 470, 120)
    fox_cta(c, c.T('Follow'), 'FOLLOW @tech.explained.dev', 1050)

SCENES = [
    (s0, "Five stages of being a developer, jab production down ho jaata hai."),
    (s1, "Stage one. Denial. Mere local pe toh chal raha tha!"),
    (s2, "Stage two. Panic. Slack pe do sau messages, aur manager typing..."),
    (s3, "Stage three. Bargaining. Bas ek console log aur daal ke dekhta hoon."),
    (s4, "Stage four. Blame. git blame chalaya, aur naam aaya, khud ka."),
    (s5, "Stage five. Acceptance. Ek line ka fix. Teen ghante."),
    (s6, "Yeh reel us dost ko bhejo jo aaj on-call hai. Follow karo."),
]
