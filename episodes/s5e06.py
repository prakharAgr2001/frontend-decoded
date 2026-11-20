from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E06', tag='S5 · E06', short='THE OFFSET BUG', hook='why page 2 repeats a post')

COLS = [BLUE, ORANGE, GRN, PURPLE, TEAL, PINK]


def hook(c):
    inner = phone(c, 540, 800, 520, 900, dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    ts = c.T('scroll')
    off = 150 * 4 * eio(lin(c.t, ts, ts + 1.6))
    two = c.T('two')
    labels = [f'Post {k}' for k in range(5, 11)]
    if c.on(two): labels += ['Post 10', 'Post 11', 'Post 12']
    else: labels += []
    for k, lb in enumerate(labels):
        y = y0 + 30 + k * 170 - off
        if y < y0 or y + 150 > y1: continue
        dup = c.on(c.T('duplicate')) and k == 6
        post(c, x0 + 24, y, x1 - 24, lb, COLS[k % 6], hi=(255, 190, 190) if dup else None, sub='page 2' if k >= 6 else 'page 1')
    td = c.T('duplicate')
    if c.on(td): stamp(c.cv, 540, 1310, 'DUPLICATE', 80, c.P(td, 0.35), -4, RED); c.sfx(td, 'thud')


def define(c):
    title(c, 'OFFSET PAGINATION', 340, c.T('offset'), 90, hlcol=YEL)
    method(c, 90, 500, 'GET', '/posts?limit=10&offset=0', c.T('one'), 30)
    method(c, 90, 600, 'GET', '/posts?limit=10&offset=10', c.T('two'), 30)
    code(c, 60, 700, 1020, 700 + 72 + 4 * 50 + 20, ['SELECT * FROM posts', 'ORDER BY created_at DESC', 'LIMIT 10 OFFSET 10;'],
         c.T('Skip'), 0.12, 30, 'query.sql', lang='sql', marks=[(2, c.T('Skip') + 0.5, YEL)])
    tn = c.T('next')
    if c.on(tn): label(c, 540, 1130, 'skip 10 rows, return the next 10', tn, YEL, INK, 32)


def bug(c):
    tp = c.T('publishes')
    sh = c.P(c.T('slides'), 0.6)
    base = [(f'Post {k}', COLS[k % 6]) for k in range(1, 15)]
    x = 140; y0 = 380; g = 56
    # new post at top
    if c.on(tp):
        s = c.B(tp, 0.4)
        c.pen.rr(x, y0, x + 300 * s, y0 + (g - 10) * s, 10, fill=YEL, outline=INK, w=3)
        c.pen.text(x + 150, y0 + (g - 10) / 2, 'NEW post', 'intx', 28 * s, INK)
    for k, (lb, col) in enumerate(base):
        y = y0 + (k + (sh if c.on(tp) else 0)) * g
        if k == 9 and c.on(c.T('eleven')): fill = (255, 190, 190)
        else: fill = WHITE
        if y > 1300: continue
        c.pen.rr(x, y, x + 300, y + g - 10, 10, fill=fill, outline=INK, w=3)
        c.pen.circ(x + 34, y + (g - 10) / 2, 15, fill=col, outline=INK, w=2)
        c.pen.text(x + 64, y + (g - 10) / 2, lb, 'int', 28, INK, 'lm')
    # page windows
    c.pen.text(470, y0 + 5 * g, 'page 1', 'intx', 30, INK, 'lm')
    c.pen.line([(455, y0), (455, y0 + 10 * g - 10)], INK, 5)
    ta = c.T('again')
    if c.on(c.T('eleven')):
        c.pen.line([(475, y0 + 10 * g), (475, min(1300, y0 + 20 * g - 10))], RED, 6)
        txt(c, 500, y0 + 10 * g + 30, 'offset 10 starts here', c.T('eleven'), 'intx', 30, RED, 'lm')
    if c.on(ta): stamp(c.cv, 760, 1180, 'POST 10 AGAIN', 56, c.P(ta, 0.35), -6, RED); c.sfx(ta, 'thud')


def deletes(c):
    title(c, 'DELETES: THE OPPOSITE', 340, c.T('Deletes'), 76)
    tr = c.T('removed')
    up = c.P(c.T('up'), 0.6)
    x = 140; y0 = 460; g = 72
    for k in range(1, 13):
        if k == 3 and c.on(tr):
            p = c.P(tr, 0.4)
            if p >= 1: continue
        yy = k - 1 - (up if k > 3 else 0)
        y = y0 + yy * g
        fill = (255, 190, 190) if (k == 11 and c.on(c.T('skipped'))) else WHITE
        c.pen.rr(x, y, x + 300, y + g - 10, 10, fill=fill, outline=INK, w=3)
        c.pen.text(x + 30, y + (g - 10) / 2, f'Post {k}', 'int', 28, INK, 'lm')
    c.pen.line([(470, y0), (470, y0 + 10 * g - 10)], INK, 5)
    c.pen.text(490, y0 + 5 * g, 'page 1', 'intx', 30, INK, 'lm')
    ts = c.T('skipped')
    if c.on(ts):
        c.pen.line([(470, y0 + 10 * g), (470, y0 + 12 * g)], RED, 5)
        stamp(c.cv, 760, 1180, 'POST 11: SKIPPED', 52, c.P(ts, 0.35), -5, RED); c.sfx(ts, 'thud')
    tn = c.T('never')
    if c.on(tn): txt(c, 760, 1270, 'you never see it', tn, 'intx', 34, INK)


def diary(c):
    title(c, 'THE GROWING DIARY', 340, c.T('diary'), 90)
    tf = c.T('front')
    n_new = int(cl((c.t - tf) / 0.35, 0, 4)) if c.on(tf) else 0
    for k in range(6, -1, -1):
        x = 300 + k * 18 - n_new * 0; y = 520 + k * 10
        c.pen.rr(x, y, x + 420, y + 560, 12, fill=WHITE, outline=INK, w=4)
    for k in range(n_new):
        x = 300 - (k + 1) * 18; y = 520 - (k + 1) * 10
        c.pen.rr(x, y, x + 420, y + 560, 12, fill=(255, 240, 200), outline=INK, w=4)
        c.sfx(tf + k * 0.35, 'swish')
    tn = c.T('number')
    if c.on(tn): pill(c.pen, 510, 800, 'p. 40', c.B(tn, 0.35), YEL, INK, 50)
    t4 = c.T('forty')
    if c.on(t4): label(c, 540, 1180, 'page 40 is no longer where you left off', t4, (255, 220, 220), INK, 30)


def slow(c):
    title(c, 'DEEP PAGES ARE SLOW', 340, c.T('second'), 84, hlcol=YEL)
    tw = c.T('walks')
    if c.on(tw):
        counter(c, 540, 560, 0, 100000, tw, tw + 1.6, '{:,.0f}', 110, INK, '')
        txt(c, 540, 660, 'rows read, then thrown away', c.T('away'), 'intx', 36, RED)
    bars(c, 100, 780, [('page 1', 10, GRN, tw), ('page 100', 1000, ORANGE, tw + 0.3), ('page 10,000', 100000, RED, c.T('slower'))],
         100000, w=440, h=70, gap=120, fmt='{:,} rows', lab_w=250, size=30)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tw = c.T('wrong')
    if c.on(tw): txt(c, 540, 470, 'So offset is always wrong?', tw, 'intx', 50, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 590, 'NO', 110, c.P(tn, 0.35), -5, RED); c.sfx(tn, 'thud')
    rows(c, 100, 760, [(c.T('rarely'), 'data that rarely changes', None, 'ok'), (c.T('seven'), 'users jump to page 7', 'admin tables, search results', 'ok'),
                       (c.T('breaks'), 'fast-changing feeds', None, 'no')], gap=140, h=110, size=36)


SCENES = [
    (hook, "You scroll a feed, and load page two. The first post on it is the last post you just saw. A duplicate. Nobody wrote a bug in the frontend."),
    (define, "Most feeds start with offset pagination. Page one: limit ten, offset zero. Page two: limit ten, offset ten. Skip the first ten rows, return the next ten."),
    (bug, "Now, while you read page one, someone publishes a new post. It goes on top, and every post slides down one place. Post ten is now at position eleven. So offset ten returns it again."),
    (deletes, "Deletes cause the opposite. One post is removed from page one, everything slides up, and a post gets skipped. You never see it."),
    (diary, "It's like saving your place in a diary by page number, while someone keeps adding pages at the front. Page forty is no longer where you left off."),
    (slow, "There's a second problem. To serve offset one hundred thousand, the database still walks past a hundred thousand rows, and throws them away. Deep pages get slower and slower."),
    (gotcha, "Interview trap. So offset pagination is always wrong? No. For data that rarely changes, like an admin table, or search results where users jump to page seven, offset is simple and fine. It breaks on fast changing feeds."),
    (scene_next('S5 · E07', 'CURSOR PAGINATION', '“give me 10 after this one”', 'cursor', 'specific'),
     "Next: cursor pagination, which asks for the next ten after one specific post. Comment NOTES for the cheat sheet."),
]
