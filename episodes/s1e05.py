from engine.lib import *

EP = dict(id='S1E05', tag='S1 · E05', short='HTTP 1 · 2 · 3')

def hook(c):
    box = panel(c, 70, 320, 1010, 900, tabs=('Network',), dy=(1 - c.P(0, 0.45)) * 900)
    c.pen.text(110, 460, 'Name', 'mono', 26, (140, 146, 156), 'lm'); c.pen.text(780, 460, 'Protocol', 'mono', 26, (140, 146, 156), 'lm')
    tp = c.T('Protocol')
    for i, (n, pr) in enumerate([('videoplayback?id=…', 'h3'), ('player.js', 'h3'), ('thumbnail.webp', 'h3'), ('stats?ev=…', 'h2')]):
        y = 540 + i * 80
        c.pen.text(110, y, n, 'mono', 30, WHITE, 'lm')
        if c.on(tp): c.pen.text(780, y, pr, 'monob', 32, (120, 220, 150) if pr == 'h3' else CYAN, 'lm')
    if c.on(tp): hl(c.pen, 760, 505, 900, 515, 0, YEL); c.pen.rr(760, 500, 900, 820, 12, outline=YEL, w=5)
    t3 = c.T('three')
    bignum(c, 540, 1080, 'HTTP/3', t3, 150, INK)
    tw = c.T('wrong')
    if c.on(tw): txt(c, 540, 1220, 'so what was wrong with 1 and 2?', tw, 'int', 38, RED)

def road(c, y, lanes, cars, t0, blocked=None, label_=None):
    for l in range(lanes):
        yy = y + l * 70
        c.pen.rect(110, yy - 28, 970, yy + 28, fill=(70, 74, 82))
        for k in range(10): c.pen.rect(130 + k * 90, yy - 3, 170 + k * 90, yy + 3, fill=(200, 200, 200))
    for (lane, start, speed, col, txt_) in cars:
        if c.t < t0: continue
        x = 140 + (c.t - t0) * speed * 100 + start
        if blocked is not None and lane == blocked[0]: x = min(x, blocked[1] - start * 0)
        x = min(x, 900)
        yy = y + lane * 70
        c.pen.rr(x - 44, yy - 22, x + 44, yy + 22, 10, fill=col, outline=INK, w=3)
        if txt_: c.pen.text(x, yy, txt_, 'int', 20, INK)

def h1(c):
    title(c, 'HTTP/1.1', 330, 0.1, 110, hlcol=YEL)
    th = c.T('one', 2)
    c.pen.text(110, 460, '1 connection = 1 request at a time', 'int', 34, INK, 'lm')
    t0 = c.T('connection')
    if c.on(t0):
        for k, (col, nm, sp) in enumerate([(RED, 'big.js', 0.6), (YEL, 'a.css', 2), (YEL, 'b.png', 2), (YEL, 'c.js', 2)]):
            x = min(860 - k * 100, 160 + (c.t - t0) * sp * 120) if k == 0 else min(760 - (k - 1) * 100, 160 + (c.t - t0) * 300)
            if k == 0: x = min(860, 200 + (c.t - t0) * 40)
            c.pen.rect(110, 540, 970, 620, fill=(70, 74, 82))
        cars = [('big.js', RED), ('a.css', YEL), ('b.png', YEL), ('c.js', YEL)]
        lead = 200 + (c.t - t0) * 45
        for k, (nm, col) in enumerate(cars):
            x = lead - k * 110
            if x < 120: continue
            c.pen.rr(x - 50, 556, x + 50, 604, 10, fill=col, outline=INK, w=3); c.pen.text(x, 580, nm, 'int', 20, INK)
    ts = c.T('slow')
    if c.on(ts): txt(c, 540, 680, 'one slow file blocks the queue', ts, 'int', 34, RED)
    t6 = c.T('six')
    if c.on(t6):
        for l in range(6):
            yy = 800 + l * 70; p = c.P(t6 + l * 0.08, 0.3)
            c.pen.rect(110, yy - 28, 110 + 860 * p, yy + 28, fill=(70, 74, 82))
            x = 160 + ((c.t - t6) * (180 + l * 30)) % 760
            if p >= 1: c.pen.rr(x - 40, yy - 20, x + 40, yy + 20, 10, fill=YEL, outline=INK, w=3)
        txt(c, 540, 1250, 'workaround: ~6 connections per site', t6, 'intx', 40, INK)

def h2(c):
    title(c, 'HTTP/2: MULTIPLEXING', 330, 0.1, 96, hlcol=YEL)
    c.pen.rr(110, 560, 970, 760, 100, fill=(70, 74, 82), outline=INK, w=5)
    c.pen.text(540, 520, 'ONE connection', 'int', 34, MUTE)
    tm = c.T('multiplexing')
    cols = [YEL, CYAN, PINK, (160, 220, 130)]
    if c.on(tm):
        for k in range(14):
            q = ((c.t - tm) * 0.35 + k / 14) % 1.0
            x = 150 + q * 780
            c.pen.rr(x - 26, 630, x + 26, 690, 8, fill=cols[k % 4], outline=INK, w=3)
        for i, (nm, col) in enumerate(zip(['page.html', 'app.js', 'style.css', 'logo.png'], cols)):
            pill(c.pen, 200 + i * 230, 860, nm, c.B(tm + i * 0.1, 0.3), col, INK, 24)
        txt(c, 540, 960, 'many requests, sliced into frames, at the same time', tm + 0.4, 'int', 34, INK)
    th = c.T('Headers')
    if c.on(th): label(c, 540, 1100, 'headers compressed (HPACK)', th, WHITE, INK, 32)

