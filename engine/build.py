#!/usr/bin/env python3
"""Usage: python -m engine.build {text|check|render} S1E01 [S1E02 ...]
  text   -> prints the exact TTS script (save the voiceover as vo/<ID>.wav)
  check  -> aligns VO, runs every scene, writes tmp/<ID>_sheet.jpg (one frame per scene)
  render -> full 1080x1920 render + mix -> out/<ID>_<slug>.mp4
"""
import importlib, json, os, re, subprocess, sys, wave
import numpy as np
from PIL import Image
from engine.lib import *
from engine.align import align

PAUSE = re.compile(r'\[\[(\d+(?:\.\d+)?)\]\]')

def load(epid):
    m = importlib.import_module('episodes.' + epid.lower())
    return m.EP, m.SCENES

def parse(scenes):
    words, pauses, paras = [], [], []
    for si, (_, text) in enumerate(scenes):
        toks = text.split()
        clean = []
        for j, tk in enumerate(toks):
            m = PAUSE.fullmatch(tk)
            if m:
                pauses.append((len(words) - 1, float(m.group(1)))); continue
            clean.append(tk)
            st = 3 if tk[-1] in '.?!' else (1 if tk[-1] in ',:;—' else 0)
            words.append(dict(w=tk, scene=si, strength=st))
        words[-1]['strength'] = 8
        paras.append(' '.join(clean))
    return words, pauses, '\n\n'.join(paras)

def timing(epid, ep, scenes):
    words, pauses, _ = parse(scenes)
    wav = f'vo/{epid}.wav'
    tm, dur = align(words, wav)
    # insert pauses into audio
    with wave.open(wav) as wf:
        sr = wf.getframerate(); ch = wf.getnchannels(); sw = wf.getsampwidth()
        a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).reshape(-1, ch)[:, 0].astype(np.float32)
    shift = [0.0] * len(words)
    for wi, secs in sorted(pauses, reverse=True):
        nxt = tm[wi + 1][0] if wi + 1 < len(tm) else tm[wi][1] + 0.2
        at = (tm[wi][1] + nxt) / 2
        i = int(at * sr)
        a = np.concatenate([a[:i], np.zeros(int(secs * sr), np.float32), a[i:]])
        for k in range(wi + 1, len(words)): shift[k] += secs
    tm = [[s + shift[k], e + shift[k]] for k, (s, e) in enumerate(tm)]
    with wave.open(f'tmp/{epid}_vo.wav', 'wb') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes(a.astype(np.int16).tobytes())
    # scene spans
    first = {}; last = {}
    for k, w in enumerate(words):
        first.setdefault(w['scene'], k); last[w['scene']] = k
    starts = []
    for si in range(len(scenes)):
        s = 0.0 if si == 0 else max(tm[last[si - 1]][1] + 0.05, tm[first[si]][0] - 0.35)
        starts.append(round(s * FPS) / FPS)
    total = round((tm[-1][1] + ep.get('tail', 2.4)) * FPS) / FPS
    spans = [(starts[i], starts[i + 1] if i + 1 < len(starts) else total) for i in range(len(starts))]
    capmap = ep.get('cap', {})
    W_ = [(capmap.get(w['w'], w['w']), tm[k][0], tm[k][1], w['scene']) for k, w in enumerate(words)]
    return W_, spans, total

# ---------------------------------------------------------------- captions + chrome
def build_chunks(W_):
    chunks, cur = [], []
    for w in W_:
        if cur and (len(cur) >= 4 or w[1] - cur[-1][2] > 0.45 or w[3] != cur[-1][3]):
            chunks.append(cur); cur = []
        cur.append(w)
        if w[0][-1] in '.?!,:;':
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    out = []
    for i, ch in enumerate(chunks):
        st = ch[0][1] - 0.08
        en = chunks[i + 1][0][1] - 0.08 if i + 1 < len(chunks) else ch[-1][2] + 1.2
        out.append((st, min(en, ch[-1][2] + 0.7), ch))
    return out

