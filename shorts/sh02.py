from engine.lib import *
from engine.shorts import hook, fox_cta, repo_card

EP = dict(id='SH02', tag='SHORT', short='4 GitHub repos', tail=1.6,
          hook='4 repos that feel illegal',
          caption=("4 GitHub repos that feel illegal to know 🤫\n\n"
                   "1. build-your-own-x: build your own Git, database, even an OS\n"
                   "2. public-apis: hundreds of free APIs for side projects\n"
                   "3. free-programming-books: thousands of free books and courses\n"
                   "4. Wireless-Device-Battery-Monitor: trending on GitHub right now\n\n"
                   "Save this 📌 Which one are you trying first? 👇"))

def s0(c):
    hook(c, ['4 GITHUB', 'REPOS'], 470, 170)
    tf = c.T('illegal')
    if c.on(tf): c.sfx(tf, 'thud'); stamp(c.cv, 540, 900, 'FEEL ILLEGAL TO KNOW', 76, c.P(tf, 0.35), -5)
    chips(c, 150, 1150, [('git clone', YEL), ('free', WHITE), ('open source', WHITE)], c.T('know'), 0.15, 34)

def s1(c):
    repo_card(c, 450, 1, 'build-your-own-x', 'Step-by-step guides to rebuild real tech yourself', 0, '563k')
    items = [('Git', YEL), ('Database', WHITE), ('Operating system', WHITE), ('Redis', WHITE), ('Docker', WHITE)]
    chips(c, 120, 760, items[:1], c.T('Git'), 0.2, 40)
    chips(c, 120 + c.pen.tw('Git', 'monob', 40) + 60, 760, items[1:2], c.T('database'), 0.2, 40)
    chips(c, 120, 860, items[2:3], c.T('operating'), 0.2, 40)
    txt(c, 540, 1060, 'step by step', c.T('step'), 'intx', 60, INK, anim='pop')

def s2(c):
    repo_card(c, 450, 2, 'public-apis', 'A giant list of free APIs to build side projects with', 0, '500k')
    ws = [('weather', 'weather'), ('movies', 'movies'), ('sports', 'sports')]
    for i, (lab, kw) in enumerate(ws):
        node(c, 220 + i * 320, 820, 260, 160, lab, c.T(kw), ['cloud', 'eye', 'bolt'][i])
    txt(c, 540, 1060, 'for your next side project', c.T('side'), 'intx', 50, INK)

def s3(c):
    repo_card(c, 450, 3, 'free-programming-books', 'Free books, courses and cheat sheets, all in one list', 0)
    for i in range(5):
        at = c.T('thousands') + i * 0.1
        if c.on(at):
            s = c.B(at, 0.35); x = 230 + i * 155
            c.pen.rr(x - 55 * s, 780 - 80 * s, x + 55 * s, 780 + 80 * s, 10 * s, fill=[YEL, WHITE, RED, WHITE, YEL][i], outline=INK, w=5)
            icon(c.pen, 'book', x, 780, 0.6 * s)
    txt(c, 540, 1000, 'in dozens of languages', c.T('languages'), 'intx', 52, INK)

def s4(c):
    tt = c.T('trending')
    if c.on(tt): c.sfx(tt, 'thud'); stamp(c.cv, 540, 330, 'TRENDING NOW', 70, c.P(tt, 0.3), -4)
    repo_card(c, 640, 4, 'Wireless-Device-Battery-Monitor', 'Every wireless battery, right in your Windows taskbar', c.T('Wireless'), tag='+1.9k stars in 1 day')
    tb = c.T('mouse')
    c_ = c
    if c.on(tb):
        s = c.P(tb, 0.4)
        c.pen.rr(110, 960, 970, 1070, 16, fill=DARK)
        for i, (lab, pct, col) in enumerate([('Mouse', 0.82, GRN), ('Headset', 0.35, YEL), ('Pad', 0.12, RED)]):
            x = 180 + i * 270
            c.pen.text(x, 1015, lab, 'ints', 30, WHITE, 'lm')
            c.pen.rr(x + 120, 1000, x + 220, 1030, 6, outline=WHITE, w=3)
            c.pen.rr(x + 124, 1004, x + 124 + 92 * pct * s, 1026, 4, fill=col)

def s5(c):
    ts = c.T('Save')
    if c.on(ts): c.sfx(ts, 'thud'); stamp(c.cv, 540, 430, 'SAVE THIS', 120, c.P(ts, 0.35), -5)
    fox_cta(c, c.T('Follow'), 'FOLLOW: ONE TOOL A DAY', 1000)

SCENES = [
    (s0, "Four GitHub repos that feel illegal to know."),
    (s1, "One. Build your own X. Rebuild Git, a database, even an operating system, step by step."),
    (s2, "Two. Public APIs. Hundreds of free APIs, weather, movies, sports, for your next side project."),
    (s3, "Three. Free programming books. Thousands of free books and courses, in dozens of languages."),
    (s4, "And four is trending right now. Wireless Device Battery Monitor shows your mouse and headset battery right in the Windows taskbar."),
    (s5, "Save this before you forget. Follow for one tool a day."),
]
