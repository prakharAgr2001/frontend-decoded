from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E01', tag='S4 · E01', short='WHAT IS STATE')


def hook(c):
    ta = c.T('Add')
    q = [1 if c.on(ta + 0.4) else 0, 0, 0]
    foodphone(c, 540, 800, q, tap=(0, ta + 0.2), url='swiggy.com')
    for kw, (x, y, s_) in (('counter', (880, 470, '1. button')), ('cart', (760, 1290, '2. cart bar')), ('two', (330, 1290, '3. total'))):
        t = c.T(kw)
        if c.on(t): label(c, x, y, s_, t, YEL, INK, 28)
    tw = c.T('Who')
    if c.on(tw): stamp(c.cv, 540, 330, 'WHO TOLD THEM?', 76, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')


def define(c):
    title(c, 'STATE', 400, 0.1, 190, hlcol=YEL)
    card(c.pen, 110, 560, 970, 820, 26, WHITE, 12, 5)
    txt(c, 540, 640, 'data your UI remembers right now', c.T('remembers'), 'intx', 44, INK)
    txt(c, 540, 730, '…that can change while the page is open', c.T('change'), 'ints', 36, MUTE)
    tr = c.T('rule')
    if c.on(tr):
        rows(c, 110, 960, [(c.T('changes'), 'it changes', None, 'ok'), (c.T('show'), 'the screen must show it', None, 'ok')], 140, 860, 110, 40)
    ti = c.T("it's")
    if c.on(ti): label(c, 540, 1240, 'then it is state', ti, YEL, INK, 36)


def formula(c):
    title(c, 'UI = f(state)', 380, c.T('equals'), 140, hlcol=YEL)
    a = objcard(c, 60, 560, 480, ['{ qty: 1 }'], c.T('change') - 0.2, fname='state', size=34)
    b = node(c, 760, 640, 360, 150, 'render()', c.T('redrawn'), sub='React calls your function', fill=(255, 238, 170))
    link(c, (60, 560, 480, 720), b, c.T('redrawn') + 0.2)
    tn = c.T("don't")
    if c.on(tn):
        cross(c.pen, 300, 960, 1.6, RED, 12, c.P(tn, 0.4))
        txt(c, 560, 960, 'edit the screen', tn, 'intx', 46, INK, 'lm')
    tc = c.T('change')
    if c.on(tc):
        check(c.pen, 300, 1100, 1.6, GRN, 12, c.P(tc, 0.4))
        txt(c, 560, 1100, 'change the state', tc, 'intx', 46, INK, 'lm')


def score(c):
    title(c, 'THE SCOREBOARD', 330, 0.1, 100)
    tb = c.T('board')
    darkcard(c.pen, 140, 450, 940, 800)
    c.pen.text(540, 520, 'INDIA', 'osw', 54, WHITE)
    tu = c.T('update')
    runs = 186 if not c.on(tu + 0.3) else 190
    c.pen.text(540, 650, f'{runs}/4', 'osw', 130 * (c.B(tu + 0.3, 0.3) if c.on(tu + 0.3) and c.t < tu + 0.8 else 1), YEL)
    c.pen.text(540, 750, '18.2 overs', 'int', 32, (180, 186, 196))
    # scorer's book
    card(c.pen, 220, 900, 860, 1120, 20, (255, 250, 235), 8, 4)
    c.pen.text(260, 950, "scorer's book", 'intx', 32, INK, 'lm')
    c.pen.text(260, 1020, f'runs = {runs}', 'monob', 40, RED if c.on(tu + 0.3) else INK, 'lm')
    if c.on(tu): flash_box(c, (220, 900, 860, 1120), tu)
    tr = c.T('UI')
    if c.on(tr): label(c, 540, 860, 'board = UI', tr, YEL, INK, 30)
    ts = c.T('book', 2)
    if c.on(ts): label(c, 540, 1190, 'book = state', ts, YEL, INK, 30)


def manual(c):
    head(c, 'BEFORE: BY HAND', 'Before', size=76)
    code(c, 40, 450, 1040, 820, ["$('#badge').text(count);", "$('#btn').replaceWith(stepper);", "$('#total').text(sum);", '// ...one more place?'],
         c.T('find') - 0.3, 0.5, 30, 'cart.js')
    tm = c.T('Miss')
    if c.on(tm):
        card(c.pen, 140, 900, 940, 1160, 24, WHITE, 10, 5)
        c.pen.text(540, 970, 'Cart: 2 items', 'intx', 46, INK)
        c.pen.text(540, 1060, 'Bill: ₹249 (1 item)', 'intx', 46, RED)
        verdict(c, 900, 920, False, c.T('disagree'), 1.6)


def hookcode(c):
    title(c, 'useState', 340, c.T('use'), 110, hlcol=YEL)
    code(c, 30, 450, 1050, 870, ['function AddButton() {', '  const [qty, setQty] = useState(0);', '  if (qty === 0)',
                                 '    return <Add onClick={() => setQty(1)} />;', '  return <Stepper qty={qty} />;', '}'],
         c.T('lives'), 0.12, 26, 'AddButton.jsx', marks=[(1, c.T('lives') + 0.8, YEL), (3, c.T('Calling'), YEL)])
    tc = c.T('again')
    if c.on(tc):
        a = node(c, 250, 1060, 330, 120, 'setQty(1)', c.T('Calling'), fill=(255, 238, 170))
        b = node(c, 790, 1060, 330, 120, 'render again', tc, fill=(200, 240, 200))
        link(c, a, b, tc)
    td = c.T('different')
    if c.on(td): label(c, 540, 1220, 'only what changed hits the DOM', td, WHITE, INK, 30)


def derived(c):
    trap(c, 'Interview')
    txt(c, 540, 470, 'Should the cart total be state?', c.T('total'), 'intx', 46, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO', 590, tn, 110, RED)
    code(c, 40, 690, 1040, 900, ['const [total, setTotal] = useState(0); // 2nd copy'], c.T('Storing'), 0.1, 24, 'bad.jsx', marks=[(0, c.T('sources'), YEL)])
    code(c, 40, 950, 1040, 1160, ['const total = items.reduce((s, i) => s + i.price, 0);'], c.T('calculate'), 0.1, 23, 'good.jsx')
    tc = c.T('calculate')
    if c.on(tc + 0.6): verdict(c, 960, 1000, True, tc + 0.6, 1.2)
    td = c.T('disagree')
    if c.on(td): label(c, 540, 1240, 'two sources of truth will drift', td, (255, 210, 210), INK, 32)


def proof(c):
    panel(c, 50, 330, 1030, 1160, tabs=('Components', 'Profiler'), dy=(1 - c.P(0, 0.45)) * 900)
    ts = c.T('select')
    if c.on(ts):
        tree_ = [('App', 0), ('Menu', 1), ('MenuItem', 2), ('AddButton', 3)]
        for k, (nm, d) in enumerate(tree_):
            y = 490 + k * 60
            if k == 3: c.pen.rect(70, y - 26, 1010, y + 26, fill=(50, 70, 110))
            c.pen.text(110 + d * 40, y, f'<{nm}>', 'mono', 28, CYAN if k < 3 else WHITE, 'lm')
    th = c.T('hooks')
    if c.on(th):
        c.pen.line([(70, 760), (1010, 760)], (60, 66, 76), 2, False)
        c.pen.text(110, 810, 'hooks', 'int', 28, (150, 156, 166), 'lm')
        tt = c.T('Tap')
        v = '1' if c.on(tt + 0.6) else '0'
        c.pen.text(110, 880, '1  State:', 'mono', 32, (200, 205, 215), 'lm')
        c.pen.text(400, 880, v, 'monob', 40 * (c.B(tt + 0.6, 0.3) if c.on(tt + 0.6) else 1), NU, 'lm')
        if c.on(tt + 0.6): flash_box(c, (90, 845, 520, 915), tt + 0.6)
    tw = c.T('watch')
    if c.on(tw): label(c, 540, 1060, 'any React app · React DevTools extension', tw, YEL, INK, 28)


SCENES = [
    (hook, "You tap Add on a biryani in Swiggy. Three things change at once. The button becomes a counter, a cart bar slides up, and the total says two forty nine. Who told all three?"),
    (define, "That's state. The data your UI remembers right now, that can change while the page is open. A simple rule: if it changes, and the screen must show it, it's state."),
    (formula, "React's big idea fits in one line. UI equals a function of state. You don't edit the screen. You change the state, and the screen is redrawn from it."),
    (score, "Think of a cricket scoreboard. Nobody repaints the board for every ball. The scorer updates one number in the book, and the board shows it. The board is the UI. The scorer's book is the state."),
    (manual, "Before this, you updated the page by hand. Find the badge, change its text. Find the button, swap it. Find the total, recalculate. Miss one place, and the cart says two items while the bill says one. They disagree."),
    (hookcode, "In React, component state lives in use state. Calling set qty doesn't touch the screen. It asks React to call your component again with the new value, and update only what's different."),
    (derived, "Interview trap. Should the cart total be its own state? No. Storing it separately creates two sources of truth, and one day they disagree. If you can calculate it from other state, calculate it."),
    (proof, "See it yourself. In React DevTools, select a component, and the hooks panel shows its state live. Tap Add, and watch the value change. Works on any React app."),
    (scene_next('S4 · E02', 'THE 5 TYPES OF STATE', 'and why mixing them up hurts', 'five', 'mixing'),
     "Next: the five types of state, and why mixing them up causes most bugs. Comment NOTES for the cheat sheet."),
]
