"""Instagram cover images (1080x1920 JPEG). S1 has hand-written titles; other seasons derive from the episode EP dict
(EP['short'], optional EP['hook']). Usage: python3 -m publish.make_covers S2E01 S2E02 ...  (no args = all of S1)"""
import importlib, io, os, sys
import cairosvg
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.lib import font, PAPER, INK, YEL, RED, DARK, WHITE
from brand.fox import fox

PINKHL = (255, 150, 150)
# id: (title lines, hook, kind)
S1 = {
    1: (['URL TO', 'PIXELS'], '5 journeys in 1 second', ''),
    2: (['DNS'], "the internet's phonebook", ''),
    3: (['TCP', 'HANDSHAKE'], 'the phone call before every page', ''),
    4: (['HTTPS'], 'what the padlock really promises', ''),
    5: (['HTTP', '1 · 2 · 3'], 'why we needed HTTP/3', ''),
    6: (['CDNs'], "why servers don't melt", ''),
    7: (['INTERVIEW', 'Qs'], 'URL → pixels · test yourself', 'iq'),
    8: (['DOM +', 'CSSOM'], 'how HTML becomes a page', ''),
    9: (['LAYOUT', 'PAINT'], 'the rendering pipeline', ''),
    10: (['REFLOW VS', 'REPAINT'], 'which one is expensive?', ''),
    11: (['LAYOUT', 'THRASHING'], 'the loop that freezes pages', ''),
    12: (['SMOOTH', 'ANIMATION'], '60 fps, explained', ''),
    13: (['INTERVIEW', 'Qs'], 'rendering · test yourself', 'iq'),
    14: (['ONE', 'CHEF'], 'why JavaScript freezes', ''),
    15: (['CALL', 'STACK'], 'stack, queue, event loop', ''),
    16: (['MICRO', 'TASKS'], 'which runs first?', ''),
    17: (['16 MS'], 'the frame budget', ''),
    18: (['LONG', 'TASKS'], 'why clicks feel slow', ''),
    19: (['INTERVIEW', 'Qs'], 'predict the output', 'iq'),
    20: (['BUBBLING'], 'capture, target, bubble', ''),
    21: (['EVENT', 'DELEGATION'], 'one listener, 1,000 items', ''),
    22: (['MEMORY', 'LEAKS'], 'the tab that keeps growing', ''),
    23: (['OBSERVERS'], 'watch without polling', ''),
    24: (['INTERVIEW', 'Qs'], 'events & memory · test yourself', 'iq'),
    25: (['FINALE'], 'one click, explained', 'finale'),
}

_FOX = None
def fox_img(w):
    global _FOX
    if _FOX is None:
        svg = fox()
        svg = svg.replace('<rect width="1080" height="1080" fill="#111418"/>', '')
        svg = svg.replace('<circle cx="540" cy="560" r="400" fill="#FFD23F"/>', '')
        _FOX = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=1080, output_height=1080))).convert('RGBA')
    return _FOX.resize((w, w), Image.LANCZOS)

def split2(t):
    w = t.split()
    if len(w) < 2 or len(t) <= 9: return [t]
    best = min(range(1, len(w)), key=lambda i: abs(len(' '.join(w[:i])) - len(' '.join(w[i:]))))
    return [' '.join(w[:best]), ' '.join(w[best:])]

def spec(ep):
    s, n = int(ep[1:ep.index('E')]), int(ep[ep.index('E') + 1:])
    if s == 1: return S1[n]
    EP = importlib.import_module(f'episodes.s{s}e{n:02d}').EP
    short, hook = EP['short'].strip(), EP.get('hook', '')
    if short.upper().startswith('IQ:'):
        return ['INTERVIEW', 'Qs'], hook or short[3:].strip().lower() + ' · test yourself', 'iq'
    if short.upper().startswith('FINALE'):
        return ['FINALE'], hook or short.split(':', 1)[-1].strip().lower(), 'finale'
    return split2(short), hook, ''

def cover(ep):
    lines, hook, kind = spec(ep)
    dark = kind == 'finale'
    bg, fg = (DARK, WHITE) if dark else (PAPER, INK)
    im = Image.new('RGB', (1080, 1920), bg); d = ImageDraw.Draw(im)
    # episode pill
    tag = ep.replace('E', ' · E', 1); f = font('int', 44)
    tw = f.getlength(tag)
    d.rounded_rectangle((540 - tw / 2 - 34, 330, 540 + tw / 2 + 34, 410), 40, fill=YEL if dark else INK)
    d.text((540, 371), tag, font=f, fill=INK if dark else WHITE, anchor='mm')
    # title on highlighter strips
    size = min(200, int(820 / max(font('osw', 100).getlength(l) for l in lines) * 100))
    fo = font('osw', size); lh = int(size * 1.0); y = 560 + (2 - len(lines)) * lh // 2
    hlc = PINKHL if kind == 'iq' else YEL
    for i, l in enumerate(lines):
        w = fo.getlength(l); x0, x1 = 540 - w / 2 - 36, 540 + w / 2 + 36
        sk = 6 if i % 2 == 0 else -5
        d.polygon([(x0, y + 12 + sk), (x1 + 8, y - 4), (x1, y + lh - 30), (x0 + 6, y + lh - 16 - sk)], fill=hlc)
        d.text((540, y + lh // 2 - 8), l, font=fo, fill=INK, anchor='mm')
        y += lh
    if hook: d.text((540, y + 60), hook, font=font('int', 48), fill=fg, anchor='mm')
    fx = fox_img(560); im.paste(fx, (260, 1150), fx)
    d.text((540, 1832), 'TECH, EXPLAINED', font=font('osw', 64), fill=YEL if dark else RED, anchor='mm')
    return im

if __name__ == '__main__':
    os.makedirs('covers', exist_ok=True)
    for ep in sys.argv[1:] or [f'S1E{n:02d}' for n in S1]:
        cover(ep).save(f'covers/{ep}.jpg', quality=92)
    print('covers ok')
