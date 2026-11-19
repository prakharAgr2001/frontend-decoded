from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E03', tag='S3 · E03', short='LCP', hook='when does a page feel loaded?')

def page(c, at_logo, at_menu, at_hero, dy=0, box_at=None):
    browser(c, 110, 330, 970, 1150, url='news.example.com', dy=dy)
    if c.on(at_logo): c.pen.rr(150, 440 + dy, 330, 500 + dy, 10, fill=INK); c.pen.text(240, 470 + dy, 'NEWS', 'osw', 36, YEL)
    if c.on(at_menu):
        for k in range(3): c.pen.rr(560 + k * 130, 450 + dy, 670 + k * 130, 490 + dy, 10, fill=LIGHT)
    if c.on(at_hero):
        p = c.P(at_hero, 0.4)
        c.pen.rect(150, 540 + dy, 150 + 780 * p, 900 + dy, fill=(120, 170, 210))
        c.pen.poly([(150, 900 + dy), (420, 680 + dy), (650, 900 + dy)], fill=(70, 120, 90))
        c.pen.circ(800, 640 + dy, 50, fill=YEL)
        c.pen.text(150, 960 + dy, 'Monsoon arrives early', 'intx', 50, INK, 'lm')
        for k in range(2): c.pen.rr(150, 1020 + k * 50 + dy, 900 - k * 200, 1045 + k * 50 + dy, 8, fill=LIGHT)
    if box_at is not None and c.on(box_at):
        q = c.P(box_at, 0.4)
        c.pen.rect(140, 530 + dy, 940, 910 + dy, outline=RED, w=int(7 * q) + 1)
        pill(c.pen, 790, 530 + dy, 'largest element', c.B(box_at, 0.35), RED, WHITE, 28, outline=None)

def hook(c):
    page(c, c.T('logo'), c.T('menu'), c.T('photo'))
    tn = c.T('name')
    if c.on(tn): stamp(c.cv, 540, 1260, 'THIS MOMENT = LCP', 64, c.P(tn, 0.35), -3, RED); c.sfx(tn, 'thud')

def define(c):
    page(c, -1, -1, -1, dy=-80, box_at=c.T('biggest'))
    tg = c.T('Good')
    if c.on(tg):
        timerbar(c, 140, 1180, 940, 0.62, tg, 'LCP', GRN, 50, '≤ 2.5 s = good')

def frontpage(c):
    card(c.pen, 220, 340, 860, 1180, 10, WHITE, 12, 5)
    c.pen.text(540, 420, 'THE DAILY', 'osw', 70, INK); c.pen.line([(260, 470), (820, 470)], INK, 5)
    tn = c.T('number')
    c.pen.text(820, 1140, 'p. 1', 'int', 26, INK, 'rm')
    if c.on(tn): c.pen.circ(800, 1140, 40, outline=GREY, w=4)
    th = c.T('headline')
    c.pen.rect(270, 510, 810, 860, fill=(200, 200, 195))
    for k in range(5): c.pen.rr(270, 900 + k * 45, 810 - (k % 2) * 120, 920 + k * 45, 6, fill=LIGHT)
    if c.on(th):
        c.pen.rect(270, 510, 810, 860, fill=(120, 170, 210)); c.pen.poly([(270, 860), (500, 660), (700, 860)], fill=(70, 120, 90))
        c.pen.rect(262, 502, 818, 868, outline=RED, w=8)
    tw = c.T('watches')
    if c.on(tw): label(c, 540, 1270, 'LCP waits for the headline photo', tw, YEL, INK, 34)

def candidates(c):
    title(c, 'WHAT COUNTS?', 330, c.T('What'), 100)
    chips(c, 110, 470, [('<img>', YEL), ('<video poster>', (255, 225, 190)), ('CSS background-image', (220, 230, 250)), ('block of text', (215, 240, 215))],
          c.T('Images'), 0.45, 34)
    tc = c.T('change')
    if c.on(tc):
        axis(c, 140, 940, 900, tc, [(0.2, 'h1 = LCP', c.T('heading'), ORANGE), (0.7, 'hero image = LCP', c.T('arrives'), GRN)])
        txt(c, 540, 1040, 'the browser keeps updating the candidate until you interact', c.T('arrives'), 'ints', 30, MUTE)

