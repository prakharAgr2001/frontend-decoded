from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E06', tag='S4 · E06', short='REDUX FROM SCRATCH', hook='the whole idea in 10 lines')


def hook(c):
    words = [('actions', 220, 520, -6), ('reducers', 760, 600, 5), ('store', 300, 760, 4), ('middleware', 740, 860, -5), ('dispatch', 330, 1000, -3), ('thunks', 780, 1080, 6)]
    for i, (w, x, y, a) in enumerate(words):
        t = 0.3 + i * 0.25
        if c.on(t) and not c.on(c.T('core')): stamp(c.cv, x, y, w.upper(), 56, c.P(t, 0.3), a, MUTE); c.sfx(t, 'tick')
    tc = c.T('core')
    if c.on(tc):
        title(c, 'REDUX =', 620, tc, 120)
        title(c, '10 LINES', 800, c.T('ten'), 170, RED, hlcol=YEL)
    tw = c.T('write')
    if c.on(tw): label(c, 540, 1010, "let's write it", tw, YEL, INK, 40)


def ideas(c):
    title(c, '3 IDEAS', 330, 0.1, 110, hlcol=YEL)
    rows(c, 90, 520, [(c.T('One'), 'one store', 'a single object holds the app state', BLUE),
                      (c.T('describe'), 'actions describe what happened', "{ type: 'cart/added', item }", ORANGE),
                      (c.T('pure'), 'reducers are pure functions', '(state, action) → new state', GRN)], 200, 900, 150, 42, 30)
    tn = c.T('edits')
    if c.on(tn): label(c, 540, 1180, 'nobody edits state directly', tn, (255, 210, 210), INK, 34)


def register(c):
    title(c, 'THE HOSTEL GATE REGISTER', 330, 0.1, 76)
    card(c.pen, 140, 440, 940, 1160, 20, (255, 250, 235), 10, 5)
    c.pen.line([(260, 450), (260, 1150)], (230, 120, 120), 3, False)
    lines = [('Rahul', 'Rahul · OUT · 6:00 pm'), ('in', 'Rahul · IN · 10:05 pm'), ('Priya', 'Priya · OUT · 10:30 pm')]
    for k, (kw, s_) in enumerate(lines):
        t = c.T(kw)
        txt(c, 290, 540 + k * 90, s_, t, 'monob', 34, INK, 'lm', 'slide')
        if c.on(t): c.pen.text(200, 540 + k * 90, str(k + 1), 'monob', 30, MUTE)
    tn = c.T('Nobody')
    if c.on(tn): cross(c.pen, 880, 540, 1.0, RED, 9, c.P(tn, 0.3))
    tr = c.T('Read')
    if c.on(tr):
        q = c.P(tr, 1.2)
        c.pen.rect(150, 500 + 270 * q, 930, 506 + 270 * q, fill=YEL)
        darkcard(c.pen, 200, 880, 880, 1100)
        c.pen.text(540, 950, 'state now:', 'int', 30, (180, 186, 196))
        c.pen.text(540, 1030, '{ Rahul: in, Priya: out }', 'monob', 36, YEL)
    tx = c.T('replay')
    if c.on(tx): label(c, 540, 1240, 'actions = entries · state = what they add up to', tx, YEL, INK, 28)


def reducer(c):
    title(c, 'THE REDUCER', 330, 0.1, 100, hlcol=YEL)
    code(c, 30, 440, 1050, 900, ['function cart(state = { items: [] }, action) {', '  switch (action.type) {', "    case 'cart/added':",
                                 '      return { items: [...state.items, action.item] };', '    default:', '      return state;', '  }', '}'],
         c.T('takes'), 0.12, 24, 'cartReducer.js', marks=[(3, c.T('new'), YEL), (5, c.T('unchanged'), YEL)])
    tn = c.T('never')
    if c.on(tn):
        card(c.pen, 120, 980, 960, 1140, 24, WHITE, 10, 5)
        c.pen.text(540, 1030, 'never: state.items.push(item)', 'monob', 32, RED)
        c.pen.text(540, 1090, 'always return a new object', 'ints', 32, INK)


def store(c):
    title(c, 'THE STORE', 330, 0.1, 100, hlcol=YEL)
    code(c, 30, 430, 1050, 1060, ['function createStore(reducer) {', '  let state = reducer(undefined, {}), subs = new Set();', '  return {',
                                  '    getState: () => state,', '    subscribe: (fn) => (subs.add(fn), () => subs.delete(fn)),',
                                  '    dispatch(action) {', '      state = reducer(state, action);', '      subs.forEach((fn) => fn());', '    } };', '}'],
         c.T('variable'), 0.1, 23, 'createStore.js',
         marks=[(1, c.T('variable') + 0.6, YEL), (4, c.T('listeners'), YEL), (6, c.T('runs'), YEL), (7, c.T('tells'), YEL)])
    tt = c.T("That's")
    if c.on(tt): stamp(c.cv, 540, 1180, 'THAT IS REDUX', 74, c.P(tt, 0.35), -3, RED); c.sfx(tt, 'thud')


