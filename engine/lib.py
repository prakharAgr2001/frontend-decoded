"""Frontend Decoded visual library. Scenes call these with a Ctx (c). Coordinates are 1080x1920 units."""
import math, os, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS, SS = 1080, 1920, 30, 2
CW, CH = W * SS, H * SS

PAPER = (244, 241, 234); INK = (22, 24, 29); YEL = (255, 210, 63); RED = (230, 57, 70)
BLUE = (43, 89, 195); GRN = (40, 150, 85); DARK = (17, 20, 24); MUTE = (128, 124, 116)
WHITE = (255, 255, 255); ORANGE = (235, 125, 55); GREY = (196, 191, 182); PURPLE = (124, 77, 214)
LIGHT = (232, 228, 219); TEAL = (32, 150, 160); PINK = (255, 122, 178); CYAN = (122, 215, 240)
KW, FN, PU, CM, NU, STR = PINK, CYAN, (232, 232, 232), (120, 128, 140), (250, 190, 110), (160, 220, 130)

FP = {'osw': 'Oswald.ttf', 'int': 'Inter-Bold.otf', 'ints': 'Inter-SemiBold.otf', 'intm': 'Inter-Medium.otf',
      'intx': 'InterDisplay-ExtraBold.otf', 'mono': 'JetBrainsMono-Medium.ttf', 'monob': 'JetBrainsMono-Bold.ttf'}
_fc = {}
def font(k, size):
    size = max(1, int(size)); key = (k, size)
    if key not in _fc:
        f = ImageFont.truetype(os.path.join(ROOT, 'fonts', FP[k]), size)
        if k == 'osw': f.set_variation_by_name('Bold')
        _fc[key] = f
    return _fc[key]

# ---------------------------------------------------------------- easing
def cl(x, a=0.0, b=1.0): return max(a, min(b, x))
def lin(t, a, b): return cl((t - a) / (b - a)) if b > a else float(t >= a)
def eo(x): return 1 - (1 - x) ** 3
def eio(x): return x * x * (3 - 2 * x)
def back(x):
    if x <= 0: return 0.0
    c = 1.9; y = x - 1
    return 1 + (c + 1) * y ** 3 + c * y ** 2
def mix(c1, c2, a): a = cl(a); return tuple(int(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))

# ---------------------------------------------------------------- pen
class Pen:
    def __init__(self, img, s):
        self.img, self.d, self.s = img, ImageDraw.Draw(img), s
    def _p(self, *v): return [int(round(x * self.s)) for x in v]
    def _w(self, w): return max(1, int(round(w * self.s))) if w else 0
    def rr(self, x0, y0, x1, y1, r, fill=None, outline=None, w=0):
        if x1 - x0 < 1 or y1 - y0 < 1: return
        r = max(0, min(r, (x1 - x0) / 2, (y1 - y0) / 2))
        self.d.rounded_rectangle(self._p(x0, y0, x1, y1), radius=int(r * self.s), fill=fill, outline=outline, width=self._w(w))
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, w=0):
        if x1 - x0 < 0.5 or y1 - y0 < 0.5: return
        self.d.rectangle(self._p(x0, y0, x1, y1), fill=fill, outline=outline, width=self._w(w))
    def ell(self, x0, y0, x1, y1, fill=None, outline=None, w=0):
        if x1 - x0 < 0.5: return
        self.d.ellipse(self._p(x0, y0, x1, y1), fill=fill, outline=outline, width=self._w(w))
    def circ(self, cx, cy, r, fill=None, outline=None, w=0): self.ell(cx - r, cy - r, cx + r, cy + r, fill, outline, w)
    def arc(self, x0, y0, x1, y1, a0, a1, fill, w):
        if a1 - a0 < 0.5: return
        self.d.arc(self._p(x0, y0, x1, y1), a0, a1, fill=fill, width=self._w(w))
    def line(self, pts, fill, w, caps=True):
        if w <= 0: return
        self.d.line([tuple(self._p(*p)) for p in pts], fill=fill, width=self._w(w), joint='curve')
        if caps:
            r = w / 2
            for p in (pts[0], pts[-1]): self.ell(p[0] - r, p[1] - r, p[0] + r, p[1] + r, fill=fill)
    def poly(self, pts, fill, outline=None, w=0):
        self.d.polygon([tuple(self._p(*p)) for p in pts], fill=fill, outline=outline, width=self._w(w))
    def text(self, x, y, s, k, size, fill, anchor='mm'):
        if size < 2 or not s: return
        self.d.text(tuple(self._p(x, y)), s, font=font(k, size * self.s), fill=fill, anchor=anchor)
    def tw(self, s, k, size): return font(k, max(2, size) * self.s).getlength(s) / self.s

# ---------------------------------------------------------------- context
def norm(w): return re.sub(r"[^a-z0-9']", '', w.lower().replace('’', "'"))

class Ctx:
    def __init__(self, pen, cv, t, words, dur, sfxset, gt0):
        self.pen, self.cv, self.t, self.words, self.dur, self._sfx, self.gt0 = pen, cv, t, words, dur, sfxset, gt0
    def T(self, w, n=1, off=0.0):
        """local start time of the n-th occurrence of word w in this scene's narration"""
        q = norm(w); k = 0
        for wd in self.words:
            if norm(wd[0]) == q:
                k += 1
                if k == n: return wd[1] + off
        k = 0
        for wd in self.words:
            if norm(wd[0]).startswith(q):
                k += 1
                if k == n: return wd[1] + off
        raise KeyError(f'word "{w}" (#{n}) not in scene: ' + ' '.join(x[0] for x in self.words))
    def E(self, w, n=1): return self._end(w, n)
    def _end(self, w, n):
        q = norm(w); k = 0
        for wd in self.words:
            if norm(wd[0]).startswith(q):
                k += 1
                if k == n: return wd[2]
        raise KeyError(w)
    def P(self, at, d=0.4, f=eo): return f(lin(self.t, at, at + d))
    def B(self, at, d=0.4): return back(lin(self.t, at, at + d))
    def on(self, at): return self.t >= at
    def sfx(self, at, kind):
        if self.t >= at - 0.5 / FPS: self._sfx.add((round(self.gt0 + at, 3), kind))

