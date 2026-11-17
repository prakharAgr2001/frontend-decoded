from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *
from episodes.s4e15 import post

EP = dict(id='S4E16', tag='S4 · E16', short='ROLLBACK')


def hook(c):
    tl = c.T('like')
    tf = c.T('fails')
    liked = c.on(tl + 0.1)
    post(c, 540, 800, liked, 1205 if liked else 1204, pop=tl + 0.1)
    if c.on(tf):
        darkcard(c.pen, 200, 1220, 880, 1320)
        c.pen.text(540, 1270, 'POST /like  →  500', 'monob', 34 * c.B(tf, 0.3), RED); c.sfx(tf, 'buzz')
    tw = c.T('lying')
    if c.on(tw): stamp(c.cv, 540, 330, 'THE SCREEN IS LYING', 70, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')


def eraser(c):
    title(c, 'THE ERASER', 330, 0.1, 110)
    card(c.pen, 160, 450, 920, 900, 18, (255, 250, 235), 10, 5)
    for k in range(5): c.pen.line([(190, 540 + k * 70), (890, 540 + k * 70)], (220, 210, 190), 2, False)
    c.pen.text(200, 500, 'FRIDAY', 'osw', 36, INK, 'lm')
    te = c.T('erase')
    a = 1 - c.P(te, 0.9) if c.on(te) else 1
    if a > 0: c.pen.text(220, 680, '4 pm · coffee with Arjun', 'intx', 40, mix((255, 250, 235), GREY, a), 'lm')
    if c.on(te) and c.t < te + 1.0:
        x = 220 + 600 * lin(c.t, te, te + 0.9)
        c.pen.rr(x - 50, 640, x + 50, 720, 12, fill=PINK, outline=INK, w=4)
    tr = c.T('Rollback')
    if c.on(tr): label(c, 540, 1000, 'rollback = put back what was there', tr, YEL, INK, 34)


def snapshot(c):
    title(c, 'SNAPSHOT · RESTORE · REFETCH', 330, 0.1, 70, hlcol=YEL)
    code(c, 30, 420, 1050, 1080, ['onMutate: async (id) => {', "  await qc.cancelQueries({ queryKey: ['post', id] });", "  const prev = qc.getQueryData(['post', id]);",
                                  "  qc.setQueryData(['post', id], liked);", '  return { prev };', '},', 'onError: (err, id, ctx) =>',
                                  "  qc.setQueryData(['post', id], ctx.prev),", 'onSettled: (data, err, id) =>', "  qc.invalidateQueries({ queryKey: ['post', id] }),"],
         c.T('snapshot'), 0.1, 23, 'LikeButton.jsx',
         marks=[(2, c.T('snapshot') + 0.3, YEL), (4, c.T('return'), YEL), (7, c.T('restore'), YEL), (9, c.T('either'), YEL)])
    tt = c.T('truth')
    if c.on(tt): label(c, 540, 1170, 'the server always has the last word', tt, (200, 240, 200), INK, 32)


def tell(c):
    title(c, "DON'T UNDO SILENTLY", 330, 0.1, 90, hlcol=YEL)
    post(c, 540, 780, False, 1204, w=440, h=640)
    tt = c.T('toast')
    if c.on(tt):
        p = c.P(tt, 0.4)
        y = 1240 - 60 * p
        c.pen.rr(170, y - 50, 910, y + 50, 25, fill=INK)
        c.pen.text(220, y, "Couldn't like. Try again", 'int', 30, WHITE, 'lm')
        c.pen.text(860, y, 'Retry', 'int', 30, YEL, 'rm')
    tf = c.T('flicker')
    if c.on(tf): label(c, 540, 1320, 'a heart that just flickers off feels like a bug', tf, (255, 210, 210), INK, 28)


def race(c):
    head(c, 'THE RACE', 'race', size=96)
    taps = [('like', 'like'), ('unlike', 'unlike'), ('like', 'again')]
    for k, (s_, kw) in enumerate(taps):
        t = c.T(kw)
        node(c, 200 + k * 340, 560, 260, 110, s_, t, fill=(255, 238, 170) if s_ == 'like' else WHITE, size=34)
    tr = c.T('return')
    if c.on(tr):
        c.pen.text(540, 720, 'responses come back out of order', 'ints', 32, INK)
        for k, (s_, col) in enumerate((('#3 OK', GRN), ('#1 OK', GRN), ('#2 FAIL', RED))):
            node(c, 200 + k * 340, 860, 260, 110, s_, tr + 0.3 + k * 0.3, fill=mix(WHITE, col, 0.3), size=32)
    ts = c.T('stale')
    if c.on(ts): label(c, 540, 1030, "#2 fails → rolls back to #1's snapshot → wrong heart", ts, (255, 210, 210), INK, 26)
    tn = c.T('season')
    if c.on(tn): chapter(c, 540, 1160, 'S5', 'race conditions, in depth', tn)


def intents(c):
    title(c, 'SEND INTENT, NOT TOGGLE', 330, 0.1, 82, hlcol=YEL)
    code(c, 30, 440, 1050, 620, ["POST /like/toggle            // depends on order"], c.T('toggle'), 0.1, 26, 'bad', marks=[(0, c.T('toggle') + 0.3, YEL)])
    code(c, 30, 680, 1050, 860, ["PUT /like  { liked: true }   // same result twice"], c.T('set'), 0.1, 26, 'good', marks=[(0, c.T('set') + 0.3, YEL)])
    rows(c, 90, 960, [(c.T('serialize'), 'serialize mutations per item', 'one in flight per post', 'ok'), (c.T('settle'), 'always settle with a refetch', None, 'ok')], 140, 900, 110, 34, 26)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'onError vs onSettled?', c.T('onSettled'), 'monob', 56, INK)
    rows(c, 90, 620, [(c.T('rolls'), 'onError: roll back + tell the user', 'only when it failed', RED),
                      (c.T('either'), 'onSettled: refetch the truth', 'runs either way', GRN)], 180, 900, 140, 38, 28)
    tb = c.T('both')
    if c.on(tb): label(c, 540, 1000, 'you usually want both', tb, YEL, INK, 34)


SCENES = [
    (hook, "You like a post. The heart fills. Then the request fails with a server error. If the heart just stays red, the screen is lying."),
    (eraser, "Back to the diary. The meeting got cancelled, so you erase the pencil line. Rollback is the eraser: put back exactly what was there before."),
    (snapshot, "It takes three steps. In onMutate, take a snapshot of the cached post, and return it. If the request fails, onError gets that snapshot, and you restore it. And onSettled runs either way, and refetches, so the server's truth wins."),
    (tell, "And tell the user. Show a toast with a retry button. A heart that just flickers off, with no explanation, feels like a bug."),
    (race, "Now the race. Like, unlike, and like again, quickly. Three requests. They return out of order. If the second one fails, it rolls back to a stale snapshot, and the heart ends up wrong. Season five covers races in depth."),
    (intents, "The fixes. Don't send toggle, because the result depends on order. Send the intent: set liked to true. Sent twice, it means the same thing. Serialize mutations, one in flight per post. And always settle with a refetch."),
    (gotcha, "Interview question: onError versus onSettled? onError only runs on failure, so it rolls back and tells the user. onSettled runs either way, and refetches the truth. You usually want both."),
    (scene_next('S4 · E17', 'INTERVIEW QUESTIONS', 'server state and caching', 'interview', 'caching'),
     "Next: four interview questions on server state and caching. Comment NOTES for the cheat sheet."),
]
