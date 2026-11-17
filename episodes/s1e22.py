from engine.lib import *

EP = dict(id='S1E22', tag='S1 · E22', short='MEMORY LEAKS')

def hook(c):
    browser(c, 120, 330, 960, 700, url='your-app.example')
    c.pen.text(540, 530, 'tab open for 24 hours…', 'intx', 40, INK)
    tg = c.T('gigabytes')
    counter(c, 540, 900, 120, 2400, c.T('day'), tg + 0.6, '{:,.0f}', 140, RED, ' MB')
    tl = c.T('leak')
    if c.on(tl): stamp(c.cv, 540, 1100, 'MEMORY LEAK', 72, c.P(tl, 0.35), -3, RED)

GRAPH = [('root', 'roots', 540, 430, None), ('a', 'window.app', 330, 610, 'root'), ('b', 'stack vars', 750, 610, 'root'),
         ('c', 'user', 250, 800, 'a'), ('d', 'cart', 450, 800, 'a'), ('e', 'items[]', 750, 800, 'b')]
ORPH = [('x', 'old modal', 330, 1000), ('y', 'temp data', 750, 1000)]

def gc(c):
    tr = c.T('roots')
    nodes = [(k, l, x, y, p, tr + i * 0.15) for i, (k, l, x, y, p) in enumerate(GRAPH)]
    tm = c.T('marks')
    tree(c, nodes, 0, col=lambda k: (190, 240, 200) if c.on(tm) else WHITE)
    tf = c.T('frees')
    for k, l, x, y in ORPH:
        if not c.on(tr + 0.6): continue
        a = 1 - c.P(tf + 0.3, 0.6)
        if a <= 0.02: continue
        w = c.pen.tw(l, 'monob', 30) + 36
        c.pen.rr(x - w / 2, y - 28, x + w / 2, y + 28, 14, fill=mix(PAPER, (255, 210, 210), a), outline=mix(PAPER, INK, a), w=4)
        c.pen.text(x, y, l, 'monob', 30, mix(PAPER, INK, a))
    if c.on(tf): label(c, 540, 1150, 'unreachable → freed', tf, GRN, WHITE, 32)

def define(c):
    title(c, 'A LEAK =', 380, 0.1, 110)
    txt(c, 540, 560, 'memory you are done with…', c.T('done'), 'intx', 46, INK)
    txt(c, 540, 650, '…that is still reachable', c.T('reachable'), 'intx', 46, RED)
    tn = c.T('never')
    if c.on(tn):
        node(c, 540, 900, 380, 200, 'GC can’t free it', tn, 'bin', fill=(255, 225, 225))

def causes(c):
    items = [('listener never removed', 'listener', 'window.addEventListener(…)'), ('interval still running', 'setInterval', 'setInterval(poll, 1000)'),
             ('cache that only grows', 'cache', 'cache[key] = bigObject'), ('detached DOM nodes', 'detached', 'saved = el; el.remove()')]
    for i, (a, kw, cd) in enumerate(items):
        at = c.T(kw); y = 420 + i * 215
        if not c.on(at - 0.01): continue
        c.sfx(at, 'pop'); s = c.B(at, 0.4)
        card(c.pen, 90, y - 85 * s, 990, y + 85 * s, 22, WHITE, 10, 5)
        c.pen.circ(160, y, 34 * s, fill=RED); c.pen.text(160, y, str(i + 1), 'osw', 40 * s, WHITE)
        c.pen.text(220, y - 22, a, 'intx', 38 * s, INK, 'lm')
        c.pen.text(220, y + 30, cd, 'mono', 26 * s, MUTE, 'lm')

def react(c):
    code(c, 40, 330, 1040, 860, ["useEffect(() => {", "  const id = setInterval(poll, 1000);", "  window.addEventListener('resize', onResize);",
                                 "  return () => {             // cleanup", "    clearInterval(id);", "    window.removeEventListener('resize', onResize);", "  };", "}, []);"],
         c.T('React'), 0.12, 24, 'Widget.jsx', marks=[(3, c.T('cleanup'), YEL), (4, c.T('clear'), (60, 120, 80)), (5, c.T('Remove'), (60, 120, 80))])
    ta = c.T('abort')
    if c.on(ta): label(c, 540, 960, '+ abort pending fetches (AbortController)', ta, WHITE, INK, 28)

