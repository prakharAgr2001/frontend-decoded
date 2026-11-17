from engine.lib import *
from engine.s5_extra import *

EP = dict(id='S5E04', tag='S5 · E04', short='BACKEND FOR FRONTEND')

SVC = ['user', 'orders', 'offers', 'recs', 'wallet']


def services(c, at, x=860, y0=440, gap=150, kws=None):
    boxes = []
    for k, s in enumerate(SVC):
        t = at_(c, kws[k]) if kws else at + k * 0.15
        boxes.append(node(c, x, y0 + k * gap, 240, 110, s, t, size=32))
    return boxes


def hook(c):
    ph = node(c, 200, 740, 220, 300, 'app', c.T('screen'), 'phone')
    tf = c.T('five', 1)
    bx = services(c, tf, kws=['User', 'orders', 'offers', 'recommendations', 'wallet'])
    tp = c.T('phone')
    if c.on(tp):
        for k, b in enumerate(bx): link(c, ph, b, tp + k * 0.12, 0.35, RED, 5)
    ts = c.T('stitches')
    if c.on(ts): stamp(c.cv, 540, 1250, '5 CALLS · ONE SCREEN', 64, c.P(ts, 0.35), -3, RED); c.sfx(ts, 'thud')


def problem(c):
    title(c, 'WHY IT HURTS', 340, 0.1, 100)
    rows(c, 100, 520, [(c.T('round'), 'each round trip: 100s of ms', 'on a mobile network', RED),
                       (c.T('fields'), 'fields it never shows', 'wasted bytes', ORANGE),
                       (c.T('repeats'), 'stitching repeated per client', 'web · iOS · Android', PURPLE)], gap=200, h=160)


def define(c):
    title(c, 'BACKEND FOR FRONTEND', 330, c.T('backend'), 80, hlcol=YEL)
    ph = node(c, 170, 760, 200, 260, 'app', 0.2, 'phone', sound=None)
    bff = node(c, 480, 760, 220, 220, 'BFF', c.T('owned'), 'server', fill=YEL, sub='frontend team')
    tf = c.T('fans')
    bx = services(c, tf, x=870, y0=480, gap=140)
    to = c.T('one')
    if c.on(to):
        link(c, ph, bff, to, 0.4, INK, 6)
        packet(c, ph, bff, to + 0.2, to + 1.0, YEL, '1 call')
    if c.on(tf):
        for k, b in enumerate(bx): link(c, bff, b, tf + k * 0.1, 0.3, INK, 4)
    tt = c.T('trims')
    if c.on(tt): packet(c, bff, ph, tt, tt + 1.0, GRN, 'screen data')


def agent(c):
    title(c, 'THE TRAVEL AGENT', 340, c.T('travel'), 90)
    person(c.pen, 200, 900, 1.6, BLUE)
    ag = node(c, 520, 780, 230, 200, 'agent', c.T('call'), 'phone')
    for k, kw in enumerate(('flight', 'hotel', 'cab')):
        node(c, 880, 560 + k * 200, 200, 120, kw, c.T(kw), size=34)
    ti = c.T('itinerary')
    if c.on(ti): label(c, 540, 1180, 'one call in · one itinerary out', ti, YEL, INK, 32)


def perclient(c):
    title(c, 'ONE BFF PER EXPERIENCE', 340, c.T('experience'), 76, hlcol=YEL)
    tm = c.T('mobile'); tw = c.T('web')
    a = node(c, 290, 620, 320, 180, 'mobile BFF', tm, 'phone', sub='small payloads')
    b = node(c, 790, 620, 320, 180, 'web BFF', tw, 'laptop', sub='richer pages')
    if c.on(tm):
        c.pen.rr(200, 790, 200 + 180 * c.P(tm + 0.3, 0.4), 830, 10, fill=GRN, outline=INK, w=3)
    if c.on(tw):
        c.pen.rr(660, 790, 660 + 280 * c.P(tw + 0.3, 0.4), 830, 10, fill=BLUE, outline=INK, w=3)
    ts = c.T('speed')
    if c.on(ts):
        svc = node(c, 540, 1060, 400, 130, 'shared services', ts, 'server', sound=None)
        link(c, a, svc, ts, 0.35); link(c, b, svc, ts + 0.1, 0.35)


def secrets(c):
    title(c, 'SECRETS STAY OFF THE DEVICE', 340, c.T('secrets'), 66, hlcol=YEL)
    br = node(c, 200, 720, 250, 230, 'browser', c.T('device'), 'laptop')
    bff = node(c, 540, 720, 220, 230, 'BFF', c.T('device'), 'lock', fill=YEL, sound=None)
    api = node(c, 880, 720, 220, 230, 'APIs', c.T('device'), 'server', sound=None)
    tt = c.T('tokens')
    if c.on(tt):
        link(c, bff, api, tt, 0.4)
        pill(c.pen, 710, 900, 'access token', c.B(tt, 0.35), WHITE, INK, 26)
    tc = c.T('cookie')
    if c.on(tc):
        link(c, bff, br, tc, 0.4)
        pill(c.pen, 370, 900, 'httpOnly cookie', c.B(tc, 0.35), GRN, WHITE, 26)
        txt(c, 540, 1070, 'JavaScript in the page never sees the token', tc, 'int', 32, INK)


def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    tp = c.T('pricing')
    if c.on(tp): txt(c, 540, 470, 'Put pricing rules in the BFF?', tp, 'intx', 50, INK)
    tn = c.T('No')
    if c.on(tn): stamp(c.cv, 540, 590, 'NO', 110, c.P(tn, 0.35), -5, RED); c.sfx(tn, 'thud')
    tsh = c.T('shaping')
    if c.on(tsh): label(c, 540, 730, 'BFF = shaping data for one screen', tsh, YEL, INK, 32)
    td = c.T('copy')
    if c.on(td):
        for k, nm in enumerate(('web BFF', 'iOS BFF', 'Android BFF')):
            x = 210 + k * 330
            node(c, x, 920, 280, 140, nm, td + k * 0.15, sub=['10% off', '12% off', '10% off'][k], size=30)
    tdr = c.T('drift')
    if c.on(tdr): stamp(c.cv, 540, 1130, 'RULES DRIFT APART', 64, c.P(tdr, 0.35), -3, RED); c.sfx(tdr, 'thud')


SCENES = [
    (hook, "Your app's home screen needs data from five services. User, orders, offers, recommendations, and wallet. So the phone makes five calls, on a patchy mobile network, and stitches it all together."),
    (problem, "Each round trip on mobile can cost hundreds of milliseconds. The phone downloads fields it never shows. And every client, web, iOS and Android, repeats the same stitching."),
    (define, "The fix is a backend for frontend. A small server, owned by the frontend team, sitting between the app and the services. The app makes one call. The BFF fans out, trims the fields, and returns exactly what the screen needs."),
    (agent, "It's like a travel agent. You make one call. They book the flight, the hotel and the cab, and hand you one itinerary."),
    (perclient, "Usually there's one BFF per experience. The mobile BFF sends small payloads. The web BFF can send richer pages. Each one changes at the speed of its own frontend."),
    (secrets, "A BFF also keeps secrets off the device. It holds the access tokens, and gives the browser only a secure, http only cookie."),
    (gotcha, "Interview trap. Should the BFF hold business logic, like pricing rules? No. It's for shaping data for one screen. Keep business rules in the services, or every BFF ends up with its own copy, and they drift apart."),
    (scene_next('S5 · E05', 'IQ: API DESIGN', '4 interview questions', 'four', 'API'),
     "Next: four interview questions on API design. Comment NOTES for the cheat sheet."),
]
