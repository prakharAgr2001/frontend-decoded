"""Web reels: HTML/CSS scenes animated per frame in headless Chrome, synced to the voiceover.
A reel lives in webreels/<id>/ : spec.py (EP dict + NARRATION list, one line per scene) and scenes.js (SCENES array).
Usage: python3 -m engine.webreel {text|check|render} WR01 [WR02 ...]
  text   -> exact TTS text (save the voiceover as vo/<ID>.wav)
  check  -> timing + one still per scene -> tmp/<ID>_sheet.jpg
  render -> out/<ID>_<slug>.mp4 (frames from Chrome + VO + generated music + sfx)
Uses engine.build for word alignment / pauses / caption chunks and its sfx bed. Does not modify engine.build."""
import importlib.util, io, json, math, os, re, subprocess, sys, wave
import numpy as np
from PIL import Image
import engine.build as B

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_orig_bed = B.bed
FPS = 30

def spec(epid):
    p = os.path.join(ROOT, 'webreels', epid.lower(), 'spec.py')
    s = importlib.util.spec_from_file_location('spec_' + epid, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.EP, [(None, line) for line in m.NARRATION]

def prep(epid):
    B.load = spec
    return B.prep(epid)

def page(epid, data):
    d = os.path.join(ROOT, 'webreels', epid.lower())
    web = os.path.join(ROOT, 'engine', 'web')
    html = f"""<!doctype html><html><head><meta charset="utf-8"><base href="file://{web}/">
<link rel="stylesheet" href="base.css"><style>{open(os.path.join(d, 'style.css')).read() if os.path.exists(os.path.join(d, 'style.css')) else ''}</style></head>
<body><div id="stage"><div id="glow"></div><div class="brand">TECH, <b>EXPLAINED</b></div><div id="scenes"></div>
<div id="cap"></div><div id="prog"></div><div id="flash"></div><div id="vig"></div><div id="grain"></div></div>
<script>const DATA={json.dumps(data)};</script><script src="base.js"></script>
<script>{open(os.path.join(d, 'scenes.js')).read()}</script></body></html>"""
    out = os.path.join(ROOT, 'tmp', f'{epid}_page.html'); open(out, 'w').write(html)
    return out

def data_for(ep, W_, spans, total, chunks):
    return dict(total=total, spans=[[a, b] for a, b in spans], words=[[w[0], w[1], w[2], w[3]] for w in W_],
                chunks=[[st, en, [[w[0], w[1], w[2]] for w in ch]] for st, en, ch in chunks])

def browser():
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
    return pw, b

def open_page(b, path):
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
    pg.goto('file://' + path); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    return pg, errs

def cmd_text(epid):
    ep, scenes = spec(epid)
    print(B.parse(scenes)[2])

def cmd_check(epid):
    ep, scenes, W_, spans, total, chunks = prep(epid)
    path = page(epid, data_for(ep, W_, spans, total, chunks))
    pw, b = browser(); pg, errs = open_page(b, path); thumbs = []
    for si, (t0, t1) in enumerate(spans):
        for q in (0.15, 0.55, 0.95):
            pg.evaluate(f'render({t0 + (t1 - t0) * q})')
        thumbs.append(Image.open(io.BytesIO(pg.screenshot(type='jpeg', quality=80))).resize((270, 480)))
    b.close(); pw.stop()
    if errs: print('PAGE ERRORS:', *errs[:5], sep='\n  ')
    cols = 5; rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new('RGB', (270 * cols, 480 * rows), 'white')
    for i, im in enumerate(thumbs): sheet.paste(im, ((i % cols) * 270, (i // cols) * 480))
    sheet.save(f'tmp/{epid}_sheet.jpg', quality=80)
    print(f'{epid}: {len(scenes)} scenes, {total:.1f}s ->', ' '.join(f'{a:.1f}' for a, _ in spans))

# ---------------------------------------------------------------- music: dark documentary pulse (generated, no copyright)
SR = 48000
def pulse_music(total, bpm=100, drops=(), seed=11):
    rng = np.random.default_rng(seed); n = int((total + 1.5) * SR); out = np.zeros(n, np.float32)
    b = 60 / bpm; tt = lambda L: np.arange(int(L * SR)) / SR
    def add(t, s, g):
        i = int(t * SR); j = min(n, i + len(s))
        if 0 <= i < n: out[i:j] += s[:j - i] * g
    k = tt(.45); kick = np.sin(2 * np.pi * np.cumsum(42 + 90 * np.exp(-k * 30)) / SR) * np.exp(-k * 7)
    tick = rng.normal(0, 1, int(.03 * SR)); tick = (tick - np.convolve(tick, np.ones(5) / 5, 'same')) * np.exp(-tt(.03) * 140)
    roots = [55.0, 55.0, 43.65, 49.0]                         # A A F G (minor, tense)
    pad_ch = [[110, 130.8, 164.8], [110, 130.8, 164.8], [87.3, 110, 130.8], [98, 123.5, 146.8]]
    t = 0.0; k_ = 0
    while t < total + 1:
        bar = int(t // (4 * b)) % 4; beat = k_ % 4
        if beat in (0, 2): add(t, kick, .9)
        for q in range(4): add(t + q * b / 4, tick, .16 if q % 2 else .07)
        L = tt(b); add(t, np.sin(2 * np.pi * roots[bar] * L) * np.exp(-L * 3) * np.minimum(1, L / .01), .5)   # sub pulse
        if beat == 0:
            L = tt(4 * b); env = np.minimum(1, L / 1.2) * np.exp(-L * .35)
            pad = sum(np.sin(2 * np.pi * f * L + .3 * np.sin(2 * np.pi * .2 * L)) for f in pad_ch[bar]) / 3
            add(t, pad * env, .22)
        t += b; k_ += 1
    g = np.ones(n, np.float32)
    for s0 in drops:                                           # silence before a reveal, then hit
        g[int(max(0, s0 - .45) * SR):int(s0 * SR)] = 0.0
    out *= g
    # riser into the first second (hook energy)
    L = tt(1.2); out[:len(L)] += (np.sin(2 * np.pi * np.cumsum(200 + 900 * (L / 1.2) ** 2) / SR) * (L / 1.2) ** 2 * .15).astype(np.float32)
    return out / (np.abs(out).max() + 1e-6) * .5

def _readwav(p):
    with wave.open(p) as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)
    if ch > 1: x = x.reshape(-1, ch).mean(1)
    x /= 32768
    if sr != SR: x = np.interp(np.arange(int(len(x) * SR / sr)) / SR, np.arange(len(x)) / sr, x).astype(np.float32)
    return x

def bed(epid, ep, sfx, total, spans):
    path = f'tmp/{epid}_bed.wav'
    _orig_bed(sfx, total, path)
    x = _readwav(path)
    drops = [spans[i][0] for i in ep.get('drop_scenes', ())]
    m = pulse_music(total, ep.get('bpm', 100), drops)[:len(x)]
    vo = _readwav(f'tmp/{epid}_vo.wav')
    env = np.convolve(np.abs(vo), np.ones(2400) / 2400, 'same')
    env = np.pad(env, (0, max(0, len(m) - len(env))))[:len(m)]
    duck = 1 - .55 * np.clip(env / (env.max() * .25 + 1e-6), 0, 1)
    y = x[:len(m)] + m * duck * ep.get('music_gain', .5)
    with wave.open(path, 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return path

def cmd_render(epid):
    ep, scenes, W_, spans, total, chunks = prep(epid)
    path = page(epid, data_for(ep, W_, spans, total, chunks))
    pw, b = browser(); pg, errs = open_page(b, path)
    vtmp = f'tmp/{epid}_v.mp4'
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', str(FPS), '-i', '-',
                           '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', vtmp], stdin=subprocess.PIPE)
    for f in range(int(math.ceil(total * FPS))):
        pg.evaluate(f'render({f / FPS})')
        ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
    ff.stdin.close(); ff.wait()
    sfx = set(tuple(x) for x in pg.evaluate('SFX')) | set((round(a, 3), 'whoosh') for a, _ in spans[1:])
    b.close(); pw.stop()
    if errs: print('PAGE ERRORS:', *errs[:5], sep='\n  ')
    bpath = bed(epid, ep, sfx, total, spans)
    slug = re.sub(r'[^A-Za-z0-9]+', '_', ep['short'].title()).strip('_')
    outp = f'out/{epid}_{slug}.mp4'; tmp = outp[:-4] + '.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vtmp, '-i', f'tmp/{epid}_vo.wav', '-i', bpath, '-filter_complex',
                    '[1:a]aresample=48000,apad[v];[2:a]aresample=48000[b];[v][b]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{total:.3f}', '-movflags', '+faststart', tmp], check=True)
    os.replace(tmp, outp)
    print('rendered', outp, f'{total:.1f}s')

if __name__ == '__main__':
    os.chdir(ROOT)
    cmd, ids = sys.argv[1], sys.argv[2:]
    for epid in ids:
        {'text': cmd_text, 'check': cmd_check, 'render': cmd_render}[cmd](epid)
