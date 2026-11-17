from engine.lib import *

EP = dict(id='S1E11', tag='S1 · E11', short='LAYOUT THRASHING')

BAD = ['for (const box of boxes) {', '  const h = box.offsetHeight;   // read', "  box.style.height = h * 2 + 'px'; // write", '}']
GOOD = ['const hs = boxes.map(b => b.offsetHeight); // reads',
        "boxes.forEach((b, i) =>", "  b.style.height = hs[i] * 2 + 'px'); // writes"]

def hook(c):
    code(c, 60, 330, 1020, 700, BAD, 0.2, 0.15, 28, 'list.js', dy=(1 - c.P(0, 0.45)) * 900)
    th = c.T('hundreds')
    if c.on(th):
        for k in range(24):
            at = th + k * 0.04
            if c.on(at): c.pen.rect(100 + k * 36, 820, 128 + k * 36, 900, fill=PURPLE, outline=INK, w=2)
        c.pen.text(540, 950, 'layout · layout · layout … in ONE frame', 'int', 34, PURPLE)
    ti = c.T('innocent')
    if c.on(ti): stamp(c.cv, 760, 1100, 'LOOKS INNOCENT', 50, c.P(ti, 0.35), -4, GRN)

def pattern(c):
    code(c, 60, 330, 1020, 700, BAD, -1, 0.0, 28, 'list.js', marks=[(1, c.T('read'), (52, 86, 168)), (2, c.T('write'), (150, 50, 60))], dy=0)
    tr = c.T('read', 2)
    if c.on(tr):
        for k in range(8):
            at = tr + k * 0.2
            if not c.on(at): continue
            c.sfx(at, 'tick')
            x = 100 + k * 110
            col = (52, 86, 168) if k % 2 == 0 else (150, 50, 60)
            c.pen.rr(x, 800, x + 96, 870, 12, fill=col, outline=INK, w=3)
            c.pen.text(x + 48, 835, 'R' if k % 2 == 0 else 'W', 'osw', 36, WHITE)
            if k % 2 == 0 and k > 0: c.pen.rect(x - 14, 890, x + 4, 960, fill=PURPLE)
    tf = c.T('forces')
    if c.on(tf): txt(c, 540, 1040, 'every read after a write → a fresh layout', tf, 'intx', 38, PURPLE)

def tailor(c):
    node(c, 300, 600, 380, 300, 'measure', c.T('measures'), 'eye', sub='tailor measures you')
    node(c, 780, 600, 380, 300, 'cut', c.T('cuts'), 'bolt', sub='cuts the cloth')
    ta = c.T('again')
    if c.on(ta):
        for k in range(3):
            q = ((c.t - ta) * 0.8 + k / 3) % 1.0
            x = 300 + 480 * q if q < 0.5 else 780 - 480 * (q - 0.5) * 2
        link(c, (110, 450, 490, 750), (590, 450, 970, 750), ta, 0.3, RED, off=-30)
        link(c, (590, 450, 970, 750), (110, 450, 490, 750), ta + 0.3, 0.3, RED, off=-30)
        txt(c, 540, 840, '…after every single cut', ta, 'int', 36, RED)
    tm = c.T('first')
    if c.on(tm): label(c, 540, 1050, 'measure everything first, then cut', tm, GRN, WHITE, 34)

def fix(c):
    title(c, 'THE FIX: BATCH IT', 320, c.T('batch'), 96, hlcol=YEL)
    code(c, 40, 420, 1040, 720, GOOD, c.T('reads'), 0.2, 26, 'list.js', marks=[(0, c.T('reads'), (52, 86, 168)), (2, c.T('writes'), (150, 50, 60))])
    to = c.T('once')
    if c.on(to):
        for k in range(4): c.pen.rr(100 + k * 110, 820, 196 + k * 110, 890, 12, fill=(52, 86, 168), outline=INK, w=3); c.pen.text(148 + k * 110, 855, 'R', 'osw', 36, WHITE)
        c.pen.rect(546, 820, 566, 890, fill=PURPLE)
        for k in range(3): c.pen.rr(580 + k * 110, 820, 676 + k * 110, 890, 12, fill=(150, 50, 60), outline=INK, w=3); c.pen.text(628 + k * 110, 855, 'W', 'osw', 36, WHITE)
        stamp(c.cv, 540, 1010, 'LAYOUT ONCE', 64, c.P(to, 0.35), -3, GRN)

