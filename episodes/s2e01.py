from engine.s2_extra import *

EP = dict(id='S2E01', tag='S2 · E01', short='WHITE SCREEN FIRST')

def hook(c):
    label(c, 540, 300, 'Slow 4G · same phone', 0.1, INK, WHITE, 30)
    ts, tsp, tf = c.T('second'), c.T('spinner'), c.T('finally')
    for cx, name, st in [(290, 'Amazon', 'full' if c.on(ts) else 'white'),
                         (790, 'typical SPA', 'full' if c.on(tf) else ('spinner' if c.on(tsp) else 'white'))]:
        c.pen.text(cx, 390, name, 'intx', 40, INK)
        fill_page(c, phone(c, cx, 790, 380, 700), st)
    if c.on(ts): label(c, 290, 1185, 'content ~1 s', ts, GRN, WHITE, 28)
    if c.on(tf): label(c, 790, 1185, 'content later', tf, RED, WHITE, 28)
    tm = c.T('Same')
    if c.on(tm): stamp(c.cv, 540, 1290, 'WHY?', 90, c.P(tm, 0.4), -5, RED)

def problem(c):
    title(c, 'WHO BUILDS THE HTML?', 360, c.T('who'), 92, hlcol=YEL)
    th = c.T('HTML')
    if c.on(th): icon(c.pen, 'doc', 540, 700, 1.7 * c.B(th, 0.4))
    a = node(c, 220, 700, 260, 220, 'server', c.T('server'), 'server', size=34)
    b = node(c, 860, 700, 260, 220, 'browser', c.T('browser'), 'laptop', size=34)
    if c.on(c.T('server')):
        arrow(c.pen, 360, 700, 470, 700, c.P(c.T('server'), 0.4), INK, 6, 20)
        label(c, 220, 880, 'before sending', c.T('before'), YEL, INK, 28)
    if c.on(c.T('browser')):
        arrow(c.pen, 720, 700, 610, 700, c.P(c.T('browser'), 0.4), INK, 6, 20)
        label(c, 860, 880, 'after arriving', c.T('after'), YEL, INK, 28)
    txt(c, 540, 1060, 'every strategy this season = an answer to this', c.T('arrives'), 'ints', 34, MUTE)

def table(pen, cx, cy, s=1.0):
    pen.rr(cx - 120 * s, cy - 50 * s, cx + 120 * s, cy - 24 * s, 6, fill=(190, 140, 90), outline=INK, w=4)
    for dx in (-95, 85):
        pen.rect(cx + dx * s, cy - 24 * s, cx + (dx + 12) * s, cy + 80 * s, fill=(160, 110, 70), outline=INK, w=3)

def flatbox(pen, cx, cy, s=1.0):
    pen.rr(cx - 130 * s, cy - 70 * s, cx + 130 * s, cy + 80 * s, 8, fill=(214, 180, 130), outline=INK, w=4)
    pen.rect(cx - 16 * s, cy - 70 * s, cx + 16 * s, cy + 80 * s, fill=(240, 220, 170))

def analogy(c):
    ta, tb = c.T('assembled'), c.T('flat')
    if c.on(ta):
        card(c.pen, 70, 380, 520, 1060, 26, WHITE, 12, 5)
        c.pen.text(295, 450, 'DELIVERED BUILT', 'osw', 44, INK)
        table(c.pen, 295, 700, 1.2 * c.B(ta, 0.4))
        verdict(c, 295, 950, True, c.T('use'), 1.6)
        txt(c, 295, 1020, 'use it immediately', c.T('use'), 'ints', 30, GRN)
    if c.on(tb):
        card(c.pen, 560, 380, 1010, 1060, 26, WHITE, 12, 5)
        c.pen.text(785, 450, 'FLAT-PACK', 'osw', 44, INK)
        flatbox(c.pen, 785, 680, c.B(tb, 0.4))
        tbl = c.T('build')
        if c.on(tbl):
            timerbar(c, 610, 850, 960, c.P(tbl, 2.5, lambda x: x), tbl, None, ORANGE, 44)
            txt(c, 785, 950, 'read · build · then use', tbl, 'ints', 30, INK)
    tw = c.T('waiting')
    if c.on(tw): stamp(c.cv, 785, 1150, 'WAITING AT HOME', 52, c.P(tw, 0.4), 4, RED)

