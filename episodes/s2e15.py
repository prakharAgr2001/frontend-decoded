from engine.s2_extra import *

EP = dict(id='S2E15', tag='S2 · E15', short='SERVER ACTIONS')

def hook(c):
    tf = c.T('submit')
    card(c.pen, 200, 330, 880, 560, 22, WHITE, 10, 5)
    c.pen.rr(250, 380, 830, 450, 12, outline=INK, w=3); c.pen.text(270, 415, 'Headphones · qty 1', 'int', 28, MUTE, 'lm')
    c.pen.rr(250, 470, 520, 530, 14, fill=YEL, outline=INK, w=4); c.pen.text(385, 500, 'Add to cart', 'int', 28, INK)
    if c.on(tf): c.pen.circ(470, 510, 20, fill=YEL, outline=INK, w=3)
    p = panel(c, 50, 620, 1030, 1180, ('Network',), 0)
    if c.on(tf + 0.4):
        c.pen.text(100, 760, 'localhost:3000/product/42', 'mono', 28, WHITE, 'lm'); c.pen.text(980, 760, 'POST', 'monob', 28, YEL, 'rm')
    th = c.T('header')
    if c.on(th):
        c.pen.text(100, 850, 'Next-Action:', 'monob', 30, CYAN, 'lm'); c.pen.text(330, 850, '7f3a9c…e21', 'mono', 30, WHITE, 'lm')
        c.pen.rr(84, 815, 1000, 885, 10, outline=YEL, w=4)
    tn = c.T('never')
    if c.on(tn): stamp(c.cv, 540, 1290, 'NO API ROUTE?', 76, c.P(tn, 0.4), -4, RED)

def define(c):
    title(c, 'SERVER ACTIONS', 340, c.T('Server'), 110, hlcol=YEL)
    tu = c.T('use')
    if c.on(tu): label(c, 540, 450, "a function marked 'use server'", tu, INK, WHITE, 32)
    a = node(c, 230, 760, 300, 220, 'client', c.T('call'), 'laptop', sub='addToCart(form)')
    b = node(c, 850, 760, 300, 220, 'server', c.T('turns'), 'server', sub='runs the function')
    tt = c.T('turns')
    if c.on(tt):
        packet(c, a, b, tt + 0.2, tt + 1.2, YEL, 'POST', off=-40)
        packet(c, b, a, tt + 1.3, tt + 2.3, CYAN, 'result', off=40)
    tb = c.T('behind')
    if c.on(tb): label(c, 540, 1010, 'React writes the fetch for you', tb, YEL, INK, 32)

def analogy(c):
    tb = c.T('bell')
    if c.on(tb):
        c.pen.text(540, 350, 'THE ROOM-SERVICE BELL', 'osw', 70, INK)
        card(c.pen, 90, 450, 470, 950, 22, WHITE, 10, 5); c.pen.text(280, 500, 'your room', 'int', 30, INK)
        c.pen.circ(280, 720, 70 * c.B(tb, 0.35), fill=YEL, outline=INK, w=6); c.pen.circ(280, 720, 22, fill=INK)
        card(c.pen, 610, 450, 990, 950, 22, DARK, 10, 5); c.pen.text(800, 500, 'kitchen', 'int', 30, WHITE)
        icon(c.pen, 'chef', 800, 720, 1.6, WHITE, DARK)
    tw = c.T('wiring')
    if c.on(tw):
        c.pen.line([(350, 720), (420, 720), (420, 1020), (680, 1020), (680, 720), (720, 720)], (150, 150, 150), 5)
        txt(c, 550, 1070, 'hidden wiring = a POST request', tw, 'ints', 30, MUTE)

CODE = ['// actions.js', "'use server';", 'export async function addToCart(formData) {', "  const id = formData.get('id');",
        '  await db.cart.add(id);', "  revalidatePath('/cart');", '}', '', '// <form action={addToCart}>…</form>']

def how(c):
    code(c, 40, 340, 1040, 340 + 72 + 9 * 52 + 40, CODE, c.T('directive'), 0.12, 28, 'actions.js',
         marks=[(1, c.T('directive'), YEL), (4, c.T('database'), YEL), (5, c.T('refresh'), YEL), (8, c.T('form'), YEL)])

