"""Shorts mode: 20-35 s trend reels for reach. Same engine, different chrome (no episode pill, big captions,
TECH, EXPLAINED wordmark) and episodes live in shorts/shNN.py.
Usage: python3 -m engine.shorts {text|check|render} SH01 [SH02 ...]
Scene rules for reach: the hook is ON SCREEN AT t=0 (never wait for a word), a new visual every 2-3 s,
one comment/share prompt, fox follow card in the last scene."""
import importlib, os, sys
from PIL import Image
import engine.build as B
from engine.lib import *

def load(epid):
    m = importlib.import_module('shorts.' + epid.lower())
    return m.EP, m.SCENES

def captions(pen, t, chunks, size0=60, ymid=1590):
    for st, en, ch in chunks:
        if not (st <= t < en): continue
        size, gap = size0, 18
        ws = [pen.tw(w[0], 'intx', size) for w in ch]
        lines = [list(range(len(ch)))]
        if sum(ws) + gap * (len(ch) - 1) > 860 and len(ch) > 1:
            m = (len(ch) + 1) // 2; lines = [list(range(m)), list(range(m, len(ch)))]
        lw = [sum(ws[i] for i in L) + gap * (len(L) - 1) for L in lines]
        if max(lw) > 940:
            size = int(size * 940 / max(lw)); ws = [pen.tw(w[0], 'intx', size) for w in ch]
            lw = [sum(ws[i] for i in L) + gap * (len(L) - 1) for L in lines]
        lh = size * 1.45; bh = lh * len(lines) + 30; bw = max(lw) + 70
        y0 = ymid - bh / 2 + (1 - eo(lin(t, st, st + 0.12))) * 16
        pen.rr(540 - bw / 2 + 8, y0 + 9, 540 + bw / 2 + 8, y0 + bh + 9, 24, fill=INK)
        pen.rr(540 - bw / 2, y0, 540 + bw / 2, y0 + bh, 24, fill=WHITE, outline=INK, w=5)
        active = max([j for j, w in enumerate(ch) if w[1] - 0.05 <= t] or [None], key=lambda v: -1 if v is None else v)
        for li, L in enumerate(lines):
            x = 540 - lw[li] / 2; y = y0 + 15 + lh * li + lh / 2
            for i in L:
                if i == active: pen.rr(x - 9, y - size * 0.62, x + ws[i] + 9, y + size * 0.62, 12, fill=YEL)
                pen.text(x, y, ch[i][0], 'intx', size, INK, 'lm')
                x += ws[i] + gap
        return

def chrome(img, t, ep, total, chunks):
    pen = Pen(img, 1)
    tw = pen.tw('TECH, EXPLAINED', 'osw', 36)
    pen.rect(540 - tw / 2, 150, 540 + tw / 2, 158, fill=YEL)
    pen.text(540, 134, 'TECH, EXPLAINED', 'osw', 36, INK)
    pen.rect(0, 1910, W * t / total, 1920, fill=RED)
    captions(pen, t, chunks)

B.load = load
B.chrome = chrome

# ---------------------------------------------------------------- shared scene helpers for shorts
_FOX = None
def fox_img():
    global _FOX
    if _FOX is None:
        from publish.make_covers import fox_img as _f
        _FOX = _f(1080)
    return _FOX

def paste(c, im, cx, cy, w):
    if w < 4: return
    s = im.resize((int(w * SS), int(w * SS * im.height / im.width)), Image.LANCZOS)
    c.cv.alpha_composite(s, (int(cx * SS - s.width / 2), int(cy * SS - s.height / 2)))

def fox_cta(c, at, line='FOLLOW @tech.explained.dev', y=900):
    """big fox + follow pill: last scene of every short"""
    if not c.on(at - 0.01): return
    c.sfx(at, 'pop'); p = c.B(at, 0.45)
    c.pen.circ(540, y, 250 * p, fill=YEL, outline=INK, w=6)
    paste(c, fox_img(), 540, y + 10 * p, 560 * p)
    if c.on(at + 0.3):
        pill(c.pen, 540, y + 330, line, c.B(at + 0.3, 0.35), INK, WHITE, 40, outline=None)

def hook(c, lines, y=520, size=150, at=-0.4, hlcol=YEL, step=0.0):
    """headline visible from frame 1 (at=0)"""
    for i, l in enumerate(lines):
        title(c, l, y + i * size * 1.05, at + i * step, size, INK, hlcol, d=0.3, sound='thud' if i == 0 else 'pop')

def repo_card(c, y, num, name, desc, at, stars=None, tag=None):
    if not c.on(at - 0.01): return
    p = c.B(at, 0.4); c.sfx(at, 'pop')
    dx = (1 - c.P(at, 0.35)) * 80
    card(c.pen, 70 + dx, y - 130, 1010 + dx, y + 130, 28, WHITE, 12, 5)
    c.pen.circ(150 + dx, y - 52, 46, fill=YEL, outline=INK, w=4)
    c.pen.text(150 + dx, y - 52, str(num), 'osw', 58 * p, INK)
    ns = min(40, 40 * 560 / max(1, c.pen.tw(name, 'monob', 40)))
    c.pen.text(220 + dx, y - 58, name, 'monob', ns, INK, 'lm')
    for i, ln in enumerate(wrap(c.pen, desc, 'ints', 34, 820)[:2]):
        c.pen.text(110 + dx, y + 18 + i * 46, ln, 'ints', 34, MUTE, 'lm')
    if stars: pill(c.pen, 850 + dx, y - 100, stars + ' stars', p, YEL, INK, 28)
    if tag: pill(c.pen, 800 + dx, y - 160, tag, p, RED, WHITE, 28, outline=None)

if __name__ == '__main__':
    cmd, ids = sys.argv[1], sys.argv[2:]
    for epid in ids:
        if cmd == 'text': print(B.parse(load(epid)[1])[2]); print('---')
        elif cmd == 'check': B.cmd_check(epid)
        elif cmd == 'render': B.cmd_render(epid)

# ---------------------------------------------------------------- fast-cut camera (shorts only)
def frame(t, si, spans, scenes, W_, ep, total, chunks, sfxset):
    """every cut: punch-in zoom 1.14 -> 1.0 in 0.2 s, a short shake, and a 1-frame white flash"""
    t0, t1 = spans[si]
    cv = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    words = [(w[0], w[1] - t0, w[2] - t0) for w in W_ if w[3] == si]
    c = Ctx(Pen(cv, SS), cv, t - t0, words, t1 - t0, sfxset, t0)
    scenes[si][0](c)
    lt = t - t0
    z = 1 + 0.14 * (1 - eo(lin(lt, 0, 0.2))) + 0.04 * lin(lt, 0.2, max(0.3, t1 - t0))
    sh = 14 * (1 - lin(lt, 0, 0.18)) * SS
    dx, dy = sh * math.sin(lt * 90), sh * math.cos(lt * 70)
    cw, ch = CW / z, CH / z
    x0 = min(max(0, (CW - cw) / 2 + dx), CW - cw); y0 = min(max(0, (CH - ch) / 2 + dy), CH - ch)
    lay = cv.resize((W, H), Image.BOX, box=(x0, y0, x0 + cw, y0 + ch))
    fr = B.papers()[int(t * FPS / 3) % 3].copy(); fr.alpha_composite(lay)
    chrome(fr, t, ep, total, chunks)
    if si > 0 and lt < 1.5 / FPS:
        fr = Image.blend(fr, Image.new('RGBA', fr.size, (255, 255, 255, 255)), 0.55)
    return fr.convert('RGB')

B.frame = frame