def weak(c):
    code(c, 60, 360, 1020, 620, ["const meta = new WeakMap();", "meta.set(element, { clicks: 3 });", "// element removed → entry can be collected"],
         c.T('WeakMap'), 0.2, 28, 'cache.js')
    tg = c.T('collected')
    if c.on(tg):
        node(c, 300, 820, 300, 160, 'Map', tg, None, fill=(255, 225, 225), sub='keeps the key alive', size=40)
        node(c, 780, 820, 300, 160, 'WeakMap', tg + 0.3, None, fill=(225, 245, 230), sub='lets it go', size=40)

def proof(c):
    panel(c, 60, 330, 1020, 1050, tabs=('Memory',), dy=(1 - c.P(0, 0.45)) * 900)
    for j, (lab, mb, kw) in enumerate([('Snapshot 1', '38 MB', 'snapshot'), ('Snapshot 2', '61 MB', 'another')]):
        at = c.T(kw)
        if c.on(at): c.sfx(at, 'pop'); c.pen.text(100, 480 + j * 70, f'{lab}   {mb}', 'monob', 32, WHITE, 'lm')
    td = c.T('Detached')
    if c.on(td):
        c.pen.rr(100, 660, 980, 730, 10, fill=(40, 46, 56), outline=YEL, w=3)
        c.pen.text(120, 695, 'Filter: Detached', 'mono', 30, YEL, 'lm')
        for i, s_ in enumerate(['Detached HTMLDivElement ×212', 'Detached HTMLImageElement ×48']):
            if c.on(td + 0.4 + i * 0.3): c.pen.text(120, 790 + i * 70, s_, 'mono', 30, (255, 140, 140), 'lm')

def gotcha(c):
    stamp(c.cv, 540, 330, 'INTERVIEW QUESTION', 70, c.P(c.T('Interview'), 0.4), -4, RED); c.sfx(c.T('Interview'), 'thud')
    txt(c, 540, 470, 'Can closures cause leaks?', c.T('closures'), 'intx', 50, INK)
    ty = c.T('Yes')
    if c.on(ty): stamp(c.cv, 540, 580, 'YES', 80, c.P(ty, 0.35), 4, BLUE)
    code(c, 80, 680, 1000, 960, ["const big = new Array(1e6).fill('x');", "button.onclick = () => console.log(big.length);", "// big lives as long as the handler does"],
         c.T('keeps'), 0.25, 24, 'leak.js')

SCENES = [
    (hook, "Leave some web apps open for a day, and the tab slowly eats gigabytes of memory. That's a memory leak."),
    (gc, "JavaScript cleans up memory automatically. The garbage collector starts from the roots, like global variables and the current stack, marks everything still reachable, and frees the rest."),
    (define, "So a leak is memory you're done with, that's still reachable. The collector can never free it."),
    (causes, "The usual suspects. A listener added but never removed. A setInterval still running after its component is gone. A global cache that only grows. And detached DOM nodes, removed from the page but still referenced in your code."),
    (react, "In React, return a cleanup function from useEffect. Clear your intervals. Remove your listeners. And abort pending fetches."),
    (weak, "For caches keyed by objects, use a WeakMap. Its entries can be collected once the key is gone."),
    (proof, "To hunt leaks, open the Memory panel. Take a heap snapshot, use the app, take another, and compare. Filter for Detached to find orphaned nodes."),
    (gotcha, "Interview question: can closures cause leaks? Yes. A closure keeps every variable it uses alive, for as long as the closure itself is reachable."),
    (scene_next('S1 · E23', 'OBSERVERS', 'the smart way to watch the page', 'observers', 'watch'),
     "Next: observers, the smart way to watch the page. Comment NOTES for the cheat sheet."),
]
