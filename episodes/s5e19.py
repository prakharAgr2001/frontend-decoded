from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E19', tag='S5 · E19', short='SUSPENSE BOUNDARIES', hook='where loading states go')

PARTS = [('header', 'header', 0, 70), ('gallery', 'gallery', 90, 300), ('price', 'price', 410, 70), ('reviews', 'reviews', 500, 130),
         ('recommendations', 'recs', 650, 110)]


def page(c, inner, ready=(), popping=None, groups=None, at=0):
    x0, y0, x1, y1 = inner
    for kw, nm, dy, h in PARTS:
        y = y0 + 20 + dy
        if nm in ready:
            c.pen.rr(x0 + 20, y, x1 - 20, y + h, 12, fill={'header': INK, 'gallery': (120, 170, 220), 'price': (200, 240, 200),
                                                            'reviews': (255, 236, 200), 'recs': (230, 210, 250)}[nm], outline=INK, w=3)
            c.pen.text(x0 + 40, y + min(h, 70) / 2, nm, 'intx', 26, WHITE if nm == 'header' else INK, 'lm')
        else:
            skel(c, x0 + 20, y, x1 - 20, y + h, 12)


def hook(c):
    inner = phone(c, 540, 830, 480, 920, dy=(1 - c.P(0, 0.45)) * 900)
    ready = [nm for kw, nm, _, _ in PARTS if c.on(c.T(kw))]
    page(c, inner, ready=[] if c.on(c.T('spinner')) else [])
    for kw, nm, dy, h in PARTS:
        if c.on(c.T(kw)) and not c.on(c.T('spinner')):
            c.pen.text(inner[2] - 40, inner[1] + 20 + dy + 30, 'waiting…', 'int', 22, MUTE, 'rm')
    ts = c.T('spinner')
    if c.on(ts) and not c.on(c.T('popping')):
        c.pen.rect(inner[0], inner[1], inner[2], inner[3], fill=WHITE); spinner(c, 540, 830, 50)
    tp = c.T('popping')
    if c.on(tp):
        order = ['recs', 'header', 'reviews', 'gallery', 'price']
        n = min(5, int((c.t - tp) / 0.3) + 1)
        page(c, inner, ready=order[:n])
        for k in range(n): c.sfx(tp + k * 0.3, 'pop')


SC = ['<Suspense fallback={<GallerySkeleton />}>', '  <Gallery />', '</Suspense>']


def define(c):
    title(c, 'SUSPENSE', 340, c.T('Suspense'), 110, hlcol=YEL)
    code(c, 40, 440, 1040, 440 + 72 + 3 * 52 + 20, SC, c.T('ready') - 0.3, 0.1, 28, 'Product.jsx', marks=[(0, c.T('nearest'), YEL)])
    tr = c.T('ready')
    if c.on(tr): bubble(c, 120, 800, 'Gallery: “I’m not ready”', tr, WHITE, 32)
    ti = c.T('inside')
    if c.on(ti): label(c, 540, 950, 'fallback until everything inside is ready', ti, YEL, INK, 30)


def callback(c):
    ts = c.T('season')
    if c.on(ts):
        chapter(c, 540, 350, 'S2 · E13', 'Streaming SSR', ts)
    tsh = c.T('shell')
    br = node(c, 200, 700, 240, 200, 'server', tsh, 'server')
    bw = node(c, 880, 700, 240, 200, 'browser', tsh, 'laptop')
    if c.on(tsh):
        packet(c, br, bw, tsh, tsh + 0.9, CYAN, 'shell')
    tb = c.T('boundary')
    if c.on(tb):
        packet(c, br, bw, tb, tb + 0.9, YEL, 'boundary 1')
        packet(c, br, bw, tb + 0.8, tb + 1.7, YEL, 'boundary 2')
    tc = c.T('click')
    if c.on(tc):
        chapter(c, 540, 960, 'S2 · E11', 'Selective hydration', tc)
        txt(c, 540, 1060, 'the boundary you click hydrates first', tc + 0.3, 'intx', 32, INK)


def courses(c):
    title(c, 'SERVE IN COURSES', 340, c.T('courses'), 96)
    for k, (kw, nm, n) in enumerate((('Starters', 'starters', 3), ('mains', 'mains', 3))):
        t = c.T(kw); y = 560 + k * 230
        if not c.on(t): continue
        c.pen.text(120, y - 80, nm, 'intx', 34, INK, 'lm')
        for j in range(n):
            x = 220 + j * 250
            s = c.B(t, 0.35)
            c.pen.circ(x, y + 20, 80 * s, fill=WHITE, outline=INK, w=4)
            c.pen.circ(x, y + 20, 50 * s, fill=[ORANGE, GRN, YEL][j])
        c.sfx(t, 'pop')
    tp = c.T('plate')
    if c.on(tp): rows(c, 140, 1060, [(tp, 'not one plate at a time', None, 'no'), (c.T('end'), 'not all at the very end', None, 'no')], gap=120, w=800, h=96, size=34)


