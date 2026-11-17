from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E24', tag='S3 · E24', short='THROTTLE')

def ticks(c, y, at, n, xs, col, label_):
    c.pen.text(110, y - 50, label_, 'intx', 32, INK, 'lm')
    c.pen.line([(110, y + 40), (970, y + 40)], GREY, 3)
    for k, x in enumerate(xs):
        t = at + k * 0.04
        if c.on(t): c.pen.line([(x, y), (x, y + 40)], col, 5)

def hook(c):
    phone(c, 300, 820, 380, 760)
    ts = c.T('Scroll')
    off = ((c.t - ts) * 300) % 120 if c.on(ts) else 0
    for k in range(6):
        y = 520 + k * 110 - off
        if 480 < y < 1120: c.pen.rect(150, y, 450, y + 80, fill=LIGHT)
    tb = c.T('button')
    if c.on(tb): c.pen.circ(410, 1110, 34, fill=YEL, outline=INK, w=4); c.pen.text(410, 1110, '↑', 'intx', 36, INK)
    if c.on(ts):
        n = int((c.t - ts) * 60)
        console(c, 540, 470, 1030, 900, [(ts + 0.2, 'scroll', None)])
        c.pen.text(780, 760, str(min(n, 120)), 'osw', 120, RED)
        c.pen.text(780, 850, 'handler calls', 'ints', 28, WHITE)
    td = c.T('dozens')
    if c.on(td): stamp(c.cv, 760, 1060, 'DOZENS / SECOND', 50, c.P(td, 0.35), -4, RED); c.sfx(td, 'thud')

def define(c):
    title(c, 'THROTTLE', 330, c.T('Throttle'), 120, hlcol=YEL)
    tf = c.T('hundred')
    ticks(c, 560, tf, 40, [120 + k * 21 for k in range(40)], GREY, 'events: 100 in 1 s')
    tr = c.T('five')
    if c.on(tr):
        c.pen.text(110, 710, 'throttled · 200 ms', 'intx', 32, GRN, 'lm')
        c.pen.line([(110, 800), (970, 800)], GREY, 3)
        for k in range(5):
            t = tr + k * 0.2; x = 120 + k * 170
            if c.on(t): c.sfx(t, 'tick'); c.pen.circ(x, 790, 20 * c.B(t, 0.3), fill=GRN, outline=INK, w=3)
    ts = c.T('steadily')
    if c.on(ts): label(c, 540, 960, 'runs 5 times · steadily · while events keep coming', ts, WHITE, INK, 30)

def vs(c):
    title(c, 'DEBOUNCE vs THROTTLE', 330, 0.1, 84)
    xs = [130 + k * 18 for k in range(30)] + [800, 818]
    ticks(c, 520, 0.2, len(xs), xs, GREY, 'events')
    td = c.T('silence')
    if c.on(td):
        c.pen.text(110, 680, 'debounce', 'intx', 32, BLUE, 'lm'); c.pen.line([(110, 760), (970, 760)], GREY, 3)
        c.pen.circ(720, 750, 20 * c.B(td, 0.3), fill=BLUE, outline=INK, w=3); c.pen.circ(940, 750, 20 * c.B(td + 0.3, 0.3), fill=BLUE, outline=INK, w=3)
    tr = c.T('regularly')
    if c.on(tr):
        c.pen.text(110, 860, 'throttle', 'intx', 32, GRN, 'lm'); c.pen.line([(110, 940), (970, 940)], GREY, 3)
        for k, x in enumerate((130, 310, 490, 800)): c.pen.circ(x, 930, 20 * c.B(tr + k * 0.1, 0.3), fill=GRN, outline=INK, w=3)
    tsr = c.T('search')
    if c.on(tsr): pill(c.pen, 300, 1080, 'debounce → search', c.B(tsr, 0.35), (200, 220, 255), INK, 30)
    tp = c.T('progress')
    if c.on(tp): pill(c.pen, 760, 1080, 'throttle → progress bar', c.B(tp, 0.35), (200, 240, 200), INK, 30)

def metro(c):
    title(c, 'THE METRO', 330, 0.1, 110)
    c.pen.rect(90, 780, 990, 800, fill=INK)
    tl = c.T('leaves')
    q = ((c.t - tl) / 2.5) % 1 if c.on(tl) else 0
    x = 90 + 1100 * q - 300
    c.pen.rr(x, 600, x + 380, 770, 30, fill=BLUE, outline=INK, w=5)
    for k in range(4): c.pen.rect(x + 30 + k * 85, 630, x + 95 + k * 85, 700, fill=CYAN, outline=INK, w=3)
    tp = c.T('passenger')
    if c.on(tp):
        for k in range(6): person(c.pen, 160 + k * 70 + 20 * math.sin(c.t * 3 + k), 1000, 0.8, ORANGE)
    tf = c.T('five')
    if c.on(tf): label(c, 540, 1120, 'every 5 min · no matter the crowd', tf, YEL, INK, 34)

