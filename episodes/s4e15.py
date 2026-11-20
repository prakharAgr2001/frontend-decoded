from engine.lib import *
from engine.s3_extra import rows, versus
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E15', tag='S4 · E15', short='OPTIMISTIC UI', hook='why the heart fills instantly')


def post(c, cx, cy, liked, likes, w=520, h=760, pop=None, signal=None):
    ib = phone_frame(c, cx, cy, w, h)
    x0, y0, x1, y1 = ib
    c.pen.circ(x0 + 50, y0 + 45, 24, fill=(255, 200, 150), outline=INK, w=3)
    c.pen.text(x0 + 90, y0 + 45, 'chai.point', 'int', 26, INK, 'lm')
    c.pen.rect(x0, y0 + 90, x1, y0 + 90 + (x1 - x0), fill=(240, 205, 160))
    c.pen.circ((x0 + x1) / 2, y0 + 90 + (x1 - x0) / 2, 90, fill=(200, 140, 90))
    hy = y0 + 90 + (x1 - x0) + 55
    s = 1.0
    if pop is not None and c.on(pop): s = 1 + 0.4 * math.sin(math.pi * cl((c.t - pop) / 0.35))
    heart(c.pen, x0 + 50, hy, 1.6 * s, RED if liked else WHITE, INK, 4)
    c.pen.text(x0 + 95, hy, f'{likes} likes', 'int', 28, INK, 'lm')
    if signal is not None:
        for k in range(4):
            c.pen.rect(x1 - 90 + k * 18, y0 - 30 - k * 10 - 10, x1 - 78 + k * 18, y0 - 30, fill=INK if k < signal else GREY)
    return ib


def hook(c):
    tt = c.T('tap')
    post(c, 540, 820, c.on(tt + 0.1), 1205 if c.on(tt + 0.1) else 1204, pop=tt + 0.1, signal=1)
    if c.on(tt):
        q = lin(c.t, tt, tt + 0.5)
        if q < 1: c.pen.circ(540, 820, 60 + 120 * q, outline=mix(RED, PAPER, q), w=8)
    ts = c.T('signal')
    if c.on(ts): label(c, 540, 330, 'one bar of signal', ts, WHITE, INK, 30)
    th = c.T("hasn't")
    if c.on(th): stamp(c.cv, 540, 1290, 'SERVER: NO REPLY YET', 60, c.P(th, 0.35), -3, RED); c.sfx(th, 'thud')


def define(c):
    title(c, 'OPTIMISTIC UI', 380, 0.1, 130, hlcol=YEL)
    for k, (kw, s_, col) in enumerate((('succeed', 'update the screen as if it worked', YEL), ('background', 'send the request in the background', (220, 225, 235)),
                                       ('fails', 'fix it only if it fails', (255, 210, 210)))):
        node(c, 540, 560 + k * 190, 820, 130, s_, c.T(kw), fill=col, size=36)


def pencil(c):
    title(c, 'PENCIL, THEN INK', 330, 0.1, 100)
    card(c.pen, 160, 450, 920, 1050, 18, (255, 250, 235), 10, 5)
    for k in range(7): c.pen.line([(190, 540 + k * 70), (890, 540 + k * 70)], (220, 210, 190), 2, False)
    c.pen.text(200, 500, 'FRIDAY', 'osw', 36, INK, 'lm')
    tw = c.T('write')
    if c.on(tw):
        ti = c.T('ink')
        col = INK if c.on(ti) else GREY
        txt(c, 220, 680, '4 pm · coffee with Arjun', tw, 'intx', 40, col, 'lm', 'slide')
        if c.on(ti):
            q = c.P(ti, 0.8)
            c.pen.line([(220, 712), (220 + 600 * q, 712)], INK, 5)
    tc = c.T('confirms')
    if c.on(tc): label(c, 540, 1130, 'write first · confirm later', tc, YEL, INK, 34)


def timeline(c):
    title(c, 'WAIT VS TRUST', 330, 0.1, 100)
    for j, (nm, kw, delay, col) in enumerate((('pessimistic', 'Pessimistic', 1.0, RED), ('optimistic', 'Optimistic', 0.0, GRN))):
        t = c.T(kw)
        if not c.on(t): continue
        y = 560 + j * 330
        c.pen.text(100, y - 80, nm, 'intx', 40, col, 'lm')
        p = c.P(t + 0.2, 1.4, lambda x: x)
        c.pen.line([(100, y), (100 + 880 * p, y)], INK, 6)
        c.pen.circ(120, y, 18, fill=INK)
        c.pen.text(120, y + 50, 'tap', 'int', 26, INK)
        hx = 120 + 880 * (0.82 if delay else 0.04)
        if c.on(t + 0.2 + 1.4 * (0.82 if delay else 0.04)): heart(c.pen, hx + (0 if delay else 70), y - 45, 1.4, RED)
        if delay:
            c.pen.rr(200, y - 25, 820, y + 25, 25, fill=(255, 225, 225))
            c.pen.text(510, y, 'waiting 800 ms…', 'int', 26, RED)
            c.pen.text(840, y + 55, 'heart', 'int', 26, INK)
        else:
            c.pen.text(860, y + 55, 'server OK', 'int', 26, MUTE)
            if c.on(t + 1.4): check(c.pen, 900, y - 40, 0.6, GRN, 6, c.P(t + 1.4, 0.3))
    tf = c.T('feels')
    if c.on(tf): label(c, 540, 1200, 'same network · feels instant', tf, YEL, INK, 34)


