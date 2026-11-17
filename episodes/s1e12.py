from engine.lib import *

EP = dict(id='S1E12', tag='S1 · E12', short='SMOOTH ANIMATION')

def track(c, y, lab, smooth, t0, col):
    c.pen.text(110, y - 80, lab, 'monob', 32, INK, 'lm')
    c.pen.rect(110, y - 50, 970, y + 70, fill=LIGHT)
    if c.t < t0: return
    q = ((c.t - t0) * 0.45) % 1.0
    q = eio(q * 2) if q < 0.5 else eio(2 - q * 2)
    if not smooth: q = math.floor(q * 9) / 9
    x = 130 + q * 720
    c.pen.rr(x, y - 30, x + 110, y + 50, 14, fill=col, outline=INK, w=4)

def hook(c):
    track(c, 520, 'left: 0 → 700px', False, 0.2, RED)
    track(c, 860, 'transform: translateX(700px)', True, 0.2, GRN)
    tg, ts = c.T('glides'), c.T('stutters')
    if c.on(tg): stamp(c.cv, 850, 760, 'GLIDES', 40, c.P(tg, 0.3), -4, GRN)
    if c.on(ts): stamp(c.cv, 850, 420, 'STUTTERS', 40, c.P(ts, 0.3), -4, RED)
    tl = c.T('line')
    if c.on(tl): label(c, 540, 1120, 'one line of CSS', tl, YEL, INK, 36)

def why(c):
    S = ('JS', 'Layout', 'Paint', 'Composite')
    pipeline(c, 60, 520, set(S[1:]), c.T('left'), S, 220, 86, 26, 'animating left → every frame')
    tm = c.T('main')
    if c.on(tm): txt(c, 540, 650, 'all on the busy main thread', tm, 'int', 34, RED)
    pipeline(c, 60, 900, {'Composite'}, c.T('transform'), S, 220, 86, 26, 'animating transform → every frame')
    tc = c.T('compositor')
    if c.on(tc): txt(c, 540, 1030, 'only the compositor works', tc, 'int', 34, GRN)

def layers(c):
    card(c.pen, 110, 360, 970, 1100, 20, WHITE, 10, 5)
    for k in range(6): c.pen.rect(160, 420 + k * 100, 920, 470 + k * 100, fill=LIGHT)
    tl = c.T('layer')
    if c.on(tl):
        q = ((c.t - tl) * 0.35) % 1.0
        q = eio(q * 2) if q < 0.5 else eio(2 - q * 2)
        x = 170 + q * 520
        c.pen.rr(x + 10, 640 + 12, x + 230 + 10, 860 + 12, 20, fill=(0, 0, 0))
        c.pen.rr(x, 640, x + 230, 860, 20, fill=YEL, outline=INK, w=5)
        c.pen.text(x + 115, 750, 'own layer', 'intx', 34, INK)
    tb = c.T('busy')
    if c.on(tb):
        c.pen.text(110, 1170, 'main thread', 'int', 30, INK, 'lm')
        c.pen.rect(330, 1150, 330 + 640 * c.P(tb, 0.6), 1195, fill=RED, outline=INK, w=3)
        c.pen.text(650, 1172, 'BUSY', 'osw', 34, WHITE)
        txt(c, 540, 1260, '…the layer still moves', tb + 0.5, 'intx', 36, GRN)

def sticker(c):
    for j, (lab, kw, ok) in enumerate([('erase + redraw every frame', 'erasing', False), ('slide the sticker', 'sticker', True)]):
        at = c.T(kw); x0 = 90 + j * 470
        if not c.on(at - 0.01): continue
        card(c.pen, x0, 450, x0 + 430, 950, 22, WHITE, 10, 5)
        c.pen.text(x0 + 215, 1010, lab, 'int', 30, RED if not ok else GRN)
        q = ((c.t - at) * 0.6) % 1.0
        if ok:
            c.pen.rr(x0 + 60 + q * 220, 640, x0 + 160 + q * 220, 740, 16, fill=YEL, outline=INK, w=4)
        else:
            k = int(q * 6)
            c.pen.rr(x0 + 60 + k * 44, 640, x0 + 160 + k * 44, 740, 16, outline=INK, w=4)
            for e in range(k): c.pen.rr(x0 + 60 + e * 44, 640, x0 + 160 + e * 44, 740, 16, outline=GREY, w=2)