def captions(pen, t, chunks):
    for st, en, ch in chunks:
        if not (st <= t < en): continue
        size, gap = 50, 16
        ws = [pen.tw(w[0], 'intx', size) for w in ch]
        total = sum(ws) + gap * (len(ch) - 1)
        lines = [list(range(len(ch)))]
        if total > 820 and len(ch) > 1:
            m = (len(ch) + 1) // 2; lines = [list(range(m)), list(range(m, len(ch)))]
        lw = [sum(ws[i] for i in L) + gap * (len(L) - 1) for L in lines]
        if max(lw) > 900:
            size = int(size * 900 / max(lw)); ws = [pen.tw(w[0], 'intx', size) for w in ch]
            lw = [sum(ws[i] for i in L) + gap * (len(L) - 1) for L in lines]
        bw = max(lw) + 64; lh = 70; bh = lh * len(lines) + 30
        oy = (1 - eo(lin(t, st, st + 0.15))) * 14
        y0 = 1490 - bh / 2 + oy
        pen.rr(540 - bw / 2 + 7, y0 + 8, 540 + bw / 2 + 7, y0 + bh + 8, 22, fill=INK)
        pen.rr(540 - bw / 2, y0, 540 + bw / 2, y0 + bh, 22, fill=WHITE, outline=INK, w=4)
        active = None
        for j, w in enumerate(ch):
            if w[1] - 0.05 <= t: active = j
        for li, L in enumerate(lines):
            x = 540 - lw[li] / 2; y = y0 + 15 + lh * li + lh / 2
            for i in L:
                if i == active: pen.rr(x - 8, y - 32, x + ws[i] + 8, y + 32, 10, fill=YEL)
                pen.text(x, y, ch[i][0], 'intx', size, INK, 'lm')
                x += ws[i] + gap
        return

def chrome(img, t, ep, total, chunks):
    pen = Pen(img, 1)
    w = pen.tw(ep['tag'], 'int', 28) + 40
    pen.rr(60, 128, 60 + w, 178, 25, fill=INK)
    pen.text(60 + w / 2, 153, ep['tag'], 'int', 28, WHITE)
    pen.text(60 + w + 18, 153, ep['short'], 'int', 28, INK, 'lm')
    tw2 = pen.tw('FRONTEND DECODED', 'osw', 34)
    pen.rect(1020 - tw2, 168, 1020, 176, fill=YEL)
    pen.text(1020, 152, 'FRONTEND DECODED', 'osw', 34, INK, 'rm')
    pen.rect(0, 1912, W * t / total, 1920, fill=YEL)
    captions(pen, t, chunks)

