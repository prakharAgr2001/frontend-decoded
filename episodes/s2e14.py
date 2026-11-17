from engine.s2_extra import *

EP = dict(id='S2E14', tag='S2 · E14', short='SERVER COMPONENTS')

def hook(c):
    p = panel(c, 50, 330, 1030, 1000, ('Network',), 0, (1 - c.P(0, 0.45)) * 900)
    tc = c.T('click')
    rows = ['getting-started?_rsc=1x8vq', 'installation?_rsc=1x8vq', 'project-structure?_rsc=1x8vq']
    for i, r in enumerate(rows):
        at = tc + 0.3 + i * 0.3
        if not c.on(at): continue
        c.sfx(at, 'tick'); y = 470 + i * 70
        c.pen.text(100, y, r, 'mono', 28, CYAN, 'lm'); c.pen.text(980, y, 'fetch', 'mono', 26, (150, 156, 166), 'rm')
    tr = c.T('ending')
    if c.on(tr): c.pen.rr(80, 435, 1000, 505, 10, outline=YEL, w=4)
    tn = c.T('HTML')
    if c.on(tn):
        chips(c, 140, 760, [('not HTML', RED), ('not JSON', RED)], tn, 0.5, 34)
    tw = c.T('what')
    if c.on(tw): stamp(c.cv, 540, 1150, 'SO WHAT IS IT?', 80, c.P(tw, 0.4), -4, RED)

def define(c):
    title(c, 'SERVER COMPONENTS', 340, c.T('Server'), 96, hlcol=YEL)
    txt(c, 540, 420, 'RSC = components that run only on the server', c.T('only'), 'ints', 34, MUTE)
    s = node(c, 260, 700, 300, 240, 'server', c.T('only'), 'server')
    d = node(c, 260, 1030, 240, 150, 'database', c.T('database'), 'db', size=28)
    if c.on(c.T('database')): link(c, s, d, c.T('database'))
    b = node(c, 820, 700, 300, 240, 'browser', c.T('output'), 'laptop')
    tc = c.T('code')
    if c.on(tc):
        c.pen.rr(140, 570, 380, 620, 10, fill=PINK, outline=INK, w=3); c.pen.text(260, 595, 'component code', 'int', 24, INK)
        cross(c.pen, 540, 640, 0.9, RED, 10, c.P(tc, 0.4)); c.pen.text(540, 720, 'never shipped', 'int', 26, RED)
    to = c.T('output')
    if c.on(to): packet(c, s, b, to, to + 1.0, YEL, 'rendered result', off=60)

def analogy(c):
    tk = c.T('kitchen')
    if c.on(tk):
        c.pen.text(540, 350, 'THE CLOUD KITCHEN', 'osw', 72, INK)
        card(c.pen, 90, 450, 500, 950, 22, DARK, 10, 5)
        c.pen.text(295, 500, 'kitchen', 'int', 30, WHITE)
        for k, s_ in enumerate(['stove', 'recipe', 'pantry']):
            at = c.T(['stove', 'recipe', 'stove'][k]) + (0.3 if k == 2 else 0)
            if c.on(at): pill(c.pen, 295, 600 + k * 110, s_, c.B(at, 0.3), WHITE, INK, 30)
    td = c.T('dish')
    if c.on(td):
        card(c.pen, 580, 450, 990, 950, 22, WHITE, 10, 5)
        c.pen.text(785, 500, 'your home', 'int', 30, INK)
        c.pen.circ(785, 720, 110 * c.B(td, 0.4), fill=(240, 200, 120), outline=INK, w=5)
        packet(c, (90, 650, 500, 750), (580, 650, 990, 750), td, td + 0.8, YEL, 'dish')
    if c.on(td + 0.5): label(c, 540, 1050, 'only the result travels', td + 0.5, YEL, INK, 32)

CODE = ['// ProductPage.jsx (server component)', "import db from './db';", "import AddToCart from './AddToCart'; // 'use client'", '',
        'export default async function ProductPage({ id }) {', '  const p = await db.product.find(id);',
        '  return <><h1>{p.name}</h1><AddToCart id={id} /></>;', '}']

