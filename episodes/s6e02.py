from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E02', tag='S6 · E02', short='SHORT POLLING')


def hook(c):
    x0, y0, x1, y1 = panel(c, 60, 330, 1020, 1150, tabs=('Network', 'Fetch/XHR'), dy=(1 - c.P(0, 0.45)) * 900)
    c.pen.text(x0 + 40, y0 + 50, 'Name', 'int', 24, (130, 136, 146), 'lm')
    c.pen.text(x0 + 560, y0 + 50, 'Status', 'int', 24, (130, 136, 146), 'lm')
    c.pen.text(x0 + 720, y0 + 50, 'Size', 'int', 24, (130, 136, 146), 'lm')
    ts = c.T('same')
    netrows(c, x0 + 40, y0 + 120, x1, [(ts + k * 0.75, 'unread?user=me', ['200', '0.3 kB'], YEL if k == 0 else None) for k in range(10)],
            gap=58, cols=[x0 + 560, x0 + 720])
    tp = c.T('short')
    if c.on(tp): stamp(c.cv, 540, 1260, 'SHORT POLLING', 80, c.P(tp, 0.35), -4, RED); c.sfx(tp, 'thud')


def define(c):
    lanes(c, 230, 850, 420, 1290, 0.1)
    tt = c.T('timer')
    if c.on(tt): pill(c.pen, 540, 420, 'every 5 s', c.B(tt, 0.35), YEL, INK, 32); c.sfx(tt, 'pop')
    for k, (kq, nq, ka, na) in enumerate((('anything', 1, 'No', 1), ('anything', 2, 'No', 2), ('Usually', 1, 'no', 3))):
        y = 620 + k * 220
        msg(c, 230, 850, y, c.T(kq, nq), 'anything new?')
        msg(c, 230, 850, y + 90, c.T(ka, na), 'no', right=False, col=MUTE)


