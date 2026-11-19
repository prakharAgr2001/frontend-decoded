from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E33', tag='S3 · E33', short='FINALE: MADE FAST', tail=3.0, hook='one product page, made fast')

BAD = {'LCP': ('4.1 s', RED), 'INP': ('410 ms', RED), 'CLS': ('0.31', RED)}
GOOD = {'LCP': ('1.9 s', GRN), 'INP': ('160 ms', GRN), 'CLS': ('0.02', GRN)}

def board(c, fixed=(), flip=None, y=430):
    """scoreboard of the three vitals; fixed = metrics already green; flip = (metric, time) turning green now"""
    for k, m in enumerate(('LCP', 'INP', 'CLS')):
        x = 220 + k * 320
        good = m in fixed or (flip and flip[0] == m and c.on(flip[1]))
        v, col = (GOOD if good else BAD)[m]
        s = c.B(flip[1], 0.4) if (flip and flip[0] == m and c.on(flip[1])) else 1
        card(c.pen, x - 140, y - 90, x + 140, y + 90, 20, WHITE, 8, 4)
        c.pen.text(x, y - 40, m, 'osw', 44, INK)
        c.pen.text(x, y + 35, v, 'intx', 46 * s, col)
        if flip and flip[0] == m and c.on(flip[1]): c.sfx(flip[1], 'ding')

def chaps(c, items, y0=650, gap=100):
    for i, (tag, name, kw) in enumerate(items):
        at = c.T(kw) if isinstance(kw, str) else kw
        chapter(c, 540, y0 + i * gap, tag, name, at)

def intro(c):
    stamp(c.cv, 540, 420, 'SEASON 3 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'ONE PRODUCT PAGE.', 640, c.T('slow'), 104)
    title(c, 'MADE FAST.', 800, c.T('fast'), 120, hlcol=YEL)
    tf = c.T('fast')
    if c.on(tf): icon(c.pen, 'bolt', 540, 1020, 1.6 * c.B(tf, 0.4))

def measure(c):
    board(c)
    chaps(c, [('E02', 'Core Web Vitals', 'PageSpeed'), ('E07', 'field data says: failing', 'failing'), ('E06', 'lab data to debug', 'debug')], 680, 120)

def loading(c):
    board(c)
    chaps(c, [('E06', 'TTFB: HTML from a CDN', 'CDN'), ('E09', 'inline critical CSS', 'critical'), ('E10', 'defer the scripts', 'defer'),
              ('E11', 'preconnect to image CDN', 'preconnect')], 640, 115)

def bundle(c):
    board(c)
    tb = c.T('drops')
    if c.on(tb): counter(c, 540, 640, 1.8, 0.4, tb, tb + 1.5, '{:.1f}', 80, GRN, ' MB of JS')
    chaps(c, [('E12', 'split by route', 'route'), ('E13', 'reviews lazy-loaded', 'reviews'), ('E15', 'moment swapped out', 'moment'),
              ('E16', 'Brotli on', 'Brotli')], 780, 110)

def hero(c):
    board(c, flip=('LCP', c.T('falls')))
    chaps(c, [('E18', 'AVIF + srcset', 'AVIF'), ('E19', 'in the HTML · fetchpriority high', 'fetchpriority'), ('E03', 'LCP under 2 s', 'falls')], 680, 120)

def shifts(c):
    board(c, fixed=('LCP',), flip=('CLS', c.T('drops')))
    chaps(c, [('E04', 'space reserved: images + ad slot', 'reserved'), ('E20', 'fonts: matched fallback', 'fallback')], 700, 130)

def third(c):
    board(c, fixed=('LCP', 'CLS'))
    chaps(c, [('E21', 'chat widget → facade', 'facade'), ('E21', 'tag manager waits for interaction', 'waits')], 700, 130)

def interact(c):
    board(c, fixed=('LCP', 'CLS'), flip=('INP', c.T('under')))
    chaps(c, [('E05', 'add to cart: feedback first', 'feedback'), ('E29', 'size picker: useTransition', 'transition'), ('E25', 'reviews virtualized', 'virtualized'),
              ('E26', 'price math in a worker', 'worker'), ('E30', 'long tasks chunked', 'chunked')], 620, 100)

def guard(c):
    board(c, fixed=('LCP', 'INP', 'CLS'))
    stamp(c.cv, 540, 640, 'ASSESSMENT: PASSED', 66, c.P(0.2, 0.4), -3, GRN); c.sfx(0.2, 'thud')
    chaps(c, [('E31', 'budget in CI keeps it fast', 'budget')], 820, 100)

SEASON = ['100 ms', 'CWV', 'LCP', 'CLS', 'INP', 'TTFB·TBT', 'LAB/FIELD', 'IQ', 'CRP', 'ASYNC', 'HINTS', 'SPLIT', 'LAZY', 'TREE', 'DIET', 'BROTLI', 'IQ',
          'IMAGES', 'PRIORITY', 'FONTS', '3RD PARTY', 'IQ', 'DEBOUNCE', 'THROTTLE', 'VIRTUAL', 'WORKERS', 'RE-RENDER', 'MEMO', 'TRANSITION', 'CHUNKS', 'BUDGETS', 'IQ', 'FINALE']

def wrap(c):
    tt = c.T('Thirty')
    yend = season_map(c, SEASON, tt, 6, 340, 'FINALE', 0.05)
    tn = c.T('Next')
    if c.on(tn):
        darkcard(c.pen, 90, 990, 990, 1230)
        c.pen.text(540, 1040, 'NEXT · SEASON 4', 'int', 32, YEL)
        c.pen.text(540, 1120, 'STATE MANAGEMENT', 'osw', 74 * c.B(tn, 0.4), WHITE)
        c.pen.text(540, 1190, 'useState → Redux → server state', 'int', 30, (180, 186, 196))
    tc = c.T('Comment')
    if c.on(tc): pill(c.pen, 540, 1320, 'Comment NOTES for the full season cheat sheet', c.B(tc, 0.35), YEL, INK, 30)

SCENES = [
    (intro, "Season three finale. One slow product page, and every fix from this season. Let's make it fast."),
    (measure, "First, measure. PageSpeed Insights shows real users failing all three vitals: LCP over four seconds, INP over four hundred milliseconds, and CLS at zero point three. Then lab runs help us debug."),
    (loading, "The HTML now comes from a CDN, so TTFB is low. We inline the critical CSS, defer every script, and preconnect to the image CDN."),
    (bundle, "The JavaScript drops from one point eight megabytes to four hundred kilobytes. Split by route. The reviews widget is lazy loaded. Moment is swapped out. And Brotli is on."),
    (hero, "The hero becomes an AVIF in a srcset, written right in the HTML, with fetchpriority high. LCP falls under two seconds."),
    (shifts, "Space is reserved for every image and the ad slot, and fonts get a matched fallback. CLS drops to zero point zero two."),
    (third, "The chat widget becomes a facade, and the tag manager waits for the first interaction."),
    (interact, "Add to cart paints feedback first. The size picker uses a transition. The reviews are virtualized. Price math runs in a worker, and the rest is chunked. INP falls under two hundred milliseconds."),
    (guard, "All three vitals pass. And a performance budget in CI keeps it that way."),
    (wrap, "Thirty three episodes. One page, every millisecond accounted for. Next season: state management, from use state to server state. Comment NOTES for the full season cheat sheet."),
]
