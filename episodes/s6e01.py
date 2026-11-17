from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E01', tag='S6 · E01', short='HOW DID IT ARRIVE?')


def chat_header(c, x0, y0, x1, name='Riya'):
    c.pen.rect(x0 + 5, y0, x1 - 5, y0 + 90, fill=(240, 238, 232))
    c.pen.line([(x0 + 5, y0 + 90), (x1 - 5, y0 + 90)], INK, 3, False)
    c.pen.circ(x0 + 60, y0 + 45, 28, fill=TEAL, outline=INK, w=3)
    c.pen.text(x0 + 105, y0 + 45, name, 'intx', 34, INK, 'lm')


def hook(c):
    x0, y0, x1, y1 = browser(c, 80, 330, 1000, 1000, 'web.whatsapp.com', dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    chat_header(c, x0, y0, x1)
    bubble(c, x0 + 40, x0 + 520, y0 + 180, 'Coming tonight?', 0.5, mine=False)
    bubble(c, x1 - 420, x1 - 40, y0 + 300, 'Yes! 8 pm?', 0.7, mine=True, n_ticks=2, tick_col=BLUE)
    ts, tp = c.T('send'), c.T('pops')
    if c.on(c.T('friend')):
        icon(c.pen, 'phone', 170, 1180, 1.3 * c.B(c.T('friend'), 0.4))
    packet(c, (120, 1120, 220, 1240), (x0, y0 + 300, x0 + 300, y0 + 500), ts, tp, YEL, 'msg')
    bubble(c, x0 + 40, x0 + 600, y0 + 420, 'Perfect, see you there', tp, mine=False)
    for kw, x, s_ in (('click', 520, 'no click'), ('refresh', 800, 'no refresh')):
        t = c.T(kw)
        if c.on(t):
            pill(c.pen, x, 1110, s_, c.B(t, 0.35), WHITE, INK, 32); c.sfx(t, 'pop')
            cross(c.pen, x - c.pen.tw(s_, 'int', 32) / 2 - 60, 1110, 0.7, RED, 7, c.P(t + 0.2, 0.3))
    tw = c.T('who')
    if c.on(tw): stamp(c.cv, 660, 1250, 'WHO TOLD IT?', 70, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')


def devtools(c):
    x0, y0, x1, y1 = panel(c, 60, 330, 1020, 1240, tabs=('Elements', 'Console', 'Network'), active=2, dy=(1 - c.P(0, 0.45)) * 900)
    tw = c.T('WS')
    xs = x0 + 40
    for k, f in enumerate(('All', 'Fetch/XHR', 'JS', 'WS')):
        w = c.pen.tw(f, 'int', 26) + 30
        on = f == 'WS' and c.on(tw)
        c.pen.rr(xs, y0 + 30, xs + w, y0 + 80, 12, fill=YEL if on else (40, 46, 56))
        c.pen.text(xs + w / 2, y0 + 55, f, 'int', 26, INK if on else (200, 205, 215))
        xs += w + 16
    if on: c.sfx(tw, 'click')
    tn = c.T('never')
    netrows(c, x0 + 40, y0 + 140, x1, [(tn, '?v=2.3000.x', ['101', 'Pending'], YEL)], cols=[x0 + 520, x0 + 680])
    tm = c.T('Messages')
    if c.on(tm):
        xs = x0 + 40
        for k, f in enumerate(('Headers', 'Messages', 'Initiator')):
            col = WHITE if f == 'Messages' else (130, 136, 146)
            c.pen.text(xs, y0 + 250, f, 'int', 28, col, 'lm')
            w = c.pen.tw(f, 'int', 28)
            if f == 'Messages': c.pen.rect(xs, y0 + 272, xs + w * c.P(tm, 0.3), y0 + 278, fill=YEL)
            xs += w + 40
        c.pen.line([(x0 + 18, y0 + 300), (x1 - 18, y0 + 300)], (60, 66, 76), 2, False)
    wsmsgs(c, x0 + 40, y0 + 370, x1 - 40, [(c.T('watch'), 'down', 'Binary Message', '1.2 kB'), (c.T('arrives'), 'down', 'Binary Message', '0.9 kB'),
                                           (c.T('Send'), 'up', 'Binary Message', '0.4 kB'), (c.T('green'), 'down', 'Binary Message', '0.2 kB')], 28, 70)
    tr = c.T('arrow')
    if c.on(tr): label(c, 540, 1080, 'down = received · up = sent', tr, YEL, INK, 30)


def postcard(c):
    title(c, 'HTTP: ASK, THEN ANSWER', 320, c.T('request'), 70, hlcol=YEL)
    lanes(c, 230, 850, 440, 1260, 0.1, 'Browser', 'Server')
    msg(c, 230, 850, 640, c.T('asks'), 'GET /messages')
    msg(c, 230, 850, 780, c.T('answers'), '200 OK', right=False)
    tn = c.T('nobody')
    msg(c, 230, 850, 980, tn, 'new message!', right=False, col=RED, dash=True)
    if c.on(tn + 0.5): cross(c.pen, 540, 1080, 1.2, RED, 11, c.P(tn + 0.5, 0.3)); c.sfx(tn + 0.5, 'buzz')
    tc = c.T('postcard')
    if c.on(tc): chapter(c, 540, 1200, 'S1 · E04', 'HTTP = a postcard', tc)


def oven(c, cx, cy, s=1.0, door=0.0):
    c.pen.rr(cx - 170, cy - 150, cx + 170, cy + 150, 20, fill=(220, 215, 205), outline=INK, w=5)
    c.pen.rr(cx - 140, cy - 80, cx + 140, cy + 125, 14, fill=(60, 50, 45) if door < 0.5 else (255, 190, 110), outline=INK, w=4)
    for k in range(3): c.pen.circ(cx - 90 + k * 60, cy - 115, 14, fill=WHITE, outline=INK, w=3)
    if door >= 0.5: c.pen.rr(cx - 70, cy + 20, cx + 70, cy + 80, 30, fill=(200, 140, 80), outline=INK, w=3)


def analogy(c):
    tb = c.T('oven')
    if c.on(tb):
        card(c.pen, 70, 400, 520, 1140, 26, WHITE, 10, 5)
        c.pen.text(295, 460, 'NO TIMER', 'osw', 48, INK)
        tc = c.T('check')
        door = (math.sin((c.t - tc) * 5) > 0) if c.on(tc) else False
        oven(c, 295, 630, door=1.0 if door else 0.0)
        person(c.pen, 295, 1050, 1.2, BLUE)
        if c.on(c.T('Again')): txt(c, 295, 1100, 'open · check · open · check', c.T('Again'), 'ints', 26, MUTE)
        label(c, 295, 835, 'PULL', tc, RED, WHITE, 32)
    to = c.T('opposite')
    if c.on(to):
        dy = (1 - c.P(to, 0.45)) * 900
        card(c.pen, 560, 400 + dy, 1010, 1140 + dy, 26, WHITE, 10, 5)
        c.pen.text(785, 460 + dy, 'THE TIMER', 'osw', 48, INK)
        icon(c.pen, 'clock', 785, 610 + dy, 1.6)
        td = c.T('dings')
        if c.on(td):
            c.sfx(td, 'ding')
            pill(c.pen, 785, 735 + dy, 'ding! ready', c.B(td, 0.35), YEL, INK, 34)
        person(c.pen, 785, 1050 + dy, 1.2, BLUE)
        label(c, 785, 835, 'PUSH', c.T('moment'), GRN, WHITE, 32)


def menu(c):
    title(c, 'THIS SEASON', 330, 0.15, 90, hlcol=YEL)
    rows(c, 100, 470, [(c.T('Short'), 'Short polling', 'ask on a timer', YEL), (c.T('Long'), 'Long polling', 'the server waits to answer', ORANGE),
                       (c.T('Server'), 'Server-Sent Events', 'a one-way stream', GRN), (c.T('WebSockets'), 'WebSockets', 'a two-way open line', BLUE),
                       (c.T('WebRTC'), 'WebRTC', 'browser to browser', PURPLE)], gap=118, h=100, size=38, sub_size=26)
    th = c.T('hard')
    if c.on(th): txt(c, 540, 1080, 'then the hard parts', th, 'intx', 36, INK)
    chips(c, 110, 1170, [('drops', LIGHT), ('ordering', LIGHT), ('duplicates', LIGHT), ('presence', LIGHT), ('co-editing', LIGHT)], c.T('dropped'), 0.45, 28)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 480, '"Real-time means WebSockets."', c.T('real'), 'intx', 46, INK)
    tn = c.T('Not')
    if c.on(tn): stamp(c.cv, 540, 610, 'NOT ALWAYS', 72, c.P(tn, 0.35), -4, RED); c.sfx(tn, 'thud')
    rows(c, 100, 790, [(c.T('badge'), 'Unread badge', 'poll every minute', YEL), (c.T('AI'), 'AI answer', 'stream with server-sent events', GRN)], gap=150, h=120)
    tp = c.T('Pick')
    if c.on(tp): label(c, 540, 1130, 'pick by: who talks, and how often', tp, YEL, INK, 34)


SCENES = [
    (hook, "Your friend hits send on her phone. Less than a second later, the message pops up in WhatsApp Web on your laptop. You didn't click. You didn't refresh. So who told your browser?"),
    (devtools, "Open DevTools, go to Network, and filter by WS. There's one connection that never finishes. Click it, open Messages, and watch. Every time a message arrives, a new frame appears with a red down arrow. Send one, and a green up arrow appears."),
    (postcard, "That's surprising, because the web was built on request and response. In season one, HTTP was a postcard. The browser asks, the server answers, done. The server can't send a postcard nobody asked for."),
    (analogy, "Think of baking a cake with no timer. You keep opening the oven to check. Again, and again. Real time is the opposite. The timer dings, the moment it's ready."),
    (menu, "This season covers five ways to get that ding. Short polling. Long polling. Server sent events. WebSockets. And WebRTC, where browsers talk directly to each other. Then the hard parts: dropped connections, ordering, duplicates, presence, and two people editing one document."),
    (trap, "Interview trap: real time means WebSockets. Not always. An unread badge can poll every minute. An AI answer streams fine over server sent events. Pick by who talks, and how often."),
    (scene_next('S6 · E02', 'SHORT POLLING', 'are we there yet?', 'polling', 'there'),
     "Next: short polling, the simplest trick of all. It's a kid asking, are we there yet? Comment NOTES for the cheat sheet."),
]
