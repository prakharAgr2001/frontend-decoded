from engine.lib import *
from engine.shorts import big, emoji, bar, fox_img, paste

EP = dict(id='SH06', tag='SHORT', short='Charging 80 rocket 100 turtle', tail=1.2, style='meme', music=True, bpm=126, drop_scenes=(1, 6),
          hook='80% rocket, 100% kachua',
          caption=("Phone charging: 0→80% 🚀 … 80→100% 🐢\nKyun?! 😭\n\n"
                   "Battery = glass of water. Khaali ho toh full speed, bharne wala ho toh dheere, warna garmi = battery ka dushman 🔥\n\n"
                   "📌 Save this: keep it between 20–80%.\n"
                   "💬 Tumhara phone abhi kitne % pe hai?\n"
                   "📩 Send this to your 1%-battery friend."))

def s0(c):
    emoji(c, 'rocket', 230, 470, 230, -0.3)
    p = lin(c.t, 0, 1.0)
    bar(c, 380, 470, 960, 0.8 * eo(p), GRN, 90, f'{int(80 * eo(p))}%')
    tk = c.T('kachua')
    emoji(c, 'turtle', 230, 760, 230, tk)
    if c.on(tk): bar(c, 380, 760, 960, 0.8 + 0.2 * lin(c.t, tk, tk + 8), YEL, 90, f'{80 + int(20 * lin(c.t, tk, tk + 8))}%')
    tq = c.T('Kyun')
    big(c, 540, 1110, 'KYUN?!', 240, tq, RED, rot=-4, sound='thud')
    emoji(c, 'loudly-crying-face', 880, 1060, 170, tq + 0.1)

def s1(c):
    emoji(c, 'mobile-phone', 540, 640, 360, -0.3)
    big(c, 540, 1020, 'NOT TROLLING', 150, c.T('troll'), YEL, rot=3, sound='thud')
    emoji(c, 'face-with-rolling-eyes', 840, 470, 170, 0.2)

def glass(c, cx, y0, level, pour=False):
    w, h = 300, 470
    c.pen.poly([(cx - w / 2, y0), (cx + w / 2, y0), (cx + w / 2 - 40, y0 + h), (cx - w / 2 + 40, y0 + h)], (255, 255, 255, 30), WHITE, 8)
    lv = max(0, min(1, level)); top = y0 + h - h * lv
    if lv > 0.01:
        ins = lambda yy: (w / 2 - 40 * (yy - y0) / h - 10)
        c.pen.poly([(cx - ins(top), top), (cx + ins(top), top), (cx + ins(y0 + h) , y0 + h - 8), (cx - ins(y0 + h), y0 + h - 8)], (70, 160, 255))
    if pour: c.pen.rr(cx - 14, y0 - 260, cx + 14, top, 10, fill=(70, 160, 255))

def s2(c):
    big(c, 540, 380, 'BATTERY =', 140, -0.3, WHITE, sound=None)
    tg = c.T('glass')
    big(c, 540, 540, 'GLASS OF WATER', 120, tg, YEL)
    glass(c, 540, 700, 0.25 * c.P(tg, 0.5))

def s3(c):
    p = lin(c.t, 0, c.dur)
    glass(c, 540, 650, 0.1 + 0.6 * eo(p), pour=True)
    big(c, 540, 400, 'KHAALI? FULL SPEED', 110, -0.3, WHITE, sound=None)
    emoji(c, 'rocket', 860, 820, 200, 0.2)

def s4(c):
    p = lin(c.t, 0, c.dur)
    glass(c, 540, 650, 0.7 + 0.25 * p, pour=True)
    big(c, 540, 400, 'BHAR GAYA? DHEERE', 110, -0.3, WHITE, sound=None)
    to = c.T('overflow')
    if c.on(to):
        emoji(c, 'droplet', 330, 640, 120, to); emoji(c, 'droplet', 760, 600, 100, to + 0.1)
        big(c, 540, 1250, 'OVERFLOW!', 170, to, RED, rot=-5, sound='thud')

def s5(c):
    emoji(c, 'fire', 540, 600, 380, -0.3)
    big(c, 540, 930, 'GARMI =', 150, c.T('garmi'), WHITE)
    big(c, 540, 1110, 'BATTERY KA DUSHMAN', 110, c.T('dushman'), RED, rot=-3, sound='thud')
    emoji(c, 'thermometer', 880, 470, 170, 0.3)

def s6(c):
    big(c, 540, 360, 'PRO TIP', 170, -0.3, YEL, rot=-3, sound=None)
    emoji(c, 'pushpin', 860, 300, 140, 0.1)
    p = c.P(c.T('twenty'), 0.5)
    c.pen.rr(140, 640, 940, 760, 60, fill=(40, 42, 50), outline=WHITE, w=6)
    c.pen.rr(140 + 800 * 0.2, 652, 140 + 800 * (0.2 + 0.6 * p), 748, 50, fill=GRN)
    c.pen.text(140 + 800 * 0.2, 820, '20%', 'intx', 60, WHITE); c.pen.text(140 + 800 * 0.8, 820, '80%', 'intx', 60, WHITE)
    big(c, 540, 1060, 'SAVE THIS', 160, c.T('zyada'), GRN, rot=3, sound='thud')

def s7(c):
    emoji(c, 'eyes', 540, 560, 300, -0.3)
    big(c, 540, 900, 'TUMHARA PHONE', 120, 0.0, WHITE, sound=None)
    big(c, 540, 1060, 'KITNE % PE HAI?', 130, c.T('percent'), YEL, rot=-2)
    emoji(c, 'backhand-index-pointing-down', 540, 1270, 140, c.T('comment') if 'comment' in [w[0].lower().strip(',.') for w in c.words] else 0.6)

def s8(c):
    bar(c, 240, 420, 840, 0.02, RED, 120)
    c.pen.text(540, 420, '1%', 'intx', 80, RED)
    emoji(c, 'skull', 920, 420, 150, -0.3)
    big(c, 540, 640, 'BHEJO US DOST KO', 110, -0.3, WHITE, sound=None)
    big(c, 540, 790, 'JO 1% PE GHOOMTA HAI', 100, c.T('ghoomta'), YEL, rot=-2)
    tf = c.T('Follow')
    if c.on(tf):
        p = c.B(tf, 0.35)
        c.pen.circ(540, 1090, 190 * p, fill=YEL, outline=WHITE, w=6)
        paste(c, fox_img(), 540, 1100, 420 * p)

SCENES = [
    (s0, "Charging: eighty tak rocket. Sau tak kachua! Kyun?!"),
    (s1, "Phone tumhe troll nahi kar raha."),
    (s2, "Battery ek glass of water jaisi hai."),
    (s3, "Khaali hai? Full speed mein bharo."),
    (s4, "Bharne wala hai? Dheere, warna overflow."),
    (s5, "Battery mein overflow matlab garmi. Aur garmi, battery ki dushman."),
    (s6, "Pro tip: twenty se eighty ke beech rakho. Battery zyada din chalegi."),
    (s7, "Comment karo, tumhara phone abhi kitne percent pe hai?"),
    (s8, "Aur us dost ko bhejo jo ek percent pe ghoomta hai. Follow karo."),
]
