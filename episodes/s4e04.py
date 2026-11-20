from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E04', tag='S4 · E04', short='THE CONTEXT TRAP', hook='one Provider, everything renders')

FLASH = (255, 210, 210)


def consumers(c, at, flash=None, only=None, y0=700, names=('Header', 'Footer', 'ItemList', 'CouponBox')):
    boxes = []
    for i, nm in enumerate(names):
        x = 160 + (i % 2) * 540 + 110; y = y0 + (i // 2) * 200
        b = node(c, x, y, 420, 130, f'<{nm}>', at + i * 0.12, size=32, sub='useContext(AppCtx)')
        boxes.append(b)
        if flash is not None and (only is None or i in only):
            ph = int(max(0, c.t - flash) / 0.8)
            flash_box(c, b, flash + ph * 0.8, RED, 0.7)
    return boxes


def hook(c):
    objcard(c, 140, 330, 940, ['value = { user, theme, cart, coupon }'], 0.1, 'AppCtx.Provider', 28, dy=0)
    tt = c.T('typing')
    consumers(c, 0.4, flash=c.T('header') if c.on(c.T('header')) else None)
    if c.on(tt): label(c, 790, 1140, 'typing "SAVE20"', tt, YEL, INK, 30)
    tn = c.T('None')
    if c.on(tn): stamp(c.cv, 540, 1280, 'ONLY ONE USES IT', 70, c.P(tn, 0.35), -3, RED); c.sfx(tn, 'thud')


def how(c):
    title(c, 'CONTEXT', 340, 0.1, 120, hlcol=YEL)
    nodes = [('p', '<Provider>', 540, 500, None, c.T('read')), ('a', '<Layout>', 540, 650, 'p', c.T('props')), ('b', '<Page>', 540, 800, 'a', c.T('props') + 0.2),
             ('d', '<Price>', 540, 950, 'b', c.T('props') + 0.4)]
    tree(c, nodes, 0, 0.1, lambda k: (255, 238, 170) if k in 'pd' else WHITE, 32)
    tp = c.T('props')
    if c.on(tp):
        q = c.P(tp + 0.5, 0.6)
        c.pen.line([(760, 500), (820, 500), (820, 500 + 450 * q), (760, 500 + 450 * q)], RED, 6)
        label(c, 900, 720, 'skips the middle', tp + 0.6, WHITE, INK, 26)
    ts = c.T('subscribes')
    if c.on(ts):
        card(c.pen, 120, 1080, 960, 1240, 24, WHITE, 10, 5)
        c.pen.text(540, 1130, 'useContext subscribes to', 'ints', 34, INK)
        c.pen.text(540, 1190, 'the WHOLE value', 'intx', 46, RED)


def pa(c):
    title(c, 'THE BUILDING PA', 330, 0.1, 100)
    for f in range(4):
        y = 1100 - f * 170
        card(c.pen, 280, y - 70, 800, y + 70, 12, WHITE, 6, 4)
        for k in range(3):
            x = 360 + k * 180
            c.pen.rect(x - 40, y - 35, x + 40, y + 35, fill=(210, 225, 245), outline=INK, w=3)
            ta = c.T('every')
            if c.on(ta):
                ph = (c.t - ta) % 1.2
                if ph < 0.5: c.pen.circ(x, y, 14 + 40 * ph, outline=RED, w=4)
    ta = c.T('announcement')
    if c.on(ta):
        icon(c.pen, 'tower', 900, 470, 1.0)
        label(c, 900, 570, '"water off at 3pm"', ta, YEL, INK, 26)
    tf = c.T('fourth')
    if c.on(tf): label(c, 540, 1240, 'only the fourth floor needed it', tf, FLASH, INK, 30)


def newobj(c):
    head(c, 'TRAP 1: NEW OBJECT', 'trap', size=76)
    code(c, 30, 440, 1050, 700, ['<AppCtx.Provider value={{ user, cart }}>', '// a brand-new object on every render'],
         c.T('render') - 0.4, 0.15, 26, 'App.jsx', circles=[(0, c.T('new'), '{{ user, cart }}')])
    tf = c.T('consumer')
    if c.on(tf): label(c, 540, 770, 'App re-renders → every consumer re-renders', tf, FLASH, INK, 30)
    code(c, 30, 860, 1050, 1140, ['const value = useMemo(() => ({ user, cart }),', '                      [user, cart]);'],
         c.T('Memoize'), 0.15, 26, 'App.jsx', marks=[(0, c.T('Memoize') + 0.4, YEL)])


def split(c):
    head(c, 'TRAP 2: ONE BIG CONTEXT', 'trap', size=70)
    objcard(c, 140, 450, 940, ['AppCtx = { user, theme, cart, coupon }'], c.T('field') - 0.3, 'before', 26, dy=0)
    tf = c.T('field')
    if c.on(tf): label(c, 540, 650, 'any field changes → all consumers', tf, FLASH, INK, 30)
    ts = c.T('Split')
    for k, (nm, col) in enumerate((('UserCtx', BLUE), ('ThemeCtx', PURPLE), ('CartCtx', ORANGE))):
        node(c, 220 + k * 320, 820, 280, 120, nm, ts + 0.2 + k * 0.2, fill=mix(WHITE, col, 0.3), size=34)
    td = c.T('dispatch')
    if c.on(td):
        card(c.pen, 120, 960, 960, 1160, 24, WHITE, 10, 5)
        c.pen.text(540, 1020, 'and split state from its setters', 'ints', 34, INK)
        c.pen.text(540, 1090, 'CartStateCtx · CartDispatchCtx', 'monob', 32, INK)


def memotrap(c):
    trap(c, 'Interview')
    txt(c, 540, 470, 'Does React.memo stop context re-renders?', c.T('memo'), 'intx', 42, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO', 600, tn, 120, RED)
    tp = c.T('props')
    a = node(c, 300, 820, 380, 150, 'React.memo', tp, sub='checks props')
    b = node(c, 780, 820, 340, 150, 'context', c.T('straight'), fill=FLASH, sub='goes straight through')
    if c.on(c.T('straight')):
        q = c.P(c.T('straight'), 0.6)
        arrow(c.pen, 780, 900, 780, 900 + 200 * q, 1, RED, 8, 24)
    chapter(c, 540, 1190, 'S3 · E28', 'memo myths', c.T('memo', 3))


def store(c):
    title(c, 'DELIVERY, NOT STORAGE', 340, c.T('delivery'), 80, hlcol=YEL)
    rows(c, 90, 520, [(c.T('rarely'), 'context: values that rarely change', 'theme · user · locale', 'ok'),
                      (c.T('often'), 'hot state: a store with selectors', 'cart · inputs · live data', BLUE)], 170, 900, 140, 38, 28)
    code(c, 30, 860, 1050, 1080, ['const count = useCart(s => s.items.length);', '// re-renders only when the count changes'],
         c.T('slice'), 0.15, 26, 'CartBadge.jsx', marks=[(0, c.T('slice') + 0.5, YEL)])
    tn = c.T('episodes')
    if c.on(tn): label(c, 540, 1180, 'stores + selectors: E08, E09', tn, WHITE, INK, 30)


def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Components', 'Profiler'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('Record')
    if c.on(tr):
        for k, (nm, w, col) in enumerate((('App', 0.95, GRN), ('Header', 0.4, YEL), ('Footer', 0.3, YEL), ('ItemList', 0.8, ORANGE), ('CouponBox', 0.25, YEL))):
            y = 470 + k * 74; c.pen.rect(100, y, 100 + 860 * w * c.P(tr + k * 0.12, 0.3), y + 58, fill=col)
            c.pen.text(120, y + 29, nm, 'int', 26, INK, 'lm')
    tw = c.T('Why')
    if c.on(tw):
        card(c.pen, 160, 900, 920, 1080, 14, WHITE, 6, 3)
        c.pen.text(200, 950, 'Why did this render?', 'intx', 30, INK, 'lm')
        c.pen.text(200, 1020, 'Context changed', 'mono', 30, RED, 'lm')


SCENES = [
    (hook, "One app context holds the user, the theme, the cart, and a coupon code. You start typing a coupon, and the header, the footer, and the whole item list re-render. None of them use the coupon."),
    (how, "Context lets a deep component read a value without passing props through every level. But any component that calls use context subscribes to the whole value."),
    (pa, "It's like the PA system in an apartment building. One announcement about the water on the fourth floor, and every flat hears it. Most of them didn't need to."),
    (newobj, "The first trap is hiding in plain sight. Passing an object literal as the value creates a new object on every render. So whenever App renders, every consumer renders too. Memoize the value."),
    (split, "The second trap is one big context. When any field changes, every consumer re-renders. Split it by concern: user, theme, cart. And split the state from its dispatch, so buttons that only update never re-render."),
    (memotrap, "Interview trap: does wrapping a consumer in React memo stop context re-renders? No. Memo only checks props. A context change goes straight through to every component that reads it. That's from season three's memo episode."),
    (store, "Context is a delivery mechanism, not a state manager. It's great for values that rarely change. For state that changes often, use a store where each component subscribes to just one slice. More in the next episodes."),
    (proof, "See it yourself. Record in the React Profiler, click a component, and it tells you why it rendered. Context changed."),
    (scene_next('S4 · E05', 'INTERVIEW QUESTIONS', 'state basics · 4 questions', 'interview', 'basics'),
     "Next: four interview questions on state basics. Comment NOTES for the cheat sheet."),
]
