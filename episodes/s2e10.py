from engine.s2_extra import *

EP = dict(id='S2E10', tag='S2 · E10', short='VISIBLE, NOT CLICKABLE')

def hook(c):
    fill_page(c, phone(c, 540, 740, 440, 780), 'full')
    c.pen.rr(390, 960, 690, 1030, 16, fill=YEL, outline=INK, w=4); c.pen.text(540, 995, 'Buy now', 'int', 30, INK)
    for k, kw in enumerate(['tap', 'again', 'harder']):
        at = c.T(kw)
        if c.on(at) and c.t < at + 0.5:
            c.sfx(at, 'click'); r = 20 + 60 * c.P(at, 0.45)
            c.pen.circ(600, 1000, r, outline=mix(INK, PAPER, c.P(at, 0.45)), w=5)
        if c.on(at): c.pen.text(860, 820 + k * 70, ['tap…', 'tap…', 'TAP!'][k], 'intx', 40, RED)
    tn = c.T('nothing')
    if c.on(tn): stamp(c.cv, 540, 1250, 'DEAD BUTTON', 80, c.P(tn, 0.4), -4, RED)

def valley(c):
    title(c, 'THE UNCANNY VALLEY', 340, c.T('uncanny'), 92, hlcol=YEL)
    x0, x1, y = 100, 980, 820
    tl = c.T('looks')
    if c.on(tl):
        c.pen.line([(x0, y), (x0 + (x1 - x0) * c.P(tl, 0.6), y)], INK, 5)
    marker(c, x0 + 200, y + 120, y - 10, 'visible', c.T('visible'), GRN)
    marker(c, x0 + 720, y + 120, y - 10, 'interactive', c.T('interactive'), BLUE)
    tj = c.T('JavaScript')
    if c.on(tj):
        p = c.P(tj, 0.6)
        pts = [(x0 + 200 + 520 * i / 40, y - 20 - 200 * math.sin(math.pi * i / 40) * p) for i in range(41)]
        c.pen.line(pts, RED, 6)
        c.pen.text(x0 + 460, y - 250, 'looks ready · isn’t', 'intx', 38, RED)
        c.pen.text(x0 + 460, y - 190, 'JS loading / hydrating', 'int', 28, INK)

def metrics(c):
    tf = c.T('First')
    rows = [('FCP', 'First Contentful Paint', 'you first see something', 'First', GRN),
            ('TTI', 'Time to Interactive', 'it reliably responds', 'Interactive', BLUE),
            ('TBT', 'Total Blocking Time', 'the stuck time in between', 'Total', RED)]
    for i, (ab, name, sub, kw, col) in enumerate(rows):
        at = c.T(kw); y = 440 + i * 210
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        card(c.pen, 90, y - 80, 990, y + 80, 20, WHITE, 8, 4)
        c.pen.text(210, y, ab, 'osw', 70 * c.B(at, 0.35), col)
        c.pen.text(330, y - 24, name, 'intx', 38, INK, 'lm'); c.pen.text(330, y + 28, sub, 'intm', 30, MUTE, 'lm')
    tp = c.T('pulls')
    if c.on(tp): label(c, 540, 1110, 'SSR pulls FCP earlier — not necessarily TTI', tp, YEL, INK, 30)

def shutter(c):
    ts = c.T('shutter')
    if c.on(ts):
        c.pen.text(540, 350, 'SHUTTER HALF UP', 'osw', 72, INK)
        card(c.pen, 140, 440, 940, 1080, 14, (236, 240, 248), 10, 5)
        for k in range(3):
            c.pen.rr(200 + k * 250, 760, 380 + k * 250, 1060, 8, fill=[YEL, CYAN, PINK][k], outline=INK, w=3)
        h = 300 + 20 * math.sin(c.t * 2)
        for k in range(int(h / 30)):
            c.pen.rect(140, 440 + k * 30, 940, 440 + k * 30 + 26, fill=(150, 154, 162), outline=INK, w=2)
    tc = c.T("can't")
    if c.on(tc): label(c, 540, 1160, 'you can see in · you can’t walk in', tc, RED, WHITE, 32)

