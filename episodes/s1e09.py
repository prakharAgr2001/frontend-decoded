from engine.lib import *

EP = dict(id='S1E09', tag='S1 · E09', short='LAYOUT → PAINT')

def hook(c):
    node(c, 290, 520, 360, 240, 'DOM', 0.1, 'doc')
    node(c, 790, 520, 360, 240, 'CSSOM', 0.3, 'eye')
    tp = c.T('pixels')
    if c.on(tp):
        arrow(c.pen, 540, 680, 540, 820, c.P(tp, 0.3), INK, 7, 26)
        for i in range(10):
            for j in range(6):
                at = tp + 0.3 + (i + j) * 0.03
                if c.on(at): c.pen.rect(240 + i * 60, 860 + j * 40, 290 + i * 60, 892 + j * 40, fill=[YEL, BLUE, RED, GRN, CYAN][(i * 3 + j) % 5])
    t60 = c.T('sixty')
    if c.on(t60): label(c, 540, 1180, '60 frames every second', t60, RED, WHITE, 34)

def house(c):
    rows = [('render tree', 'pick the rooms', 'pick'), ('layout', 'measure them', 'measure'), ('paint', 'paint the walls', 'paint'), ('composite', 'arrange the furniture', 'arrange')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw); y = 420 + i * 200
        if not c.on(at - 0.01): continue
        s = c.B(at, 0.4); c.sfx(at, 'pop')
        card(c.pen, 90, y - 70 * s, 520, y + 70 * s, 20, WHITE, 8, 4)
        c.pen.text(305, y, b, 'intx', 38 * s, INK)
        arrow(c.pen, 540, y, 620, y, c.P(at + 0.15, 0.3), INK, 6, 20)
        c.pen.rr(640, y - 55 * s, 990, y + 55 * s, 55 * s, fill=YEL, outline=INK, w=4)
        c.pen.text(815, y, a, 'osw', 50 * s, INK)

def rtree(c):
    title(c, '1 · RENDER TREE', 320, 0.1, 100, hlcol=YEL)
    tv = c.T('visible')
    items = [('header', True), ('nav', True), ('.modal { display: none }', False), ('main', True), ('footer', True)]
    for i, (nm, keep) in enumerate(items):
        y = 480 + i * 115; at = 0.4 + i * 0.12
        if not c.on(at): continue
        gone = not keep and c.on(tv)
        col = (255, 220, 220) if not keep else WHITE
        p = 1 - c.P(c.T('skipped'), 0.5) if gone else 1
        if p <= 0.02: continue
        card(c.pen, 160, y - 45, 160 + 760 * (1 if keep else p), y + 45, 16, col, 6, 4)
        c.pen.text(200, y, nm, 'monob', 32, INK, 'lm')
        if not keep and c.on(tv): cross(c.pen, 880, y, 0.9, RED, 8, c.P(tv, 0.3))
    txt(c, 540, 1110, 'only visible things make it in', tv, 'intx', 40, INK)

def layout(c):
    title(c, '2 · LAYOUT', 320, 0.1, 100, hlcol=YEL)
    boxes = [(110, 440, 970, 540, 'header  w:860 h:100'), (110, 570, 330, 1050, 'nav  w:220'), (360, 570, 970, 1050, 'main  w:610 h:480')]
    te = c.T('exact')
    for i, (a, b, x2, y2, lab) in enumerate(boxes):
        at = te + i * 0.3
        if not c.on(at): continue
        c.sfx(at, 'tick'); p = c.P(at, 0.4)
        c.pen.rect(a, b, a + (x2 - a) * p, b + (y2 - b) * p, outline=PURPLE, w=4)
        if p > 0.9: c.pen.text(a + 16, b + 30, lab, 'monob', 24, PURPLE, 'lm')
    tw = c.T('width')
    if c.on(tw):
        q = c.P(tw, 0.5)
        c.pen.rect(110, 570, 330 + 80 * q, 1050, outline=RED, w=6)
        c.pen.text(540, 1130, 'change a width → layout runs again', 'intx', 36, RED)

def paint(c):
    title(c, '3 · PAINT', 320, 0.1, 100, hlcol=YEL)
    tf = c.T('Fill')
    p = c.P(tf, 1.5, lambda x: x)
    c.pen.rect(110, 440, 110 + 860 * min(1, p * 3), 540, fill=INK)
    if p > 0.2: c.pen.text(140, 490, 'Frontend Decoded', 'intx', 40, WHITE, 'lm')
    c.pen.rect(110, 570, 330, 570 + 480 * cl(p * 2 - 0.3), fill=(236, 233, 226))
    if p > 0.5:
        c.pen.rect(360, 570, 970, 1050, fill=WHITE, outline=GREY, w=2)
        c.pen.text(400, 620, 'Headline text', 'intx', 40, INK, 'lm')
    if p > 0.7:
        c.pen.rr(400, 680, 930, 960, 16, fill=YEL); icon(c.pen, 'eye', 665, 820, 1.2)
    for i, (w, kw) in enumerate([('text', 'text'), ('colors', 'colors'), ('borders', 'borders'), ('shadows', 'shadows'), ('images', 'images')]):
        at = c.T(kw)
        if c.on(at):
            c.sfx(at, 'tick'); pill(c.pen, 175 + i * 182, 1140, w, c.B(at, 0.3), GRN, WHITE, 26, outline=None)

