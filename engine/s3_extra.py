"""Season 3 helpers (web performance). Built only on engine.lib primitives; does not change shared code."""
from engine.lib import *


def at_(c, kw, n=1):
    return c.T(kw, n) if isinstance(kw, str) else kw


def head(c, text, kw, n=1, col=RED, size=80, y=330, angle=-4, sound='thud'):
    """rubber-stamp header synced to a word"""
    at = at_(c, kw, n)
    if c.on(at - 0.01):
        stamp(c.cv, 540, y, text, size, c.P(at, 0.4), angle, col)
        if sound: c.sfx(at, sound)


def gauge(c, cx, cy, r, frac, at, name='', value='', bands=(0.42, 0.72), w=36, vcol=None):
    """semicircle dial (green / orange / red) with a needle sweeping to frac"""
    if not c.on(at - 0.01): return
    s = c.B(at, 0.45); c.sfx(at, 'pop')
    rr = r * s
    for a, b, col in ((0, bands[0], GRN), (bands[0], bands[1], ORANGE), (bands[1], 1, RED)):
        c.pen.arc(cx - rr, cy - rr, cx + rr, cy + rr, 180 + 180 * a, 180 + 180 * b, col, w)
    q = c.P(at + 0.3, 0.8)
    ang = math.radians(180 + 180 * frac * q)
    c.pen.line([(cx, cy), (cx + math.cos(ang) * rr * 0.8, cy + math.sin(ang) * rr * 0.8)], INK, 9)
    c.pen.circ(cx, cy, 16 * s, fill=INK)
    if name: c.pen.text(cx, cy + 60 * s, name, 'osw', 56 * s, INK)
    if value and c.on(at + 0.6):
        col = vcol or (GRN if frac < bands[0] else ORANGE if frac < bands[1] else RED)
        c.pen.text(cx, cy + 125 * s, value, 'intx', 40 * c.B(at + 0.6, 0.3), col)


def rows(c, x0, y0, items, gap=140, w=880, h=110, size=40, sub_size=28):
    """items: (kw|time, text, sub, mark) ; mark in ('ok','no',None) or a colour for the dot"""
    for i, it in enumerate(items):
        kw, text, sub, mark = (list(it) + [None] * 4)[:4]
        at = at_(c, kw)
        y = y0 + i * gap
        if not c.on(at - 0.01): continue
        s = c.B(at, 0.35); c.sfx(at, 'pop')
        card(c.pen, x0, y - h / 2 * s, x0 + w, y + h / 2 * s, 20, WHITE, 8, 4)
        tx = x0 + 40
        if mark == 'ok': check(c.pen, x0 + 60, y, 1.0 * s, GRN, 10, c.P(at + 0.15, 0.3)); tx = x0 + 110
        elif mark == 'no': cross(c.pen, x0 + 60, y, 1.0 * s, RED, 10, c.P(at + 0.15, 0.3)); tx = x0 + 110
        elif isinstance(mark, tuple): c.pen.circ(x0 + 60, y, 24 * s, fill=mark, outline=INK, w=4); tx = x0 + 110
        if sub:
            c.pen.text(tx, y - 20, text, 'intx', size * s, INK, 'lm')
            c.pen.text(tx, y + 26, sub, 'intm', sub_size * s, MUTE, 'lm')
        else:
            c.pen.text(tx, y, text, 'intx', size * s, INK, 'lm')


def versus(c, left, right, y0=430, y1=1060, size=38):
    """left/right = (title, colour, at, [(kw|time, line), ...])"""
    for j, (ttl, col, at, lines) in enumerate((left, right)):
        if not c.on(at - 0.01): continue
        x0 = 70 + j * 480; x1 = x0 + 460
        dy = (1 - c.P(at, 0.45)) * 900; c.sfx(at, 'whoosh')
        card(c.pen, x0, y0 + dy, x1, y1 + dy, 26, WHITE, 10, 5)
        c.pen.rr(x0, y0 + dy, x1, y0 + 100 + dy, 26, fill=col, outline=INK, w=5)
        c.pen.rect(x0 + 3, y0 + 60 + dy, x1 - 3, y0 + 98 + dy, fill=col)
        c.pen.line([(x0 + 3, y0 + 100 + dy), (x1 - 3, y0 + 100 + dy)], INK, 5, False)
        c.pen.text((x0 + x1) / 2, y0 + 52 + dy, ttl, 'osw', 50, WHITE if col in (RED, GRN, BLUE, PURPLE, INK, TEAL) else INK)
        y = y0 + 160 + dy
        for kw, ln in lines:
            t = at_(c, kw)
            for k, part in enumerate(wrap(c.pen, ln, 'ints', size, 400)):
                txt(c, x0 + 30, y, part, t, 'ints', size, INK, 'lm', 'slide')
                y += size * 1.3
            y += 22


