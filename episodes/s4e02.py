from engine.lib import *
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E02', tag='S4 · E02', short='THE 5 TYPES OF STATE')

TYPES = [('LOCAL UI', BLUE), ('SHARED CLIENT', PURPLE), ('SERVER', ORANGE), ('URL', TEAL), ('FORM', PINK)]


def hook(c):
    foodphone(c, 540, 820, [1, 0, 0], url='swiggy.com/?sort=rating')
    tags = [('dropdown open?', 860, 470, 'dropdown'), ('your cart', 860, 1180, 'cart'), ('menu + prices', 200, 760, 'prices'),
            ('?sort=rating', 200, 470, 'order'), ('address you typed', 200, 1180, 'typing')]
    for i, (s_, x, y, kw) in enumerate(tags):
        label(c, x, y, s_, c.T(kw), mix(WHITE, TYPES[i][1], 0.35), INK, 26)
    tf = c.T('five')
    if c.on(tf): stamp(c.cv, 540, 1310, '5 KINDS OF STATE', 70, c.P(tf, 0.35), -3, RED); c.sfx(tf, 'thud')


def home(c):
    title(c, 'WHERE YOU KEEP THINGS', 330, 0.1, 78)
    items = [('keys', 'keys · in your pocket', 'pocket', 'Your'), ('list', 'shopping list · fridge door', 'fridge', 'list'),
             ('bank', 'money · bank (you hold a passbook)', 'passbook', 'money'), ('addr', 'address · on the door', 'door', 'address'),
             ('form', 'half-filled form · on your desk', 'desk', 'form')]
    for i, (_, s_, kw, _k2) in enumerate(items):
        t = c.T(kw)
        y = 480 + i * 150
        if not c.on(t - 0.01): continue
        c.sfx(t, 'pop'); p = c.B(t, 0.35)
        card(c.pen, 90, y - 55 * p, 990, y + 55 * p, 20, WHITE, 8, 4)
        c.pen.circ(150, y, 26 * p, fill=TYPES[i][1], outline=INK, w=4)
        c.pen.text(150, y, str(i + 1), 'int', 26 * p, WHITE)
        c.pen.text(200, y, s_, 'intx', 36 * p, INK, 'lm')
    td = c.T('different')
    if c.on(td): label(c, 540, 1260, 'different things · different homes', td, YEL, INK, 34)


def typescene(i, name, analog, examples, homes, kw_home):
    def f(c):
        col = TYPES[i][1]
        p = c.B(0.05, 0.4); c.sfx(0.05, 'pop')
        c.pen.circ(170, 360, 70 * p, fill=col, outline=INK, w=6)
        c.pen.text(170, 360, str(i + 1), 'osw', 80 * p, WHITE)
        c.pen.text(270, 340, name, 'osw', 78 * p, INK, 'lm')
        c.pen.text(272, 405, 'STATE', 'osw', 40 * p, MUTE, 'lm')
        txt(c, 540, 520, analog, 0.4, 'ints', 34, MUTE)
        y = 640
        for k, (kw, ex) in enumerate(examples):
            t = c.T(kw)
            if c.on(t - 0.01):
                c.sfx(t, 'pop'); s = c.B(t, 0.3)
                w = c.pen.tw(ex, 'monob', 34) + 60
                c.pen.rr(540 - w / 2 * s + 6, y - 40 * s + 7, 540 + w / 2 * s + 6, y + 40 * s + 7, 20, fill=INK)
                c.pen.rr(540 - w / 2 * s, y - 40 * s, 540 + w / 2 * s, y + 40 * s, 20, fill=mix(WHITE, col, 0.3), outline=INK, w=4)
                c.pen.text(540, y, ex, 'monob', 34 * s, INK)
            y += 115
        th = c.T(kw_home)
        if c.on(th - 0.01):
            c.sfx(th, 'thud'); s = c.B(th, 0.4)
            darkcard(c.pen, 140, 1040, 940, 1180)
            c.pen.text(200, 1110, 'HOME', 'int', 30, YEL, 'lm')
            c.pen.text(330, 1110, homes, 'intx', 40 * s, WHITE, 'lm')
        for k in range(5):
            x = 540 + (k - 2) * 70
            c.pen.circ(x, 1280, 18, fill=TYPES[k][1] if k <= i else LIGHT, outline=INK, w=3)
    return f