# ---------------------------------------------------------------- primitives
def card(pen, x0, y0, x1, y1, r=26, fill=WHITE, sh=12, ow=5, outline=INK):
    pen.rr(x0 + sh, y0 + sh, x1 + sh, y1 + sh, r, fill=INK)
    pen.rr(x0, y0, x1, y1, r, fill=fill, outline=outline, w=ow)

def darkcard(pen, x0, y0, x1, y1, r=26):
    pen.rr(x0 + 12, y0 + 12, x1 + 12, y1 + 12, r, fill=INK)
    pen.rr(x0, y0, x1, y1, r, fill=DARK, outline=INK, w=5)

def hl(pen, x0, y0, x1, y1, p, col=YEL):
    if p <= 0: return
    x = x0 + (x1 - x0) * p
    pen.poly([(x0, y0 + 6), (x, y0), (x + 6, (y0 + y1) / 2), (x, y1), (x0 + 4, y1 - 4)], fill=col)

def arrow(pen, x0, y0, x1, y1, p=1.0, col=INK, w=7, head=26, dash=False):
    if p <= 0: return
    xe, ye = x0 + (x1 - x0) * p, y0 + (y1 - y0) * p
    ang = math.atan2(ye - y0, xe - x0)
    bx, by = xe - math.cos(ang) * head * 0.8, ye - math.sin(ang) * head * 0.8
    if dash:
        L = math.hypot(bx - x0, by - y0); n = int(L // 26)
        for i in range(n):
            a0, a1 = i / max(1, n), (i + 0.55) / max(1, n)
            pen.line([(x0 + (bx - x0) * a0, y0 + (by - y0) * a0), (x0 + (bx - x0) * a1, y0 + (by - y0) * a1)], col, w)
    else:
        pen.line([(x0, y0), (bx, by)], col, w)
    if p > 0.12:
        a1, a2 = ang + 2.6, ang - 2.6
        pen.poly([(xe, ye), (xe + math.cos(a1) * head, ye + math.sin(a1) * head), (xe + math.cos(a2) * head, ye + math.sin(a2) * head)], fill=col)

def check(pen, cx, cy, s=1.0, col=GRN, w=10, p=1.0):
    pts = [(cx - 22 * s, cy), (cx - 6 * s, cy + 16 * s), (cx + 24 * s, cy - 18 * s)]
    if p <= 0: return
    if p < 0.5:
        q = p / 0.5; pen.line([pts[0], (pts[0][0] + (pts[1][0] - pts[0][0]) * q, pts[0][1] + (pts[1][1] - pts[0][1]) * q)], col, w)
    else:
        q = (p - 0.5) / 0.5; pen.line([pts[0], pts[1], (pts[1][0] + (pts[2][0] - pts[1][0]) * q, pts[1][1] + (pts[2][1] - pts[1][1]) * q)], col, w)

def cross(pen, cx, cy, s=1.0, col=RED, w=10, p=1.0):
    if p <= 0: return
    q1, q2 = cl(p * 2), cl(p * 2 - 1)
    pen.line([(cx - 20 * s, cy - 20 * s), (cx - 20 * s + 40 * s * q1, cy - 20 * s + 40 * s * q1)], col, w)
    if q2 > 0: pen.line([(cx + 20 * s, cy - 20 * s), (cx + 20 * s - 40 * s * q2, cy - 20 * s + 40 * s * q2)], col, w)

def person(pen, cx, feet, s, col):
    pen.ell(cx - 24 * s, feet - 150 * s, cx + 24 * s, feet - 102 * s, fill=col, outline=INK, w=4)
    pen.rr(cx - 34 * s, feet - 96 * s, cx + 34 * s, feet, 26 * s, fill=col, outline=INK, w=4)

def keycap(pen, cx, cy, ch, s, size=70, col=WHITE):
    if s <= 0: return
    h = size / 2 * s
    pen.rr(cx - h + 5, cy - h + 7, cx + h + 5, cy + h + 7, 12 * s, fill=INK)
    pen.rr(cx - h, cy - h, cx + h, cy + h, 12 * s, fill=col, outline=INK, w=4)
    pen.text(cx, cy, ch, 'intx', size * 0.5 * s, INK)

def pill(pen, cx, cy, text, s=1.0, fill=YEL, col=INK, size=30, k='int', outline=INK):
    if s <= 0: return
    w = pen.tw(text, k, size * s) + 44 * s
    pen.rr(cx - w / 2, cy - 28 * s, cx + w / 2, cy + 28 * s, 28 * s, fill=fill, outline=outline, w=4 if outline else 0)
    pen.text(cx, cy + 1, text, k, size * s, col)

def stamp(canvas, cx, cy, text, size, p, angle=-5, col=RED, k='osw'):
    if p <= 0: return
    sc = back(p)
    tmp = Pen(Image.new('RGBA', (8, 8)), SS)
    tw = tmp.tw(text, k, size * sc)
    w, h = tw + 70 * sc, size * sc * 1.45
    lay = Image.new('RGBA', (int((w + 40) * SS), int((h + 40) * SS)), (0, 0, 0, 0))
    lp = Pen(lay, SS)
    lp.rr(20, 20, 20 + w, 20 + h, 14 * sc, fill=None, outline=col, w=8 * sc)
    lp.text(20 + w / 2, 20 + h / 2 + size * sc * 0.03, text, k, size * sc, col)
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    canvas.alpha_composite(lay, (int(cx * SS - lay.width / 2), int(cy * SS - lay.height / 2)))

# ---------------------------------------------------------------- icons (simple vector, centered, ~100 units at s=1)
def icon(pen, name, cx, cy, s=1.0, col=INK, fill=WHITE):
    u = s
    if name == 'laptop':
        pen.rr(cx - 46 * u, cy - 36 * u, cx + 46 * u, cy + 22 * u, 8 * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 36 * u, cy - 27 * u, cx + 36 * u, cy + 13 * u, fill=(210, 225, 245))
        pen.rr(cx - 60 * u, cy + 22 * u, cx + 60 * u, cy + 34 * u, 5 * u, fill=col)
    elif name == 'phone':
        pen.rr(cx - 26 * u, cy - 46 * u, cx + 26 * u, cy + 46 * u, 10 * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 18 * u, cy - 34 * u, cx + 18 * u, cy + 30 * u, fill=(210, 225, 245))
    elif name == 'server':
        for i in range(3):
            y = cy - 42 * u + i * 30 * u
            pen.rr(cx - 44 * u, y, cx + 44 * u, y + 26 * u, 6 * u, fill=fill, outline=col, w=5)
            pen.circ(cx + 28 * u, y + 13 * u, 4 * u, fill=GRN)
            pen.line([(cx - 32 * u, y + 13 * u), (cx + 6 * u, y + 13 * u)], col, 4)
    elif name == 'globe':
        pen.circ(cx, cy, 44 * u, fill=fill, outline=col, w=5)
        pen.ell(cx - 18 * u, cy - 44 * u, cx + 18 * u, cy + 44 * u, outline=col, w=4)
        pen.line([(cx - 44 * u, cy), (cx + 44 * u, cy)], col, 4, False)
        pen.arc(cx - 40 * u, cy - 50 * u, cx + 40 * u, cy - 10 * u, 20, 160, col, 4)
        pen.arc(cx - 40 * u, cy + 10 * u, cx + 40 * u, cy + 50 * u, 200, 340, col, 4)
    elif name == 'lock':
        pen.arc(cx - 24 * u, cy - 50 * u, cx + 24 * u, cy, 180, 360, col, 8)
        pen.line([(cx - 24 * u, cy - 25 * u), (cx - 24 * u, cy - 6 * u)], col, 8, False)
        pen.line([(cx + 24 * u, cy - 25 * u), (cx + 24 * u, cy - 6 * u)], col, 8, False)
        pen.rr(cx - 38 * u, cy - 8 * u, cx + 38 * u, cy + 46 * u, 8 * u, fill=fill if fill != WHITE else YEL, outline=col, w=5)
        pen.circ(cx, cy + 16 * u, 7 * u, fill=col)
    elif name == 'doc':
        pen.poly([(cx - 34 * u, cy - 46 * u), (cx + 16 * u, cy - 46 * u), (cx + 34 * u, cy - 28 * u), (cx + 34 * u, cy + 46 * u), (cx - 34 * u, cy + 46 * u)], fill=fill, outline=col, w=5)
        for i in range(4):
            pen.line([(cx - 20 * u, cy - 18 * u + i * 16 * u), (cx + 20 * u, cy - 18 * u + i * 16 * u)], col, 4)
    elif name == 'db':
        pen.rect(cx - 40 * u, cy - 30 * u, cx + 40 * u, cy + 30 * u, fill=fill)
        pen.line([(cx - 40 * u, cy - 30 * u), (cx - 40 * u, cy + 30 * u)], col, 5, False)
        pen.line([(cx + 40 * u, cy - 30 * u), (cx + 40 * u, cy + 30 * u)], col, 5, False)
        pen.ell(cx - 40 * u, cy + 16 * u, cx + 40 * u, cy + 44 * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 37 * u, cy - 30 * u, cx + 37 * u, cy + 28 * u, fill=fill)
        pen.ell(cx - 40 * u, cy - 44 * u, cx + 40 * u, cy - 16 * u, fill=fill, outline=col, w=5)
    elif name == 'book':
        pen.rr(cx - 40 * u, cy - 46 * u, cx + 40 * u, cy + 46 * u, 6 * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 40 * u, cy - 46 * u, cx - 26 * u, cy + 46 * u, fill=col)
        pen.line([(cx - 12 * u, cy - 20 * u), (cx + 26 * u, cy - 20 * u)], col, 4)
        pen.line([(cx - 12 * u, cy - 4 * u), (cx + 26 * u, cy - 4 * u)], col, 4)
    elif name == 'clock':
        pen.circ(cx, cy, 44 * u, fill=fill, outline=col, w=5)
        pen.line([(cx, cy), (cx, cy - 28 * u)], col, 6)
        pen.line([(cx, cy), (cx + 20 * u, cy + 8 * u)], col, 6)
    elif name == 'cloud':
        for (dx, dy, r) in [(-26, 8, 26), (0, -10, 32), (28, 6, 26)]:
            pen.circ(cx + dx * u, cy + dy * u, r * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 26 * u, cy + 4 * u, cx + 28 * u, cy + 33 * u, fill=fill)
        pen.line([(cx - 30 * u, cy + 34 * u), (cx + 30 * u, cy + 34 * u)], col, 5)
    elif name == 'chef':
        pen.circ(cx, cy + 8 * u, 26 * u, fill=(250, 220, 190), outline=col, w=5)
        for dx in (-18, 0, 18): pen.circ(cx + dx * u, cy - 34 * u, 16 * u, fill=WHITE, outline=col, w=4)
        pen.rect(cx - 24 * u, cy - 30 * u, cx + 24 * u, cy - 16 * u, fill=WHITE, outline=col, w=4)
        pen.circ(cx - 9 * u, cy + 6 * u, 3 * u, fill=col); pen.circ(cx + 9 * u, cy + 6 * u, 3 * u, fill=col)
    elif name == 'bolt':
        pen.poly([(cx + 8 * u, cy - 48 * u), (cx - 28 * u, cy + 6 * u), (cx - 2 * u, cy + 6 * u), (cx - 10 * u, cy + 48 * u), (cx + 28 * u, cy - 8 * u), (cx + 2 * u, cy - 8 * u)], fill=YEL, outline=col, w=4)
    elif name == 'eye':
        pen.ell(cx - 46 * u, cy - 26 * u, cx + 46 * u, cy + 26 * u, fill=fill, outline=col, w=5)
        pen.circ(cx, cy, 16 * u, fill=col)
    elif name == 'cpu':
        pen.rr(cx - 34 * u, cy - 34 * u, cx + 34 * u, cy + 34 * u, 6 * u, fill=fill, outline=col, w=5)
        pen.rr(cx - 16 * u, cy - 16 * u, cx + 16 * u, cy + 16 * u, 3 * u, fill=col)
        for i in range(3):
            o = (-18 + i * 18) * u
            for (a, b, c2, d) in [(cx + o, cy - 34 * u, cx + o, cy - 46 * u), (cx + o, cy + 34 * u, cx + o, cy + 46 * u),
                                  (cx - 34 * u, cy + o, cx - 46 * u, cy + o), (cx + 34 * u, cy + o, cx + 46 * u, cy + o)]:
                pen.line([(a, b), (c2, d)], col, 4)
    elif name == 'gpu':
        pen.rr(cx - 50 * u, cy - 30 * u, cx + 50 * u, cy + 30 * u, 6 * u, fill=fill, outline=col, w=5)
        pen.circ(cx - 18 * u, cy, 18 * u, outline=col, w=4); pen.circ(cx + 22 * u, cy, 18 * u, outline=col, w=4)
    elif name == 'bin':
        pen.rr(cx - 32 * u, cy - 30 * u, cx + 32 * u, cy + 46 * u, 6 * u, fill=fill, outline=col, w=5)
        pen.rect(cx - 42 * u, cy - 42 * u, cx + 42 * u, cy - 32 * u, fill=col)
        for dx in (-14, 0, 14): pen.line([(cx + dx * u, cy - 18 * u), (cx + dx * u, cy + 34 * u)], col, 4)
    elif name == 'shield':
        pen.poly([(cx, cy - 48 * u), (cx + 40 * u, cy - 32 * u), (cx + 34 * u, cy + 18 * u), (cx, cy + 48 * u), (cx - 34 * u, cy + 18 * u), (cx - 40 * u, cy - 32 * u)], fill=fill, outline=col, w=5)
        check(pen, cx, cy, 0.8, GRN, 7)
    elif name == 'tower':
        pen.poly([(cx, cy - 46 * u), (cx + 30 * u, cy + 46 * u), (cx - 30 * u, cy + 46 * u)], fill=fill, outline=col, w=5)
        pen.arc(cx - 50 * u, cy - 70 * u, cx + 50 * u, cy - 10 * u, 220, 320, col, 4)
    else:
        pen.circ(cx, cy, 40 * u, fill=fill, outline=col, w=5)

# ---------------------------------------------------------------- composite components (use c)
def title(c, text, y, at, size=130, col=INK, hlcol=None, x=540, k='osw', d=0.45, sound='pop'):
    if not c.on(at - 0.01): return
    p = c.B(at, d)
    if sound: c.sfx(at, sound)
    if hlcol:
        w = c.pen.tw(text, k, size) / 2 + 30
        hl(c.pen, x - w, y - size * 0.45, x + w, y + size * 0.5, c.P(at + 0.1, 0.45), hlcol)
    c.pen.text(x, y, text, k, size * p, col)

def txt(c, x, y, s, at, k='int', size=40, col=INK, anchor='mm', anim='fade', d=0.35):
    if not c.on(at - 0.01): return
    if anim == 'pop':
        c.pen.text(x, y, s, k, size * c.B(at, d), col, anchor)
    elif anim == 'slide':
        p = c.P(at, d); c.pen.text(x + (1 - p) * 40, y, s, k, size, mix(PAPER, col, p), anchor)
    else:
        p = c.P(at, d); c.pen.text(x, y + (1 - p) * 16, s, k, size, mix(PAPER, col, p), anchor)

def label(c, cx, cy, text, at, fill=YEL, col=INK, size=30):
    if not c.on(at - 0.01): return
    c.sfx(at, 'pop'); pill(c.pen, cx, cy, text, c.B(at, 0.35), fill, col, size)

def node(c, cx, cy, w, h, text, at, ic=None, fill=WHITE, sub=None, col=INK, size=34, d=0.4, sound='pop'):
    """card with optional icon above text; returns box"""
    if not c.on(at - 0.01): return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    s = c.B(at, d)
    if sound: c.sfx(at, sound)
    ww, hh = w * s, h * s
    card(c.pen, cx - ww / 2, cy - hh / 2, cx + ww / 2, cy + hh / 2, 22 * s, fill, 10 * s, 5)
    if ic:
        icon(c.pen, ic, cx, cy - h * (0.2 if sub else 0.16) * s, 0.75 * s, col)
        c.pen.text(cx, cy + h * (0.17 if sub else 0.30) * s, text, 'int', size * s, col)
    else:
        c.pen.text(cx, cy - (12 * s if sub else 0), text, 'int', size * s, col)
    if sub: c.pen.text(cx, cy + (h * 0.36 if ic else 26) * s, sub, 'intm', 24 * s, MUTE)
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)