def flow(c):
    title(c, 'ONE-WAY DATA FLOW', 330, c.T('direction'), 90, hlcol=YEL)
    pts = {'ui': (540, 520), 'act': (850, 780), 'red': (540, 1040), 'st': (230, 780)}
    ui = node(c, 540, 520, 300, 120, 'UI', c.T('click'), ic=None, fill=WHITE, size=40)
    ac = node(c, 850, 780, 340, 120, 'dispatch(action)', c.T('dispatches'), fill=(255, 225, 190), size=28)
    rd = node(c, 540, 1040, 300, 120, 'reducer', c.T('reducer'), fill=(200, 240, 200), size=36)
    st = node(c, 230, 780, 300, 120, 'new state', c.T('state'), fill=(255, 238, 170), size=32)
    link(c, ui, ac, c.T('dispatches')); link(c, ac, rd, c.T('reducer')); link(c, rd, st, c.T('state')); link(c, st, ui, c.T('subscribers'))
    ts = c.T('subscribers')
    if c.on(ts):
        k = (c.t - ts) % 2.4
        segs = [(ui, ac), (ac, rd), (rd, st), (st, ui)]
        i = int(k / 0.6); a, b = segs[i]
        packet(c, a, b, ts + int((c.t - ts) / 0.6) * 0.6, ts + int((c.t - ts) / 0.6) * 0.6 + 0.55, YEL)


def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Redux', 'Action', 'State', 'Diff'), dy=(1 - c.P(0, 0.45)) * 900)
    acts = ['@@INIT', 'cart/added', 'cart/added', 'coupon/applied', 'cart/removed']
    ta = c.T('every')
    for k, a in enumerate(acts):
        t = ta + k * 0.3
        if not c.on(t): continue
        y = 470 + k * 76; c.sfx(t, 'tick')
        tj = c.T('Jump')
        sel = c.on(tj) and k == 2
        if sel: c.pen.rect(70, y - 32, 600, y + 32, fill=(50, 70, 110))
        c.pen.text(100, y, a, 'mono', 30, WHITE, 'lm')
        if c.on(tj): c.pen.text(560, y, 'Jump', 'int', 22, YEL if sel else (130, 136, 146), 'rm')
    tj = c.T('Jump')
    if c.on(tj):
        c.pen.line([(620, 440), (620, 1100)], (60, 66, 76), 2, False)
        c.pen.text(650, 470, 'state', 'int', 26, (150, 156, 166), 'lm')
        c.pen.text(650, 540, 'items: [2]', 'monob', 28, NU, 'lm')
    tt = c.T('travel')
    if c.on(tt): label(c, 540, 1060, 'Redux DevTools extension · any Redux app', tt, YEL, INK, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 470, 'Why must reducers return new objects?', c.T('return'), 'intx', 44, INK)
    code(c, 40, 560, 1040, 770, ['state.items.push(item); return state; // mutated'], c.T('mutate'), 0.1, 26, 'bug.js', marks=[(0, c.T('reference'), YEL)])
    tr = c.T('compares')
    if c.on(tr):
        card(c.pen, 120, 840, 960, 1060, 24, WHITE, 10, 5)
        c.pen.text(540, 900, 'Object.is(prev, next) → true', 'monob', 32, INK)
        c.pen.text(540, 990, 'the UI never updates', 'intx', 42, RED)
    tt = c.T('breaks')
    if c.on(tt): label(c, 540, 1160, 'and time travel breaks', tt, (255, 210, 210), INK, 32)


SCENES = [
    (hook, "Redux sounds heavy. Actions, reducers, stores, middleware. But the core of Redux is about ten lines of code. Let's write it."),
    (ideas, "It rests on three ideas. One store, a single object that holds your app's state. Actions, plain objects that describe what happened. And reducers, pure functions that take the state and an action, and return the next state. Nobody edits state directly."),
    (register, "Think of the register at a hostel gate. Rahul out, six PM. Rahul in, ten oh five. Priya out, ten thirty. Nobody erases an old line. Read the register from the top, and you know where everyone is right now. You can even replay the day."),
    (reducer, "Here's a reducer. It takes the current cart and an action. For cart added, it returns a new object with the item appended. For anything else, it returns the state unchanged. It must never mutate."),
    (store, "And here's the store. A variable that holds the state. A set of listeners. Dispatch runs the reducer, saves the result, and tells every listener. That's Redux."),
    (flow, "So data moves in one direction. You click. The UI dispatches an action. The reducer computes the new state. And subscribers re-render with it. Every change has a name, and one path."),
    (proof, "See it yourself. With the Redux DevTools extension, every action is listed in order. Jump to any one, and the app rewinds to that moment. That's time travel debugging."),
    (gotcha, "Interview trap: why must a reducer return a new object? If you mutate and return the same reference, React Redux compares old and new, sees the same object, and decides nothing changed. Your UI never updates, and time travel breaks."),
    (scene_next('S4 · E07', 'REDUX TOOLKIT', 'the same idea · a third of the code', 'Toolkit', 'third'),
     "Next: Redux Toolkit. The same idea, with a third of the code. Comment NOTES for the cheat sheet."),
]
