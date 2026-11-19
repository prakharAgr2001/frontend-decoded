from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E18', tag='S3 · E18', short='RESPONSIVE IMAGES', hook='stop sending posters to phones')

def hook(c):
    tp = c.T('photo'); tph = c.T('phone')
    q = c.P(tph, 0.6) if c.on(tph) else 0
    if q > 0: phone(c, 710, 800, 300, 560)
    if c.on(tp):
        s = c.P(tp, 0.5)
        x0 = 110 + 490 * q; y0 = 360 + 280 * q; x1 = 110 + 860 * s - 150 * q; y1 = 360 + 600 * s - 160 * q
        c.pen.rect(x0, y0, x1, y1, fill=(120, 170, 210), outline=INK, w=5)
        if q < 0.2: c.pen.text(540, 660, 'shoe.jpg · 4000 px · 3 MB', 'intx', 42 * s, WHITE)
    if q > 0.9: c.pen.text(710, 840, 'shown at 360 px', 'ints', 24, INK)
    tpo = c.T('poster')
    if c.on(tpo): stamp(c.cv, 330, 1050, 'A POSTER', 64, c.P(tpo, 0.35), -6, RED); c.sfx(tpo, 'thud')
    ts = c.T('stamp')
    if c.on(ts): stamp(c.cv, 760, 1180, 'FOR A STAMP', 56, c.P(ts, 0.35), 5, INK); c.sfx(ts, 'thud')

def srcset(c):
    title(c, 'srcset + sizes', 330, c.T('srcset'), 100, k='monob', hlcol=YEL)
    code(c, 30, 440, 1050, 800, ['<img src="shoe-800.jpg"', '  srcset="shoe-400.jpg 400w, shoe-800.jpg 800w,', '          shoe-1600.jpg 1600w"',
                                 '  sizes="(max-width: 600px) 100vw, 50vw"', '  width="800" height="800" alt="Running shoe">'],
         c.T('List') - 0.4, 0.12, 25, 'product.html', lang='html', marks=[(1, c.T('widths'), (60, 90, 140)), (3, c.T('sizes'), (60, 90, 140))])
    tp = c.T('picks')
    if c.on(tp): label(c, 540, 900, 'browser picks the smallest sharp file', tp, YEL, INK, 34)
    td = c.T('density')
    if c.on(td): txt(c, 540, 1000, 'and accounts for 2x / 3x screens', td, 'ints', 32, INK)

def math_(c):
    title(c, 'THE BROWSER DOES THE MATH', 330, 0.1, 76)
    rows_ = [('phone', '360 px × 2x screen', '= 720 px', 'shoe-800.jpg', 'eight'),
             ('laptop', '400 px × 1x screen', '= 400 px', 'shoe-400.jpg', 'four')]
    for k, (ic, a, b, f, kw) in enumerate(rows_):
        t = c.T(ic); y = 560 + k * 330
        if not c.on(t): continue
        s = c.B(t, 0.35); c.sfx(t, 'pop')
        card(c.pen, 90, y - 130 * s, 990, y + 130 * s, 24, WHITE, 10, 5)
        icon(c.pen, ic, 190, y, 1.2 * s)
        c.pen.text(300, y - 50, a, 'intx', 38 * s, INK, 'lm'); c.pen.text(300, y + 5, b, 'intx', 38 * s, BLUE, 'lm')
        tf = c.T(kw, 2 if kw == 'four' else 1)
        if c.on(tf): pill(c.pen, 600, y + 75, '→ ' + f, c.B(tf, 0.35), (200, 240, 200), INK, 30)

def formats(c):
    title(c, 'MODERN FORMATS', 330, c.T('format'), 100, hlcol=YEL)
    bars(c, 90, 460, [('JPEG', 240, GREY, c.T('WebP') - 0.3), ('WebP', 170, BLUE, c.T('WebP')), ('AVIF', 120, GRN, c.T('AVIF'))], 240, 560, 70, 110, '{} KB', 200, 32)
    code(c, 30, 820, 1050, 1150, ['<picture>', '  <source srcset="shoe.avif" type="image/avif">', '  <source srcset="shoe.webp" type="image/webp">',
                                  '  <img src="shoe.jpg" alt="Running shoe">', '</picture>'], c.T('picture') - 0.4, 0.12, 25, 'product.html', lang='html',
         marks=[(3, c.T('fallback'), (60, 110, 70))])
    ts = c.T('same')
    if c.on(ts): txt(c, 540, 790, 'same visual quality · typical sizes', ts, 'ints', 26, MUTE)

