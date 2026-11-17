from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E03', tag='S5 · E03', short='REST vs GRAPHQL vs tRPC', cap={'tRPC': 'tRPC'})


def hook(c):
    title(c, 'THREE TEAMS', 340, 0.1, 100)
    for k, (kw, ic, nm, sub) in enumerate((('public', 'globe', 'Public API', 'thousands of devs'), ('mobile', 'phone', 'Mobile app', 'dozens of screens'),
                                           ('TypeScript', 'laptop', 'Two devs', 'one TS repo'))):
        node(c, 540, 540 + k * 230, 620, 190, nm, c.T(kw), ic, sub=sub)
    ts = c.T('same')
    if c.on(ts): stamp(c.cv, 540, 1250, 'NOT THE SAME CHOICE', 64, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')


CODE = ['// server', 'export const router = t.router({', '  getUser: t.procedure', '    .input(z.string())',
        '    .query(({ input }) => db.user.find(input)),', '});', '// client', "const user = await trpc.getUser.query('42');"]


def trpc(c):
    title(c, 'tRPC', 340, c.T('tRPC'), 120, hlcol=YEL)
    code(c, 30, 430, 1050, 430 + 72 + len(CODE) * 48 + 20, CODE, c.T('call') - 0.3, 0.1, 25, 'api.ts',
         marks=[(2, c.T('functions'), YEL), (7, c.T('local'), YEL)])
    ts = c.T('schema')
    if c.on(ts): label(c, 300, 1080, 'no schema to write', ts, WHITE, INK, 30)
    tt = c.T('types')
    if c.on(tt): label(c, 760, 1080, 'types flow across', tt, YEL, INK, 30)


def order(c):
    title(c, 'THREE WAYS TO ORDER', 340, 0.1, 80)
    items = (('menu', 'REST', 'fixed numbered menu', 'anyone can order'), ('form', 'GraphQL', 'order form', 'tick exactly what you want'),
             ('sibling', 'tRPC', 'shout to your sibling', 'fast, but only at home'))
    for k, (kw, nm, a, b) in enumerate(items):
        t = c.T(kw); y = 520 + k * 220
        if not c.on(t): continue
        s = c.B(t, 0.4); c.sfx(t, 'pop')
        card(c.pen, 90, y - 85 * s, 990, y + 85 * s, 22, WHITE, 10, 5)
        c.pen.rr(110, y - 60 * s, 330, y + 60 * s, 18, fill=YEL, outline=INK, w=4)
        c.pen.text(220, y, nm, 'intx', 38 * s, INK)
        c.pen.text(360, y - 22, a, 'intx', 36 * s, INK, 'lm')
        c.pen.text(360, y + 26, b, 'intm', 28 * s, MUTE, 'lm')
    th = c.T('house')
    if c.on(th): label(c, 540, 1230, 'same house only = same repo, same language', th, (255, 220, 220), INK, 28)


def table(c):
    ts = c.T('side')
    grid(c, 60, 380, [330, 200, 230, 200], [
        (ts, ['', 'REST', 'GraphQL', 'tRPC']),
        (c.T('clients'), ['Many clients', 'ok', 'ok', 'no']),
        (c.T('fields'), ['Fields per screen', 'no', 'ok', 'no']),
        (c.T('types'), ['End-to-end types', 'codegen', 'codegen', 'ok']),
        (c.T('Simplest'), ['Simple to start', 'ok', 'no', 'ok'])], rowh=120, size=32)


def real(c):
    title(c, 'IN THE WILD', 340, 0.1, 100)
    rows(c, 100, 520, [(c.T('GitHub'), 'GitHub', 'public REST and GraphQL APIs', BLUE),
                       (c.T('Shopify'), 'Shopify', 'Storefront API is GraphQL', GRN),
                       (c.T('T3'), 'T3-style apps', 'tRPC inside full-stack TypeScript', PURPLE)], gap=190, h=150)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tf = c.T('faster')
    if c.on(tf): txt(c, 540, 470, 'Is GraphQL faster than REST?', tf, 'intx', 50, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 600, 'NO', 110, c.P(tn, 0.35), -5, RED); c.sfx(tn, 'thud')
    tl = c.T('language')
    if c.on(tl): txt(c, 540, 730, 'a query language, not a speed boost', tl, 'ints', 36, INK)
    rows(c, 100, 860, [(c.T('round'), 'fewer round trips', None, 'ok'), (c.T('slower'), 'careless query = slow server', None, 'no'),
                       (c.T('lose'), 'lose easy HTTP caching', None, 'no')], gap=120, h=96, size=34)
    tc = c.T('clients')
    if c.on(tc): label(c, 540, 1240, 'choose by clients + teams', tc, YEL, INK, 32)


SCENES = [
    (hook, "Three teams. One builds a public API for thousands of developers. One builds a mobile app with dozens of screens. And one is two developers, with one TypeScript repo. They should not make the same choice."),
    (trpc, "Meet tRPC. If your frontend and backend are both TypeScript, in one repo, you can call server functions like local functions. There's no schema to write. The types flow straight across."),
    (order, "Think of three ways to order food. REST is a fixed menu: numbered dishes, anyone can order. GraphQL is the order form: tick exactly what you want. tRPC is shouting to your sibling in the next room. Fast and easy, but it only works inside the same house."),
    (table, "Put them side by side. Many different clients? REST or GraphQL. Each screen picking its own fields? GraphQL. End to end types, with zero codegen? tRPC. Simplest to start? REST and tRPC."),
    (real, "In the wild: GitHub offers public REST and GraphQL APIs. Shopify's storefront API is GraphQL. And tRPC shows up inside full stack TypeScript apps, like the T3 stack."),
    (gotcha, "Interview trap. Is GraphQL faster than REST? No. It's a query language, not a speed boost. It can save round trips, but a careless query can make the server slower, and you lose easy HTTP caching. Choose by your clients and teams."),
    (scene_next('S5 · E04', 'BACKEND FOR FRONTEND', 'one API layer per client', 'backend', 'layer'),
     "Next: the backend for frontend, an API layer built for one client. Comment NOTES for the cheat sheet."),
]
