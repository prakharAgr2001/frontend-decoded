from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E20', tag='S3 · E20', short='WEB FONTS', hook='invisible text + font flashes')

def page(c, y0, mode, at, label_=None):
    """mini page; mode: 'blank', 'fallback', 'web'"""
    card(c.pen, 140, y0, 940, y0 + 360, 20, WHITE, 8, 5)
    c.pen.rect(180, y0 + 40, 900, y0 + 150, fill=(120, 170, 210))
    if mode == 'blank':
        for k in range(3): c.pen.rect(180, y0 + 190 + k * 50, 860 - k * 120, y0 + 220 + k * 50, outline=(230, 230, 230), w=2)
    else:
        f = 'osw' if mode == 'web' else 'intm'
        c.pen.text(180, y0 + 205, 'Monsoon Sale is live', f, 52 if mode == 'web' else 46, INK, 'lm')
        c.pen.text(180, y0 + 280, 'Up to 50% off on shoes', f, 36 if mode == 'web' else 32, MUTE, 'lm')
    if label_: pill(c.pen, 840, y0 - 10, label_, c.B(at, 0.35), YEL, INK, 26)

def hook(c):
    tl = c.T('layout')
    if c.on(tl): page(c, 420, 'blank', tl)
    ti = c.T('invisible')
    if c.on(ti): stamp(c.cv, 540, 690, 'INVISIBLE TEXT', 62, c.P(ti, 0.35), -4, RED); c.sfx(ti, 'thud')
    tt = c.T('three')
    if c.on(tt): counter(c, 540, 930, 0, 3.0, tt, tt + 1.4, '{:.1f}', 90, RED, ' s')
    tw = c.T('waiting')
    if c.on(tw): txt(c, 540, 1080, 'the words are waiting for a font', tw, 'intx', 40, INK)

def foit(c):
    title(c, 'FOIT vs FOUT', 330, c.T('FOIT'), 110, hlcol=YEL)
    ti = c.T('hides')
    if c.on(ti):
        page(c, 440, 'blank', ti, 'FOIT')
        txt(c, 540, 840, 'flash of invisible text', ti, 'intx', 34, RED)
    tu = c.T('FOUT')
    if c.on(tu):
        page(c, 900, 'web' if c.on(c.T('swap')) else 'fallback', tu, 'FOUT')
        txt(c, 540, 1300, 'flash of unstyled text', tu, 'intx', 34, GRN)

def understudy(c):
    title(c, 'THE UNDERSTUDY', 330, c.T('understudy'), 100)
    card(c.pen, 110, 440, 970, 1050, 20, (90, 30, 40), 12, 5)
    c.pen.rect(130, 460, 950, 520, fill=(190, 40, 55))
    ts = c.T('star')
    star = c.on(ts)
    person(c.pen, 540 if not star else 760, 960, 2.0, GREY if not star else YEL)
    if not star: txt(c, 540, 600, 'understudy · on time', c.T('time'), 'intx', 36, WHITE)
    else: person(c.pen, 320, 960, 1.6, GREY); txt(c, 760, 600, 'the star steps in', ts, 'intx', 36, YEL)
    te = c.T('empty')
    if c.on(te): label(c, 540, 1160, 'better than an empty stage', te, YEL, INK, 34)

def display(c):
    title(c, 'font-display', 330, c.T('font'), 96, k='monob', hlcol=YEL)
    rows(c, 90, 510, [('Block', 'block', 'hide text up to ~3 s', RED), ('Swap', 'swap', 'fallback now · swap anytime', ORANGE),
                      ('Optional', 'optional', 'tiny window · else fallback this view', GRN)], 150, 900, 120, 40, 30)
    code(c, 60, 960, 1020, 1210, ['@font-face {', "  font-family: 'Inter';", "  src: url(inter.woff2) format('woff2');", '  font-display: swap;', '}'],
         c.T('Block') - 0.5, 0.08, 22, 'fonts.css', lang='css', marks=[(3, c.T('Swap'), YEL)])