def edge_pt(box, tx, ty):
    x0, y0, x1, y1 = box; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0: return cx, cy
    sx = (x1 - x0) / 2 / abs(dx) if dx else 1e9; sy = (y1 - y0) / 2 / abs(dy) if dy else 1e9
    s = min(sx, sy) * 1.06
    return cx + dx * s, cy + dy * s

def link(c, a, b, at, d=0.45, col=INK, w=6, txt_=None, dash=False, off=0):
    """arrow between two boxes, optional label at middle"""
    if not c.on(at): return
    ac = ((a[0] + a[2]) / 2, (a[1] + a[3]) / 2); bc = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
    nx, ny = -(bc[1] - ac[1]), bc[0] - ac[0]; L = math.hypot(nx, ny) or 1
    ox, oy = nx / L * off, ny / L * off
    p0 = edge_pt(a, bc[0], bc[1]); p1 = edge_pt(b, ac[0], ac[1])
    arrow(c.pen, p0[0] + ox, p0[1] + oy, p1[0] + ox, p1[1] + oy, c.P(at, d), col, w, 24, dash)
    if txt_ and c.on(at + d * 0.6):
        mx, my = (p0[0] + p1[0]) / 2 + ox, (p0[1] + p1[1]) / 2 + oy
        pill(c.pen, mx, my, txt_, c.B(at + d * 0.6, 0.3), WHITE, INK, 24)

