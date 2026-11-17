from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E02', tag='S5 · E02', short='GRAPHQL')

FIELDS = ['"id"', '"name"', '"avatar"', '"email"', '"phone"', '"bio"', '"created_at"', '"plan"', '"locale"', '"settings"', '"followers"', '"…"']


def hook(c):
    inner = phone(c, 260, 760, 380, 700, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    c.pen.circ((x0 + x1) / 2, y0 + 90, 50, fill=BLUE, outline=INK, w=4)
    c.pen.rr(x0 + 60, y0 + 160, x1 - 60, y0 + 190, 10, fill=INK)
    for k in range(3): c.pen.rr(x0 + 30, y0 + 230 + k * 110, x1 - 30, y0 + 320 + k * 110, 12, fill=LIGHT, outline=GREY, w=2)
    tt = c.T('three', 2)
    for k, p in enumerate(('/users/42', '/users/42/posts', '/posts/…/likes')):
        method(c, 480, 470 + k * 90, 'GET', p, tt + k * 0.25, 26)
    tf = c.T('forty')
    if c.on(tf):
        for k, f in enumerate(FIELDS):
            used = f in ('"name"', '"avatar"')
            x = 480 + (k % 2) * 260; y = 790 + (k // 2) * 62
            if c.on(tf + k * 0.05):
                c.pen.rr(x, y - 24, x + 240, y + 24, 12, fill=YEL if used else LIGHT, outline=INK if used else GREY, w=3)
                c.pen.text(x + 120, y, f, 'mono', 24, INK if used else MUTE)


def problem(c):
    to = c.T('Over')
    if c.on(to):
        title(c, 'OVER-FETCHING', 400, to, 90, hlcol=YEL)
        txt(c, 540, 490, 'too much data per call', to + 0.3, 'int', 36, MUTE)
    tu = c.T('Under')
    if c.on(tu):
        title(c, 'UNDER-FETCHING', 650, tu, 90, hlcol=YEL)
        txt(c, 540, 740, 'too little per call, so more calls', tu + 0.3, 'int', 36, MUTE)
    tp = c.T('phone')
    if c.on(tp):
        icon(c.pen, 'phone', 540, 960, 1.4 * c.B(tp, 0.4))
        stamp(c.cv, 540, 1150, 'BOTH HURT', 70, c.P(c.T('hurt'), 0.35), -4, RED); c.sfx(c.T('hurt'), 'thud')


def counter_(c):
    title(c, 'THE ORDER FORM', 340, c.T('counter'), 96)
    tt = c.T('tick')
    card(c.pen, 220, 450, 860, 1080, 20, WHITE, 10, 5)
    c.pen.text(540, 510, 'SANDWICH ORDER', 'osw', 44, INK)
    for k, (f, on) in enumerate((('bread', True), ('paneer', True), ('onion', False), ('cheese', True), ('olives', False), ('mayo', False))):
        y = 600 + k * 75
        c.pen.rr(270, y - 22, 314, y + 22, 6, fill=WHITE, outline=INK, w=4)
        if on and c.on(tt + k * 0.15): check(c.pen, 292, y, 0.8, GRN, 7, c.P(tt + k * 0.15, 0.25)); c.sfx(tt + k * 0.15, 'tick')
        c.pen.text(340, y, f, 'ints', 34, INK, 'lm')
    ts = c.T('slip')
    if c.on(ts): label(c, 540, 1160, 'one slip · exactly what you ticked', ts, YEL, INK, 32)


Q = ['query {', '  user(id: 42) {', '    name', '    avatar', '    posts(last: 3) { title }', '  }', '}']
R = ['{ "user": {', '  "name": "Asha",', '  "avatar": "/a/42.jpg",', '  "posts": [{ "title": "…" }]', '} }']


def how(c):
    te = c.T('endpoint')
    if c.on(te): method(c, 260, 350, 'POST', '/graphql', te, 34)
    code(c, 60, 420, 1020, 420 + 72 + len(Q) * 46 + 20, Q, c.T('query'), 0.1, 26, 'query.graphql', marks=[(2, c.T('shaped'), YEL), (3, c.T('shaped'), YEL)])
    tm = c.T('mirrors')
    code(c, 60, 900, 1020, 900 + 72 + len(R) * 46 + 20, R, tm - 0.2, 0.1, 26, 'response.json', dy=(1 - c.P(tm - 0.6, 0.45)) * 900)
    ts = c.T('schema')
    if c.on(ts): label(c, 540, 1300, 'schema = every type + field', ts, YEL, INK, 30)


def proof(c):
    box = panel(c, 50, 330, 1030, 1050, tabs=('Network', 'Filter: graphql'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    tg = c.T('graphql')
    netrows(c, x0 + 40, y0 + 60, x1 - 40, [(tg + k * 0.25, 'graphql/query', ['POST', '200']) for k in range(5)],
            size=28, gap=72, cols=[x1 - 260, x1 - 120])
    tu = c.T('same')
    if c.on(tu): label(c, 540, y0 + 480, 'same URL · query in the body', tu, YEL, INK, 30)
    tp = c.T('POST')
    if c.on(tp): txt(c, 540, y0 + 580, 'instagram.com on the web', tp, 'int', 30, (180, 186, 196))


def cost(c):
    head(c, 'NOT FREE', 'free', size=90)
    tc = c.T('caching')
    if c.on(tc):
        node(c, 280, 650, 300, 200, 'CDN cache', tc, 'cloud')
        cross(c.pen, 420, 560, 1.2, RED, 12, c.P(tc + 0.3, 0.3))
        txt(c, 280, 800, 'POST · one URL', tc + 0.3, 'int', 30, MUTE)
    tn = c.T('nested')
    if c.on(tn):
        tree(c, [('u', 'user', 780, 520, None, tn), ('f', 'friends', 780, 640, 'u', tn + 0.2), ('ff', 'friends', 780, 760, 'f', tn + 0.4),
                 ('fff', 'friends', 780, 880, 'ff', tn + 0.6), ('p', 'posts', 780, 1000, 'fff', tn + 0.8)], tn, size=28)
        tw = c.T('work')
        if c.on(tw): stamp(c.cv, 540, 1160, 'HUGE SERVER WORK', 64, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    t2 = c.T('worked')
    if c.on(t2): pill(c.pen, 540, 470, 'Status 200 → it worked?', c.B(t2, 0.35), WHITE, INK, 38)
    te = c.T('errors')
    code(c, 80, 560, 1000, 560 + 72 + 5 * 50 + 20, ['{', '  "data": { "user": null },', '  "errors": [', '    { "message": "Not authorised" } ]', '}'],
         c.T('often'), 0.1, 26, 'HTTP 200 OK', marks=[(2, te, YEL), (3, te, YEL)])
    ts = c.T('status')
    if c.on(ts): label(c, 540, 1060, 'check errors, not just the status', ts, (255, 220, 220), INK, 32)


SCENES = [
    (hook, "A profile page needs a name, an avatar, and the last three posts. With REST, that's often three requests. And the user endpoint sends back forty fields you'll never show."),
    (problem, "Two problems. Over fetching: too much data per call. Under fetching: too little per call, so you make more calls. On a slow phone network, both hurt."),
    (counter_, "GraphQL is like a sandwich counter with an order form. You tick exactly the fillings you want, hand over one slip, and get exactly that sandwich back."),
    (how, "There's one endpoint, usually slash graphql. The client sends a query, shaped like the answer it wants. And the response mirrors that shape. A schema on the server defines every type and field."),
    (proof, "See it live. Open Instagram on the web, and filter the Network tab by graphql. The requests keep hitting the same URL. They're POST requests, with the query in the body."),
    (cost, "But it's not free. Everything is a POST to one URL, so normal HTTP caching and CDNs can't help by default. And one deeply nested query can ask the server for a huge amount of work."),
    (gotcha, "Interview trap. The GraphQL request returned two hundred, so it worked, right? Not necessarily. GraphQL servers often return two hundred OK, with an errors array in the body. Always check errors, not just the status."),
    (scene_next('S5 · E03', 'REST · GRAPHQL · tRPC', 'how to choose', 'REST', 'choose'),
     "Next: REST, GraphQL, or tRPC, and how to choose. Comment NOTES for the cheat sheet."),
]
