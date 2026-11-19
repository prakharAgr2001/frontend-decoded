from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E11', tag='S3 · E11', short='RESOURCE HINTS', hook='tell the browser what is coming')

def hook(c):
    title(c, 'THE LATE DISCOVERY', 330, 0.1, 90)
    steps = [('HTML', 'HTML'), ('CSS', 'CSS'), ('font!', 'finds'), ('connect…', 'connecting')]
    for k, (nm, kw) in enumerate(steps):
        t = c.T(kw); y = 520 + k * 160
        if not c.on(t): continue
        xa = 110 + k * 160; w = [260, 240, 200, 300][k]
        p = c.P(t, 0.4); c.sfx(t, 'pop')
        c.pen.rect(xa, y - 45, xa + w * p, y + 45, fill=[GRN, PURPLE, YEL, RED][k], outline=INK, w=4)
        c.pen.text(xa + 20, y, nm, 'intx', 34, WHITE if k in (1, 3) else INK, 'lm')
    th = c.T('half')
    if c.on(th): stamp(c.cv, 640, 1200, '~0.5 s JUST CONNECTING', 56, c.P(th, 0.35), -3, RED); c.sfx(th, 'thud')

def hints(c):
    title(c, 'RESOURCE HINTS', 330, c.T('Resource'), 110, hlcol=YEL)
    for k, (nm, kw, col) in enumerate((('preconnect', 'preconnect', BLUE), ('dns-prefetch', 'dns', TEAL), ('preload', 'preload', RED), ('prefetch', 'prefetch', GRN))):
        t = c.T(kw); y = 560 + k * 170
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        c.pen.rr(200, y - 60 * s, 880, y + 60 * s, 30, fill=col, outline=INK, w=5)
        c.pen.text(540, y, f'rel="{nm}"', 'monob', 44 * s, WHITE)

def booking(c):
    title(c, 'CALL AHEAD', 330, c.T('calling'), 110)
    rows(c, 110, 540, [('books', 'preconnect', 'book the table', BLUE), ('definitely', 'preload', "order the dish you'll eat right away", RED),
                       ('tomorrow', 'prefetch', "order tomorrow's lunch", GRN)], 220, 860, 160, 50, 32)

def preconnect(c):
    title(c, 'PRECONNECT', 330, c.T('Preconnect'), 110, hlcol=(200, 220, 255))
    for k, (nm, kw) in enumerate((('DNS', 'DNS'), ('TCP', 'TCP'), ('TLS', 'TLS'))):
        pill(c.pen, 290 + k * 250, 500, nm, c.B(c.T(kw), 0.35), (200, 220, 255), INK, 44)
    tr = c.T('round')
    if c.on(tr): txt(c, 540, 600, 'done early · saves round trips', tr, 'intx', 38, GRN)
    code(c, 40, 700, 1040, 960, ['<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>', '<link rel="dns-prefetch" href="https://cdn.example.com">'],
         c.T('prefetch') - 0.5, 0.2, 21, 'index.html', lang='html', marks=[(1, c.T('cheap'), (60, 110, 70))])
    tc = c.T('cheap')
    if c.on(tc): label(c, 540, 1070, 'dns-prefetch = DNS only · cheap fallback', tc, WHITE, INK, 32)

def preload(c):
    title(c, 'PRELOAD', 330, c.T('Preload'), 110, hlcol=(255, 190, 190))
    rows(c, 110, 500, [('font', 'a font buried in CSS', None, RED), ('JavaScript', 'a hero image set by JavaScript', None, RED)], 130, 860, 100, 38)
    code(c, 40, 760, 1040, 1000, ['<link rel="preload" href="/fonts/inter.woff2"', '      as="font" type="font/woff2" crossorigin>'], c.T('downloads') - 0.4, 0.15, 26, 'index.html', lang='html')
    th = c.T('high')
    if c.on(th): label(c, 540, 1100, 'fetched now · high priority', th, (255, 210, 210), INK, 34)