def packet(c, a, b, t0, t1, col=YEL, text=None, r=22, off=0):
    """dot moving from box a to box b between local times t0..t1"""
    if not (t0 <= c.t <= t1 + 0.05): return
    ac = ((a[0] + a[2]) / 2, (a[1] + a[3]) / 2); bc = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
    p0 = edge_pt(a, *bc); p1 = edge_pt(b, *ac)
    nx, ny = -(bc[1] - ac[1]), bc[0] - ac[0]; L = math.hypot(nx, ny) or 1
    q = eio(lin(c.t, t0, t1))
    x = p0[0] + (p1[0] - p0[0]) * q + nx / L * off; y = p0[1] + (p1[1] - p0[1]) * q + ny / L * off
    if text:
        w = c.pen.tw(text, 'monob', 24) + 28
        c.pen.rr(x - w / 2, y - 22, x + w / 2, y + 22, 22, fill=col, outline=INK, w=3)
        c.pen.text(x, y, text, 'monob', 24, INK)
    else:
        c.pen.circ(x, y, r, fill=col, outline=INK, w=4)

def bignum(c, x, y, value, at, size=200, col=RED, sound='thud'):
    if not c.on(at - 0.01): return
    if sound: c.sfx(at, sound)
    c.pen.text(x, y, value, 'osw', size * c.B(at, 0.45), col)

