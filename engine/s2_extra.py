"""Season 2 shared drawings: phones/pages, filmstrips, timeline rows, trade-off lists."""
from engine.lib import *


def phone(c, cx, cy, w, h, dy=0):
    """phone frame, returns screen box"""
    cy += dy
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    card(c.pen, x0, y0, x1, y1, 46, DARK, 12, 5)
    c.pen.rr(cx - 40, y0 + 18, cx + 40, y0 + 30, 6, fill=(60, 64, 72))
    return (x0 + 18, y0 + 44, x1 - 18, y1 - 26)


def fill_page(c, box, state, accent=BLUE, p=1.0):
    """state: white | spinner | skeleton | full | shell"""
    x0, y0, x1, y1 = box
    c.pen.rect(x0, y0, x1, y1, fill=WHITE)
    w, h = x1 - x0, y1 - y0
    if state == 'white': return
    if state == 'spinner':
        cx, cy, r = (x0 + x1) / 2, (y0 + y1) / 2, min(w, h) * 0.09
        a = (c.t * 400) % 360
        c.pen.arc(cx - r, cy - r, cx + r, cy + r, a, a + 270, accent, max(3, r * 0.22)); return
    sk = state in ('skeleton', 'shell')
    c.pen.rect(x0, y0, x1, y0 + h * 0.08, fill=LIGHT if state == 'skeleton' else INK)
    if state == 'shell':
        c.pen.rect(x0 + w * 0.05, y0 + h * 0.025, x0 + w * 0.3, y0 + h * 0.055, fill=YEL)
    hero = (x0 + w * 0.06, y0 + h * 0.12, x1 - w * 0.06, y0 + h * 0.38)
    c.pen.rr(*hero, 10, fill=LIGHT if sk else mix(WHITE, accent, 0.75 * p))
    for k in range(2):
        yy = y0 + h * (0.43 + k * 0.05)
        c.pen.rr(x0 + w * 0.06, yy, x0 + w * (0.8 - 0.25 * k), yy + h * 0.028, 6, fill=LIGHT if sk else INK)
    for i in range(4):
        gx = x0 + w * (0.06 + (i % 2) * 0.46); gy = y0 + h * (0.58 + (i // 2) * 0.2)
        c.pen.rr(gx, gy, gx + w * 0.42, gy + h * 0.17, 8, fill=LIGHT if sk else (236, 240, 248))
        if not sk:
            c.pen.rr(gx + w * 0.04, gy + h * 0.11, gx + w * 0.2, gy + h * 0.145, 5, fill=YEL)


def filmstrip(c, x0, y, label_, states, at, step=0.18, fw=140, fh=230, gap=16, mark=None):
    """row of thumbnail frames that appear one by one; mark = index to outline in yellow (at time mark[1])"""
    if not c.on(at - 0.01): return
    c.pen.text(x0, y - 34, label_, 'int', 28, WHITE, 'lm')
    for i, st in enumerate(states):
        t = at + i * step
        if not c.on(t): continue
        x = x0 + i * (fw + gap); s = c.P(t, 0.25)
        c.sfx(t, 'tick')
        fill_page(c, (x, y, x + fw, y + fh * s), st if s > 0.95 else 'white')
        c.pen.text(x + fw / 2, y + fh + 26, f'{(i + 1) * 0.5:.1f}s', 'mono', 22, (150, 156, 166))
        if mark and mark[0] == i and c.on(mark[1]):
            q = c.P(mark[1], 0.3)
            c.pen.rr(x - 8, y - 8, x + fw + 8, y + fh + 8, 10, outline=mix(DARK, YEL, q), w=6)


def seg_row(c, x0, y, x1, segs, h=70, size=26):
    """segs: list of (label, a_frac, b_frac, color, at) - each bar grows from a to b"""
    for (lab, a, b, col, at) in segs:
        if not c.on(at - 0.01): continue
        p = c.P(at, 0.45)
        xa = x0 + (x1 - x0) * a; xb = xa + (x1 - x0) * (b - a) * p
        c.pen.rect(xa, y, xb, y + h, fill=col, outline=INK, w=3)
        if p > 0.8 and lab:
            c.pen.text((xa + xb) / 2, y + h / 2, lab, 'int', size, WHITE if col in (BLUE, PURPLE, RED, GRN, INK, TEAL) else INK)


def marker(c, x, y0, y1, text, at, col=GRN):
    if not c.on(at - 0.01): return
    p = c.P(at, 0.35); c.sfx(at, 'pop')
    c.pen.line([(x, y0), (x, y0 + (y1 - y0) * p)], col, 5, False)
    pill(c.pen, x, y0 - 30, text, c.B(at, 0.35), col, WHITE, 26, outline=INK)


def proscons(c, x0, y0, x1, items, size=34, gap=78):
    """items: list of (good:bool, text, at)"""
    for i, (good, s_, at) in enumerate(items):
        if not c.on(at - 0.01): continue
        y = y0 + i * gap; p = c.P(at, 0.3); c.sfx(at, 'pop')
        c.pen.circ(x0 + 26, y, 26 * c.B(at, 0.3), fill=GRN if good else RED, outline=INK, w=3)
        c.pen.text(x0 + 26, y, '+' if good else '–', 'int', 36, WHITE)
        c.pen.text(x0 + 74 + (1 - p) * 30, y, s_, 'ints', size, mix(PAPER, INK, p), 'lm')


def trap(c, kw='Interview'):
    at = c.T(kw)
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(at, 0.4), -4, RED); c.sfx(at, 'thud')
    return at


def qtext(c, s_, y, at, size=50, maxw=900, col=INK):
    for i, ln in enumerate(wrap(c.pen, s_, 'intx', size, maxw)):
        txt(c, 540, y + i * size * 1.3, ln, at + i * 0.1, 'intx', size, col)


def verdict(c, x, y, ok, at, s=2.2):
    if not c.on(at - 0.01): return
    c.sfx(at, 'ding' if ok else 'buzz')
    (check if ok else cross)(c.pen, x, y, s, GRN if ok else RED, 14, c.P(at, 0.4))


def htmlcard(c, x0, y0, x1, lines, at, fname='view-source', size=30, marks=(), circles=(), step=0.1):
    """plain (un-highlighted) code card for HTML/headers/payloads"""
    h = 72 + len(lines) * size * 1.8 + 30
    return code(c, x0, y0, x1, y0 + h, lines, at, step, size, fname, marks, None, circles, lang='html')
