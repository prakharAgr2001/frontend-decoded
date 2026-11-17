from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E09', tag='S6 · E09', short='HEARTBEATS')


def hook(c):
    x0, y0, x1, y1 = panel(c, 60, 330, 1020, 1150, tabs=('Network', 'WS', 'Messages'), active=2, dy=(1 - c.P(0, 0.45)) * 900)
    tn = c.T('nobody')
    items = []
    for k in range(5):
        t = tn + k * 1.1
        items += [(t, 'up', '{"type":"ping"}', f'12:0{k}:00'), (t + 0.4, 'down', '{"type":"pong"}', f'12:0{k}:00')]
    wsmsgs(c, x0 + 40, y0 + 60, x1 - 40, items[:10], 26, 62)
    tp = c.T('Pong')
    if c.on(tp): stamp(c.cv, 540, 1260, 'PING. PONG.', 80, c.P(tp, 0.35), -4, RED); c.sfx(tp, 'thud')


def silent(c):
    a = node(c, 200, 620, 220, 170, 'Laptop', 0.2, 'laptop')
    b = node(c, 880, 620, 220, 170, 'Server', 0.3, 'server')
    tw = c.T('drops')
    alive = 1 - c.P(tw, 0.6)
    pipe(c, 320, 760, 620, 0.05, YEL, 50, 0.3, alive)
    if c.on(tw):
        cross(c.pen, 540, 620, 1.2, RED, 10, c.P(tw, 0.3))
        c.sfx(tw, 'buzz')
    ta = c.T('announce')
    if c.on(ta): txt(c, 540, 790, 'no goodbye is sent', ta, 'intx', 40, RED)
    tr = c.T('Remember')
    chapter(c, 540, 920, 'S1 · E03', 'TCP: the phone call', tr)
    ts = c.T('silent')
    if c.on(ts):
        pill(c.pen, 260, 1070, 'hello?', c.B(ts, 0.35), WHITE, INK, 34)
        pill(c.pen, 820, 1070, 'hello?', c.B(ts + 0.3, 0.35), WHITE, INK, 34)
    th = c.T('half')
    if c.on(th): label(c, 540, 1200, 'a "half-open" connection', th, YEL, INK, 34)


