from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E03', tag='S4 · E03', short='STATE COLOCATION', hook='why one keystroke re-renders all')

GLOW = (255, 238, 170)


def apptree(c, at, step=0.12, flash=None, hot=None):
    nodes = [('app', '<App>', 540, 520, None, at), ('nav', '<Navbar>', 250, 700, 'app', at + step), ('page', '<MenuPage>', 540, 700, 'app', at + 2 * step),
             ('cart', '<CartBar>', 830, 700, 'app', at + 3 * step), ('search', '<Search>', 400, 880, 'page', at + 4 * step),
             ('list', '<ItemList>', 690, 880, 'page', at + 5 * step), ('card', '<ItemCard> ×40', 690, 1050, 'list', at + 6 * step)]
    col = (lambda k: GLOW if (hot and k in hot) else WHITE)
    pos = tree(c, nodes, at, step, col, 30)
    if flash is not None and c.on(flash):
        ph = int((c.t - flash) / 0.9)
        for k, (x, y, _) in pos.items():
            if hot is None or k in hot:
                flash_box(c, (x - 130, y - 34, x + 130, y + 34), flash + ph * 0.9, GRN, 0.8)
    return pos


def hook(c):
    pos = apptree(c, 0.1)
    st = c.T('state')
    if c.on(st):
        objcard(c, 640, 330, 1040, ['search, menuOpen,', 'cartOpen, tab...'], st, 'App state', 24, dy=0)
    tt = c.T('typing')
    if c.on(tt):
        apptree(c, 0.1, flash=tt + 0.3)
        label(c, 400, 1180, 'type "b" · everything re-renders', tt, (255, 210, 210), INK, 30)


def define(c):
    title(c, 'COLOCATION', 380, 0.1, 140, hlcol=YEL)
    card(c.pen, 110, 540, 970, 760, 26, WHITE, 12, 5)
    txt(c, 540, 610, 'keep state as close as possible', c.T('close'), 'intx', 44, INK)
    txt(c, 540, 690, 'to the components that use it', c.T('use'), 'intx', 44, INK)
    tl = c.T('lives')
    if c.on(tl): label(c, 540, 880, 'state lives with whoever needs it', tl, YEL, INK, 36)
    th = c.T('higher')
    if c.on(th): title(c, '…AND NO HIGHER', 1030, th, 80, RED)


def remote(c):
    title(c, 'THE TV REMOTE', 330, 0.1, 100)
    tv = node(c, 300, 600, 300, 220, 'TV', c.T('belongs'), ic='laptop')
    rm = node(c, 300, 870, 180, 110, 'remote', c.T('next'), fill=GLOW, size=30)
    to = c.T('office')
    if c.on(to):
        of = node(c, 800, 1060, 300, 160, 'society office', to, ic='server', size=28)
        tp = c.T('trip')
        if c.on(tp):
            packet(c, tv, of, tp, tp + 1.4, YEL, 'walk down')
            packet(c, of, tv, tp + 1.5, tp + 2.9, YEL, 'walk up')
        link(c, tv, of, to + 0.2, dash=True)
    tc = c.T('change')
    if c.on(tc): label(c, 760, 600, 'every channel change', tc, (255, 210, 210), INK, 30)


def lift(c):
    title(c, 'LIFT ONLY TO THE', 330, c.T('rule'), 70)
    title(c, 'CLOSEST COMMON PARENT', 420, c.T('closest'), 70, hlcol=YEL)
    ts = c.T('start')
    hot = {'search'} if not c.on(c.T('lift')) else {'page'}
    apptree(c, ts - 0.6, 0.05, hot=hot)
    tl = c.T('lift')
    if c.on(tl):
        label(c, 540, 610, 'state: query', tl, YEL, INK, 28)
        txt(c, 540, 1180, '<Search> and <ItemList> both need the query', tl, 'ints', 32, INK)
    tn = c.T('Not')
    if c.on(tn):
        cross(c.pen, 380, 520, 1.0, RED, 10, c.P(tn, 0.3))


