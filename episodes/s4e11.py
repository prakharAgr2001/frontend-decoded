from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E11', tag='S4 · E11', short='SERVER STATE', hook="the data you don't own")


def order_tab(c, x0, y0, status, col, label_):
    browser(c, x0, y0, x0 + 450, y0 + 520, url=label_)
    c.pen.text(x0 + 30, y0 + 140, 'Order #4821', 'intx', 32, INK, 'lm')
    c.pen.text(x0 + 30, y0 + 190, 'Chicken Biryani × 1', 'intm', 24, MUTE, 'lm')
    c.pen.rr(x0 + 30, y0 + 240, x0 + 300, y0 + 300, 30, fill=col, outline=INK, w=3)
    c.pen.text(x0 + 165, y0 + 270, status, 'int', 26, WHITE)


def hook(c):
    tc = c.T('cancel')
    order_tab(c, 60, 400, 'CANCELLED' if c.on(tc + 0.4) else 'PREPARING', RED if c.on(tc + 0.4) else ORANGE, 'tab 1')
    order_tab(c, 570, 400, 'PREPARING', ORANGE, 'tab 2')
    if c.on(tc): label(c, 285, 980, 'you cancelled here', tc, YEL, INK, 28)
    tl = c.T('lying')
    if c.on(tl): stamp(c.cv, 795, 1060, 'LYING', 90, c.P(tl, 0.35), -6, RED); c.sfx(tl, 'thud')


def define(c):
    title(c, 'SERVER STATE', 380, 0.1, 130, hlcol=YEL)
    rows(c, 90, 560, [(c.T('lives'), 'lives on a server', None, ORANGE), (c.T('fetch'), 'you only fetch a copy', None, ORANGE),
                      (c.T('change'), 'others can change it without telling you', None, ORANGE)], 150, 900, 120, 38)
    tm = c.T('moment')
    if c.on(tm): title(c, 'STALE ON ARRIVAL', 1100, tm, 80, RED)


def board(c):
    title(c, 'A PHOTO OF THE BOARD', 330, 0.1, 90)
    darkcard(c.pen, 120, 450, 960, 760)
    tp = c.T('platform')
    rowsd = [('12951 Rajdhani', '16:55', '3' if not c.on(tp) else '5'), ('12627 Karnataka', '17:10', '1')]
    for k, (tn, tm, pf) in enumerate(rowsd):
        y = 540 + k * 90
        c.pen.text(160, y, tn, 'monob', 32, YEL, 'lm'); c.pen.text(700, y, tm, 'monob', 32, YEL, 'lm')
        c.pen.text(900, y, pf, 'monob', 36, RED if (k == 0 and c.on(tp)) else YEL, 'mm')
    c.pen.text(540, 720, 'LIVE · the server', 'int', 24, (150, 156, 166))
    tph = c.T('photo')
    if c.on(tph):
        s = c.B(tph, 0.4)
        card(c.pen, 220, 840, 860, 1150, 16, WHITE, 10, 5)
        c.pen.rect(250, 870, 830, 1060, fill=(40, 44, 52))
        c.pen.text(290, 930, '12951  16:55  PF 3', 'monob', 30, YEL, 'lm')
        c.pen.text(290, 1000, '12627  17:10  PF 1', 'monob', 30, YEL, 'lm')
        c.pen.text(540, 1105, 'your copy · the client', 'int', 26, MUTE)
        if c.on(tp): cross(c.pen, 800, 930, 0.7, RED, 7, c.P(tp + 0.3, 0.3))


def diff(c):
    title(c, 'NOT THE SAME KIND', 330, 0.1, 96)
    versus(c, ('CLIENT', BLUE, c.T('Client'), [(c.T('own'), 'you own it'), (c.T('instant'), 'instant, sync'), (c.T('always'), 'always current')]),
           ('SERVER', ORANGE, c.T('Server', 2), [(c.T('borrow'), 'you borrow it'), (c.T('async'), 'async, can fail'), (c.T('stale'), 'can be stale')]), 430, 960, 38)
    ts = c.T('shared')
    if c.on(ts): label(c, 540, 1080, 'shared with other users and other tabs', ts, YEL, INK, 30)


