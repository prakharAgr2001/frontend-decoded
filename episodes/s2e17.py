from engine.s2_extra import *

EP = dict(id='S2E17', tag='S2 · E17', short='RESUMABILITY', hook='skip hydration entirely')

def hook(c):
    ts = c.T('server')
    node(c, 260, 600, 300, 220, 'server', ts, 'server', sub='ran every component')
    tb = c.T('browser')
    node(c, 820, 600, 300, 220, 'browser', tb, 'laptop', sub='runs them AGAIN')
    if c.on(tb): arrow(c.pen, 430, 600, 650, 600, c.P(tb, 0.4), INK, 6, 20)
    tk = c.T('knew')
    if c.on(tk): label(c, 540, 860, '…to rediscover what the server already knew', tk, RED, WHITE, 30)
    tc = c.T('continue')
    if c.on(tc): stamp(c.cv, 540, 1080, 'WHAT IF IT JUST CONTINUED?', 56, c.P(tc, 0.4), -3, BLUE)

def define(c):
    title(c, 'RESUMABILITY', 340, c.T('resumability'), 120, hlcol=YEL)
    tq = c.T('Qwik')
    if c.on(tq): label(c, 540, 450, 'the idea behind Qwik', tq, INK, WHITE, 30)
    tp = c.T('pauses')
    if c.on(tp):
        node(c, 260, 700, 300, 200, 'server', tp, 'server', sub='pauses the app')
        icon(c.pen, 'doc', 540, 700, 1.3)
        c.pen.text(540, 800, 'state + wiring', 'int', 26, INK)
    tr = c.T('resumes')
    if c.on(tr): node(c, 820, 700, 300, 200, 'browser', tr, 'laptop', sub='resumes it')
    tn = c.T('without')
    if c.on(tn): label(c, 540, 950, 'no components re-run on load', tn, GRN, WHITE, 32)

def analogy(c):
    tg = c.T('game')
    if c.on(tg):
        c.pen.text(540, 350, 'THE GAME SAVE', 'osw', 72, INK)
    tr = c.T('replaying')
    if c.on(tr):
        card(c.pen, 90, 450, 990, 720, 22, WHITE, 10, 5)
        c.pen.text(140, 500, 'hydration', 'intx', 38, RED, 'lm')
        for k in range(8):
            at = tr + k * 0.15
            if c.on(at): c.pen.rr(140 + k * 105, 570, 230 + k * 105, 670, 10, fill=LIGHT, outline=INK, w=3); c.pen.text(185 + k * 105, 620, f'L{k + 1}', 'int', 26, INK)
        c.pen.text(950, 500, 'replay every level', 'int', 26, MUTE, 'rm')
    tl = c.T('loading')
    if c.on(tl):
        card(c.pen, 90, 800, 990, 1070, 22, WHITE, 10, 5)
        c.pen.text(140, 850, 'resumability', 'intx', 38, GRN, 'lm')
        c.pen.rr(140, 920, 330, 1020, 10, fill=YEL, outline=INK, w=4); c.pen.text(235, 970, 'SAVE', 'osw', 40, INK)
        arrow(c.pen, 350, 970, 520, 970, c.P(tl, 0.4), INK, 6, 18)
        c.pen.text(560, 970, 'right where you were', 'int', 30, INK, 'lm')

def how(c):
    th = c.T('handler')
    htmlcard(c, 30, 340, 1050, ['<button on:click="q-a1b2.js#s_addToCart">', '  Add to cart', '</button>'], th, 'HTML from the server', 28,
             marks=[(0, c.T('URL'), YEL)])
    tg = c.T('global')
    if c.on(tg): label(c, 540, 720, 'one tiny global listener (~1 KB)', tg, INK, WHITE, 30)
    tc = c.T('click')
    if c.on(tc):
        b = node(c, 230, 920, 280, 160, 'click', tc, 'bolt', size=30)
        d = node(c, 540, 920, 260, 160, 'download', c.T('downloads'), 'cloud', sub='just that handler', size=28)
        r = node(c, 850, 920, 240, 160, 'run', c.T('runs'), 'cpu', size=30)
        link(c, b, d, c.T('downloads')); link(c, d, r, c.T('runs'))

def timeline(c):
    x0, x1 = 100, 980
    txt(c, x0, 420, 'Hydration', c.T('Hydration'), 'intx', 40, RED, 'lm')
    seg_row(c, x0, 460, x1, [('download all JS', 0, 0.45, YEL, c.T('download')), ('execute all', 0.45, 0.8, ORANGE, c.T('execute'))])
    marker(c, x0 + (x1 - x0) * 0.8, 580, 450, 'interactive', c.T('then'), BLUE)
    txt(c, x0, 760, 'Resumable', c.T('Resumable'), 'intx', 40, GRN, 'lm')
    seg_row(c, x0, 800, x1, [('1 KB', 0, 0.06, CYAN, c.T('Resumable'))])
    marker(c, x0 + (x1 - x0) * 0.06, 920, 790, 'interactive', c.T('immediately'), GRN)
    ti = c.T('interaction')
    if c.on(ti): seg_row(c, x0, 1000, x1, [('code fetched on interaction', 0.3, 0.75, YEL, ti)])

def gotcha(c):
    trap(c)
    qtext(c, 'So resumability has zero cost?', 450, c.T('zero'), 56)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 600, 'NO', 110, c.P(tn, 0.35), -6, RED)
    tf = c.T('first')
    if c.on(tf):
        seg_row(c, 100, 740, 980, [('click', 0, 0.12, YEL, tf), ('fetch handler on bad 3G…', 0.12, 0.85, RED, tf + 0.3)])
        label(c, 540, 870, 'first click can feel slow', tf + 0.6, RED, WHITE, 30)
    tp = c.T('prefetches')
    if c.on(tp): label(c, 540, 1000, 'fix: prefetch likely handlers in the background', tp, GRN, WHITE, 30)

SCENES = [
    (hook, "Hydration is a strange idea when you think about it. The server ran every component. Then the browser runs them all again, just to rediscover what the server already knew. What if the browser could just continue?"),
    (define, "That's resumability, the idea behind the Qwik framework. The server pauses the app, and writes its state and event wiring into the HTML. The browser resumes from there, without re-running your components."),
    (analogy, "Think of a video game. Hydration is replaying every level to get back to where you were. Resumability is loading the save file."),
    (how, "Each event handler is written into the HTML as a URL to a small chunk of code. One tiny global listener waits. When you click, it downloads just that handler, and runs it."),
    (timeline, "Hydration: download all the JavaScript, execute all of it, then you're interactive. Resumable: interactive almost immediately, with code fetched only on interaction."),
    (gotcha, "Interview trap: so resumability has zero cost? No. The first click has to fetch code, and on a bad network that can feel slow. So Qwik prefetches likely handlers in the background, before you click."),
    (scene_next('S2 · E18', 'EDGE RENDERING', 'render next door to the user', 'edge', 'door'),
     "Next: edge rendering. Render the page next door to the user. Comment NOTES for the cheat sheet."),
]
