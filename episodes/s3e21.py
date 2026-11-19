from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E21', tag='S3 · E21', short='THIRD-PARTY COST', hook='the scripts you invited in')

def hook(c):
    tl = c.T('lean')
    if c.on(tl): bars(c, 60, 420, [('your code', 120, GRN, tl)], 900, 560, 80, 0, '{} KB', 220, 32)
    items = [('chat widget', 'chat', ORANGE), ('analytics ×2', 'analytics', BLUE), ('A/B testing', 'testing', PURPLE), ('tag manager', 'tag', RED)]
    for k, (nm, kw, col) in enumerate(items):
        t = c.T(kw)
        if c.on(t): bars(c, 60, 540 + k * 110, [(nm, [180, 220, 140, 260][k], col, t)], 900, 560, 80, 0, '{} KB', 220, 32)
    ts = c.T('slower')
    if c.on(ts): stamp(c.cv, 540, 1100, '+1 s · NOT YOUR CODE', 62, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')

def why(c):
    title(c, 'IT RUNS ON YOUR THREAD', 330, c.T('main'), 80, hlcol=(255, 190, 190))
    rows(c, 90, 510, [('long', 'their long tasks block your clicks', 'INP', 'no'), ('banners', 'their late banners shift your layout', 'CLS', 'no'),
                      ('origin', 'every new origin = another connection', 'DNS + TCP + TLS', 'no')], 170, 900, 130, 38, 30)

def party(c):
    title(c, 'GUESTS BRING GUESTS', 330, c.T('party'), 90)
    tg = c.T('guests', 1)
    for k in range(3):
        if c.on(tg + k * 0.2): person(c.pen, 300 + k * 240, 760, 1.4, BLUE)
    tb = c.T('brings')
    if c.on(tb):
        for k in range(9):
            t = tb + k * 0.1
            if c.on(t): person(c.pen, 150 + k * 100, 1050, 0.9, [ORANGE, PURPLE, RED][k % 3])
    tc = c.T('control')
    if c.on(tc): label(c, 540, 1180, "you don't control who shows up", tc, YEL, INK, 34)

def measure(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Network', 'Request blocking'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tb = c.T('block')
    if c.on(tb):
        for k, (nm, on) in enumerate((('*.chat-widget.com', True), ('*.ab-tests.io', False), ('*.tagmanager.net', False))):
            y = 500 + k * 80
            c.pen.rr(100, y - 20, 140, y + 20, 6, fill=YEL if on else (60, 66, 76), outline=(150, 150, 160), w=2)
            if on: check(c.pen, 120, y, 0.6, INK, 5)
            c.pen.text(170, y, nm, 'mono', 28, WHITE, 'lm')
    tr = c.T('compare')
    if c.on(tr):
        timerbar(c, 120, 820, 960, 0.9, tr, 'LCP · with widget', RED, 44, '3.4 s')
        timerbar(c, 120, 940, 960, 0.6, tr + 0.4, 'LCP · blocked', GRN, 44, '2.3 s')
        c.pen.text(120, 792, 'LCP · with widget', 'int', 30, WHITE, 'lm'); c.pen.text(960, 792, '3.4 s', 'monob', 30, RED, 'rm')
        if c.on(tr + 0.4): c.pen.text(120, 912, 'LCP · widget blocked', 'int', 30, WHITE, 'lm'); c.pen.text(960, 912, '2.3 s', 'monob', 30, GRN, 'rm')
    td = c.T('difference')
    if c.on(td): label(c, 540, 1130, "the difference = that script's real cost", td, YEL, INK, 32)

def facade(c):
    title(c, 'USE A FACADE', 330, c.T('facade'), 110, hlcol=YEL)
    ts = c.T('screenshot')
    if c.on(ts):
        card(c.pen, 140, 460, 940, 900, 24, (40, 44, 52), 10, 5)
        c.pen.poly([(500, 620), (500, 740), (610, 680)], fill=WHITE)
        c.pen.text(540, 840, 'static image · ~5 KB', 'ints', 30, WHITE)
    tc = c.T('click')
    if c.on(tc):
        c.pen.circ(560, 680, 30 + 30 * lin(c.t, tc, tc + 0.4), outline=YEL, w=5)
        bars(c, 60, 960, [('real player', 600, RED, tc + 0.3)], 600, 460, 70, 0, '{} KB', 300, 30)
        txt(c, 540, 1110, 'loaded only on click', tc + 0.5, 'intx', 38, INK)

def fixes(c):
    title(c, 'TAME THE REST', 330, c.T('Delay'), 100)
    rows(c, 90, 510, [('Delay', 'delay non-critical tags', 'until after load or first interaction', 'ok'), ('Self', 'self-host what you can', 'no new origin', 'ok'),
                      ('Partytown', 'Partytown → web worker', 'off the main thread', 'ok')], 170, 900, 130, 38, 30)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Performance', 'Insights'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tt = c.T('Third', 1)
    if c.on(tt):
        c.pen.text(100, 470, '3rd parties', 'intx', 36, WHITE, 'lm')
        c.pen.text(560, 540, 'transfer', 'int', 24, (150, 156, 166), 'lm'); c.pen.text(800, 540, 'main thread', 'int', 24, (150, 156, 166), 'lm')
        netrows(c, 100, 620, 1000, [(tt + 0.2, 'Tag Manager', ['248 kB', '612 ms'], (90, 40, 40)), (tt + 0.4, 'Chat widget', ['310 kB', '488 ms'], (90, 40, 40)),
                                    (tt + 0.6, 'Analytics', ['92 kB', '141 ms']), (tt + 0.8, 'A/B testing', ['64 kB', '133 ms'])], 28, 80, [560, 800])
    tm = c.T('time')
    if c.on(tm): txt(c, 540, 1040, 'sorted by main-thread time', tm, 'intx', 34, YEL)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"We load it with async, so it\'s free."', c.T('free'), 'intx', 44, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 600, tn, 110, RED)
    tp = c.T('parser')
    if c.on(tp): rows(c, 140, 760, [(tp, 'async: no parser blocking', None, 'ok'), (c.T('runs'), 'still runs on your main thread', None, 'no'),
                                     (c.T('competes'), 'still competes with every tap', None, 'no')], 125, 800, 100, 36)

SCENES = [
    (hook, "Your own code is lean. Then marketing adds a chat widget, two analytics tools, an A B testing script, and a tag manager. The page gets a second slower, and none of it is your code."),
    (why, "Third party scripts run on your main thread, just like your own code. Their long tasks block your clicks. Their late banners shift your layout. And every new origin means another connection to set up."),
    (party, "It's like hosting a party, where every guest brings their own guests. You don't control who shows up, or how long they stay."),
    (measure, "So measure first. In DevTools, turn on request blocking, and block one domain at a time. Reload, and compare. The difference is that script's real cost."),
    (facade, "Then tame them. Use a facade: a lightweight static screenshot of the chat widget or video player. Load the real thing only when someone clicks."),
    (fixes, "Delay non critical tags until after load, or the first interaction. Self host what you can. And for heavy scripts, tools like Partytown move them into a web worker, off the main thread."),
    (proof, "The Performance panel's Third parties insight lists every provider, with its transfer size and main thread time. Start at the top."),
    (gotcha, "Interview trap: we load it with async, so it's free. No. Async only stops it blocking the parser. Once it arrives, it still runs on your main thread, and it still competes with every tap."),
    (scene_next('S3 · E22', 'IQ: ASSETS', 'images, fonts + third parties', 'questions', 'third'),
     "Next: four interview questions on images, fonts and third parties. Comment NOTES for the cheat sheet."),
]