def parts(c):
    title(c, '4 PARTS OF LCP', 330, c.T('four'), 100, hlcol=YEL)
    segs = [('TTFB', 0.18, BLUE, 'Time'), ('Load delay', 0.38, RED, 'delay'), ('Load duration', 0.22, ORANGE, 'duration'), ('Render delay', 0.22, PURPLE, 'render')]
    x = 90
    for k, (nm, w, col, kw) in enumerate(segs):
        t = c.T(kw); ww = 900 * w
        if c.on(t):
            p = c.P(t, 0.4); c.sfx(t, 'pop')
            c.pen.rect(x + 6, 560 + 8, x + ww * p + 6, 680 + 8, fill=INK)
            c.pen.rect(x, 560, x + ww * p, 680, fill=col, outline=INK, w=4)
            y = 740 + (k % 2) * 70
            c.pen.line([(x + ww / 2, 690), (x + ww / 2, y - 25)], INK, 3)
            c.pen.text(x + ww / 2, y, nm, 'intx', 32, INK)
        x += ww
    tm = c.T('Often')
    if c.on(tm):
        stamp(c.cv, 330, 1000, 'THE DELAY', 64, c.P(tm, 0.35), -4, RED); c.sfx(tm, 'thud')
        txt(c, 540, 1140, 'the image is found too late, not downloaded too slowly', tm + 0.4, 'ints', 32, INK)

def proof(c):
    panel(c, 60, 330, 1020, 1200, tabs=('Performance', 'Insights'), dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('record')
    if c.on(tr):
        blocks = [(0.0, 0.12, 0, 'JS'), (0.15, 0.1, 0, 'Style'), (0.27, 0.08, 0, 'Layout'), (0.36, 0.06, 0, 'Paint'), (0.5, 0.15, 0, 'JS'), (0.7, 0.08, 0, 'Paint')]
        flame(c, 100, 520, 980, blocks, tr, 60)
    tm = c.T('marker')
    if c.on(tm):
        x = 100 + 880 * 0.74
        c.pen.line([(x, 470), (x, 620)], GRN, 5); pill(c.pen, x, 455, 'LCP 3.1 s', c.B(tm, 0.3), GRN, WHITE, 26, outline=None)
    ti = c.T('insights')
    if c.on(ti):
        c.pen.text(100, 700, 'LCP breakdown', 'intx', 34, WHITE, 'lm')
        kv(c, 120, 770, 980, [(ti + 0.2, 'element ', 'img.hero', YEL), (ti + 0.4, 'TTFB          ', '0.4 s', WHITE),
                              (ti + 0.6, 'load delay    ', '1.6 s', RED), (ti + 0.8, 'load duration ', '0.6 s', WHITE), (ti + 1.0, 'render delay  ', '0.5 s', WHITE)], 30, 66)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    code(c, 70, 470, 1010, 640, ['<img src="hero.jpg" loading="lazy">'], c.T('lazy') - 0.3, 0.1, 30, 'index.html', lang='html',
         circles=[(0, c.T('equals'), 'loading="lazy"')])
    tw = c.T('waits')
    if c.on(tw):
        for k, (nm, kw) in enumerate((('HTML', 'browser'), ('layout', 'layout'), ('fetch hero', 'fetching'))):
            node(c, 220 + k * 320, 800, 260, 110, nm, c.T(kw), fill=(255, 225, 225) if k == 2 else WHITE)
            if k: arrow(c.pen, 220 + (k - 1) * 320 + 135, 800, 220 + k * 320 - 135, 800, c.P(c.T(kw), 0.3), INK, 6)
    tw2 = c.T('worse')
    if c.on(tw2): stamp(c.cv, 540, 1010, 'LCP GETS WORSE', 70, c.P(tw2, 0.35), -3, RED); c.sfx(tw2, 'thud')
    txt(c, 540, 1150, 'lazy-load below the fold only', tw2 + 0.6, 'intx', 38, GRN)

SCENES = [
    (hook, "You open a news article. The logo appears. Then the menu. But the page doesn't feel loaded until the big photo and headline show up. That moment has a name."),
    (define, "Largest Contentful Paint, or LCP, is the time until the biggest image or block of text in the viewport is rendered. Good is two point five seconds or less."),
    (frontpage, "It's like judging a newspaper's front page. Nobody judges it by the page number in the corner. You judge it by the headline photo. LCP watches for that photo."),
    (candidates, "What counts? Images, video posters, background images loaded through CSS, and blocks of text. And the candidate can change: a heading might be largest first, until the hero image arrives."),
    (parts, "Every LCP splits into four parts. Time to first byte. Load delay, before the image even starts downloading. Load duration. And render delay. Often, the biggest chunk is the delay, because the browser found the image too late."),
    (proof, "See it in DevTools. Open the Performance panel and record a reload. The LCP marker sits on the timeline, and the insights show the element and how long each part took."),
    (gotcha, "Interview trap: lazy load every image to make the page faster. Put loading equals lazy on the hero image, and the browser waits for layout before fetching it. Your LCP gets worse, not better."),
    (scene_next('S3 · E04', 'CLS', 'why buttons jump under your thumb', 'CLS', 'jump'),
     "Next: CLS, and why buttons jump right under your thumb. Comment NOTES for the cheat sheet."),
]
