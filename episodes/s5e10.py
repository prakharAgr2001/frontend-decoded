from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E10', tag='S5 · E10', short='WATERFALLS', hook='fast requests, slow page')

STAIRS = [('/api/me', 0.0, 0.25), ('/users/42/posts', 0.25, 0.5), ('/posts/7/comments', 0.5, 0.75), ('/authors?ids=…', 0.75, 1.0)]


def hook(c):
    box = panel(c, 40, 330, 1040, 1000, tabs=('Network', 'Waterfall'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    tf = c.T('fast')
    reqbars(c, x0 + 30, x1 - 30, y0 + 70, [(0.4 + k * 0.5, n, a, b, YEL, 0.45) for k, (n, a, b) in enumerate(STAIRS)], gap=90, lab_w=330)
    tt = c.T('three')
    if c.on(tt): counter(c, 540, 1120, 0, 3.2, tt, tt + 0.8, '{:.1f}', 120, RED, ' s')
    tq = c.T('queue')
    if c.on(tq): label(c, 540, y0 + 480, 'each request is fast · they wait in a queue', tq, YEL, INK, 30)


def what(c):
    title(c, 'REQUEST WATERFALL', 340, c.T('waterfall'), 88, hlcol=YEL)
    reqbars(c, 80, 1000, 520, [(c.T('staircase') + k * 0.3, n, a, b, YEL, 0.4) for k, (n, a, b) in enumerate(STAIRS)], gap=100, lab_w=330, dark=False)
    tn = c.T('needs')
    if c.on(tn):
        for k in range(3):
            xa = 80 + 330 + 590 * STAIRS[k][2]
            arrow(c.pen, xa, 540 + k * 100, xa, 600 + k * 100, c.P(tn + k * 0.15, 0.3), RED, 5, 16)
    tr = c.T('round')
    if c.on(tr): label(c, 540, 1000, 'every step pays a full round trip', tr, (255, 220, 220), INK, 32)


def rtt(c):
    tr = c.T('Remember')
    if c.on(tr): chapter(c, 540, 350, 'S1 · E03', 'TCP round trips', tr)
    th = c.T('hundred')
    for k in range(4):
        t = th + k * 0.35
        if not c.on(t): continue
        x = 110 + k * 220; c.sfx(t, 'tick')
        c.pen.rect(x, 520, x + 200 * c.P(t, 0.3), 620, fill=YEL, outline=INK, w=4)
        c.pen.text(x + 100, 570, '200 ms', 'intx', 30, INK)
    tf = c.T('Four')
    if c.on(tf): counter(c, 540, 780, 0, 800, tf, tf + 1.0, '{:.0f}', 140, RED, ' ms')
    ts = c.T('second')
    if c.on(ts): txt(c, 540, 920, 'before any data shows', ts, 'intx', 40, INK)


def relay(c):
    title(c, 'THE RELAY RACE', 340, c.T('relay'), 96)
    tb = c.T('baton')
    for k in range(4):
        x = 170 + k * 250
        moving = c.on(tb + k * 0.6)
        dx = 30 * math.sin(c.t * 10) if moving and not c.on(tb + (k + 1) * 0.6) else 0
        person(c.pen, x + dx, 780, 1.2, [BLUE, ORANGE, GRN, PURPLE][k])
        if c.on(tb + k * 0.6) and not c.on(tb + (k + 1) * 0.6):
            c.pen.rr(x + dx + 30, 680, x + dx + 90, 700, 8, fill=YEL, outline=INK, w=3)
    c.pen.line([(90, 800), (990, 800)], INK, 6)
    tsm = c.T('sum')
    if c.on(tsm): label(c, 540, 960, 'race time = the sum of every leg', tsm, YEL, INK, 34)


CODE = ['function Profile() {', "  const user = useFetch('/api/me');", '  if (!user) return <Spinner />;', '  return <Posts userId={user.id} />;', '}',
        'function Posts({ userId }) {', '  const posts = useFetch(`/users/${userId}/posts`);', '  // ...', '}']


def react(c):
    code(c, 30, 360, 1050, 360 + 72 + len(CODE) * 50 + 20, CODE, c.T('React'), 0.08, 26, 'Profile.jsx',
         marks=[(1, c.T('parent'), YEL), (3, c.T('child'), YEL), (6, c.T('own'), YEL)])
    tr = c.T('render', 2) if sum(1 for w in c.words if w[0].lower().startswith('render')) > 1 else c.T('render')
    if c.on(tr): stamp(c.cv, 540, 1060, 'FETCH-ON-RENDER', 70, c.P(tr, 0.35), -4, RED); c.sfx(tr, 'thud')


def fix(c):
    title(c, 'START FETCHES EARLY', 340, c.T('early'), 84, hlcol=YEL)
    tl = c.T('loader')
    if c.on(tl):
        txt(c, 80, 470, 'before', tl, 'intx', 32, RED, 'lm')
        reqbars(c, 80, 1000, 530, [(tl, '/api/me', 0, 0.33, RED, 0.3), (tl + 0.2, '/posts', 0.33, 0.66, RED, 0.3), (tl + 0.4, '/comments', 0.66, 1.0, RED, 0.3)],
                gap=70, lab_w=260, dark=False)
    th = c.T('hoist')
    if c.on(th):
        txt(c, 80, 800, 'after: in the route loader', th, 'intx', 32, GRN, 'lm')
        reqbars(c, 80, 1000, 860, [(th, '/api/me', 0, 0.33, GRN, 0.3), (th, '/posts', 0, 0.36, GRN, 0.3), (th, '/comments', 0, 0.3, GRN, 0.3)],
                gap=70, lab_w=260, dark=False)
    tt = c.T('then')
    if c.on(tt): label(c, 540, 1160, 'fetch-then-render, not fetch-on-render', tt, YEL, INK, 30)


def proof(c):
    box = panel(c, 40, 330, 1040, 1100, tabs=('Network', 'Waterfall'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    td = c.T('diagonal')
    if c.on(td):
        txt(c, x0 + 40, y0 + 50, 'staircase = waiting on each other', td, 'intx', 30, RED, 'lm')
        reqbars(c, x0 + 40, x1 - 40, y0 + 120, [(td + k * 0.2, f'req {k + 1}', k * 0.25, (k + 1) * 0.25, RED, 0.3) for k in range(4)], gap=60, lab_w=150)
    tv = c.T('vertically')
    if c.on(tv):
        txt(c, x0 + 40, y0 + 390, 'stacked = parallel', tv, 'intx', 30, GRN, 'lm')
        reqbars(c, x0 + 40, x1 - 40, y0 + 450, [(tv, f'req {k + 1}', 0, 0.28 + 0.04 * k, GRN, 0.3) for k in range(4)], gap=56, lab_w=150)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tn = c.T('needs')
    if c.on(tn): txt(c, 540, 470, 'Request 2 needs data from request 1?', tn, 'intx', 44, INK)
    br = node(c, 160, 720, 200, 200, 'app', c.T('server'), 'phone')
    sv = node(c, 540, 720, 240, 200, 'BFF', c.T('BFF'), 'server', fill=YEL, sub='one endpoint')
    db = node(c, 900, 720, 200, 200, 'DB', c.T('database'), 'db')
    if c.on(c.T('BFF')): link(c, br, sv, c.T('BFF'), 0.4, INK, 6, '1 call')
    if c.on(c.T('database')):
        link(c, sv, db, c.T('database'), 0.3, GRN, 5)
        label(c, 720, 900, 'join here: fast hops', c.T('database') + 0.2, (200, 240, 200), INK, 26)
    tj = c.T('join')
    if c.on(tj): txt(c, 540, 1080, 'move the join to the server', tj, 'intx', 40, INK)


SCENES = [
    (hook, "A profile page takes three point two seconds to load. Each request is fast. The problem is, they're standing in a queue."),
    (what, "That staircase is a request waterfall. Request two can't start until request one finishes, because it needs something from the response. And each step pays a full round trip."),
    (rtt, "Remember round trips from season one. On a mobile network, one can take two hundred milliseconds or more. Four in a row, and you've lost most of a second, before any data shows."),
    (relay, "It's a relay race. Each runner stands still until the baton arrives. However fast the runners are, the race takes the sum of every leg."),
    (react, "In React, waterfalls hide inside components. The parent fetches in an effect, renders the child, and only then does the child start its own fetch. It's called fetch on render."),
    (fix, "The fix: start fetches as early as possible. Kick them off in the route loader, before rendering, or hoist them up to the parent. Fetch, then render."),
    (proof, "See it yourself. Open the Network panel, and read the waterfall column. A diagonal staircase means requests are waiting on each other. Bars stacked vertically are running in parallel."),
    (gotcha, "Interview trap. Request two needs the user id from request one, so you can't parallelize. Now what? Move the join to the server. Let one endpoint, or a BFF, return the user with their posts, so that dependency is resolved next to the database, not across the internet."),
    (scene_next('S5 · E11', 'PARALLEL REQUESTS', 'Promise.all, and the one people forget', 'parallel', 'Promise'),
     "Next: running requests in parallel, with Promise dot all, and the one method people forget. Comment NOTES for the cheat sheet."),
]
