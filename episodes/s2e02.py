from engine.s2_extra import *

EP = dict(id='S2E02', tag='S2 · E02', short='CLIENT-SIDE RENDERING')

SRC = ['<!doctype html>', '<html>', '  <head><title>My App</title></head>', '  <body>', '    <div id="root"></div>',
       '    <script src="/assets/index-4f2a.js">', '    </script>', '  </body>', '</html>']

def hook(c):
    tv = c.T('View')
    htmlcard(c, 60, 330, 1020, SRC, tv, 'view-source:my-app.com', 30, circles=[(4, c.T('empty'), '<div id="root"></div>')])
    tc = c.T('content')
    if c.on(tc): stamp(c.cv, 540, 1150, 'NO CONTENT', 90, c.P(tc, 0.4), -5, RED)

def define(c):
    title(c, 'CLIENT-SIDE RENDERING', 340, c.T('client'), 84, hlcol=YEL)
    txt(c, 540, 420, 'CSR = the browser builds the page with JS', c.T('client') + 0.4, 'ints', 34, MUTE)
    s = node(c, 200, 700, 240, 200, 'server', c.T('server'), 'server')
    b = node(c, 880, 700, 240, 200, 'browser', c.T('browser'), 'laptop')
    t1 = c.T('empty')
    if c.on(t1):
        packet(c, s, b, t1, t1 + 1.0, WHITE, 'empty HTML', off=-50)
    t2 = c.T('bundle')
    if c.on(t2): packet(c, s, b, t2, t2 + 1.0, YEL, 'bundle.js', off=50)
    tb = c.T('builds')
    if c.on(tb):
        fill_page(c, (720, 870, 1040, 1250), 'full' if c.on(tb + 0.8) else 'skeleton')
        c.pen.rr(720, 870, 1040, 1250, 8, outline=INK, w=4)
        label(c, 880, 1300, 'JS builds the DOM', tb, YEL, INK, 28)

def analogy(c):
    tf = c.T('flat')
    if c.on(tf):
        card(c.pen, 120, 380, 960, 1060, 26, WHITE, 12, 5)
        c.pen.text(540, 450, 'THE FLAT-PACK, AGAIN', 'osw', 54, INK)
    rows = [('empty box', 'index.html', 'box'), ('instructions + parts', 'bundle.js', 'instructions'), ('the assembly', "user's phone CPU", 'assembly')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw); y = 590 + i * 150
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); p = c.P(at, 0.35)
        c.pen.text(180, y, a, 'intx', 40, mix(WHITE, INK, p), 'lm')
        arrow(c.pen, 590, y, 650, y, p, INK, 5, 16)
        pill(c.pen, 800, y, b, c.B(at, 0.35), YEL if i < 2 else RED, INK if i < 2 else WHITE, 30)

CODE = ["const root = document.getElementById('root');", "const res = await fetch('/api/products');", 'const items = await res.json();',
        'root.innerHTML = items', '  .map(p => `<li>${p.name}</li>`)', "  .join('');"]

def how(c):
    code(c, 40, 360, 1040, 360 + 72 + 6 * 54 + 40, CODE, c.T('Here'), 0.15, 30, 'main.js',
         marks=[(0, c.T('Find'), YEL), (1, c.T('fetch'), YEL), (3, c.T('build'), YEL)])
    tw = c.T('whole')
    if c.on(tw):
        for i, (s_, kw) in enumerate([('1 · find root', 'Find'), ('2 · fetch data', 'fetch'), ('3 · build HTML in the browser', 'build')]):
            txt(c, 100, 900 + i * 80, s_, c.T(kw), 'intx', 40, INK, 'lm', 'slide')

def tradeoffs(c):
    title(c, 'THE TRADE-OFF', 340, c.T('upside'), 96, hlcol=YEL)
    proscons(c, 100, 500, 980, [(True, 'hosting = just static files', c.T('static')), (True, 'instant after the first load', c.T('instant')),
                                 (False, 'slower first paint', c.T('slower')), (False, 'crawlers without JS see nothing', c.T('crawlers'))], 38, 110)
    tg = c.T('great')
    if c.on(tg): label(c, 540, 1050, 'great for: dashboards, admin panels, apps behind login', tg, INK, WHITE, 28)

