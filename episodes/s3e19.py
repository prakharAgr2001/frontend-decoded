from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E19', tag='S3 · E19', short='LCP IMAGE PRIORITY')

def hook(c):
    rows(c, 110, 420, [('ready', 'on the server', None, 'ok'), ('small', 'small', None, 'ok'), ('compressed', 'compressed', None, 'ok')], 120, 860, 96, 38)
    tl = c.T('last')
    if c.on(tl):
        x = 110
        for k, (nm, w, col) in enumerate((('HTML', 140, GRN), ('CSS', 150, PURPLE), ('JS', 220, YEL), ('icons', 120, GREY), ('hero', 200, RED))):
            t = tl + k * 0.15
            if c.on(t): c.pen.rect(x, 860, x + w * c.P(t, 0.3), 940, fill=col, outline=INK, w=3); c.pen.text(x + w / 2, 900, nm, 'int', 26, INK if col != RED else WHITE)
            x += w + 8
    ti = c.T('important')
    if c.on(ti): stamp(c.cv, 540, 1120, 'NOT IMPORTANT?!', 70, c.P(ti, 0.35), -3, RED); c.sfx(ti, 'thud')

def prio(c):
    title(c, 'EVERY REQUEST HAS A PRIORITY', 330, c.T('priority'), 70)
    for k, (nm, p, kw, col) in enumerate((('CSS in <head>', 'Highest', 'Scripts', RED), ('scripts in <head>', 'High', 'Scripts', ORANGE),
                                           ('images', 'Low', 'Images', GREY))):
        t = c.T(kw) + k * 0.2; y = 520 + k * 140
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        card(c.pen, 110, y - 55 * s, 970, y + 55 * s, 18, WHITE, 8, 4)
        c.pen.text(150, y, nm, 'intx', 36 * s, INK, 'lm'); pill(c.pen, 840, y, p, s, col, WHITE if col != GREY else INK, 30, outline=None)
    tb = c.T('boosted')
    if c.on(tb):
        axis(c, 140, 940, 1010, tb, [(0.1, 'request: Low', tb, GREY), (0.75, 'layout → High', c.T('late'), RED)])
        txt(c, 540, 1140, 'the boost comes late', c.T('late'), 'intx', 40, RED)

def fp(c):
    title(c, 'fetchpriority="high"', 330, c.T('fetchpriority'), 76, k='monob', hlcol=YEL)
    code(c, 30, 450, 1050, 640, ['<img src="hero.avif" fetchpriority="high"', '     width="1200" height="600" alt="Sale">'], c.T('Add') - 0.3, 0.15, 27, 'index.html', lang='html',
         circles=[(0, c.T('equals'), 'fetchpriority="high"')])
    tr = c.T('right')
    if c.on(tr): timerbar(c, 140, 760, 940, c.P(tr, 0.8), tr, 'hero.avif', GRN, 50, 'High · from the start')
    tg = c.T('Flights')
    if c.on(tg):
        card(c.pen, 140, 900, 940, 1150, 24, WHITE, 10, 5)
        c.pen.text(540, 960, 'Chrome team test · Google Flights', 'ints', 30, MUTE)
        c.pen.text(540, 1060, 'LCP 2.6 s  →  1.9 s', 'intx', 64 * c.B(c.T('two'), 0.4), GRN)

def boarding(c):
    title(c, 'PRIORITY BOARDING', 330, c.T('boarding'), 100, hlcol=YEL)
    c.pen.rr(110, 700, 970, 820, 60, fill=(220, 225, 235), outline=INK, w=5)
    for k in range(7):
        x = 220 + k * 105
        person(c.pen, x, 980, 0.8, BLUE)
    tf = c.T('first')
    if c.on(tf):
        q = c.P(tf, 0.8)
        person(c.pen, 220 + 600 * q, 880 - 120 * q, 1.0, YEL)
        pill(c.pen, 220 + 600 * q, 640, 'hero image', 1, YEL, INK, 28)
    ts = c.T('settled')
    if c.on(ts): txt(c, 540, 1110, 'same plane · first in, first settled', ts, 'intx', 38, INK)

