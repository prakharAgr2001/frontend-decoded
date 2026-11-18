from engine.s2_extra import *

EP = dict(id='S2E03', tag='S2 · E03', short='CLIENT-SIDE ROUTING', hook='new page, no page load')

def netrows(c, x0, y0, rows, at, step=0.35):
    for i, (name, typ, col) in enumerate(rows):
        t = at + i * step
        if not c.on(t): continue
        c.sfx(t, 'tick'); p = c.P(t, 0.25); y = y0 + i * 62
        c.pen.text(x0, y, name, 'mono', 28, mix(DARK, col, p), 'lm')
        c.pen.text(x0 + 700, y, typ, 'mono', 26, mix(DARK, (150, 156, 166), p), 'lm')

def hook(c):
    b = browser(c, 70, 300, 1010, 700, url='youtube.com/watch?v=…' if c.on(c.T('click')) else 'youtube.com')
    for i in range(3):
        x = 110 + i * 300
        c.pen.rr(x, 420, x + 260, 560, 12, fill=(60, 64, 72))
        c.pen.poly([(x + 112, 465), (x + 112, 515), (x + 152, 490)], fill=WHITE)
    tcl = c.T('click')
    if c.on(tcl): c.pen.circ(250, 500, 22, fill=YEL, outline=INK, w=3)
    p = panel(c, 70, 760, 1010, 1340, ('Network',), 0)
    tf = c.T('Doc')
    if c.on(tf):
        for i, (f, on) in enumerate([('All', 0), ('Fetch/XHR', 0), ('Doc', 1), ('JS', 0)]):
            x = 120 + i * 190
            c.pen.rr(x, 880, x + 170, 930, 25, fill=YEL if on else (50, 56, 66))
            c.pen.text(x + 85, 905, f, 'int', 26, INK if on else WHITE)
    netrows(c, 120, 990, [('youtube.com', 'document', WHITE)], tf + 0.2)
    tn = c.T('no')
    if c.on(tn):
        c.pen.text(540, 1110, 'no new document request', 'intx', 40, RED)
        stamp(c.cv, 540, 1230, 'NO PAGE LOAD', 70, c.P(tn, 0.4), -4, RED)

def define(c):
    title(c, 'CLIENT-SIDE ROUTING', 340, c.T('client'), 90, hlcol=YEL)
    steps = [('intercepts the click', 'intercepts', 'bolt'), ('fetches just the data', 'data', 'cloud'),
             ('swaps part of the page', 'swaps', 'doc'), ('History API updates the URL', 'history', 'clock')]
    for i, (s_, kw, ic) in enumerate(steps):
        at = c.T(kw); y = 520 + i * 160
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        card(c.pen, 110, y - 60, 970, y + 60, 20, WHITE if i < 3 else (255, 246, 214), 8, 4)
        icon(c.pen, ic, 190, y, 0.8 * c.B(at, 0.35))
        txt(c, 270, y, s_, at, 'intx', 40, INK, 'lm', 'slide')
    tb = c.T('back')
    if c.on(tb): label(c, 540, 1180, 'Back / Forward still work', tb, GRN, WHITE, 32)

def tv(pen, cx, cy, s, col):
    pen.rr(cx - 170 * s, cy - 110 * s, cx + 170 * s, cy + 110 * s, 18, fill=DARK, outline=INK, w=5)
    pen.rect(cx - 150 * s, cy - 92 * s, cx + 150 * s, cy + 92 * s, fill=col)
    pen.line([(cx - 60 * s, cy + 110 * s), (cx - 90 * s, cy + 160 * s)], INK, 6); pen.line([(cx + 60 * s, cy + 110 * s), (cx + 90 * s, cy + 160 * s)], INK, 6)

def analogy(c):
    tch = c.T('channel')
    cols = [(90, 140, 220), (230, 120, 90), (90, 190, 130)]
    k = int(max(0, c.t - tch) / 0.8) % 3 if c.on(tch) else 0
    tv(c.pen, 540, 560, 1.4, cols[k])
    c.pen.text(540, 560, f'CH {k + 1}', 'osw', 70, WHITE)
    if c.on(tch): label(c, 540, 880, 'client-side routing = change the channel', tch, YEL, INK, 32)
    tn = c.T('new')
    if c.on(tn):
        label(c, 540, 1000, 'full page load = buy a new TV', tn, RED, WHITE, 32)
        cross(c.pen, 540, 1130, 1.2, RED, 12, c.P(tn + 0.3, 0.4))

