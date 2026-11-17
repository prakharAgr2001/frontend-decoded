from engine.lib import *

EP = dict(id='S1E03', tag='S1 · E03', short='TCP HANDSHAKE')

def lanes(c, labels=('YOUR DEVICE', 'SERVER'), top=420, bottom=1240):
    for x, lab, ic in ((230, labels[0], 'laptop'), (850, labels[1], 'server')):
        icon(c.pen, ic, x, top - 70, 0.9)
        c.pen.text(x, top + 10, lab, 'int', 30, INK)
        c.pen.line([(x, top + 40), (x, bottom)], GREY, 5, False)

def msg(c, y0, left_to_right, text, at, col=YEL, dy=110):
    if not c.on(at): return
    c.sfx(at, 'swish')
    x0, x1 = (230, 850) if left_to_right else (850, 230)
    p = c.P(at, 0.55)
    arrow(c.pen, x0, y0, x1, y0 + dy, p, INK, 6, 24)
    if p > 0.5:
        s = c.B(at + 0.25, 0.3)
        w = c.pen.tw(text, 'osw', 50 * s) + 40
        mx, my = (x0 + x1) / 2, y0 + dy / 2 - 40
        c.pen.rr(mx - w / 2, my - 34 * s, mx + w / 2, my + 34 * s, 16, fill=col, outline=INK, w=4)
        c.pen.text(mx, my, text, 'osw', 50 * s, INK)

def hook(c):
    title(c, 'BEFORE THE FIRST BYTE…', 520, 0.2, 92)
    tp = c.T('phone')
    if c.on(tp):
        c.sfx(tp, 'thud'); s = c.B(tp, 0.45)
        card(c.pen, 540 - 150 * s, 820 - 210 * s, 540 + 150 * s, 820 + 210 * s, 40, WHITE, 12, 6)
        icon(c.pen, 'phone', 540, 800, 2.6 * s)
        for k in range(3):
            r = 200 + k * 50 + (c.t * 120 % 50)
            c.pen.arc(540 - r, 800 - r, 540 + r, 800 + r, -40, 40, mix(PAPER, INK, 0.6 - k * 0.15), 6)

def analogy(c):
    lanes(c, ('YOU', 'FRIEND'))
    msg(c, 520, True, '“Hello, can you hear me?”', c.T('Hello'), WHITE, 120)
    msg(c, 700, False, '“Yes! Can you hear me?”', c.T('Yes'), WHITE, 120)
    msg(c, 880, True, '“Yes.”', c.T('Yes', 2), WHITE, 120)
    tr = c.T('real')
    if c.on(tr): label(c, 540, 1150, 'now the real conversation starts', tr, GRN, WHITE, 32)

def handshake(c):
    lanes(c)
    msg(c, 500, True, 'SYN', c.T('SYN'))
    msg(c, 680, False, 'SYN-ACK', c.T('replies'))
    msg(c, 860, True, 'ACK', c.T('answers'))
    tk = c.T('know')
    if c.on(tk):
        check(c.pen, 230, 1080, 1.3, GRN, 12, c.P(tk, 0.4)); check(c.pen, 850, 1080, 1.3, GRN, 12, c.P(tk + 0.2, 0.4))
        txt(c, 540, 1180, 'both sides agree where byte #1 starts', c.T('counting'), 'int', 34, INK)

def cost(c):
    title(c, 'THE COST: 1 ROUND TRIP', 340, 0.1, 86)
    node(c, 230, 700, 260, 210, 'Bangalore', c.T('Bangalore'), 'laptop')
    node(c, 850, 700, 260, 210, 'US server', c.T('US'), 'server')
    tb = c.T('Bangalore')
    for k in range(2):
        t0 = tb + 0.6 + k * 1.1
        if c.on(t0):
            q = lin(c.t, t0, t0 + 1.0)
            x = 380 + 320 * (q * 2 if q < 0.5 else 2 - q * 2)
            c.pen.circ(x, 700, 18, fill=YEL, outline=INK, w=4)
    tm = c.T('two')
    counter(c, 540, 1010, 0, 200, tm, tm + 1.0, '{:.0f}', 150, RED, ' ms')
    txt(c, 540, 1140, '…just to say hello', c.T('hello'), 'int', 40, INK)

