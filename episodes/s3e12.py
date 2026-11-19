from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E12', tag='S3 · E12', short='CODE SPLITTING', hook="don't ship code nobody uses")

def hook(c):
    browser(c, 110, 330, 970, 720, url='blog.example.com/post', dy=(1 - c.P(0, 0.45)) * 900)
    for k in range(4): c.pen.rr(160, 450 + k * 60, 920 - (k % 2) * 200, 480 + k * 60, 8, fill=LIGHT)
    items = [('admin-dashboard.js', 'admin'), ('rich-text-editor.js', 'editor'), ('charts.js', 'charts')]
    for k, (nm, kw) in enumerate(items):
        t = c.T(kw)
        if not c.on(t): continue
        y = 820 + k * 110; s = c.B(t, 0.35); c.sfx(t, 'pop')
        c.pen.rr(200, y - 40 * s, 880, y + 40 * s, 20, fill=(255, 225, 190), outline=INK, w=4)
        c.pen.text(240, y, nm, 'monob', 32 * s, INK, 'lm')
        if c.on(c.T('never')): cross(c.pen, 830, y, 0.9, RED, 8, c.P(c.T('never') + k * 0.1, 0.3))

def bundle(c):
    title(c, 'ONE BIG BUNDLE', 330, c.T('one'), 100)
    tb = c.T('bundlers')
    if c.on(tb):
        for k, (nm, col) in enumerate((('home', GRN), ('blog', BLUE), ('admin', RED), ('editor', ORANGE), ('charts', PURPLE), ('checkout', TEAL))):
            t = tb + k * 0.15
            if not c.on(t): continue
            q = c.P(t + 0.3, 0.5)
            x0 = 140 + (k % 3) * 280; y0 = 480 + (k // 3) * 140
            y = y0 + (925 + (k // 3) * 120 - y0) * q
            c.pen.rr(x0, y, x0 + 240, y + 100, 16, fill=col, outline=INK, w=4)
            c.pen.text(x0 + 120, y + 50, nm, 'intx', 32, WHITE)
        if c.on(tb + 1.3): c.pen.rr(110, 900, 970, 1180, 26, outline=INK, w=6); txt(c, 540, 1230, 'bundle.js · 2.1 MB', tb + 1.3, 'monob', 36, INK)
    tf = c.T('first')
    if c.on(tf): label(c, 540, 400 + 60, 'every user pays for every feature', tf, (255, 210, 210), INK, 32)

def suitcase(c):
    tw = c.T('wardrobe')
    if c.on(tw):
        card(c.pen, 120, 400, 520, 900, 24, (190, 140, 90), 10, 5)
        for k in range(9): c.pen.rect(150 + (k % 3) * 120, 430 + (k // 3) * 150, 250 + (k % 3) * 120, 560 + (k // 3) * 150, fill=[RED, BLUE, GRN, YEL, PURPLE, ORANGE, TEAL, PINK, GREY][k], outline=INK, w=3)
        txt(c, 320, 960, 'whole wardrobe', tw, 'intx', 36, RED)
        if c.on(c.T('weekend')): stamp(c.cv, 320, 650, 'TOO MUCH', 54, c.P(c.T('weekend'), 0.35), -10, RED)
    tp = c.T('wear')
    if c.on(tp):
        card(c.pen, 620, 560, 940, 900, 24, (190, 140, 90), 10, 5)
        for k in range(2): c.pen.rect(660 + k * 130, 600, 770 + k * 130, 860, fill=[BLUE, GRN][k], outline=INK, w=3)
        txt(c, 780, 960, 'just the weekend', tp, 'intx', 36, GRN)
    tr = c.T('rest')
    if c.on(tr): label(c, 540, 1120, 'fetch the rest only if you need it', tr, YEL, INK, 34)

def dynamic(c):
    title(c, 'DYNAMIC import()', 330, c.T('dynamic'), 96, hlcol=YEL)
    code(c, 40, 450, 1040, 820, ["button.addEventListener('click', async () => {", "  const { openEditor } = await import('./editor.js');", '  openEditor();', '});'],
         c.T('Instead') - 0.4, 0.15, 25, 'post.js', marks=[(1, c.T('needed'), YEL)])
    ts = c.T('separate')
    if c.on(ts):
        a = node(c, 290, 1020, 340, 130, 'main.js', ts, 'doc')
        b = node(c, 790, 1020, 340, 130, 'editor.[hash].js', ts + 0.3, 'doc', fill=(255, 238, 170), size=28)
        link(c, a, b, ts + 0.3, txt_='on click', dash=True)

def where(c):
    title(c, 'WHERE TO SPLIT', 330, c.T('Split'), 100)
    rows(c, 110, 500, [('route', 'by route', '/home · /product · /checkout', 'ok'), ('heavy', 'by heavy feature', 'editor · map · charts', 'ok'),
                       ('fold', 'below the fold', 'reviews · recommendations', 'ok')], 170, 860, 130, 40, 30)
    tv = c.T('vendor')
    if c.on(tv): label(c, 540, 1080, 'shared libs → vendor chunk (caches well)', tv, WHITE, INK, 32)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Coverage',), dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('reload')
    items = [('bundle.js', 0.38), ('vendor.js', 0.52), ('styles.css', 0.3), ('analytics.js', 0.7)]
    for k, (nm, used) in enumerate(items):
        t = tr + k * 0.25
        if not c.on(t): continue
        y = 500 + k * 110; p = c.P(t, 0.5); c.sfx(t, 'tick')
        c.pen.text(100, y, nm, 'mono', 28, WHITE, 'lm')
        x0, x1 = 400, 980
        c.pen.rect(x0, y - 22, x0 + (x1 - x0) * used * p, y + 22, fill=(70, 170, 220))
        c.pen.rect(x0 + (x1 - x0) * used * p, y - 22, x0 + (x1 - x0) * p, y + 22, fill=RED)
    tb = c.T('Red')
    if c.on(tb): txt(c, 540, 1000, 'red = downloaded, never ran', tb, 'intx', 38, RED)
    th = c.T('half')
    if c.on(th): bignum(c, 540, 1240, 'often > 50% unused', th, 70, INK)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    title(c, 'SPLIT EVERYTHING?', 480, c.T('everything'), 90)
    tw = c.T('waterfall')
    for k, nm in enumerate(('chunk A', 'chunk B', 'chunk C', 'chunk D')):
        t = tw + k * 0.5
        if not c.on(t): continue
        y = 630 + k * 110; xa = 140 + k * 190
        p = c.P(t, 0.45); c.sfx(t, 'pop')
        c.pen.rect(xa, y, xa + 190 * p, y + 70, fill=[BLUE, PURPLE, ORANGE, RED][k], outline=INK, w=3)
        c.pen.text(xa + 10, y + 35, nm, 'int', 26, WHITE, 'lm')
    ts = c.T('slower')
    if c.on(ts): stamp(c.cv, 540, 1140, 'SLOWER THAN 1 BUNDLE', 60, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')

SCENES = [
    (hook, "You open a blog post. Your browser downloads the code for the admin dashboard, the rich text editor, and a charts library. You'll never use any of it."),
    (bundle, "By default, bundlers put your whole app into one big JavaScript file. So every user pays for every feature, on their very first visit."),
    (suitcase, "It's like packing your whole wardrobe for a weekend trip. Pack what you'll wear, and fetch the rest only if you need it."),
    (dynamic, "Code splitting breaks the bundle into chunks, and the key is dynamic import. Instead of importing at the top of the file, you import when it's needed. The bundler then puts that code in a separate file."),
    (where, "Split where users make choices. By route. By heavy feature, like an editor or a map. And by things below the fold. Shared libraries go in a vendor chunk that caches well."),
    (proof, "Open the Coverage tab in DevTools and reload. Red shows bytes that downloaded but never ran. On many sites, it's often more than half the JavaScript."),
    (gotcha, "Interview trap: so split everything into tiny chunks? Now one click starts a waterfall. Chunk A loads, then discovers it needs B, which needs C. Too many tiny chunks can be slower than one medium bundle."),
    (scene_next('S3 · E13', 'LAZY ROUTES', 'load pages only when visited', 'lazy', 'visits'),
     "Next: lazy routes, loading pages only when someone visits them. Comment NOTES for the cheat sheet."),
]