def how(c):
    code(c, 20, 340, 1060, 340 + 72 + 8 * 50 + 40, CODE, c.T('async'), 0.1, 25, 'ProductPage.jsx',
         marks=[(4, c.T('async'), YEL), (5, c.T('database'), YEL), (2, c.T('Interactive'), YEL)])
    tu = c.T('Interactive')
    if c.on(tu):
        code(c, 140, 900, 940, 900 + 72 + 3 * 50 + 30, ["'use client';", 'export default function AddToCart({ id }) {', '  /* useState, onClick… */ }'], tu, 0.12, 26, 'AddToCart.jsx')
    ts = c.T('ship')
    if c.on(ts): label(c, 540, 1300, 'only client components ship JS', ts, GRN, WHITE, 30)

def payload(c):
    tp = c.T('payload')
    htmlcard(c, 30, 340, 1050, ['1:I["./AddToCart.js",["chunk-91"],"default"]', '0:["$","h1",null,{"children":"Headphones"}]',
                                 '2:["$","$L1",null,{"id":"42"}]'], tp, '?_rsc= response', 25,
             marks=[(1, c.T('description'), YEL), (2, c.T('placeholders'), YEL), (0, c.T('placeholders'), YEL)])
    tm = c.T('merges')
    if c.on(tm):
        fill_page(c, (300, 720, 780, 1180), 'full'); c.pen.rr(300, 720, 780, 1180, 8, outline=INK, w=4)
        label(c, 540, 1240, 'merged in · client state kept', tm, GRN, WHITE, 30)

def versus(c):
    title(c, 'NOT JUST SSR', 340, c.T('SSR'), 110, hlcol=YEL)
    rows = [('SSR', 'components → HTML for the first load', 'turns'), ('', 'then ALL of them hydrate', 'hydrate'),
            ('RSC', 'never hydrate · never ship code', 'never'), ('', 're-fetched on navigation', 'navigation')]
    for i, (a, b, kw) in enumerate(rows):
        at = c.T(kw); y = 500 + i * 120 + (60 if i >= 2 else 0)
        if not c.on(at - 0.01): continue
        if a: pill(c.pen, 170, y, a, c.B(at, 0.35), BLUE if a == 'SSR' else GRN, WHITE, 36)
        txt(c, 270, y, b, at, 'intx', 36, INK, 'lm', 'slide')
    tb = c.T('together')
    if c.on(tb): label(c, 540, 1130, 'Next.js App Router uses both, together', tb, YEL, INK, 30)

def gotcha(c):
    trap(c)
    qtext(c, 'Can a server component use useState or onClick?', 450, c.T('useState'), 48)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 650, 'NO', 110, c.P(tn, 0.35), -6, RED)
    to = c.T('once')
    if c.on(to): txt(c, 540, 800, 'it runs once, on the server — no browser to click in', to, 'ints', 34, INK)
    tp = c.T('Put')
    if c.on(tp):
        a = node(c, 270, 1040, 360, 180, 'server comp.', tp, 'server', sub='fetches data', size=32)
        b = node(c, 810, 1040, 360, 180, "'use client'", tp + 0.3, 'bolt', sub='state + handlers', size=32)
        link(c, a, b, c.T('props'), txt_='props')

SCENES = [
    (hook, "Open nextjs dot org with the Network panel, and click a link in the docs. You'll see requests ending in underscore R S C. They're not HTML, and they're not JSON. So what are they?"),
    (define, "React Server Components. Components that run only on the server. They can read your database directly, and their code is never shipped to the browser. Only their output is."),
    (analogy, "Think of a cloud kitchen. The stove, the recipe, the pantry, none of it comes to your house. Only the dish does."),
    (how, "Server components can be async, and query the database right inside the component. Interactive parts are client components, marked with use client. Only those ship JavaScript."),
    (payload, "That underscore R S C response is the RSC payload. A compact description of the rendered tree, with placeholders where client components go. React in the browser merges it into the page, without losing state."),
    (versus, "So isn't this just SSR? No. SSR turns components into HTML for the first load, and then all of them hydrate. Server components never hydrate, never ship code, and can be re-fetched on navigation. Modern frameworks use both together."),
    (gotcha, "Interview trap: can a server component use useState, or onClick? No. It runs once, on the server. There's no browser to click in. Put state and handlers in a client component, and pass it data as props."),
    (scene_next('S2 · E15', 'SERVER ACTIONS', 'a function call that is secretly a POST', 'actions', 'secretly'),
     "Next: server actions. A function call that's secretly a POST request. Comment NOTES for the cheat sheet."),
]