def art(c):
    title(c, 'ART DIRECTION', 330, c.T('art'), 100)
    tp = c.T('phones')
    if c.on(tp):
        phone(c, 300, 760, 300, 560)
        c.pen.rect(170, 560, 430, 900, fill=(120, 170, 210)); c.pen.circ(300, 700, 70, fill=ORANGE, outline=INK, w=4)
        txt(c, 300, 1080, 'tight crop', tp, 'intx', 34, INK)
    tw = c.T('wide')
    if c.on(tw):
        card(c.pen, 520, 600, 1000, 900, 18, WHITE, 8, 5)
        c.pen.rect(540, 620, 980, 880, fill=(120, 170, 210)); c.pen.circ(760, 760, 40, fill=ORANGE, outline=INK, w=3)
        c.pen.poly([(540, 880), (650, 780), (760, 880)], fill=GRN)
        txt(c, 760, 960, 'wide shot', tw, 'intx', 34, INK)
    tm = c.T('media')
    if c.on(tm): label(c, 540, 1180, '<source media="(min-width: 800px)" …>', tm, WHITE, INK, 28)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Elements',), dy=(1 - c.P(0, 0.45)) * 900)
    c.pen.text(100, 480, '<img src="shoe.jpg" class="thumb">', 'mono', 28, (200, 205, 215), 'lm')
    th = c.T('hover')
    if c.on(th):
        card(c.pen, 160, 560, 920, 800, 14, WHITE, 6, 3)
        c.pen.text(200, 620, 'img.thumb', 'monob', 30, PURPLE, 'lm')
        c.pen.text(200, 690, 'Rendered size:  360 × 360 px', 'mono', 28, INK, 'lm')
        c.pen.text(200, 750, 'Intrinsic size: 4000 × 4000 px', 'monob', 28, RED, 'lm')
    tw = c.T('wasting')
    if c.on(tw): txt(c, 540, 900, '~120x more pixels than shown', tw, 'intx', 38, RED)
    tl = c.T('Properly')
    if c.on(tl): label(c, 540, 1040, 'Lighthouse: "Properly size images"', tl, YEL, INK, 32)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 30, 450, 1050, 640, ['<img srcset="t-400.jpg 400w, t-1600.jpg 1600w">', '<!-- no sizes! -->'], c.T('forget') - 0.3, 0.2, 27, 'thumb.html', lang='html',
         marks=[(1, c.T('forget'), (120, 60, 60))])
    ta = c.T('assumes')
    if c.on(ta): title(c, 'sizes = 100vw', 750, ta, 90, RED, k='monob')
    tl = c.T('largest')
    if c.on(tl):
        card(c.pen, 120, 860, 960, 1160, 20, WHITE, 8, 5)
        c.pen.rect(160, 900, 340, 1020, fill=(120, 170, 210)); c.pen.text(250, 1060, 'tiny thumb', 'ints', 26, INK)
        c.pen.text(400, 960, 'downloads t-1600.jpg', 'monob', 30, RED, 'lm')

SCENES = [
    (hook, "A product photo, four thousand pixels wide, three megabytes. On a phone, it's shown just three hundred and sixty pixels wide. Your user downloaded a poster to look at a stamp."),
    (srcset, "The fix is srcset. List the same image in several widths, and use sizes to tell the browser how wide it will be shown. The browser picks the smallest file that still looks sharp, and accounts for high density screens."),
    (math_, "The browser does the math. A phone shows it three hundred and sixty pixels wide, on a two x screen: that's seven hundred and twenty real pixels, so it picks the eight hundred version. An older laptop, showing it at four hundred pixels, picks the four hundred."),
    (formats, "Then use a modern format. WebP, and especially AVIF, are often much smaller than JPEG at the same quality. The picture element offers them, with JPEG as the fallback."),
    (art, "Picture also handles art direction: a tight crop for phones, and a wide shot for desktops, chosen with media queries."),
    (proof, "Check your site. In the Elements panel, hover an image. DevTools shows the rendered size and the intrinsic size. If they're miles apart, you're wasting bytes. Lighthouse flags it as Properly size images."),
    (gotcha, "Interview trap: you add srcset, but forget sizes. The browser assumes the image fills the whole viewport, a hundred v w, and on a big screen it downloads the largest file, even for a tiny thumbnail."),
    (scene_next('S3 · E19', 'LCP IMAGE PRIORITY', 'make the hero image jump the queue', 'LCP', 'queue'),
     "Next: LCP image priority, and how to make your hero image jump the queue. Comment NOTES for the cheat sheet."),
]