def axis(c, x0, x1, y, at, ticks, labels_up=True):
    """horizontal time axis; ticks: (frac, label, kw|time, colour)"""
    if not c.on(at - 0.01): return
    p = c.P(at, 0.5)
    c.pen.line([(x0, y), (x0 + (x1 - x0) * p, y)], INK, 6)
    for i, (f, lab, kw, col) in enumerate(ticks):
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        x = x0 + (x1 - x0) * f; s = c.B(t, 0.35); c.sfx(t, 'tick')
        c.pen.circ(x, y, 20 * s, fill=col, outline=INK, w=4)
        up = (i % 2 == 0) if labels_up is None else labels_up
        yy = y - 70 if up else y + 70
        c.pen.text(x, yy, lab, 'intx', 34 * s, INK)


def bars(c, x0, y0, items, maxv, w=620, h=70, gap=120, fmt='{}', lab_w=230, size=32):
    """horizontal bars: (label, value, colour, kw|time)"""
    for i, (lab, v, col, kw) in enumerate(items):
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        y = y0 + i * gap; p = c.P(t, 0.6); c.sfx(t, 'pop')
        c.pen.text(x0 + lab_w - 20, y + h / 2, lab, 'int', size, INK, 'rm')
        xb = x0 + lab_w + w * v / maxv * p
        c.pen.rect(x0 + lab_w + 6, y + 8, xb + 6, y + h + 8, fill=INK)
        c.pen.rect(x0 + lab_w, y, xb, y + h, fill=col, outline=INK, w=4)
        if p > 0.9: c.pen.text(xb + 20, y + h / 2, fmt.format(v), 'intx', size, INK, 'lm')


def phone(c, cx, cy, w=420, h=760, at=-1, dy=0, url=None):
    """phone frame, returns inner box"""
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


def spinner(c, cx, cy, r=40, col=INK):
    a = (c.t * 360 * 1.2) % 360
    c.pen.arc(cx - r, cy - r, cx + r, cy + r, a, a + 270, col, 9)


def kv(c, x0, y0, x1, items, size=30, gap=60):
    """devtools-style key: value lines; items (kw|time, key, value, colour)"""
    for i, (kw, k, v, col) in enumerate(items):
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        c.sfx(t, 'tick'); p = c.P(t, 0.25); y = y0 + i * gap
        c.pen.text(x0 + (1 - p) * 20, y, k, 'monob', size, mix(DARK, (150, 160, 175), p), 'lm')
        c.pen.text(x0 + c.pen.tw(k + ' ', 'monob', size) + (1 - p) * 20, y, v, 'monob', size, mix(DARK, col or WHITE, p), 'lm')


def netrows(c, x0, y0, x1, items, size=26, gap=58, cols=None):
    """network-table rows inside a dark panel: (kw|time, name, [col2, col3...], hilite)"""
    for i, it in enumerate(items):
        kw, name, extra = it[0], it[1], it[2]
        hi = it[3] if len(it) > 3 else None
        t = at_(c, kw)
        if not c.on(t - 0.01): continue
        y = y0 + i * gap; p = c.P(t, 0.25); c.sfx(t, 'tick')
        if hi: c.pen.rect(x0 - 10, y - gap / 2 + 4, x1 + 10, y + gap / 2 - 4, fill=mix(DARK, hi, 0.35 * p))
        c.pen.text(x0, y, name, 'mono', size, mix(DARK, WHITE, p), 'lm')
        xs = cols or [x1 - 170 * (len(extra) - k) for k in range(len(extra))]
        for k, e in enumerate(extra):
            c.pen.text(xs[k], y, e, 'mono', size, mix(DARK, (200, 205, 215), p), 'lm')


def season_map(c, names, at, cols=6, y0=360, final_label='FINALE', step=0.05):
    """grid of episode tiles for the finale"""
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
