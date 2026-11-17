from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E09', tag='S3 · E09', short='CRITICAL RENDERING PATH')

def hook(c):
    ts = c.T('server')
    if c.on(ts):
        card(c.pen, 110, 360, 970, 520, 24, WHITE, 10, 5)
        c.pen.text(150, 440, 'server response', 'intx', 40, INK, 'lm'); c.pen.text(930, 440, '100 ms', 'intx', 48, GRN, 'rm')
    tw = c.T('white')
    if c.on(tw):
        browser(c, 110, 600, 970, 1120, url='app.example.com')
        counter(c, 540, 920, 0, 2.0, tw, tw + 1.6, '{:.1f}', 90, RED, ' s of white')
    tb = c.T('blocking')
    if c.on(tb): stamp(c.cv, 540, 1250, 'SOMETHING IS BLOCKING', 62, c.P(tb, 0.35), -3, RED); c.sfx(tb, 'thud')

def path(c):
    title(c, 'CRITICAL RENDERING PATH', 330, c.T('critical'), 76, hlcol=YEL)
    a = node(c, 270, 560, 300, 130, 'HTML → DOM', c.T('DOM'), fill=WHITE)
    b = node(c, 810, 560, 300, 130, 'CSS → CSSOM', c.T('CSSOM'), fill=WHITE)
    r = node(c, 540, 800, 340, 120, 'render tree', c.T('chain'), fill=(255, 246, 214))
    p = node(c, 540, 1040, 340, 120, 'first pixels', c.T('pixels'), fill=YEL)
    link(c, a, r, c.T('chain')); link(c, b, r, c.T('chain')); link(c, r, p, c.T('pixels'))
    txt(c, 540, 1180, 'callback: S1 · E08 + E09', c.T('pixels') + 0.4, 'ints', 28, MUTE)

def css(c):
    title(c, 'CSS IS RENDER-BLOCKING', 330, c.T('render'), 80, hlcol=(255, 180, 180))
    code(c, 70, 440, 1010, 700, ['<head>', '  <link rel="stylesheet" href="main.css">', '</head>'], c.T('stylesheet') - 0.4, 0.12, 30, 'index.html', lang='html',
         marks=[(1, c.T('stylesheet'), (120, 60, 60))])
    tw = c.T('downloaded')
    if c.on(tw): timerbar(c, 140, 820, 940, c.P(tw, 1.4, lambda x: x), tw, 'main.css', ORANGE, 50)
    tp = c.T('paint')
    if c.on(tp): txt(c, 540, 960, 'no paint until it is done', tp, 'intx', 40, RED)
    tu = c.T('unstyled')
    if c.on(tu): label(c, 540, 1100, 'why? so you never see unstyled content (FOUC)', tu, WHITE, INK, 30)

def js(c):
    title(c, 'JS IS PARSER-BLOCKING', 330, c.T('parser'), 84, hlcol=(255, 180, 180))
    steps = [('build DOM', 'building', GRN), ('STOP', 'stops', RED), ('download', 'downloads', ORANGE), ('run', 'runs', YEL), ('continue', 'continues', GRN)]
    for k, (nm, kw, col) in enumerate(steps):
        t = c.T(kw); y = 500 + k * 150
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        c.pen.rr(300, y - 50 * s, 780, y + 50 * s, 22, fill=col, outline=INK, w=4)
        c.pen.text(540, y, nm, 'intx', 40 * s, WHITE if col in (RED, GRN) else INK)
        if k: arrow(c.pen, 540, y - 100, 540, y - 56, 1, INK, 5, 16)

def play(c):
    card(c.pen, 110, 380, 970, 1060, 20, (90, 30, 40), 12, 5)
    tr = c.T('rise')
    lift = 0.7
    for k in range(5):
        x = 200 + k * 160
        if c.on(c.T('actor')):
            if k != 3: person(c.pen, x, 1000, 1.2, [BLUE, GRN, ORANGE, PURPLE, TEAL][k])
            else: c.pen.text(x, 900, '?', 'osw', 120, YEL)
    c.pen.rect(130, 400, 950, 400 + 620 * (1 - lift), fill=(190, 40, 55), outline=INK, w=4)
    for k in range(6): c.pen.line([(200 + k * 140, 410), (200 + k * 140, 400 + 610 * (1 - lift))], (150, 25, 40), 6)
    tl = c.T('late')
    if c.on(tl):
        person(c.pen, 1000 - 60 * c.P(tl, 1.0), 1240, 1.0, PURPLE); txt(c, 700, 1180, 'one late actor...', tl, 'intx', 36, INK)
    tw = c.T('audience')
    if c.on(tw):
        for k in range(7): c.pen.circ(170 + k * 120, 1310, 34, fill=INK)

