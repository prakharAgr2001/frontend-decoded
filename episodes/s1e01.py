from engine.lib import *

EP = dict(id='S1E01', tag='S1 · E01', short='URL TO PIXELS')

STEPS = [('book', 'DNS', 'name  →  IP address', 'DNS'), ('phone', 'TCP', 'open a connection', 'TCP'),
         ('lock', 'TLS', 'lock it (encrypt)', 'TLS'), ('doc', 'HTTP', 'ask for the page', 'HTTP'),
         ('eye', 'RENDER', 'HTML  →  pixels', 'pixels')]

def hook(c):
    browser(c, 90, 290, 990, 600, url='')
    addressbar(c, 130, 400, 950, typed_text(c, 'google.com', c.T('type'), 0.1), True, 46)
    te = c.T('Enter')
    if c.on(te):
        c.sfx(te, 'thud'); s = c.B(te, 0.35)
        c.pen.rr(540 - 150 * s + 6, 690 - 50 * s + 8, 540 + 150 * s + 6, 690 + 50 * s + 8, 18 * s, fill=INK)
        c.pen.rr(540 - 150 * s, 690 - 50 * s, 540 + 150 * s, 690 + 50 * s, 18 * s, fill=YEL, outline=INK, w=5)
        c.pen.text(540, 690, 'ENTER', 'osw', 56 * s, INK)
    ts = c.T('second')
    if c.on(ts):
        c.sfx(ts, 'pop')
        ring(c, 300, 1010, 120, lin(c.t, ts, ts + 1.0), RED, 22)
        c.pen.text(300, 1010, '< 1s', 'osw', 84 * c.B(ts, 0.4), INK)
    tf = c.T('five')
    bignum(c, 770, 990, '5', tf, 260)
    txt(c, 770, 1170, 'separate journeys', tf + 0.2, 'int', 40, INK)

def journeys(c):
    for i, (ic, name, sub, kw) in enumerate(STEPS):
        at = c.T(kw); y = 360 + i * 195
        if not c.on(at - 0.01):
            c.pen.rr(120, y - 75, 960, y + 75, 24, outline=GREY, w=4); continue
        s = c.P(at, 0.4); c.sfx(at, 'pop')
        dx = (1 - s) * 60
        card(c.pen, 120 + dx, y - 75, 960 + dx, y + 75, 24, WHITE if i % 2 else (255, 246, 214), 10, 5)
        c.pen.circ(205 + dx, y, 52, fill=YEL, outline=INK, w=4)
        icon(c.pen, ic, 205 + dx, y, 0.62)
        c.pen.text(290 + dx, y - 22, name, 'osw', 64, INK, 'lm')
        c.pen.text(290 + dx, y + 36, sub, 'ints', 32, MUTE, 'lm')
        c.pen.text(920 + dx, y, str(i + 1), 'osw', 70, mix(WHITE, GREY, s), 'rm')
        if i > 0: arrow(c.pen, 205, y - 195 + 78, 205, y - 78, c.P(at, 0.3), INK, 5, 16)

def parcel(c):
    pill(c.pen, 290, 320, 'A PARCEL', c.B(0, 0.35), WHITE, INK, 30)
    pill(c.pen, 800, 320, 'YOUR BROWSER', c.B(0.2, 0.35), INK, WHITE, 30, outline=None)
    rows = [('Find the address', 'DNS', 'address'), ('Call ahead', 'TCP', 'Call'), ('Seal the box', 'TLS', 'Seal'),
            ('Hand it over', 'HTTP', 'Hand'), ('Unpack it', 'RENDER', 'unpack')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw); y = 470 + i * 175
        if not c.on(at - 0.01): continue
        s = c.B(at, 0.4); c.sfx(at, 'pop')
        card(c.pen, 90, y - 60 * s, 520, y + 60 * s, 20, WHITE, 8, 4)
        c.pen.text(305, y, a, 'intx', 40 * s, INK)
        arrow(c.pen, 540, y, 640, y, c.P(at + 0.15, 0.3), INK, 6, 20)
        c.pen.rr(660, y - 55 * s, 990, y + 55 * s, 55 * s, fill=YEL, outline=INK, w=4)
        c.pen.text(825, y, b, 'osw', 60 * s, INK)