CODE = ["document.addEventListener('click', e => {", "  const a = e.target.closest('a');", '  if (!a || a.origin !== location.origin) return;',
        '  e.preventDefault();', "  history.pushState({}, '', a.href);", '  render(location.pathname);', '});',
        "onpopstate = () => render(location.pathname);"]

def how(c):
    code(c, 30, 340, 1050, 340 + 72 + 8 * 52 + 40, CODE, c.T('code'), 0.12, 27, 'router.js',
         marks=[(1, c.T('delegated'), YEL), (3, c.T('stop'), YEL), (4, c.T('push'), YEL), (5, c.T('render'), YEL), (7, c.T('back'), YEL)])
    td = c.T('delegated')
    if c.on(td): chapter(c, 540, 1000, 'S1 · E21', 'one delegated listener', td)
    tb = c.T('back')
    if c.on(tb): txt(c, 540, 1100, 'popstate = user pressed Back', tb, 'ints', 34, INK)

def proof(c):
    p = panel(c, 70, 330, 1010, 1000, ('Network',), 0, (1 - c.P(0, 0.45)) * 900)
    tf = c.T('Fetch')
    if c.on(tf):
        for i, (f, on) in enumerate([('All', 0), ('Fetch/XHR', 1), ('Doc', 0), ('JS', 0)]):
            x = 120 + i * 190
            c.pen.rr(x, 450, x + 170, 500, 25, fill=YEL if on else (50, 56, 66))
            c.pen.text(x + 85, 475, f, 'int', 26, INK if on else WHITE)
    netrows(c, 120, 570, [('next?prettyPrint=false', 'fetch · JSON', CYAN), ('player?prettyPrint=false', 'fetch · JSON', CYAN)], c.T('JSON'))
    ts = c.T('Small')
    if c.on(ts):
        chips(c, 140, 1120, [('JSON, not HTML', YEL), ('no full reload', CYAN)], ts, 0.35, 32)

def gotcha(c):
    trap(c)
    addressbar(c, 90, 450, 990, 'my-app.com/products/42', False, 38)
    tr = c.T('refreshes')
    if c.on(tr):
        label(c, 540, 640, 'user hits refresh', tr, INK, WHITE, 32)
        txt(c, 540, 760, '404 Not Found', c.T('404'), 'intx', 80, RED, anim='pop')
    tk = c.T('knows')
    if c.on(tk):
        s = node(c, 260, 1000, 260, 180, 'server', tk, 'server')
        icon(c.pen, 'doc', 690, 960, 1.0); c.pen.text(690, 1060, 'index.html only', 'monob', 26, INK)
    tf = c.T('fall')
    if c.on(tf):
        htmlcard(c, 90, 1120, 990, ['# every route → index.html', 'try_files $uri /index.html;'], tf, 'nginx.conf', 28, step=0.15)

SCENES = [
    (hook, "Open YouTube, open the Network panel, filter by Doc, and click a video. The URL changes. The whole page changes. But there's no new document request."),
    (define, "That's client side routing. JavaScript intercepts the click, fetches just the data it needs, and swaps part of the page. The history API updates the URL, so back and forward still work."),
    (analogy, "It's like changing the channel on a TV. A traditional page load is buying a new TV every time you want a new channel."),
    (how, "Here's a tiny router. In code: one delegated listener catches link clicks. It stops the browser's default navigation, pushes the new URL, and renders the matching view. And popstate handles the back button."),
    (proof, "Back in DevTools, switch the filter to Fetch. There it is. JSON requests with the video's data. Small, fast, and no full reload."),
    (gotcha, "Interview trap: you deploy, a user refreshes on slash products slash forty two, and gets a 404. Why? The server only knows index dot html. Every route has to fall back to index dot html on the server."),
    (scene_next('S2 · E04', 'SERVER-SIDE RENDERING', 'what Amazon sends first', 'server', 'Amazon'),
     "Next: server side rendering. What Amazon sends before any JavaScript runs. Comment NOTES for the cheat sheet."),
]