def fix(c):
    title(c, 'SHRINK THE PATH', 330, c.T('shrink'), 100, hlcol=YEL)
    code(c, 40, 450, 1040, 820, ['<style>/* critical CSS for screen 1 */</style>', '<link rel="stylesheet" href="print.css" media="print">',
                                 '<script src="app.js" defer></script>'], c.T('Inline') - 0.4, 0.15, 24, 'index.html', lang='html',
         marks=[(0, c.T('Inline'), (60, 110, 70)), (1, c.T('media'), (60, 110, 70)), (2, c.T('Defer'), (60, 110, 70))])
    rows(c, 100, 930, [('Inline', 'inline the small critical CSS', None, 'ok'), ('rest', 'load the rest without blocking', None, 'ok'),
                       ('media', 'media="print" → not render-blocking', None, 'ok')], 115, 880, 92, 32)

def proof(c):
    panel(c, 60, 330, 1020, 1180, tabs=('Lighthouse', 'Performance'), dy=(1 - c.P(0, 0.45)) * 900)
    tl = c.T('Render')
    if c.on(tl):
        c.pen.text(110, 470, 'Render blocking requests', 'intx', 34, ORANGE, 'lm')
        netrows(c, 110, 560, 980, [(tl + 0.3, 'main.css', ['48 KB', '620 ms'], RED), (tl + 0.5, 'fonts.css', ['12 KB', '410 ms'], RED),
                                   (tl + 0.7, 'vendor.js', ['210 KB', '890 ms'], RED)], 28, 70, [700, 860])
    tp = c.T('tagged')
    if c.on(tp):
        card(c.pen, 200, 850, 900, 1080, 14, WHITE, 6, 3)
        c.pen.text(240, 900, 'main.css', 'monob', 30, INK, 'lm')
        c.pen.text(240, 960, 'Priority: Highest', 'mono', 26, INK, 'lm')
        c.pen.text(240, 1020, 'Render blocking: Blocking', 'monob', 26, RED, 'lm')

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"CSS never blocks parsing." Right?', c.T('parsing'), 'intx', 44, INK)
    code(c, 70, 560, 1010, 780, ['<link rel="stylesheet" href="slow.css">', "<script>getComputedStyle(el).color</script>"], c.T('script') - 0.3, 0.15, 26, 'index.html',
         lang='html', marks=[(1, c.T('wait'), (120, 60, 60))])
    tw = c.T('wait')
    if c.on(tw):
        node(c, 300, 920, 340, 110, 'slow.css', tw, fill=(255, 225, 190))
        node(c, 780, 920, 340, 110, 'script waits', tw + 0.2, fill=(255, 225, 225))
        arrow(c.pen, 475, 920, 605, 920, c.P(tw + 0.2, 0.3), INK, 6)
    tb = c.T('too')
    if c.on(tb): stamp(c.cv, 540, 1120, 'CSS BLOCKS PARSING TOO', 60, c.P(tb, 0.35), -3, RED); c.sfx(tb, 'thud')

SCENES = [
    (hook, "Your server responds in a hundred milliseconds. Yet the screen stays white for two whole seconds. The HTML arrived. So something is blocking the first paint."),
    (path, "To paint anything, the browser needs the DOM from your HTML, and the CSSOM from your stylesheets. That chain, from bytes to the first pixels, is the critical rendering path."),
    (css, "CSS is render blocking. The browser won't paint until every stylesheet in the head has downloaded and been parsed. That way, you never see unstyled content."),
    (js, "And a plain script tag is parser blocking. The browser is building the DOM, then stops, downloads the script, runs it, and only then continues."),
    (play, "It's like a play where the curtain won't rise until every actor is on stage. One late actor, and the whole audience waits."),
    (fix, "So shrink the path. Inline the small critical CSS for the first screen, and load the rest without blocking. Give stylesheets you don't need yet a media attribute. Defer your scripts."),
    (proof, "Lighthouse lists your Render blocking requests. And in the Performance panel, every request is tagged as render blocking, or not."),
    (gotcha, "Interview trap: CSS never blocks parsing, right? Not quite. A script after a stylesheet has to wait for that CSS, because the script might read styles. So slow CSS can block parsing too."),
    (scene_next('S3 · E10', 'ASYNC vs DEFER', 'two words that change load order', 'async', 'order'),
     "Next: async versus defer, two words that change your load order. Comment NOTES for the cheat sheet."),
]
