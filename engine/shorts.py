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

# ================================================================ MEME STYLE (EP['style'] = 'meme')
# dark bg + rotating rays, giant outlined text, Noto emoji stickers, pop captions, generated music bed.
import io as _io, wave as _wave
import numpy as np
from PIL import ImageDraw as _ID
BG0, BG1 = (12, 13, 17), (30, 32, 40)
_EP_STYLE = {}

def _bg_base():
    if 'base' not in _EP_STYLE:
        y = np.linspace(0, 1, H)[:, None]; x = np.linspace(-1, 1, W)[None, :]
        r = np.sqrt(x ** 2 * 0.6 + (y - 0.42) ** 2 * 1.4)
        g = np.clip(1 - r, 0, 1)[..., None]
        a = np.array(BG0)[None, None] * (1 - g) + np.array(BG1)[None, None] * g
        _EP_STYLE['base'] = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    return _EP_STYLE['base']

def meme_bg(t, accent=YEL):
    fr = _bg_base().copy()
    lay = Image.new('RGBA', (W // 2, H // 2), (0, 0, 0, 0)); d = _ID.Draw(lay)
    cx, cy, R, n = W // 4, int(H * 0.21), 1400, 14
    a0 = t * 0.25
    for i in range(n):
        a = a0 + i * 2 * math.pi / n
        d.polygon([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a)), (cx + R * math.cos(a + math.pi / n), cy + R * math.sin(a + math.pi / n))],
                  fill=accent + (16,))
    fr.alpha_composite(lay.resize((W, H), Image.BILINEAR))
    return fr

def big(c, x, y, s, size, at=-0.3, col=WHITE, k='osw', stroke=10, d=0.22, rot=0, sound='pop'):
    """giant outlined text with drop shadow; pops in at `at`"""
    if not c.on(at - 0.01) or not s: return
    p = c.B(at, d)
    if sound and at > 0: c.sfx(at, sound)
    size = min(size, size * 960 / max(1, c.pen.tw(s, k, size) + 2 * stroke))
    f = font(k, max(2, size * p) * SS)
    lay = Image.new('RGBA', (CW, int(size * 2.2 * SS)), (0, 0, 0, 0)); dr = _ID.Draw(lay)
    my = lay.height // 2
    dr.text((x * SS + 10 * SS, my + 12 * SS), s, font=f, fill=(0, 0, 0, 170), anchor='mm', stroke_width=int(stroke * SS), stroke_fill=(0, 0, 0, 170))
    dr.text((x * SS, my), s, font=f, fill=col, anchor='mm', stroke_width=int(stroke * SS), stroke_fill=(8, 8, 10))
    if rot: lay = lay.rotate(rot, resample=Image.BICUBIC, center=(x * SS, my))
    c.cv.alpha_composite(lay, (0, int(y * SS - my)))

_EMO = {}
def emoji(c, name, cx, cy, size, at=-0.3, bob=True, rot=0, sound='pop'):
    if not c.on(at - 0.01): return
    p = c.B(at, 0.3)
    if sound and at > 0: c.sfx(at, sound)
    px = int(size * SS)
    key = (name, px)
    if key not in _EMO:
        import cairosvg
        png = cairosvg.svg2png(url=os.path.join(ROOT, 'brand', 'emoji', name + '.svg'), output_width=px, output_height=px)
        _EMO[key] = Image.open(_io.BytesIO(png)).convert('RGBA')
    im = _EMO[key]
    s = max(0.01, p)
    if s < 0.999: im = im.resize((max(1, int(px * s)), max(1, int(px * s))), Image.LANCZOS)
    r = rot + (6 * math.sin(c.t * 5 + cx) if bob else 0)
    if r: im = im.rotate(r, resample=Image.BICUBIC, expand=True)
    dy = (10 * math.sin(c.t * 6 + cx) if bob else 0) * SS
    c.cv.alpha_composite(im, (int(cx * SS - im.width / 2), int(cy * SS - im.height / 2 + dy)))

