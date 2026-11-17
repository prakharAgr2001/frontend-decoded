from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E11', tag='S5 · E11', short='PARALLEL REQUESTS')


def hook(c):
    for k, (kw, nm, ic) in enumerate((('user', 'user', 'eye'), ('stats', 'stats', 'cpu'), ('notifications', 'notifications', 'bolt'))):
        node(c, 200 + k * 340, 470, 300, 190, nm, c.T(kw), ic, size=30)
    td = c.T('depend')
    if c.on(td): txt(c, 540, 650, 'no dependencies between them', td, 'intx', 38, INK)
    tw = c.T('wait')
    if c.on(tw):
        reqbars(c, 80, 1000, 780, [(tw, 'user', 0, 0.3, RED, 0.3), (tw + 0.3, 'stats', 0.3, 0.7, RED, 0.3), (tw + 0.6, 'notifications', 0.7, 1.0, RED, 0.3)],
                gap=80, lab_w=260, dark=False)
        stamp(c.cv, 540, 1110, 'WHY WAIT?', 80, c.P(tw + 0.8, 0.35), -4, RED); c.sfx(tw + 0.8, 'thud')


def court(c):
    title(c, 'THE FOOD COURT', 340, c.T('food'), 96)
    tt = c.T('Three')
    for k in range(3):
        x = 220 + k * 320
        if c.on(tt + k * 0.15):
            node(c, x, 560, 260, 160, ['dosa', 'momos', 'biryani'][k], tt + k * 0.15, size=34)
            person(c.pen, x, 880, 1.2, [BLUE, ORANGE, GRN][k])
    tn = c.T('Nobody')
    if c.on(tn):
        for k, d in enumerate((0.5, 0.75, 0.35)):
            x = 220 + k * 320 - 110
            c.pen.rr(x, 930, x + 220 * c.P(tn, 1.5 * d), 970, 12, fill=YEL, outline=INK, w=3)
    ts = c.T('slowest')
    if c.on(ts): label(c, 540, 1080, 'dinner is ready when the slowest stall is done', ts, YEL, INK, 28)


CODE = ['const [user, stats, notes] = await Promise.all([', '  fetchUser(),', '  fetchStats(),', '  fetchNotes(),', ']);']


def code_(c):
    code(c, 30, 360, 1050, 360 + 72 + len(CODE) * 50 + 20, CODE, c.T('code'), 0.1, 26, 'dashboard.js', marks=[(0, c.T('together'), YEL)])
    ts = c.T('start')
    if c.on(ts):
        reqbars(c, 80, 1000, 830, [(ts, 'user', 0, 0.45, GRN, 0.4), (ts, 'stats', 0, 0.8, GRN, 0.6), (ts, 'notifications', 0, 0.3, GRN, 0.3)],
                gap=80, lab_w=260, dark=False)
    tsl = c.T('slowest')
    if c.on(tsl):
        xa = 80 + 260 + 660 * 0.8
        c.pen.line([(xa, 780), (xa, 1060)], RED, 5)
        txt(c, xa, 1100, 'total = slowest', tsl, 'intx', 32, RED)
    tsu = c.T('sum')
    if c.on(tsu): txt(c, 540, 1200, 'not the sum', tsu, 'intx', 40, INK)


def road(c):
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 350, 'S1 · E05', 'the multi-lane road', ts)
    tl = c.T('lanes')
    if c.on(tl):
        c.pen.rect(80, 480, 1000, 760, fill=(90, 94, 100))
        for k in range(1, 4):
            for x in range(80, 1000, 80): c.pen.rect(x, 480 + k * 70 - 3, x + 40, 480 + k * 70 + 3, fill=WHITE)
        for k in range(4):
            x = 80 + ((c.t - tl) * (260 + k * 60)) % 920
            c.pen.rr(x, 495 + k * 70, x + 90, 535 + k * 70, 10, fill=[YEL, CYAN, PINK, GRN][k], outline=INK, w=3)
        txt(c, 540, 810, 'HTTP/2: many requests, one connection', tl, 'intx', 34, INK)
    tsx = c.T('six')
    if c.on(tsx):
        counter(c, 540, 1000, 0, 6, tsx, tsx + 0.5, '{:.0f}', 140, RED, '')
        txt(c, 540, 1120, 'HTTP/1.1: max connections per host', tsx + 0.3, 'intx', 34, INK)


