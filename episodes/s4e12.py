from engine.lib import *
from engine.s3_extra import rows, netrows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E12', tag='S4 · E12', short='REACT QUERY', hook='instant the second time')


def ordersphone(c, cx, at_load, stale_upd=None, spin=True):
    ib = phone_frame(c, cx, 800, 420, 760)
    x0, y0, x1, y1 = ib
    c.pen.text(x0 + 30, y0 + 40, 'Your orders', 'intx', 32, INK, 'lm')
    if not c.on(at_load):
        if spin:
            a = (c.t * 400) % 360
            c.pen.arc(cx - 40, 760, cx + 40, 840, a, a + 270, INK, 9)
        return
    for k, (nm, st) in enumerate((('Biryani House', 'Delivered'), ('Chai Point', 'Delivered'), ('Pizza Hub', 'Cancelled'))):
        y = y0 + 130 + k * 120
        c.pen.rr(x0 + 20, y - 45, x1 - 20, y + 45, 14, fill=(246, 243, 236))
        c.pen.text(x0 + 40, y - 12, nm, 'int', 26, INK, 'lm')
        c.pen.text(x0 + 40, y + 20, st, 'intm', 20, MUTE, 'lm')
    if stale_upd is not None and c.on(stale_upd):
        y = y0 + 130 + 3 * 120
        p = c.B(stale_upd, 0.35)
        c.pen.rr(x0 + 20, y - 45 * p, x1 - 20, y + 45 * p, 14, fill=(255, 238, 170), outline=INK, w=3)
        c.pen.text(x0 + 40, y - 12, 'Dosa Corner', 'int', 26 * p, INK, 'lm')
        c.pen.text(x0 + 40, y + 20, 'Preparing', 'intm', 20 * p, MUTE, 'lm')


def hook(c):
    ts = c.T('second')
    ordersphone(c, 300, c.T('open') + 1.2)
    if c.on(ts):
        ordersphone(c, 780, ts + 0.05, c.T('quietly') + 0.3)
        label(c, 780, 1240, 'instant', ts, (200, 240, 200), INK, 32)
    label(c, 300, 1240, 'first visit: spinner', c.T('open'), WHITE, INK, 28)
    tq = c.T('quietly')
    if c.on(tq): label(c, 780, 360, '…then quietly updates', tq, YEL, INK, 30)


def usequery(c):
    title(c, 'useQuery', 330, c.T('use'), 110, hlcol=YEL)
    code(c, 30, 440, 1050, 800, ['const { data, isPending, error } = useQuery({', "  queryKey: ['orders', userId],", '  queryFn: () => getOrders(userId),', '});'],
         c.T('use') + 0.3, 0.12, 28, 'Orders.jsx', marks=[(1, c.T('key'), YEL), (2, c.T('fetches'), YEL), (0, c.T('back'), YEL)])
    tn = c.T('effect')
    if c.on(tn): label(c, 540, 900, 'no useEffect · no useState · no loading flags', tn, (200, 240, 200), INK, 30)


def keys(c):
    title(c, 'THE KEY IS AN ADDRESS', 330, c.T('address'), 84, hlcol=YEL)
    cache = node(c, 540, 560, 520, 150, "['orders', 42]", c.T('cache'), fill=(255, 238, 170), sub='one cache entry', size=38)
    comps = []
    for k in range(4):
        b = node(c, 180 + k * 240, 860, 200, 100, ['<Header>', '<Orders>', '<Badge>', '<Help>'][k], c.T('Ten') + k * 0.15, size=26)
        comps.append(b)
        link(c, b, cache, c.T('Ten') + 0.3 + k * 0.15)
    to = c.T('one', 2)
    if c.on(to):
        srv = node(c, 540, 1130, 300, 110, 'server', to, ic='server', size=26)
        link(c, cache, srv, to + 0.2, col=GRN)
        label(c, 860, 1130, '1 request', to + 0.4, (200, 240, 200), INK, 30)


def swr(c):
    title(c, 'STALE-WHILE-REVALIDATE', 330, c.T('revalidate'), 76, hlcol=YEL)
    steps = [('cached', 'show cached data now', YEL), ('background', 'refetch in the background', (220, 225, 235)), ('swaps', 'swap in fresh data if it changed', (200, 240, 200))]
    for k, (kw, s_, col) in enumerate(steps):
        t = c.T(kw)
        node(c, 540, 500 + k * 200, 760, 140, s_, t, fill=col, size=36)
        if k and c.on(t): arrow(c.pen, 540, 500 + k * 200 - 125, 540, 500 + k * 200 - 75, c.P(t, 0.3), INK, 6, 18)
    ta = c.T('assistant')
    if c.on(ta): label(c, 540, 1140, 'like an assistant: answers from memory, then double-checks', ta, WHITE, INK, 26)