def bar(c, x0, y, x1, frac, col, h=70, label_=None):
    c.pen.rr(x0, y - h / 2, x1, y + h / 2, h / 2, fill=(40, 42, 50), outline=WHITE, w=5)
    if frac > 0.01: c.pen.rr(x0 + 8, y - h / 2 + 8, x0 + 8 + (x1 - x0 - 16) * min(1, frac), y + h / 2 - 8, h / 2 - 8, fill=col)
    if label_: c.pen.text((x0 + x1) / 2, y, label_, 'intx', h * 0.55, WHITE)

def meme_captions(img, t, chunks, ymid=1500):
    d = _ID.Draw(img)
    for st, en, ch in chunks:
        if not (st <= t < en): continue
        size = 70
        f = font('intx', size)
        words = [w[0].upper() for w in ch]
        gap = 22
        ws = [f.getlength(w) for w in words]
        lines = [list(range(len(ch)))]
        if sum(ws) + gap * (len(ch) - 1) > 900 and len(ch) > 1:
            m = (len(ch) + 1) // 2; lines = [list(range(m)), list(range(m, len(ch)))]
        active = max([j for j, w in enumerate(ch) if w[1] - 0.05 <= t] or [-1])
        for li, L in enumerate(lines):
            lw = sum(ws[i] for i in L) + gap * (len(L) - 1)
            if lw > 980: f2 = font('intx', int(size * 980 / lw))
            else: f2 = f
            x = 540 - min(lw, 980) / 2; y = ymid + (li - (len(lines) - 1) / 2) * size * 1.25
            for i in L:
                on = i == active
                ff = font('intx', int(f2.size * (1.12 if on else 1)))
                d.text((x, y), words[i], font=ff, fill=YEL if on else WHITE, anchor='lm', stroke_width=7, stroke_fill=(0, 0, 0))
                x += f2.getlength(words[i]) + gap
        return

_chrome_paper = chrome
def chrome(img, t, ep, total, chunks):
    if ep.get('style') != 'meme': return _chrome_paper(img, t, ep, total, chunks)
    d = _ID.Draw(img)
    d.text((540, 128), 'TECH, EXPLAINED', font=font('osw', 34), fill=YEL, anchor='mm')
    d.rectangle((0, 1908, W * t / total, 1920), fill=YEL)
    meme_captions(img, t, chunks)
B.chrome = chrome

_frame_paper = frame
def frame(t, si, spans, scenes, W_, ep, total, chunks, sfxset):
    if ep.get('style') != 'meme': return _frame_paper(t, si, spans, scenes, W_, ep, total, chunks, sfxset)
    t0, t1 = spans[si]
    cv = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    words = [(w[0], w[1] - t0, w[2] - t0) for w in W_ if w[3] == si]
    c = Ctx(Pen(cv, SS), cv, t - t0, words, t1 - t0, sfxset, t0)
    scenes[si][0](c)
    lt = t - t0
    z = 1 + 0.16 * (1 - eo(lin(lt, 0, 0.18))) + 0.05 * lin(lt, 0.18, max(0.3, t1 - t0))
    sh = 16 * (1 - lin(lt, 0, 0.16)) * SS
    dx, dy = sh * math.sin(lt * 90), sh * math.cos(lt * 70)
    cw, ch = CW / z, CH / z
    x0 = min(max(0, (CW - cw) / 2 + dx), CW - cw); y0 = min(max(0, (CH - ch) / 2 + dy), CH - ch)
    lay = cv.resize((W, H), Image.BOX, box=(x0, y0, x0 + cw, y0 + ch))
    fr = meme_bg(t, ep.get('accent', YEL)); fr.alpha_composite(lay)
    chrome(fr, t, ep, total, chunks)
    if si > 0 and lt < 1.5 / FPS:
        fr = Image.blend(fr, Image.new('RGBA', fr.size, (255, 255, 255, 255)), 0.5)
    return fr.convert('RGB')
B.frame = frame

# ---------------------------------------------------------------- generated music (no copyright)
SR = 48000
def _note(f, n, kind='saw', dec=6.0, harm=8):
    tt = np.arange(n) / SR
    if kind == 'sine': s = np.sin(2 * np.pi * f * tt)
    else: s = sum(np.sin(2 * np.pi * f * h * tt) / h for h in range(1, harm + 1)) * 0.6
    return s * np.exp(-tt * dec) * np.minimum(1, tt / 0.004)

