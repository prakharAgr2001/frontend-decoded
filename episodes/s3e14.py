from engine.lib import *
from engine.s3_extra import *

EP = dict(id='S3E14', tag='S3 · E14', short='TREE SHAKING')

def hook(c):
    code(c, 60, 380, 1020, 560, ["import _ from 'lodash';"], max(0.05, c.T('import') - 0.3), 0.1, 34, 'app.js')
    tg = c.T('grows')
    if c.on(tg):
        timerbar(c, 140, 700, 940, c.P(tg, 1.0), tg, 'bundle size', RED, 60)
        counter(c, 540, 870, 0, 70, tg, tg + 1.0, '+{:.0f}', 110, RED, ' KB')
    tu = c.T('used')
    if c.on(tu): txt(c, 540, 1010, 'you used: _.debounce', tu, 'mono', 40, INK)
    tw = c.T('whole')
    if c.on(tw): stamp(c.cv, 540, 1170, 'SHIPPED THE WHOLE LIBRARY', 56, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')

def define(c):
    title(c, 'TREE SHAKING', 330, c.T('Tree'), 110, hlcol=YEL)
    used = c.on(c.T('used'))
    nodes = [('entry', 'main.js', 540, 480, None, 'entry'), ('a', 'cart.js', 330, 620, 'entry', 'follow'), ('b', 'utils.js', 750, 620, 'entry', 'follow'),
             ('c', 'formatPrice', 200, 780, 'a', 'mark'), ('d', 'debounce', 460, 780, 'b', 'mark'), ('e', 'deepClone', 700, 780, 'b', 'rest'),
             ('f', 'parseCSV', 900, 780, 'b', 'rest')]
    def col(k):
        if k in ('e', 'f') and c.on(c.T('rest')): return (255, 210, 210)
        if k in ('c', 'd') and c.on(c.T('used')): return (200, 240, 200)
        return WHITE
    tree(c, nodes, c.T('entry'), 0.2, col, 26)
    tr = c.T('rest')
    if c.on(tr):
        for x in (700, 900): cross(c.pen, x, 860, 0.8, RED, 7, c.P(tr, 0.3))
        txt(c, 540, 960, 'unused exports → left out', tr, 'intx', 38, RED)

def shake(c):
    tr = c.T('Shake')
    c.pen.rect(510, 700, 570, 1150, fill=(120, 80, 50), outline=INK, w=4)
    sw = 14 * math.sin(c.t * 18) * (1 - lin(c.t, tr + 1.2, tr + 1.6)) if c.on(tr) else 0
    for k, (dx, dy, alive) in enumerate([(-200, -80, True), (-120, -220, False), (0, -280, True), (130, -200, True), (220, -60, False), (-60, -40, True), (90, -120, False)]):
        x, y = 540 + dx + sw, 640 + dy
        if alive or not c.on(c.T('dead')):
            c.pen.circ(x, y, 70, fill=GRN if alive else (190, 150, 70), outline=INK, w=4)
        else:
            q = c.P(c.T('dead') + k * 0.05, 0.8, lambda z: z * z)
            c.pen.circ(x + 30 * q, y + 600 * q, 40, fill=(190, 150, 70), outline=INK, w=3)
    tl = c.T('live')
    if c.on(tl): label(c, 540, 1240, 'used code stays · dead code falls', tl, YEL, INK, 34)

def esm(c):
    title(c, 'NEEDS ES MODULES', 330, c.T('ES'), 96)
    versus(c, ('ESM', GRN, c.T('static'), [('top', 'import / export at top level'), ('graph', 'graph known before code runs')]),
           ('CommonJS', RED, c.T('CommonJS'), [('dynamic', 'require() can be dynamic'), ('keep', 'bundler keeps all of it')]), 450, 900)
    code(c, 60, 960, 1020, 1200, ["import { debounce } from 'lodash-es';  // shakeable", "const _ = require('lodash');           // not"],
         c.T('CommonJS'), 0.3, 24, 'compare.js')

def side(c):
    title(c, 'SIDE EFFECTS', 330, c.T('side'), 110, hlcol=(255, 210, 180))
    code(c, 60, 450, 1020, 650, ["import './polyfills.js';  // changes globals!"], c.T('global') - 0.3, 0.1, 30, 'main.js', marks=[(0, c.T('global'), (120, 60, 60))])
    td = c.T('dropped')
    if c.on(td): txt(c, 540, 720, "can't be dropped, even if nothing is imported", td, 'intx', 34, RED)
    code(c, 60, 820, 1020, 1100, ['// package.json', '"sideEffects": false', '// or: "sideEffects": ["*.css"]'], c.T('package') - 0.4, 0.2, 30, 'package.json', lang='json',
         marks=[(1, c.T('package'), (60, 110, 70))])

def proof(c):
    title(c, 'BUNDLE ANALYZER', 330, c.T('analyzer'), 96)
    tw = c.T('everything')
    if c.on(tw):
        p = c.P(tw, 0.5); c.pen.rect(110, 460, 110 + 860 * p, 760, fill=(255, 210, 210), outline=INK, w=4)
        for k in range(24): c.pen.rect(130 + (k % 8) * 104, 480 + (k // 8) * 90, 220 + (k % 8) * 104, 555 + (k // 8) * 90, fill=(240, 170, 170), outline=INK, w=2)
        txt(c, 540, 800, "import _ from 'lodash'  ·  ~70 KB", tw, 'mono', 32, RED)
    tl = c.T('lodash', 2)
    if c.on(tl):
        p = c.P(tl, 0.5); c.pen.rect(110, 900, 110 + 170 * p, 1060, fill=(200, 240, 200), outline=INK, w=4)
        txt(c, 640, 960, "import { debounce } from 'lodash-es'", tl, 'mono', 24, GRN)
        txt(c, 640, 1020, 'one small module', tl + 0.3, 'intx', 32, GRN)

def gotcha(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    title(c, 'BARREL FILES', 495, c.T('barrel'), 96, hlcol=YEL)
    code(c, 60, 580, 1020, 820, ["export * from './Button';", "export * from './Chart';    // heavy, side effects", "export * from './DataGrid';"],
         c.T('re') - 0.3, 0.15, 26, 'components/index.js', marks=[(1, c.T('effects'), (120, 60, 60))])
    to = c.T('one', 2)
    if c.on(to): txt(c, 540, 880, "import { Button } from './components'", to, 'mono', 30, INK)
    tw = c.T('whole')
    if c.on(tw): stamp(c.cv, 540, 1030, 'PULLS IN EVERYTHING', 64, c.P(tw, 0.35), -3, RED); c.sfx(tw, 'thud')
    tf = c.T('directly')
    if c.on(tf): label(c, 540, 1180, "fix: import from './components/Button' directly", tf, (200, 240, 200), INK, 30)

SCENES = [
    (hook, "You import one tiny function from a utility library. Your bundle grows by seventy kilobytes. You used one function. You shipped the whole library."),
    (define, "Tree shaking is how bundlers drop code you never use. They follow your imports from the entry file, mark every export that's actually used, and leave the rest out."),
    (shake, "Shake a tree, and the dead leaves fall. Whatever is still attached to a live branch stays."),
    (esm, "It only works because ES modules are static. Imports and exports sit at the top level, so the bundler can see the whole graph before any code runs. CommonJS require can be dynamic, so bundlers usually keep all of it."),
    (side, "Bundlers also worry about side effects. If importing a file might change something global, it can't be dropped. So libraries mark themselves safe with a side effects flag in package dot json."),
    (proof, "Open a bundle analyzer and compare. Importing everything from lodash brings the whole library. Importing debounce from lodash dash E S brings one small module."),
    (gotcha, "Interview trap: barrel files. An index file that re exports everything looks clean. But if one module in it has side effects, importing one button can pull in the whole library. Import from the file directly."),
    (scene_next('S3 · E15', 'BUNDLE DIET', 'cut kilobytes your users pay for', 'bundle', 'kilobytes'),
     "Next: the bundle diet, cutting the kilobytes your users pay for. Comment NOTES for the cheat sheet."),
]
