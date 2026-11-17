from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E11', tag='S6 · E11', short='ORDERING')


def hook(c):
    x0, y0, x1, y1 = phone(c, 540, 760, 560, 900, dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    c.pen.text(540, y0 + 40, 'Trip planning (6)', 'intx', 30, INK)
    tr, tj = c.T('reply'), c.T('jump')
    swapped = c.on(tj)
    q = c.P(tj, 0.5)
    ya, yb = y0 + 260, y0 + 380
    bubble(c, x0 + 30, x1 - 120, y0 + 140, 'Leaving at 7?', 0.5, mine=False, sub='Asha')
    # reply shows up above the question, then jumps below it
    y_reply = ya + (yb - ya) * q if swapped else ya
    y_q = yb + (ya - yb) * q if swapped else yb
    bubble(c, x0 + 30, x1 - 80, y_reply, 'Yes, the blue one', tr, mine=False, sub='Kabir')
    bubble(c, x0 + 30, x1 - 80, y_q, 'Which car do we take?', tr + 0.4, mine=False, sub='Riya')
    if c.on(tr + 0.8) and not swapped:
        c.pen.circ(x1 - 40, ya, 26, fill=RED, outline=INK, w=3); c.pen.text(x1 - 40, ya, '?', 'intx', 32, WHITE)
    to = c.T('ordering')
    if c.on(to): stamp(c.cv, 540, 1290, 'ORDERING BUG', 70, c.P(to, 0.35), -4, RED); c.sfx(to, 'thud')


def paths(c):
    tc = c.T('TCP')
    a = node(c, 200, 520, 220, 150, 'Server', 0.2, 'server')
    b = node(c, 880, 520, 220, 150, 'Browser', 0.3, 'laptop')
    pipe(c, 320, 760, 520, tc, YEL, 46)
    if c.on(tc):
        for k in range(3):
            pill(c.pen, 400 + k * 140, 520, str(k + 1), 1, WHITE, INK, 26)
        txt(c, 540, 640, 'one socket: always in order', tc + 0.4, 'ints', 32, GRN)
    tm = c.T('many')
    if c.on(tm):
        items = [(c.T('two'), 'phone + laptop', 'phone'), (c.T('reconnect'), 'a reconnect', 'globe'), (c.T('HTTP'), 'HTTP + socket', 'doc')]
        for k, (t, s_, ic) in enumerate(items):
            node(c, 200 + k * 340, 900, 300, 190, s_, t, ic, size=28)
    tg = c.T('guaranteed')
    if c.on(tg): label(c, 540, 1110, 'between paths: no order guarantee', tg, (255, 210, 210), INK, 32)


def clocks(c):
    title(c, "DON'T SORT BY THE SENDER'S CLOCK", 330, c.T('clock'), 60, hlcol=YEL)
    for k, (nm, tm, col, kw) in enumerate((('Asha', '10:00:05', BLUE, 'Sorting'), ('Kabir', '10:00:02', ORANGE, 'phone'))):
        t = c.T(kw)
        x = 290 + k * 500
        if c.on(t):
            icon(c.pen, 'clock', x, 560, 1.2 * c.B(t, 0.4))
            c.pen.text(x, 680, nm, 'intx', 36, INK)
            c.pen.text(x, 740, tm, 'monob', 40, col)
    tw = c.T('wrong')
    if c.on(tw):
        txt(c, 540, 900, "Kabir answered after Asha asked…", tw, 'ints', 34, INK)
        txt(c, 540, 960, "…but his clock is 4 s behind", tw + 0.5, 'ints', 34, RED)
    tmn = c.T('minutes')
    if c.on(tmn): stamp(c.cv, 540, 1110, 'CLOCKS LIE', 72, c.P(tmn, 0.35), -4, RED); c.sfx(tmn, 'thud')


def pages(c):
    title(c, 'THE DROPPED EXAM SHEETS', 330, c.T('dropping'), 72, hlcol=YEL)
    ts = c.T('sort')
    order = [3, 1, 4, 2]
    q = c.P(c.T('corner'), 0.8)
    for k, n in enumerate(order):
        x0_ = 150 + k * 200 + 15 * math.sin(k * 2.0)
        x1_ = 150 + (n - 1) * 200
        x = x0_ + (x1_ - x0_) * q
        ang = (1 - q) * (k - 1.5) * 8
        y = 620 + (1 - q) * (k % 2) * 60
        card(c.pen, x, y, x + 170, y + 230, 10, WHITE, 6, 4)
        for j in range(4): c.pen.line([(x + 20, y + 40 + j * 34), (x + 150, y + 40 + j * 34)], LIGHT, 4)
        c.pen.circ(x + 140, y + 200, 22, fill=YEL, outline=INK, w=3)
        c.pen.text(x + 140, y + 200, str(n), 'intx', 26, INK)
    if c.on(ts): txt(c, 540, 960, 'not by when you think you wrote them', ts, 'ints', 32, MUTE)
    tp = c.T('number')
    if c.on(tp): label(c, 540, 1080, 'by the number in the corner', tp, YEL, INK, 34)


def seq(c):
    tt = c.T('stamps')
    for k, n in enumerate((41, 42, 44)):
        t = tt + k * 0.4 if n != 44 else c.T('then')
        if c.on(t):
            pill(c.pen, 220 + k * 320, 420, f'seq {n}', c.B(t, 0.35), WHITE if n != 44 else (255, 210, 210), INK, 34); c.sfx(t, 'pop')
    tm = c.T('missing')
    if c.on(tm):
        pill(c.pen, 700, 520, 'seq 43?', c.B(tm, 0.35), YEL, INK, 30)
    code(c, 40, 600, 1040, 1180, ['function onMsg(m) {', '  if (m.seq <= lastSeq) return; // seen it', '  if (m.seq > lastSeq + 1) {', '    buffer.set(m.seq, m);',
                                  '    return fetchGap(lastSeq + 1, m.seq);', '  }', '  apply(m); lastSeq = m.seq;', '  drainBuffer();', '}'],
         c.T('inserts'), 0.08, 27, 'ordering.js', marks=[(4, c.T('asks'), YEL), (6, c.T('inserts'), YEL)])


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 40, 440, 1040, 680, ['ws.onmessage = async (e) => {', '  const m = await decrypt(e.data);', '  show(m);', '};'], c.T('async'), 0.1, 28, 'bug.js',
         marks=[(1, c.T('awaits'), YEL)])
    chapter(c, 540, 760, 'S1 · E15–16', 'the task queue', c.T('fifteen'))
    tf = c.T('finish')
    if c.on(tf):
        for k, (lab, w, col) in enumerate((('msg 1: decrypt (slow)', 700, ORANGE), ('msg 2: decrypt (fast)', 260, GRN))):
            y = 860 + k * 80
            c.pen.rr(140, y, 140 + w * c.P(tf + k * 0.2, 0.6), y + 56, 12, fill=col, outline=INK, w=3)
            c.pen.text(160, y + 28, lab, 'ints', 26, INK, 'lm')
        if c.on(tf + 0.8): pill(c.pen, 600, 960, 'shown first!', c.B(tf + 0.8, 0.3), (255, 210, 210), INK, 26)
    tq = c.T('Queue')
    if c.on(tq): label(c, 540, 1150, 'fix: queue them, process one at a time', tq, YEL, INK, 32)


SCENES = [
    (hook, "In a busy group chat, have you ever seen a reply show up above the question it answers, then jump into place a second later? That's an ordering bug, being fixed live."),
    (paths, "Within one WebSocket, TCP keeps messages in order. But your users have many paths. Two devices. A reconnect. A message sent over HTTP, while another arrives on the socket. Between paths, order isn't guaranteed."),
    (clocks, "And you can't sort by the sender's clock. Sorting by device time fails, because a phone's clock can be wrong by seconds, sometimes minutes."),
    (pages, "Imagine dropping a stack of exam sheets. You don't sort them by when you think you wrote them. You sort by the page number in the corner."),
    (seq, "So the server stamps each message with a sequence number, per chat. The client inserts by that number. If it gets forty one, forty two, then forty four, it knows forty three is missing, holds forty four, and asks for the gap."),
    (trap, "Interview trap: an async message handler. Each message is its own task, from season one, episodes fifteen and sixteen. But if your handler awaits, say, decryption, message two can finish before message one. Queue messages, and process them one at a time."),
    (scene_next('S6 · E12', 'ACKS & DEDUP', 'what the ticks really mean', 'acks', 'ticks'),
     "Next: acks and dedup, and what those ticks really mean. Comment NOTES for the cheat sheet."),
]
