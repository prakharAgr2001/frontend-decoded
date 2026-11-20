from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E18', tag='S4 · E18', short='URL STATE', hook='why shared links lose filters')

FILTERS = [('Pure veg', 'veg'), ('Rating 4+', 'Rating'), ('< 30 min', 'thirty')]


def chipsrow(c, y, on_times):
    for k, (s_, _) in enumerate(FILTERS):
        x = 230 + k * 310
        on = on_times[k] is not None and c.on(on_times[k])
        c.pen.rr(x - 140, y - 36, x + 140, y + 36, 36, fill=GRN if on else WHITE, outline=INK, w=3)
        c.pen.text(x, y, s_, 'int', 28, WHITE if on else INK)


def hook(c):
    browser(c, 60, 360, 1020, 760, url='food.example.com/restaurants')
    chipsrow(c, 520, [c.T(kw) for _, kw in FILTERS])
    tf = c.T('friend')
    if c.on(tf):
        browser(c, 60, 860, 1020, 1260, url='food.example.com/restaurants')
        chipsrow(c, 1020, [None, None, None])
        label(c, 540, 1150, "friend's screen: unfiltered", tf + 0.5, (255, 210, 210), INK, 30)
    te = c.T('every')
    if c.on(te): stamp(c.cv, 800, 830, 'FILTERS LOST', 56, c.P(te, 0.35), -5, RED); c.sfx(te, 'thud')


def problem(c):
    title(c, 'STATE IN useState ONLY', 330, 0.1, 80)
    code(c, 30, 430, 1050, 640, ["const [veg, setVeg] = useState(false); // URL never changes"], c.T('lived'), 0.1, 22, 'Filters.jsx', marks=[(0, c.T('lived') + 0.4, YEL)])
    rows(c, 90, 760, [(c.T('Refresh'), 'refresh: filters gone', None, 'no'), (c.T('Back'), 'back button: leaves the page', None, 'no'),
                      (c.T('share'), "share a link: friend sees nothing", None, 'no')], 150, 900, 120, 38)


def define(c):
    title(c, 'URL STATE', 380, 0.1, 140, hlcol=YEL)
    tp = c.T('path')
    if c.on(tp):
        c.pen.rr(70, 520, 1010, 620, 50, fill=WHITE, outline=INK, w=4)
        s_ = '/restaurants?veg=1&rating=4&eta=30'
        c.pen.text(540, 570, s_, 'monob', 34, INK)
        hl(c.pen, 110, 600, 400, 612, c.P(tp, 0.4), BLUE)
        tq = c.T('query')
        if c.on(tq): hl(c.pen, 410, 600, 980, 612, c.P(tq, 0.4), ORANGE)
    rows(c, 90, 760, [(c.T('share'), 'share it', None, 'ok'), (c.T('bookmark'), 'bookmark it', None, 'ok'), (c.T('back'), 'go back to it', None, 'ok')], 140, 900, 110, 40)
    tb = c.T('belongs')
    if c.on(tb): label(c, 540, 1200, 'then it belongs in the URL', tb, YEL, INK, 36)


def book(c):
    title(c, 'A PAGE NUMBER', 330, 0.1, 110)
    card(c.pen, 180, 470, 900, 1000, 14, (255, 250, 235), 12, 5)
    c.pen.line([(540, 480), (540, 990)], (210, 200, 180), 3, False)
    for side in range(2):
        for k in range(8):
            x0 = 220 + side * 360
            c.pen.line([(x0, 540 + k * 50), (x0 + 280, 540 + k * 50)], (200, 192, 176), 6, False)
    tp = c.T('212')
    if c.on(tp):
        c.pen.text(720, 960, 'p. 212', 'monob', 30, INK)
        hl(c.pen, 580, 580, 880, 600, c.P(tp + 0.4, 0.4), YEL)
    tf = c.T('exactly')
    if c.on(tf): label(c, 540, 1090, 'say "page 212" · they land exactly there', tf, YEL, INK, 30)
    th = c.T('head')
    if c.on(th): label(c, 540, 1190, 'a place kept in your head: unshareable', th, (255, 210, 210), INK, 30)


