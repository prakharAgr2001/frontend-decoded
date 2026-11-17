from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E09', tag='S4 · E09', short='SELECTORS')


def badge(c, cx, cy, n, at_flash=None):
    icon(c.pen, 'doc', cx, cy, 1.2)
    c.pen.circ(cx + 45, cy - 45, 32, fill=RED, outline=INK, w=4)
    c.pen.text(cx + 45, cy - 45, str(n), 'int', 30, WHITE)


def hook(c):
    darkcard(c.pen, 90, 360, 990, 700)
    c.pen.text(540, 410, 'store', 'int', 28, (150, 156, 166))
    fields = [('search', 'search: "bir"'), ('theme', "theme: 'dark'"), ('toast', 'toast: "Saved"'), ('cart', 'cart: 2 items')]
    for k, (kw, s_) in enumerate(fields):
        t = c.T(kw)
        c.pen.text(150 + (k % 2) * 420, 500 + (k // 2) * 110, s_, 'monob', 32, YEL if (c.on(t) and t <= c.t < t + 0.8) else (200, 205, 215), 'lm')
    b = node(c, 540, 950, 420, 200, '<CartBadge>', 0.2, sub='shows: 2', size=40)
    for kw in ('search', 'theme', 'toast'):
        t = c.T(kw)
        if c.on(t): flash_box(c, b, t + 0.2, RED, 0.8)
    tw = c.T('anything')
    if c.on(tw): label(c, 540, 1150, 're-renders on every store change', tw, (255, 210, 210), INK, 32)


def define(c):
    title(c, 'SELECTOR', 360, 0.1, 140, hlcol=YEL)
    a = node(c, 200, 600, 280, 140, 'state', c.T('goes'), fill=(220, 225, 235), sub='the whole store')
    f = node(c, 540, 600, 260, 140, 's => ...', c.T('picks'), fill=(255, 238, 170), size=34)
    b = node(c, 880, 600, 260, 140, '2', c.T('small'), fill=(200, 240, 200), size=60)
    link(c, a, f, c.T('goes')); link(c, f, b, c.T('small'))
    code(c, 40, 760, 1040, 940, ['const count = useSelector((s) => s.cart.items.length);'], c.T('picks') + 0.3, 0.1, 24, 'CartBadge.jsx', dy=0)
    to = c.T('only')
    if c.on(to): label(c, 540, 1040, 're-render only when that value changes', to, YEL, INK, 34)


def alerts(c):
    title(c, 'TEAM ALERTS ONLY', 330, 0.1, 100)
    p = phone_frame(c, 540, 820, 460, 760)
    x0, y0, x1, y1 = p
    tn = c.T('notifications')
    items = [('IND 190/4', 'your team', True), ('AUS 120/2', 'other match', False), ('ENG 88/1', 'other match', False)]
    for k, (s_, sub, mine) in enumerate(items):
        y = y0 + 80 + k * 140
        if not c.on(tn + k * 0.3): continue
        c.pen.rr(x0 + 20, y - 50, x1 - 20, y + 50, 16, fill=(255, 238, 170) if mine else (240, 238, 232), outline=INK if mine else GREY, w=3)
        c.pen.text(x0 + 46, y - 12, s_, 'int', 30, INK if mine else GREY, 'lm')
        c.pen.text(x0 + 46, y + 24, sub, 'intm', 22, MUTE, 'lm')
        if not mine and c.on(c.T('silent')): cross(c.pen, x1 - 60, y, 0.6, RED, 6, c.P(c.T('silent'), 0.3))


def how(c):
    title(c, 'HOW IT DECIDES', 330, 0.1, 100, hlcol=YEL)
    steps = [('after', 'after every dispatch'), ('runs', 'run the selector again'), ('compares', 'old === new ?')]
    for k, (kw, s_) in enumerate(steps):
        node(c, 540, 500 + k * 170, 640, 120, s_, c.T(kw), size=36)
        if k: arrow(c.pen, 540, 500 + k * 170 - 105, 540, 500 + k * 170 - 65, c.P(c.T(kw), 0.3), INK, 6, 18)
    ts = c.T('same')
    if c.on(ts): label(c, 300, 1050, 'same → skip render', ts, (200, 240, 200), INK, 32)
    td = c.T('different')
    if c.on(td): label(c, 780, 1050, 'different → render', td, (255, 225, 190), INK, 32)


def newarr(c):
    head(c, 'THE NEW-ARRAY TRAP', 'trap', size=76)
    code(c, 30, 450, 1050, 640, ['useSelector((s) => s.cart.items.filter((i) => i.veg));'], c.T('filter'), 0.1, 23, 'VegList.jsx',
         circles=[(0, c.T('brand'), '.filter(')])
    tf = c.T('fails')
    if c.on(tf): label(c, 540, 700, 'new array every time → === fails → always renders', tf, (255, 210, 210), INK, 28)
    code(c, 30, 780, 1050, 1060, ['const selectVeg = createSelector(', '  [(s) => s.cart.items],', '  (items) => items.filter((i) => i.veg));'],
         c.T('Memoize'), 0.15, 26, 'selectors.js', marks=[(0, c.T('Memoize') + 0.5, YEL)])
    ti = c.T('inputs')
    if c.on(ti): label(c, 540, 1140, 'same inputs → same array back', ti, (200, 240, 200), INK, 30)


def derived(c):
    title(c, 'DERIVED DATA LIVES HERE', 340, 0.1, 80, hlcol=YEL)
    for k, (kw, s_) in enumerate((('totals', 'selectTotal'), ('counts', 'selectCount'), ('filtered', 'selectVegItems'))):
        label(c, 540, 500 + k * 100, s_ + '(state)', c.T(kw), WHITE, INK, 34)
    tc = c.T('store')
    if c.on(tc):
        card(c.pen, 120, 830, 960, 1030, 24, WHITE, 10, 5)
        c.pen.text(540, 890, 'compute from the store', 'intx', 42, GRN)
        c.pen.text(540, 970, "don't store what you can compute", 'ints', 34, INK)
    chapter(c, 540, 1130, 'E01', 'two sources of truth', c.T('episode'))


def proof(c):
    title(c, 'HIGHLIGHT UPDATES', 330, 0.1, 96)
    for j, (lab, kw) in enumerate((('before', 'Before'), ('after', 'After'))):
        t = c.T(kw)
        if not c.on(t): continue
        x = 300 + j * 480
        b = node(c, x, 640, 380, 170, '<CartBadge>', t, size=34, sub=lab)
        if j == 0:
            for k in range(6): flash_box(c, b, t + 0.3 + k * 0.6, GRN, 0.5)
        else:
            ta = c.T('changes')
            if c.on(ta): flash_box(c, b, ta, GRN, 0.8)
    tk = c.T('keystroke')
    if c.on(tk): label(c, 300, 840, 'flashes on every keystroke', tk, (255, 210, 210), INK, 26)
    ta = c.T('changes')
    if c.on(ta): label(c, 780, 840, 'flashes when the count changes', ta, (200, 240, 200), INK, 26)
    ts = c.T('Settings')
    if c.on(ts): label(c, 540, 1020, 'React DevTools · Settings · Highlight updates', ts, YEL, INK, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Why does this re-render on every action?', c.T('action'), 'intx', 42, INK)
    code(c, 30, 540, 1050, 720, ['useSelector((s) => ({ a: s.a, b: s.b }));'], c.T('action') + 0.3, 0.1, 28, 'Widget.jsx', dy=0,
         circles=[(0, c.T('object'), '({ a: s.a, b: s.b })')])
    tt = c.T('two')
    if c.on(tt):
        code(c, 30, 820, 1050, 1100, ['const a = useSelector((s) => s.a);', 'const b = useSelector((s) => s.b);', '// or: useSelector(fn, shallowEqual)'],
             tt, 0.2, 26, 'Widget.jsx', marks=[(2, c.T('shallow'), YEL)])


SCENES = [
    (hook, "The cart badge shows one number. Yet it re-renders when the search text changes. When the theme changes. When a toast appears. When anything in the store changes."),
    (define, "The fix is a selector. A function that picks the piece of state a component needs. The whole state goes in, a small value comes out. And the component re-renders only when that value changes."),
    (alerts, "It's like cricket notifications for just your team. Every match is being played, but your phone stays silent until your team scores."),
    (how, "Here's how it decides. After every dispatch, the store runs your selector again, and compares the result with the last one. Same value: skip the render. Different: render."),
    (newarr, "Which creates a trap. A selector that calls filter returns a brand new array every time. The equality check always fails, so it always renders. Memoize it with create selector. Same inputs give back the same array."),
    (derived, "Selectors are also where derived data lives. Totals, counts, filtered lists. Compute them from the store, instead of storing them. That's episode one's rule, at app scale."),
    (proof, "See the difference. Before, with React DevTools highlight updates on, the badge flashes on every keystroke. After, it only flashes when the count changes. Find it under Settings."),
    (gotcha, "Interview question: why does this selector re-render on every action? It builds a new object each time, so equality fails. Use two selectors, or pass shallow equal."),
    (scene_next('S4 · E10', 'INTERVIEW QUESTIONS', 'Redux, stores and selectors', 'interview', 'selectors'),
     "Next: four interview questions on Redux, stores and selectors. Comment NOTES for the cheat sheet."),
]