def balance(c):
    te = c.T('everything')
    if c.on(te):
        card(c.pen, 90, 360, 500, 900, 20, WHITE, 8, 4)
        c.pen.rr(110, 380, 480, 880, 16, outline=RED, w=5)
        spinner(c, 295, 630, 40)
        c.pen.text(295, 960, 'one boundary', 'intx', 32, INK)
        txt(c, 295, 1010, 'waits for the slowest', c.T('slowest'), 'int', 28, RED)
    tv = c.T('component')
    if c.on(tv):
        card(c.pen, 580, 360, 990, 900, 20, WHITE, 8, 4)
        for k in range(6):
            y = 380 + k * 82
            if int((c.t - tv) * 3 + k * 1.7) % 3 == 0: skel(c, 600, y, 970, y + 70, 10)
            else: c.pen.rr(600, y, 970, y + 70, 10, fill=[BLUE, ORANGE, GRN, PURPLE, TEAL, PINK][k], outline=RED, w=3)
        c.pen.text(785, 960, 'a boundary each', 'intx', 32, INK)
        txt(c, 785, 1010, 'popcorn + jumps', c.T('popcorn'), 'int', 28, RED)
    tg = c.T('Group')
    if c.on(tg): label(c, 540, 1160, 'group what belongs together', tg, YEL, INK, 34)


def layout(c):
    title(c, 'A GOOD DEFAULT', 340, c.T('default'), 96, hlcol=YEL)
    inner = phone(c, 540, 860, 460, 860)
    x0, y0, x1, y1 = inner
    page(c, inner, ready=('header', 'gallery', 'price', 'reviews', 'recs'))
    groups = [(c.T('price'), 0, 70, GRN, 'critical'), (c.T('gallery'), 90, 300, BLUE, 'own boundary'), (c.T('Reviews'), 410, 360, PURPLE, 'below the fold')]
    for t, dy, h, col, lab in groups:
        if not c.on(t): continue
        y = y0 + 20 + dy
        c.pen.rr(x0 + 8, y - 10, x1 - 8, y + h + 10, 16, outline=col, w=6)
        pill(c.pen, x1 + 40 if False else (x0 + x1) / 2, y + h / 2, lab, c.B(t, 0.35), col, WHITE, 24); c.sfx(t, 'pop')


def pair(c):
    tl = c.T('last')
    if c.on(tl): chapter(c, 540, 350, 'S5 · E18', 'Error boundaries', tl)
    code(c, 30, 440, 1050, 440 + 72 + 5 * 50 + 20, ['<ErrorBoundary fallback={<ReviewsError />}>', '  <Suspense fallback={<ReviewsSkeleton />}>',
                                                     '    <Reviews />', '  </Suspense>', '</ErrorBoundary>'], c.T('pair'), 0.1, 26, 'Product.jsx',
         marks=[(0, c.T('error'), YEL), (1, c.T('Suspense'), YEL)])
    tv = c.T('level')
    if c.on(tv): label(c, 540, 900, 'loading + failure at the same level', tv, YEL, INK, 32)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 40, 440, 1040, 440 + 72 + 4 * 50 + 20, ['function Reviews() {', '  const [d, setD] = useState(null);', '  useEffect(() => { load().then(setD); }, []);',
                                                     '  return d && <List items={d} />; }'], c.T('fallback') - 0.4, 0.1, 26, 'Reviews.jsx',
         marks=[(2, c.T('effect'), YEL)])
    tn = c.T('never')
    if c.on(tn): stamp(c.cv, 540, 800, 'FALLBACK NEVER SHOWS', 60, c.P(tn, 0.35), -3, RED); c.sfx(tn, 'thud')
    ts = c.T('suspends')
    if c.on(ts):
        chips(c, 100, 960, [('use(promise)', YEL), ('framework loader', YEL), ('useSuspenseQuery', YEL)], ts, 0.3, 28)


SCENES = [
    (hook, "A product page has a header, a gallery, the price, reviews, and recommendations. Each one is waiting on data. Do you show one big spinner? Or five little pieces popping in at random?"),
    (define, "Suspense lets a component say: I'm not ready yet. React shows the nearest boundary's fallback, until everything inside it is ready."),
    (callback, "We've seen this in season two. Streaming sends the shell first, then each boundary as it resolves. And selective hydration lets the boundary you click on hydrate first."),
    (courses, "Placing boundaries is like serving a dinner in courses. Starters arrive together, then the mains together. Not every plate one at a time, and not everything at the very end."),
    (balance, "One boundary around everything, and the page waits for the slowest part. A boundary around every component, and the page pops in like popcorn, while the layout jumps. Group what belongs together."),
    (layout, "A good default: the header and price come first, because they're critical. The gallery gets its own boundary. Reviews and recommendations share a lower one, below the fold."),
    (pair, "And pair each Suspense boundary with an error boundary from the last episode. Loading and failure, handled at the same level."),
    (gotcha, "Interview trap. You wrap a component in Suspense, but the fallback never shows. It just renders empty, then pops in. Why? Suspense only reacts to something that suspends. A promise passed to use, a framework loader, or a library in suspense mode. A fetch inside use effect never suspends."),
    (scene_next('S5 · E20', 'IQ: ASYNC EDGE CASES', '4 interview questions', 'four', 'async'),
     "Next: four interview questions on async edge cases. Comment NOTES for the cheat sheet."),
]
