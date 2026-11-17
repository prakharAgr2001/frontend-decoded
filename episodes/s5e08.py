from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E08', tag='S5 · E08', short='INFINITE SCROLL vs PAGES')

COLS = [BLUE, ORANGE, GRN, PURPLE, TEAL, PINK]


def hook(c):
    ti = c.T('Instagram')
    if c.on(ti):
        inner = phone(c, 290, 800, 400, 760, dy=(1 - c.P(ti, 0.45)) * 900)
        x0, y0, x1, y1 = inner
        off = (c.t * 160) % 170
        for k in range(6):
            y = y0 + 10 + k * 170 - off
            if y < y0 or y + 150 > y1: continue
            post(c, x0 + 14, y, x1 - 14, f'post', COLS[k % 6], h=150)
        txt(c, 290, 330, 'scrolls forever', ti + 0.3, 'intx', 36, INK)
    ta = c.T('Amazon')
    if c.on(ta):
        inner = phone(c, 790, 800, 400, 760, dy=(1 - c.P(ta, 0.45)) * 900)
        x0, y0, x1, y1 = inner
        for k in range(3): c.pen.rr(x0 + 20, y0 + 20 + k * 160, x1 - 20, y0 + 160 + k * 160, 12, fill=LIGHT, outline=GREY, w=2)
        for k in range(4):
            x = x0 + 30 + k * 85
            c.pen.rr(x, y1 - 110, x + 70, y1 - 40, 10, fill=YEL if k == 0 else WHITE, outline=INK, w=3)
            c.pen.text(x + 35, y1 - 75, str(k + 1), 'intx', 30, INK)
        txt(c, 790, 330, 'page numbers', ta + 0.3, 'intx', 36, INK)
    te = c.T('exactly')
    if c.on(te): label(c, 540, 1290, 'both are on purpose', te, YEL, INK, 34)


def analogy(c):
    tc = c.T('conveyor')
    if c.on(tc):
        title(c, 'CONVEYOR BELT', 360, tc, 80)
        c.pen.rr(80, 520, 1000, 600, 40, fill=GREY, outline=INK, w=5)
        for k in range(8):
            x = 80 + ((c.t * 140 + k * 130) % 920)
            c.pen.ell(x - 40, 525, x + 40, 560, fill=WHITE, outline=INK, w=3)
            c.pen.circ(x, 535, 12, fill=COLS[k % 6])
    ts = c.T('stop')
    if c.on(ts): txt(c, 540, 660, 'you never decide to stop', ts, 'intx', 36, INK)
    tch = c.T('chapters')
    if c.on(tch):
        title(c, 'BOOK WITH CHAPTERS', 800, tch, 80)
        for k in range(5):
            x = 150 + k * 160
            c.pen.rr(x, 900, x + 140, 1080, 10, fill=YEL if k == 3 and c.on(c.T('four')) else WHITE, outline=INK, w=4)
            c.pen.text(x + 70, 990, f'Ch {k + 1}', 'intx', 32, INK)
    tf = c.T('four')
    if c.on(tf): txt(c, 540, 1160, 'you know where you are', tf, 'intx', 36, INK)


def tradeoffs(c):
    versus(c, ('INFINITE', PURPLE, c.T('browsing'), [(c.T('browsing'), '+ endless browsing on phones'), (c.T('footer'), '− footer unreachable'),
                                                       (c.T('back'), '− back button loses place'), (c.T('memory'), '− memory keeps growing')]),
              ('PAGES', GRN, c.T('hunt'), [(c.T('hunt'), '+ good for hunting'), (c.T('share'), '+ shareable "page 3" URL'),
                                           (c.T('crawl'), '+ crawlable'), (c.T('crawl') + 0.6, '− more clicks')]), 400, 1180, 34)


