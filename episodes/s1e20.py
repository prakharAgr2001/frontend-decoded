from engine.lib import *

EP = dict(id='S1E20', tag='S1 · E20', short='BUBBLING & CAPTURING')

LAYERS = [('window', 110, 380, 970, 1200), ('document', 160, 450, 920, 1150), ('body', 210, 520, 870, 1100), ('.card', 270, 600, 810, 1040), ('button', 380, 760, 700, 900)]

def nest(c, hi=None, fills=None):
    for i, (nm, x0, y0, x1, y1) in enumerate(LAYERS):
        f = (fills or {}).get(nm, WHITE if i % 2 else (248, 245, 238))
        c.pen.rr(x0, y0, x1, y1, 20, fill=f, outline=YEL if hi == nm else INK, w=7 if hi == nm else 4)
        c.pen.text(x0 + 22, y0 + 30, nm, 'monob', 26, INK, 'lm')

def dot_path(c, t0, t1, up=False):
    ys = [400, 470, 540, 620, 830]
    if not (t0 <= c.t <= t1): return
    q = lin(c.t, t0, t1)
    if up: q = 1 - q
    idx = q * (len(ys) - 1); i = min(int(idx), len(ys) - 2); f = idx - i
    y = ys[i] + (ys[i + 1] - ys[i]) * f
    c.pen.circ(540, y, 24, fill=BLUE if not up else ORANGE, outline=INK, w=4)

def hook(c):
    nest(c)
    tc = c.T('Click')
    if c.on(tc):
        c.pen.circ(540, 830, 30 * c.B(tc, 0.3), fill=YEL, outline=INK, w=4)
    tv = c.T('visited')
    dot_path(c, tv, tv + 1.0); dot_path(c, tv + 1.1, tv + 2.1, True)
    tt = c.T('Twice')
    if c.on(tt): stamp(c.cv, 540, 1290, 'TWICE', 80, c.P(tt, 0.35), -4, RED)

def phases(c):
    tc, tt, tb = c.T('Capture'), c.T('Target', 2), c.T('Bubble')
    hi = None
    nest(c)
    dot_path(c, tc, tc + 1.6)
    if c.on(tt) and not c.on(tb): c.pen.circ(540, 830, 40, fill=YEL, outline=INK, w=5)
    dot_path(c, tb, tb + 1.6, True)
    for i, (lab, col, at) in enumerate([('1 · CAPTURE ↓', BLUE, tc), ('2 · TARGET', YEL, tt), ('3 · BUBBLE ↑', ORANGE, tb)]):
        if c.on(at): pill(c.pen, 220 + i * 320, 1290, lab, c.B(at, 0.3), col, INK if col == YEL else WHITE, 30, outline=None)

def pond(c):
    for k in range(5):
        y = 480 + k * 150
        c.pen.rect(110, y, 970, y + 150, fill=mix((210, 230, 250), (60, 100, 160), k / 5))
    ts = c.T('sinks')
    if c.on(ts):
        q = lin(c.t, ts, ts + 1.5); y = 480 + q * 700
        c.pen.ell(500, y - 30, 580, y + 30, fill=GREY, outline=INK, w=4)
    tr = c.T('ripples')
    if c.on(tr):
        for k in range(3):
            r = 60 + ((c.t - tr) * 120 + k * 60) % 200
            c.pen.ell(540 - r, 480 - r * 0.25, 540 + r, 480 + r * 0.25, outline=WHITE, w=4)
    txt(c, 540, 400, 'down through the layers… and back up', c.T('stone'), 'intx', 40, INK)

def codes(c):
    code(c, 40, 340, 1040, 640, ["card.addEventListener('click', fn);", "card.addEventListener('click', fn,", "                      { capture: true });"],
         c.T('default'), 0.25, 28, 'events.js', marks=[(0, c.T('bubble'), (230, 140, 60)), (2, c.T('capture'), (52, 86, 168))])
    if c.on(c.T('bubble')): label(c, 300, 760, '→ bubble phase (default)', c.T('bubble'), ORANGE, WHITE, 30)
    if c.on(c.T('capture')): label(c, 760, 860, '→ capture phase', c.T('capture'), BLUE, WHITE, 30)

def stopprevent(c):
    for j, (nm, kw, line1, line2, col) in enumerate([('stopPropagation()', 'stopPropagation', 'stops the journey', 'ancestors never hear it', RED),
                                                     ('preventDefault()', 'preventDefault', 'stops the default action', 'no link follow / form submit', BLUE)]):
        at = c.T(kw); y = 500 + j * 330
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.4)
        card(c.pen, 100, y - 120 * s, 980, y + 120 * s, 24, WHITE, 10, 5)
        c.pen.text(140, y - 50, nm, 'monob', 46 * s, col, 'lm')
        c.pen.text(140, y + 20, line1, 'intx', 38 * s, INK, 'lm')
        c.pen.text(140, y + 70, line2, 'int', 30 * s, MUTE, 'lm')
    tu = c.T('unrelated')
    if c.on(tu): stamp(c.cv, 540, 1180, 'UNRELATED', 70, c.P(tu, 0.35), -3, INK)

def targets(c):
    tt, tc = c.T('target'), c.T('currentTarget')
    nest(c, hi='.card' if c.on(tc) else None, fills={'button': YEL} if c.on(tt) else None)
    if c.on(tt): label(c, 540, 960, 'event.target = button (what was clicked)', tt, YEL, INK, 28)
    if c.on(tc): label(c, 540, 1270, 'event.currentTarget = .card (whose listener runs)', tc, INK, WHITE, 26)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Does every event bubble?', c.T('every'), 'intx', 50, INK)
    chips(c, 140, 620, [('focus', (255, 210, 210)), ('blur', (255, 210, 210)), ('mouseenter', (255, 210, 210)), ('mouseleave', (255, 210, 210))], c.T('focus'), 0.3, 40)
    tf = c.T('focusin')
    if c.on(tf): chips(c, 200, 880, [('focusin', (190, 240, 200)), ('focusout', (190, 240, 200))], tf, 0.3, 44); c.pen.text(540, 800, 'bubbling versions:', 'int', 32, GRN)

SCENES = [
    (hook, "Click a button, inside a card, inside a page. You clicked one thing, but the click event visited every element around it. Twice."),
    (phases, "Every event travels in three phases. Capture: down from the window to the target. Target: at the element you clicked. Bubble: back up to the window."),
    (pond, "Like dropping a stone into a pond. It sinks down through the layers, and the ripples come back up."),
    (codes, "By default, listeners fire on the way back up, in the bubble phase. Pass capture true to listen on the way down, in the capture phase."),
    (stopprevent, "Two methods people mix up. stopPropagation stops the journey, so ancestors never hear the event. preventDefault stops the browser's default action, like following a link or submitting a form. They're unrelated."),
    (targets, "And inside a handler, event dot target is what was actually clicked. Event dot currentTarget is the element whose listener is running."),
    (gotcha, "Interview trap: does every event bubble? No. Focus, blur, mouseenter and mouseleave don't. That's why focusin and focusout exist."),
    (scene_next('S1 · E21', 'DELEGATION', 'one listener instead of a thousand', 'delegation', 'thousand'),
     "Next: event delegation, one listener instead of a thousand. Comment NOTES for the cheat sheet."),
]
