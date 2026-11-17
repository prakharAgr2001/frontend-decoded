from engine.lib import *

EP = dict(id='S1E23', tag='S1 · E23', short='OBSERVERS')

def feed(c, t0, play_rule=True):
    card(c.pen, 260, 330, 820, 1180, 40, WHITE, 12, 6)
    off = ((c.t - t0) * 120) % 420 if c.t > t0 else 0
    c.pen.rect(262, 334, 818, 1176, fill=WHITE)
    for k in range(4):
        y = 360 + k * 420 - off
        if y > 1150 or y + 380 < 340: continue
        ya, yb = max(345, y), min(1170, y + 380)
        vis = (yb - ya) / 380
        playing = vis > 0.5 and play_rule
        c.pen.rect(290, ya, 790, yb, fill=(60, 64, 72) if not playing else (40, 90, 160))
        if playing and yb - ya > 120:
            c.pen.poly([(510, (ya + yb) / 2 - 40), (510, (ya + yb) / 2 + 40), (580, (ya + yb) / 2)], fill=WHITE)
    c.pen.line([(262, 755), (818, 755)], YEL, 3, False)

def hook(c):
    feed(c, 0.0)
    ts = c.T('scroll', 2)
    if c.on(ts): stamp(c.cv, 540, 1290, 'NOT A SCROLL LISTENER', 52, c.P(ts, 0.35), -3, RED)

def oldway(c):
    code(c, 40, 330, 1040, 640, ["window.addEventListener('scroll', () => {", "  for (const v of videos) {", "    const r = v.getBoundingClientRect();", "    ..."],
         0.1, 0.12, 26, 'feed.js', marks=[(2, c.T('getBoundingClientRect'), (150, 50, 60))])
    td = c.T('dozens')
    if c.on(td):
        for k in range(30):
            if c.on(td + k * 0.04): c.pen.rect(110 + k * 29, 760, 132 + k * 29, 840, fill=YEL if k % 2 else PURPLE, outline=INK, w=2)
        txt(c, 540, 900, 'scroll → JS → forced layout → repeat', td, 'int', 34, RED)

def io(c):
    code(c, 40, 330, 1040, 760, ["new IntersectionObserver((entries) => {", "  for (const e of entries)", "    e.isIntersecting ? e.target.play()", "                     : e.target.pause();",
                                 "}, { threshold: 0.5 }).observe(video);"], c.T('IntersectionObserver'), 0.15, 26, 'feed.js', marks=[(4, c.T('visible'), YEL)])
    tc = c.T('changes')
    if c.on(tc): label(c, 540, 870, 'called only when visibility crosses 50%', tc, GRN, WHITE, 30)

def uses(c):
    title(c, 'ONE API, MANY USES', 330, 0.1, 90)
    items = [('lazy images', 'lazy', 'eye'), ('infinite scroll', 'infinite', 'doc'), ('autoplay', 'autoplay', 'bolt'), ('seen analytics', 'analytics', 'clock')]
    for i, (nm, kw, ic) in enumerate(items):
        node(c, 300 + (i % 2) * 480, 560 + (i // 2) * 300, 400, 240, nm, c.T(kw), ic)

def siblings(c):
    rows = [('ResizeObserver', 'element changed size', 'ResizeObserver'), ('MutationObserver', 'the DOM itself changed', 'MutationObserver'),
            ('PerformanceObserver', 'long tasks, vitals, metrics', 'PerformanceObserver')]
    for i, (nm, sub, kw) in enumerate(rows):
        at = c.T(kw); y = 450 + i * 250
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.4)
        card(c.pen, 90, y - 95 * s, 990, y + 95 * s, 24, WHITE, 10, 5)
        c.pen.text(140, y - 25, nm, 'monob', 44 * s, BLUE, 'lm')
        c.pen.text(140, y + 35, sub, 'ints', 32 * s, MUTE, 'lm')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Why is it better than a scroll listener?', c.T('better'), 'intx', 42, INK)
    for i, (s_, kw) in enumerate([('browser computes visibility itself', 'computes'), ('your code never forces layout', 'never'), ('fires only when crossing the threshold', 'threshold')]):
        at = c.T(kw); y = 620 + i * 170
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.35)
        card(c.pen, 110, y - 65 * s, 970, y + 65 * s, 20, WHITE, 8, 4)
        check(c.pen, 190, y, 1.1 * s, GRN, 10)
        c.pen.text(250, y, s_, 'intx', 36 * s, INK, 'lm')

SCENES = [
    (hook, "Scroll through a feed, and each video starts playing the moment it's mostly on screen. How does the page know? Not by listening to scroll."),
    (oldway, "The old way: a scroll listener that calls getBoundingClientRect on every element, dozens of times a second. That's main thread work and forced layout on every scroll."),
    (io, "IntersectionObserver flips it around. You tell the browser what to watch, and how much of it should be visible. It calls you back only when that changes."),
    (uses, "That one API powers lazy loaded images, infinite scroll, autoplay, and analytics that track what users actually saw."),
    (siblings, "It has siblings. ResizeObserver tells you when an element changes size. MutationObserver tells you when the DOM itself changes. And PerformanceObserver streams metrics, like long tasks."),
    (gotcha, "Interview question: why is it better than a scroll listener? The browser computes visibility itself, during rendering. Your code never forces layout. And it only fires when visibility crosses your threshold."),
    (scene_next('S1 · E24', 'INTERVIEW Qs', 'events, memory and observers', 'interview', 'observers'),
     "Next: interview questions on events, memory and observers. Comment NOTES for the cheat sheet."),
]