def proof(c):
    tv, te = c.T('View'), c.T('Elements')
    if c.on(tv - 0.01):
        txt(c, 300, 360, 'View Source', tv, 'intx', 40, INK)
        txt(c, 300, 410, 'what the server sent', tv, 'ints', 28, MUTE)
        htmlcard(c, 50, 450, 530, ['<body>', '  <div id="root">', '  </div>', '</body>'], tv, 'source', 26)
        if c.on(c.T('empty')): label(c, 290, 820, 'EMPTY', c.T('empty'), RED, WHITE, 32)
    if c.on(te - 0.01):
        txt(c, 780, 360, 'Elements', te, 'intx', 40, INK)
        txt(c, 780, 410, 'the live DOM, after JS', te, 'ints', 28, MUTE)
        htmlcard(c, 550, 450, 1030, ['<div id="root">', '  <header>…</header>', '  <ul>', '    <li>Shoes</li>', '    <li>Watch</li>', '  </ul>', '</div>'], te, 'elements', 26)
        if c.on(c.T('full')): label(c, 790, 1010, 'FULL', c.T('full'), GRN, WHITE, 32)

def gotcha(c):
    trap(c)
    qtext(c, 'Does Google index client-rendered pages?', 450, c.T('Google'), 48)
    tc = c.T('can')
    if c.on(tc): label(c, 540, 600, 'Google: yes, usually — rendering can be deferred', tc, GRN, WHITE, 28)
    tw = c.T('WhatsApp')
    if c.on(tw):
        phonebox = phone(c, 540, 930, 420, 520)
        x0, y0, x1, y1 = phonebox
        c.pen.rect(x0, y0, x1, y1, fill=(230, 222, 210))
        c.pen.rr(x0 + 30, y0 + 40, x1 - 30, y0 + 300, 16, fill=(220, 248, 198), outline=INK, w=3)
        c.pen.rr(x0 + 50, y0 + 60, x1 - 50, y0 + 190, 10, fill=WHITE)
        c.pen.text((x0 + x1) / 2, y0 + 125, '(no title, no image)', 'intm', 24, MUTE)
        c.pen.text(x0 + 50, y0 + 240, 'my-app.com', 'int', 26, BLUE, 'lm')
    tb = c.T('blank')
    if c.on(tb): stamp(c.cv, 540, 1290, 'BLANK PREVIEW', 70, c.P(tb, 0.4), -4, RED)

SCENES = [
    (hook, "Open an app built with Vite or Create React App, and View Page Source. Look for the content you can see on screen. It isn't there. Just one empty div, and a script tag."),
    (define, "That's client side rendering. The server sends a nearly empty HTML file, plus a JavaScript bundle. The browser runs the bundle, and the JavaScript builds the page."),
    (analogy, "Remember the flat pack table? The HTML is the empty box. The bundle is the instructions and the parts. And the assembly happens on your user's phone."),
    (how, "Here's the whole idea in six lines. Find the root element, fetch the data, then build the HTML right there in the browser."),
    (tradeoffs, "The upside: hosting is just static files, and after the first load, navigation feels instant. The downside: a slower first paint, and crawlers that don't run JavaScript see nothing. It's great for dashboards and apps behind a login."),
    (proof, "Prove it in DevTools. View Source is what the server sent: empty. The Elements panel is the live DOM after JavaScript ran: full."),
    (gotcha, "Interview trap: does Google index client rendered pages? Google can run JavaScript, but it may render later. And link previews in WhatsApp or LinkedIn usually read raw HTML only. So your shared link shows up blank."),
    (scene_next('S2 · E03', 'CLIENT-SIDE ROUTING', 'new page, no page load', 'routing', 'page'),
     "Next: client side routing. How YouTube changes the page without loading a new one. Comment NOTES for the cheat sheet."),
]
