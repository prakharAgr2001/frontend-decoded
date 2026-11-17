from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E21', tag='S5 · E21', short='FINALE: ONE SEARCH PAGE', tail=3.0)


def mini(c, stage):
    """small phone at the top showing the search page getting better"""
    inner = phone(c, 540, 600, 330, 520)
    x0, y0, x1, y1 = inner
    c.pen.rr(x0 + 14, y0 + 10, x1 - 14, y0 + 50, 20, fill=LIGHT, outline=GREY, w=2)
    c.pen.text(x0 + 30, y0 + 30, 'biryani', 'int', 20, INK, 'lm')
    for k in range(4):
        y = y0 + 70 + k * 92
        if stage >= 2: c.pen.rr(x0 + 14, y, x1 - 14, y + 80, 10, fill=WHITE, outline=INK, w=2); c.pen.circ(x0 + 50, y + 40, 22, fill=[ORANGE, GRN, BLUE, PURPLE][k])
        else: skel(c, x0 + 14, y, x1 - 14, y + 80, 10)
    return inner


def chaps(c, items, y0=930, gap=95):
    for i, (tag, name, kw) in enumerate(items):
        at = c.T(kw) if isinstance(kw, str) else kw
        chapter(c, 540, y0 + i * gap, tag, name, at)


def intro(c):
    stamp(c.cv, 540, 420, 'SEASON 5 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'ONE SEARCH PAGE.', 640, c.T('search'), 104)
    title(c, 'EVERY FIX.', 800, c.T('fix'), 120, hlcol=YEL)
    tf = c.T('fix')
    if c.on(tf): icon(c.pen, 'phone', 540, 1030, 1.6 * c.B(tf, 0.4))


def api(c):
    mini(c, 1)
    chaps(c, [('E01', 'REST: restaurants + dishes', 'REST'), ('E04', 'BFF: one call per screen', 'BFF')], 960, 110)


def listing(c):
    mini(c, 2)
    chaps(c, [('E06', 'no offset duplicates', 'duplicate'), ('E07', 'cursor pagination', 'cursor'), ('E08', 'infinite scroll + sentinel', 'Infinite')], 940, 100)


def typing(c):
    mini(c, 2)
    chaps(c, [('S3·E23', 'debounced typing', 'debounced'), ('E13', 'AbortController per keystroke', 'aborts'), ('E12', 'stale answers never win', 'win')], 940, 100)


def loading(c):
    mini(c, 2)
    chaps(c, [('E11', 'cards + offers + cart in parallel', 'parallel'), ('E10', 'no waterfall', 'waterfall')], 960, 110)


def resilience(c):
    mini(c, 2)
    chaps(c, [('E14', 'retries · backoff · jitter', 'jitter'), ('E15', 'one shared cart request', 'share'), ('E16', 'Retry-After respected', 'respected')], 940, 100)


def failure(c):
    mini(c, 2)
    chaps(c, [('E17', 'skeletons that match', 'Skeletons'), ('E18', 'offers fail alone', 'offers'), ('E19', 'Suspense in groups', 'Suspense')], 940, 100)


SEASON = ['REST', 'GRAPHQL', 'tRPC', 'BFF', 'IQ', 'OFFSET', 'CURSOR', 'INFINITE', 'IQ', 'WATERFALL', 'PARALLEL', 'RACES', 'ABORT', 'RETRIES',
          'DEDUP', '429', 'SKELETONS', 'PARTIAL', 'SUSPENSE', 'IQ', 'FINALE']


def wrap(c):
    tt = c.T('Twenty')
    season_map(c, SEASON, tt, 6, 340, 'FINALE', 0.05)
    tn = c.T('Next')
    if c.on(tn):
        darkcard(c.pen, 90, 790, 990, 1030)
        c.pen.text(540, 840, 'NEXT · SEASON 6', 'int', 32, YEL)
        c.pen.text(540, 920, 'REAL-TIME', 'osw', 80 * c.B(tn, 0.4), WHITE)
        c.pen.text(540, 990, 'polling → SSE → WebSockets → CRDTs', 'int', 30, (180, 186, 196))
    tc = c.T('Comment')
    if c.on(tc): pill(c.pen, 540, 1120, 'Comment NOTES for the full season cheat sheet', c.B(tc, 0.35), YEL, INK, 30)


SCENES = [
    (intro, "Season five finale. One food search page, and every fix from this season."),
    (api, "The API: REST resources for restaurants and dishes, behind a BFF that shapes one response for the mobile screen."),
    (listing, "Results never duplicate a row, because there's no offset. They use cursor pagination. Infinite scroll, with an observer sentinel."),
    (typing, "As you type, requests are debounced. Each new keystroke aborts the last request, so a stale answer can never win."),
    (loading, "Restaurant cards, offers, and the cart all load in parallel. No waterfall."),
    (resilience, "A flaky offers service gets retries, with backoff and jitter. Five components that need the cart share one request. And a four twenty nine gets its Retry After respected."),
    (failure, "Skeletons match the real cards. If offers fail, only that strip shows an error. And Suspense boundaries reveal the page in sensible groups."),
    (wrap, "Twenty one episodes. Every request accounted for. Next season: real time, from polling to WebSockets. Comment NOTES for the full season cheat sheet."),
]
