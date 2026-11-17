from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E16', tag='S5 · E16', short='429: SLOW DOWN')


def hook(c):
    tf = c.T('fine')
    if c.on(tf): label(c, 540, 360, 'everything is fine', tf, (200, 240, 200), INK, 32)
    tt = c.T('ten')
    if c.on(tt):
        n = min(10, int((c.t - tt) / 0.12) + 1)
        for k in range(n):
            x = 120 + k * 88
            c.pen.rr(x, 450, x + 80, 500, 10, fill=WHITE, outline=INK, w=3)
            c.sfx(tt + k * 0.12, 'click')
    t4 = c.T('twenty')
    if c.on(t4):
        box = panel(c, 60, 560, 1020, 1000, tabs=('Network',), dy=0)
        netrows(c, box[0] + 40, box[1] + 50, box[2] - 40, [(t4 + k * 0.15, f'GET /api/feed?tab={k + 1}', ['429'], RED) for k in range(5)],
                size=26, gap=58, cols=[box[2] - 120])
    tm = c.T('many')
    if c.on(tm): stamp(c.cv, 540, 1130, 'TOO MANY REQUESTS', 70, c.P(tm, 0.35), -3, RED); c.sfx(tm, 'thud')


def why(c):
    title(c, 'RATE LIMITS', 340, c.T('rate'), 110, hlcol=YEL)
    tp = c.T('protect')
    if c.on(tp): node(c, 540, 580, 280, 220, 'API', tp, 'shield')
    tn = c.T('number')
    if c.on(tn): pill(c.pen, 540, 800, 'N requests', c.B(tn, 0.35), WHITE, INK, 40)
    tu = c.T('user')
    if c.on(tu): pill(c.pen, 540, 900, 'per user · or per IP', c.B(tu, 0.35), WHITE, INK, 36)
    tw = c.T('window')
    if c.on(tw): pill(c.pen, 540, 1000, 'per time window', c.B(tw, 0.35), YEL, INK, 40)


