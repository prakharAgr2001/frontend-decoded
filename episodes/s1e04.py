from engine.lib import *

EP = dict(id='S1E04', tag='S1 · E04', short='HTTPS & THE PADLOCK')

def hook(c):
    box = browser(c, 90, 300, 990, 560, url='')
    c.pen.rr(250, 315, 956, 355, 20, fill=(236, 233, 226))
    icon(c.pen, 'lock', 285, 335, 0.35, INK, YEL)
    c.pen.text(310, 336, 'https://yourbank.example', 'intm', 26, INK, 'lm')
    tp = c.T('padlock')
    if c.on(tp):
        s = c.B(tp, 0.5); c.sfx(tp, 'pop')
        c.pen.circ(540, 820, 170 * s, fill=YEL, outline=INK, w=6)
        icon(c.pen, 'lock', 540, 820, 2.4 * s, INK, WHITE)
    tt = c.T('three')
    bignum(c, 540, 1110, '3 PROMISES', tt, 110, INK)
    tn = c.T('one')
    if c.on(tn): txt(c, 540, 1230, 'most devs can name only one', tn, 'int', 36, RED)

def plain(c):
    x0 = 100
    card(c.pen, x0, 400, 700, 680, 18, WHITE, 10, 5)
    c.pen.text(130, 450, 'POSTCARD', 'int', 26, MUTE, 'lm')
    tr = c.T('read')
    if c.on(tr): hl(c.pen, 120, 580, 560, 625, c.P(tr + 0.2, 0.4), (255, 150, 150))
    c.pen.text(130, 530, 'user: prakhar', 'monob', 38, INK, 'lm')
    c.pen.text(130, 600, 'password: hunter2', 'monob', 38, INK, 'lm')
    if c.on(tr):
        person(c.pen, 870, 700, 1.3 * c.B(tr, 0.4), ORANGE)
        icon(c.pen, 'eye', 870, 470, 0.9 * c.B(tr, 0.4))
        txt(c, 870, 760, 'café Wi-Fi snooper', tr, 'int', 30, INK)
    tc = c.T('change')
    if c.on(tc):
        stamp(c.cv, 540, 900, 'READ IT · CHANGE IT', 60, c.P(tc, 0.4), -3, RED)
    txt(c, 540, 1060, 'plain HTTP = a postcard anyone can read', c.T('Without'), 'int', 36, INK)

def promises(c):
    title(c, 'HTTPS = HTTP + TLS', 340, c.T('TLS'), 100, hlcol=YEL)
    for i, (ic, name, sub, kw) in enumerate([('lock', 'Encryption', 'nobody can read it', 'Encryption'),
                                             ('shield', 'Integrity', 'nobody can change it', 'Integrity'),
                                             ('eye', 'Authentication', "it's really that site", 'authentication')]):
        at = c.T(kw); y = 560 + i * 230
        if not c.on(at - 0.01): continue
        s = c.P(at, 0.4); c.sfx(at, 'pop'); dx = (1 - s) * 80
        card(c.pen, 110 + dx, y - 90, 970 + dx, y + 90, 24, (255, 246, 214) if i == 2 else WHITE, 10, 5)
        c.pen.circ(210 + dx, y, 62, fill=YEL, outline=INK, w=4); icon(c.pen, ic, 210 + dx, y, 0.75)
        c.pen.text(310 + dx, y - 24, name, 'osw', 62, INK, 'lm')
        c.pen.text(310 + dx, y + 36, sub, 'ints', 32, MUTE, 'lm')

def cert(c):
    title(c, 'CHAIN OF TRUST', 330, 0.1, 100)
    rc = node(c, 540, 560, 420, 150, 'Root CA', c.T('authority'), 'shield', sub='already in your browser')
    ic = node(c, 540, 820, 420, 150, 'Intermediate CA', c.T('authority') + 0.6, 'doc', sub='signed by root')
    sc = node(c, 540, 1080, 420, 150, 'yourbank.example', c.T('certificate'), 'lock', fill=(255, 246, 214), sub='signed by intermediate')
    link(c, rc, ic, c.T('authority') + 0.5); link(c, ic, sc, c.T('authority') + 1.1)
    tt = c.T('trust')
    if c.on(tt): check(c.pen, 840, 1080, 1.4, GRN, 12, c.P(tt, 0.4)); c.sfx(tt, 'ding')

