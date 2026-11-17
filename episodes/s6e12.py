from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E12', tag='S6 · E12', short='ACKS & DEDUP')


def hook(c):
    title(c, 'THE TICKS', 330, 0.1, 100, hlcol=YEL)
    for k, (kw, n, col, s_) in enumerate((('One', 1, MUTE, 'the server got it'), ('Two', 2, MUTE, 'on their phone'), ('blue', 2, BLUE, 'read'))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 520 + k * 200
        bubble(c, 140, 640, y, 'See you at 8', t, mine=True, n_ticks=n, tick_col=col)
        txt(c, 680, y, s_, t + 0.2, 'ints', 32, INK, 'lm')
    ta = c.T('acknowledgement')
    if c.on(ta): label(c, 540, 1160, 'each tick = an ack coming back', ta, YEL, INK, 34)


def optimistic(c):
    tc = c.T('clock')
    x0, y0, x1, y1 = phone(c, 540, 720, 560, 760, dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    acked = c.on(c.T('tick'))
    bubble(c, x1 - 380, x1 - 30, y0 + 160, 'On my way!', c.T('instantly'), mine=True, n_ticks=1 if acked else 0)
    if c.on(tc) and not acked: icon(c.pen, 'clock', x1 - 80, y0 + 170, 0.28)
    chapter(c, 540, 1180, 'S4 · E15', 'optimistic UI', c.T('optimistic'))
    if acked: c.sfx(c.T('tick'), 'tick')


def lost(c):
    lanes(c, 230, 850, 360, 1300, 0.1, 'You', 'Server', 'phone', 'server')
    msg(c, 230, 850, 560, c.T('reached'), 'msg: On my way')
    tc = c.T('died')
    msg(c, 230, 850, 680, tc, 'ack', right=False, col=MUTE, dash=True)
    if c.on(tc + 0.5): cross(c.pen, 400, 720, 1.0, RED, 9, c.P(tc + 0.5, 0.3)); c.sfx(tc + 0.5, 'buzz')
    tr = c.T('retries')
    msg(c, 230, 850, 860, tr, 'msg: On my way (again)', col=ORANGE)
    tw = c.T('twice')
    if c.on(tw):
        bubble(c, 300, 780, 1080, 'On my way', tw, mine=False)
        bubble(c, 300, 780, 1190, 'On my way', tw + 0.3, mine=False)
        stamp(c.cv, 880, 1135, 'TWICE', 52, c.P(tw + 0.4, 0.35), 8, RED)


def laundry(c):
    title(c, 'THE LAUNDRY SLIP', 330, c.T('laundry'), 100, hlcol=YEL)
    ts = c.T('slip')
    if c.on(ts):
        s = c.B(ts, 0.4)
        card(c.pen, 380 - 140 * s, 560 - 90 * s, 380 + 140 * s, 560 + 90 * s, 12, (255, 246, 214), 8, 4)
        c.pen.text(380, 530, 'SLIP', 'osw', 34 * s, INK)
        c.pen.text(380, 590, '#4417', 'monob', 44 * s, RED)
    tt = c.T('twice')
    if c.on(tt):
        for k in range(2):
            if c.on(tt + k * 0.4): pill(c.pen, 760, 500 + k * 90, 'hand in #4417', c.B(tt + k * 0.4, 0.3), WHITE, INK, 30)
    to = c.T('shirt')
    if c.on(to):
        x, y, s = 540, 880, c.B(to, 0.4)
        c.pen.poly([(x - 90 * s, y - 80 * s), (x - 30 * s, y - 100 * s), (x + 30 * s, y - 100 * s), (x + 90 * s, y - 80 * s), (x + 130 * s, y - 20 * s),
                    (x + 80 * s, y), (x + 70 * s, y + 110 * s), (x - 70 * s, y + 110 * s), (x - 80 * s, y), (x - 130 * s, y - 20 * s)], fill=CYAN, outline=INK, w=5)
        txt(c, 540, 1050, 'one shirt', to, 'intx', 42, INK)
    tn = c.T('safe')
    if c.on(tn): label(c, 540, 1170, 'the number makes the retry safe', tn, YEL, INK, 34)


def code_(c):
    at = c.T('id', 1)
    code(c, 40, 340, 1040, 980, ['const msg = { id: crypto.randomUUID(), text };', 'outbox.set(msg.id, msg);', "render({ ...msg, status: 'pending' });", 'send(msg);',
                                 '// later, from the server:', 'onAck = ({ id, seq }) => {', '  outbox.delete(id);', "  update(id, { status: 'sent', seq });", '};'],
         at, 0.08, 27, 'send.js', marks=[(0, c.T('UUID'), YEL), (3, c.T('Retries'), YEL), (6, c.T('ack'), YEL)])
    ts = c.T('drops')
    if c.on(ts): label(c, 540, 1080, 'server: seen this id? drop it', ts, WHITE, INK, 32)
    te = c.T('echo')
    if c.on(te): label(c, 540, 1190, 'client: own echo? merge, never add', te, WHITE, INK, 32)


def guarantee(c):
    title(c, 'THE REAL GUARANTEE', 330, 0.1, 90, hlcol=YEL)
    rows(c, 100, 520, [(c.T('least'), 'At-least-once delivery', 'retry until acked', 'ok'), (c.T('dedup'), '+ dedup by id', 'drop repeats on both ends', 'ok')], gap=160, h=130)
    tf = c.T('feels')
    if c.on(tf): txt(c, 540, 860, '= feels like exactly once', tf, 'intx', 46, GRN)
    tx = c.T('network')
    if c.on(tx): stamp(c.cv, 540, 1020, 'TRUE EXACTLY-ONCE? NO', 56, c.P(tx, 0.35), -3, RED); c.sfx(tx, 'thud')


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Who generates the id?', c.T('generate'), 'intx', 54, INK)
    tc = c.T('Client', 2)
    if c.on(tc): stamp(c.cv, 540, 610, 'THE CLIENT', 80, c.P(tc, 0.35), -4, GRN); c.sfx(tc, 'thud')
    rows(c, 100, 800, [(c.T('exist'), 'Server id', "doesn't exist until attempt 1 succeeds", 'no'),
                       (c.T('protect'), 'Client id', 'exists before the first send', 'ok')], gap=160, h=130)


SCENES = [
    (hook, "Look at the ticks under a WhatsApp message. One grey tick: the server got it. Two grey ticks: it reached your friend's phone. Two blue ticks: read. Each tick is an acknowledgement, coming back."),
    (optimistic, "Your message appears instantly, with a little clock, before the server confirms anything. That's optimistic UI, from season four, episode fifteen. When the ack arrives, the clock becomes a tick."),
    (lost, "But what if the ack gets lost? Your message reached the server, and then the connection died before the ack came back. So the app retries, and your friend gets the message twice."),
    (laundry, "Think of a laundry slip. Hand in the same numbered slip twice, and you still get one shirt back. The number makes the retry safe."),
    (code_, "So the client gives every message a unique id before sending, a UUID. Retries reuse it. The server remembers ids it has seen, and drops repeats. When the ack comes back, the outbox entry is cleared, and the client also ignores its own echo."),
    (guarantee, "That's the real guarantee: at least once delivery, plus dedup, which feels like exactly once. True exactly once, across an unreliable network, isn't something you get for free."),
    (trap, "Interview trap: who should generate the id, client or server? Client. A server id doesn't exist until the first attempt succeeds, so it can't protect the retry. A client id exists before the very first send."),
    (scene_next('S6 · E13', 'SCALING WEBSOCKETS', 'a million open connections', 'scaling', 'million'),
     "Next: scaling WebSockets to a million open connections. Comment NOTES for the cheat sheet."),
]