def counter(c, x, y, v0, v1, t0, t1, fmt='{:,.0f}', size=150, col=RED, suffix=''):
    if not c.on(t0 - 0.01): return
    v = v0 + (v1 - v0) * eio(lin(c.t, t0, t1))
    c.pen.text(x, y, fmt.format(v) + suffix, 'osw', size * c.B(t0, 0.35), col)

def timerbar(c, x0, y, x1, frac, at, labeltxt=None, col=YEL, h=50, right=None):
    if not c.on(at - 0.01): return
    p = c.P(at, 0.4)
    if labeltxt: c.pen.text(x0, y - 28, labeltxt, 'int', 32, mix(PAPER, INK, p), 'lm')
    if right: c.pen.text(x1, y - 28, right, 'monob', 32, mix(PAPER, INK, p), 'rm')
    xe = x0 + (x1 - x0) * p
    c.pen.rr(x0, y, xe, y + h, h / 2, fill=WHITE, outline=INK, w=5)
    f = cl(frac)
    if f > 0.02: c.pen.rr(x0 + 6, y + 6, x0 + 6 + (x1 - x0 - 12) * f, y + h - 6, (h - 12) / 2, fill=col)

def ring(c, cx, cy, r, frac, col=YEL, w=16, back_=LIGHT):
    c.pen.circ(cx, cy, r, outline=back_, w=w)
    if frac > 0.005: c.pen.arc(cx - r, cy - r, cx + r, cy + r, -90, -90 + 360 * cl(frac), col, w)

# ---------------------------------------------------------------- browser / devtools
def browser(c, x0, y0, x1, y1, url='shop.example.com', at=-1, dy=0, fill=WHITE):
    y0 += dy; y1 += dy
    card(c.pen, x0, y0, x1, y1, 28, fill, 12, 5)
    c.pen.line([(x0 + 3, y0 + 70), (x1 - 3, y0 + 70)], INK, 4, False)
    for i, col in enumerate([RED, YEL, GRN]):
        c.pen.circ(x0 + 40 + i * 38, y0 + 35, 12, fill=col, outline=INK, w=2)
    c.pen.rr(x0 + 160, y0 + 15, x1 - 34, y0 + 55, 20, fill=(236, 233, 226))
    if url:
        c.pen.text(x0 + 184, y0 + 36, url, 'intm', 26, MUTE, 'lm')
    return (x0, y0 + 72, x1, y1)

def typed_text(c, s, t0, step=0.09):
    n = int(max(0, (c.t - t0) / step) + 1) if c.t >= t0 else 0
    for i in range(min(n, len(s))): c.sfx(t0 + i * step, 'click')
    return s[:min(n, len(s))]

def addressbar(c, x0, y0, x1, text, cursor=True, size=44, h=96, placeholder=''):
    c.pen.rr(x0, y0, x1, y0 + h, h / 2, fill=WHITE, outline=INK, w=4)
    cx, cy = x0 + 56, y0 + h / 2 - 2
    c.pen.circ(cx - 4, cy - 4, 15, outline=INK, w=5); c.pen.line([(cx + 7, cy + 7), (cx + 20, cy + 20)], INK, 6)
    if text: c.pen.text(x0 + 96, y0 + h / 2 + 2, text, 'ints', size, INK, 'lm')
    elif placeholder: c.pen.text(x0 + 96, y0 + h / 2 + 2, placeholder, 'intm', size * 0.85, GREY, 'lm')
    if cursor and int(c.t * 2.6) % 2 == 0:
        tw = c.pen.tw(text, 'ints', size) if text else 0
        c.pen.rect(x0 + 100 + tw, y0 + 24, x0 + 104 + tw, y0 + h - 24, fill=INK)

def panel(c, x0, y0, x1, y1, tabs=('Network',), active=0, dy=0):
    y0 += dy; y1 += dy
    darkcard(c.pen, x0, y0, x1, y1)
    x = x0 + 36
    for i, tb in enumerate(tabs):
        col = WHITE if i == active else (130, 136, 146)
        c.pen.text(x, y0 + 44, tb, 'int', 30, col, 'lm')
        w = c.pen.tw(tb, 'int', 30)
        if i == active: c.pen.rect(x, y0 + 68, x + w, y0 + 74, fill=YEL)
        x += w + 36
    c.pen.line([(x0 + 18, y0 + 92), (x1 - 18, y0 + 92)], (60, 66, 76), 2, False)
    return (x0, y0 + 96, x1, y1)