def proof(c):
    title(c, 'WATCH THE ADDRESS BAR', 330, 0.1, 86)
    ta = c.T('filter')
    url = '/search?q=headphones'
    if c.on(c.T('sort')): url += '&sort=price'
    if c.on(c.T('page')): url += '&page=2'
    addressbar(c, 50, 440, 1030, url, cursor=False, size=34)
    for k, (kw, s_) in enumerate((('sort', 'sort by price'), ('page', 'page 2'))):
        label(c, 300 + k * 480, 640, s_, c.T(kw), WHITE, INK, 30)
    tr = c.T('Reload')
    if c.on(tr): label(c, 540, 760, 'reload or share → same results', tr, (200, 240, 200), INK, 32)
    ts = c.T('shopping')
    if c.on(ts): txt(c, 540, 880, 'any big shopping site · try it', ts, 'ints', 32, MUTE)


def codes(c):
    title(c, 'useSearchParams', 330, c.T('Read'), 96, hlcol=YEL)
    code(c, 30, 430, 1050, 830, ['const [params, setParams] = useSearchParams();', "const veg = params.get('veg') === '1';", 'function toggleVeg() {',
                                 "  setParams((p) => { p.set('veg', veg ? '0' : '1'); return p; });", '}'],
         c.T('Read'), 0.12, 23, 'Filters.jsx', marks=[(1, c.T('Read') + 0.4, YEL), (3, c.T('write'), YEL)])
    ts = c.T('single')
    if c.on(ts): label(c, 540, 920, 'the URL is the single source of truth', ts, YEL, INK, 32)
    tc = c.T('copy')
    if c.on(tc): label(c, 540, 1020, 'no useState copy to drift', tc, WHITE, INK, 30)


def history(c):
    title(c, 'PUSH VS REPLACE', 330, 0.1, 100, hlcol=YEL)
    tp = c.T('push')
    for k in range(3):
        x = 250 + k * 290
        node(c, x, 560, 240, 110, ['?veg=1', '&rating=4', '&eta=30'][k], tp + k * 0.3, size=28)
    if c.on(tp): label(c, 540, 680, 'push: back undoes each filter', tp + 0.9, (200, 240, 200), INK, 30)
    tt = c.T('typing')
    if c.on(tt):
        for k in range(8):
            t = tt + k * 0.12
            if c.on(t): c.pen.rr(90 + k * 115, 800, 190 + k * 115, 870, 12, fill=(255, 210, 210), outline=INK, w=3); c.pen.text(140 + k * 115, 835, f'#{k + 1}', 'monob', 26, INK)
        label(c, 540, 930, 'one history entry per keystroke', tt + 0.6, (255, 210, 210), INK, 30)
    tr = c.T('replace')
    if c.on(tr): label(c, 540, 1060, 'replace for keystrokes · push for committed choices', tr, YEL, INK, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, "What should NOT go in the URL?", c.T('shouldn'), 'intx', 46, INK)
    rows(c, 90, 600, [(c.T('Secrets'), 'secrets and personal data', 'URLs land in logs, history, referrers', 'no'), (c.T('Huge'), 'huge objects', None, 'no'),
                      (c.T('tooltip'), 'temporary UI (tooltip open?)', None, 'no')], 150, 900, 120, 36, 26)
    tv = c.T('validate')
    if c.on(tv): label(c, 540, 1100, 'URL values are strings: parse + validate', tv, YEL, INK, 32)


SCENES = [
    (hook, "You filter restaurants. Pure veg. Rating four plus. Under thirty minutes. You send the link to a friend. They open it, and see every restaurant, unfiltered."),
    (problem, "The filters lived in use state, and the URL never changed. Refresh, and they're gone. Back, and you leave the page. Share, and your friend sees nothing."),
    (define, "URL state is state you keep in the address bar: the path, and the query string. The rule: if someone should be able to share it, bookmark it, or go back to it, then it belongs in the URL."),
    (book, "It's like a page number in a book. Tell a friend page 212, and they land exactly where you are. A place you only keep in your head can't be shared."),
    (proof, "Try it on any big shopping site. Search, apply a filter, sort by price, go to page two, and watch the address bar. Reload or share it, and you get the same results."),
    (codes, "In React Router, use search params. Read the filter from the URL, and write it back to the URL. The URL becomes the single source of truth, with no use state copy to drift."),
    (history, "Each change can push a history entry, so back undoes one filter at a time. But typing in a search box would push one entry per keystroke. So use replace while typing, and push for committed choices."),
    (gotcha, "Interview trap: what shouldn't go in the URL? Secrets and personal data, because URLs end up in logs and history. Huge objects. And temporary UI, like whether a tooltip is open. And remember, anyone can edit a URL, so parse and validate every value."),
    (scene_next('S4 · E19', 'FORM STATE', 'controlled, uncontrolled, and the lag', 'form', 'lag'),
     "Next: form state. Controlled, uncontrolled, and why typing can lag. Comment NOTES for the cheat sheet."),
]
