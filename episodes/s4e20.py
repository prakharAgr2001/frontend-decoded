from engine.lib import *
from engine.s3_extra import rows
from engine.s2_extra import trap, verdict
from engine.s4_extra import *

EP = dict(id='S4E20', tag='S4 · E20', short='STATE MACHINES')


def hook(c):
    ib = phone_frame(c, 540, 780, 460, 700)
    x0, y0, x1, y1 = ib
    c.pen.text(x0 + 30, y0 + 50, 'Pay ₹448', 'intx', 40, INK, 'lm')
    c.pen.rr(x0 + 30, y0 + 140, x1 - 30, y0 + 230, 18, fill=GRN)
    a = (c.t * 400) % 360
    cx = (x0 + x1) / 2
    c.pen.arc(cx - 30, y0 + 155, cx + 30, y0 + 215, a, a + 270, WHITE, 8)
    te = c.T('error')
    if c.on(te):
        c.pen.rr(x0 + 30, y0 + 280, x1 - 30, y0 + 380, 14, fill=(255, 225, 225), outline=RED, w=3)
        c.pen.text(cx, y0 + 330, 'Payment failed', 'int', 30, RED)
    tb = c.T('together')
    if c.on(tb):
        objcard(c, 140, 1180, 940, ['isLoading: true,  isError: true'], tb, 'state', 30, dy=0)


