from engine.lib import *

EP = dict(id='S1E02', tag='S1 · E02', short='DNS')

def hook(c):
    card(c.pen, 220, 380, 860, 520, 24, WHITE, 10, 5)
    c.pen.text(540, 450, 'google.com', 'osw', 84 * c.B(0, 0.4), INK)
    tn = c.T('numbers')
    if c.on(tn):
        c.sfx(tn, 'pop')
        darkcard(c.pen, 220, 800, 860, 940)
        c.pen.text(540, 870, '142.250.x.x', 'monob', 70 * c.B(tn, 0.4), (120, 220, 150))
    tt = c.T('translates')
    if c.on(tt):
        arrow(c.pen, 540, 540, 540, 780, c.P(tt, 0.4), INK, 7, 26)
        c.sfx(tt, 'thud'); s = c.B(tt, 0.4)
        c.pen.circ(540, 660, 60 * s, fill=YEL, outline=INK, w=5); c.pen.text(540, 660, '?', 'osw', 90 * s, INK)
    txt(c, 540, 1080, 'humans → names   ·   computers → numbers', c.T('only'), 'int', 34, MUTE)

def phonebook(c):
    def phone(cx, rows, hi_at, head):
        card(c.pen, cx - 200, 330, cx + 200, 1180, 40, WHITE, 12, 6)
        c.pen.text(cx, 400, head, 'int', 30, MUTE)
        for i, (a, b) in enumerate(rows):
            y = 500 + i * 150
            hit = i == 0 and c.on(hi_at)
            if hit: c.pen.rr(cx - 180, y - 60, cx + 180, y + 60, 16, fill=YEL)
            c.pen.text(cx - 160, y - 18, a, 'intx', 36, INK, 'lm')
            c.pen.text(cx - 160, y + 24, b, 'mono', 26, INK if hit else MUTE, 'lm')
            c.pen.line([(cx - 170, y + 70), (cx + 170, y + 70)], LIGHT, 3, False)
    tm = c.T('Mom')
    phone(290, [('Mom', '+91 98xxx xxx01'), ('Rahul', '+91 99xxx xxx44'), ('Office', '080 xxxx xx10')], tm, 'CONTACTS')
    if c.on(tm): c.sfx(tm, 'tick')
    td = c.T('domain')
    if c.on(td - 0.01):
        c.sfx(td, 'whoosh')
        phone(790, [('google.com', '142.250.x.x'), ('youtube.com', '142.250.x.x'), ('flipkart.com', '103.x.x.x')], c.T('returns'), 'DNS')
        arrow(c.pen, 500, 760, 580, 760, c.P(td, 0.3), INK, 7, 22)
    tp = c.T('phonebook')
    if c.on(tp): stamp(c.cv, 540, 1270, "THE INTERNET'S PHONEBOOK", 52, c.P(tp, 0.4), -3, BLUE)

def chain(c):
    you = node(c, 190, 760, 210, 200, 'You', 0.0, 'laptop')
    res = node(c, 500, 760, 230, 200, 'Resolver', c.T('resolver'), 'server', fill=(255, 246, 214))
    root = node(c, 860, 420, 240, 190, 'Root', c.T('root'), 'globe')
    com = node(c, 860, 760, 240, 190, '.com', c.T('com'), 'server')
    gns = node(c, 860, 1100, 240, 190, 'Google NS', c.T('Google'), 'db')
    link(c, you, res, c.T('resolver') + 0.2)
    tr, tc, tg, tret = c.T('root'), c.T('com'), c.T('Google'), c.T('return')
    packet(c, res, root, tr, tr + 0.6, YEL, '?')
    link(c, root, res, tr + 0.7, 0.4, MUTE, txt_='ask .com', off=-28)
    packet(c, res, com, tc, tc + 0.6, YEL, '?')
    link(c, com, res, tc + 0.7, 0.4, MUTE, txt_='ask Google', off=-28)
    packet(c, res, gns, tg, tg + 0.6, YEL, '?')
    if c.on(tret):
        link(c, gns, res, tret, 0.4, GRN, txt_='142.250.x.x', off=-28)
        packet(c, res, you, tret + 0.6, tret + 1.2, GRN, 'IP')