def prefetch(c):
    title(c, 'PREFETCH', 330, c.T('Prefetch'), 110, hlcol=(200, 240, 200))
    a = node(c, 270, 620, 340, 160, 'cart page', c.T('next'), 'doc')
    b = node(c, 810, 620, 340, 160, 'checkout.js', c.T('checkout'), 'doc', fill=(215, 240, 215))
    tl = c.T('lowest')
    if c.on(tl): link(c, a, b, tl, txt_='Lowest priority', dash=True)
    ti = c.T('idle')
    if c.on(ti): txt(c, 540, 860, 'only when the browser is idle', ti, 'intx', 38, INK)
    code(c, 60, 960, 1020, 1140, ['<link rel="prefetch" href="/checkout.js">'], c.T('checkout') - 0.3, 0.1, 28, 'cart.html', lang='html')

def proof(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Network',), dy=(1 - c.P(0, 0.45)) * 900)
    tp = c.T('Priority')
    if c.on(tp):
        c.pen.text(100, 470, 'Name', 'int', 26, (150, 156, 166), 'lm'); c.pen.text(760, 470, 'Priority', 'int', 26, YEL, 'lm')
    th = c.T('top')
    netrows(c, 100, 550, 1000, [(th, 'inter.woff2', ['High'], (90, 40, 40)), (th + 0.2, 'hero.avif', ['High'], (90, 40, 40)), (tp + 0.3, 'app.js', ['Low']),
                                (c.T('Lowest'), 'checkout.js', ['Lowest'], (40, 80, 50))], 28, 80, [760])
    if c.on(th): txt(c, 540, 1130, 'preloaded files jump the queue', th, 'intx', 36, INK)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    title(c, 'PRELOAD EVERYTHING?', 480, c.T('everything'), 84)
    tc = c.T('competes')
    if c.on(tc):
        for k in range(7):
            pill(c.pen, 200 + (k % 4) * 230, 620 + (k // 4) * 80, 'preload', c.B(tc + k * 0.06, 0.3), (255, 210, 210), INK, 26)
    tw = c.T('warns')
    if c.on(tw): console(c, 50, 800, 1030, 1000, [(tw, 'preloaded but not used within', YEL), (tw + 0.2, 'a few seconds of load', YEL)])
    tt = c.T('twice')
    if c.on(tt): label(c, 540, 1110, 'font preload without crossorigin = downloaded twice', tt, YEL, INK, 30)

SCENES = [
    (hook, "Your page needs a web font. But the browser only finds out after it downloads the HTML, then the CSS. Only then does it start connecting to the font server. Half a second, gone."),
    (hints, "Resource hints let you tell the browser what's coming. Four matter: preconnect, dns prefetch, preload, and prefetch."),
    (booking, "It's like calling a restaurant ahead. Preconnect books the table. Preload orders the dish you'll definitely eat right away. Prefetch orders tomorrow's lunch."),
    (preconnect, "Preconnect does the DNS lookup, TCP and TLS early, for another origin, saving a round trip or three. DNS prefetch does only the lookup, a cheap fallback."),
    (preload, "Preload fetches a file this page will definitely need, but would discover late. A font buried in CSS. A hero image set by JavaScript. It downloads now, at high priority."),
    (prefetch, "Prefetch grabs something for the next page, like the checkout code while you browse the cart. It runs at the lowest priority, only when the browser is idle."),
    (proof, "In the Network panel, add the Priority column. Preloaded files jump to the top with High. Prefetched ones sit at Lowest."),
    (gotcha, "Interview trap: just preload everything. Every preload competes for bandwidth with what the page needs first. Chrome even warns in the console when a preload isn't used within a few seconds. And a font preload without crossorigin gets downloaded twice."),
    (scene_next('S3 · E12', 'CODE SPLITTING', "don't ship what nobody uses", 'code', 'nobody'),
     "Next: code splitting, and why you shouldn't ship code nobody uses. Comment NOTES for the cheat sheet."),
]
