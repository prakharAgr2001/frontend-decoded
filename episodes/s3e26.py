from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E26', tag='S3 · E26', short='WEB WORKERS')

def hook(c):
    tu = c.T('upload')
    if c.on(tu): node(c, 540, 450, 520, 150, 'orders.csv · 200,000 rows', tu, 'doc', size=32)
    tf = c.T('freezes')
    browser(c, 110, 600, 970, 1150, url='admin.example.com')
    c.pen.rr(380, 720, 700, 800, 20, fill=YEL, outline=INK, w=4); c.pen.text(540, 760, 'Export', 'intx', 34, INK)
    frozen = c.on(tf)
    a = 0 if frozen else (c.t * 400) % 360
    c.pen.arc(500, 880, 580, 960, a, a + 270, INK, 9)
    if frozen:
        stamp(c.cv, 540, 1010, 'FROZEN', 80, c.P(tf, 0.35), -4, RED); c.sfx(tf, 'thud')
    ts = c.T('spinning')
    if c.on(ts): txt(c, 540, 1240, 'even the spinner stops', ts, 'intx', 40, RED)

def define(c):
    title(c, 'WEB WORKERS', 330, c.T('Worker'), 110, hlcol=YEL)
    tm = c.T('separate')
    if c.on(tm):
        c.pen.text(110, 520, 'main thread', 'intx', 32, INK, 'lm')
        for k, (a, b, col) in enumerate(((0, 0.1, YEL), (0.15, 0.2, GRN), (0.3, 0.35, YEL), (0.45, 0.5, GRN), (0.6, 0.65, YEL), (0.75, 0.8, GRN))):
            c.pen.rect(110 + 860 * a, 560, 110 + 860 * b, 620, fill=col, outline=INK, w=3)
        c.pen.text(110, 720, 'worker thread', 'intx', 32, INK, 'lm')
        p = c.P(c.T('Heavy'), 1.5, lambda x: x)
        c.pen.rect(110, 760, 110 + 860 * p, 820, fill=ORANGE, outline=INK, w=3)
        if p > 0.2: c.pen.text(130, 790, 'parse 200k rows', 'int', 26, INK, 'lm')
    tf = c.T('free')
    if c.on(tf): label(c, 540, 940, 'main thread stays free for input + paint', tf, (200, 240, 200), INK, 32)

def kitchen(c):
    title(c, 'A SECOND CHEF', 330, c.T('second'), 110)
    card(c.pen, 90, 450, 560, 1000, 24, WHITE, 10, 5); c.pen.text(325, 500, 'dining room (DOM)', 'intx', 30, INK)
    for k in range(3): c.pen.rr(140 + k * 140, 820, 240 + k * 140, 900, 10, fill=LIGHT, outline=INK, w=3)
    icon(c.pen, 'chef', 325, 660, 1.5)
    tb = c.T('back')
    if c.on(tb):
        card(c.pen, 620, 450, 990, 1000, 24, (255, 238, 210), 10, 5); c.pen.text(805, 500, 'back room', 'intx', 30, INK)
        icon(c.pen, 'chef', 805, 660, 1.5 * c.B(tb, 0.4))
    td = c.T("can't")
    if c.on(td):
        c.pen.line([(590, 450), (590, 1000)], RED, 8)
        stamp(c.cv, 805, 860, 'NO DOM', 54, c.P(c.T('touch'), 0.35), -6, RED)
    ts = c.T('season')
    if c.on(ts): txt(c, 540, 1080, 'callback: the one-chef kitchen, S1 · E14', ts, 'ints', 30, MUTE)

def code_(c):
    code(c, 30, 330, 1050, 640, ["const worker = new Worker(new URL('./parse.worker.js', import.meta.url));", 'worker.postMessage(file);',
                                 'worker.onmessage = (e) => renderTable(e.data);'], c.T('send') - 0.5, 0.15, 20, 'main.js',
         marks=[(1, c.T('send'), YEL), (2, c.T('back', 1), YEL)])
    code(c, 30, 700, 1050, 1020, ['self.onmessage = async (e) => {', '  const rows = parseCSV(await e.data.text());', '  self.postMessage(rows);', '};'],
         c.T('worker', 2) - 0.3, 0.15, 26, 'parse.worker.js', marks=[(1, c.T('parses'), (60, 110, 70)), (2, c.T('posts'), YEL)])
    tm = c.T('messages')
    if c.on(tm): label(c, 540, 1110, 'they talk only through messages', tm, YEL, INK, 32)