def proof(c):
    p = panel(c, 50, 330, 1030, 1150, ('Performance',), 0, (1 - c.P(0, 0.45)) * 900)
    tcpu = c.T('CPU')
    if c.on(tcpu):
        c.pen.rr(600, 440, 990, 490, 10, fill=(50, 56, 66), outline=YEL, w=3); c.pen.text(620, 465, 'CPU: 4x slowdown', 'int', 26, WHITE, 'lm')
    tr = c.T('record')
    filmstrip(c, 100, 560, 'Screenshots', ['white', 'full', 'full', 'full', 'full', 'full'], tr, 0.15, 128, 190, 22, mark=(1, c.T('first')))
    if c.on(tr + 0.5):
        c.pen.text(100, 860, 'Main', 'int', 28, WHITE, 'lm')
        for k, (a, b) in enumerate([(0.2, 0.45), (0.47, 0.72), (0.74, 0.9)]):
            xa, xb = 250 + 700 * a, 250 + 700 * b
            c.pen.rect(xa, 900, xa + (xb - xa) * c.P(tr + 0.5 + k * 0.3, 0.3), 960, fill=YEL, outline=INK, w=2)
            c.pen.poly([(xb - 16, 900), (xb, 900), (xb, 916)], fill=RED)
    tg = c.T('gap')
    if c.on(tg):
        c.pen.rr(282, 880, 900, 980, 10, outline=RED, w=5)
        label(c, 590, 1060, 'the valley', tg, RED, WHITE, 32)

def fixes(c):
    title(c, 'GETTING OUT', 340, c.T('Fixes'), 110, hlcol=YEL)
    items = [('ship less JavaScript', 'less'), ('split it per route', 'split'), ('hydrate what matters first', 'important'),
             ('defer widgets below the fold', 'defer'), ('or skip hydration where it’s static', 'skip')]
    for i, (s_, kw) in enumerate(items):
        at = c.T(kw); y = 500 + i * 120
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        c.pen.circ(150, y, 32 * c.B(at, 0.3), fill=INK); c.pen.text(150, y, str(i + 1), 'int', 32, WHITE)
        txt(c, 210, y, s_, at, 'intx', 42, INK, 'lm', 'slide')
    tn = c.T('next')
    if c.on(tn): label(c, 540, 1150, 'the next episodes = each of these', tn, YEL, INK, 30)

def gotcha(c):
    trap(c)
    qtext(c, 'Lighthouse is green. So users can click immediately?', 450, c.T('Lighthouse'), 46)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 640, 'NO', 110, c.P(tn, 0.35), -6, RED)
    tl = c.T('Lab')
    if c.on(tl):
        node(c, 280, 860, 330, 200, 'lab: 1 device', tl, 'laptop', size=30)
        node(c, 800, 860, 330, 200, 'field: real phones', c.T('Real'), 'phone', size=30)
    ti = c.T('Interaction')
    if c.on(ti): label(c, 540, 1080, 'check field INP (Interaction to Next Paint)', ti, GRN, WHITE, 30)

SCENES = [
    (hook, "You've done this. A page appears, you tap a button, and nothing. You tap again. You tap harder. Still nothing."),
    (valley, "That gap has a name: the uncanny valley. The page looks ready, so it's visible. But it isn't interactive yet, because the JavaScript is still loading or hydrating."),
    (metrics, "Three numbers describe it. First Contentful Paint, when you first see something. Time to Interactive, when it reliably responds. And Total Blocking Time, the stuck time in between. Server rendering pulls the first one earlier, but not necessarily the second."),
    (shutter, "It's a shop with the shutter half up. You can see everything inside, but you can't walk in yet."),
    (proof, "To see it, set the CPU to a four times slowdown in DevTools Performance, and record a reload. Find the first screenshot with content, then look at the long tasks that follow. That gap is the valley."),
    (fixes, "Fixes: ship less JavaScript, split it, hydrate the important parts first, defer widgets below the fold, or skip hydration where the page is static. The next episodes cover each one."),
    (gotcha, "Interview trap: Lighthouse is green, so users can click immediately? No. Lab tests run on one device. Real users on cheap phones stay in the valley much longer. Check field data, like Interaction to Next Paint."),
    (scene_next('S2 · E11', 'SELECTIVE HYDRATION', 'hydrate what the user touches first', 'selective', 'touches'),
     "Next: selective hydration. Hydrate what the user touches first. Comment NOTES for the cheat sheet."),
]
