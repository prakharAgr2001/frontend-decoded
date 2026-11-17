from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E17', tag='S5 · E17', short='SKELETON SCREENS')


def skel_page(c, x0, y0, x1):
    skel(c, x0 + 20, y0 + 20, x1 - 20, y0 + 200, 14)
    for k in range(3):
        y = y0 + 230 + k * 140
        c.pen.circ(x0 + 60, y + 50, 34, fill=(226, 222, 213))
        skel(c, x0 + 110, y + 20, x1 - 30, y + 46, 8)
        skel(c, x0 + 110, y + 64, x1 - 100, y + 86, 8)


def hook(c):
    tt = c.T('Two')
    if c.on(tt):
        a = phone(c, 290, 800, 400, 760, dy=(1 - c.P(tt, 0.45)) * 900)
        b = phone(c, 790, 800, 400, 760, dy=(1 - c.P(tt + 0.2, 0.45)) * 900)
        ts = c.T('spinner')
        if c.on(ts): spinner(c, 290, 800, 50)
        tg = c.T('grey')
        if c.on(tg): skel_page(c, b[0], b[1], b[2])
        c.pen.text(290, 1240, 'spinner', 'intx', 34, INK)
        c.pen.text(790, 1240, 'skeleton', 'intx', 34, INK)
    if c.on(tt): txt(c, 540, 360, 'both load in 1.5 s', tt, 'intx', 40, INK)
    tf = c.T('faster')
    if c.on(tf): stamp(c.cv, 790, 1310, 'FELT FASTER', 54, c.P(tf, 0.35), -5, GRN); c.sfx(tf, 'thud')


def why(c):
    title(c, 'LAYOUT BEFORE DATA', 340, c.T('layout'), 84, hlcol=YEL)
    b = phone(c, 540, 820, 440, 760)
    tsk = c.T('skeleton')
    tj = c.T('jumps')
    if c.on(tj):
        p = c.P(tj, 0.5)
        c.pen.rr(b[0] + 20, b[1] + 20, b[2] - 20, b[1] + 200, 14, fill=mix((226, 222, 213), (120, 170, 220), p))
        for k in range(3):
            y = b[1] + 230 + k * 140
            c.pen.circ(b[0] + 60, y + 50, 34, fill=mix((226, 222, 213), [BLUE, ORANGE, GRN][k], p))
            c.pen.rr(b[0] + 110, y + 20, b[2] - 30, y + 46, 8, fill=mix((226, 222, 213), INK, p))
            c.pen.rr(b[0] + 110, y + 64, b[2] - 100, y + 86, 8, fill=(226, 222, 213))
    else:
        skel_page(c, b[0], b[1], b[2])
    ts = c.T('structure')
    if c.on(ts): label(c, 540, 1270, 'eyes read the structure first', ts, YEL, INK, 30)


def table(c):
    title(c, 'THE TABLE IS LAID', 340, c.T('laying'), 90)
    c.pen.ell(140, 560, 940, 1060, fill=(250, 248, 240), outline=INK, w=6)
    tp = c.T('Plates')
    for k in range(4):
        a = math.radians(45 + k * 90)
        x = 540 + math.cos(a) * 270; y = 810 + math.sin(a) * 160
        if c.on(tp + k * 0.15):
            s = c.B(tp + k * 0.15, 0.3); c.sfx(tp + k * 0.15, 'pop')
            c.pen.circ(x, y, 60 * s, fill=WHITE, outline=INK, w=4)
            c.pen.circ(x, y, 36 * s, outline=GREY, w=3)
            c.pen.circ(x + 80, y - 40, 16 * s, fill=(200, 230, 250), outline=INK, w=3)
    te = c.T('exactly')
    if c.on(te): label(c, 540, 1150, 'you know where everything will go', te, YEL, INK, 32)


def match(c):
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 350, 'S3 · E04', 'CLS', ts)
    tm = c.T('match')
    if c.on(tm): txt(c, 540, 450, 'the skeleton must match the real layout', tm, 'intx', 38, INK)
    tsh = c.T('shorter')
    b = phone(c, 540, 860, 440, 680)
    x0, y0, x1, _ = b
    tsf = c.T('shifts')
    if not c.on(tsf):
        skel(c, x0 + 20, y0 + 20, x1 - 20, y0 + 120, 14)
        if c.on(tsh): c.pen.rr(x0 + 14, y0 + 14, x1 - 14, y0 + 126, 16, outline=RED, w=5)
        skel(c, x0 + 20, y0 + 150, x1 - 20, y0 + 260, 14)
    else:
        p = c.P(tsf, 0.4)
        c.pen.rr(x0 + 20, y0 + 20, x1 - 20, y0 + 120 + 120 * p, 14, fill=(120, 170, 220))
        c.pen.rr(x0 + 20, y0 + 150 + 120 * p, x1 - 20, y0 + 260 + 120 * p, 14, fill=(226, 222, 213))
        arrow(c.pen, x1 + 50, y0 + 160, x1 + 50, y0 + 160 + 120 * p, 1, RED, 6)
        stamp(c.cv, 540, 1290, 'LAYOUT SHIFT', 66, c.P(tsf, 0.35), -4, RED); c.sfx(tsf, 'thud')