def code_(c):
    code(c, 40, 330, 1040, 860, ['function throttle(fn, wait) {', '  let last = 0;', '  return (...args) => {', '    const now = Date.now();',
                                 '    if (now - last >= wait) { last = now; fn(...args); }', '  };', '}'], c.T('remembers') - 0.6, 0.1, 25, 'throttle.js',
         marks=[(1, c.T('remembers'), YEL), (4, c.T('enough'), YEL)])
    code(c, 40, 930, 1040, 1090, ["window.addEventListener('scroll', throttle(updateProgress, 200));"], c.T('wire'), 0.1, 22, 'progress.js')

def better(c):
    title(c, 'EVEN BETTER', 330, c.T('better'), 110, hlcol=YEL)
    node(c, 540, 560, 760, 170, 'requestAnimationFrame', c.T('requestAnimationFrame'), 'clock', sub='at most once per frame, right before paint')
    node(c, 540, 830, 760, 170, 'IntersectionObserver', c.T('IntersectionObserver'), 'eye', sub='"is it visible?" without scroll events')
    ts = c.T('season')
    if c.on(ts): txt(c, 540, 1010, 'callbacks: S1 · E17 + S1 · E23', ts, 'ints', 30, MUTE)

def proof(c):
    ta = c.T('count')
    console(c, 60, 360, 1020, 760, [(ta + 0.5, 'scroll: 1', None), (ta + 0.6, 'scroll: 2', None), (ta + 0.7, 'scroll: 3', None), (ta + 0.8, '... scroll: 87', RED)])
    tt = c.T('throttle')
    if c.on(tt):
        console(c, 60, 820, 1020, 1160, [(tt + 0.6, 'scroll: 1', GRN), (tt + 0.9, 'scroll: 2', GRN), (tt + 1.2, '... scroll: 9', GRN)])
    td = c.T('drop')
    if c.on(td): stamp(c.cv, 760, 1240, '87 DOWN TO 9', 70, c.P(td, 0.35), -4, GRN); c.sfx(td, 'thud')

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"My throttle loses the final scroll position."', c.T('final'), 'intx', 40, INK)
    ti = c.T('ignores')
    if c.on(ti):
        xs = [140 + k * 40 for k in range(20)]
        for k, x in enumerate(xs): c.pen.line([(x, 600), (x, 650)], GREY if k != 19 else RED, 5 if k != 19 else 8)
        for k in (0, 5, 10, 15): c.pen.circ(xs[k], 700, 16, fill=GRN, outline=INK, w=3)
        txt(c, xs[19], 760, 'last event: lost', c.T('lost'), 'ints', 30, RED)
    tt = c.T('trailing')
    if c.on(tt):
        c.pen.circ(140 + 19 * 40 + 60, 700, 22 * c.B(tt, 0.3), fill=YEL, outline=INK, w=4)
        label(c, 540, 900, 'add a trailing call → final state applied', tt, YEL, INK, 32)

SCENES = [
    (hook, "You add a scroll listener to show a back to top button. Scroll for one second, and your handler fires dozens of times a second."),
    (define, "Throttle runs a function at most once per interval. Fire it a hundred times in one second with a two hundred millisecond throttle, and it runs just five times, steadily, while the events keep coming."),
    (vs, "Debounce waits for silence, then runs once. Throttle runs regularly through the storm. Debounce for search. Throttle for things that should keep updating, like a scroll progress bar."),
    (metro, "Think of a metro train that leaves every five minutes. It doesn't wait for the platform to empty, and it doesn't leave every time a passenger arrives."),
    (code_, "In code, throttle remembers when it last ran, and only calls the function again once enough time has passed. Then wire it to scroll."),
    (proof, "Prove it. Add a console count inside your scroll handler, and scroll. Then wrap it in throttle, and scroll again. Watch the number drop."),
    (better, "For visual updates, there's something even better: requestAnimationFrame runs at most once per frame, right before paint. And to check if something is visible, skip scroll events and use IntersectionObserver. Both are from season one."),
    (gotcha, "Interview trap: my throttle loses the final scroll position. A simple throttle ignores calls inside the window, so the last event can be lost. Add a trailing call, so the final state is always applied."),
    (scene_next('S3 · E25', 'VIRTUALIZATION', 'render 10,000 rows without dying', 'virtualization', 'rows'),
     "Next: virtualization, and how to show ten thousand rows without freezing the page. Comment NOTES for the cheat sheet."),
]
