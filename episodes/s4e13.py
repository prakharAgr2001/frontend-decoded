from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E13', tag='S4 · E13', short='CACHE INVALIDATION', hook='why checkout still says Home')


def hook(c):
    ts = c.T('saved', 2)
    browser(c, 60, 380, 520, 900, url='/account')
    c.pen.text(90, 520, 'Saved address', 'intx', 30, INK, 'lm')
    c.pen.rr(90, 570, 490, 640, 12, fill=WHITE, outline=INK, w=3)
    c.pen.text(110, 605, typed_text(c, 'Office', c.T('Office'), 0.1) if c.on(c.T('Office')) else 'Home', 'ints', 30, INK, 'lm')
    if c.on(ts):
        c.pen.rr(90, 700, 330, 770, 35, fill=GRN)
        c.pen.text(210, 735, 'Saved', 'int', 30 * c.B(ts, 0.3), WHITE)
    tc = c.T('checkout')
    if c.on(tc):
        browser(c, 560, 380, 1020, 900, url='/checkout')
        c.pen.text(590, 520, 'Deliver to', 'intx', 30, INK, 'lm')
        c.pen.rr(590, 570, 990, 640, 12, fill=(255, 225, 225), outline=RED, w=3)
        c.pen.text(610, 605, 'Home', 'ints', 30, INK, 'lm')
    th = c.T('Home', 2)
    if c.on(th): stamp(c.cv, 540, 1030, 'OLD DATA', 90, c.P(th, 0.35), -4, RED); c.sfx(th, 'thud')


def quote(c):
    card(c.pen, 90, 400, 990, 780, 26, WHITE, 12, 5)
    txt(c, 540, 500, '"There are only two hard things', 0.2, 'intx', 42, INK)
    txt(c, 540, 570, 'in computer science:', 0.4, 'intx', 42, INK)
    ti = c.T('invalidation')
    if c.on(ti): hl(c.pen, 220, 615, 860, 690, c.P(ti, 0.4));
    txt(c, 540, 650, 'cache invalidation', ti, 'intx', 50, INK)
    txt(c, 540, 730, 'and naming things."', c.T('naming'), 'intx', 42, INK)
    txt(c, 540, 830, '— Phil Karlton', c.T('naming') + 0.6, 'ints', 30, MUTE)
    tm = c.T('means')
    if c.on(tm):
        darkcard(c.pen, 120, 960, 960, 1150)
        c.pen.text(540, 1020, 'invalidate =', 'int', 32, (180, 186, 196))
        c.pen.text(540, 1090, '"this data is out of date"', 'intx', 42, YEL)


def tag(c):
    title(c, 'THE RED STICKER', 330, 0.1, 100)
    card(c.pen, 300, 480, 780, 900, 20, WHITE, 10, 5)
    c.pen.text(540, 560, 'Basmati Rice 5 kg', 'intx', 36, INK)
    c.pen.text(540, 680, '₹649', 'osw', 110, INK)
    ts = c.T('sticker')
    if c.on(ts):
        stamp(c.cv, 640, 800, 'OLD', 64, c.P(ts, 0.35), 10, RED); c.sfx(ts, 'thud')
    tn = c.T('checks')
    if c.on(tn):
        node(c, 540, 1060, 520, 130, 'checks the real price', tn, ic=None, fill=(200, 240, 200), size=36)
    tk = c.T('keeps')
    if c.on(tk): label(c, 540, 1200, "the label isn't thrown away · just marked", tk, YEL, INK, 28)


def codes(c):
    title(c, 'invalidateQueries', 330, c.T('invalidate'), 88, hlcol=YEL)
    code(c, 30, 430, 1050, 830, ['const qc = useQueryClient();', 'const save = useMutation({', '  mutationFn: updateAddress,', '  onSuccess: () =>',
                                 "    qc.invalidateQueries({ queryKey: ['addresses'] }),", '});'],
         c.T('mutation'), 0.12, 26, 'AddressForm.jsx', marks=[(4, c.T('invalidate'), YEL)])
    rows(c, 90, 950, [(c.T('marks'), 'marks matching queries stale', None, ORANGE), (c.T('screen'), 'refetches the ones on screen now', None, GRN)], 140, 900, 110, 36)