def loadmore(c):
    inner = phone(c, 540, 820, 480, 900, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    for k in range(3): post(c, x0 + 20, y0 + 20 + k * 170, x1 - 20, 'post', COLS[k], h=150)
    tl = c.T('load')
    if c.on(tl):
        s = c.B(tl, 0.35); c.sfx(tl, 'pop')
        c.pen.rr(x0 + 60, y0 + 540, x1 - 60, y0 + 620, 40, fill=YEL, outline=INK, w=4)
        c.pen.text((x0 + x1) / 2, y0 + 580, 'Load more', 'intx', 36 * s, INK)
    tf = c.T('footer')
    if c.on(tf):
        c.pen.rect(x0, y1 - 80, x1, y1, fill=INK)
        c.pen.text((x0 + x1) / 2, y1 - 40, 'footer · about · help', 'int', 24, WHITE)
        check(c.pen, x1 + 70, y1 - 40, 1.2, GRN, 10, c.P(tf, 0.3))
    tc = c.T('control')
    if c.on(tc): label(c, 540, 330, 'the user stays in control', tc, YEL, INK, 34)


CODE = ['const io = new IntersectionObserver(([e]) => {', '  if (e.isIntersecting) loadMore();', "}, { rootMargin: '600px' });", '', 'io.observe(sentinel);']


def build(c):
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 340, 'S1 · E23', 'Observers', ts)
    code(c, 30, 420, 1050, 420 + 72 + len(CODE) * 50 + 20, CODE, c.T('Intersection'), 0.1, 26, 'feed.js',
         marks=[(4, c.T('sentinel'), YEL), (1, c.T('fetch'), YEL)])
    tv = c.T('view')
    lx0, lx1 = 300, 780
    if c.on(c.T('sentinel')):
        for k in range(3): c.pen.rr(lx0, 840 + k * 90, lx1, 910 + k * 90, 10, fill=WHITE, outline=INK, w=3)
        c.pen.rr(lx0, 1120, lx1, 1150, 6, fill=None, outline=RED, w=4)
        c.pen.text(540, 1190, 'sentinel', 'monob', 26, RED)
    if c.on(tv):
        p = c.P(tv, 0.6)
        c.pen.rr(lx0 - 30, 1250 - 330 * p, lx1 + 30, 1250 - 330 * p + 260, 16, outline=BLUE, w=6)
        c.pen.text(lx0 - 50, 1250 - 330 * p + 130, 'viewport', 'int', 24, BLUE, 'rm')


def memory(c):
    tt = c.T('thousand')
    if c.on(tt): counter(c, 540, 470, 0, 1000, tt, tt + 1.2, '{:,.0f}', 120, RED, ' DOM nodes')
    tv = c.T('virtualization')
    if c.on(tv):
        chapter(c, 540, 640, 'S3 · E25', 'Virtualization', tv)
        for k in range(10):
            y = 740 + k * 56
            vis = 3 <= k <= 6
            c.pen.rr(330, y, 750, y + 46, 8, fill=WHITE if vis else LIGHT, outline=INK if vis else GREY, w=3)
        tvi = c.T('visible')
        if c.on(tvi):
            c.pen.rr(300, 740 + 3 * 56 - 14, 780, 740 + 7 * 56 + 4, 14, outline=BLUE, w=6)
            txt(c, 540, 1340, 'only visible rows stay in the DOM', tvi, 'intx', 32, INK)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tb = c.T('back')
    if c.on(tb):
        node(c, 260, 600, 300, 200, 'post 87', tb - 0.6, 'doc')
        node(c, 820, 600, 300, 200, 'top of feed', c.T('top'), 'phone', fill=(255, 220, 220))
        arrow(c.pen, 430, 600, 650, 600, c.P(tb, 0.4), RED, 7)
        txt(c, 540, 550, 'back', tb, 'intx', 30, RED)
    rows(c, 100, 860, [(c.T('cache'), 'keep pages + scroll position', 'in a query cache or the URL', 'ok'),
                       (c.T('restore'), 'restore them on back', None, 'ok'), (c.T('refetch'), 'refetch from page 1', None, 'no')], gap=140, h=115, size=36)


SCENES = [
    (hook, "Instagram scrolls forever. Amazon search results still have page numbers. Both teams know exactly what they're doing."),
    (analogy, "Infinite scroll is a conveyor belt sushi bar. Plates keep coming, and you never decide to stop. Pages are a book with chapters. You know where you are, and you can come back to chapter four."),
    (tradeoffs, "Infinite scroll wins for browsing, especially on phones. But the footer becomes unreachable, the back button loses your place, and memory keeps growing. Pages win when users hunt for something, share a link to page three, or need search engines to crawl it."),
    (loadmore, "The middle ground is a load more button. The user stays in control, and the footer stays reachable."),
    (build, "Infinite scroll is built with an Intersection Observer, from season one. Watch an invisible sentinel at the bottom of the list. When it comes into view, fetch the next page."),
    (memory, "After a thousand posts, you have thousands of DOM nodes. That's where virtualization, from season three, keeps only the visible rows alive."),
    (gotcha, "Interview trap. A user opens post eighty seven, presses back, and lands at the top of the feed. How do you fix it? Keep the loaded pages and the scroll position, in a query cache or in the URL. Restore them when the user returns. Don't refetch from page one."),
    (scene_next('S5 · E09', 'IQ: PAGINATION', '4 interview questions', 'four', 'pagination'),
     "Next: four interview questions on pagination. Comment NOTES for the cheat sheet."),
]
