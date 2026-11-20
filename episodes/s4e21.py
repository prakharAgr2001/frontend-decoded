from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E21', tag='S4 · E21', short='IMMER', hook='mutate without mutating')


def hook(c):
    title(c, 'CHANGE ONE CITY', 330, 0.1, 100)
    code(c, 30, 430, 1050, 830, ['setState({', '  ...state,', '  user: {', '    ...state.user,', '    address: {', "      ...state.user.address, city: 'Pune',",
                                 '    },', '  },', '});'], c.T('write'), 0.15, 24, 'update.js', marks=[(5, c.T('field'), YEL)])
    tt = c.T('typo')
    if c.on(tt): label(c, 540, 930, 'forget one ...spread → half the object silently gone', tt, (255, 210, 210), INK, 28)


def why(c):
    title(c, 'WHY NOT JUST MUTATE?', 330, 0.1, 90)
    a = node(c, 260, 600, 340, 160, 'old state', c.T('compares'), ic='doc')
    b = node(c, 820, 600, 340, 160, 'new state', c.T('compares') + 0.3, ic='doc')
    tm = c.T('mutate')
    if c.on(tm):
        txt(c, 540, 820, 'mutate → same object', tm, 'intx', 44, INK)
        txt(c, 540, 890, 'Object.is(old, new) → true', tm + 0.5, 'monob', 36, RED)
    tn = c.T('nothing')
    if c.on(tn): label(c, 540, 1010, 'React sees nothing changed → no re-render', tn, (255, 210, 210), INK, 30)


def sharing(c):
    title(c, 'STRUCTURAL SHARING', 330, 0.1, 90, hlcol=YEL)
    tn = c.T('new')
    nodes = [('r', 'state', 540, 480, None, 0.2), ('u', 'user', 320, 640, 'r', 0.4), ('i', 'items', 760, 640, 'r', 0.5),
             ('a', 'address', 200, 800, 'u', 0.6), ('p', 'prefs', 440, 800, 'u', 0.7), ('c', "city: 'Pune'", 200, 960, 'a', 0.8)]
    hot = set('ruac') if c.on(tn) else set()
    tree(c, nodes, 0, 0.1, lambda k: (255, 238, 170) if k in hot else WHITE, 30)
    ts = c.T('reused')
    if c.on(ts):
        for (x, y) in ((440, 800), (760, 640)): check(c.pen, x + 90, y - 30, 0.6, GRN, 6, c.P(ts, 0.3))
        label(c, 760, 1050, 'unchanged branches: reused', ts, (200, 240, 200), INK, 28)
    if c.on(tn): label(c, 300, 1150, 'changed path: new objects', tn, YEL, INK, 28)


def suggest(c):
    title(c, 'SUGGESTING MODE', 330, 0.1, 100)
    card(c.pen, 120, 440, 960, 900, 20, WHITE, 10, 5)
    c.pen.text(170, 520, 'Delivery address', 'intx', 36, INK, 'lm')
    tsc = c.T('scribble')
    c.pen.text(170, 610, 'City: Mumbai', 'ints', 34, GREY if c.on(tsc) else INK, 'lm')
    if c.on(tsc):
        c.pen.line([(260, 610), (170 + c.pen.tw('City: Mumbai', 'ints', 34), 610)], RED, 4)
        txt(c, 420, 610, 'Pune', tsc + 0.3, 'intx', 36, GRN, 'lm')
    tc = c.T('clean')
    if c.on(tc):
        a = node(c, 290, 1080, 300, 130, 'original', tc, ic='doc', sub='untouched', size=28)
        b = node(c, 790, 1080, 300, 130, 'new version', tc + 0.3, ic='doc', sub='City: Pune', size=28, fill=(200, 240, 200))


def produce_(c):
    title(c, 'produce()', 330, c.T('produce'), 120, hlcol=YEL)
    code(c, 30, 440, 1050, 700, ['const next = produce(state, (draft) => {', "  draft.user.address.city = 'Pune';", '});'],
         c.T('produce') + 0.3, 0.15, 28, 'update.js', marks=[(1, c.T('draft', 2), YEL)])
    rows(c, 90, 820, [(c.T('Proxy'), 'draft is a Proxy that records writes', None, BLUE), (c.T('copies'), 'copy-on-write: only touched paths', None, ORANGE),
                      (c.T('freezes'), 'result frozen in development', None, PURPLE)], 140, 900, 110, 34)


def where(c):
    title(c, "YOU'VE ALREADY USED IT", 340, 0.1, 86)
    rows(c, 90, 520, [(c.T('createSlice'), 'Redux Toolkit createSlice', 'E07: state.items.push()', ORANGE), (c.T('useImmer'), 'useImmer hook', 'useState with a draft', BLUE),
                      (c.T('Zustand'), 'Zustand immer middleware', None, GRN)], 180, 900, 140, 38, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Why does this produce() throw?', c.T('throw'), 'intx', 46, INK)
    code(c, 30, 540, 1050, 730, ['produce(state, (d) => d.count = 5);'], c.T('arrow'), 0.1, 30, 'bug.js', circles=[(0, c.T('returns'), 'd.count = 5')])
    tb = c.T('both')
    if c.on(tb): label(c, 540, 810, 'it mutates AND returns 5 → Immer throws', tb, (255, 210, 210), INK, 30)
    code(c, 30, 890, 1050, 1080, ['produce(state, (d) => { d.count = 5; });'], c.T('Wrap'), 0.1, 30, 'fix.js', marks=[(0, c.T('braces', 2), YEL)])


SCENES = [
    (hook, "To change one city, deep inside your state, you write this. A spread at every level. Forget one spread, or make one typo, and half the object silently disappears. All to change one field."),
    (why, "Why not just mutate? Because React compares old state and new state by reference. If you mutate, it's the same object. React sees nothing changed, and skips the render."),
    (sharing, "The trick is structural sharing. The path you changed gets new objects. Every branch you didn't touch is reused as is. Cheap to create, and memo still works."),
    (suggest, "Immer is like suggesting mode in a shared document. You scribble your edits on a draft. When you're done, a clean new version is produced, and the original was never touched."),
    (produce_, "You call produce with your state, and a recipe that mutates a draft. The draft is a Proxy that records every write. Immer copies only the paths you touched, and freezes the result in development."),
    (where, "You've probably used it already. Redux Toolkit's createSlice runs on Immer. There's a useImmer hook for local state. And Zustand has an Immer middleware."),
    (gotcha, "Interview trap: why does this produce throw? The arrow function has no braces, so it returns the assignment, which is five. It mutates the draft and returns a value, both. Immer refuses. Wrap the body in braces."),
    (scene_next('S4 · E22', 'INTERVIEW QUESTIONS', 'URL, forms, machines, Immer', 'interview', 'machines'),
     "Next: four interview questions on URLs, forms, state machines, and Immer. Comment NOTES for the cheat sheet."),
]