def soup(c):
    head(c, 'BOOLEAN SOUP', 'soup', size=96)
    code(c, 30, 440, 1050, 700, ['const [isLoading, setLoading] = useState(false);', 'const [isError, setError] = useState(false);',
                                 'const [isSuccess, setSuccess] = useState(false);'], c.T('Three'), 0.2, 24, 'Pay.jsx')
    te = c.T('eight')
    if c.on(te):
        for k in range(8):
            x = 160 + (k % 4) * 255; y = 820 + (k // 4) * 130
            valid = k in (0, 1, 2, 4)
            tv = c.T('valid')
            col = ((200, 240, 200) if valid else (255, 210, 210)) if c.on(tv) else WHITE
            node(c, x, y, 220, 100, format(k, '03b').replace('0', 'F ').replace('1', 'T ').strip(), te + k * 0.1, fill=col, size=28)
    tv = c.T('valid')
    if c.on(tv): label(c, 540, 1100, '8 combinations · only 4 make sense', tv, YEL, INK, 32)


def signal(c):
    title(c, 'THE TRAFFIC SIGNAL', 330, 0.1, 100)
    tn = c.T('never')
    cyc = [RED, YEL, GRN]
    ph = int(max(0, c.t - c.T('moves')) / 1.0) % 3 if c.on(c.T('moves')) else 0
    card(c.pen, 400, 440, 680, 1060, 40, INK, 12, 5)
    for k, col in enumerate(cyc):
        lit = (2 - ph) % 3 == k if c.on(c.T('moves')) else k == 0
        c.pen.circ(540, 540 + k * 200, 80, fill=col if lit else (60, 60, 64), outline=INK, w=4)
    if c.on(tn): label(c, 540, 1140, 'never red and green at once', tn, (255, 210, 210), INK, 32)
    ta = c.T('allowed')
    if c.on(ta): label(c, 540, 1240, 'green → yellow → red → green', ta, YEL, INK, 32)


def fsm(c):
    title(c, 'FINITE STATE MACHINE', 330, 0.1, 86, hlcol=YEL)
    idle = node(c, 220, 560, 280, 120, 'idle', c.T('states'), size=36)
    sub = node(c, 760, 560, 320, 120, 'submitting', c.T('states') + 0.2, size=36, fill=(255, 238, 170))
    ok = node(c, 760, 900, 280, 120, 'success', c.T('states') + 0.4, size=36, fill=(200, 240, 200))
    er = node(c, 220, 900, 280, 120, 'error', c.T('states') + 0.6, size=36, fill=(255, 210, 210))
    te = c.T('events')
    link(c, idle, sub, te, txt_='SUBMIT'); link(c, sub, ok, te + 0.3, txt_='OK'); link(c, sub, er, te + 0.6, txt_='FAIL')
    link(c, er, sub, c.T('retry'), txt_='RETRY', off=100)
    to = c.T('exactly')
    if c.on(to): label(c, 540, 1120, 'always exactly one state', to, YEL, INK, 34)


def table(c):
    title(c, 'TRANSITIONS AS DATA', 330, 0.1, 90, hlcol=YEL)
    code(c, 30, 430, 1050, 900, ['const machine = {', "  idle:       { SUBMIT: 'submitting' },", "  submitting: { OK: 'success', FAIL: 'error' },",
                                 "  error:      { RETRY: 'submitting' },", '  success:    {},', '};', 'const next = (s, e) => machine[s][e] ?? s;'],
         c.T('table'), 0.12, 26, 'payMachine.js', marks=[(2, c.T('click'), YEL), (6, c.T('ignored'), YEL)])
    tc = c.T('click')
    if c.on(tc): label(c, 540, 990, 'SUBMIT while submitting → no such event → ignored', tc + 0.6, (200, 240, 200), INK, 28)


def xstate(c):
    title(c, 'XSTATE', 340, c.T('XState'), 130, hlcol=YEL)
    rows(c, 90, 520, [(c.T('nested'), 'nested and parallel states', None, BLUE), (c.T('guards'), 'guards, delays, side effects', None, PURPLE),
                      (c.T('diagram'), 'see the machine as a diagram', 'Stately visual editor', ORANGE)], 160, 900, 130, 36, 26)
    tw = c.T('checkout')
    if c.on(tw):
        for k, s_ in enumerate(('checkout', 'onboarding', 'video player', 'file upload')):
            label(c, 300 + (k % 2) * 480, 1000 + (k // 2) * 100, s_, tw + k * 0.2, WHITE, INK, 30)
    tt = c.T('toggle')
    if c.on(tt): label(c, 540, 1220, 'not for a simple toggle', tt, (255, 210, 210), INK, 30)


def gotcha(c):
    trap(c, 'Interview')
    txt(c, 540, 460, 'How do you stop a double payment?', c.T('double'), 'intx', 46, INK)
    rows(c, 90, 620, [(c.T('ignores'), 'machine ignores SUBMIT while submitting', None, 'ok'), (c.T('disable'), 'disable the button', 'but never rely on it alone', 'ok'),
                      (c.T('idempotency'), 'idempotency key on the server', 'same key twice = charged once', 'ok')], 160, 900, 130, 34, 26)


SCENES = [
    (hook, "A payment screen shows a spinner, and an error message, at the same time. Because the code said is loading, true, and is error, true. Together."),
    (soup, "This is boolean soup. Three booleans give eight possible combinations. Only four of them are valid. The other four are bugs waiting to happen."),
    (signal, "Think of a traffic signal. It's never red and green at once. It's in exactly one state, and it moves only along allowed paths."),
    (fsm, "That's a finite state machine. A fixed set of states: idle, submitting, success, error. Events move it from one to the next: submit, ok, fail, and retry. It's always in exactly one state."),
    (table, "You can write it as a plain table. Each state lists the events it accepts. A double click on pay while submitting? There's no submit event in that state, so it's ignored."),
    (xstate, "For complex flows, XState adds nested and parallel states, guards, and timers, and you can see the machine as a diagram. Use it for checkout, onboarding, a video player, or a file upload. Not for a simple toggle."),
    (gotcha, "Interview question: how do you stop a double payment on a double click? The machine ignores submit while submitting. Disable the button too. And send an idempotency key, so the server charges once, even if a request arrives twice."),
    (scene_next('S4 · E21', 'IMMER', 'mutate without mutating', 'Immer', 'mutating'),
     "Next: Immer, and how to mutate without mutating. Comment NOTES for the cheat sheet."),
]