def timers(c):
    title(c, 'TWO TIMERS', 330, 0.1, 110, hlcol=YEL)
    for k, (nm, kw, d, sub, col) in enumerate((('staleTime', 'Stale', 'default 0', 'fresh = no refetch', YEL), ('gcTime', 'G', 'default 5 min', 'unused data kept in memory', CYAN))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 560 + k * 330; c.sfx(t, 'pop'); s = c.B(t, 0.35)
        darkcard(c.pen, 90, y - 120 * s, 990, y + 120 * s)
        c.pen.text(140, y - 50, nm, 'monob', 50 * s, col, 'lm')
        c.pen.text(940, y - 50, d, 'int', 30 * s, (180, 186, 196), 'rm')
        c.pen.text(140, y + 45, sub, 'ints', 34 * s, WHITE, 'lm')
    tz = c.T('zero')
    if c.on(tz): label(c, 540, 1180, 'staleTime 0: everything is stale immediately', tz, (255, 225, 190), INK, 28)


def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Network',), dy=(1 - c.P(0, 0.45)) * 900)
    tf = c.T('focus')
    netrows(c, 90, 480, 990, [(c.T('Switch'), 'orders?u=42', ['200', 'fetch'], None), (tf, 'orders?u=42', ['200', 'fetch'], YEL)], 28, 70)
    if c.on(tf): label(c, 540, 700, 'refetch on window focus', tf, YEL, INK, 30)
    tr = c.T('reconnect')
    if c.on(tr): label(c, 540, 800, '+ on reconnect · on mount when stale', tr, WHITE, INK, 28)
    td = c.T('DevTools')
    if c.on(td):
        for k, (st, col) in enumerate((('fresh', GRN), ('stale', ORANGE), ('inactive', GREY))):
            x = 230 + k * 310
            c.pen.rr(x - 130, 920, x + 130, 990, 35, fill=col)
            c.pen.text(x, 955, st, 'int', 30 * c.B(td + k * 0.2, 0.3), WHITE)
        c.pen.text(540, 1060, 'React Query DevTools', 'int', 28, (180, 186, 196))


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'isPending vs isFetching', c.T('isPending'), 'monob', 52, INK)
    rows(c, 90, 620, [(c.T('yet'), 'isPending: no data yet', 'show a skeleton', 'ok'), (c.T('flight'), 'isFetching: any request in flight', 'includes background refetches', BLUE)],
         170, 900, 140, 38, 28)
    tf = c.T('flickers')
    if c.on(tf):
        card(c.pen, 120, 960, 960, 1150, 24, WHITE, 10, 5)
        c.pen.text(540, 1020, 'spinner on isFetching =', 'ints', 34, INK)
        c.pen.text(540, 1090, 'flicker on every tab focus', 'intx', 42, RED)


SCENES = [
    (hook, "You open your orders. A spinner, then the list. You go back, and open them a second time. Instant. And a moment later, it quietly updates."),
    (usequery, "That's what React Query does. You call use query with a key, and a function that fetches. It gives back the data, a pending flag, and an error. No use effect, no extra state."),
    (keys, "The query key is an address in the cache. Ten components asking for the same key share one cache entry, and React Query sends one request."),
    (swr, "When you come back, it shows the cached data immediately, then refetches in the background, and swaps in fresh data only if it changed. This is called stale while revalidate. Like an assistant who answers from memory, then quietly double checks."),
    (timers, "Two timers control it. Stale time: how long data counts as fresh, so no refetch. The default is zero. G C time: how long unused data stays in memory after the last component unmounts. Five minutes by default."),
    (proof, "See it yourself. Open the Network panel. Switch tabs, then come back, and a request fires on focus. It also refetches on reconnect. And React Query DevTools shows every query as fresh, stale, or inactive."),
    (gotcha, "Interview trap: isPending versus isFetching. isPending means there's no data yet, so show a skeleton. isFetching means any request is in flight, even a background refetch. Show a spinner on isFetching, and your page flickers every time the user comes back."),
    (scene_next('S4 · E13', 'CACHE INVALIDATION', 'the hard thing in computer science', 'invalidation', 'hard'),
     "Next: cache invalidation, the famously hard thing in computer science. Comment NOTES for the cheat sheet."),
]
