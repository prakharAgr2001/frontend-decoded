from engine.s2_extra import *

EP = dict(id='S2E18', tag='S2 · E18', short='EDGE RENDERING', hook='render next door to the user')

CITIES = {'Virginia': (250, 620), 'Bengaluru': (780, 820), 'Frankfurt': (520, 540), 'Singapore': (860, 900), 'Sao Paulo': (330, 1000), 'Sydney': (930, 1100)}

def worldmap(c):
    c.pen.rr(70, 420, 1010, 1200, 30, fill=(225, 236, 245), outline=INK, w=5)
    for (x0, y0, x1, y1) in [(130, 480, 420, 760), (260, 860, 430, 1150), (450, 470, 620, 640), (480, 650, 640, 900), (640, 480, 960, 860), (850, 1020, 990, 1160)]:
        c.pen.rr(x0, y0, x1, y1, 50, fill=(236, 230, 214), outline=(180, 170, 150), w=3)

def city(c, name, at, col=INK, r=16):
    if not c.on(at): return
    x, y = CITIES[name]; c.sfx(at, 'pop')
    c.pen.circ(x, y, r * c.B(at, 0.3), fill=col, outline=INK, w=3)
    c.pen.text(x, y - 36, name, 'int', 24, INK)

def hook(c):
    worldmap(c)
    city(c, 'Virginia', c.T('Virginia'), RED, 22)
    city(c, 'Bengaluru', c.T('Bengaluru'), BLUE, 18)
    tr = c.T('crosses')
    if c.on(tr):
        x0, y0 = CITIES['Bengaluru']; x1, y1 = CITIES['Virginia']
        for k in range(3):
            t0 = tr + k * 1.0
            if t0 <= c.t <= t0 + 1.0:
                q = eio(lin(c.t, t0, t0 + 1.0)); a, b = ((x0, y0), (x1, y1)) if k % 2 == 0 else ((x1, y1), (x0, y0))
                c.pen.circ(a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q - 120 * math.sin(math.pi * q), 16, fill=YEL, outline=INK, w=3)
    tm = c.T('milliseconds')
    if c.on(tm): bignum(c, 540, 1300, '~250 ms round trip', tm, 70, RED)

def define(c):
    worldmap(c)
    title(c, 'EDGE RENDERING', 340, c.T('Edge'), 100, hlcol=YEL)
    tm = c.T('many')
    for k, n in enumerate(CITIES):
        city(c, n, tm + k * 0.15, GRN, 16)
    tc = c.T('CDNs')
    if c.on(tc): chapter(c, 540, 1270, 'S1 · E06', 'same places as the kirana store', tc)

def analogy(c):
    tf = c.T('franchise')
    if c.on(tf):
        c.pen.text(540, 350, 'THE FRANCHISE', 'osw', 72, INK)
    tc = c.T('central')
    if c.on(tc):
        node(c, 540, 560, 320, 200, 'central kitchen', tc, 'chef', size=30)
        arrow(c.pen, 540, 670, 540, 760, c.P(tc, 0.4), INK, 5, 16)
        txt(c, 540, 800, 'ships the recipe once', tc + 0.3, 'ints', 30, MUTE)
    to = c.T('outlets')
    if c.on(to):
        for k, nm in enumerate(['Delhi', 'Pune', 'Kochi', 'Jaipur']):
            node(c, 175 + k * 243, 960, 210, 150, nm, to + k * 0.15, 'chef', size=26)
    tl = c.T('locally')
    if c.on(tl): label(c, 540, 1130, 'same recipe, cooked locally', tl, YEL, INK, 32)

CODE = ['export default {', '  async fetch(request) {', "    const city = request.cf?.city ?? 'there';",
        '    return new Response(`<h1>Hello, ${city}!</h1>`, {', "      headers: { 'content-type': 'text/html' },", '    });', '  },', '};']

def how(c):
    code(c, 30, 340, 1050, 340 + 72 + 8 * 52 + 40, CODE, c.T('Worker'), 0.12, 25, 'worker.js', marks=[(2, c.T('city'), YEL), (3, c.T('HTML'), YEL)])
    tr = c.T('runtimes')
    if c.on(tr):
        proscons(c, 110, 940, 980, [(False, 'no full Node.js', c.T('Node')), (False, 'small memory, short CPU time', c.T('memory')),
                                     (True, 'great for personalization, redirects, A/B, auth', c.T('Great'))], 32, 85)

def gotcha(c):
    trap(c)
    worldmap(c)
    city(c, 'Singapore', c.T('edge'), GRN, 18)
    city(c, 'Virginia', c.T('database'), RED, 22)
    if c.on(c.T('database')):
        icon(c.pen, 'db', 250, 700, 0.9)
    tq = c.T('query')
    if c.on(tq):
        x0, y0 = CITIES['Singapore']; x1, y1 = CITIES['Virginia']
        for k in range(4):
            t0 = tq + k * 0.8
            if t0 <= c.t <= t0 + 0.8:
                q = eio(lin(c.t, t0, t0 + 0.8)); a, b = ((x0, y0), (x1, y1)) if k % 2 == 0 else ((x1, y1), (x0, y0))
                c.pen.circ(a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q - 140 * math.sin(math.pi * q), 14, fill=YEL, outline=INK, w=3)
        label(c, 540, 470, 'every query crosses the planet', tq, RED, WHITE, 30)
    tc = c.T('close')
    if c.on(tc): label(c, 540, 1280, 'edge helps only if data is close or cached', tc, GRN, WHITE, 30)

SCENES = [
    (hook, "Your server rendering runs in Virginia. A user opens the page from Bengaluru. Before the HTML even starts cooking, the request crosses the planet. That's about two hundred and fifty milliseconds, round trip."),
    (define, "Edge rendering runs your rendering code in many small data centers around the world. The same places CDNs cache your files. The page is rendered close to the user."),
    (analogy, "Instead of one central kitchen shipping food across the country, franchise outlets in every city cook the same recipe locally."),
    (how, "Here's a Cloudflare Worker. It reads the visitor's city, and returns personalized HTML from the nearest location. Edge runtimes are lighter, though. No full Node, small memory, and short CPU time. Great for personalization, redirects, A B tests, and auth checks."),
    (gotcha, "Interview trap: you move rendering to the edge, but your database is still in Virginia. Now every query crosses the planet, maybe several times per page. Edge rendering helps only when the data is also close, or cached."),
    (scene_next('S2 · E19', 'CASE STUDY', 'design the rendering for a store', 'case', 'store'),
     "Next: a case study. Design the rendering for a whole online store. Comment NOTES for the cheat sheet."),
]
