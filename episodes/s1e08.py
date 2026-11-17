from engine.lib import *

EP = dict(id='S1E08', tag='S1 · E08', short='DOM & CSSOM')

RAW = ['<!doctype html>', '<html>', '<head>', '  <link rel="stylesheet"', '        href="app.css">', '</head>', '<body>',
       '  <h1>Hello</h1>', '  <p>Welcome back', '  <img src="me.png">', '</body>', '</html>']

def hook(c):
    darkcard(c.pen, 90, 300, 990, 1080)
    c.pen.text(130, 345, 'response body  ·  text/html', 'intm', 26, (140, 146, 156), 'lm')
    for i, ln in enumerate(RAW):
        at = 0.2 + i * 0.12
        if c.on(at): c.pen.text(130, 410 + i * 54, ln, 'mono', 32, (230, 230, 230), 'lm')
    tj = c.T('characters')
    if c.on(tj): stamp(c.cv, 760, 1140, 'JUST TEXT', 64, c.P(tj, 0.35), -4, RED)
    tq = c.T('click')
    if c.on(tq):
        c.sfx(tq, 'thud'); s = c.B(tq, 0.4)
        c.pen.circ(250, 1170, 70 * s, fill=YEL, outline=INK, w=5); c.pen.text(250, 1170, '?', 'osw', 100 * s, INK)

DOM = [('html', 'html', 540, 430, None, 'tree'), ('head', 'head', 300, 590, 'html', 'tree'), ('body', 'body', 780, 590, 'html', 'tree'),
       ('link', 'link', 300, 750, 'head', 'Every'), ('h1', 'h1', 600, 750, 'body', 'Every'), ('p', 'p', 780, 750, 'body', 'Every'),
       ('img', 'img', 950, 750, 'body', 'Every')]

def dom(c):
    title(c, 'DOM', 300, c.T('DOM'), 110, hlcol=YEL)
    nodes = [(k, l, x, y, p, (c.T(kw) + i * 0.12) if kw else None) for i, (k, l, x, y, p, kw) in enumerate(DOM)]
    tree(c, nodes, 0)
    txt(c, 540, 900, 'Document Object Model: every tag → a node', c.T('Document'), 'int', 36, INK)
    tj = c.T('JavaScript')
    if c.on(tj):
        code(c, 140, 990, 940, 1200, ["document.querySelector('h1')", "  .textContent = 'Hi Prakhar';"], tj, 0.2, 30, 'app.js', dy=0)

def cssom(c):
    darkcard(c.pen, 90, 300, 520, 640)
    for i, ln in enumerate(['body { font: 16px Inter }', 'h1 { color: crimson }', 'p { margin: 8px }', 'img { width: 100% }']):
        c.pen.text(120, 360 + i * 60, ln, 'mono', 25, (230, 230, 230) if c.on(0.2 + i * 0.1) else DARK, 'lm')
    arrow(c.pen, 540, 470, 610, 470, c.P(c.T('parses'), 0.3), INK, 6, 20)
    nodes = [('b', 'body · 16px Inter', 800, 380, None, c.T('tree')), ('h', 'h1 · crimson + 16px Inter', 760, 540, 'b', c.T('tree') + 0.15),
             ('p', 'p · 8px + 16px Inter', 760, 680, 'b', c.T('tree') + 0.3)]
    tree(c, nodes, 0, size=24)
    title(c, 'CSSOM', 830, c.T('CSSOM'), 110, hlcol=YEL)
    txt(c, 540, 960, 'knows the final style of every element', c.T('final'), 'int', 36, INK)
    txt(c, 540, 1030, '(styles cascade + inherit down the tree)', c.T('final') + 0.5, 'intm', 30, MUTE)

def recipe(c):
    node(c, 280, 560, 380, 280, 'DOM', c.T('ingredients'), 'doc', sub='the ingredients')
    node(c, 800, 560, 380, 280, 'CSSOM', c.T('look'), 'eye', sub='how each should look')
    tb = c.T('both')
    if c.on(tb):
        arrow(c.pen, 300, 720, 500, 900, c.P(tb, 0.35), INK, 6, 22); arrow(c.pen, 780, 720, 580, 900, c.P(tb, 0.35), INK, 6, 22)
        node(c, 540, 1020, 420, 200, 'the plated dish', tb + 0.3, 'chef', fill=(255, 246, 214))

