from engine.s2_extra import *

EP = dict(id='S2E19', tag='S2 · E19', short='CASE STUDY: A STORE', hook='design rendering for a store')

ROUTES = [('/blog', 'SSG', GRN), ('/', 'ISR', TEAL), ('/product/:id', 'ISR + client islands', TEAL), ('/search', 'streaming SSR', BLUE),
          ('/cart · /checkout', 'CSR (client)', ORANGE), ('/account', 'CSR (client)', ORANGE)]

def hook(c):
    title(c, 'DESIGN THE RENDERING', 340, c.T('Design'), 90, hlcol=YEL)
    for i, (r, s, col) in enumerate(ROUTES):
        at = c.T('pages') + i * 0.15
        if c.on(at):
            c.sfx(at, 'tick')
            c.pen.rr(150, 450 + i * 105, 930, 530 + i * 105, 14, fill=WHITE, outline=INK, w=4)
            c.pen.text(190, 490 + i * 105, r, 'monob', 34, INK, 'lm')
            c.pen.text(890, 490 + i * 105, '?', 'osw', 48, MUTE, 'rm')
    tw = c.T('wrong')
    if c.on(tw): stamp(c.cv, 540, 1180, 'ONE STRATEGY ≠ ONE APP', 60, c.P(tw, 0.4), -3, RED)

def questions(c):
    title(c, '3 QUESTIONS', 340, c.T('three'), 110, hlcol=YEL)
    qs = [('Does it need SEO?', 'SEO'), ('Is it the same for everyone?', 'same'), ('How often does the data change?', 'often')]
    for i, (q, kw) in enumerate(qs):
        at = c.T(kw); y = 520 + i * 180
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        card(c.pen, 100, y - 70, 980, y + 70, 20, WHITE, 8, 4)
        c.pen.circ(170, y, 36 * c.B(at, 0.3), fill=INK); c.pen.text(170, y, str(i + 1), 'int', 34, WHITE)
        txt(c, 230, y, q, at, 'intx', 40, INK, 'lm', 'slide')

def row(c, i, at, y=None):
    r, s, col = ROUTES[i]
    if not c.on(at - 0.01): return
    y = y or 450
    c.sfx(at, 'pop')
    c.pen.text(540, y, r, 'monob', 56, INK)
    pill(c.pen, 540, y + 100, s, c.B(at, 0.35), col, WHITE, 40)

def why(c, items, y0=720):
    for k, (s_, at) in enumerate(items):
        txt(c, 540, y0 + k * 80, s_, at, 'ints', 36, INK)

def blog(c):
    row(c, 0, c.T('blog'), 420)
    why(c, [('needs SEO · same for everyone · rarely changes', c.T('SEO')), ('→ build once, serve from the CDN', c.T('once'))], 640)
    row(c, 1, c.T('home'), 900)
    why(c, [('changes daily → revalidate every few minutes', c.T('revalidate'))], 1110)

def product(c):
    row(c, 2, c.T('product'), 420)
    fill_page(c, (260, 650, 820, 1150), 'full'); c.pen.rr(260, 650, 820, 1150, 8, outline=INK, w=4)
    ts = c.T('stock')
    if c.on(ts):
        for (a, b, cc, d, lab) in [(300, 1000, 540, 1130, 'price / stock'), (560, 1000, 800, 1130, 'Add to cart')]:
            c.pen.rr(a, b, cc, d, 10, fill=None, outline=GRN, w=8)
        label(c, 540, 1210, 'live bits = small client islands', ts, GRN, WHITE, 30)
    tsf = c.T('static')
    if c.on(tsf): label(c, 540, 600, 'title, images, description: static', tsf, YEL, INK, 28)

def search(c):
    row(c, 3, c.T('search'), 420)
    why(c, [('different for every query → can’t prebuild', c.T('every')), ('SEO matters → render on the server', c.T('server')),
            ('stream: header first, results when ready', c.T('stream'))], 680)

def cart(c):
    row(c, 4, c.T('cart'), 420)
    row(c, 5, c.T('account'), 700)
    why(c, [('behind login · no SEO · per user', c.T('login')), ('→ client rendering is fine', c.T('fine'))], 960)

def map_(c):
    title(c, 'THE WHOLE STORE', 340, c.T('Put'), 100, hlcol=YEL)
    for i, (r, s, col) in enumerate(ROUTES):
        at = c.T('Put') + 0.4 + i * 0.2
        if not c.on(at): continue
        y = 470 + i * 110; c.sfx(at, 'pop')
        c.pen.rr(80, y - 42, 1000, y + 42, 14, fill=WHITE, outline=INK, w=4)
        c.pen.text(110, y, r, 'monob', 32, INK, 'lm')
        pill(c.pen, 760, y, s, c.B(at, 0.3), col, WHITE, 28)
    tf = c.T('frameworks')
    if c.on(tf): label(c, 540, 1180, 'Next.js · Nuxt · Remix · Astro: per route', tf, INK, WHITE, 30)

def gotcha(c):
    trap(c)
    qtext(c, 'The #1 mistake in this interview?', 460, c.T('mistake'), 54)
    tp = c.T('pick')
    if c.on(tp): label(c, 540, 640, '“we’ll just use SSR for everything”', tp, RED, WHITE, 34)
    tr = c.T('route')
    if c.on(tr):
        chips(c, 150, 800, [('per route', YEL), ('per component', CYAN), ('per data freshness', WHITE)], tr, 0.4, 34)
    ts = c.T('Say')
    if c.on(ts): stamp(c.cv, 540, 1080, 'SAY IT OUT LOUD', 76, c.P(ts, 0.4), -4, GRN)

SCENES = [
    (hook, "Design the rendering for an online store. Here are the pages. Most candidates get this wrong in the very first sentence."),
    (questions, "Ask three questions for every page. Does it need SEO? Is it the same for everyone? And how often does the data change?"),
    (blog, "The blog needs SEO, is the same for everyone, and rarely changes. So build it once, and serve it from the CDN. The home page changes daily, so make it static too, and revalidate every few minutes."),
    (product, "Product pages: the title, images and description are static, so regenerate them incrementally. But price and stock change constantly, and the add button needs to work, so those are small client islands that fetch fresh data."),
    (search, "Search results are different for every query, so you can't prebuild them. But they need SEO, so render them on the server, and stream: header first, results when ready."),
    (cart, "The cart, checkout, and account pages are behind a login, need no SEO, and are different per user. Client rendering is fine here."),
    (map_, "Put it together, and one store uses four strategies. Modern frameworks let you choose per route."),
    (gotcha, "Interview trap: the most common mistake? Candidates pick one strategy for the whole app. Choose per route, even per component, based on SEO, personalization, and freshness. Say that out loud."),
    (scene_next('S2 · E20', 'INTERVIEW QUESTIONS', 'RSC · actions · islands · edge', 'interview', 'Four'),
     "Next: interview questions. Four questions on the modern rendering toolbox. Comment NOTES for the cheat sheet."),
]
