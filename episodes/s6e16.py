from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E16', tag='S6 · E16', short='EDIT CONFLICTS')


def letters(c, cx, y, s, at, hi=None, hicol=YEL, gone=None, size=64, box=96, label_=None):
    """characters in index boxes, centred at cx; hi = index to highlight; gone = index to strike"""
    if not c.on(at - 0.01): return
    p = c.B(at, 0.35); c.sfx(at, 'pop')
    n = len(s); x0 = cx - n * box / 2
    if label_: c.pen.text(x0 - 30, y, label_, 'int', 30, MUTE, 'rm')
    for i, ch in enumerate(s):
        x = x0 + i * box
        fill = hicol if i == hi else WHITE
        c.pen.rr(x + 4, y - box / 2 * p, x + box - 4, y + box / 2 * p, 12, fill=fill, outline=INK, w=4)
        c.pen.text(x + box / 2, y, ch, 'monob', size * p, INK)
        c.pen.text(x + box / 2, y + box / 2 + 22, str(i), 'mono', 22, MUTE)
        if gone == i: cross(c.pen, x + box / 2, y, 1.1, RED, 9, c.P(at + 0.3, 0.3))


def hook(c):
    x0, y0, x1, y1 = browser(c, 80, 330, 1000, 980, 'docs.google.com', dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    for k in range(3): c.pen.line([(x0 + 60, y0 + 90 + k * 60), (x1 - 60 - k * 120, y0 + 90 + k * 60)], LIGHT, 14)
    base = 'Meet at the station at '
    ta, tk = c.T('cursor'), c.T('same')
    s_ = base + ('8 pm' if c.on(tk) else '')
    tail = ', near gate 2' if c.on(tk + 0.8) else ''
    c.pen.text(x0 + 60, y0 + 300, s_ + tail, 'intm', 34, INK, 'lm')
    w1 = c.pen.tw(s_, 'intm', 34); w2 = c.pen.tw(s_ + tail, 'intm', 34)
    caret(c, x0 + 60 + w1 + 4, y0 + 300, 'You', BLUE, 0.6, 50)
    caret(c, x0 + 60 + w2 + 4, y0 + 300, 'Asha', PINK, ta, 50)
    tl = c.T('lost')
    if c.on(tl): stamp(c.cv, 540, 1120, 'NOTHING LOST. HOW?', 64, c.P(tl, 0.35), -4, RED); c.sfx(tl, 'thud')


def naive(c):
    title(c, 'LAST SAVE WINS', 330, c.T('last'), 96, hlcol=YEL)
    ty, tf = c.T('add'), c.T('friend')
    node(c, 260, 560, 360, 140, 'cat + "black"', ty, size=32, fill=(220, 235, 255))
    node(c, 820, 560, 360, 140, 'cat + "fat"', tf, size=32, fill=(255, 225, 235))
    s = node(c, 540, 900, 380, 150, 'Server', ty, 'server', size=30)
    to = c.T('overwrites')
    link(c, (80, 490, 440, 630), s, to - 0.6, txt_='save 1')
    link(c, (640, 490, 1000, 630), s, to, txt_='save 2')
    if c.on(to + 0.4): label(c, 540, 1060, 'stored: "fat cat"', to + 0.4, WHITE, INK, 34)
    tg = c.T('gone')
    if c.on(tg): stamp(c.cv, 540, 1200, 'YOUR WORD IS GONE', 60, c.P(tg, 0.35), -4, RED); c.sfx(tg, 'thud')


def form(c):
    title(c, 'THE LAST FORM HANDED IN', 330, c.T('form'), 76, hlcol=YEL)
    for k, (col, nm) in enumerate(((BLUE, 'You'), (ORANGE, 'Friend'))):
        x = 300 + k * 480
        t = c.T('people') + k * 0.3
        if not c.on(t): continue
        card(c.pen, x - 150, 480, x + 150, 820, 10, WHITE, 8, 4)
        for j in range(4): c.pen.line([(x - 110, 540 + j * 60), (x + 110, 540 + j * 60)], LIGHT, 4)
        c.pen.text(x, 560 + k * 120, 'edited here', 'intx', 26, col)
        person(c.pen, x, 1010, 0.9, col)
    tk = c.T('keeps')
    if c.on(tk):
        q = c.P(tk, 0.5)
        cross(c.pen, 300, 650, 2.0, RED, 12, q)
        label(c, 780, 880, 'kept', tk, (200, 240, 200), INK, 30)
    tv = c.T('vanishes')
    if c.on(tv): label(c, 540, 1120, "the other person's edits vanish", tv, YEL, INK, 32)


def ops(c):
    title(c, 'SEND OPERATIONS', 330, c.T('operations'), 96, hlcol=YEL)
    tw = c.T('whole')
    if c.on(tw):
        pill(c.pen, 540, 500, 'PUT /doc  (all 40 pages)', c.B(tw, 0.35), (255, 210, 210), INK, 32)
        cross(c.pen, 270, 500, 1.0, RED, 8, c.P(tw + 0.3, 0.3))
    ti = c.T('insert')
    code(c, 60, 590, 1020, 760, ["{ op: 'insert', pos: 1, text: 'h' }"], ti, 0.1, 32, 'operation', dy=(1 - c.P(ti - 0.45, 0.45)) * 900)
    ts = c.T('Small')
    if c.on(ts): rows(c, 100, 900, [(ts, 'Tiny on the wire', None, 'ok'), (c.T('combined'), 'Can be combined and reordered', None, 'ok')], gap=140)


def clash(c):
    head(c, 'POSITIONS SHIFT', 'shift', col=INK, y=330)
    letters(c, 540, 480, 'cat', c.T('cat'), label_='start')
    letters(c, 540, 660, 'chat', c.T('insert'), hi=1, label_='you')
    tf = c.T('friend')
    if c.on(tf): label(c, 540, 790, 'friend: delete pos 2 (the t)', tf, (255, 225, 235), INK, 32)
    tb = c.T('blindly')
    letters(c, 540, 940, 'chat', tb, hi=2, hicol=(255, 210, 210), gone=2, label_='apply')
    tw = c.T('Wrong')
    letters(c, 540, 1140, 'cht', c.T('get'), label_='result')
    if c.on(tw): stamp(c.cv, 880, 1140, 'WRONG', 56, c.P(tw, 0.35), 6, RED); c.sfx(tw, 'thud')


def fix(c):
    title(c, 'ADJUST FOR WHAT CAME FIRST', 330, c.T('adjust'), 70, hlcol=YEL)
    tp = c.T('pushed')
    if c.on(tp): label(c, 540, 470, 'your insert at 1 shifts everything right', tp, WHITE, INK, 30)
    tm = c.T('moves')
    if c.on(tm):
        pill(c.pen, 330, 580, 'delete 2', c.B(tm, 0.35), (255, 225, 235), INK, 36)
        arrow(c.pen, 470, 580, 620, 580, c.P(tm + 0.2, 0.3), INK, 6)
        pill(c.pen, 760, 580, 'delete 3', c.B(tm + 0.4, 0.35), YEL, INK, 36)
    letters(c, 540, 760, 'chat', c.T('Now'), hi=3, hicol=(255, 210, 210), gone=3)
    letters(c, 540, 960, 'cha', c.T('both'))
    tb = c.T('both')
    if c.on(tb + 0.3): check(c.pen, 800, 960, 1.4, GRN, 11, c.P(tb + 0.3, 0.3))
    tn = c.T('name')
    if c.on(tn): label(c, 540, 1140, 'it has a name: episode seventeen', tn, YEL, INK, 32)


def version(c):
    title(c, 'FOR FORMS: A VERSION CHECK', 330, c.T('forms'), 72, hlcol=YEL)
    tv = c.T('version')
    code(c, 40, 430, 1040, 900, ["const res = await fetch('/api/profile', {", "  method: 'PUT',", "  headers: { 'If-Match': etag },", '  body: JSON.stringify(form),',
                                 '});', 'if (res.status === 412) showConflict();'], tv, 0.1, 28, 'save.js',
         marks=[(2, c.T('started'), YEL), (5, c.T('conflict'), YEL)])
    to = c.T('optimistic')
    if c.on(to): label(c, 540, 1010, 'optimistic concurrency: no locks', to, WHITE, INK, 34)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Why not lock the document?', c.T('lock'), 'intx', 52, INK)
    th = c.T('hate')
    if c.on(th): stamp(c.cv, 540, 600, 'USERS HATE IT', 72, c.P(th, 0.35), -4, RED); c.sfx(th, 'thud')
    tf = c.T('forgets')
    if c.on(tf):
        icon(c.pen, 'lock', 540, 790, 1.4 * c.B(tf, 0.35))
        txt(c, 540, 900, 'one forgotten tab blocks everyone', tf + 0.3, 'ints', 34, INK)
    tl = c.T('Locks')
    if c.on(tl): rows(c, 100, 1040, [(tl, 'Locks: forms, tickets', None, 'ok'), (c.T('live'), 'Not live text', None, 'no')], gap=130, h=100)


SCENES = [
    (hook, "Share a Google Doc, and type with a friend. Her cursor shows up in color, with her name. You both type in the same sentence, at the same time, and nothing gets lost. How?"),
    (naive, "The naive approach: each client sends the whole document, and the last save wins. You add a word. Your friend adds a word. The later save overwrites yours, and your word is gone."),
    (form, "It's like two people filling in the same paper form, while the office keeps only the last copy handed in. Whatever the other person wrote, vanishes."),
    (ops, "Better: send operations, not documents. Not: here's the whole doc again. But: insert the letter h, at position one. Small, and they can be combined."),
    (clash, "But positions shift under you. The text is cat. You insert h at position one: chat. At the same moment, your friend deletes position two, the t. Apply that blindly to chat, and it deletes the a instead. You get c, h, t. Wrong."),
    (fix, "The fix is to adjust each operation for what happened first. Your insert pushed everything right by one, so the delete moves to position three. Now both sides end up with cha. That adjustment has a name. Next episode."),
    (version, "For simple forms, there's a cheaper trick: a version number. Save only if the version you started from is still current. If not, the server answers with a conflict, and you merge, or ask the user. That's optimistic concurrency."),
    (trap, "Interview trap: why not just lock the document while someone edits? It works, and users hate it. One person forgets a tab open, and everyone is blocked. Locks fit forms and tickets, not live text."),
    (scene_next('S6 · E17', 'OT vs CRDT', 'two ways to merge edits', 'OT', 'merge'),
     "Next: OT versus CRDT, two ways to merge everyone's edits. Comment NOTES for the cheat sheet."),
]