def music(total, bpm=124, stops=(), seed=7):
    """house-ish loop in A minor: kick 4/4, clap 2&4, offbeat hats, offbeat bass, chord stabs. Am F C G."""
    rng = np.random.default_rng(seed)
    n = int((total + 1) * SR); out = np.zeros(n, np.float32)
    b = 60 / bpm; bar_ = 4 * b
    roots = [55.0, 43.65, 65.41, 49.0]                      # A1 F1 C2 G1
    chords = [[220, 261.6, 329.6], [174.6, 220, 261.6], [196, 261.6, 329.6], [196, 246.9, 293.7]]
    def add(t, s, g=1.0):
        i = int(t * SR); j = min(n, i + len(s))
        if i < n: out[i:j] += s[: j - i] * g
    tk = np.arange(int(0.32 * SR)) / SR
    kick = np.sin(2 * np.pi * np.cumsum(45 + 110 * np.exp(-tk * 28)) / SR) * np.exp(-tk * 9)
    clap = rng.normal(0, 1, int(0.18 * SR)); clap = (clap - np.convolve(clap, np.ones(12) / 12, 'same')) * np.exp(-np.arange(len(clap)) / SR * 22)
    hat = rng.normal(0, 1, int(0.05 * SR)); hat = (hat - np.convolve(hat, np.ones(4) / 4, 'same')) * np.exp(-np.arange(len(hat)) / SR * 90)
    t = 0.0; k = 0
    while t < total + 0.5:
        bi = int(t // bar_) % 4; beat = k % 4
        add(t, kick, 0.9)
        if beat in (1, 3): add(t, clap, 0.35)
        add(t + b / 2, hat, 0.22); add(t + b / 4, hat, 0.08); add(t + 3 * b / 4, hat, 0.08)
        add(t + b / 2, _note(roots[bi], int(b / 2 * SR), 'saw', 9, 5), 0.32)
        if beat in (1, 3):
            for f in chords[bi]: add(t + b / 2, _note(f, int(0.25 * SR), 'saw', 14, 6), 0.06)
        t += b; k += 1
    g = np.ones(n, np.float32)
    for s0 in stops:  # beat drop: silence for half a beat
        i, j = int(s0 * SR), int((s0 + b / 2 + 0.05) * SR); g[i:j] = 0.0
    out *= g
    return out / (np.abs(out).max() + 1e-6) * 0.5

def _readwav(p):
    with _wave.open(p) as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16 if sw == 2 else np.int32).astype(np.float32)
    if ch > 1: x = x.reshape(-1, ch).mean(1)
    x /= 32768 if sw == 2 else 2 ** 31
    if sr != SR: x = np.interp(np.arange(int(len(x) * SR / sr)) / SR, np.arange(len(x)) / sr, x).astype(np.float32)
    return x

_bed_paper = B.bed
def bed(sfx, total, path):
    _bed_paper(sfx, total, path)
    epid = os.path.basename(path).split('_')[0]
    ep = load(epid)[0]
    if not ep.get('music'): return
    x = _readwav(path)
    stops = list(ep.get('drops', ()))
    if ep.get('drop_scenes'):
        spans = B.prep_cache(epid)[3]
        stops += [spans[i][0] - 0.3 for i in ep['drop_scenes']]
    m = music(total, ep.get('bpm', 124), stops)[:len(x)]
    vo = _readwav(f'tmp/{epid}_vo.wav') if os.path.exists(f'tmp/{epid}_vo.wav') else np.zeros(len(x))
    env = np.convolve(np.abs(vo), np.ones(2400) / 2400, 'same')[:len(m)]
    env = np.pad(env, (0, max(0, len(m) - len(env))))
    duck = 1 - 0.6 * np.clip(env / (env.max() * 0.25 + 1e-6), 0, 1)
    y = x[:len(m)] + m * duck * ep.get('music_gain', 0.55)
    with _wave.open(path, 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
B.bed = bed
