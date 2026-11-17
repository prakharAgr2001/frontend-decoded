from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E08', tag='S4 · E08', short='ZUSTAND · JOTAI · MOBX')

COLS = {'Z': (255, 225, 190), 'J': (220, 205, 250), 'M': (200, 240, 200)}


def hook(c):
    title(c, 'NOT JUST REDUX', 340, 0.1, 100)
    for k, (nm, kw, sub, col) in enumerate((('Zustand', 'One', 'one store', 'Z'), ('Jotai', 'atoms', 'many atoms', 'J'), ('MobX', 'observable', 'observable objects', 'M'))):
        node(c, 540, 560 + k * 220, 700, 170, nm, c.T(kw), fill=COLS[col], sub=sub, size=56)


def zustand(c):
    title(c, 'ZUSTAND', 330, 0.1, 110, hlcol=COLS['Z'])
    txt(c, 540, 440, 'a tiny store with a hook', 0.4, 'ints', 38, MUTE)
    for k, (kw, s_) in enumerate((('provider', 'no Provider'), ('actions', 'no actions'), ('reducers', 'no reducers'))):
        label(c, 230 + k * 310, 540, s_, c.T(kw), WHITE, INK, 30)
    code(c, 30, 620, 1050, 960, ['const useCart = create((set) => ({', '  items: [],', '  add: (item) => set((s) => ({ items: [...s.items, item] })),',
                                 '}));', 'const count = useCart((s) => s.items.length);'], c.T('create'), 0.12, 22, 'cart.js', marks=[(4, c.T('slices'), YEL)])
    tb = c.T('board')
    if c.on(tb): label(c, 540, 1060, 'like one notice board: read only your section', tb, COLS['Z'], INK, 30)


def jotai(c):
    title(c, 'JOTAI', 330, 0.1, 110, hlcol=COLS['J'])
    txt(c, 540, 440, 'state built bottom-up from atoms', 0.4, 'ints', 38, MUTE)
    code(c, 30, 520, 1050, 760, ['const itemsAtom = atom([]);', 'const countAtom = atom((get) => get(itemsAtom).length);', 'const count = useAtomValue(countAtom);'],
         c.T('tiny'), 0.25, 24, 'atoms.js', marks=[(1, c.T('Derived'), YEL)])
    a = node(c, 250, 960, 280, 110, 'itemsAtom', c.T('tiny') + 0.5, fill=COLS['J'], size=30)
    b = node(c, 540, 960, 260, 110, 'countAtom', c.T('Derived'), fill=COLS['J'], size=30)
    d = node(c, 830, 960, 260, 110, '<Badge>', c.T('reads'), size=30)
    link(c, a, b, c.T('Derived')); link(c, b, d, c.T('reads'))
    ts = c.T('sticky')
    if c.on(ts): label(c, 540, 1110, 'like sticky notes: one fact per note', ts, COLS['J'], INK, 30)


def mobx(c):
    title(c, 'MOBX', 330, 0.1, 110, hlcol=COLS['M'])
    code(c, 30, 420, 1050, 840, ['class Cart {', '  items = [];', '  constructor() { makeAutoObservable(this); }', '  get count() { return this.items.length; }',
                                 '  add(item) { this.items.push(item); }', '}', 'const Badge = observer(() => <b>{cart.count}</b>);'],
         c.T('observable'), 0.1, 24, 'cart.js', marks=[(4, c.T('mutate'), YEL), (6, c.T('read'), YEL)])
    ts = c.T('spreadsheet')
    if c.on(ts):
        for r in range(2):
            for k in range(3):
                x = 300 + k * 240; y = 930 + r * 90
                v = ['A1: 249', 'B1: 199', 'C1: =A1+B1', '', '', ''][r * 3 + k]
                hot = (r == 0 and k == 2 and c.on(c.T('changes')))
                c.pen.rect(x - 115, y - 40, x + 115, y + 40, fill=YEL if hot else WHITE, outline=INK, w=3)
                if r == 0: c.pen.text(x, y, v if not (hot and k == 2) else 'C1: 448', 'monob', 26, INK)
        label(c, 540, 1160, 'like a spreadsheet: cells update themselves', ts, COLS['M'], INK, 30)


def table(c):
    title(c, 'PICK BY MENTAL MODEL', 330, 0.1, 86)
    hdr = ['', 'model', 'code', 'feels like']
    data = [('Redux', 'actions → reducer', 'more', 'strict, logged'), ('Zustand', 'one store + hook', 'little', 'simple'),
            ('Jotai', 'atoms', 'little', 'useState, shared'), ('MobX', 'observables', 'little', 'just mutate')]
    xs = [110, 330, 600, 760]
    for k, h in enumerate(hdr): c.pen.text(xs[k], 450, h, 'int', 28, MUTE, 'lm')
    for i, row in enumerate(data):
        t = c.T(['Redux', 'Zustand', 'Jotai', 'MobX'][i])
        if not c.on(t): continue
        y = 540 + i * 120; c.sfx(t, 'pop'); p = c.P(t, 0.3)
        card(c.pen, 80, y - 48, 1000, y + 48, 16, WHITE, 6, 3)
        for k, v in enumerate(row):
            c.pen.text(xs[k] + (1 - p) * 20, y, v, 'intx' if k == 0 else 'ints', 30 if k == 0 else 26, INK, 'lm')
    tt = c.T('team')
    if c.on(tt): label(c, 540, 1080, 'all of them are fine · pick what your team reads easily', tt, YEL, INK, 28)


def ssr(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'A module-level store on the server?', c.T('singleton'), 'intx', 44, INK)
    srv = node(c, 540, 700, 360, 160, 'server', c.T('rendering'), ic='server', sub='one module, every request')
    u1 = node(c, 220, 980, 280, 130, 'user A', c.T('request'), ic='phone', size=28)
    u2 = node(c, 860, 980, 280, 130, 'user B', c.T('request') + 0.2, ic='phone', size=28)
    link(c, srv, u1, c.T('request')); link(c, srv, u2, c.T('request') + 0.2)
    tl = c.T('leak')
    if c.on(tl): packet(c, srv, u2, tl, tl + 1.0, RED, "A's cart")
    tp = c.T('per')
    if c.on(tp): label(c, 540, 1170, 'fix: create a store per request, pass it via context', tp, (200, 240, 200), INK, 28)


SCENES = [
    (hook, "Redux isn't the only way to share state. Three popular libraries take very different approaches. One store. Many atoms. Or observable objects."),
    (zustand, "Zustand is a tiny store with a hook. No provider, no actions, no reducers. You call create, put state and functions in one object, and read just the slices you need. Like one notice board, where you only read your own section."),
    (jotai, "Jotai builds state from the bottom up. Each piece is a tiny atom. Derived atoms combine them. And a component re-renders only when an atom it reads changes. Like sticky notes, one fact per note."),
    (mobx, "MobX makes objects observable. You mutate them directly, and any component that read a field re-renders by itself. Like a spreadsheet: change one cell, and every formula that uses it changes too."),
    (table, "So pick by mental model. Redux: strict actions, everything logged. Zustand: one simple store. Jotai: feels like use state, but shared. MobX: just mutate. All of them work. Pick what your team reads easily."),
    (ssr, "Interview trap: a Zustand store is a module level singleton. In the browser, that's fine. But during server rendering, one module serves every request. One user's cart can leak into another user's page. On the server, create a store per request, and pass it down with context."),
    (scene_next('S4 · E09', 'SELECTORS', 'subscribe to just the slice you need', 'selectors', 'slice'),
     "Next: selectors, and how to subscribe to just the slice you need. Comment NOTES for the cheat sheet."),
]
