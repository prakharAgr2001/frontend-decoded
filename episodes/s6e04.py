from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E04', tag='S6 · E04', short='SERVER-SENT EVENTS')

ANSWER = 'An event loop runs one task at a time, then checks the queue for the next one...'


def hook(c):
    x0, y0, x1, y1 = browser(c, 80, 330, 1000, 800, 'chat.example.ai', dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    bubble(c, x1 - 470, x1 - 40, y0 + 70, 'What is an event loop?', 0.5, mine=True)
    tt = c.T('types')
    if c.on(tt):
        n = int(max(0, c.t - tt) * 14)
        s = ANSWER[:n]
        for i, ln in enumerate(wrap(c.pen, s, 'intm', 32, 800)[:4]):
            c.pen.text(x0 + 40, y0 + 190 + i * 52, ln, 'intm', 32, INK, 'lm')
    tn = c.T('Network')
    if c.on(tn):
        px0, py0, px1, py1 = panel(c, 60, 880, 1020, 1280, tabs=('Headers', 'Response'), dy=(1 - c.P(tn, 0.45)) * 600)
        kv(c, px0 + 40, py0 + 60, px1, [(c.T('click'), 'Status:', '200', GRN), (c.T('text'), 'content-type:', 'text/event-stream', YEL),
                                        (c.T('arriving'), 'Time:', 'still loading…', WHITE)], 30, 64)


def define(c):
    title(c, 'SERVER-SENT EVENTS', 330, c.T('server'), 96, hlcol=YEL)
    tr = c.T('request')
    b = node(c, 200, 760, 230, 190, 'Browser', tr, 'laptop')
    s = node(c, 880, 760, 230, 190, 'Server', tr + 0.2, 'server')
    if c.on(tr + 0.4):
        arrow(c.pen, 330, 580, 750, 580, c.P(tr + 0.4, 0.4), INK, 6, 22)
        pill(c.pen, 540, 580, 'GET /stream', c.B(tr + 0.6, 0.3), WHITE, INK, 28)
    tn = c.T('never')
    pipe(c, 320, 760, 760, tn, YEL, 56)
    blips(c, 320, 760, 760, c.T('writing'), 99, 0.6, right=False, col=WHITE, r=16, speed=0.8)
    tw = c.T('news')
    if c.on(tw): label(c, 540, 960, 'event · event · event', tw, WHITE, INK, 32)
    tn2 = c.T('closes')
    if c.on(tn2): txt(c, 540, 1080, 'the response never ends', tn2, 'intx', 40, INK)


def radio(c):
    title(c, 'TUNE IN ONCE', 330, c.T('radio'), 100, hlcol=YEL)
    tt = c.T('station')
    if c.on(tt):
        icon(c.pen, 'tower', 270, 720, 2.2 * c.B(tt, 0.4))
    tk = c.T('keeps')
    if c.on(tk):
        for k in range(3):
            r = 90 + ((c.t - tk) * 140 + k * 70) % 210
            c.pen.arc(270 - r, 640 - r, 270 + r, 640 + r, -35, 35, mix(PAPER, BLUE, 1 - (r - 90) / 210), 8)
    ti = c.T('tune')
    if c.on(ti):
        s = c.B(ti, 0.4)
        card(c.pen, 640, 600 - 90 * s, 940, 600 + 120 * s, 24, ORANGE, 10, 5)
        c.pen.circ(720, 640, 46 * s, fill=WHITE, outline=INK, w=4)
        for k in range(4): c.pen.line([(800, 590 + k * 26), (900, 590 + k * 26)], INK, 5)
    tl = c.T('listen')
    if c.on(tl): label(c, 540, 930, 'server → you: all day', tl, (200, 240, 200), INK, 34)
    tb = c.T('back')
    if c.on(tb):
        label(c, 540, 1060, 'you → server: not on this channel', tb, (255, 210, 210), INK, 34)


def fmt(c):
    tw = c.T('wire')
    code(c, 40, 330, 1040, 780, ['id: 42', 'event: message', 'data: {"text":"Hello"}', '', 'id: 43', 'data: {"text":"World"}'], tw, 0.12, 30, 'GET /stream (text)',
         marks=[(1, c.T('name'), YEL), (2, c.T('data'), YEL), (0, c.T('id'), YEL)], lang='text')
    tb = c.T('blank')
    if c.on(tb): label(c, 760, 610, '← blank line ends it', tb, YEL, INK, 26)
    te = c.T('EventSource')
    code(c, 40, 850, 1040, 1180, ["const es = new EventSource('/stream');", 'es.onmessage = (e) => {', '  render(JSON.parse(e.data));', '};'], te, 0.12, 30, 'app.js')


def resume(c):
    lanes(c, 230, 850, 380, 1300, 0.1)
    msg(c, 230, 850, 560, 0.4, 'id: 41', right=False)
    msg(c, 230, 850, 660, 0.9, 'id: 42', right=False)
    td = c.T('drops')
    if c.on(td): stamp(c.cv, 540, 780, 'CONNECTION DROPPED', 56, c.P(td, 0.35), -3, RED); c.sfx(td, 'thud')
    msg(c, 230, 850, 880, c.T('reconnects'), 'GET /stream')
    th = c.T('header')
    if c.on(th): pill(c.pen, 540, 980, 'Last-Event-ID: 42', c.B(th, 0.35), YEL, INK, 32); c.sfx(th, 'pop')
    msg(c, 230, 850, 1080, c.T('resumes'), 'id: 43', right=False, col=GRN)
    tn = c.T('nothing')
    if c.on(tn): check(c.pen, 540, 1230, 1.4, GRN, 11, c.P(tn, 0.35)); c.sfx(tn, 'tick')


def lanes6(c, at, busy):
    for k in range(6):
        y = 610 + k * 46
        c.pen.line([(140, y + 20), (940, y + 20)], GREY, 3, False)
        if c.on(at + k * 0.1) and busy:
            x = 160 + ((c.t - at) * 60 + k * 90) % 700
            c.pen.rr(x, y + 2, x + 80, y + 38, 8, fill=YEL, outline=INK, w=3)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    ts = c.T('seven')
    for k in range(7):
        t = ts + k * 0.08
        if not c.on(t): continue
        x = 110 + k * 125
        bad = k == 6
        c.pen.rr(x, 450, x + 110, 520, 12, fill=(255, 210, 210) if bad else WHITE, outline=RED if bad else INK, w=4)
        c.pen.text(x + 55, 485, f'tab {k + 1}', 'int', 22, INK)
    th = c.T('hangs')
    if c.on(th):
        spinner(c, 875, 565, 22, RED)
    tr = c.T('road')
    if c.on(tr):
        lanes6(c, tr, True)
        chapter(c, 540, 930, 'S1 · E05', 'the multi-lane road', tr)
    tsx = c.T('six')
    if c.on(tsx): label(c, 540, 1030, 'HTTP/1.1: ~6 connections per site', tsx, (255, 210, 210), INK, 30)
    tsh = c.T('share')
    if c.on(tsh):
        pipe(c, 140, 940, 1150, tsh, GRN, 50)
        blips(c, 140, 940, 1150, tsh + 0.3, 99, 0.25, right=False, col=WHITE, r=12, speed=1.2)
        txt(c, 540, 1240, 'HTTP/2: every stream shares one connection', tsh + 0.5, 'ints', 30, INK)


def limits(c):
    title(c, 'TWO LIMITS', 330, c.T('limits'), 100, hlcol=YEL)
    rows(c, 100, 540, [(c.T('way'), 'One way only', 'to send, use a normal POST', 'no'), (c.T('text'), 'Text only', 'no binary frames', 'no')], gap=170, h=130)
    tb = c.T('both')
    if c.on(tb): label(c, 540, 960, 'both directions, fast? → next tool', tb, YEL, INK, 34)


SCENES = [
    (hook, "Ask an AI chatbot a question, and the answer types itself out, word by word. Open the Network tab, and click that request. In many AI chat apps, the content type is text slash event stream. One response, still arriving."),
    (define, "That's server sent events, or SSE. A normal HTTP request, but the server never closes the response. It keeps writing small events down the same open pipe, whenever it has news."),
    (radio, "It's a radio station. You tune in once, and the station keeps talking. You can listen all day. But you can't talk back on the same channel."),
    (fmt, "On the wire, it's plain text. Each event is a few lines: an optional event name, the data, an id, and a blank line to end it. In the browser, EventSource reads them for you."),
    (resume, "And here's the gift. If the connection drops, EventSource reconnects by itself, and sends a header called Last Event ID, with the last id it saw. The server resumes from there. You lose nothing."),
    (trap, "Interview trap: an SSE dashboard works fine in one tab. Open seven tabs, and the seventh just hangs. Remember the multi lane road, from season one, episode five? On HTTP one point one, a browser allows about six connections per site, and every open stream holds one. On HTTP two, all streams share one connection."),
    (limits, "SSE has two limits. It's one way: to send, you use a normal POST. And it's text only. When you need both directions, fast, you need a different tool."),
    (scene_next('S6 · E05', 'WEBSOCKETS', 'a line that never hangs up', 'WebSockets', 'hangs'),
     "Next: WebSockets, a line that never hangs up. Comment NOTES for the cheat sheet."),
]
