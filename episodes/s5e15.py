from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E15', tag='S5 · E15', short='DEDUPLICATION', hook='3 components, 1 request')


def hook(c):
    box = panel(c, 40, 330, 1040, 960, tabs=('Network', 'Fetch/XHR'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    tm = c.T('me')
    netrows(c, x0 + 40, y0 + 70, x1 - 40, [(tm + k * 0.25, 'GET /api/me', ['200', '12:00:01.204'], RED if c.on(c.T('moment')) else None) for k in range(3)],
            size=28, gap=80, cols=[x1 - 380, x1 - 270])
    tt = c.T('Three')
    if c.on(tt): bignum(c, 540, 1110, '×3', tt, 150, RED)
    tmo = c.T('moment')
    if c.on(tmo): label(c, 540, y0 + 360, 'same URL · same moment', tmo, YEL, INK, 32)


def why(c):
    app = node(c, 540, 420, 220, 110, 'App', 0.2, size=34, sound=None)
    parts = [('header', 'Header', 'avatar'), ('sidebar', 'Sidebar', 'name'), ('settings', 'Settings', 'plan')]
    boxes = []
    for k, (kw, nm, sub) in enumerate(parts):
        t = c.T(kw)
        b = node(c, 200 + k * 340, 640, 280, 150, nm, t, sub=sub, size=34)
        boxes.append(b)
        if c.on(t): link(c, app, b, t, 0.3, INK, 4)
    api = node(c, 540, 1000, 300, 150, '/api/me', c.T('own'), 'server', size=32)
    to = c.T('own')
    if c.on(to):
        for k, b in enumerate(boxes):
            link(c, b, api, to + k * 0.15, 0.35, RED, 5)
            packet(c, b, api, to + 0.4 + k * 0.15, to + 1.2 + k * 0.15, RED)


def pizza(c):
    title(c, 'THREE CALLS, ONE PIZZA', 340, c.T('pizza'), 80)
    tp = c.T('pizza')
    for k in range(3):
        x = 230 + k * 310
        person(c.pen, x, 760, 1.2, [BLUE, ORANGE, GRN][k])
        if c.on(tp + k * 0.25) and not c.on(c.T('enough')):
            icon(c.pen, 'phone', x + 60, 600, 0.6); c.sfx(tp + k * 0.25, 'tick')
    te = c.T('enough')
    if c.on(te):
        icon(c.pen, 'phone', 290, 600, 0.6)
        stamp(c.cv, 540, 880, 'ONE CALL', 70, c.P(te, 0.35), -4, GRN); c.sfx(te, 'thud')
    ts = c.T('shares')
    if c.on(ts):
        s = c.B(ts, 0.4)
        c.pen.circ(540, 1090, 130 * s, fill=(240, 190, 90), outline=INK, w=5)
        c.pen.circ(540, 1090, 105 * s, fill=(230, 90, 60))
        for a in range(0, 360, 60):
            r = math.radians(a)
            c.pen.line([(540, 1090), (540 + math.cos(r) * 130 * s, 1090 + math.sin(r) * 130 * s)], INK, 3, False)


CODE = ['const inflight = new Map();', 'function dedupFetch(url) {', '  if (!inflight.has(url)) {', '    const p = fetch(url).then((r) => r.json())',
        '      .finally(() => inflight.delete(url));', '    inflight.set(url, p);', '  }', '  return inflight.get(url);', '}']


def how(c):
    title(c, 'DEDUPLICATION', 340, c.T('deduplication'), 100, hlcol=YEL)
    code(c, 30, 430, 1050, 430 + 72 + len(CODE) * 50 + 20, CODE, c.T('map') - 0.3, 0.08, 26, 'dedup.js',
         marks=[(0, c.T('flight'), YEL), (7, c.T('promise'), YEL)])
    ts = c.T('same')
    if c.on(ts): label(c, 540, 1060, 'same key while loading → same promise', ts, YEL, INK, 30)


def rq(c):
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 350, 'S4 · E12', 'React Query', ts)
    tc = c.T('Three')
    for k in range(3):
        y = 440 + k * 145
        if c.on(tc + k * 0.2):
            code(c, 60, y, 1020, y + 130, ["useQuery({ queryKey: ['me'], queryFn: getMe })"], tc + k * 0.2, 0.1, 25, f'Comp{k + 1}.jsx', dy=0)
    to = c.T('one')
    if c.on(to):
        box = panel(c, 60, 900, 1020, 1160, tabs=('Network',), dy=(1 - c.P(to, 0.45)) * 600)
        netrows(c, box[0] + 40, box[1] + 60, box[2] - 40, [(to + 0.3, 'GET /api/me', ['200'])], size=28, gap=70, cols=[box[2] - 120])
        txt(c, 540, 1110 + (1 - c.P(to, 0.45)) * 600, '1 request, 3 components', to + 0.5, 'intx', 32, WHITE)


def vscache(c):
    head(c, 'DEDUP IS NOT CACHE', 'Careful', size=84)
    c.pen.line([(100, 800), (980, 800)], INK, 6)
    tf = c.T('flight')
    if c.on(tf):
        p = c.P(tf, 0.5)
        c.pen.rect(160, 680, 160 + 380 * p, 790, fill=YEL, outline=INK, w=4)
        c.pen.text(350, 735, 'in flight: dedup', 'intx', 32, INK)
        c.pen.text(160, 850, 'request starts', 'int', 26, MUTE, 'lm')
    tc = c.T('cache')
    if c.on(tc):
        p = c.P(tc, 0.5)
        c.pen.rect(560, 680, 560 + 400 * p, 790, fill=(200, 230, 250), outline=INK, w=4)
        c.pen.text(760, 735, 'after: cache', 'intx', 32, INK)
        c.pen.text(560, 850, 'response lands', 'int', 26, MUTE, 'lm')
    tl = c.T('later')
    if c.on(tl): label(c, 540, 1000, 'dedup shares a request · cache keeps the answer', tl, WHITE, INK, 28)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tt = c.T('twice')
    if c.on(tt):
        box = panel(c, 60, 430, 1020, 650, tabs=('Network · dev',), dy=0)
        netrows(c, box[0] + 40, box[1] + 40, box[2] - 40, [(tt, 'GET /api/me', ['200']), (tt + 0.3, 'GET /api/me', ['200'])], size=26, gap=50, cols=[box[2] - 120])
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 740, 'NOT A BUG', 70, c.P(tn, 0.35), -4, GRN); c.sfx(tn, 'thud')
    tsm = c.T('Strict')
    if c.on(tsm):
        for k, (s_, col) in enumerate((('mount', GRN), ('unmount', RED), ('mount', GRN))):
            pill(c.pen, 220 + k * 320, 880, s_, c.B(tsm + k * 0.25, 0.35), col, WHITE, 32); c.sfx(tsm + k * 0.25, 'pop')
        txt(c, 540, 970, '<StrictMode> in development', tsm + 0.8, 'intx', 34, INK)
    tp = c.T('Production')
    if c.on(tp): label(c, 540, 1100, 'production: fetches once', tp, YEL, INK, 32)


SCENES = [
    (hook, "Open the Network tab on a dashboard. You see slash api slash me. Three times. Same URL, at the same moment."),
    (why, "The header needs the user's avatar. The sidebar needs their name. The settings card needs their plan. And each component fetches it on its own."),
    (pizza, "It's like three people in one house, each calling the same pizza place, to order the same pizza. One call is enough, and everyone shares."),
    (how, "The fix is deduplication. Keep a map of requests in flight. If someone asks for the same key while it's still loading, hand them the same promise."),
    (rq, "React Query does this by query key, from season four. Three components ask for the key me, and only one request goes out."),
    (vscache, "Careful: dedup is not caching. Dedup shares a request while it's in flight. A cache keeps the answer after it lands, for later."),
    (gotcha, "Interview trap. In development, your effect fetches twice, even with one component. Is your dedup broken? No. React Strict Mode mounts, unmounts, and mounts again in development, to surface missing cleanups. Production fetches once."),
    (scene_next('S5 · E16', '429: SLOW DOWN', 'rate limits + Retry-After', 'twenty', 'limit'),
     "Next: four twenty nine, too many requests, and how to respect a rate limit. Comment NOTES for the cheat sheet."),
]
