from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E07', tag='S5 · E07', short='CURSOR PAGINATION', hook='"10 older than this one"')


def hook(c):
    ts = c.T('skip')
    if c.on(ts):
        pill(c.pen, 540, 370, '“skip 10”', c.B(ts, 0.35), WHITE, INK, 40)
        cross(c.pen, 700, 370, 1.0, RED, 10, c.P(c.T('what'), 0.3))
    to = c.T('older')
    if c.on(to): pill(c.pen, 540, 470, '“10 posts older than #a91f”', c.B(to, 0.35), YEL, INK, 40)
    x = 300; y0 = 580; g = 68
    tm = c.T('matter')
    new = c.on(tm)
    for k in range(10):
        y = y0 + (k + (c.P(tm, 0.5) if new else 0)) * g
        mark = k == 3
        c.pen.rr(x, y, x + 480, y + g - 12, 10, fill=YEL if mark and c.on(c.T('exact')) else WHITE, outline=INK, w=3)
        c.pen.text(x + 30, y + (g - 12) / 2, '#a91f' if mark else f'post {k + 1}', 'monob' if mark else 'int', 28, INK, 'lm')
    if new:
        s = c.B(tm, 0.35)
        c.pen.rr(x, y0, x + 480 * s, y0 + g - 12, 10, fill=(200, 240, 200), outline=INK, w=3)
        c.pen.text(x + 240, y0 + (g - 12) / 2, 'NEW posts on top', 'intx', 28 * s, INK)
    if c.on(c.T('exact')):
        arrow(c.pen, 820, y0 + 4.6 * g, 820, y0 + 9.5 * g, c.P(c.T('exact'), 0.5), INK, 7)
        txt(c, 880, y0 + 7 * g, 'next 10', c.T('exact') + 0.3, 'intx', 30, INK, 'lm')


def ribbon(c):
    title(c, 'A BOOKMARK RIBBON', 340, c.T('bookmark'), 90)
    ta = c.T('added')
    n = int(cl((c.t - ta) / 0.4, 0, 4)) if c.on(ta) else 0
    for k in range(6, -1, -1):
        x = 300 + k * 18; y = 520 + k * 10
        c.pen.rr(x, y, x + 420, y + 560, 12, fill=WHITE, outline=INK, w=4)
    for k in range(n):
        x = 300 - (k + 1) * 18; y = 520 - (k + 1) * 10
        c.pen.rr(x, y, x + 420, y + 560, 12, fill=(255, 240, 200), outline=INK, w=4)
        c.sfx(ta + k * 0.4, 'swish')
    rx = 600
    c.pen.poly([(rx, 470), (rx + 50, 470), (rx + 50, 1180), (rx + 25, 1150), (rx, 1180)], fill=RED, outline=INK, w=4)
    tsp = c.T('stopped')
    if c.on(tsp): label(c, 540, 1260, 'stays exactly where you stopped', tsp, YEL, INK, 32)


def how(c):
    title(c, 'THE CURSOR', 340, c.T('cursor'), 100, hlcol=YEL)
    code(c, 60, 430, 1020, 430 + 72 + 6 * 50 + 20, ['{', '  "items": [ …10 posts… ],', '  "nextCursor": "eyJpZCI6OTF9"', '}'],
         c.T('items') - 0.2, 0.1, 30, 'GET /posts', marks=[(2, c.T('opaque'), YEL)])
    tb = c.T('back')
    if c.on(tb): method(c, 90, 900, 'GET', '/posts?after=eyJpZCI6OTF9', tb, 28)
    te = c.T('end')
    if c.on(te):
        code(c, 60, 1000, 1020, 1000 + 72 + 1 * 50 + 30, ['"nextCursor": null   // the end'], te - 0.2, 0.1, 30, 'last page', dy=0)


CODE = ['let cursor = null;', 'async function loadMore() {', "  const q = cursor ? `?after=${cursor}` : '';",
        '  const res = await fetch(`/api/posts${q}`);', '  const { items, nextCursor } = await res.json();', '  render(items);', '  cursor = nextCursor;', '}']


def client(c):
    code(c, 30, 380, 1050, 380 + 72 + len(CODE) * 50 + 20, CODE, c.T('tiny'), 0.1, 26, 'feed.js',
         marks=[(0, c.T('variable'), YEL), (2, c.T('after'), YEL), (6, c.T('replace'), YEL)])


