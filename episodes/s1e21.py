from engine.lib import *

EP = dict(id='S1E21', tag='S1 · E21', short='EVENT DELEGATION')

def inbox(c, y0=330, rows=8, ears=False, one=False, new_at=None):
    card(c.pen, 110, y0, 970, y0 + 90 + rows * 90, 24, WHITE, 10, 5)
    c.pen.text(150, y0 + 45, 'Inbox', 'intx', 36, INK, 'lm')
    for i in range(rows):
        y = y0 + 90 + i * 90
        isnew = new_at is not None and i == 0
        if isnew and not c.on(new_at): continue
        c.pen.line([(130, y), (950, y)], LIGHT, 3, False)
        c.pen.circ(170, y + 45, 18, fill=[BLUE, ORANGE, GRN, PURPLE][i % 4])
        c.pen.text(210, y + 32, ['Swiggy', 'Bank', 'GitHub', 'Mom', 'Flipkart', 'LinkedIn', 'IRCTC', 'Team'][i % 8] + ('  · NEW' if isnew else ''), 'int', 26, INK, 'lm')
        c.pen.rect(210, y + 55, 620, y + 65, fill=LIGHT)
        if ears and not (isnew):
            c.pen.circ(920, y + 45, 16, fill=YEL, outline=INK, w=3)
    if one:
        c.pen.circ(930, y0 + 45, 26, fill=YEL, outline=INK, w=4); c.pen.text(930, y0 + 45, '1', 'osw', 30, INK)

def hook(c):
    inbox(c, ears=c.on(c.T('thousand')))
    tt = c.T('thousand')
    if c.on(tt): stamp(c.cv, 540, 1230, '× 1,000 LISTENERS?', 64, c.P(tt, 0.35), -3, RED)
    to = c.T('One')
    if c.on(to): label(c, 540, 1320, 'one is enough', to, GRN, WHITE, 34)

def problem(c):
    tn = c.T('new')
    inbox(c, ears=True, new_at=tn)
    tm = c.T('memory')
    if c.on(tm): label(c, 540, 1240, 'memory + setup time × every row', tm, RED, WHITE, 30)
    td = c.T('nothing')
    if c.on(td):
        c.pen.circ(700, 465, 26, fill=YEL, outline=INK, w=4)
        stamp(c.cv, 770, 380, 'CLICK = NOTHING', 40, c.P(td, 0.3), -4, RED)

def deleg(c):
    tp = c.T('parent')
    inbox(c, one=c.on(tp))
    tb = c.T('bubbling')
    if c.on(tb):
        q = lin(c.t, tb, tb + 1.0)
        y = 690 - q * 300
        c.pen.circ(400, 690, 24, fill=YEL, outline=INK, w=4)
        arrow(c.pen, 430, 680, 900, 400, q, ORANGE, 6, 22)
    tc = c.T('check')
    if c.on(tc): label(c, 540, 1240, 'then check where it came from', tc, YEL, INK, 32)

def codeit(c):
    code(c, 40, 330, 1040, 760, ["list.addEventListener('click', (e) => {", "  const row = e.target.closest('.row');", "  if (!row) return;",
                                 "  open(row.dataset.id);", "});"], 0.1, 0.2, 28, 'inbox.js', marks=[(1, c.T('closest'), YEL)])
    tc = c.T('closest')
    if c.on(tc): txt(c, 540, 860, 'closest() climbs from the clicked text to its row', tc + 0.3, 'int', 34, INK)

def reception(c):
    node(c, 540, 470, 400, 220, 'Front desk', c.T('receptionist'), 'chef', fill=(255, 246, 214), sub='one receptionist')
    tg = c.T('guard')
    for k in range(6):
        x = 160 + k * 152
        c.pen.rr(x - 60, 820, x + 60, 1000, 10, fill=WHITE, outline=INK, w=4)
        c.pen.text(x, 1030, f'room {k + 1}', 'int', 24, INK)
        if c.on(tg + k * 0.1):
            person(c.pen, x, 940, 0.45, RED)
            cross(c.pen, x, 760, 0.7, RED, 7, c.P(tg + 0.6, 0.3))

def benefits(c):
    for i, (s_, kw) in enumerate([('1 listener, not 1,000', 'listener'), ('rows added later just work', 'later'), ("removed rows can't leak listeners", 'leak')]):
        at = c.T(kw); y = 470 + i * 220
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.4)
        card(c.pen, 110, y - 80 * s, 970, y + 80 * s, 22, WHITE, 10, 5)
        check(c.pen, 200, y, 1.4 * s, GRN, 12)
        c.pen.text(270, y, s_, 'intx', 42 * s, INK, 'lm')

def proof(c):
    panel(c, 60, 330, 1020, 1000, tabs=('Styles', 'Event Listeners'), active=1, dy=(1 - c.P(0, 0.45)) * 900)
    ta = c.T('Ancestors')
    c.pen.rr(100, 460, 136, 496, 6, fill=YEL if c.on(ta) else None, outline=WHITE, w=3)
    if c.on(ta): check(c.pen, 118, 478, 0.5, INK, 5)
    c.pen.text(150, 478, 'Ancestors', 'int', 30, WHITE, 'lm')
    rows = [('▾ click', CYAN), ('   ul.inbox-list  ← the real listener', (120, 220, 150)), ('▾ scroll', CYAN), ('   window', WHITE)]
    for i, (s_, col) in enumerate(rows):
        if c.on(ta + 0.3 + i * 0.2): c.pen.text(100, 580 + i * 80, s_, 'mono', 30, col, 'lm')
    tr = c.T('parent')
    if c.on(tr): c.pen.rr(80, 610, 1000, 690, 10, outline=YEL, w=4)

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW TRAP', 84, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    node(c, 290, 600, 380, 220, 'needs bubbling', c.T('bubble'), None, sub='focus / mouseenter won’t work', size=36)
    ts = c.T('stopPropagation')
    if c.on(ts):
        node(c, 790, 600, 380, 220, 'stopPropagation', ts, None, fill=(255, 225, 225), sub='parent never hears it', size=36)
        arrow(c.pen, 790, 1000, 790, 760, c.P(ts + 0.3, 0.4), RED, 6, 22); cross(c.pen, 790, 860, 1.2, RED, 10, c.P(ts + 0.7, 0.3))

SCENES = [
    (hook, "An inbox with a thousand emails. Do you attach a thousand click listeners? You don't have to. One is enough."),
    (problem, "A listener on every row costs memory and setup time. And every new email that arrives needs its own listener, or clicking it does nothing."),
    (deleg, "Event delegation: put one listener on the parent. Thanks to bubbling, every click inside reaches it. Then check where the click came from."),
    (codeit, "The trick is closest. It climbs up from whatever was clicked, even the subject text, to the row that contains it."),
    (reception, "It's one receptionist at the front desk, instead of a security guard outside every room."),
    (benefits, "One listener. Rows added later just work. And removing rows can't leak listeners."),
    (proof, "In DevTools, select an element and open Event Listeners. Tick Ancestors, and you'll often find the real listener sitting on a parent."),
    (gotcha, "Interview trap: delegation only works for events that bubble. And if a child calls stopPropagation, the parent never hears it."),
    (scene_next('S1 · E22', 'MEMORY LEAKS', 'why some tabs eat gigabytes', 'memory', 'gigabytes'),
     "Next: memory leaks, and why some tabs eat gigabytes. Comment NOTES for the cheat sheet."),
]
