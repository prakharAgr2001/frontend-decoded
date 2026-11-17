from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E17', tag='S6 · E17', short='OT vs CRDT')


def chars(c, cx, y, items, at, box=110, step=0.12, hi=None):
    """items: list of (char, id) drawn as boxes with ids under them"""
    n = len(items); x0 = cx - n * box / 2
    for i, (ch, cid) in enumerate(items):
        t = at + i * step
        if not c.on(t): continue
        p = c.B(t, 0.3); c.sfx(t, 'tick')
        x = x0 + i * box
        c.pen.rr(x + 5, y - 50 * p, x + box - 5, y + 50 * p, 12, fill=YEL if hi == i else WHITE, outline=INK, w=4)
        c.pen.text(x + box / 2, y, ch, 'monob', 56 * p, INK)
        c.pen.rr(x + 18, y + 62, x + box - 18, y + 100, 10, fill=INK)
        c.pen.text(x + box / 2, y + 81, cid, 'monob', 22, YEL)


def hook(c):
    x0, y0, x1, y1 = browser(c, 80, 330, 1000, 860, 'docs.google.com', dy=(1 - c.P(0, 0.45)) * 900)
    if c.t < 0.45: return
    to = c.T('offline')
    off = c.on(to) and not c.on(c.T('reconnect'))
    status(c, x0 + 50, y0 + 50, 'Working offline' if off else 'Saved to Drive', MUTE if off else GRN, 0.5, 30)
    for k in range(4): c.pen.line([(x0 + 60, y0 + 140 + k * 60), (x1 - 60 - (k % 2) * 160, y0 + 140 + k * 60)], LIGHT, 14)
    tf = c.T('flight')
    if c.on(tf): icon(c.pen, 'cloud', 900, 1000, 1.0); txt(c, 760, 1000, 'edits on a flight', tf, 'ints', 30, INK, 'rm')
    tm = c.T('merge')
    if c.on(tm): label(c, 540, 1110, 'your edits + everyone else\'s, merged', tm, (200, 240, 200), INK, 30)
    ti = c.T('ideas')
    if c.on(ti): stamp(c.cv, 540, 1250, 'OT  ·  CRDT', 76, c.P(ti, 0.35), -4, RED); c.sfx(ti, 'thud')


def ot(c):
    title(c, 'OPERATIONAL TRANSFORMATION', 330, c.T('Operational'), 64, hlcol=YEL)
    s = node(c, 540, 520, 300, 140, 'Server', c.T('central'), 'server', size=30)
    to = c.T('order')
    for k, (op, col) in enumerate((('1: insert h @1', (220, 235, 255)), ('2: insert ! @4', (220, 235, 255)))):
        if c.on(to + k * 0.3): pill(c.pen, 540, 690 + k * 80, op, c.B(to + k * 0.3, 0.3), col, INK, 30)
    ta = c.T('old')
    if c.on(ta): pill(c.pen, 540, 890, 'late: delete @2  (based on v0)', c.B(ta, 0.35), (255, 225, 235), INK, 30)
    tt = c.T('transforms')
    if c.on(tt):
        arrow(c.pen, 540, 930, 540, 1010, c.P(tt, 0.3), INK, 6)
        pill(c.pen, 540, 1060, 'becomes: delete @3', c.B(tt + 0.3, 0.35), YEL, INK, 34)


def referee(c):
    title(c, 'THE REFEREE', 330, c.T('referee'), 100, hlcol=YEL)
    for i in range(6):
        for j in range(6):
            col = (225, 215, 195) if (i + j) % 2 else WHITE
            c.pen.rect(300 + i * 80, 460 + j * 80, 380 + i * 80, 540 + j * 80, fill=col, outline=INK, w=2)
    c.pen.circ(460, 620, 28, fill=BLUE, outline=INK, w=4)
    tl = c.T('late')
    if c.on(tl):
        q = c.P(c.T('adjusting'), 0.6)
        x = 620 + 80 * q
        c.pen.circ(x, 780, 28, fill=ORANGE, outline=INK, w=4)
        if c.on(c.T('adjusting')): arrow(c.pen, 620, 840, 700, 840, q, INK, 5, 18)
    person(c.pen, 880, 1100, 1.0, INK)
    tc = c.T('current')
    if c.on(tc): label(c, 540, 1060, 'still makes sense on the current board', tc, YEL, INK, 30)


def crdt(c):
    title(c, 'CRDT', 330, c.T('CRDT'), 110, hlcol=YEL)
    tf = c.T('conflict')
    if c.on(tf): txt(c, 540, 440, 'Conflict-free Replicated Data Type', tf, 'intx', 40, INK)
    tu = c.T('unique')
    chars(c, 540, 600, [('c', 'a1'), ('a', 'a2'), ('t', 'b1')], tu)
    tp = c.T('point')
    if c.on(tp): label(c, 540, 790, 'insert "h" after a1', tp, (220, 235, 255), INK, 34)
    chars(c, 540, 940, [('c', 'a1'), ('h', 'c1'), ('a', 'a2'), ('t', 'b1')], c.T('shift'), hi=1, step=0.05)
    tn = c.T('never')
    if c.on(tn): label(c, 540, 1140, 'positions shift · ids never do', tn, YEL, INK, 34)


