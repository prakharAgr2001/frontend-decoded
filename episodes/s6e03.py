from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E03', tag='S6 · E03', short='LONG POLLING')


def hook(c):
    x0, y0, x1, y1 = panel(c, 60, 330, 1020, 1100, tabs=('Network', 'Fetch/XHR'), dy=(1 - c.P(0, 0.45)) * 900)
    tp, tt = c.T('pending'), c.T('Then')
    done = c.on(tt)
    if c.on(0.5):
        c.pen.text(x0 + 40, y0 + 80, 'updates?since=812', 'mono', 28, WHITE, 'lm')
        c.pen.text(x0 + 560, y0 + 80, '200' if done else '(pending)', 'mono', 28, GRN if done else (200, 205, 215), 'lm')
        f = lin(c.t, tp, tt)
        c.pen.rect(x0 + 40, y0 + 130, x0 + 40 + 820 * f, y0 + 160, fill=YEL if not done else GRN)
    if c.on(tp): counter(c, 540, y0 + 330, 0, 30, tp, tt, '{:.0f}', 160, INK if not done else GRN, ' s')
    if done:
        c.pen.text(x0 + 40, y0 + 500, 'updates?since=813', 'mono', 28, WHITE, 'lm')
        c.pen.text(x0 + 560, y0 + 500, '(pending)', 'mono', 28, (200, 205, 215), 'lm')
        c.pen.rect(x0 + 40, y0 + 550, x0 + 40 + 820 * lin(c.t, tt, tt + 8), y0 + 580, fill=YEL)
    tb = c.T('broken')
    if c.on(tb): txt(c, 540, 1200, "It isn't broken.", tb, 'intx', 46, INK)
    tpu = c.T('purpose')
    if c.on(tpu): stamp(c.cv, 540, 1310, 'ON PURPOSE', 76, c.P(tpu, 0.35), -4, GRN); c.sfx(tpu, 'thud')


def how(c):
    lanes(c, 230, 850, 400, 1300, 0.1)
    ta = c.T('asks', 1)
    msg(c, 230, 850, 600, ta, 'anything new?')
    th = c.T('holds')
    hold(c, 850, 650, 900, th, YEL, 2.0)
    if c.on(th): txt(c, 690, 760, 'holding…', th + 0.3, 'ints', 30, MUTE)
    tr = c.T('arrives')
    packet(c, (980, 860, 1060, 900), (830, 860, 870, 900), tr, tr + 0.5, YEL, 'msg')
    msg(c, 230, 850, 900, c.T('answers'), 'here: 1 message', right=False)
    tg = c.T('again')
    msg(c, 230, 850, 1080, tg, 'anything new?')
    hold(c, 850, 1130, 1260, tg + 0.4, YEL, 1.5)


def window(c):
    title(c, 'THE ENQUIRY WINDOW', 330, c.T('enquiry'), 90, hlcol=YEL)
    card(c.pen, 560, 450, 980, 900, 20, (230, 222, 205), 10, 5)
    c.pen.rr(620, 520, 920, 760, 14, fill=(210, 225, 245), outline=INK, w=4)
    c.pen.rr(660, 470, 880, 520, 10, fill=INK)
    c.pen.text(770, 495, 'ENQUIRY', 'osw', 32, YEL)
    person(c.pen, 770, 760, 1.0, ORANGE)
    person(c.pen, 330, 1000, 1.3, BLUE)
    tl = c.T('later')
    if c.on(tl):
        pill(c.pen, 400, 520, 'not yet, come back later', c.B(tl, 0.35), WHITE, INK, 28); c.sfx(tl, 'pop')
        cross(c.pen, 400, 520, 1.6, RED, 9, c.P(tl + 0.4, 0.3))
    tw = c.T('wait')
    if c.on(tw): pill(c.pen, 600, 1010, "wait here, I'll tell you", c.B(tw, 0.35), YEL, INK, 32); c.sfx(tw, 'pop')
    ta = c.T('announced')
    if c.on(ta): label(c, 540, 1160, 'Platform 3!', ta + 0.3, GRN, WHITE, 40); c.sfx(ta + 0.3, 'ding')


