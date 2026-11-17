from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E13', tag='S6 · E13', short='SCALING WEBSOCKETS')


def hook(c):
    s = node(c, 540, 820, 240, 170, 'one server', c.T('specific'), 'server')
    tc = c.T('cheap')
    if c.on(tc):
        pipe(c, 150, 420, 820, tc, YEL, 40)
        icon(c.pen, 'laptop', 110, 820, 0.8)
    th = c.T('hours')
    if c.on(th): txt(c, 540, 1000, 'held open for hours', th, 'ints', 34, INK)
    tm = c.T('million')
    if c.on(tm):
        n = int(min(160, (c.t - tm) * 120))
        for k in range(n):
            ang = k * 2.4; r = 260 + (k * 37) % 180
            x, y = 540 + r * math.cos(ang), 820 + r * math.sin(ang) * 0.9
            c.pen.circ(x, y, 9, fill=YEL, outline=INK, w=2)
        counter(c, 540, 400, 0, 1000000, tm, tm + 1.2, '{:,.0f}', 110, RED, '')


def stateful(c):
    title(c, 'STATELESS vs STATEFUL', 330, c.T('stateless'), 80, hlcol=YEL)
    sa = node(c, 300, 760, 240, 160, 'Server A', c.T('Alice'), 'server')
    sb = node(c, 780, 760, 240, 160, 'Server B', c.T('Bob'), 'server')
    ta, tb = c.T('Alice'), c.T('Bob')
    if c.on(ta): person(c.pen, 300, 1080, 0.9, PINK); txt(c, 300, 1110, 'Alice', ta, 'intx', 30, INK)
    if c.on(tb): person(c.pen, 780, 1080, 0.9, CYAN); txt(c, 780, 1110, 'Bob', tb, 'intx', 30, INK)
    if c.on(ta): c.pen.line([(300, 840), (300, 940)], YEL, 10)
    if c.on(tb): c.pen.line([(780, 840), (780, 940)], YEL, 10)
    ts = c.T('sends')
    packet(c, (260, 940, 340, 1000), sa, ts, ts + 0.6, YEL, 'hi Bob')
    tn = c.T('have')
    if c.on(tn):
        pill(c.pen, 300, 590, 'Bob? not here', c.B(tn, 0.35), (255, 210, 210), INK, 30); c.sfx(tn, 'buzz')


def callcentre(c):
    title(c, 'THE CALL CENTRE', 330, c.T('centre'), 96, hlcol=YEL)
    for k in range(3):
        x = 240 + k * 300
        person(c.pen, x, 700, 1.0, [BLUE, ORANGE, GRN][k])
        icon(c.pen, 'phone', x + 60, 580, 0.45)
        txt(c, x, 740, f'operator {k + 1}', c.T('operator'), 'ints', 26, MUTE)
    tm = c.T('mail')
    if c.on(tm):
        s = c.B(tm, 0.4)
        card(c.pen, 540 - 200 * s, 900 - 80 * s, 540 + 200 * s, 900 + 80 * s, 16, (225, 215, 195), 8, 4)
        c.pen.text(540, 900, 'MAIL ROOM', 'osw', 44 * s, INK)
        packet(c, (180, 640, 300, 720), (340, 820, 740, 980), tm + 0.3, tm + 0.9, YEL, 'note')
    tp = c.T('picks')
    if c.on(tp):
        packet(c, (340, 820, 740, 980), (780, 640, 900, 720), tp, tp + 0.6, YEL, 'note')
        label(c, 540, 1080, 'whoever holds that caller picks it up', tp + 0.4, YEL, INK, 30)


def pubsub(c):
    sa = node(c, 230, 520, 240, 150, 'Server A', 0.2, 'server', size=30)
    sb = node(c, 850, 520, 240, 150, 'Server B', 0.3, 'server', size=30)
    sc = node(c, 540, 1120, 240, 150, 'Server C', 0.4, 'server', size=30)
    tr = c.T('Redis')
    hub = node(c, 540, 800, 340, 140, 'pub/sub', c.T('pub'), fill=YEL, sub='Redis · Kafka · NATS', size=40)
    tp = c.T('publishes')
    link(c, sa, hub, tp, txt_="publish 'user:bob'")
    packet(c, sa, hub, tp + 0.4, tp + 1.0, PINK, r=16)
    tsb = c.T('subscribed')
    link(c, hub, sb, tsb, dash=True)
    link(c, hub, sc, tsb + 0.2, dash=True)
    packet(c, hub, sb, tsb + 0.6, tsb + 1.2, PINK, r=16)
    td = c.T('down')
    if c.on(td):
        person(c.pen, 1000, 760, 0.7, CYAN)
        arrow(c.pen, 900, 600, 980, 640, c.P(td, 0.3), INK, 5, 18)


def ops(c):
    title(c, 'KEEP SERVERS DUMB', 330, c.T('dumb'), 96, hlcol=YEL)
    rows(c, 100, 500, [(c.T('balancers'), 'Load balancer', 'supports Upgrade + long idle timeouts', 'ok'),
                       (c.T('limited'), 'Each server: limited connections', 'memory + file descriptors', None),
                       (c.T('add'), 'Scale out', 'add servers; state lives in pub/sub', 'ok')], gap=160, h=130)
    td = c.T('deploys')
    if c.on(td): stamp(c.cv, 540, 1010, 'HIDDEN COST: DEPLOYS', 60, c.P(td, 0.35), -3, RED); c.sfx(td, 'thud')
    tdr = c.T('Drain')
    if c.on(tdr): label(c, 540, 1150, 'drain slowly · clients reconnect with jitter (E10)', tdr, YEL, INK, 28)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"Sticky sessions solve this."', c.T('Sticky'), 'intx', 50, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 600, 'NO', 90, c.P(tn, 0.35), -4, RED); c.sfx(tn, 'thud')
    rows(c, 100, 780, [(c.T('reconnects'), 'Sticky = same server on reconnect', 'useful, but only that', None),
                       (c.T('deliver'), "Doesn't move Alice's message", 'to Bob on another server', 'no'),
                       (c.T('still'), 'You still need pub/sub', 'or a shared message bus', 'ok')], gap=160, h=130)


SCENES = [
    (hook, "One WebSocket in your DevTools looks cheap. But each one is a live connection, held on one specific server, sometimes for hours. Now picture a million of them."),
    (stateful, "HTTP servers are stateless: any server can answer any request. Sockets are stateful. Alice is connected to server A. Bob is connected to server B. Alice sends Bob a message. Server A doesn't have Bob."),
    (callcentre, "It's a call centre. Each operator holds their own callers. To reach someone on another operator's line, you drop a note in the mail room, and whoever holds that caller picks it up."),
    (pubsub, "That mail room is a pub sub layer, like Redis or Kafka. Server A publishes to Bob's channel. Every server subscribed to it, including B, receives it, and pushes it down Bob's socket."),
    (ops, "Keep the socket servers dumb. Load balancers must support the upgrade, and long idle timeouts. Each server holds a limited number of connections, so you add servers, and keep state in the pub sub layer. The hidden cost is deploys. Restarting a server drops every socket on it. Drain slowly, and let clients reconnect with jitter."),
    (trap, "Interview trap: sticky sessions solve this, right? No. Stickiness makes reconnects land on the same server. It doesn't deliver Alice's message to Bob on another server. You still need pub sub."),
    (scene_next('S6 · E14', 'PRESENCE', 'online, typing, last seen', 'presence', 'typing'),
     "Next: presence. Online, typing, and last seen. Comment NOTES for the cheat sheet."),
]