def anyorder(c):
    title(c, 'ANY ORDER, SAME RESULT', 330, c.T('order'), 76, hlcol=YEL)
    to = c.T('device')
    devs = [('laptop', 'laptop', 200), ('phone', 'phone', 540), ('tablet', 'laptop', 880)]
    boxes = []
    for k, (nm, ic, x) in enumerate(devs):
        boxes.append(node(c, x, 520, 220, 160, nm, to + k * 0.2, ic, size=30))
    tn = c.T('server')
    if c.on(tn):
        for i in range(3):
            for j in range(3):
                if i < j: link(c, boxes[i], boxes[j], tn + 0.2 * (i + j), col=MUTE, dash=True, off=0)
        txt(c, 540, 690, 'no server needed', tn, 'intx', 36, INK)
    ti = c.T('identical')
    if c.on(ti):
        for k, (_, _, x) in enumerate(devs):
            pill(c.pen, x, 860, 'chat!', c.B(ti + k * 0.15, 0.35), (200, 240, 200), INK, 36)
        check(c.pen, 540, 990, 1.6, GRN, 12, c.P(ti + 0.6, 0.3))


def guests(c):
    title(c, 'THE GUEST LIST', 330, c.T('guest'), 100, hlcol=YEL)
    tl = c.T('add')
    for k, (nm, removed) in enumerate((('Asha', False), ('Kabir', True), ('Riya', False), ('Dev', False))):
        t = tl + k * 0.3
        if not c.on(t): continue
        for side, x in enumerate((140, 600)):
            y = 490 + k * 90
            c.pen.text(x, y, nm, 'intx', 40, INK, 'lm')
            if removed and c.on(c.T('mark')):
                c.pen.text(x + 180, y, '(removed)', 'ints', 28, RED, 'lm')
    if c.on(tl):
        c.pen.text(300, 420, 'copy A', 'int', 28, MUTE); c.pen.text(760, 420, 'copy B', 'int', 28, MUTE)
    te = c.T('eraser')
    if c.on(te): txt(c, 540, 900, 'a mark, never an eraser', te, 'ints', 32, MUTE)
    tm = c.T('Merge')
    if c.on(tm): label(c, 540, 1040, 'merge in any order: the same list', tm, YEL, INK, 34)


def trade(c):
    versus(c, ('OT', BLUE, c.T('OT'), [(c.T('central'), 'needs a central server'), (c.T('lean'), 'lean documents'), (c.T('decades'), 'decades of practice')]),
           ('CRDT', GRN, c.T('CRDTs'), [(c.T('peer'), 'peer to peer + offline'), (c.T('metadata'), 'extra metadata'), (c.T('tombstones'), 'tombstones for deletes')]),
           400, 1060)
    tl = c.T('Yjs')
    if c.on(tl): label(c, 540, 1170, 'libraries: Yjs · Automerge', tl, YEL, INK, 34)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, 'Write your own merge algorithm?', c.T('write'), 'intx', 48, INK)
    th = c.T('Almost')
    if c.on(th): stamp(c.cv, 540, 600, 'ALMOST NEVER', 72, c.P(th, 0.35), -4, RED); c.sfx(th, 'thud')
    tf = c.T('famously')
    if c.on(tf): txt(c, 540, 730, 'edge cases are famously hard', tf, 'ints', 34, INK)
    tl = c.T('library')
    if c.on(tl): label(c, 540, 850, 'use a library: Yjs, Automerge', tl, (200, 240, 200), INK, 32)
    chips(c, 160, 1000, [('presence', LIGHT), ('cursors', LIGHT), ('undo', LIGHT)], c.T('presence'), 0.3, 34)


SCENES = [
    (hook, "In Google Docs, turn on offline mode, edit on a flight, and reconnect when you land. Your edits merge with everyone else's. Two big ideas make that possible: OT, and CRDTs."),
    (ot, "Operational transformation, or OT. A central server puts every operation in one order. When an operation arrives that was based on an old version, the server transforms it against the ones that got there first. Delete at two becomes delete at three."),
    (referee, "Think of a referee in a board game, adjusting a late move, so it still makes sense on the current board."),
    (crdt, "CRDT stands for conflict free replicated data type. Every character gets a unique, permanent id. Inserts point at ids, not positions: put h after the character with id a one. Positions shift. Ids never do."),
    (anyorder, "So operations can be applied in any order, on any device, even with no server at all, and every copy ends up identical."),
    (guests, "Think of a shared guest list, where people only ever add names, and a removal is a mark next to a name, never an eraser. Merge any two copies, in any order, and you get the same list."),
    (trade, "The trade offs. OT needs a central server, but keeps documents lean, with decades of practice behind it. CRDTs work peer to peer, and offline, but carry extra metadata, like tombstones for deleted characters. Libraries like Yjs and Automerge do the hard part."),
    (trap, "Interview trap: should you write your own merge algorithm? Almost never. The edge cases are famously hard. Use a library, and spend your time on presence, cursors, and undo."),
    (scene_next('S6 · E18', 'INTERVIEW QUESTIONS', 'presence and collaboration', 'interview', 'collaboration'),
     "Next: interview questions on presence and collaboration. Comment NOTES for the cheat sheet."),
]
