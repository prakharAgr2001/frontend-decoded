from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E28', tag='S3 · E28', short='MEMO MYTHS')

def hook(c):
    for k, (nm, kw) in enumerate((('useCallback(…)', 'useCallback'), ('useMemo(…)', 'useMemo'), ('React.memo(…)', 'memo'))):
        t = c.T(kw)
        if not c.on(t): continue
        for j in range(4):
            tt = t + j * 0.1
            if c.on(tt): pill(c.pen, 200 + j * 230, 430 + k * 110, nm, c.B(tt, 0.3), [(200, 220, 255), (255, 238, 170), (230, 210, 255)][k], INK, 22)
    ts = c.T('slower')
    if c.on(ts):
        counter(c, 540, 870, 120, 180, ts, ts + 0.8, '{:.0f}', 110, RED, ' ms render')
        stamp(c.cv, 540, 1060, 'SLOWER?!', 80, c.P(ts + 0.5, 0.35), -4, RED); c.sfx(ts + 0.5, 'thud')

def what(c):
    title(c, 'THE THREE TOOLS', 330, 0.1, 96)
    rows(c, 90, 520, [('React', 'React.memo', 'skip re-render if props are shallow-equal', PURPLE), ('caches', 'useMemo', 'cache a computed value', YEL),
                      ('identity', 'useCallback', 'keep a function identity stable', BLUE)], 200, 900, 160, 44, 30)

def fridge(c):
    title(c, 'CHECK THE FRIDGE FIRST?', 330, c.T('fridge'), 84)
    card(c.pen, 140, 450, 420, 1050, 20, (230, 240, 250), 10, 5); c.pen.line([(140, 700), (420, 700)], INK, 5)
    c.pen.rr(380, 520, 395, 640, 6, fill=INK)
    te = c.T('expensive')
    if c.on(te):
        node(c, 720, 580, 400, 160, 'shop is far', te, 'globe', fill=(200, 240, 200)); check(c.pen, 940, 520, 1.0, GRN, 9, c.P(te + 0.3, 0.3))
        txt(c, 720, 700, 'worth checking', te + 0.3, 'ints', 30, GRN)
    tn = c.T('door')
    if c.on(tn):
        node(c, 720, 880, 400, 160, 'shop next door', tn, 'globe', fill=(255, 220, 220)); cross(c.pen, 940, 820, 1.0, RED, 9, c.P(tn + 0.3, 0.3))
        txt(c, 720, 1000, 'checking costs more', tn + 0.3, 'ints', 30, RED)

def myth1(c):
    head(c, 'MYTH 1: MEMO IS FREE', 'free', size=70, y=340)
    rows(c, 90, 520, [('stores', 'stores the previous value', 'memory', ORANGE), ('compares', 'compares deps on every render', 'CPU', ORANGE)], 170, 900, 130, 40, 30)
    tc = c.T('cheap')
    if c.on(tc):
        bars(c, 60, 860, [('re-render', 40, GRN, tc), ('memo check', 55, RED, tc + 0.3)], 60, 520, 80, 120, '{} µs', 260, 32)
        txt(c, 540, 1140, 'cheap component: the check costs more', tc + 0.5, 'intx', 34, RED)

def myth2(c):
    head(c, 'MYTH 2: MEMO IS ENOUGH', 'enough', size=66, y=340)
    code(c, 30, 440, 1050, 840, ["const Chart = memo(function Chart({ options, onSelect }) {", '  /* heavy rendering */', '});', '',
                                 "<Chart options={{ theme: 'dark' }} onSelect={() => pick(id)} />"], c.T('inline') - 0.4, 0.15, 23, 'Dashboard.jsx',
         circles=[(4, c.T('object'), "{{ theme: 'dark' }}"), (4, c.T('arrow'), '() => pick(id)')])
    tf = c.T('fails')
    if c.on(tf): stamp(c.cv, 540, 900, 'NEW PROPS EVERY RENDER', 54, c.P(tf, 0.35), -3, RED); c.sfx(tf, 'thud')
    code(c, 30, 980, 1050, 1220, ["const options = useMemo(() => ({ theme: 'dark' }), []);", 'const onSelect = useCallback(() => pick(id), [id]);'],
         c.T('Stabilize'), 0.15, 23, 'Dashboard.jsx', marks=[(0, c.T('Stabilize'), (60, 110, 70)), (1, c.T('Stabilize') + 0.3, (60, 110, 70))])

