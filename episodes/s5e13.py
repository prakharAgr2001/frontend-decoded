from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E13', tag='S5 · E13', short='ABORTCONTROLLER')


def hook(c):
    ti = c.T('ignore')
    if c.on(ti): pill(c.pen, 540, 360, 'ignore flag: stale result dropped', c.B(ti, 0.35), YEL, INK, 32)
    br = node(c, 200, 700, 240, 220, 'browser', 0.2, 'laptop', sound=None)
    sv = node(c, 880, 700, 240, 220, 'server', 0.2, 'server', sound=None)
    ts = c.T('still')
    if c.on(ts):
        link(c, br, sv, ts, 0.4)
        for k in range(4):
            t0 = ts + 0.4 + k * 0.5
            packet(c, sv, br, t0, t0 + 0.8, GREY, 'bytes')
    td = c.T('downloads')
    if c.on(td): txt(c, 540, 900, 'still downloading · still using the network', td, 'intx', 34, INK)
    tst = c.T('stop')
    if c.on(tst): stamp(c.cv, 540, 1090, 'CAN WE STOP IT?', 76, c.P(tst, 0.35), -4, RED); c.sfx(tst, 'thud')


def define(c):
    title(c, 'AbortController', 340, c.T('AbortController'), 90, hlcol=YEL, k='intx')
    code(c, 40, 440, 1040, 440 + 72 + 4 * 52 + 20, ['const ctrl = new AbortController();', 'fetch(url, { signal: ctrl.signal });', '// later…', 'ctrl.abort();'],
         c.T('Create'), 0.12, 30, 'cancel.js', marks=[(1, c.T('signal'), YEL), (3, c.T('abort'), YEL)])
    ta = c.T('abort')
    br = node(c, 250, 1000, 240, 200, 'browser', ta, 'laptop')
    sv = node(c, 830, 1000, 240, 200, 'server', ta, 'server')
    if c.on(ta + 0.3):
        link(c, br, sv, ta + 0.3, 0.4, GREY, 5, dash=True)
        cross(c.pen, 540, 1000, 1.4, RED, 12, c.P(ta + 0.6, 0.3)); c.sfx(ta + 0.6, 'buzz')


def delivery(c):
    title(c, 'CANCEL THE ORDER', 340, c.T('cancelling'), 96)
    node(c, 250, 650, 260, 230, 'restaurant', 0.2, 'chef', sound=None)
    tr = c.T('rider')
    x = 470 + 30 * math.sin(c.t * 2)
    c.pen.circ(x, 680, 30, fill=YEL, outline=INK, w=4)
    c.pen.text(x, 740, 'rider', 'int', 26, INK)
    if c.on(tr): stamp(c.cv, 640, 880, 'ORDER CANCELLED', 56, c.P(tr, 0.35), -6, RED); c.sfx(tr, 'thud')
    tw = c.T('waiting')
    if c.on(tw):
        person(c.pen, 540, 1080, 1.2, BLUE)
        label(c, 540, 1180, 'you stop waiting', tw, YEL, INK, 32)


FIX = ['useEffect(() => {', '  const ctrl = new AbortController();', '  fetch(`/u/${id}`, { signal: ctrl.signal })', '    .then((r) => r.json()).then(setUser)',
       '    .catch((e) => {', "      if (e.name !== 'AbortError') setError(e);", '    });', '  return () => ctrl.abort();', '}, [id]);']


def react(c):
    code(c, 30, 360, 1050, 360 + 72 + len(FIX) * 50 + 20, FIX, c.T('React') - 0.3, 0.08, 26, 'User.jsx',
         marks=[(7, c.T('cleanup'), YEL), (5, c.T('AbortError'), YEL)])
    tp = c.T('previous')
    if c.on(tp): label(c, 540, 1000, 'id changes → previous request cancelled', tp, YEL, INK, 30)
    tf = c.T('failure')
    if c.on(tf): txt(c, 540, 1100, 'a cancel is not a real failure', tf, 'intx', 36, INK)