def keepalive(c):
    title(c, 'KEEP-ALIVE', 340, c.T('keep'), 120, hlcol=YEL)
    y = 720
    c.pen.rr(140, y - 70, 940, y + 70, 70, fill=WHITE, outline=INK, w=6)
    c.pen.text(540, y - 110, 'one open connection', 'int', 32, MUTE)
    tf, tn = c.T('first'), c.T('next')
    hs = c.P(tf, 0.5)
    if c.on(tf):
        c.pen.rr(160, y - 50, 160 + 160 * hs, y + 50, 50, fill=ORANGE, outline=INK, w=3)
        c.pen.text(240, y, 'handshake', 'int', 26 * hs, INK)
    for k in range(5):
        at = tn + k * 0.35
        if not c.on(at): continue
        c.sfx(at, 'tick')
        q = lin(c.t, at, at + 1.6)
        x = 340 + 560 * q
        if q < 1: c.pen.rr(x - 40, y - 30, x + 40, y + 30, 14, fill=YEL, outline=INK, w=3); c.pen.text(x, y, 'GET', 'monob', 22, INK)
    txt(c, 540, 930, 'request 2, 3, 4… skip the handshake', tn, 'int', 38, GRN)

def proof(c):
    box = panel(c, 70, 330, 1010, 1060, tabs=('Network', 'Timing'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    rows = [('1st request · Initial connection', 300, ORANGE, c.T('first')), ('later request · Initial connection', 0, ORANGE, c.T('Later'))]
    for j, (lab, w, col, at) in enumerate(rows):
        if not c.on(at): continue
        c.sfx(at, 'tick'); y = 520 + j * 220
        c.pen.text(110, y - 40, lab, 'mono', 28, WHITE, 'lm')
        c.pen.rect(110, y, 110 + max(4, w * c.P(at, 0.5)), y + 48, fill=col)
        c.pen.text(140 + max(4, w), y + 24, '182 ms' if w else '0 ms  (reused)', 'monob', 30, WHITE, 'lm')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 500, 'TCP guarantees order + delivery', c.T('guarantees'), 'intx', 46, INK)
    tl = c.T('lost')
    for i in range(7):
        x = 150 + i * 130; y = 760
        lost = i == 2
        at = c.T('guarantees') + 0.3 + i * 0.12
        if not c.on(at): continue
        s = c.B(at, 0.3)
        col = RED if (lost and c.on(tl)) else YEL
        wait = c.on(c.T('holds')) and i > 2
        c.pen.rr(x - 50 * s, y - 50 * s, x + 50 * s, y + 50 * s, 12, fill=mix(col, GREY, 0.6) if wait else col, outline=INK, w=4)
        c.pen.text(x, y, str(i + 1), 'osw', 50 * s, INK)
        if lost and c.on(tl): cross(c.pen, x, y - 90, 1.0, RED, 9, c.P(tl, 0.3))
    th = c.T('holds')
    if c.on(th):
        c.sfx(th, 'buzz'); txt(c, 700, 880, 'everything behind it waits…', th, 'int', 34, RED)
    t3 = c.T('three')
    if c.on(t3): stamp(c.cv, 540, 1110, 'WHY HTTP/3 EXISTS', 64, c.P(t3, 0.4), -3, BLUE)

SCENES = [
    (hook, "Before your browser can send a single byte of your request, it has to make a phone call."),
    (analogy, "Hello, can you hear me? Yes, I can hear you. Can you hear me? Yes. Only then does the real conversation start."),
    (handshake, "That's the TCP three-way handshake. Your device sends a SYN. The server replies with a SYN-ACK. Your device answers with an ACK. Now both sides know the line works, and they've agreed where to start counting bytes."),
    (cost, "The catch? It costs a full round trip before any real data moves. Between Bangalore and a server in the US, that's roughly two hundred milliseconds, just to say hello."),
    (keepalive, "That's why browsers keep connections alive and reuse them. The first request pays for the handshake. The next requests on that connection skip it."),
    (proof, "You can see it in DevTools. The first request to a site shows time for the initial connection. Later requests to the same site often show zero, because the connection was reused."),
    (gotcha, "Interview trap: TCP guarantees order and delivery, by resending lost packets. Great, until one lost packet holds up everything behind it. Remember that. It's exactly why HTTP three exists."),
    (scene_next('S1 · E04', 'HTTPS', 'what the padlock really promises', 'HTTPS', 'padlock'),
     "Next: HTTPS, and what the padlock really promises. Comment NOTES for the cheat sheet."),
]
