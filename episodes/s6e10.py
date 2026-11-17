from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E10', tag='S6 · E10', short='RECONNECT')


def hook(c):
    x0, y0, x1, y1 = browser(c, 80, 330, 1000, 1060, 'web.whatsapp.com', dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    toff, ton = c.T('off'), c.T('gone')
    if c.on(toff) and not c.on(ton):
        banner(c, x0 + 30, x1 - 30, y0 + 70, 'Computer not connected', c.T('banner'), YEL, INK, 32, 90)
    for k, (s_, mine) in enumerate((('On my way', False), ('ok!', True))):
        bubble(c, (x1 - 300) if mine else (x0 + 40), (x1 - 40) if mine else (x0 + 420), y0 + 200 + k * 110, s_, 0.5 + k * 0.2, mine=mine, n_ticks=2 if mine else 0, tick_col=BLUE)
    tm = c.T('missed')
    for k, s_ in enumerate(('Where are you?', 'Call me', 'Reached?')):
        bubble(c, x0 + 40, x0 + 480, y0 + 420 + k * 110, s_, tm + k * 0.3, mine=False)
    if c.on(toff):
        on = c.on(c.T('back'))
        status(c, 140, 1150, 'Wi-Fi on' if on else 'Wi-Fi off', GRN if on else RED, toff, 34)
    ts = c.T('strategy')
    if c.on(ts): stamp(c.cv, 680, 1250, 'RECONNECT STRATEGY', 56, c.P(ts, 0.35), -4, RED); c.sfx(ts, 'thud')


def herd(c):
    title(c, 'THE NAIVE VERSION', 330, 0.1, 90, hlcol=YEL)
    code(c, 60, 420, 1020, 560, ['ws.onclose = () => connect(); // now!'], c.T('naive'), 0.1, 28, 'bad.js', dy=(1 - c.P(c.T('naive') - 0.45, 0.45)) * 900)
    s = node(c, 540, 1120, 240, 150, 'Server', c.T('restarts'), 'server')
    tr = c.T('restarts')
    if c.on(tr + 0.3) and not c.on(c.T('hundred')):
        txt(c, 540, 1230, 'restarting…', tr + 0.3, 'ints', 30, MUTE)
    th = c.T('hundred')
    if c.on(th):
        counter(c, 540, 650, 0, 100000, th, th + 1.0, '{:,.0f}', 90, RED, ' clients')
        rng = [(140 + (k * 97) % 800, 760 + (k * 53) % 160) for k in range(40)]
        q = c.P(c.T('second'), 0.6)
        for (x, y) in rng:
            xx = x + (540 - x) * q * 0.85; yy = y + (1080 - y) * q * 0.85
            c.pen.circ(xx, yy, 12, fill=YEL, outline=INK, w=2)
    to = c.T('over')
    if c.on(to): stamp(c.cv, 540, 1300, 'DOWN AGAIN', 64, c.P(to, 0.35), -4, RED); c.sfx(to, 'thud')


def gates(c):
    title(c, 'POWER CUT AT THE STADIUM', 330, c.T('stadium'), 72, hlcol=YEL)
    tr = c.T('rushes')
    ts = c.T('Stagger')
    c.pen.rect(470, 560, 490, 760, fill=INK); c.pen.rect(590, 560, 610, 760, fill=INK)
    c.pen.text(540, 520, 'GATE', 'osw', 40, INK)
    if c.on(tr) and not c.on(ts):
        for k in range(18):
            x = 300 + (k % 6) * 90 + 10 * math.sin(c.t * 9 + k); y = 870 + (k // 6) * 80
            person(c.pen, x, y + 60, 0.45, RED)
        cross(c.pen, 540, 660, 1.2, RED, 9, c.P(c.T('nobody'), 0.3))
    if c.on(ts):
        for k in range(6):
            q = ((c.t - ts) * 0.6 + k / 6) % 1
            y = 1100 - 600 * q
            person(c.pen, 540, y + 60, 0.45, GRN)
        label(c, 540, 1200, 'staggered: everyone gets in', c.T('everyone', 2), (200, 240, 200), INK, 32)


def backoff(c):
    chapter(c, 540, 340, 'S5 · E14', 'retries + backoff', c.T('backoff'))
    t1 = c.T('one')
    for k, (v, kw) in enumerate(((1, 'one'), (2, 'two'), (4, 'four'), (8, 'eight'), (30, 'thirty'))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 450 + k * 95; c.sfx(t, 'pop')
        w = 30 + 600 * min(v, 30) / 30 * c.P(t, 0.4)
        c.pen.text(200, y, f'try {k + 1}', 'int', 30, INK, 'rm')
        c.pen.rr(230, y - 30, 230 + w, y + 30, 12, fill=YEL if v < 30 else ORANGE, outline=INK, w=3)
        c.pen.text(250 + w, y, f'{v} s' + (' (cap)' if v == 30 else ''), 'intx', 30, INK, 'lm')
    tj = c.T('jitter')
    if c.on(tj):
        for k in range(30):
            x = 120 + ((k * 137) % 840); y = 980
            c.pen.line([(x, y - 25), (x, y + 25)], BLUE, 5)
        txt(c, 540, 1050, 'random jitter spreads clients out', tj, 'ints', 32, INK)
    code(c, 40, 1100, 1040, 1350, ['const max = Math.min(3e4, 1e3 * 2 ** n++);', 'setTimeout(connect, Math.random() * max);'], c.T('spread'), 0.12, 28, 'reconnect.js')


def resync(c):
    lanes(c, 230, 850, 360, 1300, 0.1)
    to = c.T('open')
    msg(c, 230, 850, 560, to, 'connected')
    msg(c, 230, 850, 690, c.T('ask'), 'since: seq 812')
    msg(c, 230, 850, 820, c.T('everything'), '813, 814, 815', right=False, col=GRN)
    tr = c.T('resend')
    msg(c, 230, 850, 980, tr, 'outbox: 2 unsent', col=ORANGE)
    tt = c.T('only')
    if c.on(tt): label(c, 540, 1170, 'then mark yourself online', tt, YEL, INK, 32)


def signals(c):
    title(c, 'LISTEN TO THE BROWSER', 330, c.T('Listen'), 84, hlcol=YEL)
    chips(c, 110, 470, [("'online'", (200, 240, 200)), ("'offline'", (255, 210, 210)), ("'visibilitychange'", LIGHT)], c.T('online'), 0.4, 30)
    tc = c.T('AbortController')
    chapter(c, 540, 650, 'S5 · E13', 'AbortController', tc)
    code(c, 40, 730, 1040, 1150, ['const ac = new AbortController();', "ws.addEventListener('message', onMsg,", '  { signal: ac.signal });',
                                  'fetch(`/sync?since=${seq}`, { signal: ac.signal });', '// socket dropped again:', 'ac.abort();'],
         tc + 0.4, 0.1, 27, 'teardown.js', marks=[(5, c.T('abort'), YEL)])
    to = c.T('call')
    if c.on(to): label(c, 540, 1250, 'one call cleans up the old socket', to, YEL, INK, 32)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Reconnect after every close?', c.T('every'), 'intx', 50, INK)
    rows(c, 100, 640, [(c.T('thousand'), 'code 1000', 'normal close: you meant it', 'no'), (c.T('auth'), 'logged out / auth failed', 'retrying will never fix it', 'no'),
                       (c.T('network'), 'network error, 1006', 'retry with backoff', 'ok')], gap=160, h=130)


SCENES = [
    (hook, "Turn off Wi-Fi with WhatsApp Web open. A yellow banner appears: computer not connected. Turn it back on, and seconds later, it's gone, and the messages you missed appear. That's a reconnect strategy, quietly at work."),
    (herd, "The naive version: on close, reconnect immediately. Now imagine the server restarts. A hundred thousand clients reconnect in the same second, and knock it right back over."),
    (gates, "It's a stadium after a power cut. If everyone rushes the same gate at once, nobody gets through. Stagger them, and everyone does."),
    (backoff, "This is the exponential backoff from season five, episode fourteen. Wait one second, then two, four, eight, capped at thirty. And add random jitter, so a hundred thousand clients spread out, instead of arriving together."),
    (resync, "Reconnecting isn't enough. You missed messages while you were offline. On open, ask the server for everything since the last sequence number you saw. Then resend anything still sitting in your outbox. Only then are you truly back."),
    (signals, "Listen to the browser, too. The online, offline, and visibility events tell you when a retry is worth it. And with an AbortController, from season five, episode thirteen, one abort call removes the old socket's listeners, and cancels its catch up fetch."),
    (trap, "Interview trap: should you reconnect after every close? No. Close code one thousand means a normal close, you meant it. And if the server closed you because your auth expired, retrying won't fix it. Retry on network errors. Stop, and re-authenticate, on auth failures."),
    (scene_next('S6 · E11', 'ORDERING', 'when replies arrive before questions', 'ordering', 'replies'),
     "Next: ordering, and why replies can arrive before the questions. Comment NOTES for the cheat sheet."),
]