def waterfall(c, x0, y, x1, segs, t0, total, labels=True, h=40):
    """segs: list of (name, dur, color); draws timing bar growing from t0 over `total` local seconds"""
    S = sum(d for _, d, _ in segs); x = x0; acc = 0
    for name, d, col in segs:
        start = t0 + total * acc / S; acc += d
        p = lin(c.t, start, t0 + total * acc / S)
        if p <= 0: break
        w = (x1 - x0) * d / S * p
        c.pen.rect(x, y, x + w, y + h, fill=col, outline=INK, w=3)
        x += (x1 - x0) * d / S
    return

# ---------------------------------------------------------------- code
JS_KW = {'function', 'let', 'const', 'var', 'return', 'if', 'else', 'for', 'while', 'new', 'await', 'async', 'class', 'this',
         'typeof', 'try', 'catch', 'throw', 'import', 'from', 'export', 'of', 'in', 'true', 'false', 'null', 'undefined', 'default'}
TOK = re.compile(r"(//.*$)|('[^']*'|\"[^\"]*\"|`[^`]*`)|(\b\d+(?:\.\d+)?\b)|([A-Za-z_$][\w$]*)|(\s+)|(.)")
def hl_js(line):
    out = []
    for m in TOK.finditer(line):
        cm, st, nu, idn, ws, ot = m.groups()
        if cm: out.append((cm, CM))
        elif st: out.append((st, STR))
        elif nu: out.append((nu, NU))
        elif idn:
            rest = line[m.end():]
            out.append((idn, KW if idn in JS_KW else (FN if rest.startswith('(') else PU)))
        else: out.append((m.group(0), PU))
    return out

def code(c, x0, y0, x1, y1, lines, at, step=0.12, size=32, fname='app.js', marks=(), focus=None, circles=(), lang='js', dy=None):
    """lines: list of str. marks: (line_idx, t, color). focus: (t, {idx}). circles: (line_idx, t, substr)."""
    if dy is None: dy = (1 - c.P(at - 0.45, 0.45)) * 900
    y0 += dy; y1 += dy
    darkcard(c.pen, x0, y0, x1, y1)
    for i, col in enumerate([RED, YEL, GRN]): c.pen.circ(x0 + 38 + i * 36, y0 + 36, 11, fill=col)
    c.pen.text((x0 + x1) / 2, y0 + 37, fname, 'intm', 26, (150, 156, 166))
    c.pen.line([(x0 + 4, y0 + 72), (x1 - 4, y0 + 72)], (50, 56, 66), 2, False)
    lh = size * 1.8; ys = []
    cx0 = x0 + 84
    for i, ln in enumerate(lines):
        y = y0 + 72 + lh * 0.75 + i * lh; ys.append(y)
        ap = c.P(at + i * step, 0.22)
        if ap <= 0 or not ln.strip():
            continue
        c.sfx(at + i * step, 'click')
        c.pen.text(x0 + 58, y, str(i + 1), 'mono', size * 0.7, (80, 86, 96), 'rm')
        band = None
        for (li, tt, colr) in marks:
            if li == i and c.t >= tt: band = (colr, c.P(tt, 0.35))
        dim = focus is not None and c.t >= focus[0] and i not in focus[1]
        if band and not dim:
            w = c.pen.tw(ln.rstrip(), 'mono', size) + 28
            c.pen.rr(cx0 - 14, y - lh * 0.45, cx0 - 14 + w * band[1], y + lh * 0.47, 8, fill=band[0])
        x = cx0 + (1 - ap) * 30
        toks = hl_js(ln) if lang == 'js' else [(ln, PU)]
        for s, colr in toks:
            colr2 = colr
            if band and band[0] in (YEL, (255, 210, 63)) and band[1] > 0.5: colr2 = INK
            if dim: colr2 = mix(DARK, colr, 0.3)
            if ap < 1: colr2 = mix(DARK, colr2, ap)
            c.pen.text(x, y, s, 'mono', size, colr2, 'lm')
            x += c.pen.tw(s, 'mono', size)
    for (li, tt, sub) in circles:
        if c.t < tt: continue
        ln = lines[li]; k = ln.find(sub)
        if k < 0: continue
        xa = cx0 + c.pen.tw(ln[:k], 'mono', size); xb = xa + c.pen.tw(sub, 'mono', size)
        pr = c.P(tt, 0.55); c.sfx(tt, 'swish')
        c.pen.arc(xa - 22, ys[li] - lh * 0.75, xb + 22, ys[li] + lh * 0.75, -200, -200 + 360 * pr, RED, 7)
    return ys

def console(c, x0, y0, x1, y1, outputs, dy=0):
    """outputs: list of (t, text, color)"""
    y0 += dy; y1 += dy
    darkcard(c.pen, x0, y0, x1, y1)
    c.pen.text(x0 + 36, y0 + 40, 'Console', 'int', 30, WHITE, 'lm')
    c.pen.rect(x0 + 36, y0 + 62, x0 + 36 + c.pen.tw('Console', 'int', 30), y0 + 68, fill=YEL)
    y = y0 + 120
    for (tt, s, colr) in outputs:
        if c.t < tt: continue
        c.sfx(tt, 'tick')
        p = c.P(tt, 0.25)
        c.pen.text(x0 + 40, y, '›', 'monob', 34, (120, 128, 140), 'lm')
        c.pen.text(x0 + 76 + (1 - p) * 20, y, s, 'monob', 34, mix(DARK, colr or WHITE, p), 'lm')
        y += 62

