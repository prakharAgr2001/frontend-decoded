from engine.lib import *
from engine.s4_extra import *

EP = dict(id='S4E23', tag='S4 · E23', short='FINALE: ONE ORDER', tail=3.0, hook='one food order, every state')

HOMES = [('URL', TEAL), ('LOCAL', BLUE), ('SERVER', ORANGE), ('STORE', PURPLE), ('CONTEXT', PURPLE), ('FORM', PINK), ('MACHINE', RED)]


def chaps(c, items, y0=900, gap=100):
    for i, (tag, name, kw) in enumerate(items):
        at = c.T(kw) if isinstance(kw, str) else kw
        chapter(c, 540, y0 + i * gap, tag, name, at)


def homebar(c, active):
    """row of 'state homes' at the top; active ones lit"""
    for k, (nm, col) in enumerate(HOMES):
        x = 110 + k * 143
        on = nm in active
        c.pen.rr(x - 66, 300, x + 66, 350, 25, fill=col if on else LIGHT, outline=INK if on else GREY, w=3)
        c.pen.text(x, 325, nm, 'int', 20, WHITE if on else GREY)


def intro(c):
    stamp(c.cv, 540, 420, 'SEASON 4 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'ONE FOOD ORDER.', 640, c.T('order'), 104)
    title(c, 'EVERY KIND OF STATE.', 800, c.T('every'), 92, hlcol=YEL)
    td = c.T('doorstep')
    if c.on(td): label(c, 540, 960, 'search → menu → cart → checkout → pay → track', td, WHITE, INK, 28)


def search(c):
    homebar(c, {'URL', 'LOCAL'})
    addressbar(c, 50, 420, 1030, typed_text(c, '/search?q=biryani', c.T('search'), 0.06) + ('&veg=1' if c.on(c.T('veg')) else ''), cursor=False, size=34)
    tv = c.T('veg')
    if c.on(tv): label(c, 540, 600, 'pure veg ✓', tv, (200, 240, 200), INK, 32)
    chaps(c, [('E18', 'filters live in the URL', 'URL'), ('E03', 'dropdown open? local, colocated', 'colocated')], 760, 120)


def menu(c):
    homebar(c, {'SERVER'})
    objcard(c, 90, 420, 990, ["useQuery({ queryKey: ['menu', 42], queryFn })"], c.T('caches') - 0.3, 'Menu.jsx', 28, dy=0)
    chaps(c, [('E11', 'the menu is server state', 'server'), ('E12', 'cached by key · instant on return', 'instant'), ('E12', 'refetched quietly in the background', 'background')], 720, 120)


def cart(c):
    homebar(c, {'STORE'})
    ta = c.T('add')
    q = [1 if c.on(ta + 0.3) else 0, 1 if c.on(ta + 0.9) else 0, 0]
    foodphone(c, 300, 760, q, w=520, h=740, url='food app')
    for i, (tag, name, kw) in enumerate([('E08', 'cart: small store', 'store'), ('E09', 'badge selects count', 'count'), ('E01', 'total is derived', 'derived')]):
        at = c.T(kw)
        if c.on(at): chapter(c, 810, 520 + i * 180, tag, name, at)


def ctx(c):
    homebar(c, {'CONTEXT'})
    for k, (nm, kw) in enumerate((('ThemeCtx', 'theme'), ('UserCtx', 'user'))):
        node(c, 300 + k * 480, 560, 400, 160, nm, c.T(kw), fill=(220, 205, 250), sub='rarely changes', size=40)
    chaps(c, [('E04', 'context for values that rarely change', 'rarely')], 800, 100)


def checkout(c):
    homebar(c, {'FORM', 'SERVER'})
    card(c.pen, 140, 420, 940, 720, 20, WHITE, 10, 5)
    c.pen.text(180, 470, 'Delivery address', 'intx', 32, INK, 'lm')
    c.pen.rr(180, 510, 900, 580, 12, fill=WHITE, outline=INK, w=3)
    c.pen.text(200, 545, '14, MG Road, Pune', 'ints', 28, INK, 'lm')
    tl = c.T('leave')
    c.pen.rr(180, 610, 900, 680, 12, fill=WHITE, outline=RED if c.on(tl) else INK, w=3)
    c.pen.text(200, 645, 'PIN: 4110', 'ints', 28, INK, 'lm')
    if c.on(tl): c.pen.text(900, 700, 'PIN must be 6 digits', 'int', 22, RED, 'rm')
    chaps(c, [('E19', 'React Hook Form · errors on blur', 'Hook'), ('E13', 'save → invalidate addresses', 'invalidates')], 840, 120)


def pay(c):
    homebar(c, {'MACHINE'})
    names = ['idle', 'paying', 'paid']
    tp = c.T('paying')
    cur = 0 if not c.on(c.T('Idle')) else (1 if c.on(tp) else 0)
    for k, nm in enumerate(names + ['failed']):
        x = 160 + k * 253
        lit = (k == cur)
        node(c, x, 520, 220, 110, nm, c.T('Idle') + k * 0.2, fill=YEL if lit else WHITE, size=32)
    td = c.T('double')
    if c.on(td):
        for k in range(3):
            if c.on(td + k * 0.25): c.pen.circ(413, 650, 30 + 25 * lin(c.t, td + k * 0.25, td + k * 0.25 + 0.3), outline=RED, w=4)
        label(c, 413, 720, 'SUBMIT ignored', td + 0.5, (200, 240, 200), INK, 28)
    chaps(c, [('E20', 'payment is a state machine', 'machine'), ('E20', 'double click: ignored', 'ignored')], 860, 120)


def track(c):
    homebar(c, {'SERVER'})
    tl = c.T('like')
    tf = c.T('fails')
    liked = c.on(tl + 0.1) and not c.on(tf + 0.4)
    heart(c.pen, 240, 520, 3.0, RED if liked else WHITE)
    c.pen.text(330, 520, 'Biryani House', 'intx', 40, INK, 'lm')
    if c.on(tf):
        c.pen.rr(330, 580, 900, 650, 30, fill=INK)
        c.pen.text(615, 615, "Couldn't save. Retry", 'int', 26, WHITE)
    chaps(c, [('E14', 'orders normalized by id', 'normalized'), ('E15', 'like: optimistic', 'instantly'), ('E16', 'failed? roll back + toast', 'rolls'),
              ('E21', 'updates written with Immer', 'Immer')], 760, 110)


SEASON = ['WHAT IS', '5 TYPES', 'COLOCATE', 'CONTEXT', 'IQ', 'REDUX', 'RTK', 'ZUSTAND', 'SELECTORS', 'IQ', 'SERVER', 'R. QUERY',
          'INVALIDATE', 'NORMALIZE', 'OPTIMISTIC', 'ROLLBACK', 'IQ', 'URL', 'FORMS', 'MACHINES', 'IMMER', 'IQ', 'FINALE']


def wrap_(c):
    tt = c.T('Twenty')
    season_map(c, SEASON, tt, 6, 340, 'FINALE', 0.05)
    tn = c.T('Next')
    if c.on(tn):
        darkcard(c.pen, 90, 790, 990, 1030)
        c.pen.text(540, 840, 'NEXT · SEASON 5', 'int', 32, YEL)
        c.pen.text(540, 920, 'DATA FETCHING & APIS', 'osw', 70 * c.B(tn, 0.4), WHITE)
        c.pen.text(540, 990, 'REST → GraphQL → race conditions', 'int', 30, (180, 186, 196))
    tc = c.T('Comment')
    if c.on(tc): pill(c.pen, 540, 1120, 'Comment NOTES for the full season cheat sheet', c.B(tc, 0.35), YEL, INK, 30)


SCENES = [
    (intro, "Season four finale. One food order, from search to doorstep, and every kind of state it touches."),
    (search, "You search for biryani, and tick pure veg. The query and the filter live in the URL, so a refresh or a shared link keeps them. Whether the sort dropdown is open is local state, colocated in its own component."),
    (menu, "The menu is server state. React Query caches it under the restaurant's key, so coming back is instant, and it refetches quietly in the background."),
    (cart, "You add two items. The cart is shared client state, in a small store. The badge selects just the count. And the total is derived, never stored."),
    (ctx, "The theme and the logged in user sit in context, because they rarely change."),
    (checkout, "At checkout, the address is form state, in React Hook Form, with errors shown once you leave a field. Saving it invalidates the addresses query, so every screen agrees."),
    (pay, "Pay is a state machine. Idle, paying, paid, or failed. A double click while paying is simply ignored."),
    (track, "The orders screen reads orders normalized by id. You like the restaurant, and the heart fills instantly. The request fails, so it rolls back, with a toast. And every update is written with Immer."),
    (wrap_, "Twenty three episodes. One order, and every piece of state in its right home. Next season: data fetching and APIs, from REST to race conditions. Comment NOTES for the full season cheat sheet."),
]
