from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E12', tag='S5 · E12', short='RACE CONDITIONS')


def hook(c):
    tr = c.T('Riya'); ta = c.T('Arjun')
    for k, (nm, t) in enumerate((('Riya', tr), ('Arjun', ta))):
        x = 300 + k * 480
        if c.on(t):
            c.sfx(t, 'click'); s = c.B(t, 0.3)
            c.pen.rr(x - 180 * s, 340, x + 180 * s, 430, 45, fill=YEL if (k == 1) else WHITE, outline=INK, w=4)
            c.pen.text(x, 385, nm, 'intx', 38 * s, INK)
    inner = browser(c, 80, 490, 1000, 1200, 'app.example.com/profile', dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    th = c.T('header')
    if c.on(th):
        c.pen.circ(x0 + 90, y0 + 90, 50, fill=ORANGE, outline=INK, w=4)
        c.pen.text(x0 + 170, y0 + 90, 'Arjun', 'intx', 50, INK, 'lm')
    tp = c.T('posts')
    if c.on(tp):
        for k in range(3):
            y = y0 + 190 + k * 150
            c.pen.rr(x0 + 40, y, x1 - 40, y + 120, 14, fill=(255, 220, 220), outline=RED, w=4)
            c.pen.text(x0 + 70, y + 60, f'Riya’s post #{k + 1}', 'intx', 34, INK, 'lm')
        stamp(c.cv, 540, 1290, 'WRONG DATA', 76, c.P(c.T('posts') + 0.5, 0.35), -4, RED); c.sfx(tp + 0.5, 'thud')


def why(c):
    title(c, 'BOTH IN FLIGHT', 340, c.T('flight'), 96, hlcol=YEL)
    t0 = c.T('flight')
    axis(c, 100, 980, 600, t0, [(0.08, 'ask Riya', t0, BLUE), (0.3, 'ask Arjun', t0 + 0.4, ORANGE)], labels_up=True)
    ts = c.T('slow')
    axis(c, 100, 980, 820, ts, [(0.5, 'Arjun arrives', ts, ORANGE), (0.88, 'Riya arrives', c.T('last'), RED)], labels_up=False)
    to = c.T('overwrote')
    if c.on(to): stamp(c.cv, 700, 1010, 'OVERWRITES', 60, c.P(to, 0.35), -4, RED); c.sfx(to, 'thud')
    tn = c.T('network')
    if c.on(tn): label(c, 540, 1160, 'network order, not request order', tn, YEL, INK, 32)


def micro(c):
    tr = c.T('Remember')
    if c.on(tr): chapter(c, 540, 350, 'S1 · E16', 'Microtasks', tr)
    code(c, 60, 460, 1020, 460 + 72 + 3 * 50 + 20, ["fetchPosts('riya').then(setPosts);", "fetchPosts('arjun').then(setPosts);", '// whichever settles last wins'],
         c.T('promise'), 0.12, 28, 'profile.js', marks=[(2, c.T('settles'), YEL)])
    tn = c.T('Nothing')
    if c.on(tn): stamp(c.cv, 540, 900, 'NO ORDER GUARANTEE', 66, c.P(tn, 0.35), -3, RED); c.sfx(tn, 'thud')


def friends(c):
    title(c, 'ASKING FOR DIRECTIONS', 340, c.T('friends'), 80)
    person(c.pen, 540, 900, 1.4, BLUE)
    tf = c.T('friends')
    if c.on(tf):
        person(c.pen, 220, 900, 1.2, ORANGE); person(c.pen, 860, 900, 1.2, GRN)
    tl = c.T('last')
    bubble(c, 120, 600, '“turn left”', c.T('other') - 0.2, WHITE, 32)
    bubble(c, 600, 520, '“go right”', tl, (255, 220, 220), 32)
    tw = c.T('wrong')
    if c.on(tw): stamp(c.cv, 540, 1110, 'WRONG PLACE', 76, c.P(tw, 0.35), -4, RED); c.sfx(tw, 'thud')


FIX = ['useEffect(() => {', '  let ignore = false;', '  fetchPosts(userId).then((p) => {', '    if (!ignore) setPosts(p);', '  });',
       '  return () => { ignore = true; };', '}, [userId]);']


def fix(c):
    code(c, 40, 360, 1040, 360 + 72 + len(FIX) * 52 + 20, FIX, c.T('React') - 0.3, 0.1, 28, 'Profile.jsx',
         marks=[(1, c.T('ignore'), YEL), (5, c.T('cleaned'), YEL), (3, c.T('drop'), YEL)])
    ts = c.T('stale')
    if c.on(ts): label(c, 540, 900, 'old request marked stale', ts, YEL, INK, 32)
    td = c.T('drop')
    if c.on(td): txt(c, 540, 1000, 'its result is dropped', td, 'intx', 36, INK)


def where(c):
    title(c, 'RACES ARE EVERYWHERE', 340, 0.1, 84)
    for k, (kw, nm, ic) in enumerate((('search', 'search boxes', 'eye'), ('tab', 'tab switches', 'laptop'), ('filters', 'filters', 'cpu'),
                                      ('pagination', 'pagination', 'doc'))):
        node(c, 300 + (k % 2) * 480, 540 + (k // 2) * 260, 420, 200, nm, c.T(kw), ic, size=34)
    ts = c.T('same')
    if c.on(ts): label(c, 540, 1130, 'same state · more than one request', ts, YEL, INK, 32)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    td = c.T('debounce')
    if c.on(td): txt(c, 540, 470, 'Debounce fixes this, right?', td, 'intx', 50, INK)
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 580, 'S3 · E23', 'Debounce trap', ts)
    to = c.T('overlap')
    if c.on(to):
        axis(c, 140, 940, 740, to, [(0.15, 'req 1', to, BLUE), (0.85, 'res 1 (late)', to + 0.3, RED)], labels_up=True)
        axis(c, 140, 940, 880, to + 0.2, [(0.45, 'req 2', to + 0.2, ORANGE), (0.65, 'res 2', to + 0.4, ORANGE)], labels_up=False)
    tc = c.T('cancel')
    if c.on(tc): label(c, 540, 1060, 'ignore or cancel the stale one', tc, (255, 220, 220), INK, 32)
    tr = c.T('React', 1)
    if c.on(tr): label(c, 540, 1170, "React Query: data keyed by ['posts', userId]", tr, YEL, INK, 28)


SCENES = [
    (hook, "You click Riya's profile, then quickly Arjun's. The header says Arjun. But the posts are Riya's."),
    (why, "Both requests were in flight. Riya's server call was slow, so her response arrived last, and overwrote Arjun's. Responses arrive in network order, not in the order you asked."),
    (micro, "Remember microtasks from season one. A promise callback runs whenever its promise settles. Nothing in JavaScript keeps them in request order for you."),
    (friends, "It's like asking two friends for directions. You ask one, change your mind, and ask the other. If the first one answers last, and you follow whoever spoke last, you end up at the wrong place."),
    (fix, "The simplest fix in React: an ignore flag. When the effect is cleaned up, because the user picked someone else, the old request is marked stale, and we drop its result."),
    (where, "Races show up everywhere. Search boxes, tab switches, filters, pagination. Any time the same state can be set by more than one request."),
    (gotcha, "Interview trap. Doesn't debounce fix this? We saw it in season three. No. Debounce sends fewer requests, but two can still overlap. You need to ignore, or cancel, the stale one. React Query does this for you, by keying data by its query."),
    (scene_next('S5 · E13', 'ABORTCONTROLLER', 'cancel the request for real', 'AbortController', 'real'),
     "Next: AbortController, to cancel the old request for real. Comment NOTES for the cheat sheet."),
]