SEGS = [('DNS Lookup', 0.10, PURPLE, 'DNS'), ('Initial connection', 0.16, ORANGE, 'initial'), ('SSL', 0.13, (200, 110, 220), 'SSL'),
        ('Waiting for server response', 0.36, GRN, 'waiting'), ('Content Download', 0.12, BLUE, 'content')]

def proof(c):
    box = panel(c, 70, 300, 1010, 1180, tabs=('Headers', 'Preview', 'Timing'), active=2, dy=(1 - c.P(0, 0.45)) * 900)
    acc = 0.0
    for i, (name, d, col, kw) in enumerate(SEGS):
        at = c.T(kw); y = 500 + i * 135
        c.pen.text(110, y - 30, name, 'mono', 28, WHITE if c.on(at) else (80, 86, 96), 'lm')
        x0 = 110 + 860 * acc; w = 860 * d * c.P(at, 0.5)
        if c.on(at): c.sfx(at, 'tick')
        if w > 1: c.pen.rect(x0, y, x0 + w, y + 40, fill=col)
        acc += d
    tj = c.T('journeys')
    if c.on(tj): stamp(c.cv, 540, 1265, 'ONE BAR = ONE JOURNEY', 46, c.P(tj, 0.35), -3, YEL)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    for i, (ic, name, kw) in enumerate([('laptop', 'Browser', 'browser'), ('cpu', 'OS', 'operating'), ('server', 'Resolver', 'resolver')]):
        b = node(c, 220 + i * 320, 600, 260, 230, name, c.T(kw), ic, sub='DNS cache')
        if c.on(c.T(kw) + 0.4): check(c.pen, 220 + i * 320 + 105, 500, 0.8, GRN, 8, c.P(c.T(kw) + 0.4, 0.3))
    ts = c.T('second')
    if c.on(ts):
        for j, (lab, segs, y) in enumerate([('1st visit', [0.10, 0.16, 0.13, 0.36, 0.12], 860), ('Repeat', [0.0, 0.0, 0.0, 0.36, 0.12], 1010)]):
            at = ts + j * 0.6; p = c.P(at, 0.5)
            if not c.on(at): continue
            c.sfx(at, 'pop')
            c.pen.text(110, y - 40, lab, 'int', 34, INK, 'lm')
            x = 110
            for k, d in enumerate(segs):
                w = 860 * d * p
                if w > 1: c.pen.rect(x, y, x + w, y + 50, fill=SEGS[k][2], outline=INK, w=3)
                x += w
            c.pen.text(970, y - 40, f'{int(sum(segs) * 400)} ms', 'monob', 32, INK, 'rm')
    tf = c.T('first')
    if c.on(tf): hl(c.pen, 100, 1090, 980, 1110, c.P(tf, 0.4), RED)

SCENES = [
    (hook, "You type google dot com and press Enter. In under a second, the page is there. But in that second, your browser just made five separate journeys. Let's follow them."),
    (journeys, "First, DNS turns the name into an address. Then TCP opens a connection to that address. Then TLS locks it, so nobody can read along. Then HTTP asks for the page. And finally, the browser turns the HTML it gets back into pixels."),
    (parcel, "Think of sending a parcel. Find the address. Call ahead, so someone's home. Seal the box. Hand it over. Then unpack it at the other end."),
    (proof, "You can watch this happen. In DevTools, open the Network tab, reload, and look at the first request's timing. DNS lookup. Initial connection. SSL. Waiting for the server. Content download. Each bar is one of those journeys."),
    (gotcha, "Interview trap: people say DNS happens on every visit. It doesn't. Your browser, your operating system and your network's resolver all cache the answer. So a second visit often skips DNS and the connection setup. That's why the first load is usually the slowest."),
    (scene_try([('Open', 'Open DevTools', 'F12  ·  Cmd + Opt + I'), ('reload', 'Network tab → reload', 'any website'),
                ('timing', 'Click the first request', 'Timing tab shows every stage'), ('compare', 'Reload and compare', 'DNS & connection shrink')]),
     "Try it. Open DevTools, reload any site, and check the timing of the first request. Then reload again and compare."),
    (scene_next('S1 · E02', 'DNS', "the internet's phonebook", 'DNS', 'phonebook'),
     "Next: DNS, the internet's phonebook. Comment NOTES for the cheat sheet."),
]