# ---------------------------------------------------------------- reusable scene templates
def scene_try(steps, kw_title='Try'):
    """steps: list of (keyword, title, sub)"""
    def f(c):
        t0 = c.T(kw_title)
        hl(c.pen, 120, 270, 960, 395, c.P(t0 + 0.1, 0.45))
        title(c, 'TRY IT YOURSELF', 335, t0, 120, sound='thud')
        dy = (1 - c.P(0, 0.5)) * 800
        n = len(steps)
        gap = 165 if n <= 4 else 135
        card(c.pen, 90, 450 + dy, 990, 450 + 80 + gap * n + dy, 28, WHITE, 12, 5)
        for i, (kw, a, b) in enumerate(steps):
            ts = c.T(kw) if isinstance(kw, str) else kw
            y = 545 + i * gap + dy
            pp = c.B(ts, 0.4)
            if pp <= 0:
                c.pen.circ(160, y, 38, outline=GREY, w=4); continue
            c.sfx(ts, 'pop')
            c.pen.circ(160, y, 38 * pp, fill=INK)
            c.pen.text(160, y, str(i + 1), 'int', 36 * pp, WHITE)
            al = c.P(ts, 0.35)
            c.pen.text(230 + (1 - al) * 30, y - 20, a, 'intx', 44, mix(WHITE, INK, al), 'lm')
            c.pen.text(230 + (1 - al) * 30, y + 30, b, 'intm', 30, mix(WHITE, MUTE, al), 'lm')
            if c.on(ts + 0.7):
                c.sfx(ts + 0.7, 'tick'); check(c.pen, 925, y, 1.0, GRN, 10, c.P(ts + 0.7, 0.3))
    return f

def scene_next(tag, name, sub, kw_name, kw_sub, cta=True):
    def f(c):
        pin = c.P(0, 0.5); c.sfx(0.05, 'whoosh')
        dx = (1 - pin) * 1100
        x0, x1 = 70 + dx, 1010 + dx
        darkcard(c.pen, x0, 330, x1, 1110, 30)
        cx = (x0 + x1) / 2
        c.pen.text(cx, 430, 'NEXT EPISODE', 'int', 34, YEL)
        c.pen.text(cx, 505, tag, 'osw', 64, WHITE)
        tn = c.T(kw_name)
        size = min(200, 800 / max(1, c.pen.tw(name, 'osw', 100)) * 100)
        if c.on(tn - 0.01):
            c.sfx(tn, 'thud'); c.pen.text(cx, 680, name, 'osw', size * c.B(tn, 0.45), YEL)
        ts = c.T(kw_sub)
        if c.on(ts - 0.01): c.pen.text(cx, 830, sub, 'int', 44 * c.B(ts, 0.4), WHITE)
        if cta:
            tc = c.T('comment') if any(norm(w[0]) == 'comment' for w in c.words) else ts + 1.0
            if c.on(tc - 0.01):
                c.sfx(tc, 'pop'); pn = c.B(tc, 0.4); hw = 360 * pn
                c.pen.rr(cx - hw, 940, cx + hw, 1030, 45, fill=YEL, outline=INK, w=4)
                c.pen.text(cx, 985, 'Comment NOTES for the cheat sheet', 'int', 36 * pn, INK)
            tf = tc + 1.2
            if c.on(tf): c.pen.text(540, 1215, 'Follow for the full series', 'int', 44 * c.B(tf, 0.4), INK)
    return f

def scene_iq_intro(theme, sub='4 questions · pause and answer before the reveal', kw='questions'):
    def f(c):
        stamp(c.cv, 540, 360, 'INTERVIEW QUESTIONS', 80, c.P(0.1, 0.4), -4, RED); c.sfx(0.1, 'thud')
        title(c, theme, 600, 0.6, 96 if len(theme) < 20 else 76, hlcol=YEL)
        txt(c, 540, 740, sub, 1.2, 'int', 36, MUTE)
        for i in range(4):
            tt = 1.6 + i * 0.25
            if c.on(tt):
                c.sfx(tt, 'pop'); s = c.B(tt, 0.35)
                card(c.pen, 150 + i * 205 - 80 * s, 900 - 80 * s, 150 + i * 205 + 80 * s, 900 + 80 * s, 20, WHITE, 8, 5)
                c.pen.text(150 + i * 205, 900, f'Q{i + 1}', 'osw', 80 * s, INK)
    return f

def scene_iq(num, question, answer, kw_answer='answer', code_lines=None):
    """question: str (wrapped); answer: list of short lines. Narration: 'Question N. ... [[pause]] Answer: ...'"""
    def f(c):
        c.sfx(0.05, 'whoosh')
        pill(c.pen, 540, 300, f'QUESTION {num}', c.B(0.0, 0.35), INK, WHITE, 30, outline=None)
        qy = 400
        lines = wrap(c.pen, question, 'intx', 54, 880)
        for i, ln in enumerate(lines):
            txt(c, 540, qy + i * 70, ln, 0.15 + i * 0.12, 'intx', 54, INK)
        y = qy + len(lines) * 70 + 30
        if code_lines:
            csz = min(30, int(820 / (0.6 * max(len(l) for l in code_lines))))
            code(c, 90, y, 990, y + 90 + len(code_lines) * 54, code_lines, 0.4, 0.08, csz, 'question.js', dy=0)
            y += 130 + len(code_lines) * 54
        ta = c.T(kw_answer)
        # think timer between question end and answer
        tq = ta - 0.1
        think0 = max(0.5, tq - 3.2)
        if think0 <= c.t < ta:
            frac = lin(c.t, think0, tq)
            ring(c, 540, y + 140, 90, frac, YEL, 18)
            c.pen.text(540, y + 140, str(max(1, 3 - int((c.t - think0) / ((tq - think0) / 3)))), 'osw', 90, INK)
            c.pen.text(540, y + 270, 'pause & think', 'int', 34, MUTE)
            for k in range(3): c.sfx(think0 + k * (tq - think0) / 3, 'tick')
        if c.on(ta - 0.01):
            c.sfx(ta, 'ding')
            h = 70 + len(answer) * 64
            s = c.P(ta, 0.4)
            card(c.pen, 90, y + 20 + (1 - s) * 60, 990, y + 20 + h + (1 - s) * 60, 24, (255, 246, 214), 10, 5)
            c.pen.text(130, y + 62 + (1 - s) * 60, 'ANSWER', 'int', 28, GRN, 'lm')
            for i, a in enumerate(answer):
                kw = a[0] if isinstance(a, tuple) else None
                s_ = a[1] if isinstance(a, tuple) else a
                at = c.T(kw) if kw else ta + 0.3 + i * 0.9
                txt(c, 130, y + 120 + i * 64 + (1 - s) * 60, s_, at, 'ints', 36, INK, 'lm', 'slide')
    return f