def fix(c):
    title(c, 'MOVE IT DOWN', 330, c.T('before'), 100, hlcol=YEL)
    code(c, 30, 440, 1050, 760, ['function App() {', '  const [menuOpen, setMenuOpen] = useState(false);', '  return <><Navbar open={menuOpen} ... /><Page /></>;', '}'],
         c.T('before'), 0.12, 24, 'before.jsx', marks=[(1, c.T('App'), YEL)])
    code(c, 30, 810, 1050, 1080, ['function Navbar() {', '  const [open, setOpen] = useState(false);', '  return <nav>...</nav>;', '}'],
         c.T('After'), 0.12, 24, 'after.jsx', marks=[(1, c.T('Navbar'), YEL)])
    tp = c.T('page')
    if c.on(tp): label(c, 540, 1160, 'menu toggles no longer re-render the page', tp, (200, 240, 200), INK, 30)


def callback(c):
    chapter(c, 540, 340, 'S3 · E27', 'Why React re-renders', 0.1)
    pos = apptree(c, 0.3, 0.05)
    tt = c.T('top', 2)
    if c.on(tt): apptree(c, 0.3, 0.05, flash=tt)
    tp = c.T('parent')
    if c.on(tp): label(c, 540, 1180, 'parent renders → children render', tp, YEL, INK, 32)


def delete(c):
    title(c, 'EASIER TO DELETE', 340, c.T('delete'), 100, hlcol=YEL)
    rows(c, 90, 520, [(c.T('faster'), 'fewer components re-render', None, 'ok'), (c.T('remove'), 'delete a component · its state goes too', None, 'ok'),
                      (c.T('orphan'), 'no orphan fields in a global store', None, 'ok')], 160, 900, 120, 36)
    to = c.T('reads')
    if c.on(to):
        objcard(c, 140, 1000, 940, ['store.legacyFilterOpen // used by... nobody?'], to, 'store.js', 24, dy=0)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 470, 'When should state be global?', c.T('global'), 'intx', 48, INK)
    tw = c.T('wide')
    if c.on(tw):
        for k, ex in enumerate(('user', 'theme', 'locale')):
            label(c, 300 + k * 240, 610, ex, tw + 0.3 + k * 0.2, (200, 240, 200), INK, 34)
    td = c.T('distant')
    if c.on(td): txt(c, 540, 720, 'read by many distant components', td, 'ints', 36, INK)
    tg = c.T('giant')
    if c.on(tg):
        card(c.pen, 120, 830, 960, 1110, 24, WHITE, 10, 5)
        c.pen.text(540, 900, 'global ≠ one giant object', 'intx', 46, RED)
        c.pen.text(540, 990, 'split by concern · small stores', 'ints', 34, INK)
        c.pen.text(540, 1050, '(next episode: why)', 'intm', 28, MUTE)


SCENES = [
    (hook, "A team put every piece of state at the top of the app, in one App component. It felt organised. Then typing one letter in the search box re-rendered the entire page."),
    (define, "The fix has a name: colocation. Keep state as close as possible to the components that use it. In plain English, state lives with whoever needs it, and no higher."),
    (remote, "Think of the TV remote. It belongs in the living room, next to the TV. Now imagine keeping it in the society office downstairs. Every channel change means a trip down and back up."),
    (lift, "The rule is simple. Start local. When two components need the same state, lift it to their closest common parent. Not to the top of the app."),
    (fix, "Here's the before. The menu toggle lives in App, so opening the menu re-renders the whole app. After: it lives inside Navbar, and toggling it never touches the page."),
    (callback, "This is season three, episode twenty seven again. When a parent re-renders, its children re-render. So state at the top means every update starts at the top."),
    (delete, "Colocated state is faster, and easier to delete. Remove a component, and its state goes with it. No orphan fields in a global store that nobody reads anymore."),
    (gotcha, "Interview question: so when should state be global? When it's truly app wide, like the user, the theme, or the language, and many distant components read it. Even then, global doesn't mean one giant object."),
    (scene_next('S4 · E04', 'THE CONTEXT TRAP', 'why one Provider re-renders everything', 'context', 'everything'),
     "Next: the context trap, and why one provider can re-render everything. Comment NOTES for the cheat sheet."),
]