def raf(c):
    code(c, 80, 380, 1000, 640, ['requestAnimationFrame(() => {', "  box.style.height = h * 2 + 'px';", '});'], c.T('requestAnimationFrame'), 0.2, 30, 'scroll.js')
    tf = c.T('frame')
    if c.on(tf):
        for k in range(5):
            x = 120 + k * 170
            c.pen.rr(x, 760, x + 150, 880, 12, fill=WHITE, outline=INK, w=4)
            c.pen.text(x + 75, 820, f'frame {k + 1}', 'int', 26, INK)
        k = int(lin(c.t, tf, tf + 2.5) * 4.99)
        c.pen.rr(120 + k * 170 + 100, 770, 120 + k * 170 + 140, 870, 8, fill=YEL, outline=INK, w=3)
        txt(c, 540, 960, 'your write lands right before the next paint', tf, 'int', 34, INK)

def proof(c):
    panel(c, 60, 330, 1020, 900, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    tp = c.T('purple')
    blocks = [(0.0, 0.08, 0, 'JS')] + [(0.08 + k * 0.07, 0.05, 1, 'Layout', True) for k in range(12)]
    flame(c, 100, 500, 980, blocks, tp - 0.3, 60, labels=False)
    tw = c.T('warning')
    if c.on(tw):
        c.sfx(tw, 'pop'); s = c.B(tw, 0.35)
        card(c.pen, 140, 700, 940, 840, 14, WHITE, 6, 3)
        c.pen.poly([(180, 790), (200, 750), (220, 790)], fill=RED)
        c.pen.text(240, 770, 'Forced reflow is a likely', 'ints', 30 * s, INK, 'lm')
        c.pen.text(240, 810, 'performance bottleneck.', 'ints', 30 * s, INK, 'lm')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Which reads force layout?', c.T('which'), 'intx', 48, INK)
    items = [('offsetHeight', 'offsetHeight'), ('offsetTop', 'offsetTop'), ('clientWidth', 'clientWidth'), ('scrollTop', 'scrollTop'), ('getBoundingClientRect()', 'getBoundingClientRect')]
    for i, (s_, kw) in enumerate(items):
        at = c.T(kw); y = 600 + i * 110
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); p = c.B(at, 0.3)
        w = c.pen.tw(s_, 'monob', 40) + 50
        c.pen.rr(540 - w / 2 * p, y - 38 * p, 540 + w / 2 * p, y + 38 * p, 38 * p, fill=(220, 210, 250), outline=INK, w=4)
        c.pen.text(540, y, s_, 'monob', 40 * p, INK)

SCENES = [
    (hook, "Your code looks innocent. A simple loop over a list. But it's forcing the browser to run layout hundreds of times in a single frame."),
    (pattern, "Here's the pattern. Inside the loop, you read a box's height, then write a new one. Read, write, read, write. Every read after a write forces a fresh layout."),
    (tailor, "It's like a tailor who measures you, cuts the cloth, and then measures you again, after every single cut. Measure everything first, then cut."),
    (fix, "The fix: batch them. Do all the reads first, then all the writes. Now the browser runs layout once."),
    (raf, "For writes triggered by events like scroll, schedule them with requestAnimationFrame, so they land right before the next frame."),
    (proof, "In the Performance panel, thrashing shows up as a wall of purple layout blocks, each with a red warning about forced reflow."),
    (gotcha, "Interview question: which properties force layout when you read them? offsetHeight, offsetTop, clientWidth, scrollTop, and getBoundingClientRect, to name a few."),
    (scene_next('S1 · E12', 'TRANSFORM', 'why it animates smoothly and top does not', 'transform', 'smoothly'),
     "Next: why transform animates smoothly, and top doesn't. Comment NOTES for the cheat sheet."),
]