# ---------------------------------------------------------------- background
_P = None
def papers():
    global _P
    if _P is not None: return _P
    paths = [f'tmp/paper{i}.png' for i in range(3)]
    if all(os.path.exists(p) for p in paths):
        _P = [Image.open(p).convert('RGBA') for p in paths]; return _P
    rng = np.random.default_rng(7)
    lf = rng.normal(0, 1, (H // 24, W // 24)).astype(np.float32)
    lfi = Image.fromarray(((lf * 40 + 128).clip(0, 255)).astype(np.uint8)).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(20))
    lfa = (np.asarray(lfi, np.float32) - 128) / 128 * 7
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    base = np.array(PAPER, np.float32); _P = []
    for s in range(3):
        g = np.random.default_rng(100 + s).normal(0, 4.2, (H, W)).astype(np.float32)
        arr = base[None, None, :] + (lfa - (d ** 2.2) * 9 + g)[..., None]
        im = Image.fromarray(arr.clip(0, 255).astype(np.uint8)).convert('RGBA'); im.save(paths[s]); _P.append(im)
    return _P

def frame(t, si, spans, scenes, W_, ep, total, chunks, sfxset):
    t0, t1 = spans[si]
    fn = scenes[si][0]
    cv = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    words = [(w[0], w[1] - t0, w[2] - t0) for w in W_ if w[3] == si]
    c = Ctx(Pen(cv, SS), cv, t - t0, words, t1 - t0, sfxset, t0)
    fn(c)
    z = 1 + 0.03 * eio(lin(t, t0, t1))
    cw, ch = CW / z, CH / z; x0, y0 = (CW - cw) / 2, (CH - ch) / 2
    lay = cv.resize((W, H), Image.BOX, box=(x0, y0, x0 + cw, y0 + ch))
    fr = papers()[int(t * FPS / 3) % 3].copy(); fr.alpha_composite(lay)
    chrome(fr, t, ep, total, chunks)
    return fr.convert('RGB')

# ---------------------------------------------------------------- audio bed
SR = 48000
def bed(sfx, total, path):
    n = int((total + 1) * SR); out = np.zeros(n, np.float32); rng = np.random.default_rng(3)
    def env(L, a=0.004, dec=8.0):
        tt = np.arange(int(L * SR)) / SR; return np.minimum(1, tt / a) * np.exp(-tt * dec), tt
    def lp(x, k): return np.convolve(x, np.ones(k) / k, mode='same')
    last = {}
    for t, k in sorted(sfx):
        if t - last.get(k, -9) < 0.05: continue
        last[k] = t; i = int(t * SR)
        if k == 'click': e, tt = env(0.03, 0.001, 140); s = rng.normal(0, 1, len(tt)); s = (s - lp(s, 6)) * e * 0.25
        elif k == 'tick': e, tt = env(0.02, 0.001, 220); s = np.sin(2 * np.pi * 2400 * tt) * e * 0.09
        elif k == 'pop': e, tt = env(0.12, 0.002, 30); f = 520 + 600 * tt / 0.12; s = np.sin(2 * np.pi * np.cumsum(f) / SR) * e * 0.2
        elif k == 'whoosh':
            tt = np.arange(int(0.42 * SR)) / SR; e = np.sin(np.pi * tt / 0.42) ** 2; s = rng.normal(0, 1, len(tt)); s = (lp(s, 18) - lp(s, 90)) * e * 0.5
        elif k == 'swish':
            tt = np.arange(int(0.18 * SR)) / SR; e = np.sin(np.pi * tt / 0.18) ** 2; s = rng.normal(0, 1, len(tt)); s = (lp(s, 4) - lp(s, 30)) * e * 0.16
        elif k == 'thud':
            e, tt = env(0.35, 0.003, 11); s = (np.sin(2 * np.pi * 68 * tt) + 0.4 * np.sin(2 * np.pi * 136 * tt)) * e * 0.5
            s += lp(rng.normal(0, 1, len(tt)), 40) * np.exp(-tt * 40) * 0.55
        elif k == 'ding':
            e, tt = env(1.1, 0.002, 4.5); s = (np.sin(2 * np.pi * 1318.5 * tt) + 0.35 * np.sin(2 * np.pi * 2637 * tt) + 0.2 * np.sin(2 * np.pi * 1976 * tt)) * e * 0.15
        elif k == 'buzz': e, tt = env(0.11, 0.002, 18); s = lp(np.sign(np.sin(2 * np.pi * 150 * tt)) * e * 0.06, 8)
        elif k == 'door':
            tt = np.arange(int(0.55 * SR)) / SR; s = lp(rng.normal(0, 1, len(tt)), 60) * np.sin(np.pi * tt / 0.55) * 0.45
        else: continue
        j = min(n, i + len(s)); out[i:j] += s[:j - i]
    tt = np.arange(n) / SR; pad = np.zeros(n, np.float32)
    for f, a in [(110, 1.0), (164.81, .7), (220, .5), (261.63, .45), (329.63, .35), (493.88, .2)]:
        pad += (a * np.sin(2 * np.pi * f * tt) * (0.6 + 0.4 * np.sin(2 * np.pi * (0.05 + f / 20000) * tt + f))).astype(np.float32)
    pad = lp(pad, 24)
    fade = np.minimum(1, tt / 2.5) * np.minimum(1, np.maximum(0, (total + 0.5 - tt) / 3))
    out += pad * fade * 0.018
    pulse = np.zeros(n, np.float32)
    for b in np.arange(0.0, total - 2, 60 / 92):
        i = int(b * SR); L = int(0.18 * SR); e = np.exp(-np.arange(L) / SR * 25)
        pulse[i:i + L] += (np.sin(2 * np.pi * 55 * np.arange(L) / SR) * e).astype(np.float32)[: n - i]
    out += pulse * 0.05 * fade
    out = np.clip(out, -0.95, 0.95)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((out * 32767).astype(np.int16).tobytes())

# ---------------------------------------------------------------- commands
def prep(epid):
    ep, scenes = load(epid)
    W_, spans, total = timing(epid, ep, scenes)
    return ep, scenes, W_, spans, total, build_chunks(W_)

def cmd_check(epid):
    ep, scenes, W_, spans, total, chunks = prep(epid)
    S = set(); thumbs = []
    for si, (t0, t1) in enumerate(spans):
        for q in (0.0, 0.3, 0.6, 0.97):
            t = t0 + (t1 - t0) * q
            im = frame(t, si, spans, scenes, W_, ep, total, chunks, S)
            if q == 0.97: thumbs.append(im.resize((270, 480)))
    cols = 5; rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new('RGB', (270 * cols, 480 * rows), 'white')
    for i, im in enumerate(thumbs): sheet.paste(im, ((i % cols) * 270, (i // cols) * 480))
    sheet.save(f'tmp/{epid}_sheet.jpg', quality=80)
    print(f'{epid}: {len(scenes)} scenes, {total:.1f}s ->', ' '.join(f'{a:.1f}' for a, _ in spans))

def render_part(args):
    epid, si = args
    ep, scenes, W_, spans, total, chunks = prep_cache(epid)
    t0, t1 = spans[si]; S = set()
    tmp, fin = f'out/parts/{epid}_{si:02d}.tmp.mp4', f'out/parts/{epid}_{si:02d}.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp], stdin=subprocess.PIPE)
    for f in range(round(t0 * FPS), round(t1 * FPS)):
        p.stdin.write(frame(f / FPS, si, spans, scenes, W_, ep, total, chunks, S).tobytes())
    p.stdin.close()
    if p.wait() == 0: os.replace(tmp, fin)
    return sorted(S)

_cache = {}
def prep_cache(epid):
    if epid not in _cache: _cache[epid] = prep(epid)
    return _cache[epid]

def cmd_render(epid):
    from multiprocessing import Pool
    os.makedirs('out/parts', exist_ok=True)
    ep, scenes, W_, spans, total, chunks = prep_cache(epid)
    sfx = set((round(a, 3), 'whoosh') for a, _ in spans[1:])
    with Pool(2) as pool:
        for S in pool.imap_unordered(render_part, [(epid, i) for i in range(len(scenes))]): sfx |= set(S)
    with open(f'tmp/{epid}_list.txt', 'w') as f:
        for i in range(len(scenes)): f.write(f"file '../out/parts/{epid}_{i:02d}.mp4'\n")
    bed(sfx, total, f'tmp/{epid}_bed.wav')
    slug = re.sub(r'[^A-Za-z0-9]+', '_', ep['short'].title()).strip('_')
    outp = f'out/{epid}_{slug}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'tmp/{epid}_list.txt', '-c', 'copy', f'tmp/{epid}_v.mp4'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'tmp/{epid}_v.mp4', '-i', f'tmp/{epid}_vo.wav', '-i', f'tmp/{epid}_bed.wav', '-filter_complex',
                    '[1:a]aresample=48000,apad[v];[2:a]aresample=48000[b];[v][b]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-crf', '23', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-t', f'{total:.3f}', '-movflags', '+faststart', outp], check=True)
    for i in range(len(scenes)): os.remove(f'out/parts/{epid}_{i:02d}.mp4')
    print('rendered', outp, f'{total:.1f}s')

if __name__ == '__main__':
    cmd, ids = sys.argv[1], sys.argv[2:]
    for epid in ids:
        if cmd == 'text': print(parse(load(epid)[1])[2]); print('---')
        elif cmd == 'check': cmd_check(epid)
        elif cmd == 'render': cmd_render(epid)
