from engine.s2_extra import *

EP = dict(id='S2E06', tag='S2 · E06', short='INCREMENTAL STATIC REGEN', hook='static pages that update')

def pricecard(c, x0, y0, price, at, stale=False):
    if not c.on(at - 0.01): return
    s = c.B(at, 0.35)
    card(c.pen, x0, y0, x0 + 400, y0 + 260 * s, 20, WHITE, 8, 4)
    if s > 0.9:
        c.pen.rr(x0 + 30, y0 + 30, x0 + 370, y0 + 120, 10, fill=(236, 240, 248))
        c.pen.text(x0 + 30, y0 + 170, 'Headphones', 'int', 30, INK, 'lm')
        c.pen.text(x0 + 30, y0 + 220, price, 'intx', 38, RED if stale else GRN, 'lm')

def hook(c):
    for i in range(12):
        at = 0.1 + i * 0.05
        if c.on(at):
            x = 120 + (i % 4) * 220; y = 380 + (i // 4) * 200
            c.pen.rr(x, y, x + 180, y + 160, 12, fill=WHITE, outline=INK, w=3)
            c.pen.text(x + 90, y + 80, 'page', 'intm', 26, MUTE)
    tp = c.T('price')
    if c.on(tp):
        c.pen.rr(334, 574, 526, 746, 14, outline=RED, w=6)
        label(c, 430, 800, '₹2,499 → ₹1,999', tp, RED, WHITE, 28)
    tr = c.T('rebuild')
    if c.on(tr):
        qtext(c, 'Rebuild all 50,000 pages?', 1000, tr, 54)
        cross(c.pen, 540, 1200, 1.3, RED, 12, c.P(tr + 0.5, 0.4))

def define(c):
    title(c, 'ISR', 330, c.T('Incremental'), 140, hlcol=YEL)
    txt(c, 540, 430, 'static page + an expiry date', c.T('expiry'), 'intx', 40, INK)
    x0, x1, y = 100, 980, 600
    tl = c.T('sixty')
    if c.on(tl):
        c.pen.line([(x0, y), (x0 + (x1 - x0) * c.P(tl, 0.5), y)], INK, 5)
        mx = x0 + (x1 - x0) * 0.45
        c.pen.line([(mx, y - 30), (mx, y + 30)], RED, 5); c.pen.text(mx, y - 60, '60 s', 'monob', 30, RED)
    tn = c.T('next')
    if c.on(tn):
        person(c.pen, 650, 810, 0.9, BLUE); c.pen.text(650, 850, 'next visitor', 'int', 26, INK)
        pricecard(c, 100, 900, '₹2,499', c.T('old'), True)
        label(c, 300, 1200, 'old page, instantly', c.T('old'), ORANGE, WHITE, 28)
    tb = c.T('background')
    if c.on(tb):
        node(c, 780, 990, 300, 170, 'rebuild', tb, 'server', size=30)
        label(c, 780, 1110, 'in the background', tb + 0.2, INK, WHITE, 26)
    ta = c.T('after', 2)
    if c.on(ta):
        pricecard(c, 580, 1170, '₹1,999', ta)

def bread(pen, cx, cy, s, col):
    pen.rr(cx - 70 * s, cy - 36 * s, cx + 70 * s, cy + 36 * s, 34 * s, fill=col, outline=INK, w=4)
    for k in range(3): pen.line([(cx - 40 * s + k * 40 * s, cy - 24 * s), (cx - 24 * s + k * 40 * s, cy + 6 * s)], INK, 3)

def analogy(c):
    tb = c.T('bakery')
    if c.on(tb):
        c.pen.text(540, 360, 'THE BAKERY SHELF', 'osw', 70, INK)
        card(c.pen, 100, 440, 980, 720, 20, WHITE, 8, 4)
        for k in range(4): bread(c.pen, 210 + k * 220, 580, 1.0, (210, 160, 100))
    to = c.T('oven')
    if c.on(to):
        card(c.pen, 600, 820, 960, 1100, 20, DARK, 8, 4)
        c.pen.rect(640, 880, 920, 1060, fill=(255, 150, 60) if int(c.t * 3) % 2 else (240, 120, 40))
        bread(c.pen, 780, 970, 0.9, (240, 210, 150)); c.pen.text(780, 1140, 'fresh tray baking', 'int', 28, INK)
    tc = c.T('customer')
    if c.on(tc):
        person(c.pen, 280, 1080, 1.0, BLUE)
        bread(c.pen, 280, 940, 0.8, (210, 160, 100))
        label(c, 280, 1140, 'takes today’s bread now', tc, YEL, INK, 26)

CODE = ['// app/product/[id]/page.js  (Next.js)', 'export const revalidate = 60; // seconds', '',
        'export default async function Page({ params }) {', '  const { id } = await params;', '  const p = await getProduct(id);',
        '  return <h1>{p.name}: {p.price}</h1>;', '}']

def how(c):
    code(c, 30, 340, 1050, 340 + 72 + 8 * 52 + 40, CODE, c.T('Next'), 0.12, 28, 'page.js', marks=[(1, c.T('revalidate'), YEL)])
    ts = c.T('stale')
    if c.on(ts):
        title(c, 'STALE-WHILE-REVALIDATE', 1000, ts, 64, hlcol=YEL)
        htmlcard(c, 60, 1080, 1020, ['Cache-Control: s-maxage=60, stale-while-revalidate'], c.T('HTTP'), 'header', 26)

def ondemand(c):
    title(c, 'ON-DEMAND', 340, c.T('demand'), 110, hlcol=YEL)
    a = node(c, 200, 620, 280, 200, 'admin panel', c.T('admin'), 'laptop', size=30)
    s = node(c, 820, 620, 280, 200, '/product/42', c.T('only'), 'doc', size=30)
    tr = c.T('revalidatePath')
    if c.on(tr):
        link(c, a, s, tr, txt_='revalidatePath')
        code(c, 60, 820, 1020, 820 + 72 + 3 * 54 + 30, ["'use server';", 'await savePrice(42, 1999);', "revalidatePath('/product/42');"], tr, 0.15, 30, 'action.js', marks=[(2, tr + 0.5, YEL)])
    to = c.T('only')
    if c.on(to): label(c, 540, 1220, 'only that page, right away', to, GRN, WHITE, 32)

def gotcha(c):
    trap(c)
    qtext(c, 'revalidate = 60. Does every user see the new price within 60 s?', 450, c.T('every'), 46)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 690, 'NO', 110, c.P(tn, 0.35), -6, RED)
    items = [(False, 'first visitor after expiry gets the OLD page', c.T('first')), (False, 'it only triggers the rebuild', c.T('triggers')),
             (False, 'no visitors → page stays stale forever', c.T('nobody'))]
    proscons(c, 80, 860, 1000, items, 34, 100)