def sharp(c):
    head(c, 'A SHARP EDGE', 'sharp', size=84)
    tf = c.T('fails')
    for k, (nm, ok) in enumerate((('user', True), ('stats', True), ('notifications', False))):
        y = 560 + k * 130
        c.pen.rr(100, y - 45, 980, y + 45, 16, fill=WHITE, outline=INK, w=4)
        c.pen.text(140, y, nm, 'intx', 36, INK, 'lm')
        if c.on(tf):
            if ok: check(c.pen, 920, y, 1.1, GRN, 10, c.P(tf, 0.3))
            else: cross(c.pen, 920, y, 1.1, RED, 10, c.P(tf, 0.3)); c.sfx(tf, 'buzz')
    tl = c.T('lose')
    if c.on(tl):
        stamp(c.cv, 540, 1000, 'ALL REJECTED', 84, c.P(tl, 0.35), -4, RED); c.sfx(tl, 'thud')
        txt(c, 540, 1140, 'the two good results are thrown away', tl + 0.3, 'intx', 34, INK)


SCODE = ['const results = await Promise.allSettled([', '  fetchUser(), fetchStats(), fetchNotes(),', ']);', 'results.forEach((r) => {',
         "  if (r.status === 'fulfilled') show(r.value);", '  else showError(r.reason);', '});']


def settled(c):
    code(c, 30, 360, 1050, 360 + 72 + len(SCODE) * 50 + 20, SCODE, c.T('settled') - 0.4, 0.1, 26, 'dashboard.js',
         marks=[(0, c.T('settled'), YEL), (4, c.T('worked'), YEL), (5, c.T('error'), YEL)])
    te = c.T('error')
    for k, (nm, ok) in enumerate((('user', True), ('stats', True), ('notifications', False))):
        t = c.T('stats') + k * 0.2 if k < 2 else te
        x = 200 + k * 340
        if c.on(t): node(c, x, 1050, 300, 170, nm if ok else 'couldn’t load', t, fill=WHITE if ok else (255, 220, 220), sub=None if ok else 'retry', size=30)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 40, 440, 1040, 440 + 72 + 3 * 50 + 20, ['const a = await fetchA();', 'const b = await fetchB(); // waits', 'const c = await fetchC(); // waits'],
         c.T('awaits'), 0.12, 28, 'is-this-parallel.js', marks=[(1, c.T('pauses'), YEL), (2, c.T('pauses') + 0.2, YEL)])
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 780, 'NOT PARALLEL', 70, c.P(tn, 0.35), -4, RED); c.sfx(tn, 'thud')
    ts = c.T('Start')
    code(c, 40, 900, 1040, 900 + 72 + 2 * 50 + 20, ['const pa = fetchA(), pb = fetchB();', 'const [a, b] = await Promise.all([pa, pb]);'],
         ts, 0.12, 27, 'fixed.js', marks=[(0, ts + 0.4, YEL), (1, c.T('await', 2), YEL)])


SCENES = [
    (hook, "A dashboard needs the user, the stats, and the notifications. None of them depend on each other. So why wait for one, before starting the next?"),
    (court, "Picture a food court. Three friends, three stalls. Nobody waits for the others to order. Dinner is ready when the slowest stall is done."),
    (code_, "In code, start all three, then await them together, with Promise dot all. Total time becomes the slowest request, not the sum."),
    (road, "This works because of what we saw in season one. HTTP two sends many requests over one connection, like lanes on a multi lane road. On old HTTP one point one, browsers open at most six connections per host."),
    (sharp, "But Promise dot all has a sharp edge. If one request fails, the whole thing rejects, and you lose the two that succeeded."),
    (settled, "Promise dot all settled waits for every request, and tells you which ones worked. Show the user and the stats, and an error card only where notifications failed."),
    (gotcha, "Interview trap. This code awaits three fetches, one per line. Is it parallel? No. Each await pauses before the next fetch even starts. Start the promises first, then await them together."),
    (scene_next('S5 · E12', 'RACE CONDITIONS', 'when an old response wins', 'race', 'old'),
     "Next: race conditions, when an old response arrives last, and wins. Comment NOTES for the cheat sheet."),
]
