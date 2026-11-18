from engine.lib import *
from engine.shorts import hook, fox_cta

EP = dict(id='SH03', tag='SHORT', short='AI teacher at PW', tail=1.6,
          hook='9 in 10 doubts: solved by AI',
          caption=("9 out of 10 doubts at PhysicsWallah are now solved by AI, says co-founder Prateek Maheshwari. 🤖\n\n"
                   "AI has also evaluated 2 million+ answer sheets, and PW says its headcount dipped last quarter partly due to AI efficiencies.\n\n"
                   "So… if AI can solve your doubt at 2 AM, what is a teacher for? Comment 👇"))

def s0(c):
    hook(c, ['9 IN 10 DOUBTS'], 360, 120)
    tai = c.T('AI')
    for i in range(10):
        x = 200 + (i % 5) * 170; y = 650 + (i // 5) * 260
        ai = i < 9 and c.on(tai + i * 0.06)
        s = c.B(tai + i * 0.06, 0.3) if ai else 1
        c.pen.circ(x, y, 70, fill=YEL if ai else WHITE, outline=INK, w=5)
        if ai: icon(c.pen, 'cpu', x, y, 0.6 * s)
        else: person(c.pen, x, y + 50, 0.62, LIGHT)
    tt = c.T('teacher')
    if c.on(tt): c.sfx(tt, 'thud'); stamp(c.cv, 540, 1230, 'NOT A TEACHER', 100, c.P(tt, 0.35), -5)

def s1(c):
    card(c.pen, 90, 450, 990, 900, 30, WHITE, 12, 5)
    c.pen.text(150, 560, '“', 'osw', 200, YEL, 'lm')
    title(c, '90% OF DOUBTS', 640, 0, 96, INK, d=0.3, sound=None)
    title(c, 'SOLVED BY AI', 760, 0.15, 96, INK, YEL, d=0.3)
    txt(c, 540, 1000, 'Prateek Maheshwari, PW co-founder', c.T('Prateek'), 'ints', 40, INK)
    label(c, 540, 1090, 'via PTI', c.T('PTI'), LIGHT, INK, 30)

def s2(c):
    t2 = c.T('two')
    counter(c, 540, 600, 0, 2000000, t2, t2 + 0.9, '{:,.0f}+', 140, RED)
    txt(c, 540, 760, 'answer sheets evaluated by AI', c.T('answer'), 'intx', 48, INK)
    for i in range(6):
        at = c.T('two') + 0.3 + i * 0.12
        if c.on(at):
            s = c.B(at, 0.3); x = 190 + i * 140; y = 1010 + (i % 2) * 40
            c.pen.rr(x - 50 * s, y - 70 * s, x + 50 * s, y + 70 * s, 8, fill=WHITE, outline=INK, w=4)
            check(c.pen, x, y, 0.5 * s, GRN, 8)

def s3(c):
    pill(c.pen, 540, 330, 'PW · LAST QUARTER', c.B(0, 0.3), INK, WHITE, 32, outline=None)
    th = c.T('headcount')
    for i in range(12):
        x = 190 + (i % 6) * 140; y = 640 + (i // 6) * 220
        gone = i >= 9 and c.on(c.T('down'))
        person(c.pen, x, y + 70, 0.95, mix(YEL, LIGHT, c.P(c.T('down'), 0.4)) if gone else YEL)
    if c.on(c.T('down')):
        arrow(c.pen, 940, 560, 940, 980, c.P(c.T('down'), 0.4), RED, 12, 34)
    txt(c, 540, 1130, 'partly due to AI, says PW', c.T('partly'), 'intx', 50, INK)

def s4(c):
    hook(c, ['2:00 AM'], 450, 170, at=0, hlcol=None)
    tq = c.T('teacher')
    if c.on(tq):
        c.sfx(tq, 'thud'); c.pen.text(540, 860, '?', 'osw', 380 * c.B(tq, 0.4), RED)
    tcm = c.T('Comment')
    if c.on(tcm): label(c, 540, 1180, 'COMMENT YOUR ANSWER', tcm, YEL, INK, 40)

def s5(c):
    fox_cta(c, 0.05, 'FOLLOW FOR TECH CHANGING INDIA', 900)

SCENES = [
    (s0, "Nine out of ten doubts at PhysicsWallah are now solved by AI. Not a teacher."),
    (s1, "That's what co-founder Prateek Maheshwari told PTI."),
    (s2, "AI has also evaluated over two million answer sheets."),
    (s3, "And last quarter, PW's headcount went down, partly, the company says, because of AI."),
    (s4, "So if AI can solve your doubt at two AM, what is a teacher actually for? Comment your answer."),
    (s5, "Follow for the tech that's changing India."),
]