def blocking(c):
    title(c, 'WHO BLOCKS WHAT', 320, 0.1, 96)
    tc = c.T('blocks')
    c.pen.text(110, 470, 'HTML parsing', 'int', 32, INK, 'lm')
    c.pen.rect(110, 500, 110 + 860 * c.P(0.2, 2.5, lambda x: x), 550, fill=BLUE, outline=INK, w=3)
    if c.on(tc):
        c.pen.text(110, 630, 'app.css download', 'int', 32, INK, 'lm')
        c.pen.rect(110, 660, 110 + 480 * c.P(tc, 0.8), 710, fill=(150, 120, 230), outline=INK, w=3)
        c.pen.rr(110, 740, 590, 800, 12, fill=(255, 220, 220), outline=RED, w=3)
        c.pen.text(350, 770, 'nothing painted yet', 'int', 28, RED)
        c.pen.rect(600, 740, 600 + 370 * c.P(tc + 0.9, 0.5), 800, fill=GRN, outline=INK, w=3)
        if c.on(tc + 1.0): c.pen.text(785, 770, 'first paint', 'int', 28, WHITE)
    tf = c.T('flash')
    if c.on(tf): txt(c, 540, 860, 'otherwise: a flash of unstyled content', tf, 'int', 32, MUTE)
    ts = c.T('script')
    if c.on(ts):
        c.pen.text(110, 960, '<script src="app.js">', 'monob', 32, INK, 'lm')
        c.pen.rect(110, 990, 450, 1040, fill=BLUE, outline=INK, w=3)
        c.pen.rect(450, 990, 450 + 220 * c.P(ts + 0.3, 0.6), 1040, fill=YEL, outline=INK, w=3)
        if c.on(ts + 0.3): c.pen.text(560, 1015, 'parser paused', 'int', 24, INK)
        c.pen.rect(670, 990, 670 + 300 * c.P(ts + 1.0, 0.6), 1040, fill=BLUE, outline=INK, w=3)
    tm = c.T('might')
    if c.on(tm): txt(c, 540, 1130, 'the script might change the DOM', tm, 'intx', 38, INK)

def proof(c):
    tv = c.T('View')
    card(c.pen, 70, 330, 510, 1000, 24, WHITE, 10, 5)
    c.pen.text(290, 380, 'View Source', 'intx', 36, INK)
    for i, ln in enumerate(['<body>', '  <div id="root">', '  </div>', '  <script', '   src="app.js">', '</body>']):
        if c.on(tv + i * 0.1): c.pen.text(100, 460 + i * 56, ln, 'mono', 27, INK, 'lm')
    te = c.T('Elements')
    if c.on(te):
        darkcard(c.pen, 570, 330, 1010, 1000)
        c.pen.text(790, 380, 'Elements (live DOM)', 'int', 30, WHITE)
        rows = ['<body>', ' <div id="root">', '  <header>…</header>', '  <nav>…</nav>', '  <main>', '   <article>×24', '  </main>', ' </div>', '</body>']
        for i, ln in enumerate(rows):
            if c.on(te + i * 0.12): c.pen.text(600, 460 + i * 56, ln, 'mono', 26, CYAN if '<' in ln else WHITE, 'lm')
    tc = c.T('Compare')
    if c.on(tc): label(c, 540, 1110, 'source = what arrived · Elements = what is live', tc, YEL, INK, 28)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Is the DOM the same as your HTML?', c.T('same'), 'intx', 46, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 580, 'NO', 80, c.P(tn, 0.35), 4, BLUE)
    tf = c.T('fixes')
    if c.on(tf):
        code(c, 80, 680, 520, 900, ['<p>Hi', '<p>Bye'], tf, 0.15, 30, 'you wrote', dy=0, lang='html')
        arrow(c.pen, 530, 790, 580, 790, c.P(tf + 0.4, 0.3), INK, 6, 18)
        code(c, 590, 680, 1010, 900, ['<p>Hi</p>', '<p>Bye</p>'], tf + 0.5, 0.15, 30, 'DOM', dy=0, lang='html')
    ta = c.T('adds')
    if c.on(ta):
        darkcard(c.pen, 80, 960, 1010, 1060)
        c.pen.text(120, 1010, "el.append(newNode)  →  DOM ≠ HTML", 'monob', 34 * c.B(ta, 0.4), CYAN, 'lm')
    tl = c.T('live')
    if c.on(tl): label(c, 540, 1160, 'HTML = starting point · DOM = live state', tl, YEL, INK, 30)

SCENES = [
    (hook, "The server sends your browser a long string of text. Just characters. So how does that become a page you can click?"),
    (dom, "First, the browser parses the HTML into a tree. That tree is the DOM, the Document Object Model. Every tag becomes a node, and JavaScript can read it and change it."),
    (cssom, "CSS gets the same treatment. The browser parses every stylesheet into a second tree, the CSSOM, which knows the final style of every element."),
    (recipe, "Think of a recipe. The DOM is the list of ingredients. The CSSOM says how each one should look. You need both before you can plate the dish."),
    (blocking, "That's why CSS blocks rendering. The browser won't paint until the CSSOM is ready, or you'd see a flash of unstyled content. And a regular script tag pauses parsing, because the script might change the DOM."),
    (proof, "See the difference yourself. View Source shows the raw text the server sent. The Elements panel shows the live DOM, after JavaScript changed it. Compare them on any modern site."),
    (gotcha, "Interview trap: is the DOM the same as your HTML? No. The browser fixes broken markup, and JavaScript adds and removes nodes. The HTML is the starting point. The DOM is what's live right now."),
    (scene_next('S1 · E09', 'LAYOUT · PAINT', 'how the trees become pixels', 'layout', 'pixels'),
     "Next: layout, paint and composite, how those trees become pixels. Comment NOTES for the cheat sheet."),
]
