from engine.s2_extra import *

EP = dict(id='S2E11', tag='S2 · E11', short='SELECTIVE HYDRATION')

PARTS = [('Header', 330, 110), ('Gallery', 470, 250), ('Add to cart', 750, 100), ('Reviews', 880, 200), ('Recommendations', 1110, 180)]

def blocks(c, x0, x1, state):
    """state(name) -> fill"""
    for name, y, h in PARTS:
        col = state(name)
        c.pen.rr(x0, y, x1, y + h, 14, fill=col, outline=INK, w=4)
        c.pen.text((x0 + x1) / 2, y + h / 2, name, 'intx', 34, INK if col != DARK else WHITE)

def hook(c):
    for i, (name, y, h) in enumerate(PARTS):
        at = 0.2 + i * 0.25
        if c.on(at):
            c.sfx(at, 'pop')
            c.pen.rr(200, y, 880, y + h * c.P(at, 0.3), 14, fill=YEL if name == 'Add to cart' else WHITE, outline=INK, w=4)
            if c.P(at, 0.3) > 0.9: c.pen.text(540, y + h / 2, name, 'intx', 34, INK)
    tt = c.T('tap')
    if c.on(tt): c.pen.circ(700, 800, 24, fill=YEL, outline=INK, w=4)
    tw = c.T('wait')
    if c.on(tw): stamp(c.cv, 540, 1340, 'WAIT FOR THE CAROUSEL?', 56, c.P(tw, 0.4), -3, RED)

def allornothing(c):
    title(c, 'ALL OR NOTHING', 340, c.T('nothing'), 100, hlcol=YEL)
    th = c.T('hydrates')
    prog = c.P(th, 4.0, lambda x: x) if c.on(th) else 0
    x0, x1 = 160, 920
    c.pen.rr(x0, 460, x1, 520, 30, fill=WHITE, outline=INK, w=4)
    if prog > 0.02: c.pen.rr(x0 + 6, 466, x0 + 6 + (x1 - x0 - 12) * prog, 514, 24, fill=RED)
    c.pen.text(540, 570, 'hydrating the whole tree…' if prog < 1 else 'done', 'int', 30, INK)
    tn = c.T('responds')
    if c.on(tn):
        for k, nm in enumerate(['Header', 'Gallery', 'Add to cart', 'Reviews']):
            y = 680 + k * 120
            c.pen.rr(260, y, 820, y + 90, 12, fill=LIGHT, outline=GREY, w=3)
            c.pen.text(540, y + 45, nm + ' · frozen', 'ints', 32, MUTE)

def analogy(c):
    tw = c.T('waiter')
    if c.on(tw):
        c.pen.text(540, 350, 'THE SMART WAITER', 'osw', 72, INK)
        for k in range(4):
            x = 180 + k * 240
            c.pen.circ(x, 700, 80, fill=WHITE, outline=INK, w=5); c.pen.text(x, 700, f'T{k + 1}', 'osw', 50, INK)
    th = c.T('hand')
    if c.on(th):
        c.pen.line([(660, 640), (680, 520)], INK, 8); c.pen.circ(682, 512, 18, fill=YEL, outline=INK, w=4)
        tx = 180 + (660 - 180) * c.P(th + 0.3, 0.8)
        person(c.pen, tx, 960, 1.0, BLUE)
        label(c, 540, 1080, 'goes to the raised hand first', th, YEL, INK, 32)
    tr = c.T('rest')
    if c.on(tr): txt(c, 540, 1180, 'then serves the rest, one by one', tr, 'ints', 34, MUTE)

CODE = ['<Header />', '<Suspense fallback={<Spinner />}>', '  <Gallery />', '</Suspense>', '<Suspense fallback={<Spinner />}>',
        '  <Reviews />', '</Suspense>']

def how(c):
    code(c, 60, 340, 1020, 340 + 72 + 7 * 52 + 40, CODE, c.T('Suspense'), 0.12, 30, 'Product.jsx',
         marks=[(1, c.T('boundary'), YEL), (4, c.T('boundary'), YEL)])
    ti = c.T('independently')
    if c.on(ti): label(c, 540, 900, 'each boundary hydrates on its own', ti, YEL, INK, 32)
    tb = c.T('breaks')
    if c.on(tb): label(c, 540, 990, 'main thread gets breaks between chunks', tb, GRN, WHITE, 32)

