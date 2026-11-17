from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E27', tag='S3 · E27', short='WHY REACT RE-RENDERS')

def flash(c, box, at, col=GRN):
    if c.on(at) and c.t < at + 1.2:
        q = 1 - lin(c.t, at, at + 1.2)
        c.pen.rect(box[0] - 4, box[1] - 4, box[2] + 4, box[3] + 4, outline=mix(PAPER, col, q), w=6)

def hook(c):
    browser(c, 90, 340, 990, 1180, url='shop.example.com')
    boxes = [(130, 440, 950, 510), (130, 540, 330, 1140)] + [(360 + (k % 3) * 200, 640 + (k // 3) * 250, 540 + (k % 3) * 200, 860 + (k // 3) * 250) for k in range(6)]
    for b in boxes[1:]: c.pen.rect(*b, fill=LIGHT)
    c.pen.rect(*boxes[0], fill=WHITE, outline=INK, w=3)
    tt = c.T('type')
    c.pen.text(150, 475, typed_text(c, 's', tt, 0.1) or 'Search', 'ints', 30, INK if c.on(tt) else GREY, 'lm')
    tl = c.T('lights')
    if c.on(tl):
        for k, b in enumerate(boxes): flash(c, b, tl + k * 0.05 + (int((c.t - tl) / 1.3)) * 1.3)
    tw = c.T('Why')
    if c.on(tw): stamp(c.cv, 540, 1270, 'WHY?', 90, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')

def reasons(c):
    title(c, '3 REASONS TO RE-RENDER', 330, c.T('three'), 84, hlcol=YEL)
    rows(c, 90, 520, [('state', 'its own state changes', 'useState / useReducer', BLUE), ('context', 'a context it reads changes', 'useContext', PURPLE),
                      ('parent', 'its parent re-renders', 'the big one', RED)], 190, 900, 150, 42, 30)

def myth(c):
    head(c, 'THE MYTH', 'myth', size=96, y=340)
    txt(c, 540, 470, '"It re-renders when its props change."', c.T('props'), 'intx', 42, INK)
    tq = c.T('quite')
    if c.on(tq): cross(c.pen, 540, 470, 3.5, RED, 10, c.P(tq, 0.4))
    tp = c.T('parent')
    nodes = [('p', '<Parent>', 540, 620, None, tp), ('a', '<Header>', 260, 800, 'p', tp + 0.4), ('b', '<List>', 540, 800, 'p', tp + 0.5),
             ('c', '<Footer>', 820, 800, 'p', tp + 0.6), ('d', '<Row>', 440, 960, 'b', tp + 0.8), ('e', '<Row>', 640, 960, 'b', tp + 0.9)]
    tree(c, nodes, tp, 0.2, lambda k: (255, 238, 170), 30)
    tw = c.T('whether')
    if c.on(tw): label(c, 540, 1120, "props changed or not · every child re-renders", tw, (255, 210, 210), INK, 30)

def register(c):
    title(c, 'THE CLASS REGISTER', 330, 0.1, 100)
    ts = c.T('seat')
    for k in range(8):
        x = 180 + (k % 4) * 240; y = 560 + (k // 4) * 260
        moved = k == 5 and c.on(ts)
        person(c.pen, x + (60 if moved else 0), y + 120, 1.0, ORANGE if moved else BLUE)
        tr = c.T('called')
        if c.on(tr) and c.on(tr + k * 0.15): check(c.pen, x + 50, y - 50, 0.7, GRN, 6, c.P(tr + k * 0.15, 0.2))
    te = c.T('entire')
    if c.on(te): label(c, 540, 1160, 'one change · every name called', te, YEL, INK, 34)

def commit(c):
    title(c, 'RENDER ≠ DOM UPDATE', 330, c.T('update'), 90, hlcol=YEL)
    a = node(c, 270, 580, 380, 150, 'render', c.T('calling'), sub='call component + diff')
    b = node(c, 810, 580, 380, 150, 'commit', c.T('touches'), sub='only real changes → DOM', fill=(200, 240, 200))
    link(c, a, b, c.T('touches'))
    tn = c.T('nothing')
    if c.on(tn): txt(c, 540, 780, 'nothing changed → nothing in the DOM is touched', tn, 'ints', 32, INK)
    tc = c.T('cheap')
    if c.on(tc): label(c, 540, 920, 'usually cheap… until a component is slow or a list is huge', tc, WHITE, INK, 28)

def fix(c):
    title(c, 'MOVE STATE DOWN', 330, c.T('down'), 100, hlcol=YEL)
    code(c, 30, 440, 1050, 760, ['// before: every keystroke re-renders <ProductGrid />', 'function Page() {', "  const [q, setQ] = useState('');",
                                 '  return <><SearchBox q={q} onChange={setQ} /><ProductGrid /></>;', '}'], c.T('structural') - 0.4, 0.12, 22, 'Page.jsx',
         marks=[(2, c.T('structural'), (120, 60, 60))])
    code(c, 30, 820, 1050, 1060, ['// after: state lives inside <SearchBox />', 'function Page() {', '  return <><SearchBox /><ProductGrid /></>;', '}'],
         c.T('closer'), 0.12, 22, 'Page.jsx', marks=[(2, c.T('closer') + 0.5, (60, 110, 70))])
    tc = c.T('children')
    if c.on(tc): label(c, 540, 1140, 'or pass components as children', tc, YEL, INK, 32)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Components', 'Profiler'), dy=(1 - c.P(0, 0.45)) * 900)
    th = c.T('Highlight')
    if c.on(th):
        c.pen.rr(100, 460, 140, 500, 6, fill=YEL); check(c.pen, 120, 480, 0.6, INK, 5)
        c.pen.text(170, 480, 'Highlight updates when components render', 'ints', 28, WHITE, 'lm')
    tp = c.T('Profiler')
    if c.on(tp):
        for k, (nm, w, col) in enumerate((('Page', 0.9, GRN), ('SearchBox', 0.3, YEL), ('ProductGrid', 0.75, ORANGE), ('ProductCard ×48', 0.6, ORANGE))):
            y = 600 + k * 80; c.pen.rect(100, y, 100 + 860 * w * c.P(tp + k * 0.15, 0.3), y + 60, fill=col)
            c.pen.text(120, y + 30, nm, 'int', 26, INK, 'lm')
    tw = c.T('why')
    if c.on(tw):
        card(c.pen, 200, 950, 900, 1100, 14, WHITE, 6, 3)
        c.pen.text(240, 995, 'Why did this render?', 'intx', 28, INK, 'lm')
        c.pen.text(240, 1055, 'The parent component rendered.', 'mono', 26, RED, 'lm')

def gotcha(c):
    head(c, 'INTERVIEW QUESTION', 'Interview', size=70)
    txt(c, 540, 470, 'setState with the same value: re-render?', c.T('same'), 'intx', 44, INK)
    tn = c.T('Usually')
    if c.on(tn): title(c, 'USUALLY NO', 600, tn, 90, GRN)
    to = c.T('Object')
    if c.on(to): label(c, 540, 720, 'Object.is(old, new) → React bails out', to, (200, 240, 200), INK, 32)
    code(c, 40, 820, 1040, 1060, ['setCount(5);           // 5 → 5: bail out', "setUser({ ...user });  // new object: renders!"], c.T('new') - 0.3, 0.2, 28, 'Counter.jsx',
         marks=[(1, c.T('different'), (120, 60, 60))])

SCENES = [
    (hook, "You type one letter into a search box, and React DevTools lights up the whole page. The header, the sidebar, every product card. All of them re-rendered. Why?"),
    (reasons, "A component re-renders for three reasons. Its own state changes. A context it reads changes. Or its parent re-renders."),
    (myth, "And here's the myth: a component re-renders when its props change. Not quite. When a parent re-renders, every child re-renders by default, whether its props changed or not."),
    (register, "It's like a teacher who moves one student to a new seat, then reads the entire register from the top. Nothing changed for most students, but every name gets called."),
    (commit, "But a re-render isn't a DOM update. Rendering means calling your component and diffing the result. If nothing changed, React touches nothing in the DOM. Re-renders are usually cheap, until a component is slow, or a list is huge."),
    (fix, "The best fix is structural. Move state down, closer to where it's used. Or pass components as children, so they're created by a parent that doesn't re-render."),
    (proof, "In React DevTools, turn on Highlight updates, and watch what flashes as you type. Then record in the Profiler, and it can tell you why each component rendered."),
    (gotcha, "Interview question: does setState with the same value re-render? Usually no. If the new value is identical by Object dot is, React bails out. But a new object with the same contents is a different value, so it renders again."),
    (scene_next('S3 · E28', 'MEMO MYTHS', 'when useMemo makes it slower', 'memo', 'slower'),
     "Next: memo myths, and when useMemo actually makes things slower. Comment NOTES for the cheat sheet."),
]