def keys(c):
    title(c, 'KEYS ARE FOLDERS', 330, c.T('folders'), 100, hlcol=YEL)
    nodes = [('r', "['addresses']", 540, 500, None, c.T('prefix')), ('a', "['addresses','list']", 290, 680, 'r', c.T('list')),
             ('b', "['addresses', 7]", 790, 680, 'r', c.T('seven')), ('o', "['orders']", 540, 900, None, c.T('untouched'))]
    tree(c, nodes, 0, 0.1, lambda k: (255, 238, 170) if (k in 'rab' and c.on(c.T('list'))) else WHITE, 30)
    tu = c.T('untouched')
    if c.on(tu): label(c, 540, 990, 'untouched', tu, (200, 240, 200), INK, 28)
    te = c.T('exact')
    if c.on(te): label(c, 540, 1130, 'exact: true → only that one key', te, WHITE, INK, 30)


def setdata(c):
    title(c, 'OR SKIP THE REFETCH', 330, 0.1, 90, hlcol=YEL)
    code(c, 30, 430, 1050, 700, ['onSuccess: (saved) =>', "  qc.setQueryData(['addresses', saved.id], saved),"], c.T('returns'), 0.15, 28, 'AddressForm.jsx',
         marks=[(1, c.T('directly'), YEL)])
    a = node(c, 270, 900, 360, 150, 'server reply', c.T('returns'), ic='server', size=28)
    b = node(c, 810, 900, 360, 150, 'cache', c.T('directly'), ic='db', size=28, fill=(255, 238, 170))
    link(c, a, b, c.T('directly'))
    ts = c.T('saves')
    if c.on(ts): label(c, 540, 1090, 'saves a round trip', ts, (200, 240, 200), INK, 32)


def balance(c):
    title(c, 'TOO LITTLE VS TOO MUCH', 330, 0.1, 84)
    versus(c, ('TOO LITTLE', RED, c.T('little'), [(c.T('lie'), 'screens lie')]), ('TOO MUCH', ORANGE, c.T('much'), [(c.T('world'), 'refetch the world on every click')]),
           430, 760, 38)
    td = c.T('Design')
    if c.on(td):
        card(c.pen, 120, 880, 960, 1060, 24, WHITE, 10, 5)
        c.pen.text(540, 940, 'design keys like folders', 'intx', 42, INK)
        c.pen.text(540, 1010, 'invalidate the smallest folder that changed', 'ints', 30, MUTE)


def tabs(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Edit in one tab. How does the other update?', c.T('other'), 'intx', 40, INK)
    t1 = node(c, 250, 650, 300, 140, 'tab 1', c.T('own'), ic='laptop', sub='own cache', size=30)
    t2 = node(c, 830, 650, 300, 140, 'tab 2', c.T('own'), ic='laptop', sub='own cache', size=30)
    rows(c, 90, 860, [(c.T('focus'), 'refetch on window focus', 'covers most cases', 'ok'), (c.T('BroadcastChannel'), 'BroadcastChannel: tell other tabs', 'instant, same browser', BLUE),
                      (c.T('server', 1), 'push from the server', 'WebSocket / SSE (season 6)', PURPLE)], 150, 900, 125, 34, 26)
    tb = c.T('BroadcastChannel')
    if c.on(tb): packet(c, t1, t2, tb, tb + 1.0, YEL, 'invalidate')


SCENES = [
    (hook, "You change your saved address from Home to Office. The form says saved. Then you open checkout, and it still says Home."),
    (quote, "There's a famous line: there are only two hard things in computer science. Cache invalidation, and naming things. Invalidation means telling the cache: this data is out of date."),
    (tag, "It's like a shop putting a red sticker on a price tag. The label isn't thrown away. It keeps working. But the next customer who asks, the shopkeeper checks the real price."),
    (codes, "In React Query, after a mutation succeeds, you invalidate. This marks every matching query as stale, and refetches the ones on screen right now."),
    (keys, "Matching works by prefix. Keys are folders. Invalidate the addresses prefix, and both the addresses list, and address number seven, refetch. Orders stay untouched. Want only one key? Pass exact."),
    (setdata, "Or skip the refetch. If the server returns the saved object, write it into the cache directly with set query data. That saves a round trip."),
    (balance, "The balance is the hard part. Invalidate too little, and screens lie. Invalidate too much, and you refetch the world after every click. Design your keys like folders."),
    (tabs, "Interview question: the user edits in one tab. How does the other tab update? Each tab has its own cache. Refetch on window focus covers most cases. For instant sync, send a message with BroadcastChannel. Or push changes from the server."),
    (scene_next('S4 · E14', 'NORMALIZATION', 'one record per thing', 'normalization', 'record'),
     "Next: normalization. One record per thing, in your client. Comment NOTES for the cheat sheet."),
]
