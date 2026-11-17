from engine.lib import *

EP = dict(id='S1E06', tag='S1 · E06', short='CDNs')

CITIES = [('Delhi', 470, 470), ('Mumbai', 330, 800), ('Kolkata', 760, 680), ('Bangalore', 450, 1040), ('Chennai', 560, 1060), ('Hyderabad', 500, 900)]

def india(c, a=1.0):
    pts = [(470, 330), (560, 380), (600, 470), (700, 560), (840, 600), (860, 680), (720, 720), (660, 860), (600, 1020), (520, 1200),
           (470, 1180), (420, 1040), (340, 900), (280, 780), (230, 700), (300, 620), (360, 540), (400, 430)]
    c.pen.poly(pts, fill=mix(PAPER, (225, 218, 200), a), outline=mix(PAPER, INK, a), w=5)

def hook(c):
    title(c, 'ONE FINAL. ONE STREAM.', 360, 0.1, 92)
    tm = c.T('millions')
    if c.on(tm):
        for r in range(8):
            for k in range(13):
                at = tm + (r * 13 + k) * 0.01
                if c.on(at): person(c.pen, 130 + k * 68, 560 + r * 80, 0.32 * c.B(at, 0.3), BLUE if (r + k) % 3 else ORANGE)
    to = c.T('one', 2)
    if c.on(to):
        node(c, 540, 1180, 300, 170, '1 server', to, 'server', fill=(255, 220, 220))
    tmelt = c.T('melt')
    if c.on(tmelt): stamp(c.cv, 540, 1330, 'IT WOULD MELT', 62, c.P(tmelt, 0.4), -4, RED)

def distance(c):
    india(c)
    node(c, 450, 1040, 220, 120, 'You', 0.0, None)
    ts = c.T('far')
    srv = node(c, 900, 360, 220, 150, 'Origin', ts, 'server', sub='far away')
    if c.on(ts):
        for k in range(2):
            t0 = ts + 0.4 + k * 1.3
            if c.on(t0):
                q = lin(c.t, t0, t0 + 1.2); q2 = q * 2 if q < 0.5 else 2 - q * 2
                x = 450 + (900 - 450) * q2; y = 980 + (430 - 980) * q2
                c.pen.circ(x, y, 18, fill=YEL, outline=INK, w=4)
        c.pen.line([(470, 980), (880, 440)], mix(PAPER, INK, 0.4), 4, False)
    tr = c.T('round')
    if c.on(tr): label(c, 540, 1250, 'every request pays the distance', tr, RED, WHITE, 32)

def cdn(c):
    india(c)
    te = c.T('edge')
    for i, (nm, x, y) in enumerate(CITIES):
        at = te + i * 0.15
        if c.on(at):
            c.sfx(at, 'tick'); s = c.B(at, 0.3)
            c.pen.circ(x, y, 26 * s, fill=YEL, outline=INK, w=4)
            c.pen.text(x, y - 46, nm, 'int', 24 * s, INK)
    tc = c.T('closest')
    if c.on(tc):
        person(c.pen, 380, 1150, 0.6, BLUE)
        arrow(c.pen, 400, 1110, 440, 1065, c.P(tc, 0.3), GRN, 6, 18)
        label(c, 760, 1250, 'served from the nearest edge', tc, GRN, WHITE, 30)
    title(c, 'CONTENT DELIVERY NETWORK', 300, c.T('CDN'), 70, hlcol=YEL)

def kirana(c):
    f = node(c, 540, 420, 330, 190, 'Factory', c.T('factory'), 'server', sub='= origin server')
    s = node(c, 540, 820, 330, 190, 'Kirana store', c.T('store'), 'db', fill=(255, 246, 214), sub='= CDN edge')
    tb = c.T('biscuits')
    if c.on(tb):
        person(c.pen, 540, 1230, 0.9, BLUE)
        link(c, (480, 1100, 600, 1230), s, tb, 0.4, GRN)
    tr = c.T('reorders')
    if c.on(tr): link(c, s, f, tr, 0.5, MUTE, txt_='only when it runs out', dash=True)

