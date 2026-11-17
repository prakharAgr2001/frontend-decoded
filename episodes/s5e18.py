from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E18', tag='S5 · E18', short='PARTIAL FAILURE')

W6 = ['profile', 'orders', 'wallet', 'offers', 'recs', 'activity']


def widgets(c, x0, y0, broken=None, ok_all=True, at=0.0, w=290, h=200, gx=320, gy=230):
    for k, nm in enumerate(W6):
        x = x0 + (k % 3) * gx; y = y0 + (k // 3) * gy
        bad = broken == nm
        fill = (255, 220, 220) if bad else WHITE
        card(c.pen, x, y, x + w, y + h, 18, fill, 8, 4)
        c.pen.text(x + w / 2, y + 50, nm, 'intx', 32, INK)
        if bad: cross(c.pen, x + w / 2, y + 125, 1.2, RED, 10, c.P(at, 0.3))
        else:
            c.pen.rr(x + 30, y + 100, x + w - 30, y + 120, 8, fill=LIGHT)
            c.pen.rr(x + 30, y + 140, x + w - 80, y + 160, 8, fill=LIGHT)


def hook(c):
    ts = c.T('six')
    tw = c.T('whole')
    tr = c.T('recommendations')
    if c.on(ts) and not c.on(tw):
        widgets(c, 75, 420, 'recs' if c.on(tr) else None, at=tr)
    if c.on(tw):
        b = browser(c, 80, 400, 1000, 1150, 'app.example.com/dashboard')
        c.pen.text(540, 760, 'Something went wrong.', 'intx', 44, INK)
        c.pen.text(540, 830, 'Please reload the page.', 'intm', 32, MUTE)
        stamp(c.cv, 540, 1260, 'ONE WIDGET. WHOLE PAGE.', 60, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')
    if c.on(ts) and not c.on(tw): txt(c, 540, 360, 'a dashboard, six widgets', ts, 'intx', 40, INK)


def why(c):
    tt = c.T('thrown')
    code(c, 60, 360, 1020, 360 + 72 + 3 * 52 + 20, ['function Recs({ data }) {', '  return data.items.map(Card); // crash', '}'], tt - 0.4, 0.1, 28, 'Recs.jsx',
         marks=[(1, tt, YEL)])
    tb = c.T('boundary')
    if c.on(tb): txt(c, 540, 730, 'no error boundary above it', tb, 'intx', 38, RED)
    tu = c.T('unmounts')
    if c.on(tu):
        tree(c, [('a', 'App', 540, 830, None, tu), ('d', 'Dashboard', 540, 940, 'a', tu + 0.1)] +
             [(f'w{k}', W6[k], 130 + k * 165, 1060, 'd', tu + 0.2) for k in range(6)], tu, size=24,
             col=lambda k: (255, 220, 220))
    tf = c.T('five')
    if c.on(tf): stamp(c.cv, 540, 1220, 'ALL UNMOUNTED', 66, c.P(tf, 0.35), -3, RED); c.sfx(tf, 'thud')


def fuse(c):
    title(c, 'ONE FUSE PER ROOM', 340, c.T('fuse'), 90)
    tf = c.T('fuse'); td = c.T('dark')
    for k in range(4):
        x = 130 + (k % 2) * 430; y = 470 + (k // 2) * 330
        dark = k == 1 and c.on(td)
        c.pen.rect(x, y, x + 390, y + 290, fill=(60, 62, 70) if dark else (255, 244, 200), outline=INK, w=6)
        if not dark:
            c.pen.circ(x + 195, y + 80, 30, fill=YEL, outline=INK, w=3)
            c.pen.line([(x + 195, y), (x + 195, y + 50)], INK, 3, False)
        c.pen.text(x + 195, y + 220, ['kitchen', 'study', 'bedroom', 'hall'][k], 'intx', 34, WHITE if dark else INK)
    tl = c.T('lit')
    if c.on(tl): label(c, 540, 1180, 'one room dark · the rest stay lit', tl, YEL, INK, 32)


EB = ['<ErrorBoundary fallback={<WidgetError />}>', '  <Recommendations />', '</ErrorBoundary>', '<ErrorBoundary fallback={<WidgetError />}>',
      '  <Orders />', '</ErrorBoundary>']


def boundary(c):
    code(c, 30, 360, 1050, 360 + 72 + len(EB) * 50 + 20, EB, c.T('boundary') - 0.4, 0.08, 26, 'Dashboard.jsx',
         marks=[(0, c.T('boundary'), YEL), (3, c.T('boundary') + 0.3, YEL)])
    tf = c.T('fallback')
    if c.on(tf):
        card(c.pen, 290, 860, 790, 1120, 20, (255, 236, 236), 8, 4)
        c.pen.text(540, 920, 'Recommendations', 'intx', 34, INK)
        c.pen.text(540, 975, 'couldn’t load right now', 'intm', 28, MUTE)
    tr = c.T('retry')
    if c.on(tr):
        s = c.B(tr, 0.35); c.sfx(tr, 'pop')
        c.pen.rr(440, 1020, 640, 1090, 35, fill=YEL, outline=INK, w=4)
        c.pen.text(540, 1055, 'Retry', 'intx', 32 * s, INK)


def settled(c):
    te = c.T('eleven')
    if c.on(te): chapter(c, 540, 350, 'S5 · E11', 'Promise.allSettled', te)
    code(c, 30, 440, 1050, 440 + 72 + 4 * 50 + 20, ['const r = await Promise.allSettled(', '  W.map((w) => fetchWidget(w)));', "// r[3] = { status: 'rejected' }",
                                                     "// the other five: 'fulfilled'"], c.T('settled'), 0.1, 26, 'load.js', marks=[(3, c.T('rest'), YEL)])
    tr = c.T('rest')
    if c.on(tr): widgets(c, 75, 830, 'offers', at=tr, h=160, gy=190)


def critical(c):
    title(c, 'WHAT IS CRITICAL?', 340, c.T('critical'), 90, hlcol=YEL)
    rows(c, 100, 520, [(c.T('price'), 'price fails', 'show an error page', RED),
                       (c.T('recommendations'), 'recommendations fail', None, ORANGE),
                       (c.T('hide'), 'quietly hide that section', None, GRN)], gap=170, h=140)


def product(c):
    inner = phone(c, 540, 820, 480, 900, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    c.pen.rr(x0 + 20, y0 + 20, x1 - 20, y0 + 240, 14, fill=(120, 170, 220))
    c.pen.text(x0 + 30, y0 + 280, 'Running shoes', 'intx', 32, INK, 'lm')
    c.pen.text(x0 + 30, y0 + 330, '₹2,499', 'intx', 36, GRN, 'lm')
    tf = c.T('fail')
    for k, nm in enumerate(('reviews', 'recommendations', 'delivery estimate')):
        y = y0 + 380 + k * 80
        bad = c.on(tf + k * 0.3)
        c.pen.rr(x0 + 20, y, x1 - 20, y + 64, 10, fill=(255, 230, 230) if bad else LIGHT, outline=RED if bad else GREY, w=3)
        c.pen.text(x0 + 40, y + 32, nm + (' · unavailable' if bad else ''), 'int', 24, INK, 'lm')
    tb = c.T('buy')
    if c.on(tb):
        s = c.B(tb, 0.35); c.sfx(tb, 'ding')
        c.pen.rr(x0 + 30, y1 - 110, x1 - 30, y1 - 30, 40, fill=YEL, outline=INK, w=4)
        c.pen.text((x0 + x1) / 2, y1 - 70, 'Add to cart', 'intx', 34 * s, INK)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tc = c.T('caught')
    if c.on(tc): txt(c, 540, 470, 'Boundary in place, fetch error not caught?', tc, 'intx', 40, INK)
    tr = c.T('rendering')
    rows(c, 100, 620, [(tr, 'errors thrown during render', None, 'ok'), (c.T('handlers'), 'event handlers', None, 'no'), (c.T('async'), 'async code (fetch .catch)', None, 'no')],
         gap=125, h=100, size=34)
    tl = c.T('library')
    code(c, 40, 1000, 1040, 1000 + 72 + 2 * 50 + 20, ['if (error) throw error;  // during render', 'useQuery({ ..., throwOnError: true })'],
         c.T('state'), 0.12, 26, 'fix.jsx', marks=[(1, tl, YEL)])


SCENES = [
    (hook, "A dashboard has six widgets. The recommendations service goes down. And the whole page turns into a white screen, with one error message."),
    (why, "In React, an error thrown while rendering, with no boundary above it, unmounts the entire tree. One broken widget takes down five healthy ones."),
    (fuse, "Your house doesn't black out when one appliance shorts. Each room has its own fuse. One room goes dark, and the rest stay lit."),
    (boundary, "So give each widget its own error boundary, with a small fallback, and a retry button."),
    (settled, "On the data side, fetch with Promise dot all settled, from episode eleven, so one failed request doesn't throw away the rest."),
    (critical, "Then decide what's critical. If the product price fails, show an error page. If recommendations fail, quietly hide that section."),
    (product, "Think of any big product page. Reviews, recommendations, a delivery estimate. Any of them can fail, and you should still be able to buy."),
    (gotcha, "Interview trap. You wrapped a widget in an error boundary, but a failed fetch still isn't caught. Why? Error boundaries only catch errors thrown during rendering. Not in event handlers, not in async code. Put the error in state and throw it while rendering, or let your data library do it."),
    (scene_next('S5 · E19', 'SUSPENSE BOUNDARIES', 'where your loading states go', 'Suspense', 'loading'),
     "Next: Suspense boundaries, and deciding where your loading states go. Comment NOTES for the cheat sheet."),
]