def cost(c):
    title(c, 'THE TLS HANDSHAKE', 340, 0.1, 96)
    y = 640
    for j, (lab, w, col, kw) in enumerate([('TCP  ·  1 round trip', 330, ORANGE, 'top'), ('TLS 1.3  ·  1 round trip', 330, PURPLE, 'one'),
                                            ('then your request', 260, GRN, 'Then')]):
        at = c.T(kw)
        if not c.on(at): continue
        c.sfx(at, 'pop'); x0 = 110 + j * 0
        yy = y + j * 170
        c.pen.text(110, yy - 40, lab, 'int', 34, INK, 'lm')
        xs = 110 + sum(r[1] for r in [(0, 330), (0, 330)][:j]) if j < 2 else 770
        c.pen.rect(xs, yy, xs + w * c.P(at, 0.5) * (0.5 if j == 2 else 1), yy + 56, fill=col, outline=INK, w=3)
    tb = c.T('older')
    if c.on(tb): txt(c, 540, 1180, 'TLS 1.2 needed 2 round trips', tb, 'int', 36, MUTE)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    browser(c, 120, 470, 960, 900, url='')
    c.pen.rr(280, 485, 926, 525, 20, fill=(236, 233, 226))
    icon(c.pen, 'lock', 312, 505, 0.32, INK, YEL)
    c.pen.text(338, 506, 'https://yourbank-login.example', 'intm', 25, INK, 'lm')
    c.pen.text(540, 650, 'Login to Your Bank', 'intx', 48, INK)
    c.pen.rr(300, 720, 780, 790, 14, outline=GREY, w=4); c.pen.rr(300, 810, 780, 880, 14, outline=GREY, w=4)
    tp = c.T('phishing')
    if c.on(tp): stamp(c.cv, 760, 760, 'FAKE SITE', 64, c.P(tp, 0.4), 8, RED)
    tv = c.T('private')
    if c.on(tv):
        label(c, 540, 1060, 'padlock = private, NOT safe', tv, YEL, INK, 40)

SCENES = [
    (hook, "That little padlock in your address bar is making three promises. Most developers can only name one."),
    (plain, "Without HTTPS, everything you send travels as plain text, like a postcard. Anyone on the same café Wi-Fi could read your password, or even change the page before it reaches you."),
    (promises, "HTTPS is just HTTP sent through TLS, and TLS promises three things. Encryption: nobody can read it. Integrity: nobody can change it. And authentication: you're really talking to that site, not an impostor."),
    (cert, "Authentication comes from a certificate. The site presents a certificate signed by a certificate authority your browser already trusts. That's the chain of trust."),
    (cost, "Setting this up is the TLS handshake, on top of TCP's. With TLS one point three, it takes just one extra round trip. Then your request finally goes out. The older version needed two."),
    (gotcha, "Interview trap: does the padlock mean a site is safe? No. It means the connection is private. A phishing site can have a perfectly valid padlock."),
    (scene_try([('padlock', 'Click the padlock', 'on any HTTPS site'), ('certificate', 'Open the certificate', '“Connection is secure” → details'),
                ('chain', 'Read the chain', 'root → intermediate → site')], 'Try'),
     "Try it. Click the padlock on any site, open the certificate, and read the whole chain."),
    (scene_next('S1 · E05', 'HTTP 1 · 2 · 3', 'why YouTube runs on HTTP/3', 'HTTP', 'YouTube'),
     "Next: HTTP one, two and three, and why YouTube runs on three. Comment NOTES for the cheat sheet."),
]