def fits(c):
    title(c, 'GOOD FITS', 330, c.T('fits'), 110, hlcol=YEL)
    chips(c, 110, 500, [('parsing big files', (255, 238, 170)), ('image processing', (200, 220, 255)), ('search indexes', (200, 240, 200)),
                        ('encryption', (255, 220, 200)), ('diffing', (230, 210, 255))], c.T('parsing'), 0.35, 36)
    tc = c.T('CPU')
    if c.on(tc): txt(c, 540, 800, 'CPU-heavy, and no DOM needed', tc, 'intx', 42, INK)

def proof(c):
    panel(c, 50, 330, 1030, 1050, tabs=('Performance',), dy=(1 - c.P(0, 0.45)) * 900)
    tt = c.T('track')
    if c.on(tt):
        c.pen.text(100, 480, 'Main', 'int', 28, WHITE, 'lm')
        for a, b in ((0.05, 0.1), (0.3, 0.33), (0.6, 0.64), (0.85, 0.88)): c.pen.rect(240 + 740 * a, 460, 240 + 740 * b, 500, fill=YEL)
        c.pen.text(100, 620, 'Worker', 'int', 28, ORANGE, 'lm')
        p = c.P(tt, 1.2, lambda x: x); c.pen.rect(240, 600, 240 + 700 * p, 640, fill=ORANGE)
    tc = c.T('clear')
    if c.on(tc): txt(c, 540, 820, 'main thread stays clear', tc, 'intx', 40, GRN)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    txt(c, 540, 470, '"postMessage is free, right?"', c.T('free'), 'intx', 46, INK)
    tc = c.T('copied')
    if c.on(tc):
        node(c, 270, 650, 300, 130, 'main', tc, fill=WHITE)
        node(c, 810, 650, 300, 130, 'worker', tc, fill=(255, 238, 210))
        packet(c, (120, 585, 420, 715), (660, 585, 960, 715), tc, tc + 1.2, YEL, '50 MB copy')
        txt(c, 540, 780, 'structured clone = a full copy', tc + 0.3, 'ints', 32, INK)
    tb = c.T('block')
    if c.on(tb): stamp(c.cv, 540, 900, 'THE COPY BLOCKS', 64, c.P(tb, 0.35), -3, RED); c.sfx(tb, 'thud')
    tt = c.T('Transfer')
    if c.on(tt): code(c, 40, 990, 1040, 1150, ['worker.postMessage(buffer, [buffer]); // transfer, no copy'], tt, 0.1, 24, 'main.js', dy=0)

SCENES = [
    (hook, "You upload a CSV with two hundred thousand rows. While your app parses it, the page freezes. Buttons don't respond. Even the spinner stops spinning."),
    (define, "A Web Worker runs JavaScript on a separate thread. Heavy work moves there, and the main thread stays free for input and painting."),
    (kitchen, "Remember the one chef kitchen from season one? A worker is a second chef in a back room. They can cook anything, but they can't step into the dining room. Workers can't touch the DOM."),
    (code_, "You create the worker, send it the file, and listen for the result to come back. Inside the worker, it parses the rows, and posts them back. They talk only through messages."),
    (fits, "Good fits: parsing big files, image processing, search indexes, encryption, diffing. Anything CPU heavy that doesn't need the DOM."),
    (proof, "In the Performance panel, the worker gets its own track. The heavy work runs there, while the main thread stays clear."),
    (gotcha, "Interview trap: postMessage is free, right? No. Data is copied, using structured cloning. Send a huge object, and the copy itself can block the main thread. Transfer array buffers instead, or send less."),
    (scene_next('S3 · E27', 'WHY REACT RE-RENDERS', 'and the myth everyone believes', 'React', 'myth'),
     "Next: why React re renders, and the myth almost everyone believes. Comment NOTES for the cheat sheet."),
]
