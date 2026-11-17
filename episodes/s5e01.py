from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E01', tag='S5 · E01', short='REST')


def hook(c):
    box = panel(c, 50, 330, 1030, 1000, tabs=('Network', 'Fetch/XHR'), active=1 if c.on(c.T('Fetch')) else 0,
                dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    tf = c.T('Fetch')
    netrows(c, x0 + 40, y0 + 60, x1 - 40, [
        (tf + 0.2, 'GET /api/me', ['200', 'json']), (tf + 0.4, 'GET /api/feed?limit=10', ['200', 'json']),
        (tf + 0.6, 'GET /api/notifications', ['200', 'json']), (tf + 0.8, 'POST /api/events', ['201', 'json'])],
        size=26, gap=70, cols=[x1 - 230, x1 - 130])
    tj = c.T('JSON')
    if c.on(tj): label(c, 540, y0 + 420, 'your app asking a server for data', tj, YEL, INK, 30)
    tr = c.T('REST')
    if c.on(tr):
        hl(c.pen, 330, 1080, 750, 1220, c.P(tr + 0.1, 0.45))
        title(c, 'REST', 1150, tr, 150)


def define(c):
    title(c, 'EVERYTHING IS A RESOURCE', 340, c.T('resource'), 72, hlcol=YEL)
    for k, (kw, path, nm) in enumerate((('user', '/users/42', 'a user'), ('post', '/posts/7', 'a post'), ('comment', '/posts/7/comments', 'its comments'))):
        t = c.T(kw); y = 520 + k * 150
        if c.on(t):
            s = c.B(t, 0.35); c.sfx(t, 'pop')
            card(c.pen, 110, y - 55 * s, 970, y + 55 * s, 18, WHITE, 8, 4)
            c.pen.text(150, y, path, 'monob', 36 * s, INK, 'lm')
            c.pen.text(930, y, nm, 'int', 30 * s, MUTE, 'rm')
    tv = c.T('verbs')
    if c.on(tv):
        chips(c, 110, 1000, [(m, MCOL[m]) for m in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')], tv, 0.15, 30)


def library(c):
    title(c, 'THE LIBRARY', 340, c.T('library'), 100)
    ts = c.T('shelf')
    for r in range(4):
        for k in range(6):
            x = 140 + k * 135; y = 470 + r * 120
            hi = r == 2 and k == 3 and c.on(ts)
            c.pen.rect(x, y, x + 120, y + 100, fill=YEL if hi else WHITE, outline=INK, w=3)
            for b in range(4):
                c.pen.rect(x + 12 + b * 26, y + 18, x + 32 + b * 26, y + 92, fill=[BLUE, RED, GRN, ORANGE][(b + k + r) % 4])
    if c.on(ts): label(c, 540, 990, 'shelf F · row 12', ts, INK, WHITE, 32)
    for k, (kw, txt_, m) in enumerate((('borrow', 'borrow = GET', 'GET'), ('add', 'add = POST', 'POST'),
                                       ('replace', 'replace = PUT', 'PUT'), ('remove', 'remove = DELETE', 'DELETE'))):
        t = c.T(kw)
        x = 290 + (k % 2) * 500; y = 1110 + (k // 2) * 90
        if c.on(t): c.sfx(t, 'pop'); pill(c.pen, x, y, txt_, c.B(t, 0.35), MCOL[m], WHITE, 30)


def verbs(c):
    title(c, 'FIVE VERBS', 330, 0.1, 96, hlcol=YEL)
    for k, (m, path, sub) in enumerate((('GET', '/users/42', 'read it'), ('POST', '/users', 'create a new one'),
                                        ('PUT', '/users/42', 'replace the whole thing'), ('PATCH', '/users/42', 'change some fields'),
                                        ('DELETE', '/users/42', 'remove it'))):
        method(c, 110, 470 + k * 115, m, path, c.T(m), 32, None)
        if c.on(c.T(m) + 0.2): txt(c, 970, 470 + k * 115, sub, c.T(m) + 0.2, 'int', 28, MUTE, 'rm')
    for k, (kw, s_, col) in enumerate((('OK', '200 OK', GRN), ('created', '201 Created', GRN), ('found', '404 Not Found', RED))):
        t = c.T(kw)
        if c.on(t): c.sfx(t, 'pop'); pill(c.pen, 220 + k * 320, 1100, s_, c.B(t, 0.35), col, WHITE, 30)
    ts = c.T('status')
    if c.on(ts): txt(c, 540, 1020, 'the status code says what happened', ts, 'int', 32, INK)


def code_(c):
    code(c, 40, 380, 1040, 380 + 72 + 4 * 52 + 40, ["const res = await fetch('/api/users/42');",
                                                     'if (!res.ok) throw new Error(res.status);',
                                                     'const user = await res.json();'],
         c.T('fetch') - 0.3, 0.12, 26, 'user.js', marks=[(1, c.T('ok'), YEL), (2, c.T('parse'), YEL)])
    tt = c.T('throw')
    if c.on(tt): stamp(c.cv, 540, 860, 'FETCH DOESN’T THROW ON 404', 58, c.P(tt, 0.35), -3, RED); c.sfx(tt, 'thud')


def proof(c):
    inner = browser(c, 60, 330, 1020, 1130, 'api.github.com/users/torvalds', dy=(1 - c.P(0, 0.45)) * 900)
    tg = c.T('github')
    code(c, 100, 470, 980, 470 + 72 + 6 * 52 + 30, ['{', '  "login": "torvalds",', '  "name": "Linus Torvalds",', '  "type": "User",',
                                                     '  "repos_url": ".../torvalds/repos",', '}'],
         tg + 0.6, 0.12, 28, 'response.json', dy=0)
    tr = c.T('resource')
    if c.on(tr): label(c, 540, 980, 'one resource · one URL · JSON', tr, YEL, INK, 32)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 460, 'PUT vs POST?', c.T('difference'), 'intx', 56, INK)
    tn = c.T('not')
    if c.on(tn):
        txt(c, 540, 550, 'not "create vs update"', tn, 'ints', 36, MUTE)
    ti = c.T('idempotency')
    if c.on(ti): title(c, 'IDEMPOTENCY', 650, ti, 90, hlcol=YEL)
    tp = c.T('PUT', 2)
    if c.on(tp):
        for k in range(5): method(c, 90, 780 + k * 70, 'PUT', '', tp + k * 0.12, 26)
        node(c, 380, 920, 150, 110, '1 user', tp + 0.8, fill=(200, 240, 200), size=30)
    to = c.T('POST', 2)
    if c.on(to):
        for k in range(5): method(c, 560, 780 + k * 70, 'POST', '', to + k * 0.12, 26)
        tq = c.T('orders')
        for k in range(5):
            if c.on(tq + k * 0.1): node(c, 880, 790 + k * 70, 150, 56, 'order', tq + k * 0.1, fill=(255, 220, 220), size=24, sound='tick')


SCENES = [
    (hook, "Open any app, and refresh it with the Network tab open. Filter by Fetch. Those rows are your frontend asking a server for data, usually as JSON. Most of them speak one style. REST."),
    (define, "REST means every thing in your app is a resource, with its own address. A user. A post. Its comments. And you act on each one with a handful of standard verbs."),
    (library, "Think of a library. Every book has a fixed shelf address. You don't describe the book to the librarian, you go to its spot. Then you can borrow it, add a new one, replace it, or remove it."),
    (verbs, "In HTTP, GET reads. POST creates. PUT replaces the whole thing. PATCH changes just some fields. DELETE removes it. And the status code tells you what happened. Two hundred, OK. Two oh one, created. Four oh four, not found."),
    (code_, "In the browser, it's one fetch call. Check response dot ok, because fetch does not throw on a four oh four. Then parse the JSON."),
    (proof, "Try it right now. Open api dot github dot com, slash users, slash torvalds. That's a real REST resource. One user, one URL, as JSON."),
    (gotcha, "Interview trap. What's the difference between PUT and POST? It's not create versus update. It's idempotency. Send the same PUT five times, you still have one user. Send the same POST five times, and you might get five orders."),
    (scene_next('S5 · E02', 'GRAPHQL', 'ask for exactly what you need', 'GraphQL', 'exactly'),
     "Next: GraphQL, where the client asks for exactly what it needs. Comment NOTES for the cheat sheet."),
]
