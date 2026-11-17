from engine.lib import *

EP = dict(id='S1E14', tag='S1 · E14', short='ONE-CHEF KITCHEN')

def hook(c):
    console(c, 70, 300, 1010, 560, [(0.3, 'const end = Date.now() + 3000;', CYAN), (0.6, 'while (Date.now() < end) {}', CYAN)])
    ts = c.T('scroll')
    browser(c, 120, 640, 960, 1150, url='any-site.example')
    for k in range(4): c.pen.rect(170, 760 + k * 90, 910, 820 + k * 90, fill=LIGHT)
    if c.on(ts):
        y = 900 + 30 * math.sin((c.t - ts) * 8)
        c.pen.circ(820, y, 26, fill=YEL, outline=INK, w=4)
        arrow(c.pen, 820, y + 40, 820, y + 110, 1, INK, 5, 16)
    tf = c.T('frozen')
    if c.on(tf): stamp(c.cv, 540, 900, 'FROZEN', 100, c.P(tf, 0.4), -6, BLUE)

def chef(c):
    icon(c.pen, 'chef', 540, 640, 3.2 * c.B(0.1, 0.5))
    c.pen.rr(380, 760, 700, 840, 14, fill=(70, 74, 82), outline=INK, w=4)
    c.pen.text(540, 800, 'your loop', 'monob', 30, YEL)
    tb = c.T('busy')
    for i, (lab, kw) in enumerate([('click', 'clicks'), ('scroll', 'scrolling'), ('paint', 'painting')]):
        at = c.T(kw)
        if not c.on(at): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.35)
        x = 220 + i * 320
        c.pen.rr(x - 110 * s, 980 - 50 * s, x + 110 * s, 980 + 50 * s, 10, fill=WHITE, outline=INK, w=4)
        c.pen.text(x, 980, lab, 'monob', 34 * s, INK)
        c.pen.text(x, 1060, 'waiting…', 'int', 26, RED)
    txt(c, 540, 400, 'one cook · one dish at a time', c.T('one', 2), 'intx', 44, INK)

def mainthread(c):
    title(c, 'THE MAIN THREAD', 330, c.T('main'), 110, hlcol=YEL)
    blocks = [(0.0, 0.2, 0, 'JS'), (0.2, 0.12, 0, 'Style'), (0.32, 0.12, 0, 'Layout'), (0.44, 0.12, 0, 'Paint'), (0.56, 0.18, 0, 'JS'), (0.74, 0.12, 0, 'Layout'), (0.86, 0.12, 0, 'Paint')]
    flame(c, 100, 560, 980, blocks, c.T('runs'), 90)
    tt = c.T('time')
    if c.on(tt): label(c, 540, 800, 'one thing at a time', tt, RED, WHITE, 36)

def helpers(c):
    icon(c.pen, 'chef', 300, 560, 1.8)
    c.pen.text(300, 690, 'main thread', 'int', 30, INK)
    for i, (lab, kw) in enumerate([('timers', 'Timers'), ('network', 'network'), ('events', 'events')]):
        at = c.T(kw); y = 440 + i * 150
        node(c, 790, y, 330, 120, lab, at, None, fill=(225, 240, 255), size=36)
    tw = c.T('Web')
    if c.on(tw): label(c, 790, 330, 'Web APIs (browser helpers)', tw, BLUE, WHITE, 28)
    tq = c.T('queue')
    if c.on(tq):
        c.pen.rr(110, 930, 970, 1060, 20, outline=INK, w=5)
        c.pen.text(130, 905, 'QUEUE', 'int', 28, INK, 'lm')
        for k in range(3):
            at = tq + k * 0.4
            if c.on(at):
                q = c.P(at, 0.6)
                x = 900 - 220 * k - (1 - q) * 0
                c.pen.rr(x - 90, 955, x + 90, 1035, 12, fill=YEL, outline=INK, w=3)
                c.pen.text(x, 995, ['done!', 'data!', 'click!'][k], 'monob', 26, INK)
    tf = c.T('free')
    if c.on(tf): arrow(c.pen, 200, 920, 260, 720, c.P(tf, 0.4), GRN, 6, 22)

def proof(c):
    for j, (lab, ok, kw, sub) in enumerate([('await fetch(url)', True, 'fetch', 'waiting happens outside'), ('for (…1e9) {}', False, 'loop', 'computing blocks the chef')]):
        at = c.T(kw); x0 = 90 + j * 470
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        card(c.pen, x0, 420, x0 + 430, 1000, 22, (225, 245, 230) if ok else (255, 225, 225), 10, 5)
        c.pen.text(x0 + 215, 500, lab, 'monob', 30, INK)
        if ok: check(c.pen, x0 + 215, 680, 2.5, GRN, 16, c.P(at + 0.3, 0.4))
        else: cross(c.pen, x0 + 215, 680, 2.5, RED, 16, c.P(at + 0.3, 0.4))
        c.pen.text(x0 + 215, 880, 'page responsive' if ok else 'page frozen', 'intx', 38, GRN if ok else RED)
        c.pen.text(x0 + 215, 940, sub, 'int', 26, INK)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    code(c, 80, 440, 1000, 680, ['setTimeout(fn, 0);', 'heavyWork(); // 200ms'], c.T('setTimeout'), 0.3, 32, 'app.js')
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 760, 1080, 'NOT IMMEDIATE', 48, c.P(tn, 0.35), 6, BLUE)
    tw = c.T('waits')
    if c.on(tw):
        c.pen.rect(110, 800, 110 + 640 * c.P(tw, 0.6), 870, fill=RED, outline=INK, w=3)
        c.pen.text(430, 835, 'heavyWork()', 'monob', 30, WHITE)
        if c.on(tw + 0.7): c.pen.rect(760, 800, 760 + 180 * c.P(tw + 0.7, 0.3), 870, fill=YEL, outline=INK, w=3); c.pen.text(850, 835, 'fn', 'monob', 30, INK)
        txt(c, 540, 950, '0 ms = "as soon as possible", not "now"', tw + 0.5, 'int', 34, INK)

SCENES = [
    (hook, "Run a three second loop in the console, on any website. Now try to scroll. Nothing moves. The whole page is frozen. Why?"),
    (chef, "Because JavaScript has one chef. One kitchen, one cook, one dish at a time. While the chef is busy with your loop, nothing else gets served. Not clicks, not scrolling, not even painting the screen."),
    (mainthread, "That chef is the main thread. It runs your JavaScript, handles events, and does style, layout and paint. All of it, one thing at a time."),
    (helpers, "So how does anything wait without blocking? The chef has helpers. Timers, network requests and events are handled by the browser's Web APIs, outside the chef. When they finish, they leave a note in a queue, and the chef picks it up when it's free."),
    (proof, "That's why a fetch doesn't freeze the page, but a long loop does. Waiting happens outside the chef. Computing happens on it."),
    (gotcha, "Interview trap: does setTimeout with zero delay run immediately? No. It means: queue this as soon as possible. It still waits until the chef finishes what it's doing."),
    (scene_next('S1 · E15', 'CALL STACK', "the chef's to-do list", 'stack', 'list'),
     "Next: the call stack and the task queue, the chef's to-do list. Comment NOTES for the cheat sheet."),
]