def flash(c):
    head(c, 'DON’T FLASH IT', 'flash', size=84)
    th = c.T('hundred')
    if c.on(th):
        axis(c, 100, 980, 640, th, [(0.0, '0 ms', th, GREY), (0.3, 'data at 100 ms', th + 0.3, GRN)], labels_up=True)
    tb = c.T('blinks')
    if c.on(tb):
        on = int((c.t - tb) * 6) % 2 == 0 and c.t < tb + 1.2
        c.pen.rr(340, 760, 740, 860, 16, fill=(226, 222, 213) if on else PAPER, outline=GREY if on else None, w=3)
        txt(c, 540, 920, 'skeleton blinks on, then off', tb, 'intx', 32, RED)
    tw = c.T('Wait')
    if c.on(tw):
        axis(c, 100, 980, 1080, tw, [(0.0, 'start', tw, GREY), (0.6, 'show skeleton only after ~200 ms', tw + 0.3, YEL)], labels_up=False)


CODE = ['const { data, isPending, isFetching } = useQuery(q);', '', 'if (isPending) return <FeedSkeleton />;', 'return <Feed data={data} refreshing={isFetching} />;']


def rq(c):
    ts = c.T('season')
    if c.on(ts): chapter(c, 540, 350, 'S4 · E11', 'Server state', ts)
    code(c, 20, 430, 1060, 430 + 72 + len(CODE) * 52 + 20, CODE, c.T('skeleton'), 0.1, 24, 'Feed.jsx',
         marks=[(2, c.T('first'), YEL), (3, c.T('old'), YEL)])
    tf = c.T('first')
    if c.on(tf): rows(c, 100, 880, [(tf, 'first load, no data', 'skeleton', 'ok'), (c.T('refetch'), 'background refetch', 'keep old data + small spinner', 'ok')],
                      gap=160, h=130)


def proof(c):
    tb = c.T('YouTube')
    inner = browser(c, 60, 330, 1020, 1150, 'youtube.com', dy=(1 - c.P(0, 0.45)) * 900)
    x0, y0, x1, y1 = inner
    tth = c.T('thumbnails')
    tt = c.T('Throttle')
    if c.on(tt): pill(c.pen, 800, 400, 'Slow 4G', c.B(tt, 0.35), YEL, INK, 28)
    for k in range(6):
        x = x0 + 40 + (k % 2) * 450; y = y0 + 40 + (k // 2) * 250
        if c.on(tth + k * 0.2):
            c.pen.rr(x, y, x + 410, y + 160, 12, fill=[BLUE, ORANGE, GRN, PURPLE, TEAL, PINK][k], outline=INK, w=3)
            c.pen.rr(x, y + 180, x + 300, y + 205, 8, fill=INK)
        else:
            skel(c, x, y, x + 410, y + 160, 12); skel(c, x, y + 180, x + 300, y + 205, 8)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    te = c.T('everywhere')
    if c.on(te): txt(c, 540, 470, 'Skeletons everywhere, always?', te, 'intx', 50, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 590, 'NO', 100, c.P(tn, 0.35), -5, RED); c.sfx(tn, 'thud')
    tsv = c.T('saving')
    if c.on(tsv):
        s = c.B(tsv, 0.35); c.sfx(tsv, 'pop')
        c.pen.rr(560, 720, 960, 820, 50, fill=BLUE, outline=INK, w=4)
        c.pen.text(790, 770, 'Saving…', 'intx', 36 * s, WHITE)
        c.pen.arc(600, 745, 650, 795, (c.t * 400) % 360, (c.t * 400) % 360 + 270, WHITE, 6)
    tc = c.T('content')
    if c.on(tc):
        skel(c, 120, 720, 480, 760, 10); skel(c, 120, 780, 420, 820, 10)
        rows(c, 100, 980, [(tc, 'content loading', 'skeleton', YEL), (c.T('actions', 2), 'action in progress', 'spinner on the button', BLUE)], gap=160, h=130)


SCENES = [
    (hook, "Two apps load in exactly one point five seconds. One shows a spinner. One shows grey shapes of the page. People say the second one felt faster."),
    (why, "A skeleton shows the layout before the data. Your eyes start reading the structure, so the wait feels shorter. And nothing jumps when the content arrives."),
    (table, "It's like a restaurant laying the table before the food comes. Plates, glasses, cutlery, all in place. You know exactly where everything will go."),
    (match, "But the skeleton must match the real layout. If the grey card is shorter than the real one, the page shifts when the data lands. That's layout shift, from season three."),
    (flash, "And don't flash it. If data arrives in a hundred milliseconds, a skeleton that blinks on and off looks worse than nothing. Wait about two hundred milliseconds before showing it."),
    (rq, "With server state from season four, show the skeleton only on the first load, when there's no data yet. On a background refetch, keep the old data on screen, with a small spinner at most."),
    (proof, "See it on YouTube. Throttle the network to slow 4G, and reload the home page. Grey blocks first, then the thumbnails fill in."),
    (gotcha, "Interview trap. Skeletons everywhere, always? No. For actions like saving a form, a spinner on the button is clearer. Skeletons are for content that's loading. Spinners are for actions in progress."),
    (scene_next('S5 · E18', 'PARTIAL FAILURE', 'when one widget breaks', 'partial', 'widget'),
     "Next: partial failure, when one widget breaks, and the page should not. Comment NOTES for the cheat sheet."),
]
