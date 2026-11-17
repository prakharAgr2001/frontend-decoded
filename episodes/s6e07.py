from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E07', tag='S6 · E07', short='THE SHOWDOWN')

TOOLS = [('Polling', YEL), ('Long poll', ORANGE), ('SSE', GRN), ('WebSocket', BLUE), ('WebRTC', PURPLE)]


def intro(c):
    stamp(c.cv, 540, 360, 'THE SHOWDOWN', 96, c.P(0.1, 0.4), -4, RED); c.sfx(0.1, 'thud')
    tf = c.T('Five')
    for k, (nm, col) in enumerate(TOOLS):
        t = tf + k * 0.2
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        y = 540 + k * 115
        card(c.pen, 260, y - 45 * s, 820, y + 45 * s, 20, col, 8, 4)
        c.pen.text(540, y, nm, 'intx', 40 * s, WHITE if col in (BLUE, PURPLE, GRN) else INK)
    tq = c.T('four')
    if c.on(tq): label(c, 540, 1200, 'decide in 4 questions', tq, WHITE, INK, 36)


def q(c, num, question, kw_q, answer, kw_a, col, examples, kw_e):
    pill(c.pen, 540, 330, f'QUESTION {num}', c.B(0.0, 0.35), INK, WHITE, 30, outline=None)
    for i, ln in enumerate(wrap(c.pen, question, 'intx', 54, 880)):
        txt(c, 540, 440 + i * 72, ln, c.T(kw_q) + i * 0.1, 'intx', 54, INK)
    te = c.T(kw_e)
    for k, ex in enumerate(examples):
        t = te + k * 0.5
        if c.on(t): pill(c.pen, 540, 700 + k * 90, ex, c.B(t, 0.35), WHITE, INK, 32); c.sfx(t, 'pop')
    ta = c.T(kw_a)
    if c.on(ta):
        s = c.B(ta, 0.45); c.sfx(ta, 'ding')
        card(c.pen, 540 - 340 * s, 1060 - 80 * s, 540 + 340 * s, 1060 + 80 * s, 26, col, 12, 5)
        c.pen.text(540, 1060, answer, 'osw', 84 * s, WHITE if col in (BLUE, PURPLE, GRN) else INK)


def q1(c):
    q(c, 1, 'Is it audio, video, or browser-to-browser data?', 'audio', 'WEBRTC', 'WebRTC', PURPLE, ['video calls', 'screen share', 'file drop'], 'calls')


def q2(c):
    q(c, 2, 'Does the client send often, with low latency?', 'client', 'WEBSOCKETS', 'WebSockets', BLUE, ['chat', 'multiplayer games', 'live cursors'], 'Chat')


def q3(c):
    q(c, 3, 'Is the server pushing, and the client mostly listening?', 'server', 'SSE', 'sent', GRN, ['live scores', 'notifications', 'AI answers'], 'scores')


def q4(c):
    q(c, 4, 'Are updates rare, or is a few seconds of delay fine?', 'updates', 'POLLING', 'Polling', YEL, ['dashboards', 'build status', 'unread count'], 'Dashboards')


COLS = ['', 'SSE', 'WS', 'Poll']
ROWSD = [('Direction', ['server → you', 'both ways', 'you ask'], 'way'),
         ('Reconnect', ['built in', 'DIY', 'n/a'], 'free'),
         ('Binary', ['no', 'yes', 'yes'], 'binary'),
         ('Plain HTTP', ['yes', 'upgrade', 'yes'], 'HTTP'),
         ('Waste', ['low', 'low', 'high'], 'wasteful')]


def table(c):
    title(c, 'SIDE BY SIDE', 330, 0.1, 96, hlcol=YEL)
    dy = (1 - c.P(0.2, 0.45)) * 900
    card(c.pen, 50, 430 + dy, 1030, 1220 + dy, 24, WHITE, 12, 5)
    xs = [80, 420, 640, 860]
    for k, h in enumerate(COLS):
        c.pen.text(xs[k] + (0 if k == 0 else 70), 500 + dy, h, 'osw', 46, INK, 'lm' if k == 0 else 'mm')
    c.pen.line([(70, 545 + dy), (1010, 545 + dy)], INK, 4, False)
    for i, (nm, vals, kw) in enumerate(ROWSD):
        t = c.T(kw)
        y = 610 + i * 120 + dy
        if not c.on(t): continue
        c.sfx(t, 'pop'); p = c.P(t, 0.3)
        c.pen.text(80, y, nm, 'intx', 32, mix(WHITE, INK, p), 'lm')
        for k, v in enumerate(vals):
            good = v in ('built in', 'yes', 'low', 'both ways')
            bad = v in ('DIY', 'no', 'high')
            col = GRN if good else RED if bad else INK
            c.pen.text(xs[k + 1] + 70, y, v, 'ints', 30, mix(WHITE, col, p))
        if i < len(ROWSD) - 1: c.pen.line([(70, y + 60), (1010, y + 60)], LIGHT, 2, False)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 480, '"Chat needs WebSockets."', c.T('Chat'), 'intx', 50, INK)
    tn = c.T('necessarily')
    if c.on(tn): stamp(c.cv, 540, 610, 'NOT NECESSARILY', 64, c.P(tn, 0.35), -4, RED); c.sfx(tn, 'thud')
    a = node(c, 200, 880, 220, 160, 'Browser', c.T('Receive'), 'laptop')
    b = node(c, 880, 880, 220, 160, 'Server', c.T('Receive') + 0.2, 'server')
    tr = c.T('Receive')
    if c.on(tr + 0.3):
        arrow(c.pen, 760, 830, 320, 830, c.P(tr + 0.3, 0.4), GRN, 7)
        pill(c.pen, 540, 830, 'SSE stream', c.B(tr + 0.5, 0.3), (200, 240, 200), INK, 28)
    ts = c.T('send')
    if c.on(ts):
        arrow(c.pen, 320, 930, 760, 930, c.P(ts, 0.4), INK, 7)
        pill(c.pen, 540, 930, 'POST /messages', c.B(ts + 0.2, 0.3), WHITE, INK, 28)
    tj = c.T('just')
    if c.on(tj): label(c, 540, 1120, 'just HTTP: caching, auth, load balancing', tj, YEL, INK, 32)


SCENES = [
    (intro, "Five tools, and one question in every system design interview: which one do you pick? Here's the decision, in four questions."),
    (q1, "First. Is it audio, video, or data straight between browsers? Video calls, screen sharing, file drops. That's WebRTC. Nothing else is built for it."),
    (q2, "Second. Does the client send often, with low latency? Chat, multiplayer games, live cursors. WebSockets."),
    (q3, "Third. Is the server pushing, and the client mostly listening? Live scores, notifications, AI answers. Server sent events: plain HTTP, with reconnect for free."),
    (q4, "Fourth. Are updates rare, or is a few seconds of delay fine? Dashboards, build status, an unread count. Polling. Long polling, if you need it faster, but can't hold streams open."),
    (table, "Side by side. SSE is one way, and reconnects for free. WebSockets go both ways, carry binary, but reconnect is your job. And they leave plain HTTP after the upgrade. Polling is the most compatible, and the most wasteful."),
    (trap, "Interview trap: chat needs WebSockets, right? Not necessarily. Receive over server sent events, and send with a normal POST. It's a valid design, and it's just HTTP, so caching, auth, and load balancing all work as usual."),
    (scene_next('S6 · E08', 'INTERVIEW QUESTIONS', 'transports, under pressure', 'interview', 'pressure'),
     "Next: interview questions on everything so far, under pressure. Comment NOTES for the cheat sheet."),
]