def car(c):
    title(c, 'ARE WE THERE YET?', 340, c.T('kid'), 96, hlcol=YEL)
    p = c.P(0, 0.5); dx = (1 - p) * -900
    bob = 4 * math.sin(c.t * 12)
    c.pen.poly([(330 + dx, 560 + bob), (700 + dx, 560 + bob), (790 + dx, 650 + bob), (250 + dx, 650 + bob)], fill=RED, outline=INK, w=5)
    c.pen.rr(180 + dx, 640 + bob, 900 + dx, 790 + bob, 34, fill=RED, outline=INK, w=5)
    for x in (350, 600):
        c.pen.rect(x - 70 + dx, 585 + bob, x + 70 + dx, 645 + bob, fill=(210, 225, 245), outline=INK, w=3)
    c.pen.circ(350 + dx, 620 + bob, 18, fill=YEL, outline=INK, w=3)
    c.pen.circ(600 + dx, 615 + bob, 22, fill=(250, 220, 190), outline=INK, w=3)
    for x in (330, 740):
        c.pen.circ(x + dx, 800, 52, fill=INK); c.pen.circ(x + dx, 800, 20, fill=GREY)
    for k, (kw, n, s_, left) in enumerate((('there', 1, 'Are we there yet?', True), ('No', 1, 'No.', False), ('there', 2, 'Are we there yet?', True), ('No', 2, 'No.', False))):
        t = c.T(kw, n)
        y = 920 + (k // 2) * 100
        if c.on(t):
            c.sfx(t, 'pop')
            pill(c.pen, 330 if left else 820, y, s_, c.B(t, 0.35), WHITE if left else LIGHT, INK, 32)
    tn = c.T('Ninety')
    if c.on(tn): counter(c, 540, 1180, 0, 99, tn, tn + 0.9, '{:.0f}', 90, RED, ' questions')
    tu = c.T('useful')
    if c.on(tu): label(c, 540, 1300, '1 useful answer', tu, (200, 240, 200), INK, 32)


def code_(c):
    at = c.T('code') + 0.3
    code(c, 40, 360, 1040, 860, ['setInterval(async () => {', "  const res = await fetch('/api/unread');", '  const { count } = await res.json();',
                                 '  badge.textContent = count;', '}, 5000);'], at, 0.12, 30, 'poll.js',
         marks=[(0, c.T('timer'), YEL), (4, c.T('five'), YEL), (1, c.T('fetch'), YEL), (3, c.T('badge'), YEL)])
    tb = c.T('badge')
    if c.on(tb):
        s = c.B(tb, 0.4); c.sfx(tb, 'pop')
        card(c.pen, 330, 1000, 750, 1160, 24, WHITE, 10, 5)
        c.pen.text(470, 1080, 'Inbox', 'intx', 50 * s, INK)
        c.pen.circ(660, 1080, 46 * s, fill=RED, outline=INK, w=4)
        c.pen.text(660, 1080, '3', 'intx', 50 * s, WHITE)


def cost(c):
    title(c, 'THE COST', 330, c.T('cost'), 100, hlcol=YEL)
    tl = c.T('Latency')
    timerbar(c, 120, 480, 960, c.P(tl + 0.3, 1.2, lambda x: x), tl, 'latency: a message waits', YEL, 56, 'up to 5 s')
    tt = c.T('ten')
    if c.on(tt): txt(c, 540, 680, '10,000 tabs ÷ every 5 s', tt, 'intx', 46, INK)
    tr = c.T('requests')
    if c.on(tr): counter(c, 540, 820, 0, 2000, tr, tr + 0.9, '{:,.0f}', 130, RED, ' req/s')
    te = c.T('empty')
    if c.on(te):
        for k in range(20):
            t = te + k * 0.02
            if not c.on(t): continue
            x = 150 + (k % 10) * 80; y = 990 + (k // 10) * 90
            hit = k == 13
            c.pen.rr(x, y, x + 64, y + 64, 10, fill=GRN if hit else LIGHT, outline=INK, w=3)
        txt(c, 540, 1230, '19 of 20 come back empty', te + 0.45, 'ints', 34, MUTE)


def whenok(c):
    title(c, 'STILL THE RIGHT CALL', 330, c.T('right'), 84, hlcol=YEL)
    txt(c, 540, 440, 'when updates are rare and seconds of delay are fine', c.T('rare'), 'ints', 32, MUTE)
    rows(c, 100, 570, [(c.T('dashboard'), 'Dashboards', None, 'ok'), (c.T('build'), 'Build status', None, 'ok'), (c.T('unread'), 'Unread badge', None, 'ok')], gap=140)
    tp = c.T('proxy')
    if c.on(tp): label(c, 540, 1010, 'works through every proxy and firewall', tp, WHITE, INK, 32)
    ts = c.T('simple')
    if c.on(ts): stamp(c.cv, 540, 1150, 'DEAD SIMPLE', 70, c.P(ts, 0.35), -4, GRN); c.sfx(ts, 'thud')


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 460, 'setInterval + fetch', c.T('set'), 'monob', 44, INK)
    tp = c.T('pile')
    for k in range(4):
        t = tp + k * 0.25
        if not c.on(t): continue
        x = 140 + k * 150; y = 540 + k * 46
        w = 420 * c.P(t, 0.5)
        c.pen.rr(x, y, x + w, y + 36, 10, fill=(255, 200, 200), outline=RED, w=3)
    to = c.T('order')
    if c.on(to): stamp(c.cv, 760, 610, 'OVERLAP', 56, c.P(to, 0.35), 5, RED); c.sfx(to, 'thud')
    ti = c.T('Instead')
    code(c, 40, 800, 1040, 1150, ['async function poll() {', '  if (!document.hidden) await refresh();', '  setTimeout(poll, 5000);', '}'], ti, 0.12, 28, 'poll.js',
         marks=[(2, c.T('finishes'), YEL), (1, c.T('hidden'), YEL)])


SCENES = [
    (hook, "Open a page with a live notification count, and watch the Network tab. On many sites, you'll see the same tiny request, again and again, every few seconds, forever. That's short polling."),
    (define, "Short polling means the browser asks the server for news on a fixed timer. Every five seconds: anything new? No. Anything new? No. Usually, the answer is no."),
    (car, "It's a kid in the back seat. Are we there yet? No. Are we there yet? No. Ninety nine questions, for one useful answer."),
    (code_, "In code, it's just a timer. Fetch the unread count, update the badge, and repeat every five seconds."),
    (cost, "The cost comes in two numbers. Latency: a new message can wait up to five seconds before it shows. And load: ten thousand open tabs, polling every five seconds, is two thousand requests a second. Almost all of them come back empty."),
    (whenok, "Still, it's often the right call, when updates are rare, and a few seconds of delay is fine. A dashboard. A build status. An unread badge. It works through every proxy and firewall, and it's dead simple."),
    (trap, "Interview trap: set interval with fetch. If the server slows down, requests pile up, overlap, and can arrive out of order. Instead, schedule the next poll only after the last one finishes. And skip the work while the tab is hidden."),
    (scene_next('S6 · E03', 'LONG POLLING', 'the server waits before it answers', 'long', 'waits'),
     "Next: long polling, where the server doesn't say no. It waits. Comment NOTES for the cheat sheet."),
]