def click(c):
    tc = c.T('clicks')
    order = {'Header': 0, 'Reviews': 1, 'Gallery': 2, 'Add to cart': 3, 'Recommendations': 4}
    t0 = c.T('first')
    def st(name):
        if not c.on(t0): return LIGHT
        done = int((c.t - t0) / 0.9) + 1
        return GRN if order[name] < done else LIGHT
    blocks(c, 200, 880, lambda n: (YEL if n == 'Reviews' and c.on(tc) and not c.on(t0) else st(n)))
    if c.on(tc): c.pen.circ(760, 980, 24, fill=YEL, outline=INK, w=4)
    if c.on(t0): label(c, 540, 1060, 'clicked part jumps the queue', t0, INK, WHITE, 30)
    tr = c.T('replays')
    if c.on(tr): stamp(c.cv, 540, 1360, 'CLICK REPLAYED', 64, c.P(tr, 0.4), -3, BLUE)

def flames(c):
    tl = c.T('long')
    c.pen.text(80, 420, 'classic hydration', 'intx', 36, INK, 'lm')
    flame(c, 80, 460, 1000, [(0, 0.85, 0, 'JS', True)], tl, 80)
    if c.on(tl): label(c, 540, 610, 'one long task', tl, RED, WHITE, 28)
    ts = c.T('selective')
    if c.on(ts):
        c.pen.text(80, 760, 'selective hydration', 'intx', 36, INK, 'lm')
        flame(c, 80, 800, 1000, [(0, 0.15, 0, 'JS'), (0.2, 0.15, 0, 'JS'), (0.4, 0.15, 0, 'JS'), (0.6, 0.15, 0, 'JS'), (0.8, 0.15, 0, 'JS')], ts, 80)
        label(c, 540, 950, 'short chunks · input can squeeze in', ts + 0.8, GRN, WHITE, 28)
    tc = c.T('season')
    if c.on(tc): chapter(c, 540, 1100, 'S1 · E18', 'long tasks', tc)

def gotcha(c):
    trap(c)
    qtext(c, 'Does selective hydration make your JavaScript smaller?', 450, c.T('smaller'), 46)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 650, 'NO', 110, c.P(tn, 0.35), -6, RED)
    items = [(False, 'same code downloads', c.T('downloads')), (False, 'same code runs', c.T('runs')),
             (True, 'better ORDER + smaller pieces', c.T('order'))]
    proscons(c, 150, 800, 980, items, 38, 100)
    tl = c.T('less')
    if c.on(tl): label(c, 540, 1150, 'to ship less: server components, islands', tl, YEL, INK, 30)

SCENES = [
    (hook, "A product page has a header, a gallery, the add to cart button, reviews, and a recommendations carousel. You tap add to cart. Should your tap wait for the carousel to hydrate?"),
    (allornothing, "With classic hydration, yes. It's all or nothing. React hydrates the whole tree in one go, and nothing responds until it's done."),
    (analogy, "Picture a smart waiter. Instead of serving tables strictly in order, he goes to the table where someone raised a hand. Then he serves the rest."),
    (how, "React eighteen does this with Suspense. Every Suspense boundary hydrates independently, so the main thread gets breaks between chunks."),
    (click, "And if the user clicks inside a part that hasn't hydrated yet, React hydrates that part first, then replays the click on it."),
    (flames, "In the Performance panel, one long hydration task turns into several short ones. That's the long tasks lesson from season one, applied to hydration. With selective hydration, input can squeeze in between."),
    (gotcha, "Interview trap: does selective hydration make your JavaScript smaller? No. The same code still downloads, and still runs. It changes the order, and breaks the work into pieces. To ship less code, you need other tools."),
    (scene_next('S2 · E12', 'INTERVIEW QUESTIONS', 'all about hydration', 'interview', 'hydration'),
     "Next: interview questions, all about hydration. Comment NOTES for the cheat sheet."),
]