def holb(c):
    title(c, 'BUT IT STILL RUNS ON TCP', 330, 0.1, 86)
    c.pen.rr(110, 560, 970, 760, 100, fill=(70, 74, 82), outline=INK, w=5)
    tl = c.T('Lose')
    cols = [YEL, CYAN, PINK, (160, 220, 130)]
    stop = c.T('pauses')
    for k in range(10):
        q = (min(c.t, stop) * 0.35 + k / 10) % 1.0
        x = 150 + q * 780
        lost = k == 4 and c.on(tl)
        c.pen.rr(x - 26, 630, x + 26, 690, 8, fill=RED if lost else (mix(cols[k % 4], GREY, 0.6) if c.on(stop) else cols[k % 4]), outline=INK, w=3)
        if lost: cross(c.pen, x, 590, 0.8, RED, 8, c.P(tl, 0.3))
    if c.on(stop): c.sfx(stop, 'buzz'); stamp(c.cv, 540, 900, 'EVERY STREAM WAITS', 62, c.P(stop, 0.4), -3, RED)
    tj = c.T('jam')
    if c.on(tj): txt(c, 540, 1080, 'head-of-line blocking, one layer down', tj, 'int', 36, INK)

def h3(c):
    title(c, 'HTTP/3 = QUIC over UDP', 330, 0.1, 90, hlcol=YEL)
    ti = c.T('independent')
    cols = [YEL, CYAN, PINK, (160, 220, 130)]
    tlost = c.T('lost')
    for l in range(4):
        yy = 520 + l * 95
        c.pen.rect(110, yy - 34, 970, yy + 34, fill=(70, 74, 82))
        for k in range(3):
            q = (c.t * 0.3 + k / 3 + l * 0.11) % 1.0
            if l == 1 and c.on(tlost): q = (tlost * 0.3 + k / 3 + l * 0.11) % 1.0
            x = 150 + q * 780
            c.pen.rr(x - 26, yy - 24, x + 26, yy + 24, 8, fill=RED if (l == 1 and k == 0 and c.on(tlost)) else cols[l], outline=INK, w=3)
    if c.on(ti): label(c, 540, 930, 'streams are independent', ti, WHITE, INK, 32)
    if c.on(tlost): txt(c, 540, 1000, 'a lost packet only delays its own stream', tlost, 'int', 34, INK)
    tw = c.T('Wi-Fi')
    if c.on(tw):
        c.sfx(tw, 'pop'); s = c.B(tw, 0.4)
        icon(c.pen, 'phone', 300, 1180, 1.0 * s)
        pill(c.pen, 520, 1150, 'Wi-Fi', s, WHITE, INK, 26); pill(c.pen, 760, 1150, '4G', s, YEL, INK, 26)
        arrow(c.pen, 590, 1150, 700, 1150, c.P(tw + 0.3, 0.3), INK, 5, 18)
        txt(c, 640, 1230, 'no reconnect needed', tw + 0.5, 'int', 30, GRN)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 480, 'Is HTTP/2 always faster?', c.T('always'), 'intx', 52, INK)
    tn = c.T('Not')
    if c.on(tn): stamp(c.cv, 540, 610, 'NOT ALWAYS', 70, c.P(tn, 0.4), 3, BLUE)
    tl = c.T('lossy')
    if c.on(tl):
        node(c, 290, 900, 360, 240, '1 connection', tl, 'server', sub='HTTP/2: one loss stalls all')
        node(c, 790, 900, 360, 240, '6 connections', tl + 0.4, 'server', sub='HTTP/1.1: loss hits one')
        cross(c.pen, 290, 1060, 1.0, RED, 9, c.P(tl + 0.8, 0.3))

SCENES = [
    (hook, "Open YouTube, turn on the Protocol column in DevTools, and you'll likely see h3. That's HTTP three. So what was wrong with one and two?"),
    (h1, "With HTTP one point one, each connection handles one request at a time. A slow file blocks everything queued behind it. So browsers cheat, and open about six connections per site."),
    (h2, "HTTP two fixed that with multiplexing. Many requests share one connection at the same time, sliced into small frames. Headers get compressed too."),
    (holb, "But it still runs on TCP. Lose a single packet, and TCP pauses every stream until it's resent. The traffic jam just moved one layer down."),
    (h3, "HTTP three switches to QUIC, built on UDP. Streams are independent, so a lost packet only delays its own stream. And your connection can survive switching from Wi-Fi to mobile data."),
    (gotcha, "Interview question: is HTTP two always faster? Not always. On a very lossy network, one shared TCP connection can stall harder than six separate ones."),
    (scene_try([('Network', 'Network tab', 'right-click a column header'), ('Protocol', 'Enable “Protocol”', 'see http/1.1, h2, h3'),
                ('compare', 'Compare sites', 'YouTube vs an old blog')], 'Try'),
     "Try it. In the Network tab, enable the Protocol column, and compare a few sites."),
    (scene_next('S1 · E06', 'CDNs', 'how millions stream the same match', 'CDNs', 'match'),
     "Next: CDNs, and how millions of fans stream the same match at once. Comment NOTES for the cheat sheet."),
]
