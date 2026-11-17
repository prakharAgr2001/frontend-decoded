"""Season 5 helpers (data fetching & APIs). Built only on engine.lib + engine.s3_extra; does not change shared code."""
from engine.lib import *
from engine.s3_extra import *

MCOL = {'GET': GRN, 'POST': ORANGE, 'PUT': BLUE, 'PATCH': PURPLE, 'DELETE': RED}


def method(c, x, y, m, path, at, size=34, sub=None):
    """HTTP method pill + path (left-aligned at x)"""
    if not c.on(at - 0.01): return
    c.sfx(at, 'pop'); s = c.B(at, 0.35)
    w = c.pen.tw(m, 'monob', size) + 34
    col = MCOL.get(m, YEL)
    c.pen.rr(x, y - 28 * s, x + w, y + 28 * s, 14, fill=col, outline=INK, w=4)
    c.pen.text(x + w / 2, y, m, 'monob', size * s, WHITE if col != YEL else INK)
    p = c.P(at + 0.1, 0.3)
    c.pen.text(x + w + 20 + (1 - p) * 20, y, path, 'monob', size, mix(PAPER, INK, p), 'lm')
    if sub: c.pen.text(x + w + 20, y + 44, sub, 'intm', 26, mix(PAPER, MUTE, p), 'lm')


def reqbars(c, x0, x1, y0, items, gap=82, h=44, lab_w=260, size=26, dark=True):
    """network waterfall rows: (kw|time, label, start_frac, end_frac, colour, grow_secs)"""
    tc = WHITE if dark else INK
    for i, (kw, lab, a, b, col, d) in enumerate(items):
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        y = y0 + i * gap
        p = c.P(t, 0.25); c.sfx(t, 'tick')
        c.pen.text(x0, y, lab, 'mono', size, mix(DARK if dark else PAPER, tc, p), 'lm')
        xa = x0 + lab_w + (x1 - x0 - lab_w) * a
        xb = x0 + lab_w + (x1 - x0 - lab_w) * b
        q = lin(c.t, t, t + d)
        if q > 0: c.pen.rect(xa, y - h / 2, xa + (xb - xa) * q, y + h / 2, fill=col, outline=INK if not dark else None, w=3 if not dark else 0)


def grid(c, x0, y0, colw, rows, rowh=96, size=30, head_fill=INK):
    """table: rows = [(kw|time, [cells])]; first row is the header. cell 'ok'/'no' draws a mark."""
    W_ = sum(colw)
    for r, (kw, cells) in enumerate(rows):
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        y = y0 + r * rowh; s = c.P(t, 0.3); c.sfx(t, 'pop')
        fill = head_fill if r == 0 else WHITE
        c.pen.rect(x0 + 6, y + 6, x0 + W_ + 6, y + rowh + 6, fill=INK)
        c.pen.rect(x0, y, x0 + W_, y + rowh, fill=fill, outline=INK, w=4)
        x = x0
        for k, cell in enumerate(cells):
            cx = x + colw[k] / 2; cy = y + rowh / 2
            if k: c.pen.line([(x, y), (x, y + rowh)], INK, 3, False)
            if cell == 'ok': check(c.pen, cx, cy, 0.9, GRN, 9, c.P(t + 0.1, 0.3))
            elif cell == 'no': cross(c.pen, cx, cy, 0.8, RED, 9, c.P(t + 0.1, 0.3))
            elif cell:
                col = WHITE if r == 0 else INK
                k_ = 'intx' if (r == 0 or k == 0) else 'ints'
                sz = size
                while c.pen.tw(cell, k_, sz) > colw[k] - 20 and sz > 16: sz -= 1
                c.pen.text(cx, cy, cell, k_, sz, mix(fill, col, s))
            x += colw[k]


def post(c, x0, y, x1, label_, col=BLUE, hi=None, h=150, sub=None):
    """feed card (avatar + title + grey line)"""
    if hi: c.pen.rr(x0 - 8, y - 8, x1 + 8, y + h + 8, 18, fill=hi)
    c.pen.rr(x0, y, x1, y + h, 14, fill=WHITE, outline=INK, w=3)
    c.pen.circ(x0 + 50, y + h / 2, 30, fill=col, outline=INK, w=3)
    c.pen.text(x0 + 100, y + h / 2 - 22, label_, 'intx', 30, INK, 'lm')
    c.pen.rr(x0 + 100, y + h / 2 + 12, x1 - 40, y + h / 2 + 30, 8, fill=LIGHT)
    if sub: c.pen.text(x1 - 20, y + h / 2 - 22, sub, 'int', 22, MUTE, 'rm')


def skel(c, x0, y0, x1, y1, r=10):
    """shimmering skeleton block"""
    c.pen.rr(x0, y0, x1, y1, r, fill=(226, 222, 213))
    w = x1 - x0
    sx = x0 + ((c.t * 600) % (w + 300)) - 150
    a, b = max(x0, sx - 60), min(x1, sx + 60)
    if b > a: c.pen.rr(a, y0, b, y1, min(r, (b - a) / 2), fill=(238, 235, 228))


def bubble(c, x, y, text, at, fill=WHITE, size=32, anchor_left=True, k='ints'):
    """speech bubble with tail, left/right aligned at x"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.35); c.sfx(at, 'pop')
    w = c.pen.tw(text, k, size) + 50; h = size * 1.9
    x0 = x if anchor_left else x - w
    c.pen.rr(x0 + 6, y - h / 2 + 6, x0 + w * s + 6, y + h / 2 + 6, 22, fill=INK)
    c.pen.rr(x0, y - h / 2, x0 + w * s, y + h / 2, 22, fill=fill, outline=INK, w=4)
    tx = x0 + 30 if anchor_left else x0 + w - 30 - c.pen.tw(text, k, size)
    if s > 0.8: c.pen.text(x0 + w / 2, y, text, k, size, INK)


def note(c, y, text, at, col=INK, size=36, k='intx'):
    """centred wrapped caption line(s)"""
    for i, ln in enumerate(wrap(c.pen, text, k, size, 900)):
        txt(c, 540, y + i * size * 1.3, ln, at, k, size, col)