def shift(c):
    title(c, 'SWAP CAN SHIFT', 330, c.T('cost'), 100, hlcol=(255, 190, 190))
    tw = c.T('widths')
    if c.on(tw):
        c.pen.text(140, 520, 'Monsoon Sale is live today', 'intm', 48, GREY, 'lm')
        c.pen.text(140, 600, 'Monsoon Sale is live today', 'osw', 58, INK, 'lm')
        c.pen.text(140, 690, '↑ fallback  ·  ↓ web font: different width', 'ints', 28, MUTE, 'lm')
    tl = c.T('shifts')
    if c.on(tl): stamp(c.cv, 760, 780, 'CLS', 64, c.P(tl, 0.35), -6, RED); c.sfx(tl, 'thud')
    code(c, 60, 860, 1020, 1210, ['@font-face {', "  font-family: 'Inter Fallback';", "  src: local('Arial');", '  size-adjust: 107%;', '  ascent-override: 90%;', '}'],
         c.T('matching') - 0.5, 0.1, 24, 'fonts.css', lang='css', marks=[(3, c.T('size'), (60, 110, 70)), (4, c.T('ascent'), (60, 110, 70))])

def faster(c):
    title(c, 'MAKE IT ARRIVE SOONER', 330, c.T('sooner'), 84)
    rows(c, 90, 510, [('self', 'self-host it', 'no extra origin to connect to', 'ok'), ('preload', 'preload 1–2 above-the-fold files', None, 'ok'),
                      ('woff2', 'use woff2', 'best-compressed font format', 'ok'), ('subset', 'subset it', 'only the characters you need', 'ok')], 150, 900, 120, 40, 28)

def proof(c):
    panel(c, 50, 330, 1030, 900, tabs=('Network', 'Font'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tt = c.T('throttle')
    if c.on(tt):
        c.pen.rr(100, 460, 560, 530, 12, fill=(40, 46, 56), outline=(90, 96, 106), w=2); c.pen.text(130, 495, 'Slow 4G', 'int', 30, YEL, 'lm')
        netrows(c, 100, 610, 1000, [(tt + 0.3, 'inter-400.woff2', ['24 KB', '2.1 s']), (tt + 0.5, 'inter-700.woff2', ['26 KB', '2.3 s'])], 28, 80, [620, 820])
    tr = c.T('Reload')
    if c.on(tr):
        page(c, 960, 'blank' if int((c.t - tr) / 1.5) % 2 == 0 else 'fallback', tr)

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, 'Safest font-display for Core Web Vitals?', c.T('safest'), 'intx', 44, INK)
    to = c.T('optional')
    if c.on(to): title(c, 'optional', 620, to, 110, GRN, k='monob')
    rows(c, 140, 790, [('invisible', 'no invisible text', None, 'ok'), ('swap', 'no late swap → no shift', None, 'ok'),
                       ('trade', 'slow first visit: may skip your font', None, 'no')], 130, 800, 100, 36)

SCENES = [
    (hook, "The page loads. The layout is there. But the text is invisible, blank space where the headline should be, for up to three seconds. The words are waiting for a font."),
    (foit, "That's FOIT, a flash of invisible text: the browser hides text while the web font downloads. The alternative is FOUT, a flash of unstyled text: show a fallback font right away, and swap when the web font arrives."),
    (understudy, "Think of an understudy. The show starts on time, and the star steps in when they arrive. It beats an audience staring at an empty stage."),
    (display, "You choose with font display. Block hides text for up to three seconds. Swap shows the fallback immediately, and swaps whenever the font arrives. Optional gives the font a tiny window, and if it misses, keeps the fallback for this page view."),
    (shift, "But swap has a cost. The fallback and the web font have different widths, so when they swap, text reflows, and the layout shifts. Fix it by matching the fallback, with size adjust and ascent override."),
    (faster, "And make the font arrive sooner. Self host it. Preload the one or two files above the fold. Use woff2. And subset it to the characters you need."),
    (proof, "Try it. In DevTools, open Network, filter by Font, and throttle to Slow 4G. Reload, and watch whether your text goes invisible, or swaps."),
    (gotcha, "Interview question: what's the safest font display value for Core Web Vitals? Often, optional. No invisible text, and no late swap to shift the layout. The trade off: on a slow first visit, users might not see your font at all."),
    (scene_next('S3 · E21', 'THIRD-PARTY COST', 'the scripts you invited in', 'third', 'invited'),
     "Next: the real cost of third party scripts, the code you invited in. Comment NOTES for the cheat sheet."),
]
