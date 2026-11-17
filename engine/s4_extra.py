"""Season 4 helpers (state management). Built only on engine.lib primitives; does not change shared code."""
from engine.lib import *


def at_(c, kw, n=1):
    return c.T(kw, n) if isinstance(kw, str) else kw


def head(c, text, kw, n=1, col=RED, size=80, y=330, angle=-4, sound='thud'):
    """rubber-stamp header synced to a word (Oswald: no arrows / ticks)"""
    at = at_(c, kw, n)
    if c.on(at - 0.01):
        stamp(c.cv, 540, y, text, size, c.P(at, 0.4), angle, col)
        if sound: c.sfx(at, sound)
    return at


def heart(pen, cx, cy, s, fill, outline=INK, w=4):
    pts = []
    for i in range(48):
        a = 2 * math.pi * i / 48
        x = 16 * math.sin(a) ** 3
        y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
        pts.append((cx + x * s, cy + y * s))
    pen.poly(pts, fill, outline, w)


def phone_frame(c, cx, cy, w=440, h=820, dy=0, url=None):
    cy += dy
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    card(c.pen, x0, y0, x1, y1, 50, INK, 12, 5)
    c.pen.rr(x0 + 18, y0 + 18, x1 - 18, y1 - 18, 36, fill=WHITE)
    c.pen.rr(cx - 50, y0 + 30, cx + 50, y0 + 50, 10, fill=INK)
    if url:
        c.pen.rr(x0 + 40, y0 + 66, x1 - 40, y0 + 112, 23, fill=(236, 233, 226))
        c.pen.text(cx, y0 + 89, url, 'intm', 22, MUTE)
        return (x0 + 18, y0 + 124, x1 - 18, y1 - 18)
    return (x0 + 18, y0 + 66, x1 - 18, y1 - 18)


MENU = [('Chicken Biryani', 249), ('Paneer Tikka', 199), ('Gulab Jamun', 89)]


def foodphone(c, cx, cy, qty, w=520, h=840, dy=0, title_='Biryani House', items=MENU, cart_p=None, tap=None, url='food app', bill=None):
    """food-delivery phone mock. qty: list of ints per item. cart_p: 0..1 slide-in of the cart bar (None = auto from qty).
    tap: (item_idx, t) draws a tap ripple. Returns list of button boxes."""
    ib = phone_frame(c, cx, cy, w, h, dy, url)
    x0, y0, x1, y1 = ib
    c.pen.text(x0 + 30, y0 + 40, title_, 'intx', 34, INK, 'lm')
    c.pen.text(x0 + 30, y0 + 84, '4.4 ★ · 30 min', 'intm', 22, MUTE, 'lm')
    boxes = []
    for i, (nm, pr) in enumerate(items):
        y = y0 + 170 + i * 150
        c.pen.rr(x0 + 22, y - 44, x0 + 102, y + 44, 16, fill=(250, 228, 200) if i != 1 else (235, 240, 210))
        c.pen.text(x0 + 118, y - 18, nm, 'int', 24, INK, 'lm')
        c.pen.text(x0 + 118, y + 22, f'₹{pr}', 'intm', 22, MUTE, 'lm')
        bx0, bx1 = x1 - 134, x1 - 20
        boxes.append((bx0, y - 30, bx1, y + 30))
        q = qty[i] if i < len(qty) else 0
        if q == 0:
            c.pen.rr(bx0, y - 30, bx1, y + 30, 12, fill=WHITE, outline=GRN, w=3)
            c.pen.text((bx0 + bx1) / 2, y, 'ADD', 'int', 26, GRN)
        else:
            c.pen.rr(bx0, y - 30, bx1, y + 30, 12, fill=GRN)
            c.pen.text(bx0 + 22, y, '−', 'int', 30, WHITE)
            c.pen.text((bx0 + bx1) / 2, y, str(q), 'int', 28, WHITE)
            c.pen.text(bx1 - 22, y, '+', 'int', 30, WHITE)
        if tap and tap[0] == i and tap[1] <= c.t < tap[1] + 0.6:
            q_ = lin(c.t, tap[1], tap[1] + 0.6)
            c.pen.circ((bx0 + bx1) / 2, y, 20 + 50 * q_, outline=mix(INK, WHITE, q_), w=5)
    n = sum(qty); total = sum(q * p for q, (_, p) in zip(qty, items))
    if bill is not None: total = bill
    p = cart_p if cart_p is not None else (1.0 if n else 0.0)
    if p > 0:
        by = y1 - 20 - 90 * eo(p)
        c.pen.rr(x0 + 20, by, x1 - 20, by + 80, 18, fill=GRN)
        c.pen.text(x0 + 46, by + 40, f'{n} item{"s" if n != 1 else ""} | ₹{total}', 'int', 26, WHITE, 'lm')
        c.pen.text(x1 - 46, by + 40, 'View Cart', 'int', 26, WHITE, 'rm')
    return boxes