def problems(c):
    title(c, 'NEW PROBLEMS', 330, 0.1, 110, hlcol=YEL)
    items = [('caching', 'caching'), ('deduplicating', 'dedupe identical requests'), ('refetching', 'refetch when stale'), ('background', 'background updates'),
             ('pagination', 'pagination'), ('throw', 'garbage-collect old data')]
    for k, (kw, s_) in enumerate(items):
        t = c.T(kw)
        if not c.on(t): continue
        x = 300 + (k % 2) * 480; y = 520 + (k // 2) * 170
        c.sfx(t, 'pop'); s = c.B(t, 0.35)
        card(c.pen, x - 220 * s, y - 60 * s, x + 220 * s, y + 60 * s, 18, WHITE, 8, 4)
        c.pen.text(x, y, s_, 'ints', 30 * s, INK)


def naive(c):
    head(c, 'THE useEffect FETCH', 'effect', size=70)
    code(c, 30, 440, 1050, 880, ['function Orders() {', '  const [orders, setOrders] = useState([]);', '  const [loading, setLoading] = useState(true);',
                                 '  useEffect(() => {', "    fetch('/api/orders').then((r) => r.json())", '      .then((d) => { setOrders(d); setLoading(false); });',
                                 '  }, []);'], c.T('effect') + 0.3, 0.1, 24, 'Orders.jsx')
    for k, (kw, s_) in enumerate((('cache', 'no cache: refetch on every mount'), ('twice', 'two components = two requests'), ('race', 'race: old response can win'))):
        t = c.T(kw)
        if c.on(t):
            c.sfx(t, 'buzz'); p = c.P(t, 0.3)
            c.pen.circ(130, 960 + k * 100, 20, fill=RED)
            txt(c, 170, 960 + k * 100, s_, t, 'ints', 34, INK, 'lm', 'slide')


def rsc(c):
    chapter(c, 540, 340, 'S2 · E14', 'Server Components', 0.1)
    a = node(c, 270, 560, 360, 170, 'server', c.T('fetch'), ic='server', sub='fetches + renders')
    b = node(c, 810, 560, 360, 170, 'browser', c.T('UI'), ic='laptop', sub='gets finished UI')
    link(c, a, b, c.T('UI'))
    tn = c.T('copy')
    if c.on(tn): label(c, 540, 760, 'read-only data: no client copy to manage', tn, (200, 240, 200), INK, 30)
    tm = c.T('moment')
    if c.on(tm):
        rows(c, 90, 900, [(c.T('interactive'), 'interactive · refetched · edited by the user', None, ORANGE)], 140, 900, 120, 32)
        title(c, 'BACK TO A CLIENT CACHE', 1080, c.T('back'), 70, RED)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 470, 'Should server data go into Redux?', c.T('Redux'), 'intx', 48, INK)
    tu = c.T('Usually')
    if c.on(tu): title(c, 'USUALLY NOT', 600, tu, 100, RED)
    tc = c.T('cache', 1)
    if c.on(tc): txt(c, 540, 720, "it's a cache · treat it like one", tc, 'intx', 42, INK)
    for k, (kw, s_) in enumerate((('React', 'TanStack Query'), ('SWR', 'SWR'), ('RTK', 'RTK Query'))):
        label(c, 230 + k * 310, 880, s_, c.T(kw), (255, 238, 170), INK, 34)


SCENES = [
    (hook, "You open your orders in two tabs. In one tab, you cancel an order. The other tab still says preparing. Both tabs show the same data, and one of them is lying."),
    (define, "That's server state. Data that lives on a server. You fetch a copy of it, and other people, or other tabs, can change it without telling you. Your copy starts going stale the moment it arrives."),
    (board, "It's a photo of the train departures board. Accurate when you took it. Then the platform changes, and your photo has no idea."),
    (diff, "Client state and server state are different animals. Client state: you own it, it's instant, and it's always current. Server state: you borrow it, it's async, and it can be stale. And it's shared."),
    (problems, "So server state brings problems client state never has. Caching. Deduplicating identical requests. Refetching when it's stale. Background updates. Pagination. And knowing when to throw old data away."),
    (naive, "Most apps start with a use effect fetch. It works, but there's no cache, so it refetches on every mount. Two components asking means two requests, fetched twice. And a slow old response can win a race."),
    (rsc, "Remember server components from season two? They fetch on the server and send finished UI, so read only data needs no client copy at all. But the moment data is interactive, refetched, or edited by the user, you're back to managing a client cache."),
    (gotcha, "Interview question: should server data go into Redux? Usually not. It's a cache, so treat it like one. Use a library built for caching, like TanStack's React Query, SWR, or RTK Query."),
    (scene_next('S4 · E12', 'REACT QUERY', 'a cache with superpowers', 'React', 'superpowers'),
     "Next: React Query, a cache with superpowers. Comment NOTES for the cheat sheet."),
]
