"""Word timings from the known script + the voiceover's silences (no transcription call)."""
import re, subprocess

ACRO1 = {'DOM': 1, 'CORS': 1, 'JSON': 2, 'NASA': 2, 'GIF': 1, 'RAM': 1, 'QUIC': 1, 'DevTools': 3, 'SYN': 1, 'ACK': 1, 'SYNACK': 2, 'QUIC': 1, 'CSSOM': 4, 'GPU': 3, 'CPU': 3, 'API': 3, 'URL': 3, 'UDP': 3}

def norm(w):
    return re.sub(r"[^a-z0-9']", '', w.lower().replace('’', "'"))

def syl(w):
    raw = re.sub(r"[^A-Za-z0-9]", '', w)
    if not raw: return 0
    if raw in ACRO1: return ACRO1[raw]
    if raw.isupper() and len(raw) <= 6:
        return sum(3 if ch == 'W' else 1 for ch in raw)
    if raw.isdigit(): return max(1, len(raw) * 2)
    s = raw.lower()
    n = len(re.findall(r'[aeiouy]+', s))
    if s.endswith('e') and n > 1 and not s.endswith(('le', 'ee', 'ye')): n -= 1
    if s.endswith(('ed',)) and n > 1 and not s.endswith(('ted', 'ded')): n -= 1
    return max(1, n)

def silences(wav, noise=-40, d=0.14):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', wav, '-af', f'silencedetect=noise={noise}dB:d={d}', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    dur = float(re.findall(r'Duration: (\d+):(\d+):([\d.]+)', r)[0][2]) + 60 * float(re.findall(r'Duration: (\d+):(\d+):([\d.]+)', r)[0][1])
    pairs = []
    for i, s in enumerate(st):
        e = en[i] if i < len(en) else dur
        pairs.append((s, e))
    return pairs, dur

def align(words, wav):
    """words: list of dicts {w, scene, strength} strength = punctuation after word (0 none, 1 comma, 3 sentence, 8 scene end)
    returns list of (start, end) per word."""
    sil, dur = silences(wav)
    # speech region
    sp0 = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
    sp1 = sil[-1][0] if sil and sil[-1][1] >= dur - 0.05 else dur
    gaps = [(s, e) for s, e in sil if s > sp0 + 0.01 and e < sp1 - 0.01]
    anchors = [(sp0, sp0)] + gaps + [(sp1, sp1)]   # anchor g: speech resumes at anchors[g][1], stops at anchors[g][0]
    K = len(anchors)
    # phrases
    phrases, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if w['strength'] > 0 or i == len(words) - 1:
            phrases.append((cur, w['strength'])); cur = []
    psyl = [sum(syl(words[i]['w']) for i in p) for p, _ in phrases]
    gapdur = [e - s for s, e in anchors]
    total_speech = (sp1 - sp0) - sum(e - s for s, e in gaps)
    rate = total_speech / max(1, sum(psyl))
    M = len(phrases)
    INF = 1e18
    dp = [[INF] * K for _ in range(M + 1)]
    bk = [[None] * K for _ in range(M + 1)]
    dp[0][0] = 0.0
    pre = [0]
    for s in psyl: pre.append(pre[-1] + s)
    for i in range(1, M + 1):
        for g in range(1, K):
            best, arg = INF, None
            for di in range(1, min(5, i) + 1):
                ip = i - di
                exp = rate * (pre[i] - pre[ip])
                merge = sum(min(phrases[j][1], 8) * (1.0 if phrases[j][1] >= 3 else 0.5) for j in range(ip, i - 1))
                for dg in range(1, min(6, g) + 1):
                    gp = g - dg
                    if dp[ip][gp] >= INF: continue
                    act = (anchors[g][0] - anchors[gp][1]) - sum(gapdur[s] for s in range(gp + 1, g))
                    if act <= 0: continue
                    c = ((act - exp) / (0.2 + 0.18 * exp)) ** 2
                    c += sum(1.2 + 4 * gapdur[s] for s in range(gp + 1, g))
                    c += merge
                    st = phrases[i - 1][1]
                    if g < K - 1 and st >= 3 and gapdur[g] < 0.3: c += 1.5
                    v = dp[ip][gp] + c
                    if v < best: best, arg = v, (ip, gp)
            dp[i][g], bk[i][g] = best, arg
    # backtrack
    i, g = M, K - 1
    groups = []
    while i > 0:
        ip, gp = bk[i][g]
        groups.append((ip, i, gp, g)); i, g = ip, gp
    groups.reverse()
    out = [None] * len(words)
    for ip, i, gp, g in groups:
        t0, t1 = anchors[gp][1], anchors[g][0]
        segs, a = [], t0
        for s in range(gp + 1, g):
            segs.append((a, anchors[s][0])); a = anchors[s][1]
        segs.append((a, t1))
        L = sum(b - a for a, b in segs)
        idx = [w for p, _ in phrases[ip:i] for w in p]
        sy = [max(1, syl(words[k]['w'])) for k in idx]
        S = sum(sy)
        def at(frac):
            x = frac * L
            for a, b in segs:
                if x <= b - a + 1e-9: return a + x
                x -= b - a
            return segs[-1][1]
        c = 0
        for k, s in zip(idx, sy):
            out[k] = [at(c / S), at((c + s) / S)]
            c += s
    return out, dur