def hitmiss(c):
    o = node(c, 540, 380, 300, 170, 'Origin', 0.0, 'server')
    e = node(c, 540, 760, 300, 170, 'Edge', 0.0, 'db', fill=(255, 246, 214))
    th = c.T('hit')
    if c.on(th):
        stamp(c.cv, 230, 980, 'HIT · fast', 50, c.P(th, 0.35), -5, GRN)
        packet(c, e, (180, 1060, 280, 1160), th, th + 0.6, GRN, 'logo.png')
    tm = c.T('miss')
    if c.on(tm):
        stamp(c.cv, 850, 980, 'MISS', 50, c.P(tm, 0.35), 5, RED)
        packet(c, e, o, tm + 0.5, tm + 1.1, YEL, 'GET')
        packet(c, o, e, tm + 1.3, tm + 1.9, GRN, 'logo.png')
    tk = c.T('keeps')
    if c.on(tk): txt(c, 540, 1180, 'fetched once → cached → served to everyone after', tk, 'int', 32, INK)

def proof(c):
    box = panel(c, 70, 320, 1010, 1080, tabs=('Headers', 'Preview', 'Response'), active=0, dy=(1 - c.P(0, 0.45)) * 900)
    rows = [('content-type', 'image/png', None), ('cache-control', 'max-age=31536000', None),
            ('x-cache', 'HIT', 'x'), ('cf-cache-status', 'HIT', 'cf'), ('age', '86400', 'age')]
    for i, (k, v, kw) in enumerate(rows):
        y = 480 + i * 105
        c.pen.text(110, y, k + ':', 'monob', 32, CYAN, 'lm'); c.pen.text(470, y, v, 'mono', 32, WHITE, 'lm')
        if kw and c.on(c.T(kw)):
            p = c.P(c.T(kw), 0.3); c.sfx(c.T(kw), 'tick')
            c.pen.rr(96, y - 36, 96 + 880 * p, y + 36, 10, outline=YEL, w=4)
    tl = c.T('long')
    if c.on(tl): txt(c, 540, 1200, 'age = seconds since the edge cached it', tl, 'int', 34, INK)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    tn = c.T('new')
    node(c, 290, 620, 320, 220, 'logo.png', tn, 'doc', sub='you deployed v2')
    node(c, 790, 620, 320, 220, 'logo.png', c.T('old'), 'doc', fill=(255, 220, 220), sub='users still see v1')
    te = c.T('edges')
    if c.on(te): txt(c, 540, 820, 'edges are serving their cached copy', te, 'int', 34, RED)
    tv = c.T('versioned')
    if c.on(tv):
        darkcard(c.pen, 150, 920, 930, 1020)
        c.pen.text(540, 970, 'logo.3f9a2c.png', 'monob', 44 * c.B(tv, 0.4), (120, 220, 150))
    tp = c.T('purge')
    if c.on(tp): label(c, 540, 1120, 'or purge the CDN cache', tp, YEL, INK, 34)

SCENES = [
    (hook, "During a big cricket final, millions of people hit play at the same moment. If every one of them had to reach one server in one city, it would melt."),
    (distance, "And distance costs time. Every request to a far away server pays for that round trip."),
    (cdn, "A CDN, a content delivery network, keeps copies of files on edge servers in many cities. You get the copy from the edge closest to you."),
    (kirana, "Think of your local kirana store. You don't drive to the factory for biscuits. The store keeps stock nearby, and only reorders from the warehouse when it runs out."),
    (hitmiss, "If the edge already has the file, that's a cache hit, and it's fast. If not, it's a miss. The edge fetches it from the origin once, keeps a copy, and serves everyone after you."),
    (proof, "Check the response headers on an image from a big site. Headers like x-cache, cf-cache-status, or age tell you a CDN served it, and how long it's been cached."),
    (gotcha, "Interview trap: you deploy a new logo, but users still see the old one. The edges are serving cached copies. Fix it with versioned file names, or purge the CDN cache."),
    (scene_next('S1 · E07', 'INTERVIEW Qs', 'URL to pixels: test yourself', 'interview', 'pixels'),
     "Next: interview questions on everything from URL to pixels. Comment NOTES for the cheat sheet."),
]