SCENES = [
    (hook, "A store has a static page for every product. Then the price of one item changes. Do you rebuild all fifty thousand pages?"),
    (define, "Incremental static regeneration says: serve the static page, but give it an expiry. After, say, sixty seconds, the next visitor still gets the old page instantly, while the server rebuilds just that page in the background. Everyone after that gets the new one."),
    (analogy, "Think of a bakery shelf. The bread is baked ahead. When a batch gets old, the baker puts a fresh tray in the oven. But the customer doesn't wait. They take today's bread right now."),
    (how, "In Next dot js, it's one line. Export revalidate, in seconds. The pattern has a name: stale while revalidate. And the same idea exists as an HTTP cache header."),
    (ondemand, "Even better is on demand revalidation. When the price changes in your admin panel, call revalidatePath, and only that page is rebuilt, right away."),
    (gotcha, "Interview trap: with revalidate sixty, does every user see the new price within sixty seconds? No. The first visitor after the expiry still gets the old page. It only triggers the rebuild. And a page nobody visits stays stale forever."),
    (scene_next('S2 · E07', 'INTERVIEW QUESTIONS', 'CSR · SSR · SSG · ISR', 'interview', 'Four'),
     "Next: interview questions. Four rendering questions, with time to think. Comment NOTES for the cheat sheet."),
]