def ttl(c):
    title(c, 'TTL = TIME TO LIVE', 360, c.T('TTL'), 96, hlcol=YEL)
    for i, (ic, name, kw) in enumerate([('laptop', 'Browser', 'browser'), ('cpu', 'OS', 'operating'), ('server', 'Resolver', 'resolver')]):
        at = c.T(kw); cx = 210 + i * 330
        node(c, cx, 640, 270, 230, name, at, ic, sub='cached answer')
        if c.on(at):
            frac = 1 - lin(c.t, at, at + 9)
            ring(c, cx, 920, 70, frac, YEL, 14)
            c.pen.text(cx, 920, f'{int(300 * frac)}s', 'monob', 32, INK)
    txt(c, 540, 1110, 'until it hits zero → reuse, no lookup', c.T('expires'), 'int', 38, INK)

def proof(c):
    lines = [(c.T('nslookup'), '$ nslookup google.com', CYAN), (c.T('nslookup') + 1.2, 'Name:    google.com', None),
             (c.T('IP'), 'Address: 142.250.x.x', (120, 220, 150))]
    console(c, 80, 300, 1000, 640, lines, dy=(1 - c.P(0, 0.45)) * 900)
    td = c.T('DevTools')
    if c.on(td):
        txt(c, 110, 760, 'Network → first request → Timing', td, 'int', 34, INK, 'lm')
        tr = c.T('Reload')
        for j, (lab, w, y) in enumerate([('DNS Lookup  ·  1st load', 260, 860), ('DNS Lookup  ·  reload', 4, 1010)]):
            at = td + 0.5 if j == 0 else tr
            if not c.on(at): continue
            c.sfx(at, 'tick')
            c.pen.text(110, y - 34, lab, 'mono', 28, INK, 'lm')
            c.pen.rect(110, y, 110 + max(4, w * c.P(at, 0.5)), y + 44, fill=PURPLE, outline=INK, w=3)
            c.pen.text(130 + max(4, w), y + 22, '38 ms' if j == 0 else '0 ms', 'monob', 30, INK, 'lm')

def gotcha(c):
    tq = c.T('Interview')
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(tq, 0.4), -4, RED); c.sfx(tq, 'thud')
    old = node(c, 260, 620, 250, 200, 'Old server', c.T('move'), 'server')
    new = node(c, 820, 620, 250, 200, 'New server', c.T('new'), 'server', fill=(220, 245, 225))
    tu = c.T('users')
    if c.on(tu):
        for i in range(3):
            person(c.pen, 400 + i * 140, 1040, 0.7 * c.B(tu + i * 0.1, 0.3), BLUE if i < 2 else ORANGE)
        link(c, (360, 900, 600, 1050), old, tu + 0.4, 0.5, RED, txt_='old cached IP')
        link(c, (620, 900, 760, 1050), new, tu + 0.6, 0.5, GRN)
    tc = c.T('Cached')
    if c.on(tc): stamp(c.cv, 540, 1170, 'CACHED DNS', 56, c.P(tc, 0.35), -6, RED)
    tl = c.T('lower')
    if c.on(tl): label(c, 540, 1310, 'lower the TTL before a migration', tl, YEL, INK, 34)

SCENES = [
    (hook, "Computers don't understand google dot com. They only understand IP addresses, long strings of numbers. So who translates the name into the number?"),
    (phonebook, "Think of your phone's contacts. You tap Mom, and the phone dials her number. You type a domain, and DNS returns its IP address. DNS is the internet's phonebook."),
    (chain, "If nobody nearby knows the answer, your resolver walks a chain. The root servers point it to the dot com servers. Those point it to Google's own name servers. And they finally return the IP address."),
    (ttl, "Walking that chain every time would be slow. So every answer comes with a TTL, a time to live. Until it expires, your browser, your operating system and your resolver all reuse the cached answer."),
    (proof, "See it yourself. In a terminal, type nslookup google dot com, and the IP comes back. In DevTools, the first request's timing shows the DNS lookup. Reload, and it often drops to zero."),
    (gotcha, "Interview question: you move your site to a new server, but some users keep hitting the old one for hours. Why? Cached DNS. They keep the old answer until its TTL runs out. That's why teams lower the TTL before a migration."),
    (scene_next('S1 · E03', 'TCP HANDSHAKE', 'the phone call before every request', 'handshake', 'phone'),
     "Next: the TCP handshake, the phone call before every request. Comment NOTES for the cheat sheet."),
]