def when(c):
    title(c, 'MEMOIZE ON EVIDENCE', 330, c.T('evidence'), 90, hlcol=YEL)
    rows(c, 90, 520, [('slow', 'slow to render (measured!)', None, 'ok'), ('often', 're-renders often, same props', None, 'ok'),
                      ('child', 'passed into a memoized child', None, 'ok'), ('effect', 'a dependency of an effect', None, 'ok')], 140, 900, 110, 38)

def proof(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Profiler', 'Ranked'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    tr = c.T('render')
    items = [('ProductGrid', 0.9, '38.2 ms', RED), ('Chart', 0.6, '21.0 ms', ORANGE), ('Header', 0.06, '0.4 ms', GRN), ('Button', 0.03, '0.1 ms', GRN)]
    for k, (nm, w, v, col) in enumerate(items):
        t = tr + k * 0.2
        if not c.on(t): continue
        y = 480 + k * 100; p = c.P(t, 0.4)
        c.pen.rect(100, y, 100 + 600 * w * p + 8, y + 70, fill=col)
        c.pen.text(120 if w > 0.2 else 120 + 600 * w + 20, y + 35, nm, 'int', 28, INK if w > 0.2 else WHITE, 'lm')
        c.pen.text(980, y + 35, v, 'monob', 28, WHITE, 'rm')
    ts = c.T('slow')
    if c.on(ts): c.pen.rect(90, 470, 990, 670, outline=YEL, w=5)
    tt = c.T('tiny')
    if c.on(tt): txt(c, 540, 930, 'memoize the slow bars · skip the tiny ones', tt, 'intx', 34, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, 'useMemo with [] — a guarantee?', c.T('guarantee'), 'intx', 46, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 600, tn, 110, RED)
    tt = c.T('throw')
    if c.on(tt): txt(c, 540, 740, 'React may throw cached values away', tt, 'ints', 34, INK)
    tp = c.T('correctness')
    if c.on(tp):
        pill(c.pen, 330, 880, 'for performance', c.B(c.T('performance'), 0.35), (200, 240, 200), INK, 36)
        pill(c.pen, 760, 880, 'never for correctness', c.B(tp, 0.35), (255, 210, 210), INK, 36)

SCENES = [
    (hook, "Your team wraps every function in useCallback, every value in useMemo, and every component in React dot memo. And the app gets slower. How?"),
    (what, "First, the tools. React dot memo skips re-rendering a component when its props are shallowly equal to last time. useMemo caches a computed value. And useCallback keeps a function's identity stable."),
    (fridge, "Memoization is like checking your fridge before going shopping. Worth it when the shop is far and expensive. Pointless when the shop is next door."),
    (myth1, "Myth one: memo is free. Every memo stores the previous value, and compares dependencies on every render. For cheap components and simple values, the check can cost more than just rendering again."),
    (myth2, "Myth two: memo is enough. Pass an inline object, or an arrow function, and that prop is brand new every render. The comparison fails, and memo does nothing. Stabilize them with useMemo and useCallback."),
    (when, "So memoize on evidence. A component that's measurably slow to render, that re-renders often with the same props. A value passed into a memoized child. Or a dependency of an effect."),
    (proof, "The Profiler's ranked view sorts components by render time. Memoize the slow bars at the top, and skip the tiny ones."),
    (gotcha, "Interview question: is useMemo with an empty dependency array a guarantee? No. React may throw cached values away. Use it for performance, never for correctness."),
    (scene_next('S3 · E29', 'useTransition', 'and the React Compiler', 'transition', 'Compiler'),
     "Next: use transition, and the React Compiler that memoizes for you. Comment NOTES for the cheat sheet."),
]
