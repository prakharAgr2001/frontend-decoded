from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E29', tag='S3 · E29', short='useTransition + COMPILER')

def hook(c):
    tt = c.T('type')
    q = typed_text(c, 'nike', tt, 0.45)
    addressbar(c, 110, 380, 970, q, True, 44, 96, 'Filter products')
    for k in range(6):
        y = 540 + k * 100
        c.pen.rr(110, y, 970, y + 80, 12, fill=WHITE, outline=GREY, w=3)
        c.pen.rect(130, y + 15, 180, y + 65, fill=LIGHT); c.pen.rr(200, y + 25, 600 - (k % 3) * 80, y + 50, 8, fill=LIGHT)
    tf = c.T('freezes')
    if c.on(tf):
        if int((c.t - tf) / 0.45) % 2 == 0: c.pen.rr(110, 380, 970, 476, 48, outline=RED, w=6)
        stamp(c.cv, 540, 1200, 'INPUT FREEZES', 70, c.P(tf, 0.35), -3, RED); c.sfx(tf, 'thud')
    tl = c.T('letter')
    if c.on(tl): txt(c, 540, 1330, 'whole list re-renders before your letter shows', tl, 'ints', 30, INK)

def urgent(c):
    title(c, 'NOT ALL UPDATES ARE URGENT', 330, c.T('urgent'), 76)
    rows(c, 90, 520, [('instantly', 'the letter in the input', 'urgent · now', RED), ('wait', 'the filtered list', 'can wait a few ms', BLUE)], 180, 900, 140, 42, 30)
    tu = c.T('useTransition')
    if c.on(tu): label(c, 540, 900, 'useTransition: mark which is which', tu, YEL, INK, 34)

def code_(c):
    code(c, 30, 330, 1050, 900, ["const [query, setQuery] = useState('');", "const [filter, setFilter] = useState('');", 'const [isPending, startTransition] = useTransition();', '',
                                 'function onChange(e) {', '  setQuery(e.target.value);                  // urgent',
                                 '  startTransition(() => setFilter(e.target.value)); // can wait', '}'], c.T('input') - 0.6, 0.1, 21, 'Search.jsx',
         marks=[(5, c.T('input'), (120, 60, 60)), (6, c.T('transition'), (60, 90, 140))])
    tp = c.T('isPending')
    if c.on(tp): label(c, 540, 990, 'isPending → show a subtle spinner', tp, WHITE, INK, 32)

def triage(c):
    title(c, 'TRIAGE', 330, c.T('triage'), 120, hlcol=(255, 190, 190))
    ts = c.T('sprained')
    if c.on(ts): node(c, 300, 600, 380, 160, 'sprained ankle', ts, sub='the list render', fill=(200, 220, 255))
    te = c.T('emergency')
    if c.on(te): node(c, 780, 600, 380, 160, 'emergency', te, sub='your keystroke', fill=(255, 210, 210))
    tp = c.T('pauses')
    if c.on(tp):
        x = 110
        for k, (w, col, nm) in enumerate(((260, BLUE, 'list…'), (120, RED, 'key'), (220, BLUE, 'list…'), (120, RED, 'key'), (140, BLUE, 'list'))):
            t = tp + k * 0.35
            if c.on(t): c.pen.rect(x, 820, x + w * c.P(t, 0.3), 900, fill=col, outline=INK, w=3); c.pen.text(x + w / 2, 860, nm, 'int', 26, WHITE)
            x += w + 6
    tb = c.T('back')
    if c.on(tb): label(c, 540, 1000, 'interruptible: keystrokes cut in line', tb, YEL, INK, 32)

def deferred(c):
    title(c, 'useDeferredValue', 330, c.T('useDeferredValue'), 90, hlcol=YEL)
    code(c, 30, 450, 1050, 700, ['const deferredQuery = useDeferredValue(query);', '<ProductList query={deferredQuery} />'], c.T('lagging') - 0.4, 0.15, 26, 'Search.jsx',
         marks=[(0, c.T('lagging'), YEL)])
    to = c.T('own')
    if c.on(to): txt(c, 540, 800, "when you don't own the setter", to, 'intx', 38, INK)

