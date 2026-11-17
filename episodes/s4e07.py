from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E07', tag='S4 · E07', short='REDUX TOOLKIT')


def hook(c):
    files = [('actionTypes.js', 'types'), ('actions.js', 'creators'), ('reducer.js', 'switch'), ('store.js', 'spread')]
    for i, (fn, kw) in enumerate(files):
        t = c.T(kw)
        if not c.on(t - 0.01): continue
        c.sfx(t, 'pop'); s = c.B(t, 0.35)
        x = 230 + (i % 2) * 520 - 100; y = 590 + (i // 2) * 280
        card(c.pen, x - 40 * s + 60, y - 110 * s, x + 260 * s + 60, y + 110 * s, 20, WHITE, 10, 5)
        icon(c.pen, 'doc', x + 70 + 60, y - 20, 0.8 * s)
        c.pen.text(x + 110 + 60, y + 70, fn, 'monob', 28 * s, INK)
    tf = c.T('four')
    if c.on(tf): stamp(c.cv, 540, 360, '4 FILES · 1 FEATURE', 76, c.P(tf, 0.35), -3, RED); c.sfx(tf, 'thud')
    ts = c.T('spread')
    if c.on(ts):
        code(c, 40, 1050, 1040, 1250, ['return { ...s, cart: { ...s.cart, items: [...s.cart.items, x] } };'], ts, 0.1, 20, 'reducer.js', dy=0)


def what(c):
    title(c, 'REDUX TOOLKIT', 380, 0.1, 130, hlcol=YEL)
    txt(c, 540, 500, 'the official way to write Redux today', c.T('official'), 'ints', 40, INK)
    for k, (kw, s_) in enumerate((('store', 'same store'), ('actions', 'same actions'), ('flow', 'same one-way flow'))):
        label(c, 540, 650 + k * 100, s_, c.T(kw), WHITE, INK, 36)
    tl = c.T('Less')
    if c.on(tl): title(c, 'LESS TYPING', 1020, tl, 110, GRN)


def slice_(c):
    title(c, 'createSlice', 330, c.T('createSlice'), 100, hlcol=YEL)
    code(c, 30, 430, 1050, 1060, ['const cartSlice = createSlice({', "  name: 'cart',", '  initialState: { items: [] },', '  reducers: {',
                                  '    added(state, action) {', '      state.items.push(action.payload);', '    },', '  },', '});',
                                  'export const { added } = cartSlice.actions;'],
         c.T('createSlice') + 0.3, 0.1, 26, 'cartSlice.js', marks=[(9, c.T('generates'), YEL)])
    tg = c.T('generates')
    if c.on(tg): label(c, 540, 1130, "type 'cart/added' + creator added(item)", tg, (200, 240, 200), INK, 30)


def immer(c):
    head(c, 'WAIT, PUSH?', 'push', size=90)
    code(c, 40, 450, 1040, 620, ['state.items.push(action.payload);'], 0.2, 0.1, 30, 'cartSlice.js', marks=[(0, c.T('push'), YEL)], dy=0)
    td = c.T('draft')
    a = node(c, 250, 820, 330, 150, 'draft', td, sub='you mutate this', fill=(255, 238, 170))
    tp = c.T('produces')
    b = node(c, 830, 820, 330, 150, 'new state', tp, sub='immutable copy', fill=(200, 240, 200))
    tm = c.T('Immer')
    if c.on(tm):
        m = node(c, 540, 820, 170, 110, 'Immer', tm, fill=WHITE, size=34)
        link(c, a, m, tp - 0.2); link(c, m, b, tp)
    te = c.T('episode')
    if c.on(te): label(c, 540, 1050, 'how Immer works: E21', te, WHITE, INK, 30)


def store(c):
    title(c, 'configureStore', 330, c.T('configure'), 96, hlcol=YEL)
    code(c, 40, 430, 1040, 640, ['const store = configureStore({', '  reducer: { cart: cartSlice.reducer },', '});'], c.T('configure'), 0.12, 28, 'store.js', dy=0)
    rows(c, 90, 760, [(c.T('DevTools'), 'Redux DevTools wired up', None, 'ok'), (c.T('mutate'), 'warns on mutation outside reducers', None, 'ok'),
                      (c.T('serializable'), 'warns on non-serializable values', 'Dates · functions · class instances', 'ok')], 150, 900, 120, 36, 26)


def gears(c):
    title(c, 'MANUAL VS AUTOMATIC', 330, 0.1, 90)
    versus(c, ('CLASSIC', RED, c.T('manual'), [(c.T('every'), 'you shift every gear'), (c.T('stall'), 'easy to stall')]),
           ('TOOLKIT', GRN, c.T('automatic'), [(c.T('engine'), 'same engine'), (c.T('fewer'), 'fewer ways to stall')]), 430, 780, 40)
    tr = c.T('road')
    if c.on(tr): label(c, 540, 900, 'same Redux store underneath', tr, YEL, INK, 34)


def rtkq(c):
    title(c, 'RTK QUERY', 340, c.T('Query'), 120, hlcol=YEL)
    code(c, 40, 450, 1040, 760, ['const api = createApi({', '  endpoints: (b) => ({ menu: b.query({ query: () => \'/menu\' }) }),', '});',
                                 'const { data, isLoading } = useMenuQuery();'], c.T('Query') + 0.3, 0.15, 22, 'api.js', marks=[(3, c.T('loading'), YEL)])
    chapter(c, 540, 870, 'E02', 'server state needs a cache', c.T('episode'))
    tl = c.T('later')
    if c.on(tl): label(c, 540, 1000, 'caching, refetching, dedupe: E11 to E13', tl, WHITE, INK, 30)


def dead(c):
    trap(c, 'Interview')
    txt(c, 540, 470, '"Is Redux dead?"', c.T('dead'), 'intx', 56, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO', 600, tn, 110, GRN)
    rows(c, 90, 760, [(c.T('many'), 'big app · many writers of shared state', None, 'ok'), (c.T('logged'), 'every change logged and replayable', None, 'ok'),
                      (c.T('small'), 'small app or server data only', 'overkill', 'no')], 150, 900, 120, 36, 26)


SCENES = [
    (hook, "Classic Redux had a reputation. One feature meant four files. Action types, action creators, a big switch, and spread operators nested five levels deep."),
    (what, "Redux Toolkit is now the official way to write Redux. Same store. Same actions. Same one way flow. Less typing."),
    (slice_, "The heart of it is createSlice. You name the slice, give it initial state, and write reducers. It generates the action types and action creators for you."),
    (immer, "Wait. Push? Didn't we say never mutate? Inside createSlice, a library called Immer gives you a draft. You mutate the draft, and Immer produces a brand new state behind the scenes. Full episode on that later."),
    (store, "Then configure store builds the store. It wires up Redux DevTools, and adds development checks that warn if you mutate state outside a reducer, or put non serializable values like dates and functions in the store."),
    (gears, "Classic Redux is a manual car. You shift every gear yourself, and it's easy to stall. Toolkit is the automatic. Same engine, same road, fewer ways to stall."),
    (rtkq, "It also ships RTK Query, for server state. Define an endpoint, and you get data and loading flags, cached for you. Remember episode two: server data doesn't belong in hand written reducers. We'll go deep on this later."),
    (dead, "Interview question: is Redux dead? No. It shines when a big app has many places changing shared client state, and you want every change logged and replayable. For a small app, or for server data only, it's overkill."),
    (scene_next('S4 · E08', 'ZUSTAND · JOTAI · MOBX', 'three other ways to share state', 'Zustand', 'share'),
     "Next: Zustand, Jotai and MobX. Three other ways to share state. Comment NOTES for the cheat sheet."),
]