def objcard(c, x0, y0, x1, lines, at, fname='state', size=30, marks=(), step=0.1, dy=None):
    """dark code card sized to its lines (JS-highlighted)"""
    h = 72 + len(lines) * size * 1.8 + 24
    return code(c, x0, y0, x1, y0 + h, lines, at, step, size, fname, marks, None, (), 'js', dy)


def flash_box(c, box, at, col=YEL, dur=1.0):
    if at <= c.t < at + dur:
        q = 1 - lin(c.t, at, at + dur)
        c.pen.rr(box[0] - 8, box[1] - 8, box[2] + 8, box[3] + 8, 14, outline=mix(PAPER, col, q), w=8)


def bullets(c, x0, y0, items, gap=96, size=40, dot=YEL, maxw=860):
    """items: (kw|time, text). simple slide-in list with yellow dots"""
    y = y0
    for kw, s_ in items:
        t = at_(c, kw)
        lines = wrap(c.pen, s_, 'ints', size, maxw)
        if c.on(t - 0.01):
            c.sfx(t, 'pop'); p = c.B(t, 0.3)
            c.pen.circ(x0 + 14, y, 14 * p, fill=dot, outline=INK, w=3)
            for k, ln in enumerate(lines):
                txt(c, x0 + 50, y + k * size * 1.25, ln, t, 'ints', size, INK, 'lm', 'slide')
        y += gap + (len(lines) - 1) * size * 1.25


def boxrow(c, cx, cy, labels, at, w=200, h=110, gap=30, fills=None, size=30, step=0.15):
    """a row of labelled boxes centred at cx; returns boxes"""
    n = len(labels); tot = n * w + (n - 1) * gap; out = []
    for i, lab in enumerate(labels):
        x = cx - tot / 2 + i * (w + gap) + w / 2
        f = fills[i] if fills else WHITE
        out.append(node(c, x, cy, w, h, lab, at + i * step, fill=f, size=size))
    return out


def season_map(c, names, at, cols=6, y0=360, final_label='FINALE', step=0.05):
    n = len(names); rows_ = (n + cols - 1) // cols
    cw = 940 / cols
    for i, nm in enumerate(names):
        x = 70 + cw * (i % cols) + cw / 2; y = y0 + (i // cols) * 96
        t = at + i * step
        if not c.on(t): continue
        c.sfx(t, 'tick'); s = c.B(t, 0.3)
        c.pen.rr(x - (cw / 2 - 6) * s, y - 42 * s, x + (cw / 2 - 6) * s, y + 42 * s, 10, fill=YEL if nm == final_label else WHITE, outline=INK, w=3)
        c.pen.text(x, y - 15 * s, f'E{i + 1:02d}', 'int', 18 * s, MUTE)
        c.pen.text(x, y + 13 * s, nm, 'int', 19 * s, INK)
    return y0 + rows_ * 96
