from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E14', tag='S6 · E14', short='PRESENCE')


def hook(c):
    x0, y0, x1, y1 = phone(c, 540, 700, 600, 560, dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    c.pen.circ(x0 + 70, y0 + 80, 40, fill=TEAL, outline=INK, w=3)
    c.pen.text(x0 + 130, y0 + 60, 'Riya', 'intx', 40, INK, 'lm')
    to, tt, tl = c.T('online'), c.T('typing'), c.T('last')
    s_ = 'last seen today at 9:41' if c.on(tl) else 'typing…' if c.on(tt) else 'online' if c.on(to) else ''
    col = MUTE if c.on(tl) else GRN
    if s_: c.pen.text(x0 + 130, y0 + 112, s_, 'ints', 30, col, 'lm')
    th = c.T('hard')
    if c.on(th): stamp(c.cv, 540, 1150, 'SURPRISINGLY HARD', 66, c.P(th, 0.35), -4, RED); c.sfx(th, 'thud')


def basic(c):
    a = node(c, 200, 600, 220, 160, 'Riya', 0.2, 'phone')
    s = node(c, 860, 600, 240, 160, 'Server', 0.3, 'server')
    tc = c.T('Connect')
    pipe(c, 310, 740, 600, tc, YEL, 40, alive=1 - c.P(c.T('dies'), 0.5))
    if c.on(tc): status(c, 640, 760, 'online', GRN, tc, 34)
    td = c.T('Disconnect')
    if c.on(td): status(c, 640, 830, 'offline', MUTE, td, 34)
    tdi = c.T('dies')
    if c.on(tdi):
        cross(c.pen, 525, 600, 1.0, RED, 9, c.P(tdi, 0.3))
        txt(c, 540, 980, 'no disconnect ever arrives', c.T('never'), 'intx', 38, RED)
        stamp(c.cv, 540, 1110, 'ONLINE FOREVER', 64, c.P(c.T('never') + 0.4, 0.35), -4, RED)


def ttl(c):
    chapter(c, 540, 340, 'S6 · E09', 'heartbeats', c.T('heartbeats'))
    tr = c.T('renews')
    if c.on(tr):
        for k in range(4):
            t = tr + k * 0.6
            if c.on(t):
                x = 140 + k * 200
                c.pen.line([(x, 470), (x, 530)], GRN, 8); c.sfx(t, 'tick')
        frac = 1 - ((c.t - tr) % 0.6) / 0.6 * 0.3 if not c.on(c.T('Miss')) else max(0, 0.7 - (c.t - c.T('Miss')) / 2.0)
        timerbar(c, 140, 600, 940, frac, tr, "presence:riya  TTL 60 s", GRN if frac > 0.2 else RED, 56)
    tm = c.T('expires')
    if c.on(tm): status(c, 380, 820, 'entry expired → offline', MUTE, tm, 36)
    code(c, 40, 920, 1040, 1150, ["SET presence:riya online EX 60"], c.T('heartbeat'), 0.1, 30, 'redis', lang='text')


def room(c):
    title(c, 'THE MEETING ROOM SIGN', 330, c.T('sign'), 84, hlcol=YEL)
    card(c.pen, 300, 450, 780, 1000, 16, (225, 215, 195), 10, 5)
    c.pen.circ(720, 740, 14, fill=INK)
    ext = c.T('extending')
    stop = c.T('Stop')
    occ = not c.on(stop + 0.8)
    c.pen.rr(360, 520, 720, 620, 12, fill=RED if occ else GRN, outline=INK, w=4)
    c.pen.text(540, 570, 'OCCUPIED' if occ else 'FREE', 'osw', 54, WHITE)
    if c.on(ext): label(c, 540, 1080, 'valid only while someone extends it', ext, YEL, INK, 32)
    if c.on(stop + 0.8): c.sfx(stop + 0.8, 'ding')


def multi(c):
    title(c, 'COUNT CONNECTIONS, NOT USERS', 330, c.T('Count'), 66, hlcol=YEL)
    tl = c.T('Laptop')
    for k, (ic, nm, kw) in enumerate((('laptop', 'laptop', 'Laptop'), ('phone', 'phone', 'phone'))):
        t = c.T(kw)
        x = 340 + k * 400
        closed = k == 0 and c.on(c.T('closes'))
        node(c, x, 560, 240, 170, nm, t, ic, fill=LIGHT if closed else WHITE)
        if closed: cross(c.pen, x, 560, 1.4, RED, 9, c.P(c.T('closes'), 0.3))
    ts = c.T('still')
    if c.on(ts): status(c, 400, 750, 'still online (1 connection left)', GRN, ts, 32)
    tf = c.T('flapping')
    if c.on(tf):
        for k in range(8):
            x = 140 + k * 100
            on = k % 2 == 0
            c.pen.rr(x, 880, x + 80, 930, 10, fill=GRN if on else GREY, outline=INK, w=3)
        txt(c, 540, 980, 'tunnel: on, off, on, off…', tf, 'ints', 30, MUTE)
    tw = c.T('wait')
    if c.on(tw): label(c, 540, 1100, 'wait a few seconds before broadcasting offline', tw, YEL, INK, 28)


def fanout(c):
    tf = c.T('five')
    s = node(c, 540, 480, 220, 140, 'Riya', tf, 'phone', size=30)
    if c.on(tf + 0.3):
        n = int(min(40, (c.t - tf - 0.3) * 50))
        for k in range(n):
            ang = math.pi * (0.1 + 0.8 * k / 39)
            x, y = 540 + 380 * math.cos(ang), 560 + 330 * math.sin(ang)
            c.pen.line([(540, 560), (x, y)], mix(PAPER, RED, 0.4), 2, False)
            c.pen.circ(x, y, 12, fill=WHITE, outline=INK, w=2)
        counter(c, 540, 700, 0, 500, tf + 0.3, tf + 1.3, '{:.0f}', 70, RED, ' updates')
    tl = c.T('looking')
    if c.on(tl): label(c, 540, 1000, 'send only to people looking at her', tl, (200, 240, 200), INK, 30)
    tt = c.T('throttle')
    code(c, 40, 1060, 1040, 1350, ["input.addEventListener('input', () => {", '  if (Date.now() - last < 3000) return;', '  last = Date.now();',
                                   "  ws.send('{\"type\":\"typing\"}');", '});'], tt, 0.08, 26, 'typing.js', marks=[(1, c.T('every'), YEL)])


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Store presence in your main database?', c.T('Store'), 'intx', 44, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 600, 'NO', 90, c.P(tn, 0.35), -4, RED); c.sfx(tn, 'thud')
    rows(c, 100, 780, [(c.T('constantly'), 'Changes constantly', 'a write every heartbeat', 'no'), (c.T('expire'), 'Must expire by itself', 'databases do not forget', 'no'),
                       (c.T('memory'), 'In-memory store with TTLs', 'like Redis', 'ok')], gap=160, h=130)


SCENES = [
    (hook, "Open a chat. Under the name, it says online. Then: typing. Close the app on her side, and it becomes last seen. Three tiny words, and a surprisingly hard problem."),
    (basic, "Presence is the server tracking who has a live connection. Connect: online. Disconnect: offline. Simple, until a socket dies silently, and the server never hears a disconnect at all."),
    (ttl, "So presence leans on heartbeats, from episode nine, plus a time to live. Each heartbeat renews the user's entry for, say, sixty seconds. Miss them, and the entry expires. Offline."),
    (room, "It's the occupied sign on a meeting room booking. It's only valid while someone keeps extending it. Stop extending, and the room frees itself."),
    (multi, "Count connections, not users. Laptop closes, but the phone is still open? Still online. And smooth out flapping. In a tunnel, a phone drops and rejoins every few seconds, so wait a little before broadcasting offline."),
    (fanout, "Then there's the cost. A user with five hundred contacts coming online means five hundred updates. So only send presence to people actually looking at that user, and throttle typing to once every few seconds."),
    (trap, "Interview trap: store presence in your main database? No. It changes constantly, and it must expire by itself. Use an in memory store with time to live, like Redis."),
    (scene_next('S6 · E15', 'INTERVIEW QUESTIONS', 'keeping connections alive', 'interview', 'alive'),
     "Next: interview questions on keeping connections alive. Comment NOTES for the cheat sheet."),
]