def compiler(c):
    title(c, 'THE REACT COMPILER', 330, c.T('Compiler'), 96, hlcol=YEL)
    tb = c.T('build')
    if c.on(tb):
        a = node(c, 270, 560, 360, 150, 'your code', tb, 'doc')
        b = node(c, 810, 560, 360, 150, 'auto-memoized', tb + 0.4, 'cpu', fill=(200, 240, 200))
        link(c, a, b, tb + 0.4, txt_='build time')
    tv = c.T('version')
    if c.on(tv): label(c, 540, 760, 'v1.0 · late 2025', tv, WHITE, INK, 32)
    tu = c.T('unnecessary')
    if c.on(tu):
        for k, nm in enumerate(('useMemo', 'useCallback', 'React.memo')):
            x = 230 + k * 310
            pill(c.pen, x, 900, nm, c.B(tu + k * 0.1, 0.3), LIGHT, MUTE, 32)
            c.pen.line([(x - 100, 900), (x + 100, 900)], RED, 5)

def proof(c):
    panel(c, 50, 330, 1030, 1000, tabs=('Components',), dy=(1 - c.P(0, 0.45)) * 900)
    tb = c.T('badge')
    for k, (nm, memo) in enumerate((('App', False), ('SearchBox', True), ('ProductList', True), ('ProductCard', True))):
        y = 480 + k * 90
        c.pen.text(100 + k * 30, y, nm, 'mono', 30, (220, 160, 255), 'lm')
        if memo and c.on(tb):
            w = c.pen.tw(nm, 'mono', 30)
            pill(c.pen, 100 + k * 30 + w + 90, y, 'Memo', c.B(tb + k * 0.15, 0.3), (60, 70, 90), WHITE, 24, outline=None)
    tm = c.T('optimized')
    if c.on(tm): txt(c, 540, 900, 'compiler-optimized components get a badge', tm, 'ints', 30, YEL)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"useTransition makes the work faster."', c.T('faster'), 'intx', 44, INK)
    tn = c.T('No')
    if c.on(tn): title(c, 'NO.', 600, tn, 110, RED)
    tl = c.T('long')
    if c.on(tl):
        bars(c, 60, 720, [('before', 400, BLUE, tl), ('after', 400, BLUE, tl + 0.3)], 400, 540, 70, 110, '{} ms', 200, 32)
    ti = c.T('interruptible')
    if c.on(ti): label(c, 540, 980, 'same work · now interruptible', ti, YEL, INK, 34)
    tv = c.T('virtualize')
    if c.on(tv): txt(c, 540, 1080, 'list still too slow? virtualize it, or do less', tv, 'ints', 32, INK)

SCENES = [
    (hook, "You type into a filter box, above a list of five thousand products. Every keystroke freezes the input for a moment, because React re-renders the whole list before showing your letter."),
    (urgent, "But not every update is equally urgent. The letter in the input must appear instantly. The filtered list can wait a few milliseconds. useTransition lets you mark which is which."),
    (code_, "Update the input state normally. Wrap the slow filter update in start transition. And isPending tells you when to show a subtle spinner."),
    (triage, "It's hospital triage. A sprained ankle waits when an emergency comes in. React pauses the list render when a new keystroke arrives, handles it, then picks the list back up."),
    (deferred, "If you don't own the setter, useDeferredValue works from the other side. It gives you a lagging copy of a value, to render the slow part with."),
    (compiler, "And all that manual memoization? The React Compiler, which reached version one point zero in late twenty twenty five, memoizes components and values for you, at build time. Most hand written useMemo and useCallback become unnecessary."),
    (proof, "With the compiler on, React DevTools shows a Memo badge on every component it optimized."),
    (gotcha, "Interview trap: useTransition makes the work faster. No. The work takes just as long. It only becomes interruptible, so typing stays responsive. If the list is still too slow, virtualize it, or do less work."),
    (scene_next('S3 · E30', 'CHUNKING LONG TASKS', 'yield like you mean it', 'long', 'yield'),
     "Next: chunking long tasks, and how to yield like you mean it. Comment NOTES for the cheat sheet."),
]
