from engine.s2_extra import *

EP = dict(id='S2E09', tag='S2 · E09', short='HYDRATION MISMATCH')

def hook(c):
    tc = c.T('console')
    console(c, 50, 360, 1030, 760, [], (1 - c.P(0, 0.45)) * 900)
    te = c.T('Hydration')
    if c.on(te):
        c.sfx(te, 'buzz')
        c.pen.rr(80, 450, 1000, 700, 12, fill=(80, 30, 36), outline=RED, w=3)
        for i, ln in enumerate(['Hydration failed because the server', 'rendered HTML didn’t match the client.', 'This tree will be regenerated', 'on the client.']):
            if c.on(te + i * 0.3): c.pen.text(110, 500 + i * 56, ln, 'mono', 28, (255, 160, 160), 'lm')
    tw = c.T('mean')
    if c.on(tw): stamp(c.cv, 540, 960, 'WHAT DOES IT MEAN?', 64, c.P(tw, 0.4), -4, RED)

def rule(c):
    title(c, 'THE RULE', 340, c.T('expects'), 110, hlcol=YEL)
    ts, tb = c.T('server'), c.T('browser')
    if c.on(ts):
        card(c.pen, 90, 460, 510, 760, 20, WHITE, 8, 4)
        c.pen.text(300, 510, 'server HTML', 'int', 30, MUTE); c.pen.text(300, 640, '<p>10:00:01</p>', 'monob', 34, INK)
    if c.on(tb):
        card(c.pen, 570, 460, 990, 760, 20, WHITE, 8, 4)
        c.pen.text(780, 510, 'first browser render', 'int', 30, MUTE); c.pen.text(780, 640, '<p>10:00:01</p>', 'monob', 34, INK)
    te = c.T('exactly')
    if c.on(te): bignum(c, 540, 900, '=', te, 160, GRN)
    tsf = c.T('safely')
    if c.on(tsf): label(c, 540, 1100, 'otherwise React can’t safely attach', tsf, RED, WHITE, 32)

def analogy(c):
    tt = c.T('tracing')
    if c.on(tt):
        c.pen.text(540, 350, 'TRACING PAPER', 'osw', 72, INK)
        card(c.pen, 190, 450, 890, 1050, 20, WHITE, 10, 5)
        c.pen.circ(540, 700, 160, outline=INK, w=8); c.pen.rect(400, 880, 680, 960, outline=INK, w=8)
    tl = c.T('line')
    if c.on(tl):
        off = 0 if not c.on(c.T('shifts')) else 50 * c.P(c.T('shifts'), 0.5)
        c.pen.circ(540 + off, 700 + off * 0.4, 160, outline=(80, 140, 230), w=6); c.pen.rect(400 + off, 880 + off * 0.4, 680 + off, 960 + off * 0.4, outline=(80, 140, 230), w=6)
        c.pen.rr(200, 460, 880, 1040, 18, fill=None, outline=(80, 140, 230), w=3)
    tm = c.T('mess')
    if c.on(tm): stamp(c.cv, 540, 1180, 'MISMATCH', 90, c.P(tm, 0.4), -5, RED)

def culprits(c):
    code(c, 40, 340, 1040, 340 + 72 + 4 * 52 + 30, ['function Footer() {', '  return <p>{new Date().toLocaleTimeString()}</p>;', '}',
                                                   '// server 10:00:01 · browser 10:00:03'], c.T('time'), 0.15, 27, 'Footer.jsx', marks=[(1, c.T('time'), YEL)])
    tc = c.T('usual')
    if c.on(tc):
        chips(c, 80, 760, [('Date.now()', YEL), ('Math.random()', YEL), ('window / localStorage', YEL), ('timezone & locale', YEL),
                           ('<div> inside <p>', YEL), ('browser extensions', YEL)], tc, 0.45, 32)

FIX = ['function Clock() {', '  const [time, setTime] = useState(null);', '  useEffect(() => {', '    setTime(new Date().toLocaleTimeString());',
       '  }, []);', "  return <p>{time ?? '--:--'}</p>;", '}']

def fix(c):
    code(c, 40, 340, 1040, 340 + 72 + 7 * 52 + 40, FIX, c.T('Render'), 0.12, 28, 'Clock.jsx',
         marks=[(5, c.T('placeholder'), YEL), (2, c.T('useEffect'), YEL), (3, c.T('useEffect'), YEL)])
    tp = c.T('both')
    if c.on(tp): label(c, 540, 900, "server + first render: '--:--'  (same)", tp, YEL, INK, 30)
    ta = c.T('after')
    if c.on(ta): label(c, 540, 990, 'then the effect fills in the real time', ta, GRN, WHITE, 30)
    ts = c.T('suppressHydrationWarning')
    if c.on(ts): txt(c, 540, 1110, 'tiny unavoidable diff? suppressHydrationWarning', ts, 'ints', 30, MUTE)

def gotcha(c):
    trap(c)
    code(c, 60, 450, 1020, 450 + 72 + 2 * 54 + 30, ["const theme = typeof window !== 'undefined'", "  ? localStorage.theme : 'light';"], c.T('typeof'), 0.15, 28, 'Header.jsx', dy=0)
    tb = c.T('Because')
    if c.on(tb):
        txt(c, 300, 790, "server: 'light'", tb, 'monob', 36, INK); txt(c, 790, 790, "browser: 'dark'", tb + 0.3, 'monob', 36, INK)
        bignum(c, 540, 790, '≠', tb + 0.5, 90, RED)
    tm = c.T('mismatch')
    if c.on(tm): stamp(c.cv, 540, 940, 'THAT IS THE MISMATCH', 60, c.P(tm, 0.4), -3, RED)
    te = c.T('effect')
    if c.on(te): label(c, 540, 1100, 'browser-only values → read them in useEffect', te, GRN, WHITE, 30)

SCENES = [
    (hook, "Open the console on a React app in development, and you might see this. Hydration failed because the server rendered HTML didn't match the client. What does that actually mean?"),
    (rule, "Hydration expects one thing. The server's HTML, and the browser's first render, must be exactly the same. If they're not, React can't safely attach to the page, and throws that part away."),
    (analogy, "Think of tracing paper. You lay it over a drawing, and trace every line. If the drawing shifts underneath, nothing lines up, and you get a mess."),
    (culprits, "The usual cause? Something that changes between server and browser. Like the current time. The server renders ten oh one, the browser renders ten oh three. The usual suspects: dates, random numbers, window or localStorage, time zones and locales, invalid HTML nesting, and even browser extensions."),
    (fix, "The fix: Render the same placeholder on both sides, then fill in the browser-only value in useEffect, which only runs after hydration. For a tiny unavoidable difference, like a timestamp, there's suppressHydrationWarning."),
    (gotcha, "Interview trap: why not just check typeof window during render? Because then the server and the browser render different things. And that's exactly a mismatch. Browser-only values belong in an effect."),
    (scene_next('S2 · E10', 'VISIBLE, NOT CLICKABLE', 'the uncanny valley', 'visible', 'uncanny'),
     "Next: visible, but not clickable. The uncanny valley of server rendering. Comment NOTES for the cheat sheet."),
]