def mistake(c):
    head(c, 'THE CLASSIC MISTAKE', 'mistake', size=76)
    code(c, 40, 440, 1040, 860, ['// server data copied into a global store', "case 'menu/loading': return { ...s, loading: true };",
                                 "case 'menu/loaded':  return { ...s, menu: a.data };", "case 'menu/failed':  return { ...s, error: a.err };",
                                 '// + refetch? stale? dedupe? cache time?'], c.T('copying'), 0.25, 24, 'menuSlice.js',
         marks=[(4, c.T('cache'), YEL)])
    tb = c.T('bloat')
    if c.on(tb):
        title(c, 'SERVER STATE', 980, tb, 90, hlcol=YEL)
        txt(c, 540, 1080, 'in disguise', c.T('disguise'), 'intx', 50, RED)
    tl = c.T('later')
    if c.on(tl): label(c, 540, 1210, 'its real home: a server cache (E11)', tl, WHITE, INK, 30)


def decide(c):
    title(c, '3 QUESTIONS', 330, 0.1, 100, hlcol=YEL)
    qs = [('server', 'From the server?', 'server cache', ORANGE), ('refresh', 'Survive refresh or a share?', 'the URL', TEAL),
          ('distant', 'Needed by distant components?', 'context / store', PURPLE)]
    for i, (kw, q, a, col) in enumerate(qs):
        t = c.T(kw); y = 500 + i * 190
        if not c.on(t - 0.01): continue
        c.sfx(t, 'pop'); s = c.B(t, 0.35)
        card(c.pen, 70, y - 65 * s, 650, y + 65 * s, 20, WHITE, 8, 4)
        c.pen.text(100, y, q, 'ints', 32 * s, INK, 'lm')
        ta = t + 0.9
        if c.on(ta):
            arrow(c.pen, 660, y, 720, y, c.P(ta, 0.3), INK, 6, 18)
            c.pen.rr(730, y - 45, 1020, y + 45, 22, fill=mix(WHITE, col, 0.35), outline=INK, w=4)
            c.pen.text(875, y, a, 'int', 30 * c.B(ta, 0.3), INK)
    to = c.T('Otherwise')
    if c.on(to):
        c.sfx(to, 'thud'); s = c.B(to, 0.4)
        darkcard(c.pen, 170, 1090, 910, 1230)
        c.pen.text(540, 1160, 'otherwise: keep it local', 'intx', 46 * s, YEL)


SCENES = [
    (hook, "One Swiggy screen. Is the sort dropdown open? What's in your cart? The menu and its prices. The sort order in the address bar. The address you're typing. That's five kinds of state, on one screen."),
    (home, "Think about where you keep things at home. Your keys go in your pocket. The family shopping list goes on the fridge door. Your money sits in the bank, and you only hold the passbook. Your address is on the door. And a half filled form waits on your desk. Different things, different homes."),
    (typescene(0, 'LOCAL UI', 'keys in your pocket', [('dropdown', 'isOpen'), ('tab', 'activeTab'), ('hover', 'hovered')], 'useState', 'use'),
     "One. Local UI state. Is the dropdown open, which tab is active, what's hovered. Only one component cares, so keep it in use state."),
    (typescene(1, 'SHARED CLIENT', 'the list on the fridge door', [('cart', 'cart'), ('theme', 'theme'), ('user', 'user')], 'context / store', 'store'),
     "Two. Shared client state. The cart, the theme, the logged in user. Many components read it, and the browser owns it. That's when you reach for context or a store."),
    (typescene(2, 'SERVER', 'money in the bank · you hold the passbook', [('menu', 'menu'), ('prices', 'prices'), ('orders', 'pastOrders')], 'a server cache', 'cache'),
     "Three. Server state. The menu, prices, your past orders. The database owns it. You only hold a copy, and copies go stale. It needs a cache that refetches."),
    (typescene(3, 'URL', 'the address on your door', [('query', '?q=biryani'), ('filters', '&veg=1'), ('page', '&page=2')], 'the address bar', 'bar'),
     "Four. URL state. The search query, the filters, the page number. Put it in the address bar, and it survives a refresh, and you can share it."),
    (typescene(4, 'FORM', 'the form on your desk', [('typed', 'values'), ('touched', 'touched'), ('invalid', 'errors')], 'a form library', 'library'),
     "Five. Form state. What you've typed, which fields you touched, and which are invalid. It's a draft until you submit, so let a form library hold it."),
    (mistake, "The classic mistake is copying server data into a global store. Now you're hand writing loading flags, refetching, and cache rules. Most store bloat is server state in disguise. We'll give it a real home later."),
    (decide, "So ask three questions. Does it come from the server? Use a server cache. Should it survive a refresh, or a share? Put it in the URL. Do distant components need it? Use context or a store. Otherwise, keep it local."),
    (scene_next('S4 · E03', 'COLOCATION', 'keep state close to where it is used', 'colocation', 'close'),
     "Next: colocation, and why state should live as close as possible to where it's used. Comment NOTES for the cheat sheet."),
]
