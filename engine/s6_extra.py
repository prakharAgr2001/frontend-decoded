"""Season 6 helpers (real-time). Built only on engine.lib primitives (+ S3 helpers); does not change shared code."""
from engine.lib import *
from engine.s3_extra import at_, head, rows, versus, axis, bars, phone, spinner, kv, netrows, season_map

BUBBLE_ME = (220, 246, 200)
SENT_BG = (34, 64, 44)


def lanes(c, xl, xr, y0, y1, at, left='Browser', right='Server', lic='laptop', ric='server'):
    """sequence-diagram lifelines: icon + name on top, dashed line down"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.4); p = c.P(at + 0.1, 0.6)
    for x, nm, ic in ((xl, left, lic), (xr, right, ric)):
        icon(c.pen, ic, x, y0, 0.85 * s)
        c.pen.text(x, y0 + 72, nm, 'intx', 32 * s, INK)
        yb = y0 + 105; ye = yb + (y1 - yb) * p
        k = 0
        while yb + k * 30 < ye:
            c.pen.line([(x, yb + k * 30), (x, min(ye, yb + k * 30 + 16))], GREY, 5, False); k += 1


def msg(c, xl, xr, y, at, text=None, right=True, col=INK, d=0.45, dash=False, slope=36, size=26, fill=WHITE):
    """arrow between lifelines at height y (sloping down = travel time), pill label on it"""
    if not c.on(at): return
    c.sfx(at, 'swish')
    x0, x1 = (xl + 14, xr - 14) if right else (xr - 14, xl + 14)
    arrow(c.pen, x0, y, x1, y + slope, c.P(at, d), col, 6, 22, dash)
    if text and c.on(at + d * 0.5):
        pill(c.pen, (x0 + x1) / 2, y + slope / 2, text, c.B(at + d * 0.5, 0.3), fill, INK, size)


def hold(c, x, y0, y1, at, col=YEL, d=0.6, w=26):
    """activation bar on a lifeline (server holding a request open)"""
    if not c.on(at): return
    ye = y0 + (y1 - y0) * c.P(at, d, lambda q: q)
    c.pen.rect(x - w / 2, y0, x + w / 2, ye, fill=col, outline=INK, w=3)


def pipe(c, x0, x1, y, at, col=YEL, h=44, d=0.5, alive=1.0):
    """an open connection drawn as a tube; alive<1 fades it to grey"""
    if not c.on(at - 0.01): return
    xe = x0 + (x1 - x0) * c.P(at, d)
    fill = mix(LIGHT, col, alive)
    c.pen.rr(x0 + 6, y - h / 2 + 7, xe + 6, y + h / 2 + 7, h / 2, fill=INK)
    c.pen.rr(x0, y - h / 2, xe, y + h / 2, h / 2, fill=fill, outline=INK, w=4)


def blips(c, x0, x1, y, t0, t1, period=0.8, right=True, col=WHITE, r=13, speed=0.7, phase=0.0):
    """dots streaming along a pipe from t0 to t1, one every `period` s"""
    if c.t < t0: return
    k = 0
    while True:
        ts = t0 + phase + k * period
        if ts > min(c.t, t1): break
        q = (c.t - ts) / speed
        if 0 <= q <= 1:
            x = x0 + (x1 - x0) * q if right else x1 - (x1 - x0) * q
            c.pen.circ(x, y, r, fill=col, outline=INK, w=3)
            if q < 0.08: c.sfx(ts, 'tick')
        k += 1


def wsmsgs(c, x0, y0, x1, items, size=26, gap=58):
    """DevTools WS -> Messages rows: (kw|time, 'up'|'down', text, meta)"""
    for i, it in enumerate(items):
        kw, dr, text = it[0], it[1], it[2]
        meta = it[3] if len(it) > 3 else ''
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        y = y0 + i * gap; p = c.P(t, 0.25); c.sfx(t, 'tick')
        if dr == 'up': c.pen.rect(x0 - 12, y - gap / 2 + 4, x1 + 12, y + gap / 2 - 4, fill=mix(DARK, SENT_BG, p))
        c.pen.text(x0, y, '↑' if dr == 'up' else '↓', 'monob', size + 4, mix(DARK, GRN if dr == 'up' else RED, p), 'lm')
        c.pen.text(x0 + 44, y, text, 'mono', size, mix(DARK, WHITE, p), 'lm')
        if meta: c.pen.text(x1, y, meta, 'mono', size - 4, mix(DARK, (150, 156, 166), p), 'rm')


def ticks(pen, x, y, n=2, col=MUTE, s=0.55):
    for k in range(n):
        check(pen, x + k * 16 * s * 1.6, y, s, col, 5)


def bubble(c, x0, x1, y, text, at, mine=True, n_ticks=0, tick_col=MUTE, size=30, sub=None, fill=None):
    """chat bubble spanning x0..x1 (mine = green, right-aligned text box), optional ticks"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.35); c.sfx(at, 'pop')
    h = 78 if not sub else 104
    f = fill or (BUBBLE_ME if mine else WHITE)
    cx, cy = (x0 + x1) / 2, y
    w2, h2 = (x1 - x0) / 2 * s, h / 2 * s
    card(c.pen, cx - w2, cy - h2, cx + w2, cy + h2, 22, f, 6, 4)
    if s > 0.7:
        c.pen.text(x0 + 26, cy - (12 if sub else 0), text, 'ints', size, INK, 'lm')
        if sub: c.pen.text(x0 + 26, cy + 28, sub, 'intm', 22, MUTE, 'lm')
        if n_ticks: ticks(c.pen, x1 - 54, cy + 14, n_ticks, tick_col)


def status(c, x, y, text, col, at, size=32, anchor='lm'):
    """coloured status dot + label"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.3)
    c.pen.circ(x, y, 14 * s, fill=col, outline=INK, w=3)
    c.pen.text(x + 30, y, text, 'ints', size * s, INK, 'lm')


def banner(c, x0, x1, y, text, at, col=YEL, tcol=INK, size=30, h=80):
    if not c.on(at - 0.01): return
    p = c.P(at, 0.35); c.sfx(at, 'pop')
    yy = y - (1 - p) * 30
    c.pen.rr(x0, yy - h / 2, x1, yy + h / 2, 14, fill=mix(WHITE, col, p), outline=INK, w=4)
    c.pen.text((x0 + x1) / 2, yy, text, 'ints', size, mix(WHITE, tcol, p))


def caret(c, x, y, name, col, at, h=56):
    """collaborator cursor: coloured caret with a name flag"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.3)
    c.pen.rect(x - 3, y - h / 2, x + 3, y + h / 2, fill=col)
    w = c.pen.tw(name, 'int', 22) + 20
    c.pen.rr(x - 3, y - h / 2 - 36 * s, x - 3 + w * s, y - h / 2, 6, fill=col)
    if s > 0.6: c.pen.text(x + 7, y - h / 2 - 18, name, 'int', 22, WHITE, 'lm')


def chaps(c, items, y0=650, gap=100):
    for i, (tag, name, kw) in enumerate(items):
        chapter(c, 540, y0 + i * gap, tag, name, at_(c, kw))
