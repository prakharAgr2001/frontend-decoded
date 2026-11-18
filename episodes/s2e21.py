from engine.s2_extra import *

EP = dict(id='S2E21', tag='S2 · E21', short='FINALE: THREE SITES', tail=3.0, hook='Amazon vs Gmail vs a blog')

def chaps(c, items, y0=820, gap=95):
    for i, (tag, name, kw) in enumerate(items):
        at = c.T(kw) if isinstance(kw, str) else kw
        chapter(c, 540, y0 + i * gap, tag, name, at)

def intro(c):
    stamp(c.cv, 540, 400, 'SEASON 2 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'THREE SITES.', 620, c.T('Three'), 120)
    title(c, 'THREE STRATEGIES.', 770, c.T('ways'), 110, hlcol=YEL)
    for k, (nm, ic) in enumerate([('a blog', 'book'), ('Amazon', 'globe'), ('Gmail', 'doc')]):
        at = c.T('ways') + 0.4 + k * 0.2
        if c.on(at): node(c, 220 + k * 320, 1020, 260, 180, nm, at, ic, size=32)

def blog(c):
    t0 = c.T('blog')
    if c.on(t0):
        fill_page(c, phone(c, 540, 560, 300, 460), 'full')
    chaps(c, [('E05', 'built once · SSG', 'built'), ('E06', 'edited → ISR', 'edited'), ('E16', 'one island: comments', 'islands')], 900, 110)

def amazon(c):
    tv = c.T('View')
    if c.on(tv):
        htmlcard(c, 90, 330, 990, ['<span id="productTitle">Headphones…</span>', '<span class="a-price-whole">2,499</span>'], tv, 'view-source:amazon.in', 26)
    chaps(c, [('E04', 'server-side rendering', 'server'), ('E01', 'fast first paint on slow 4G', 'fast'), ('E08', 'then JS makes it interactive', 'interactive'),
              ('E10', 'the uncanny valley', 'valley')], 720, 110)

def gmail(c):
    tl = c.T('loading')
    b = browser(c, 90, 330, 990, 700, url='mail.google.com/mail/u/0/#inbox' if not c.on(c.T('URL')) else 'mail.google.com/mail/u/0/#inbox/FMfcg…')
    if c.on(tl) and not c.on(c.T('after')):
        timerbar(c, 240, 520, 840, c.P(tl, 2.5, lambda x: x), tl, None, RED, 30)
    elif c.on(c.T('after')):
        for k in range(4): c.pen.rr(130, 430 + k * 60, 950, 475 + k * 60, 8, fill=LIGHT)
    chaps(c, [('E02', 'client-side rendering', 'client'), ('E03', 'client-side routing', 'routing'), ('E01', 'slow to start · instant after', 'instant')], 830, 110)

def why(c):
    title(c, 'WHY SO DIFFERENT?', 330, c.T('Why'), 90, hlcol=YEL)
    cols = [('SEO?', 330), ('same for all?', 560), ('changes', 820)]
    for nm, x in cols: txt(c, x, 450, nm, c.T('questions'), 'int', 30, MUTE)
    rows = [('blog', ['yes', 'yes', 'rarely'], 'blog'), ('Amazon', ['yes', 'mostly', 'prices: often'], 'Amazon'), ('Gmail', ['no', 'no — per user', 'every second'], 'Gmail')]
    for i, (nm, vals, kw) in enumerate(rows):
        at = c.T(kw); y = 560 + i * 150
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop')
        card(c.pen, 70, y - 55, 1010, y + 55, 16, WHITE, 6, 4)
        c.pen.text(100, y, nm, 'intx', 36, INK, 'lm')
        for (cn, x), v in zip(cols, vals): c.pen.text(x, y, v, 'ints', 28, INK)
    tr = c.T('open')
    if c.on(tr): label(c, 540, 1060, 'the answers pick the strategy', tr, YEL, INK, 32)

def modern(c):
    title(c, 'THE MODERN MIX', 330, c.T('modern'), 100, hlcol=YEL)
    chaps(c, [('E13', 'streaming SSR', 'streaming'), ('E14', 'server components', 'components'), ('E15', 'server actions', 'actions'),
              ('E18', 'edge rendering', 'edge'), ('E17', 'resumability', 'resumability')], 470, 105)
    tt = c.T('trade')
    if c.on(tt): label(c, 540, 1060, 'less work on the phone · same interactivity', tt, INK, WHITE, 30)

SEASON = ['WHITE SCREEN', 'CSR', 'ROUTING', 'SSR', 'SSG', 'ISR', 'IQ', 'HYDRATION', 'MISMATCH', 'UNCANNY', 'SELECTIVE', 'IQ', 'STREAMING',
          'RSC', 'ACTIONS', 'ISLANDS', 'RESUMABLE', 'EDGE', 'CASE STUDY', 'IQ', 'FINALE']

def wrap(c):
    tt = c.T('Twenty')
    for i, nm in enumerate(SEASON):
        x = 130 + (i % 5) * 205; y = 360 + (i // 5) * 120
        at = tt + i * 0.06
        if not c.on(at): continue
        c.sfx(at, 'tick'); s = c.B(at, 0.3)
        c.pen.rr(x - 92 * s, y - 46 * s, x + 92 * s, y + 46 * s, 12, fill=YEL if nm == 'FINALE' else WHITE, outline=INK, w=3)
        c.pen.text(x, y - 14 * s, f'E{i + 1:02d}', 'int', 20 * s, MUTE)
        c.pen.text(x, y + 14 * s, nm, 'int', 22 * s, INK)
    tn = c.T('Next')
    if c.on(tn):
        darkcard(c.pen, 90, 1000, 990, 1240)
        c.pen.text(540, 1050, 'NEXT · SEASON 3', 'int', 32, YEL)
        c.pen.text(540, 1130, 'WEB PERFORMANCE', 'osw', 80 * c.B(tn, 0.4), WHITE)
        c.pen.text(540, 1200, 'Core Web Vitals → LCP · CLS · INP → bundle diet', 'int', 30, (180, 186, 196))
    tc = c.T('Comment')
    if c.on(tc): pill(c.pen, 540, 1330, 'Comment NOTES for the full season cheat sheet', c.B(tc, 0.35), YEL, INK, 30)

SCENES = [
    (intro, "Season two finale. Three sites you use every day, and three completely different ways to render a page."),
    (blog, "Start with a blog. The posts are built once, at build time, and served from a CDN edge near you. Nothing is cooked per request. When a post is edited, incremental regeneration refreshes just that page. And with islands, the only JavaScript might be the comment box."),
    (amazon, "Now Amazon. View Source shows the products already in the HTML. That's server side rendering, so you see the page fast, even on slow 4G. Then JavaScript has to make it interactive. Until it does, you're in the uncanny valley."),
    (gmail, "Then Gmail. First a loading screen, while a big JavaScript app downloads. That's client side rendering. But after that, opening an email changes the URL without a new document. Client side routing. Slow to start, instant after."),
    (why, "Why so different? Ask the three questions. The blog needs SEO, and rarely changes. Amazon needs SEO, and fresh prices. Gmail is behind a login, different for every user, and you keep it open all day."),
    (modern, "And the modern toolbox mixes them all. Streaming, server components, server actions, edge rendering, and even resumability. Every one is the same trade: less work on the user's phone, without losing interactivity."),
    (wrap, "Twenty one episodes. One question: who builds the HTML, and when? Next season: web performance. Core Web Vitals, and how to make every millisecond count. Comment NOTES for the full season cheat sheet."),
]