def harm(c):
    title(c, 'WHY IT HURTS', 330, 0.1, 96, hlcol=YEL)
    to = c.T('online')
    if c.on(to):
        card(c.pen, 120, 450, 960, 600, 22, WHITE, 10, 5)
        c.pen.circ(200, 525, 34, fill=TEAL, outline=INK, w=3)
        c.pen.text(260, 505, 'Riya', 'intx', 36, INK, 'lm')
        status(c, 270, 555, 'online', GRN, to, 26)
        stamp(c.cv, 760, 525, 'SHE ISN\'T', 50, c.P(to + 0.5, 0.35), -5, RED)
    tp = c.T('pile')
    if c.on(tp):
        for k in range(6):
            if c.on(tp + k * 0.15):
                pill(c.pen, 260 + (k % 3) * 280, 700 + (k // 3) * 80, 'msg', c.B(tp + k * 0.15, 0.3), YEL, INK, 28)
        txt(c, 540, 880, 'messages pile up, going nowhere', tp + 0.5, 'ints', 32, INK)
    tl = c.T('idle')
    if c.on(tl):
        label(c, 540, 1020, 'proxies cut idle connections (~60 s)', tl, (255, 210, 210), INK, 32)


def rope(c):
    title(c, 'THE ROPE TUG', 330, c.T('climbers'), 100, hlcol=YEL)
    tc = c.T('climbers')
    if c.on(tc):
        c.pen.line([(180, 560), (900, 1060)], (120, 80, 50), 8)
        person(c.pen, 200, 620, 1.1, ORANGE)
        person(c.pen, 880, 1120, 1.1, BLUE)
    tt = c.T('tug')
    if c.on(tt):
        q = ((c.t - tt) * 1.2) % 1
        x = 300 + 500 * q; y = 630 + 350 * q
        c.pen.circ(x, y, 16, fill=YEL, outline=INK, w=3)
        pill(c.pen, 390, 860, 'tug', c.B(tt, 0.35), WHITE, INK, 32)
    tb = c.T('back')
    if c.on(tb): pill(c.pen, 760, 760, 'tug back: all good', c.B(tb, 0.35), (200, 240, 200), INK, 30); c.sfx(tb, 'pop')
    ta = c.T('acts')
    if c.on(ta): label(c, 540, 1240, 'no tug back = act now, not later', ta, YEL, INK, 34)


def code_(c):
    at = c.T('pings') + 0.2
    code(c, 40, 340, 1040, 1000, ['let timer;', 'function heartbeat() {', '  clearTimeout(timer);', '  timer = setTimeout(() => ws.close(), 35000);', '}',
                                  'ws.onmessage = (e) => {', '  heartbeat();', "  if (e.data === 'ping') return ws.send('pong');", '  handle(e.data);', '};'],
         at, 0.08, 26, 'heartbeat.js',
         marks=[(6, c.T('resets'), YEL), (3, c.T('dead'), YEL), (7, c.T('answer'), YEL)])
    tr = c.T('reconnect')
    if c.on(tr): label(c, 540, 1110, 'onclose → reconnect (episode ten)', tr, WHITE, INK, 32)


def builtin(c):
    title(c, 'PROTOCOL PINGS?', 330, c.T('built'), 90, hlcol=YEL)
    rows(c, 100, 520, [(c.T('silently'), 'Browser answers server pings', 'automatically, invisible to JS', 'ok'),
                       (c.T('JavaScript'), 'JS cannot send a ping frame', 'no ws.ping() in browsers', 'no')], gap=170, h=130)
    ta = c.T('own')
    if c.on(ta): label(c, 540, 900, "so apps send their own: {type: 'ping'}", ta, YEL, INK, 32)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'What interval?', c.T('interval'), 'intx', 56, INK)
    tf = c.T('fast')
    if c.on(tf): rows(c, 100, 620, [(tf, 'Too fast', 'drains batteries + server CPU', 'no')], h=120)
    ts = c.T('slow')
    if c.on(ts): rows(c, 100, 780, [(ts, 'Too slow', 'the idle timeout kills you first', 'no')], h=120)
    tu = c.T('under')
    if c.on(tu): rows(c, 100, 940, [(tu, 'Under the shortest idle timeout', 'often 20 to 30 seconds', 'ok')], h=120)


SCENES = [
    (hook, "Leave a chat tab open, with WS messages showing. Even when nobody types, on many apps, a tiny message goes out every few seconds, and one comes back. Ping. Pong."),
    (silent, "Here's why. When Wi-Fi drops, or a laptop sleeps, a TCP connection doesn't announce that it's dead. Remember the phone call, from season one, episode three? The line can go silent, and neither side knows if the other hung up. That's a half open connection."),
    (harm, "So your app shows your friend as online, while messages pile up, going nowhere. And proxies and load balancers quietly cut connections that stay idle for too long."),
    (rope, "It's two climbers on a rope. Every few minutes, one gives a tug. A tug back means: all good. If no tug comes back, the climber acts now, not later."),
    (code_, "In code: the server pings every thirty seconds. Every message resets a timer. No message for thirty five seconds? Assume the connection is dead, and close it. Answer pings with pongs, so the server can do the same. Then reconnect."),
    (builtin, "Wait, doesn't WebSocket have built in ping frames? It does. But the browser answers them silently, and JavaScript can't send them. That's why apps send their own heartbeat messages."),
    (trap, "Interview trap: what interval? Too fast, and you drain phone batteries and server CPU. Too slow, and the idle timeout kills you first. Stay under the shortest idle timeout on the path, often twenty to thirty seconds."),
    (scene_next('S6 · E10', 'RECONNECT', 'without stampeding the server', 'reconnect', 'stampeding'),
     "Next: how to reconnect, without stampeding the server. Comment NOTES for the cheat sheet."),
]