def discover(c):
    title(c, 'IT MUST BE FINDABLE', 330, c.T('see'), 90)
    ts = c.T('scanner')
    if c.on(ts):
        node(c, 540, 500, 520, 120, 'preload scanner', ts, sub='skims raw HTML for files to fetch early', fill=(255, 246, 214))
    for k, (nm, kw) in enumerate((('CSS background-image', 'background'), ('injected by JavaScript', 'JavaScript'))):
        t = c.T(kw)
        if c.on(t): pill(c.pen, 540, 650 + k * 80, nm + ' → invisible', c.B(t, 0.35), (255, 210, 210), INK, 32)
    code(c, 30, 860, 1050, 1080, ['<link rel="preload" as="image" href="hero.avif"', '      fetchpriority="high">'], c.T('preload', 2) - 0.3, 0.15, 27, 'index.html', lang='html')
    ti = c.T('img')
    if c.on(ti): label(c, 540, 1160, 'best: a plain <img> in the HTML', ti, (200, 240, 200), INK, 32)

def dont(c):
    title(c, 'AND NEVER…', 330, c.T('never'), 100, RED)
    rows(c, 90, 520, [('lazy', 'loading="lazy" on the hero', None, 'no'), ('client', 'wait for client-side JS to render it', None, 'no'),
                      ('Server', 'server-render the hero', None, 'ok')], 170, 900, 130, 40)

def proof(c):
    panel(c, 50, 330, 1030, 1180, tabs=('Network', 'Performance'), dy=(1 - c.P(0, 0.45)) * 900)
    tp = c.T('Priority')
    if c.on(tp):
        c.pen.text(100, 470, 'Name', 'int', 26, (150, 156, 166), 'lm'); c.pen.text(760, 470, 'Priority', 'int', 26, YEL, 'lm')
        c.pen.text(100, 550, 'hero.avif', 'mono', 30, WHITE, 'lm')
        th = c.T('High')
        lab = 'Low → High' if c.on(th) else 'Low'
        c.pen.text(760, 550, lab, 'monob', 30, RED if c.on(th) else (180, 180, 190), 'lm')
    ti = c.T('insight')
    if c.on(ti):
        c.pen.text(100, 700, 'LCP request discovery', 'intx', 34, WHITE, 'lm')
        kv(c, 120, 780, 1000, [(ti + 0.2, '✓', 'request is discoverable in HTML', GRN), (ti + 0.4, '✓', 'lazy load not applied', GRN),
                               (ti + 0.6, '✗', 'fetchpriority=high should be applied', RED)], 30, 70)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    title(c, 'ALL IMAGES HIGH?', 480, c.T('every'), 96)
    te = c.T('everything')
    if c.on(te):
        for k in range(8):
            pill(c.pen, 200 + (k % 4) * 225, 640 + (k // 4) * 90, 'high', c.B(te + k * 0.05, 0.3), (255, 210, 210), INK, 30)
        stamp(c.cv, 540, 880, 'NOTHING IS', 70, c.P(c.T('nothing'), 0.35), -3, RED); c.sfx(c.T('nothing'), 'thud')
    to = c.T('one')
    if c.on(to): label(c, 540, 1060, 'use it on the 1–2 images that matter', to, (200, 240, 200), INK, 32)

SCENES = [
    (hook, "Your hero image is ready on the server. It's small. It's compressed. And it still shows up last, because the browser didn't think it was important."),
    (prio, "Browsers give every request a priority. Scripts and CSS in the head are high. Images start low, and are boosted only after layout shows they're on screen. That boost comes late."),
    (fp, "So tell the browser. Add fetchpriority equals high to your hero image, and it downloads at high priority right from the start. In a Chrome team test on Google Flights, this one attribute took LCP from two point six seconds to one point nine."),
    (boarding, "It's priority boarding. Everyone flies on the same plane, but whoever boards first gets settled first."),
    (discover, "But priority only helps if the browser can see the image. The preload scanner skims the raw HTML for files to fetch early. A CSS background, or an image injected by JavaScript, is invisible to it. So add a preload link, or better, put a plain img tag in the HTML."),
    (dont, "And never put loading lazy on the hero, and don't wait for client side JavaScript to render it. Server render the hero."),
    (proof, "In the Network panel, show the Priority column, and watch your hero go from Low to High. The Performance panel's LCP insight even checks whether fetchpriority high is applied."),
    (gotcha, "Interview trap: mark every image as high priority. If everything is high priority, nothing is. Use it on the one or two images that really matter."),
    (scene_next('S3 · E20', 'WEB FONTS', 'invisible text and font flashes', 'fonts', 'flashes'),
     "Next: web fonts, invisible text, and font flashes. Comment NOTES for the cheat sheet."),
]