def how(c):
    x0, x1 = 100, 980
    txt(c, x0, 440, 'Server rendered', c.T('server'), 'intx', 40, BLUE, 'lm')
    seg_row(c, x0, 480, x1, [('HTML + content', 0, 0.36, CYAN, c.T('arrives')), ('JS → interactive', 0.36, 0.72, YEL, c.T('JavaScript'))])
    marker(c, x0 + (x1 - x0) * 0.36, 600, 470, 'FIRST PAINT', c.T('paints'))
    y = 860
    txt(c, x0, y - 40, 'Client rendered', c.T('client'), 'intx', 40, RED, 'lm')
    seg_row(c, x0, y, x1, [('HTML', 0, 0.12, CYAN, c.T('empty')), ('download JS', 0.12, 0.45, YEL, c.T('downloads')),
                           ('run JS', 0.45, 0.66, ORANGE, c.T('runs')), ('fetch data', 0.66, 0.88, PURPLE, c.T('fetches'))])
    marker(c, x0 + (x1 - x0) * 0.88, 980, 850, 'FIRST PAINT', c.T('anything'), RED)
    tt = c.T('only')
    if c.on(tt):
        arrow(c.pen, x0 + 20, 1110, x0 + (x1 - x0) * 0.88 - 10, 1110, c.P(tt, 0.6), RED, 6, 20)
        txt(c, 540, 1170, 'white screen the whole time', tt + 0.3, 'ints', 32, RED)

def proof(c):
    p = panel(c, 60, 330, 1020, 1260, ('Elements', 'Network', 'Performance'), 2, (1 - c.P(0, 0.45)) * 900)
    tsc, tsl = c.T('Screenshots'), c.T('slow')
    if c.on(tsc):
        c.pen.rr(110, 460, 146, 496, 6, fill=YEL, outline=WHITE, w=3); check(c.pen, 128, 478, 0.35, INK, 6, c.P(tsc, 0.3))
        c.pen.text(166, 478, 'Screenshots', 'int', 28, WHITE, 'lm')
    if c.on(tsl):
        c.pen.rr(560, 456, 960, 500, 10, fill=(50, 56, 66), outline=YEL, w=3)
        c.pen.text(580, 478, 'Network: Slow 4G', 'int', 26, WHITE, 'lm')
    tr, tw = c.T('reload'), c.T('white')
    filmstrip(c, 110, 610, 'Amazon', ['white', 'full', 'full', 'full', 'full'], tr, mark=(1, tw))
    filmstrip(c, 110, 960, 'typical SPA', ['white', 'white', 'spinner', 'spinner', 'full'], tr + 0.4, mark=(4, tw))

def gotcha(c):
    trap(c)
    qtext(c, 'Is a white screen always the network’s fault?', 450, c.T('white'), 46)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 640, 'NO', 110, c.P(tn, 0.35), -6, RED)
    tb = c.T('budget')
    if c.on(tb):
        icon(c.pen, 'phone', 200, 860, 1.6 * c.B(tb, 0.4))
        label(c, 200, 990, 'fast Wi-Fi', c.T('fast'), GRN, WHITE, 26)
        tp = c.T('parsing')
        if c.on(tp):
            c.pen.rect(330, 830, 330 + 640 * c.P(tp, 2.0, lambda x: x), 900, fill=RED, outline=INK, w=3)
            c.pen.text(350, 865, 'parse + run 2 MB bundle', 'int', 28, WHITE, 'lm')
        txt(c, 650, 950, 'can take seconds on a cheap CPU', c.T('seconds'), 'ints', 32, INK)
    tt = c.T('throttle')
    if c.on(tt):
        chips(c, 140, 1120, [('CPU: 4x slowdown', YEL), ('Network: Slow 4G', CYAN)], tt, 0.4, 32)

SCENES = [
    (hook, "Open Amazon on slow 4G, next to a typical single page app. Amazon shows products in about a second. The app shows a white screen, then a spinner, then finally the page. Same phone. Same network. So why?"),
    (problem, "The difference is who builds the page. In the end, every page is HTML. The only question is where that HTML is made. On the server, before it's sent? Or in the browser, by JavaScript, after it arrives?"),
    (analogy, "Think about buying a table. One shop delivers it assembled. The moment it arrives, you can use it. Another sends a flat pack box. You read the instructions, and build it yourself. Same table in the end. One just keeps you waiting at home."),
    (how, "With server rendering, the HTML arrives with content, so the browser paints it right away, and JavaScript loads afterwards to make it interactive. With client rendering, the HTML arrives empty. The browser downloads the JavaScript, runs it, often fetches data, and only then paints anything."),
    (proof, "See it yourself. Open DevTools, go to Performance, tick Screenshots, set the network to slow 4G, and reload. The filmstrip shows exactly when each site stops being white."),
    (gotcha, "Interview trap: is a white screen always the network's fault? No. On a budget phone, even on fast wifi, parsing and running a big JavaScript bundle can take seconds. So throttle the CPU too, not just the network."),
    (scene_next('S2 · E02', 'CLIENT-SIDE RENDERING', 'the mystery of the empty div', 'client', 'mystery'),
     "This whole season is about that one choice. Next: client side rendering, and the mystery of the empty div. Comment NOTES for the cheat sheet."),
]