def jar(c):
    title(c, 'THE TOKEN BUCKET', 340, c.T('bucket'), 96)
    tj = c.T('jar')
    if not c.on(tj): return
    # jar
    c.pen.rr(380, 520, 700, 1000, 30, fill=(235, 245, 250), outline=INK, w=6)
    c.pen.rr(400, 490, 680, 530, 10, fill=GREY, outline=INK, w=4)
    ts = c.T('spends'); tr = c.T('refills'); te = c.T('Empty')
    n = 10
    if c.on(ts): n -= min(4, int((c.t - ts) / 0.3))
    if c.on(tr): n = min(10, n + int((c.t - tr) / 0.6))
    if c.on(te): n = max(0, 10 - int((c.t - te) / 0.12) - 0)
    for k in range(n):
        x = 440 + (k % 4) * 66; y = 950 - (k // 4) * 70
        c.pen.circ(x + 20, y, 26, fill=YEL, outline=INK, w=3)
    if c.on(ts): label(c, 860, 620, '1 request = 1 coin', ts, WHITE, INK, 26)
    if c.on(tr): label(c, 860, 740, 'refills steadily', tr, (200, 240, 200), INK, 26)
    tw = c.T('wait')
    if c.on(tw): stamp(c.cv, 540, 1110, 'EMPTY: WAIT', 70, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')


def proof(c):
    browser(c, 50, 330, 1030, 1150, 'api.github.com/users/octocat', dy=(1 - c.P(0, 0.45)) * 900)
    th = c.T('headers')
    if c.on(th):
        box = panel(c, 90, 460, 990, 1080, tabs=('Headers',), dy=0)
        kv(c, box[0] + 40, box[1] + 60, box[2], [(c.T('sixty'), 'x-ratelimit-limit:', '60', YEL),
                                                 (c.T('remaining'), 'x-ratelimit-remaining:', str(max(55, 59 - int(max(0, c.t - c.T('remaining')) / 0.5))), YEL),
                                                 (c.T('reset'), 'x-ratelimit-reset:', '1763...', YEL)], size=30, gap=80)
    t6 = c.T('sixty')
    if c.on(t6): label(c, 540, 1010, 'unauthenticated: 60 per hour', t6, YEL, INK, 30)


CODE = ['if (res.status === 429) {', "  const s = Number(res.headers.get('Retry-After'));", '  await sleep((s || 1) * 1000);', '}']


def retry_after(c):
    t4 = c.T('twenty')
    if c.on(t4): method(c, 90, 360, 'GET', '/api/feed  → 429', t4, 32)
    tr = c.T('Retry')
    if c.on(tr):
        box = panel(c, 60, 450, 1020, 620, tabs=('Response headers',), dy=0)
        kv(c, box[0] + 40, box[1] + 40, box[2], [(tr, 'retry-after:', '30', YEL)], size=32)
    code(c, 30, 700, 1050, 700 + 72 + len(CODE) * 52 + 20, CODE, c.T('exactly'), 0.1, 26, 'fetch.js', marks=[(1, c.T('exactly') + 0.5, YEL), (2, c.T('Respect'), YEL)])
    tg = c.T('guessing')
    if c.on(tg): label(c, 540, 1160, 'respect it instead of guessing', tg, YEL, INK, 32)


def good(c):
    title(c, 'BE A GOOD CLIENT', 340, c.T('client'), 96, hlcol=YEL)
    tdb = c.T('Debounce')
    if c.on(tdb): chapter(c, 540, 500, 'S3 · E23', 'debounce search', tdb)
    tdd = c.T('Dedupe')
    if c.on(tdd): chapter(c, 540, 620, 'S5 · E15', 'dedupe identical calls', tdd)
    tc = c.T('Cache')
    if c.on(tc): chapter(c, 540, 740, 'S4 · E12', 'cache what doesn’t change', tc)
    ti = c.T('inflicted')
    if c.on(ti): stamp(c.cv, 540, 950, 'MOSTLY SELF-INFLICTED', 64, c.P(ti, 0.35), -3, RED); c.sfx(ti, 'thud')


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tp = c.T('IP')
    if c.on(tp): pill(c.pen, 540, 470, 'limit: 100 req / min per IP', c.B(tp, 0.35), WHITE, INK, 34)
    to = c.T('office')
    if c.on(to):
        for k in range(10):
            person(c.pen, 130 + k * 92, 740, 0.7, [BLUE, ORANGE, GRN, PURPLE, TEAL][k % 5])
        c.pen.rr(100, 580, 980, 770, 20, outline=INK, w=4)
        c.pen.text(540, 560, 'office', 'int', 28, INK)
    ts = c.T('share')
    if c.on(ts):
        node(c, 540, 900, 380, 130, '1 public IP', ts, 'globe', size=30)
        stamp(c.cv, 540, 1050, 'EVERYONE BLOCKED', 60, c.P(ts + 0.4, 0.35), -3, RED); c.sfx(ts + 0.4, 'thud')
    tk = c.T('key')
    if c.on(tk): label(c, 540, 1180, 'limit per user or API key, not just per IP', tk, YEL, INK, 28)


SCENES = [
    (hook, "Your app is working fine. Then one user opens ten tabs, and every request comes back four twenty nine. Too many requests."),
    (why, "APIs protect themselves with rate limits. A fixed number of requests, per user, or per IP address, in a time window."),
    (jar, "A common design is the token bucket. Picture a jar of coins. Every request spends one coin. The jar refills at a steady rate. Burst a little, and you're fine. Empty the jar, and you wait."),
    (proof, "GitHub shows you the meter. Call its API without logging in, and check the response headers. X rate limit limit: sixty. X rate limit remaining, counting down with every call. And a reset time."),
    (retry_after, "When you do get a four twenty nine, look for the Retry After header. It tells you exactly how long to wait. Respect it, instead of guessing."),
    (good, "And be a good client. Debounce search, from season three. Dedupe identical calls. Cache what doesn't change. Most four twenty nines are self inflicted."),
    (gotcha, "Interview trap. Your rate limit is per IP address, and a whole office of users suddenly gets blocked. Why? They share one public IP, behind the same network. Limit per user, or per API key, not just per IP."),
    (scene_next('S5 · E17', 'SKELETON SCREENS', 'loading that feels faster', 'skeleton', 'faster'),
     "Next: skeleton screens, and why some loading states feel faster than others. Comment NOTES for the cheat sheet."),
]
