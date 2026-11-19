from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E23', tag='S3 · E23', short='DEBOUNCE', hook='stop firing on every keystroke')

WORD = 'running shoes'

def hook(c):
    tt = c.T('type')
    addressbar(c, 110, 380, 970, typed_text(c, WORD, tt, 0.12), True, 44, 96, 'Search')
    tk = c.T('Thirteen')
    if c.on(tt):
        n = min(len(WORD), int((c.t - tt) / 0.12) + 1)
        for k in range(n):
            x = 130 + (k % 7) * 122; y = 560 + (k // 7) * 90
            c.pen.rr(x, y, x + 110, y + 70, 10, fill=(255, 225, 190), outline=INK, w=3)
            c.pen.text(x + 55, y + 35, 'GET', 'monob', 24, INK)
            if c.on(c.T('wasted')) and k < n - 1: cross(c.pen, x + 55, y + 35, 0.8, RED, 6, c.P(c.T('wasted'), 0.3))
    if c.on(tk): counter(c, 540, 860, 0, 13, tk, tk + 0.8, '{:.0f}', 100, RED, ' requests')
    to = c.T('order')
    if c.on(to): stamp(c.cv, 540, 1060, 'AND OUT OF ORDER', 64, c.P(to, 0.35), -3, RED); c.sfx(to, 'thud')

def define(c):
    title(c, 'DEBOUNCE', 330, c.T('Debounce'), 120, hlcol=YEL)
    tr = c.T('resets')
    if c.on(tr):
        for k in range(5):
            t = tr + k * 0.35
            if not c.on(t): continue
            x = 140 + k * 90
            c.pen.line([(x, 520), (x, 600)], INK, 6); c.sfx(t, 'click')
            if k < 4 and c.on(t + 0.35): c.pen.rect(x, 640, x + 80, 670, fill=(230, 220, 205), outline=GREY, w=2)
        c.pen.text(140, 490, 'keystrokes', 'int', 28, INK, 'lm')
    tp = c.T('pauses')
    if c.on(tp):
        p = c.P(tp, 1.0, lambda x: x)
        c.pen.rect(500, 640, 500 + 400 * p, 670, fill=YEL, outline=INK, w=3)
        c.pen.text(700, 720, '300 ms of quiet', 'ints', 30, INK)
    to = c.T('once')
    if c.on(to):
        node(c, 900, 880, 220, 110, 'search()', to, fill=(200, 240, 200))
        stamp(c.cv, 450, 900, 'RUNS ONCE', 64, c.P(to, 0.35), -4, GRN)

def photo(c):
    title(c, 'THE GROUP PHOTO', 330, 0.1, 100)
    tm = c.T('moving')
    still = c.on(c.T('stop'))
    for k in range(5):
        dx = 0 if still else 14 * math.sin(c.t * 9 + k * 1.7)
        person(c.pen, 260 + k * 140 + dx, 900, 1.3, [BLUE, ORANGE, GRN, PURPLE, TEAL][k])
    icon(c.pen, 'eye', 540, 1080, 1.2)
    ts = c.T('stop')
    if c.on(ts):
        c.pen.rect(140, 560, 940, 960, outline=YEL, w=10)
        if c.on(c.T('click')): c.sfx(c.T('click'), 'ding'); c.pen.rect(140, 560, 940, 960, fill=None, outline=WHITE, w=int(18 * (1 - c.P(c.T('click'), 0.4))) + 1)
    to = c.T('one')
    if c.on(to): label(c, 540, 1200, 'one photo, after the movement stops', to, YEL, INK, 32)

def code_(c):
    code(c, 40, 330, 1040, 830, ['function debounce(fn, wait) {', '  let timer;', '  return (...args) => {', '    clearTimeout(timer);',
                                 '    timer = setTimeout(() => fn(...args), wait);', '  };', '}'], c.T('closure') - 0.6, 0.1, 27, 'debounce.js',
         marks=[(3, c.T('cancels'), (120, 60, 60)), (4, c.T('fresh'), YEL)])
    code(c, 40, 900, 1040, 1060, ["input.addEventListener('input', debounce(search, 300));"], c.T('wire'), 0.1, 25, 'search.js')

def where(c):
    title(c, 'WHEN ONLY THE LAST VALUE MATTERS', 330, c.T('final'), 64)
    for k, (nm, kw, ic) in enumerate((('search box', 'search', 'eye'), ('auto-save', 'save', 'doc'), ('window resize', 'resize', 'laptop'))):
        t = c.T(kw)
        node(c, 540, 520 + k * 230, 600, 170, nm, t, ic)

def proof(c):
    panel(c, 50, 330, 1030, 1150, tabs=('Network', 'Fetch/XHR'), dy=(1 - c.P(0, 0.45)) * 900)
    tb = c.T('Before')
    if c.on(tb):
        c.pen.text(100, 470, 'before', 'intx', 34, RED, 'lm')
        for k in range(13):
            if c.on(tb + k * 0.06): c.pen.rect(100 + k * 68, 510, 155 + k * 68, 560, fill=RED)
    ta = c.T('After')
    if c.on(ta):
        c.pen.text(100, 680, 'after debounce', 'intx', 34, GRN, 'lm')
        for k, x in enumerate((420, 980)):
            if c.on(ta + k * 0.4): c.pen.rect(x - 55, 720, x, 770, fill=GRN)
        txt(c, 540, 900, 'one request per pause', ta + 0.4, 'intx', 40, WHITE)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Debounce fixes race conditions, right?', c.T('race'), 'intx', 44, INK)
    ts = c.T('slow')
    if c.on(ts):
        axis(c, 140, 940, 680, ts, [(0.1, '"run" sent', ts, GREY), (0.58, '"running shoes" sent', ts + 0.3, BLUE)], labels_up=True)
        axis(c, 140, 940, 820, ts + 0.6, [(0.45, 'shoes arrives', ts + 0.6, BLUE), (0.88, '"run" arrives', c.T('after'), RED)], labels_up=False)
    tw = c.T('wrong')
    if c.on(tw): stamp(c.cv, 540, 1010, 'WRONG RESULTS', 66, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')
    ta = c.T('AbortController')
    if c.on(ta): label(c, 540, 1160, 'fix: AbortController or ignore stale responses', ta, (200, 240, 200), INK, 30)

SCENES = [
    (hook, "You type running shoes into a search box. Thirteen keystrokes, thirteen requests. Twelve of them were wasted, and they can even come back out of order."),
    (define, "Debounce waits until the user stops. Every keystroke resets a timer. Only when typing pauses for, say, three hundred milliseconds, does the function finally run. Once."),
    (photo, "It's like a photographer taking a group photo. While people keep moving, they wait. Only when everyone stops, they click. One photo."),
    (code_, "The code is a small closure. Each call cancels the pending timer, and starts a fresh one. Then wire it to the input."),
    (where, "Use it wherever only the final value matters. A search box. Form auto save. A window resize handler."),
    (proof, "Try it on your own search box with the Network panel open. Before: one request per key. After: one request per pause."),
    (gotcha, "Interview trap: debounce fixes race conditions, right? Not fully. If a slow response for run arrives after the one for running shoes, you still show the wrong results. Cancel the old request with an AbortController, or ignore stale responses."),
    (scene_next('S3 · E24', 'THROTTLE', 'at most once every N ms', 'throttle', 'once'),
     "Next: throttle, the cousin of debounce, that runs at most once every few milliseconds. Comment NOTES for the cheat sheet."),
]
