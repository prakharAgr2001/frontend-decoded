from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E05', tag='S6 · E05', short='WEBSOCKETS')


def hook(c):
    x0, y0, x1, y1 = panel(c, 60, 330, 1020, 1100, tabs=('Network', 'WS'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tf = c.T('filter')
    netrows(c, x0 + 40, y0 + 70, x1, [(tf, '?v=2.3000.x', ['101', 'Pending'], YEL)], cols=[x0 + 520, x0 + 680])
    tst = c.T('status')
    if c.on(tst): c.pen.circ(x0 + 545, y0 + 70, 44, outline=RED, w=6); c.sfx(tst, 'swish')
    tsw = c.T('switching')
    kv(c, x0 + 40, y0 + 220, x1, [(tsw, 'Status Code:', '101 Switching Protocols', YEL), (tsw + 0.5, 'Upgrade:', 'websocket', WHITE),
                                  (tsw + 0.9, 'Connection:', 'Upgrade', WHITE)], 30, 66)
    tb = c.T('born')
    if c.on(tb): stamp(c.cv, 540, 1220, 'A WEBSOCKET IS BORN', 66, c.P(tb, 0.35), -4, RED); c.sfx(tb, 'thud')


def upgrade(c):
    lanes(c, 230, 850, 360, 1300, 0.1)
    msg(c, 230, 850, 560, c.T('ordinary'), 'GET /chat')
    tu = c.T('upgrade')
    if c.on(tu): pill(c.pen, 540, 650, 'Upgrade: websocket', c.B(tu, 0.35), YEL, INK, 30); c.sfx(tu, 'pop')
    msg(c, 230, 850, 760, c.T('agrees'), '101 Switching', right=False, col=GRN)
    tt = c.T('stops')
    if c.on(tt): txt(c, 540, 900, 'no more HTTP on this connection', tt, 'ints', 30, MUTE)
    tf = c.T('frames')
    pipe(c, 250, 830, 1030, tf, YEL, 52)
    blips(c, 250, 830, 1030, tf + 0.3, 99, 0.9, right=True, col=WHITE, r=14, speed=0.7)
    blips(c, 250, 830, 1030, tf + 0.6, 99, 1.1, right=False, col=BLUE, r=14, speed=0.7)
    tw = c.T('ways')
    if c.on(tw): label(c, 540, 1140, 'frames, both ways', tw, WHITE, INK, 32)


def call(c):
    tr = c.T('Remember')
    chapter(c, 540, 350, 'S1 · E03', 'TCP: the phone call', tr)
    for x, col in ((230, BLUE), (850, ORANGE)):
        person(c.pen, x, 830, 1.4, col)
        icon(c.pen, 'phone', x + 70, 640, 0.6)
    th = c.T('hanging')
    to = c.T('open')
    if c.on(th) and not c.on(to):
        cyc = ((c.t - th) * 1.4) % 1
        if cyc < 0.6: arrow(c.pen, 320, 640, 760, 640, cyc / 0.6, INK, 6, 22, dash=True)
        else: cross(c.pen, 540, 640, 1.1, RED, 9, 1)
        txt(c, 540, 960, 'call · hang up · call · hang up', th, 'ints', 32, MUTE)
    if c.on(to):
        pipe(c, 320, 760, 640, to, YEL, 52)
        txt(c, 540, 960, 'one call, never hung up', to, 'intx', 38, INK)
    te = c.T('either')
    blips(c, 320, 760, 640, te, 99, 0.9, right=True, col=WHITE, r=14)
    blips(c, 320, 760, 640, te + 0.45, 99, 0.9, right=False, col=BLUE, r=14)
    if c.on(te): label(c, 540, 1100, 'either side, any time', te, (200, 240, 200), INK, 34)


def frames(c):
    title(c, 'TINY FRAMES', 340, c.T('frame'), 100, hlcol=YEL)
    tf = c.T('frame')
    if c.on(tf):
        for k, (s_, col) in enumerate((('FIN · opcode', CYAN), ('length', YEL), ('payload: "hi"', WHITE))):
            x = 120 + [0, 300, 500][k]; w = [280, 180, 360][k]
            if c.on(tf + k * 0.2):
                c.pen.rr(x, 500, x + w, 590, 10, fill=col, outline=INK, w=4)
                c.pen.text(x + w / 2, 545, s_, 'monob', 26, INK)
        txt(c, 540, 650, 'header: 2 to 14 bytes', c.T('bytes'), 'intx', 40, GRN)
    bars(c, 80, 780, [('WS frame', 14, GRN, c.T('two')), ('HTTP request', 700, RED, c.T('hundreds'))], 700, w=560, gap=150, fmt='~{} B', lab_w=260, size=32)
    te = c.T('every')
    if c.on(te): txt(c, 540, 1140, 'headers on every request, cookies included', te, 'ints', 32, MUTE)


def code_(c):
    at = c.T('API') + 0.3
    code(c, 40, 380, 1040, 800, ["const ws = new WebSocket('wss://chat.example.com');", "ws.onopen = () => ws.send('hello');", 'ws.onmessage = (e) => show(e.data);',
                                 'ws.onclose = () => scheduleReconnect();'], at, 0.12, 26, 'chat.js',
         marks=[(0, c.T('Open'), YEL), (1, c.T('Send'), YEL), (2, c.T('Handle'), YEL), (3, c.T('closes'), YEL)])
    tw = c.T('WSS')
    if c.on(tw): label(c, 540, 930, 'wss:// = WebSocket over TLS', tw, WHITE, INK, 32)


def loop(c):
    chapter(c, 540, 350, 'S1 · E15', 'the event loop', c.T('loop'))
    tb = c.T('burst')
    if c.on(tb):
        n = int(min(36, (c.t - tb) * 30))
        for k in range(n):
            x = 120 + (k % 12) * 72; y = 460 + (k // 12) * 70
            c.pen.rr(x, y, x + 60, y + 54, 8, fill=YEL, outline=INK, w=3)
        counter(c, 540, 760, 0, 1000, tb, tb + 1.5, '{:,.0f}', 90, RED, ' tasks')
    tr = c.T('renders')
    if c.on(tr): stamp(c.cv, 540, 880, '1,000 RENDERS', 60, c.P(tr, 0.35), -4, RED); c.sfx(tr, 'thud')
    tbu = c.T('Buffer')
    code(c, 40, 960, 1040, 1330, ['ws.onmessage = (e) => {', '  buf.push(e.data);', '  if (buf.length === 1) requestAnimationFrame(flush);', '};',
                                  'const flush = () => render(buf.splice(0));'], tbu, 0.1, 26, 'batch.js',
         marks=[(2, c.T('once'), YEL)])


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    rows(c, 100, 540, [(c.T('EventSource'), 'EventSource', 'reconnects + Last-Event-ID', 'ok'), (c.T('drops'), 'WebSocket', 'one close event, then silence', 'no')], gap=170, h=130)
    tj = c.T('job')
    if c.on(tj): label(c, 540, 930, 'reconnect · catch up · resend = your job', tj, YEL, INK, 32)
    te = c.T('ten')
    if c.on(te): chapter(c, 540, 1060, 'S6 · E10', 'reconnect strategies', te)


SCENES = [
    (hook, "Back to WhatsApp Web. In the Network tab, filter by WS. That one row has status one oh one: switching protocols. It's the moment a WebSocket is born."),
    (upgrade, "It starts as an ordinary HTTP request, carrying a header: upgrade to websocket. The server agrees, with one oh one. From then on, the same TCP connection stops speaking HTTP. It carries frames, both ways."),
    (call, "Remember the phone call from season one, episode three, the TCP handshake? Plain HTTP is like hanging up after every single question. A WebSocket keeps the line open, and either side can speak, any time."),
    (frames, "Each message travels as a frame, text or binary, with just two to fourteen bytes of header. Compare that with hundreds of bytes of headers on every HTTP request."),
    (code_, "The API is four events. Open the connection. Send once it's open. Handle each message. And when it closes, plan a reconnect. Note the WSS: that's WebSocket over TLS."),
    (loop, "One catch. Each incoming message becomes a task in the event loop, from season one, episode fifteen. A burst of a thousand messages means a thousand tasks, and a thousand renders. Buffer them, and render once per frame."),
    (trap, "Interview trap: does a WebSocket reconnect by itself, like EventSource does? No. When it drops, you get one close event, and silence. Reconnecting, catching up, and resending are all your job. That's episode ten."),
    (scene_next('S6 · E06', 'WEBRTC', 'browser to browser, directly', 'WebRTC', 'directly'),
     "Next: WebRTC, where two browsers skip the server, and talk directly. Comment NOTES for the cheat sheet."),
]