def progressive(c):
    title(c, 'WORKS BEFORE JS', 340, c.T('before'), 100, hlcol=YEL)
    b = browser(c, 140, 460, 940, 900, url='shop.example.com')
    c.pen.rr(380, 650, 700, 730, 14, fill=YEL, outline=INK, w=4); c.pen.text(540, 690, 'Add to cart', 'int', 32, INK)
    tj = c.T('loads')
    if c.on(tj): label(c, 540, 820, 'JS: still loading…', tj, ORANGE, WHITE, 28)
    tc = c.T('classic')
    if c.on(tc):
        c.pen.circ(640, 710, 20, fill=YEL, outline=INK, w=3)
        label(c, 540, 1000, 'browser submits a classic form POST', tc, GRN, WHITE, 30)
    tp = c.T('progressive')
    if c.on(tp): txt(c, 540, 1100, '= progressive enhancement', tp, 'intx', 40, INK)

def proof(c):
    p = panel(c, 50, 330, 1030, 1120, ('Headers', 'Payload', 'Response'), 0, (1 - c.P(0, 0.45)) * 900)
    rows = [('Request Method', 'POST', 'POST'), ('Next-Action', '7f3a9c…e21', 'ID'), ('Content-Type', 'multipart/form-data', 'ID')]
    for i, (k, v, kw) in enumerate(rows):
        at = c.T(kw) + i * 0.2; y = 500 + i * 90
        if not c.on(at): continue
        c.sfx(at, 'tick')
        c.pen.text(100, y, k + ':', 'monob', 28, CYAN, 'lm'); c.pen.text(470, y, v, 'mono', 28, WHITE, 'lm')
    tn = c.T('code')
    if c.on(tn): label(c, 540, 820, 'an ID — not your function’s code', tn, YEL, INK, 30)
    tr = c.T('response')
    if c.on(tr): label(c, 540, 920, 'response = RSC payload with the updated UI', tr, WHITE, INK, 28)
    te = c.T('RSC')
    if c.on(te): chapter(c, 540, 1040, 'S2 · E14', 'the RSC payload', te)

def gotcha(c):
    trap(c)
    qtext(c, 'No API route, so a server action is private?', 450, c.T('private'), 48)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 640, 'NO', 110, c.P(tn, 0.35), -6, RED)
    tp = c.T('public')
    if c.on(tp): label(c, 540, 780, 'it is a PUBLIC POST endpoint', tp, RED, WHITE, 34)
    ta = c.T('Always')
    if c.on(ta):
        code(c, 80, 880, 1000, 880 + 72 + 4 * 52 + 30, ["'use server';", 'export async function deleteOrder(id) {', '  const user = await auth(); if (!user) throw …;',
                                                        '  const safeId = z.string().parse(id); // validate'], ta, 0.15, 26, 'actions.js', marks=[(2, c.T('auth'), YEL), (3, c.T('validate'), YEL)])

SCENES = [
    (hook, "In a Next dot js app, submit a form, and watch the Network panel. A POST request goes out, with a Next Action header. But you never wrote an API route."),
    (define, "These are Server Actions. A function marked use server, that you call from the client like a normal function. React turns that call into a POST request, behind the scenes."),
    (analogy, "It's like the room service bell in a hotel. You press the bell in your room, and the kitchen does the work. You never see the wiring."),
    (how, "Here's one. The use server directive at the top. Then normal server code: write to the database, and refresh the cart page's cache. And you can pass the action straight to a form."),
    (progressive, "Because it's a real form, it works even before JavaScript loads. If the page is still loading, the browser submits it like a classic form. That's progressive enhancement."),
    (proof, "In DevTools, the request shows a POST, with a Next Action ID, not your function's code. And the response is an RSC payload, with the updated UI."),
    (gotcha, "Interview trap: no API route, so a server action is private, right? No. It's a public POST endpoint. Anyone can call it with any arguments. Always check auth, and validate the input, inside the action."),
    (scene_next('S2 · E16', 'ISLANDS', 'a sea of HTML, islands of JS', 'islands', 'sea'),
     "Next: islands architecture. A sea of static HTML, with small islands of JavaScript. Comment NOTES for the cheat sheet."),
]