def rq(c):
    title(c, 'IN REACT QUERY', 330, 0.1, 90, hlcol=YEL)
    code(c, 30, 430, 1050, 1000, ['useMutation({', '  mutationFn: likePost,', '  onMutate: async (id) => {', "    await qc.cancelQueries({ queryKey: ['post', id] });",
                                  "    qc.setQueryData(['post', id], (p) =>", '      ({ ...p, liked: true, likes: p.likes + 1 }));', '  },', '});'],
         c.T('onMutate'), 0.12, 24, 'LikeButton.jsx', marks=[(2, c.T('onMutate') + 0.4, YEL), (4, c.T('writes'), YEL)])
    tb = c.T('before')
    if c.on(tb): label(c, 540, 1090, 'runs before the request is sent', tb, (200, 240, 200), INK, 32)


def react19(c):
    title(c, 'useOptimistic', 330, c.T('use'), 110, hlcol=YEL)
    code(c, 30, 440, 1050, 800, ['const [likes, addLike] = useOptimistic(', '  serverLikes, (n) => n + 1);', 'async function like() {',
                                 '  addLike(); await likePost(id);', '}'], c.T('use') + 0.3, 0.12, 28, 'Like.jsx', marks=[(3, c.T('shows'), YEL)])
    te = c.T('ends')
    if c.on(te): label(c, 540, 900, 'optimistic value lives only while the action runs', te, WHITE, INK, 28)


def when(c):
    title(c, 'WHEN TO TRUST', 330, 0.1, 100)
    versus(c, ('YES', GRN, c.T('likely'), [(c.T('likes'), 'likes, toggles'), (c.T('reordering'), 'reordering'), (c.T('chat'), 'chat messages')]),
           ('NO', RED, c.T("Don't"), [(c.T('payments'), 'payments'), (c.T('stock'), 'last item in stock'), (c.T('cost'), 'anything a false success costs')]), 430, 1000, 36)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'Why cancelQueries before the update?', c.T('first'), 'intx', 44, INK)
    a = node(c, 250, 700, 340, 150, 'your update', c.T('optimistic'), fill=(200, 240, 200), sub='likes: 1205')
    b = node(c, 830, 700, 340, 150, 'old refetch', c.T('flight'), fill=(255, 210, 210), sub='likes: 1204')
    to = c.T('overwrite')
    if c.on(to):
        packet(c, b, a, to, to + 0.8, RED, 'lands late')
        if c.on(to + 0.8): cross(c.pen, 250, 700, 1.3, RED, 10, c.P(to + 0.8, 0.3))
    tc = c.T('Cancel', 2)
    if c.on(tc): label(c, 540, 960, 'cancel in-flight queries, then write', tc, YEL, INK, 32)


SCENES = [
    (hook, "You double tap a photo on Instagram, on a train, with one bar of signal. The heart fills instantly. But the server hasn't even answered yet."),
    (define, "That's optimistic UI. Update the screen as if the request will succeed. Send the request in the background. And fix things only if it fails."),
    (pencil, "It's like a diary. You write the meeting in pencil before your friend confirms. When they confirm, you go over it in ink."),
    (timeline, "Compare the two. Pessimistic: tap, wait eight hundred milliseconds, then the heart. Optimistic: the heart appears on the tap, and the server catches up. Same network, but it feels instant."),
    (rq, "In React Query, you do it in onMutate, which runs before the request is sent. First cancel any refetch for this post. Then it writes the liked version straight into the cache."),
    (react19, "React nineteen adds a hook for this: use optimistic. It shows the optimistic value while the action is running. When the action ends, it falls back to the real value."),
    (when, "Use it when success is very likely, and easy to undo. Likes, toggles, reordering, chat messages. Don't use it for payments, the last item in stock, or anything where a false success would cost the user."),
    (gotcha, "Interview question: why cancel queries first? Because a refetch already in flight could land after your optimistic update, and overwrite it with old data. Cancel, then write."),
    (scene_next('S4 · E16', 'ROLLBACK', 'when the optimistic guess was wrong', 'rollback', 'wrong'),
     "Next: rollback, for when the optimistic guess was wrong. Comment NOTES for the cheat sheet."),
]