def proof(c):
    box = panel(c, 40, 330, 1040, 1100, tabs=('Network', 'Fetch/XHR'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, _ = box
    tt = c.T('Type')
    q = ['s', 'sh', 'sho', 'shoe', 'shoes']
    if c.on(tt):
        n = min(5, int((c.t - tt) / 0.35) + 1)
        tc = c.T('canceled')
        for k in range(n):
            y = y0 + 60 + k * 76
            done = k == 4
            canc = (not done) and (c.t > tt + (k + 1) * 0.35)
            c.sfx(tt + k * 0.35, 'click')
            col = (140, 146, 156) if canc else WHITE
            c.pen.text(x0 + 40, y, f'search?q={q[k]}', 'mono', 28, col, 'lm')
            c.pen.text(x1 - 60, y, '(canceled)' if canc else ('200' if done and c.on(tc) else 'pending'), 'mono', 28,
                       (150, 156, 166) if canc else (GRN if done else YEL), 'rm')
            if canc: c.pen.line([(x0 + 40, y), (x0 + 40 + c.pen.tw(f'search?q={q[k]}', 'mono', 28), y)], (140, 146, 156), 3, False)
    tc = c.T('canceled')
    if c.on(tc): label(c, 540, y0 + 520, 'old requests: (canceled), in grey', tc, YEL, INK, 30)


def timeout(c):
    code(c, 40, 380, 1040, 380 + 72 + 2 * 52 + 20, ['fetch(url, {', '  signal: AbortSignal.timeout(5000) });'], c.T('timeout') - 0.3, 0.12, 28, 'timeout.js',
         marks=[(1, c.T('itself'), YEL)])
    tf = c.T('Five')
    if c.on(tf):
        ring(c, 540, 780, 130, c.P(tf, 2.0, lambda x: x), YEL, 22)
        c.pen.text(540, 780, str(max(0, 5 - int(c.P(tf, 2.0, lambda x: x) * 5))) + ' s', 'osw', 90, INK)
    th = c.T('hanging')
    if c.on(th): label(c, 540, 1000, 'gives up instead of hanging forever', th, YEL, INK, 32)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tp = c.T('Pay')
    if c.on(tp): pill(c.pen, 540, 470, 'Pay ₹499', c.B(tp, 0.35), GRN, WHITE, 40)
    ta = c.T('abort')
    if c.on(ta): txt(c, 540, 570, 'user cancels → ctrl.abort()', ta, 'intx', 36, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 680, 'NO', 100, c.P(tn, 0.35), -5, RED); c.sfx(tn, 'thud')
    tb = c.T('browser')
    br = node(c, 230, 880, 240, 180, 'browser', tb, 'laptop', sub='stops waiting')
    sv = node(c, 850, 880, 240, 180, 'server', tb + 0.2, 'server', sub='still running')
    tch = c.T('charged')
    if c.on(tch): label(c, 850, 1020, 'card charged', tch, (255, 220, 220), INK, 28)
    ti = c.T('idempotency')
    if c.on(ti): label(c, 540, 1160, 'writes: idempotency key + check status', ti, YEL, INK, 30)


SCENES = [
    (hook, "The ignore flag drops a stale response. But the request still runs. It still downloads, still uses the network. Can we actually stop it?"),
    (define, "Yes, with AbortController. Create a controller, pass its signal to fetch, and call abort when you no longer need the answer."),
    (delivery, "It's like cancelling a food delivery order before the rider leaves. Nothing gets carried to you, and you stop waiting."),
    (react, "In React, abort in the effect's cleanup. Every time the id changes, the previous request is cancelled. And catch the AbortError, because a cancel is not a real failure."),
    (proof, "Watch it in DevTools. Type fast into a search box that aborts. In the Network panel, the old requests show up as canceled, in grey."),
    (timeout, "One more trick. AbortSignal dot timeout gives you a signal that aborts itself. Five seconds, and the request gives up, instead of hanging forever."),
    (gotcha, "Interview trap. The user hits Pay, then cancels, and you call abort. Is the payment cancelled? No. Abort only stops the browser from waiting. The server may have already charged the card. For writes, use an idempotency key, and check the status on the server."),
    (scene_next('S5 · E14', 'RETRIES + BACKOFF', 'try again, politely', 'retries', 'politely'),
     "Next: retries with exponential backoff, or how to try again politely. Comment NOTES for the cheat sheet."),
]