def server(c):
    code(c, 60, 380, 1020, 380 + 72 + 4 * 54 + 20, ['SELECT * FROM posts', 'WHERE created_at < :cursor', 'ORDER BY created_at DESC', 'LIMIT 10;'],
         c.T('server'), 0.12, 32, 'query.sql', lang='sql', marks=[(1, c.T('WHERE'), YEL)])
    ti = c.T('index')
    if c.on(ti):
        bars(c, 100, 840, [('page 1', 10, GRN, ti), ('page 1,000', 10, GRN, c.T('thousand'))], 100, w=560, h=70, gap=120,
             fmt='{} rows read', lab_w=250, size=30)
    tf = c.T('fast')
    if c.on(tf): stamp(c.cv, 540, 1140, 'SAME SPEED', 70, c.P(tf, 0.35), -4, GRN); c.sfx(tf, 'thud')


def proof(c):
    browser(c, 60, 330, 1020, 1120, 'reddit.com/r/javascript.json', dy=(1 - c.P(0, 0.45)) * 900)
    tj = c.T('json')
    code(c, 100, 470, 980, 470 + 72 + 6 * 52 + 30, ['"data": {', '  "children": [ … ],', '  "after": "t3_1q2w3e",', '  "before": null', '}'],
         tj + 0.3, 0.12, 30, 'response', dy=0, marks=[(2, c.T('after'), YEL)])
    tc = c.T('cursor')
    if c.on(tc): label(c, 540, 960, 'after = the cursor for the next page', tc, YEL, INK, 30)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    ts = c.T('same')
    if c.on(ts):
        for k, (tm, nm) in enumerate((('12:00:01', 'post A'), ('12:00:01', 'post B'), ('12:00:01', 'post C'))):
            y = 500 + k * 90
            c.pen.rr(140, y, 700, y + 70, 10, fill=WHITE, outline=INK, w=3)
            c.pen.text(170, y + 35, tm, 'monob', 28, INK, 'lm')
            c.pen.text(670, y + 35, nm, 'int', 28, INK, 'rm')
        c.pen.line([(130, 590), (720, 590)], RED, 5)
        txt(c, 740, 590, 'page cut here', ts + 0.4, 'intx', 28, RED, 'lm')
    tk = c.T('skip')
    if c.on(tk): stamp(c.cv, 540, 840, 'B + C SKIPPED', 60, c.P(tk, 0.35), -4, RED); c.sfx(tk, 'thud')
    code(c, 60, 950, 1020, 950 + 72 + 2 * 50 + 30, ['ORDER BY created_at DESC, id DESC', '-- cursor = (created_at, id)'],
         c.T('unique'), 0.12, 28, 'fix.sql', lang='sql', marks=[(0, c.T('unique') + 0.6, YEL), (1, c.T('both'), YEL)])


def tradeoff(c):
    title(c, 'THE COST', 340, 0.1, 100)
    tj = c.T('jump')
    if c.on(tj):
        for k in range(5):
            x = 170 + k * 150
            lab = ['1', '2', '…', '50', '…'][k]
            c.pen.rr(x, 470, x + 120, 570, 14, fill=WHITE, outline=INK, w=4)
            c.pen.text(x + 60, 520, lab, 'intx', 40, INK)
        cross(c.pen, 680, 520, 1.6, RED, 12, c.P(tj + 0.2, 0.3))
    tf = c.T('forward')
    if c.on(tf): label(c, 540, 680, 'only forward (or back)', tf, YEL, INK, 34)
    tfe = c.T('feeds')
    rows(c, 140, 850, [(tfe, 'feeds, timelines, chats', 'cursor', 'ok'), (c.T('search'), 'jump-to-page tables', 'often offset', GREY)], gap=170, w=800, h=130)


SCENES = [
    (hook, "Instead of saying skip ten, what if page two said: give me ten posts older than this exact post? Then new posts on top don't matter anymore."),
    (ribbon, "That's a bookmark ribbon, instead of a page number. However many pages get added, the ribbon stays tucked in exactly where you stopped."),
    (how, "The server returns the items, plus a cursor. An opaque string that points at the last item. The client sends it back to get the next page. And when there's no cursor, you've reached the end."),
    (client, "On the client, it's tiny. Keep the cursor in a variable, send it as after, and replace it with the next cursor every time."),
    (server, "On the server, it's a WHERE clause, instead of OFFSET. Created before the cursor, ordered, limit ten. With an index, page one thousand is as fast as page one."),
    (proof, "See it on Reddit. Add dot json to a subreddit URL. Near the bottom of the response there's a field called after. That's the cursor for the next page."),
    (gotcha, "Interview trap. What if two posts have the same timestamp, right at the page edge? Your cursor can skip them. Make the sort key unique. Order by created at, then by id, and put both in the cursor."),
    (tradeoff, "The cost: you can't jump to page fifty. Cursors only move forward, or back. That's why feeds use cursors, and jump to page search results often don't."),
    (scene_next('S5 · E08', 'INFINITE SCROLL vs PAGES', 'which one your product needs', 'infinite', 'product'),
     "Next: infinite scroll versus pages, and which one your product needs. Comment NOTES for the cheat sheet."),
]