def timeout(c):
    lanes(c, 230, 850, 400, 1300, 0.1)
    msg(c, 230, 850, 600, 0.3, 'anything new?')
    tn = c.T('nothing')
    hold(c, 850, 650, 960, 0.6, YEL, 4.0)
    tt = c.T('thirty')
    if c.on(tt): pill(c.pen, 960, 900, '30 s', c.B(tt, 0.35), YEL, INK, 30); icon(c.pen, 'clock', 960, 820, 0.7 * c.B(tt, 0.35))
    tp = c.T('proxies')
    if c.on(tp): label(c, 540, 780, 'proxies cut idle requests', tp, (255, 210, 210), INK, 28)
    msg(c, 230, 850, 970, c.T('empty'), '204 · nothing', right=False, col=MUTE)
    msg(c, 230, 850, 1130, c.T('again'), 'anything new?')
    th = c.T('harm')
    if c.on(th): check(c.pen, 540, 1260, 1.4, GRN, 11, c.P(th, 0.35)); c.sfx(th, 'tick')


def code_(c):
    at = c.T('loop', 1) + 0.2
    code(c, 40, 360, 1040, 960, ['async function poll() {', '  try {', '    const res = await fetch(`/updates?since=${last}`);',
                                 '    if (res.status === 200) handle(await res.json());', '  } catch {', '    await sleep(2000);', '  }', '  poll();', '}'],
         at, 0.1, 26, 'long-poll.js',
         marks=[(2, c.T('Fetch'), YEL), (3, c.T('Handle'), YEL), (5, c.T('wait'), YEL), (7, c.T('loop', 2), YEL)])
    tl = c.T('seen')
    if c.on(tl): label(c, 540, 1080, 'since = the last id you saw', tl, YEL, INK, 32)


def trade(c):
    versus(c, ('WINS', GRN, c.T('wins'), [(c.T('instant'), 'near-instant delivery'), (c.T('anywhere'), 'plain HTTP, works anywhere')]),
           ('COSTS', RED, c.T('costs'), [(c.T('headers'), 'full request + headers per message'), (c.T('open'), 'one open request per user')]), 400, 1100)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tg = c.T('gap', 1)
    if c.on(tg):
        p = c.P(tg, 0.5)
        c.pen.rr(120, 520, 120 + 360 * p, 580, 14, fill=YEL, outline=INK, w=4)
        c.pen.text(300, 620, 'poll 1 returns', 'ints', 28, INK)
        if c.on(tg + 0.6):
            c.pen.rr(620, 520, 620 + 340 * c.P(tg + 0.6, 0.5), 580, 14, fill=YEL, outline=INK, w=4)
            c.pen.text(790, 620, 'poll 2 starts', 'ints', 28, INK)
    tl = c.T('lost')
    if c.on(tl):
        c.pen.circ(550, 550, 26 * c.B(tl, 0.35), fill=RED, outline=INK, w=4); c.sfx(tl, 'pop')
        txt(c, 550, 690, 'message lands in the gap', tl, 'intx', 36, RED)
    tc = c.T('cursor')
    if c.on(tc): label(c, 540, 830, 'GET /updates?since=812', tc, WHITE, INK, 34)
    ta = c.T('after', 2)
    if c.on(ta): txt(c, 540, 950, 'server returns everything after 812', ta, 'ints', 34, INK)
    ts = c.T('slips')
    if c.on(ts): stamp(c.cv, 540, 1110, 'NOTHING LOST', 76, c.P(ts, 0.35), -4, GRN); c.sfx(ts, 'thud')


SCENES = [
    (hook, "Sometimes in the Network tab, one request just sits there, pending, for thirty seconds. Then it finishes, and a new one starts. It isn't broken. It's long polling, on purpose."),
    (how, "The browser asks: anything new? Instead of saying no, the server holds the request open. The moment a message arrives, it answers. The browser shows it, and immediately asks again."),
    (window, "It's like the enquiry window at a railway station. You ask about your train, and instead of: not yet, come back later, the clerk says: wait right here. I'll tell you the moment it's announced."),
    (timeout, "If nothing happens, the server doesn't hold forever. After about thirty seconds, it answers empty, so proxies and load balancers don't cut the idle request. The browser just asks again. No harm done."),
    (code_, "The client is a simple loop. Fetch, with the id of the last thing you've seen. Handle anything new. On a network error, wait a moment. Then loop."),
    (trade, "The wins: delivery is near instant, and it's plain HTTP, so it works anywhere. The costs: every message pays for a full request with headers, and the server keeps one open request per user."),
    (trap, "Interview trap: a message lands in the gap, after one poll returns and before the next one starts. Is it lost? Not if you send a cursor, like the last message id, with every request. The server returns everything after it, so nothing slips through the gap."),
    (scene_next('S6 · E04', 'SERVER-SENT EVENTS', 'one request, endless answers', 'server', 'keeps'),
     "Next: server sent events. One request, and the server keeps talking. Comment NOTES for the cheat sheet."),
]
