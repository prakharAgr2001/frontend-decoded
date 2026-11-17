from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E14', tag='S4 · E14', short='NORMALIZATION')


def hook(c):
    tc = c.T('changes')
    new = c.on(tc + 0.4)
    card(c.pen, 90, 380, 990, 560, 22, WHITE, 10, 5)
    c.pen.circ(170, 470, 50, fill=(200, 215, 245), outline=INK, w=4)
    c.pen.text(250, 450, 'Riya Sharma' if not new else 'Riya Kapoor', 'intx', 40, INK, 'lm')
    c.pen.text(250, 505, 'profile', 'intm', 26, MUTE, 'lm')
    if new: flash_box(c, (90, 380, 990, 560), tc + 0.4, GRN, 1.0)
    tm = c.T('comments')
    for k in range(3):
        y = 680 + k * 170
        if not c.on(tm + k * 0.2): continue
        card(c.pen, 150, y - 65, 990, y + 65, 18, WHITE, 8, 4)
        c.pen.text(190, y - 20, 'Riya Sharma', 'int', 30, RED if c.on(c.T('old', 2)) else INK, 'lm')
        c.pen.text(190, y + 25, ['Loved the biryani!', 'Order arrived cold.', 'Best chai in town'][k], 'intm', 26, MUTE, 'lm')
    to = c.T('old', 2)
    if c.on(to): stamp(c.cv, 540, 1250, 'STILL THE OLD NAME', 64, c.P(to, 0.35), -3, RED); c.sfx(to, 'thud')


def nested(c):
    title(c, 'NESTED DATA', 330, 0.1, 110, hlcol=YEL)
    code(c, 30, 430, 1050, 1000, ['posts: [', "  { id: 101, author: { id: 7, name: 'Riya' } },", "  { id: 102, author: { id: 7, name: 'Riya' } },",
                                  "  { id: 103, author: { id: 7, name: 'Riya' } },", ']'],
         c.T('copy'), 0.2, 24, 'cache', circles=[(1, c.T('every'), "name: 'Riya'"), (2, c.T('every') + 0.3, "name: 'Riya'"), (3, c.T('every') + 0.6, "name: 'Riya'")])
    tu = c.T('update')
    if c.on(tu): label(c, 540, 1090, 'rename = find and update every copy', tu, (255, 210, 210), INK, 32)


def define(c):
    title(c, 'NORMALIZE', 360, 0.1, 140, hlcol=YEL)
    rows(c, 90, 560, [(c.T('once'), 'store each entity once', None, 'ok'), (c.T('keyed'), 'in a table keyed by id', None, 'ok'),
                      (c.T('point'), 'everything else points to the id', None, 'ok')], 150, 900, 120, 40)
    td = c.T('database')
    if c.on(td): label(c, 540, 1060, 'a tiny database inside your client', td, YEL, INK, 34)


def school(c):
    title(c, 'THE SCHOOL OFFICE', 330, 0.1, 100)
    f = node(c, 540, 560, 520, 200, 'Roll 23 · Riya', c.T('file'), ic='doc', sub='phone: 98xxx', fill=(255, 238, 170), size=36)
    sheets = []
    for k, nm in enumerate(('attendance', 'marks', 'bus list')):
        t = c.T(['attendance', 'marks', 'bus'][k])
        b = node(c, 200 + k * 340, 960, 280, 150, nm, t, sub='roll 23', size=32)
        sheets.append(b)
        link(c, b, f, t + 0.2, dash=True)
    tc = c.T('Change')
    if c.on(tc): flash_box(c, f, tc, GRN, 1.2)
    te = c.T('every')
    if c.on(te):
        for b in sheets: check(c.pen, b[2] - 30, b[1] + 30, 0.6, GRN, 6, c.P(te, 0.3))


def shape(c):
    title(c, 'THE SHAPE', 330, 0.1, 110, hlcol=YEL)
    code(c, 30, 430, 1050, 920, ['{', '  users: {', "    byId: { 7: { id: 7, name: 'Riya' } },", '    allIds: [7],', '  },', '  posts: {',
                                 "    byId: { 101: { id: 101, author: 7 } },", '  },', '}'],
         c.T('users'), 0.1, 26, 'store', marks=[(2, c.T('stored'), YEL), (6, c.T('author'), YEL)])
    to = c.T('rename')
    if c.on(to): label(c, 540, 1010, 'rename = one write: users.byId[7].name', to, (200, 240, 200), INK, 30)
    tl = c.T('lookup')
    if c.on(tl): label(c, 540, 1110, 'O(1) lookup by id', tl, WHITE, INK, 30)


def tools(c):
    title(c, 'WHO DOES IT FOR YOU', 330, 0.1, 90)
    rows(c, 90, 500, [(c.T('createEntityAdapter'), 'RTK createEntityAdapter', 'byId + ids + CRUD helpers', ORANGE),
                      (c.T('Apollo'), 'Apollo / Relay (GraphQL)', 'auto: __typename + id', PURPLE),
                      (c.T('React'), "React Query: doesn't normalize", 'caches per query · invalidate instead', BLUE)], 180, 900, 140, 38, 26)
    tw = c.T('often')
    if c.on(tw): label(c, 540, 1080, 'normalize when one entity shows up in many places', tw, YEL, INK, 28)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Why normalize client state?', c.T('normalize'), 'intx', 50, INK)
    rows(c, 90, 620, [(c.T('truth'), 'one source of truth per entity', None, 'ok'), (c.T('place'), 'updates touch one place', None, 'ok'),
                      (c.T('lookups'), 'fast lookups by id', None, 'ok'), (c.T('spreads'), 'no deep nested spreads', None, 'ok')], 140, 900, 110, 36)


SCENES = [
    (hook, "On a food app, a user changes her name. Her profile updates. But scroll down to her old comments, and they still show the old name."),
    (nested, "The data came back nested. Every post carries its own copy of the author. Three posts, three copies. To rename her, you have to find and update every copy."),
    (define, "The fix is normalizing. Store each entity once, in a table keyed by its id. And everything else just points to that id. It's a tiny database inside your client."),
    (school, "Think of a school office. Each student has one file, under a roll number. The attendance sheet, the marks sheet, the bus list only write the roll number. Change the phone number in the file, and every sheet is right."),
    (shape, "Here's the shape. Users, stored by id. Posts store the author's id, not the author. A rename is now one write. And any lookup by id is instant."),
    (tools, "You rarely do this by hand. Redux Toolkit has createEntityAdapter. GraphQL clients like Apollo normalize automatically, using type name and id. React Query doesn't normalize at all. It caches per query, and you invalidate instead. Normalize when one entity shows up in many places, and changes often."),
    (gotcha, "Interview question: why normalize client state? One source of truth per entity. Updates touch one place. Lookups by id are fast. And reducers avoid deep nested spreads."),
    (scene_next('S4 · E15', 'OPTIMISTIC UI', 'heart first · server later', 'optimistic', 'heart'),
     "Next: optimistic UI, and why the heart fills before the server even answers. Comment NOTES for the cheat sheet."),
]
