from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E14', tag='S5 · E14', short='RETRIES + BACKOFF', hook='try again, but politely')


def hook(c):
    sv = node(c, 540, 520, 260, 220, 'server', 0.2, 'server', sound=None)
    th = c.T('hiccups')
    if c.on(th) and not c.on(th + 1.0): cross(c.pen, 540, 520, 2.2, RED, 14, c.P(th, 0.3))
    tt = c.T('Ten')
    if c.on(tt):
        for k in range(40):
            x = 110 + (k % 10) * 95; y = 1000 + (k // 10) * 80
            icon(c.pen, 'phone', x, y, 0.45)
    ti = c.T('instantly')
    if c.on(ti):
        for w in range(3):
            t0 = ti + w * 0.9
            q = lin(c.t, t0, t0 + 0.6)
            if 0 < q < 1:
                for k in range(10):
                    x = 110 + k * 95
                    c.pen.circ(x + (540 - x) * q, 960 - (960 - 640) * q, 12, fill=RED, outline=INK, w=2)
            c.sfx(t0, 'tick')
    to = c.T('outage')
    if c.on(to): stamp(c.cv, 540, 800, 'BLIP → OUTAGE', 70, c.P(to, 0.35), -4, RED, k='intx'); c.sfx(to, 'thud')


def counter_(c):
    title(c, 'THE TICKET COUNTER', 340, c.T('counter'), 84)
    node(c, 540, 560, 360, 190, 'counter', 0.2, 'doc', sound=None)
    tr = c.T('rushes')
    if c.on(tr) and not c.on(c.T('one')):
        for k in range(7): person(c.pen, 200 + k * 110, 980 - 160 * c.P(tr, 0.5), 0.9, RED)
    to = c.T('one')
    for k, (kw, lab) in enumerate((('one', '1 min'), ('two', '2 min'), ('four', '4 min'))):
        t = c.T(kw)
        if c.on(t): pill(c.pen, 260 + k * 280, 840, lab, c.B(t, 0.35), YEL, INK, 36); c.sfx(t, 'pop')
    ts = c.T('same')
    if c.on(ts): label(c, 540, 1060, '…and not all at the same moment', ts, (255, 220, 220), INK, 30)


def backoff(c):
    title(c, 'EXPONENTIAL BACKOFF', 340, c.T('exponential'), 84, hlcol=YEL)
    td = c.T('double')
    for k, s in enumerate((1, 2, 4, 8, 16)):
        t = td + k * 0.35
        if not c.on(t): continue
        x = 140 + k * 170; h = min(500, 32 * s) if s < 16 else 500
        hh = h * c.P(t, 0.4)
        c.pen.rect(x + 6, 1050 - hh + 6, x + 126, 1056, fill=INK)
        c.pen.rect(x, 1050 - hh, x + 120, 1050, fill=YEL if s < 16 else LIGHT, outline=INK, w=4)
        c.pen.text(x + 60, 1100, f'{s} s' if s < 16 else 'cap', 'intx', 34, INK)
        c.sfx(t, 'tick')
    label(c, 540, 470, 'wait, then double it after every failure', td, YEL, INK, 30)


def jitter(c):
    title(c, 'ADD JITTER', 340, c.T('jitter'), 100, hlcol=YEL)
    txt(c, 540, 450, 'a random slice of each delay', c.T('random'), 'intx', 36, INK)
    c.pen.line([(100, 900), (980, 900)], INK, 5)
    c.pen.text(100, 940, 'when clients retry', 'int', 26, MUTE, 'lm')
    tsp = c.T('spread')
    p = c.P(tsp, 0.8) if c.on(tsp) else 0.0
    for k in range(18):
        x = 540 + (140 + k * 48 - 540) * p
        h = 380 * (1 - p) + (30 + (k * 37) % 50) * p
        c.pen.rect(x - 18, 900 - h, x + 18, 900, fill=mix(RED, GRN, p), outline=INK, w=2)
    if p < 0.3: txt(c, 540, 1010, 'everyone at the same instant', 0.3, 'int', 30, RED)
    th = c.T('herd')
    if c.on(th): label(c, 540, 1060, 'no thundering herd', th, (200, 240, 200), INK, 34)


CODE = ['async function withRetry(fn, tries = 3) {', '  for (let i = 0; ; i++) {', '    try { return await fn(); }', '    catch (e) {',
        '      if (i >= tries || !retryable(e)) throw e;', '      const wait = 2 ** i * 500;', '      await sleep(Math.random() * wait);', '    }', '  }', '}']


def code_(c):
    code(c, 30, 360, 1050, 360 + 72 + len(CODE) * 48 + 20, CODE, c.T('code'), 0.08, 26, 'retry.js',
         marks=[(1, c.T('loop'), YEL), (2, c.T('try'), YEL), (5, c.T('grows'), YEL), (6, c.T('randomness'), YEL), (4, c.T('Give'), YEL)])


def which(c):
    title(c, 'ONLY RETRY WHAT’S SAFE', 340, c.T('safe'), 62, hlcol=YEL, k='intx')
    grid(c, 90, 450, [520, 380], [
        (c.T('safe'), ['', 'retry?']),
        (c.T('Network'), ['network error', 'ok']),
        (c.T('timeouts'), ['timeout · 408', 'ok']),
        (c.T('three'), ['503 unavailable', 'ok']),
        (c.T('twenty'), ['429 (after Retry-After)', 'ok']),
        (c.T('Never'), ['400 bad request', 'no']),
        (c.T('oh', 2), ['404 not found', 'no'])], rowh=100, size=32)
    tf = c.T('forever')
    if c.on(tf): label(c, 540, 1230, 'they fail the same way forever', tf, (255, 220, 220), INK, 30)


def rq(c):
    tr = c.T('season')
    if c.on(tr): chapter(c, 540, 350, 'S4 · E12', 'React Query', tr)
    code(c, 30, 440, 1050, 440 + 72 + 5 * 50 + 20, ['useQuery({', "  queryKey: ['me'], queryFn: getMe,", '  retry: 3,   // the default',
                                                     '  retryDelay: (n) => Math.min(1000 * 2 ** n, 30000),', '});'],
         c.T('React'), 0.1, 25, 'Profile.jsx', marks=[(2, c.T('three'), YEL), (3, c.T('backoff'), YEL)])
    tb = c.T('backoff')
    if c.on(tb): label(c, 540, 900, '1 s · 2 s · 4 s … capped at 30 s', tb, YEL, INK, 32)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tp = c.T('POST')
    if c.on(tp): method(c, 200, 480, 'POST', '/orders  (timed out)', tp, 32)
    ts = c.T('second')
    if c.on(ts):
        node(c, 340, 680, 300, 150, 'order #1', ts, fill=WHITE, size=34)
        node(c, 740, 680, 300, 150, 'order #2', ts + 0.3, fill=(255, 220, 220), size=34)
        stamp(c.cv, 540, 850, 'CHARGED TWICE', 70, c.P(ts + 0.5, 0.35), -4, RED); c.sfx(ts + 0.5, 'thud')
    ti = c.T('idempotency')
    if c.on(ti): label(c, 540, 1000, 'retry writes only with Idempotency-Key', ti, YEL, INK, 30)
    tm = c.T('mutations')
    if c.on(tm): txt(c, 540, 1110, 'React Query: mutations retry 0 times by default', tm, 'intx', 32, INK)


SCENES = [
    (hook, "The server hiccups for one second. Ten thousand phones see the error, and all of them retry instantly. Then again. And again. You just turned a blip into an outage."),
    (counter_, "Picture a crowded ticket counter that closes for a minute. If everyone rushes back the second it reopens, it jams again. Better: come back in one minute, then two, then four. And not all at the same moment."),
    (backoff, "That's exponential backoff. Wait, then double the wait after every failure. One second, two, four, eight, up to a cap."),
    (jitter, "Now add jitter, a random slice of each delay. Ten thousand clients spread out, instead of retrying in sync. That's how you avoid the thundering herd."),
    (code_, "In code, it's a loop, a try, and a sleep that grows each time, with randomness on top. Give up after a few tries."),
    (which, "Only retry what's safe. Network errors, timeouts, five oh three, and four twenty nine. Never retry a four hundred bad request, or a four oh four. They'll fail the same way forever."),
    (rq, "You rarely write this yourself. React Query, from season four, retries failed queries three times by default, with exponential backoff."),
    (gotcha, "Interview trap. Should you auto retry a failed POST that places an order? Not blindly. If the first attempt reached the server, a retry places a second order. Retry writes only with an idempotency key. That's also why React Query doesn't retry mutations by default."),
    (scene_next('S5 · E15', 'DEDUPLICATION', 'one request, many components', 'deduplication', 'five'),
     "Next: request deduplication, when five components ask for the same data. Comment NOTES for the cheat sheet."),
]