def willchange(c):
    code(c, 100, 360, 980, 560, ['.card {', '  will-change: transform;', '}'], c.T('will'), 0.15, 34, 'styles.css', marks=[(1, c.T('will') + 0.4, YEL)], lang='css')
    te = c.T('everything')
    if c.on(te):
        stamp(c.cv, 540, 660, "DON'T PUT IT ON EVERYTHING", 46, c.P(te, 0.35), -3, RED)
    tg = c.T('GPU')
    if c.on(tg):
        for k in range(12):
            at = tg + k * 0.1
            if c.on(at): c.pen.rr(140 + (k % 6) * 140, 780 + (k // 6) * 120, 250 + (k % 6) * 140, 870 + (k // 6) * 120, 12, fill=YEL, outline=INK, w=3)
        c.pen.text(110, 1080, 'GPU memory', 'int', 30, INK, 'lm')
        f = lin(c.t, tg, tg + 1.2)
        c.pen.rr(330, 1060, 970, 1100, 20, outline=INK, w=4)
        c.pen.rr(334, 1064, 334 + 632 * f, 1096, 16, fill=RED if f > 0.8 else ORANGE)

def proof(c):
    title(c, 'FRAME RENDERING STATS', 330, 0.1, 80)
    for j, (lab, fps, kw, col) in enumerate([('animating left', 34, 'compare', RED), ('animating transform', 60, 'compare', GRN)]):
        at = c.T(kw) + j * 0.6
        if not c.on(at): continue
        x0 = 90 + j * 470
        darkcard(c.pen, x0, 480, x0 + 430, 900)
        c.pen.text(x0 + 215, 540, lab, 'int', 28, WHITE)
        counter(c, x0 + 215, 690, 0, fps, at, at + 0.8, '{:.0f}', 150, col)
        c.pen.text(x0 + 215, 820, 'fps', 'int', 34, (150, 156, 166))
    tr = c.T('Rendering')
    if c.on(tr): label(c, 540, 1010, 'DevTools → Rendering → Frame Rendering Stats', tr, YEL, INK, 28)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'What is cheap to animate?', c.T('cheap'), 'intx', 48, INK)
    chips(c, 160, 600, [('transform', (190, 240, 200)), ('opacity', (190, 240, 200))], c.T('Transform'), 0.4, 40)
    chips(c, 110, 820, [('width', (255, 210, 210)), ('height', (255, 210, 210)), ('top', (255, 210, 210)), ('left', (255, 210, 210))], c.T('Width'), 0.3, 40)
    if c.on(c.T('Transform')): c.pen.text(110, 530, 'cheap → compositor only', 'int', 32, GRN, 'lm')
    if c.on(c.T('Width')): c.pen.text(110, 750, 'expensive → layout every frame', 'int', 32, RED, 'lm')

SCENES = [
    (hook, "Two boxes slide across the screen. One glides. One stutters. The only difference is a single line of CSS."),
    (why, "Animating left changes geometry, so every frame runs layout, paint and composite, all on the busy main thread. Animating transform only needs the compositor."),
    (layers, "The browser can promote an element to its own layer. The GPU then moves that layer around without repainting anything, and it keeps moving even when the main thread is busy."),
    (sticker, "It's the difference between erasing and redrawing a drawing every frame, and simply sliding a sticker across the page."),
    (willchange, "You can hint it with will-change: transform. But don't put it on everything. Every extra layer costs GPU memory."),
    (proof, "Measure it yourself. Open the Rendering panel, turn on frame rendering stats, and compare the two animations."),
    (gotcha, "Interview question: which properties are cheap to animate? Transform and opacity. Width, height, top and left trigger layout, so avoid animating them."),
    (scene_next('S1 · E13', 'INTERVIEW Qs', 'the rendering pipeline: test yourself', 'interview', 'pipeline'),
     "Next: interview questions on the rendering pipeline. Comment NOTES for the cheat sheet."),
]