def wrap(pen, s, k, size, maxw):
    out, cur = [], ''
    for w in s.split():
        t = (cur + ' ' + w).strip()
        if pen.tw(t, k, size) <= maxw: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def chapter(c, x, y, tag, name, at):
    """finale chapter stamp: small ink pill with episode tag + name"""
    if not c.on(at - 0.01): return
    c.sfx(at, 'pop'); s = c.B(at, 0.35)
    w1 = c.pen.tw(tag, 'int', 26 * s) + 30; w2 = c.pen.tw(name, 'intx', 34 * s) + 34
    c.pen.rr(x - (w1 + w2) / 2 + 6, y - 30 * s + 6, x + (w1 + w2) / 2 + 6, y + 30 * s + 6, 30 * s, fill=INK)
    c.pen.rr(x - (w1 + w2) / 2, y - 30 * s, x + (w1 + w2) / 2, y + 30 * s, 30 * s, fill=YEL, outline=INK, w=4)
    c.pen.rr(x - (w1 + w2) / 2, y - 30 * s, x - (w1 + w2) / 2 + w1, y + 30 * s, 30 * s, fill=INK)
    c.pen.text(x - (w1 + w2) / 2 + w1 / 2, y, tag, 'int', 26 * s, WHITE)
    c.pen.text(x - (w1 + w2) / 2 + w1 + w2 / 2, y, name, 'intx', 34 * s, INK)

# ---------------------------------------------------------------- pipeline / perf helpers
STAGE_COL = {'JS': YEL, 'Style': (150, 120, 230), 'Layout': PURPLE, 'Paint': GRN, 'Composite': CYAN}

def pipeline(c, x0, y, active, at, stages=('Layout', 'Paint', 'Composite'), w=230, h=90, gap=40, label_=None):
    """row of stage chips; active = set of lit stages"""
    if not c.on(at - 0.01): return
    c.sfx(at, 'pop')
    if label_: c.pen.text(x0, y - 70, label_, 'intx', 40, INK, 'lm')
    for i, st in enumerate(stages):
        x = x0 + i * (w + gap); p = c.B(at + i * 0.12, 0.3)
        on = st in active
        fill = STAGE_COL.get(st, YEL) if on else LIGHT
        c.pen.rr(x + 6, y - h / 2 * p + 8, x + w + 6, y + h / 2 * p + 8, 18, fill=INK if on else None)
        c.pen.rr(x, y - h / 2 * p, x + w, y + h / 2 * p, 18, fill=fill, outline=INK if on else GREY, w=4)
        c.pen.text(x + w / 2, y, st, 'intx', 36 * p, (INK if st not in ('Layout',) else WHITE) if on else GREY)
        if i < len(stages) - 1: arrow(c.pen, x + w + 4, y, x + w + gap - 4, y, 1, INK if on else GREY, 4, 14)

def flame(c, x0, y0, x1, blocks, at, h=54, labels=True):
    """blocks: list of (start_frac, dur_frac, row, kind, warn) drawn left->right as time sweeps"""
    for (s, d, row, kind, *rest) in blocks:
        warn = rest[0] if rest else False
        t0 = at + s * 2.0
        if not c.on(t0): continue
        p = c.P(t0, max(0.15, d * 2.0), lambda x: x)
        xa = x0 + (x1 - x0) * s; xb = xa + (x1 - x0) * d * p
        y = y0 + row * (h + 8)
        c.pen.rect(xa, y, xb, y + h, fill=STAGE_COL.get(kind, YEL), outline=INK, w=2)
        if labels and (xb - xa) > 70: c.pen.text((xa + xb) / 2, y + h / 2, kind, 'int', 22, INK if kind != 'Layout' else WHITE)
        if warn and p >= 1: c.pen.poly([(xb - 16, y), (xb, y), (xb, y + 16)], fill=RED)

def tree(c, nodes, at, step=0.15, col=WHITE, size=30):
    """nodes: list of (key, label, x, y, parent_key, kw_or_None). draws edges + pills in order"""
    pos = {}
    for i, (k, lab, x, y, par, kw) in enumerate(nodes):
        t = c.T(kw) if isinstance(kw, str) else (at + i * step if kw is None else kw)
        pos[k] = (x, y, t)
    for (k, lab, x, y, par, kw) in nodes:
        t = pos[k][2]
        if par and c.on(t): 
            px, py, _ = pos[par]
            q = c.P(t, 0.3); c.pen.line([(px, py + 26), (px + (x - px) * q, py + 26 + (y - 26 - py - 26) * q)], INK, 4)
    for (k, lab, x, y, par, kw) in nodes:
        t = pos[k][2]
        if not c.on(t): continue
        c.sfx(t, 'tick'); s = c.B(t, 0.3)
        w = c.pen.tw(lab, 'monob', size) + 36
        fill = col(k) if callable(col) else col
        c.pen.rr(x - w / 2 * s + 5, y - 28 * s + 6, x + w / 2 * s + 5, y + 28 * s + 6, 14, fill=INK)
        c.pen.rr(x - w / 2 * s, y - 28 * s, x + w / 2 * s, y + 28 * s, 14, fill=fill, outline=INK, w=4)
        c.pen.text(x, y, lab, 'monob', size * s, INK)
    return pos

def chips(c, x0, y, items, at, step=0.25, size=32):
    """items: list of (text, fill). wraps at 960"""
    x = x0
    for i, (s_, fill) in enumerate(items):
        w = c.pen.tw(s_, 'monob', size) + 40
        if x + w > 990: x = x0; y += 80
        t = at + i * step
        if c.on(t):
            c.sfx(t, 'pop'); p = c.B(t, 0.3)
            c.pen.rr(x, y - 30 * p, x + w, y + 30 * p, 30 * p, fill=fill, outline=INK, w=4)
            c.pen.text(x + w / 2, y, s_, 'monob', size * p, INK)
        x += w + 20
