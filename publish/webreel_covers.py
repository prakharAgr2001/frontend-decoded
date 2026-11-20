"""Designed Instagram covers for web reels (WRnn): blurred key frame + brand title strips + fox.
Usage: python3 -m publish.webreel_covers [WR01 ...]"""
import glob, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.lib import font, INK, YEL, RED, WHITE
from publish.make_covers import fox_img
C = {  # id: (title lines, hook, key-frame second)
    'WR01': (['YOUTUBE', 'ALMOST BROKE'], 'because of one number', 2.5),
    'WR02': (['8.5 MILLION', 'PCs. DEAD.'], 'one update did this', 2.2),
    'WR03': (['7 CRORE.', 'ONE BALL.'], "why Hotstar didn't crash", 1.5),
    'WR04': (['FACEBOOK', 'VANISHED'], 'gone from the internet for 6 hours', 1.6),
    'WR05': (['1 SETTING', 'BROKE THE WEB'], 'Amazon, Reddit, NYT: all down', 2.6),
    'WR06': (['0.1 SECOND', '= LOST SALES'], "Amazon's secret experiment", 1.2),
    'WR07': (['23 SECONDS', 'TO TAP'], 'how Pinterest fixed it', 1.5),
    'WR08': (['NETFLIX', 'DELETED REACT'], '…and got 50% faster', 2.0),
    'WR09': (['THE PAGE', 'JUMPED'], '…and you tapped an ad', 1.6),
    'WR10': (['HINGE USES', 'NOBEL MATH'], 'to pick your match', 1.4),
    'WR12': (['REBOOT EVERY', '248 DAYS'], 'or a Boeing 787 loses power', 1.0),
    'WR13': (['$440 MILLION', 'IN 45 MINUTES'], 'killed by old code', 1.2),
    'WR14': (['16,000 CASES', 'LOST IN EXCEL'], 'one hidden row limit', 1.2),
    'WR15': (['11 LINES', 'BROKE THE WEB'], 'the left-pad disaster', 1.0),
    'WR16': (['$125M LOST', 'TO UNITS'], 'pounds vs newtons', 1.2),
    'WR17': (['37 SECONDS', 'TO EXPLODE'], 'a number too big for 16 bits', 1.0),
    'WR18': (['2038:', 'TIME RUNS OUT'], 'computers will think it is 1901', 1.0),
    'WR19': (['GPS JUMPED', 'BACK 20 YEARS'], 'a 10-bit counter rolled over', 1.0),
    'WR20': (['ONE TYPO', 'BROKE THE WEB'], 'the S3 outage of 2017', 1.0),
    'WR21': (['ONE REGEX', '27 MIN OF 502s'], 'how Cloudflare went down', 1.0),
    'WR22': (['EXCEL RENAMED', 'HUMAN GENES'], 'well, scientists had to', 1.0),
    'WR11': (['AN AI SEES', 'IT FIRST'], 'what Bumble does to some photos', 1.4),
}
def cover(ep):
    lines, hook, t = C[ep]
    src = glob.glob(f'out/{ep}_*.mp4')[0]; fr = f'/tmp/{ep}_kf.jpg'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(t), '-i', src, '-frames:v', '1', fr], check=True)
    bg = Image.open(fr).convert('RGB').resize((1080, 1920)).filter(ImageFilter.GaussianBlur(14))
    im = ImageEnhance.Brightness(bg).enhance(.38); d = ImageDraw.Draw(im)
    f = font('int', 40); tag = 'TRUE STORY'; tw = f.getlength(tag)
    d.rounded_rectangle((540 - tw / 2 - 34, 400, 540 + tw / 2 + 34, 476), 38, fill=RED); d.text((540, 438), tag, font=f, fill=WHITE, anchor='mm')
    size = min(190, int(860 / max(font('osw', 100).getlength(l) for l in lines) * 100)); fo = font('osw', size); lh = size; y = 560
    for i, l in enumerate(lines):
        w = fo.getlength(l); x0, x1 = 540 - w / 2 - 34, 540 + w / 2 + 34; sk = 6 if i % 2 == 0 else -5
        d.polygon([(x0, y - 4 + sk), (x1 + 8, y - 14), (x1, y + lh - 14), (x0 + 6, y + lh - 4 - sk)], fill=YEL)
        d.text((540, y + lh // 2 - 6), l, font=fo, fill=INK, anchor='mm'); y += lh + 14
    d.text((540, y + 70), hook, font=font('int', 50), fill=WHITE, anchor='mm')
    fx = fox_img(380); im.paste(fx, (350, 1190), fx)
    d.text((540, 1620), 'TECH, EXPLAINED', font=font('osw', 60), fill=YEL, anchor='mm')
    return im
if __name__ == '__main__':
    for ep in sys.argv[1:] or list(C):
        cover(ep).save(f'covers/{ep}.jpg', quality=92)
    print('covers ok')
