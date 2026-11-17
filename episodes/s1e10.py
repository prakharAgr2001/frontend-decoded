from engine.lib import *

EP = dict(id='S1E10', tag='S1 · E10', short='REFLOW vs REPAINT')

def hook(c):
    for j, (lab, smooth, kw) in enumerate([('one property', True, 'smooth'), ('another', False, 'stutters')]):
        at = c.T(kw); y = 520 + j * 330
        if not c.on(at - 0.01): continue
        c.pen.text(110, y - 90, lab, 'int', 34, INK, 'lm')
        c.pen.rect(110, y - 50, 970, y + 70, fill=LIGHT)
        q = ((c.t - at) * 0.5) % 1.0
        if not smooth: q = math.floor(q * 7) / 7
        x = 140 + q * 700
        c.pen.rr(x, y - 30, x + 100, y + 50, 14, fill=GRN if smooth else RED, outline=INK, w=4)
        stamp(c.cv, 820, y - 90, 'SMOOTH' if smooth else 'STUTTER', 40, c.P(at, 0.3), -4, GRN if smooth else RED)
    td = c.T('difference')
    if c.on(td): txt(c, 540, 1180, 'which pipeline steps run again', td, 'intx', 42, INK)

def lanes(c):
    S = ('Layout', 'Paint', 'Composite')
    pipeline(c, 110, 520, set(S), c.T('geometry'), S, 250, 90, 50, 'width · height · top')
    tr = c.T('reflow')
    if c.on(tr): stamp(c.cv, 820, 400, 'REFLOW · $$$', 44, c.P(tr, 0.35), -3, RED)
    pipeline(c, 110, 820, {'Paint', 'Composite'}, c.T('color'), S, 250, 90, 50, 'color · background')
    tp = c.T('repaint')
    if c.on(tp): stamp(c.cv, 820, 700, 'REPAINT · $$', 44, c.P(tp, 0.35), -3, ORANGE)
    pipeline(c, 110, 1120, {'Composite'}, c.T('transform'), S, 250, 90, 50, 'transform · opacity')
    tc = c.T('composite', 2)
    if c.on(tc): stamp(c.cv, 820, 1000, 'COMPOSITE · $', 44, c.P(tc, 0.35), -3, GRN)

def analogy(c):
    rows = [('Move a wall', 're-measure the whole house', 'Moving', RED), ('Repaint a wall', 'just needs paint', 'Repainting', ORANGE),
            ('Slide a picture', 'needs neither', 'Sliding', GRN)]
    for i, (a, b, kw, col) in enumerate(rows):
        at = c.T(kw); y = 460 + i * 260
        if not c.on(at - 0.01): continue
        s = c.B(at, 0.4); c.sfx(at, 'pop')
        card(c.pen, 110, y - 95 * s, 970, y + 95 * s, 24, WHITE, 10, 5)
        c.pen.circ(210, y, 50 * s, fill=col, outline=INK, w=4)
        c.pen.text(300, y - 25, a, 'osw', 58 * s, INK, 'lm')
        c.pen.text(300, y + 38, b, 'ints', 32 * s, MUTE, 'lm')

def cascade(c):
    title(c, 'REFLOW IS CONTAGIOUS', 330, 0.1, 96, hlcol=(255, 180, 180))
    tw = c.T('wider')
    grow = c.P(tw, 0.6)
    ys = [470, 620, 770, 920]
    push = 0
    for i, y in enumerate(ys):
        h = 120 + (90 * grow if i == 0 else 0)
        yy = y + push
        hit = c.on(c.T('siblings')) and i > 0
        c.pen.rr(160, yy, 920, yy + h - 20, 14, fill=(255, 220, 220) if hit else WHITE, outline=RED if (i == 0 and c.on(tw)) else INK, w=5)
        c.pen.text(200, yy + (h - 20) / 2, ['card (made wider)', 'sibling', 'sibling', 'footer'][i], 'int', 30, INK, 'lm')
        if i == 0: push = 90 * grow
    tp = c.T('parent')
    if c.on(tp): c.pen.rr(130, 440, 950, 1080 + 90 * grow, 20, outline=PURPLE, w=5); c.pen.text(540, 1130 + 90 * grow, 'parent re-laid out too', 'int', 30, PURPLE)

def proof(c):
    box = browser(c, 90, 320, 990, 1080, url='news.example.com')
    c.pen.rect(130, 420, 950, 500, fill=INK)
    for k in range(4):
        c.pen.rect(130, 540 + k * 130, 600, 640 + k * 130, fill=LIGHT); c.pen.rect(630, 540 + k * 130, 950, 640 + k * 130, fill=(220, 220, 230))
    tf = c.T('flashing')
    if c.on(tf):
        k = int((c.t - tf) / 0.5) % 4
        c.pen.rect(130, 540 + k * 130, 600, 640 + k * 130, fill=(120, 230, 120), outline=GRN, w=5)
        if int(c.t * 3) % 2: c.pen.rect(630, 540 + ((k + 2) % 4) * 130, 950, 640 + ((k + 2) % 4) * 130, fill=(120, 230, 120), outline=GRN, w=5)
    tr = c.T('Rendering')
    if c.on(tr): label(c, 540, 1160, 'DevTools → Rendering → Paint flashing', tr, YEL, INK, 30)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    tr = c.T('reading')
    code(c, 80, 450, 1000, 760, ["el.style.width = '300px';  // write", 'const h = el.offsetHeight; // read'], tr, 0.4, 30, 'app.js',
         marks=[(1, c.T('offsetHeight'), YEL)], dy=(1 - c.P(tr - 0.45, 0.45)) * 900)
    ti = c.T('immediately')
    if c.on(ti):
        stamp(c.cv, 540, 860, 'FORCED LAYOUT', 64, c.P(ti, 0.4), -3, PURPLE)
        txt(c, 540, 990, 'the browser must lay out now, just to answer you', ti + 0.3, 'int', 34, INK)

SCENES = [
    (hook, "Change one CSS property, and your page stays smooth. Change another, and it stutters. The difference is which steps of the pipeline have to run again."),
    (lanes, "Change geometry, like width, height or top, and the browser runs layout, paint and composite. That's a reflow, the most expensive path. Change just a color or background, and it skips layout. That's a repaint. Change transform or opacity, and it can skip both, and only composite."),
    (analogy, "Moving a wall means re-measuring the whole house. Repainting a wall just needs paint. Sliding a picture along the wall needs neither."),
    (cascade, "And reflow is contagious. Make one element wider, and its siblings, its parent, and everything below it may need new positions too."),
    (proof, "Watch it happen. In DevTools, open Rendering and turn on paint flashing. Green flashes show what just got repainted."),
    (gotcha, "Interview trap: reading can trigger layout too. Change a style, then immediately read offsetHeight, and the browser has to run layout immediately, just to give you the answer."),
    (scene_next('S1 · E11', 'LAYOUT THRASHING', 'the silent lag in your loops', 'thrashing', 'lag'),
     "Next: layout thrashing, the silent lag hiding in your loops. Comment NOTES for the cheat sheet."),
]