def composite(c):
    title(c, '4 · COMPOSITE', 320, 0.1, 100, hlcol=YEL)
    tl = c.T('layers')
    cols = [(236, 233, 226), (200, 220, 250), (255, 236, 170)]
    labs = ['background', 'content', 'sticky header']
    for i in range(3):
        at = tl + i * 0.3
        if not c.on(at): continue
        merge = c.P(c.T('stacks'), 0.8)
        y = 560 + i * 170 * (1 - merge) + (100 + i * 22) * merge
        x = 200 + i * 60 * (1 - merge) + i * 22 * merge
        c.pen.poly([(x, y + 220), (x + 560, y + 220), (x + 680, y), (x + 120, y)], fill=cols[i], outline=INK, w=4)
        c.pen.text(x + 340, y + 110, labs[i], 'int', 30, INK)
    tg = c.T('GPU')
    if c.on(tg): icon(c.pen, 'gpu', 880, 470, 1.1); txt(c, 880, 560, 'GPU', tg, 'int', 30, INK)
    tp = c.T('projector')
    if c.on(tp): label(c, 540, 1180, 'like transparent sheets on a projector', tp, YEL, INK, 30)

def proof(c):
    box = panel(c, 60, 330, 1020, 1000, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('Record')
    blocks = [(0.0, 0.18, 0, 'JS'), (0.18, 0.08, 0, 'Style'), (0.26, 0.14, 0, 'Layout'), (0.40, 0.12, 0, 'Paint'), (0.52, 0.06, 0, 'Composite'),
              (0.62, 0.12, 1, 'JS'), (0.74, 0.1, 1, 'Layout'), (0.84, 0.1, 1, 'Paint')]
    flame(c, 100, 500, 980, blocks, tr, 64)
    tpu = c.T('purple')
    if c.on(tpu): label(c, 300, 760, 'purple = layout', tpu, PURPLE, WHITE, 30)
    tg = c.T('green')
    if c.on(tg): label(c, 760, 760, 'green = paint', tg, GRN, WHITE, 30)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    for j, (nm, kw, keep) in enumerate([('display: none', 'removes', False), ('visibility: hidden', 'keeps', True)]):
        at = c.T(kw); x0 = 90 + j * 470
        if not c.on(at - 0.01):
            continue
        c.sfx(at, 'pop')
        card(c.pen, x0, 470, x0 + 430, 1080, 22, WHITE, 10, 5)
        c.pen.text(x0 + 215, 520, nm, 'monob', 30, INK)
        for k in range(3):
            y = 600 + k * 150
            if k == 1:
                if keep: c.pen.rr(x0 + 40, y, x0 + 390, y + 120, 12, outline=GREY, w=4); c.pen.text(x0 + 215, y + 60, 'space kept', 'int', 26, MUTE)
                continue
            yy = y if (keep or k == 0) else y - 150 * c.P(at + 0.3, 0.5)
            c.pen.rr(x0 + 40, yy, x0 + 390, yy + 120, 12, fill=YEL, outline=INK, w=4)
        c.pen.text(x0 + 215, 1040, 'no box, nothing takes space' if not keep else 'invisible, still takes space', 'int', 24, RED if not keep else GRN)

SCENES = [
    (hook, "Your browser now has two trees. It has to turn them into pixels, up to sixty times a second when anything moves. Here's the assembly line."),
    (house, "Think of building a house. First pick the rooms. Then measure them. Then paint the walls. Then arrange the furniture."),
    (rtree, "Step one: the render tree. The browser combines the DOM and CSSOM, and keeps only visible things. Anything with display none is skipped completely."),
    (layout, "Step two: layout. The browser calculates the exact size and position of every box. Change a width, and this runs again."),
    (paint, "Step three: paint. Fill in the pixels. Text, colors, borders, shadows and images."),
    (composite, "Step four: composite. The page is split into layers, and the GPU stacks them into the final frame, like transparent sheets on a projector."),
    (proof, "Record a reload in the Performance panel and you'll see the whole line. Purple blocks are layout. Green blocks are paint."),
    (gotcha, "Interview question: display none versus visibility hidden. Display none removes the element from the render tree, so it takes no space. Visibility hidden keeps its space, it's just invisible."),
    (scene_next('S1 · E10', 'REFLOW vs REPAINT', 'why some CSS changes cost more', 'reflow', 'cost'),
     "Next: reflow versus repaint, and why some CSS changes cost more than others. Comment NOTES for the cheat sheet."),
]
