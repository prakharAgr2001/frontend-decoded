from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E06', tag='S6 · E06', short='WEBRTC')


def hook(c):
    tt = c.T('tab')
    addressbar(c, 90, 360, 990, typed_text(c, 'chrome://webrtc-internals', tt, 0.06), True, 40, 92)
    tp = c.T('peer')
    if c.on(tp):
        x0, y0, x1, y1 = panel(c, 60, 510, 1020, 1200, tabs=('RTCPeerConnection',), dy=(1 - c.P(tp, 0.45)) * 900)
        kv(c, x0 + 40, y0 + 60, x1, [(tp + 0.3, 'connectionState:', 'connected', GRN), (tp + 0.6, 'kind:', 'audio + video', WHITE)], 28, 60)
        tg = c.T('graphs')
        if c.on(tg):
            pts = []
            for k in range(60):
                x = x0 + 50 + k * 14
                if tg + k * 0.03 > c.t: break
                y = y0 + 460 - 120 * (0.5 + 0.4 * math.sin(k * 0.45) + 0.1 * math.sin(k * 1.7))
                pts.append((x, y))
            if len(pts) > 1: c.pen.line(pts, GRN, 5)
            c.pen.text(x0 + 50, y0 + 230, 'bytesReceived/s', 'mono', 24, (150, 156, 166), 'lm')


def detour(c):
    tf = c.T('frame')
    a = node(c, 200, 900, 220, 170, 'You', 0.2, 'laptop')
    b = node(c, 880, 900, 220, 170, 'Friend', 0.3, 'laptop')
    s = node(c, 540, 520, 240, 170, 'Server', c.T('server'), 'server', fill=LIGHT)
    if c.on(tf):
        link(c, a, s, tf, col=MUTE); link(c, s, b, tf + 0.2, col=MUTE)
        for k in range(4):
            packet(c, a, s, tf + k * 0.5, tf + k * 0.5 + 0.5, YEL, r=14)
            packet(c, s, b, tf + k * 0.5 + 0.5, tf + k * 0.5 + 1.0, YEL, r=14)
        txt(c, 540, 700, 'up, then down', tf + 0.4, 'ints', 30, MUTE)
    tw = c.T('WebRTC')
    if c.on(tw):
        pipe(c, 320, 760, 900, tw, GRN, 46)
        blips(c, 320, 760, 900, tw + 0.3, 99, 0.35, True, WHITE, 11, 0.5)
        label(c, 540, 1100, 'direct: audio · video · data', tw + 0.4, (200, 240, 200), INK, 32)


def party(c):
    title(c, 'THE INTRODUCTION', 330, c.T('introduced'), 90, hlcol=YEL)
    person(c.pen, 220, 900, 1.3, BLUE); person(c.pen, 860, 900, 1.3, ORANGE)
    tf = c.T('friend')
    if c.on(tf): person(c.pen, 540, 760, 1.1, GRN)
    tt = c.T('tells')
    if c.on(tt):
        pill(c.pen, 320, 560, 'meet Asha, table 4', c.B(tt, 0.35), WHITE, INK, 26)
        pill(c.pen, 760, 560, 'meet Kabir, table 9', c.B(tt + 0.3, 0.35), WHITE, INK, 26)
    td = c.T('directly')
    if c.on(td):
        arrow(c.pen, 290, 980, 790, 980, c.P(td, 0.4), INK, 7)
        arrow(c.pen, 790, 1020, 290, 1020, c.P(td + 0.2, 0.4), INK, 7)
    ti = c.T('isn')
    if c.on(ti): label(c, 540, 1160, 'the friend steps away', ti, YEL, INK, 32)


def signal(c):
    a = node(c, 170, 760, 220, 160, 'Browser A', 0.2, 'laptop', size=30)
    b = node(c, 910, 760, 220, 160, 'Browser B', 0.3, 'laptop', size=30)
    s = node(c, 540, 440, 300, 150, 'Signaling', c.T('signaling'), 'server', size=30)
    to = c.T('offer')
    link(c, a, s, to, txt_='offer', off=-20)
    link(c, s, b, to + 0.4, txt_='offer', off=20)
    ta = c.T('answer')
    link(c, b, s, ta, txt_='answer', off=-20)
    link(c, s, a, ta + 0.4, txt_='answer', off=20)
    tc = c.T('codecs')
    if c.on(tc): txt(c, 540, 960, 'offer / answer = SDP: codecs, formats', tc, 'ints', 32, INK)
    ti = c.T('ICE')
    if c.on(ti): txt(c, 540, 1030, 'ICE candidates = possible addresses', ti, 'ints', 32, INK)
    tu = c.T('Usually')
    if c.on(tu): label(c, 540, 1160, 'how? your choice — usually a WebSocket', tu, YEL, INK, 32)


def nat(c):
    title(c, 'THE HARD PART: ROUTERS', 330, c.T('routers'), 76, hlcol=YEL)
    a = node(c, 170, 780, 220, 150, 'You', 0.2, 'laptop')
    b = node(c, 910, 780, 220, 150, 'Friend', 0.3, 'laptop')
    st = c.T('STUN')
    s1 = node(c, 300, 500, 240, 120, 'STUN', st, 'globe', size=30)
    if c.on(st + 0.4):
        link(c, a, s1, st + 0.4, txt_='what is my public IP?', off=0)
    tb = c.T('blocked')
    if c.on(tb):
        c.pen.rect(530, 680, 550, 880, fill=RED, outline=INK, w=3); c.sfx(tb, 'thud')
        cross(c.pen, 540, 650, 1.0, RED, 9, c.P(tb, 0.3))
    tt = c.T('TURN')
    t2 = node(c, 540, 1060, 260, 130, 'TURN relay', tt, 'server', fill=LIGHT, size=30)
    if c.on(tt + 0.3):
        link(c, a, t2, tt + 0.3, col=ORANGE); link(c, t2, b, tt + 0.5, col=ORANGE)
    tw = c.T('works')
    if c.on(tw): label(c, 540, 1230, 'not peer to peer anymore, but it works', tw, WHITE, INK, 30)


def code_(c):
    at = c.T('code') + 0.3
    code(c, 40, 360, 1040, 830, ['const pc = new RTCPeerConnection({ iceServers });', "const ch = pc.createDataChannel('chat');",
                                 'const offer = await pc.createOffer();', 'await pc.setLocalDescription(offer);', 'signal.send(offer); // your WebSocket'],
         at, 0.12, 26, 'call.js',
         marks=[(0, c.T('servers'), YEL), (1, c.T('channel'), YEL), (2, c.T('offer'), YEL), (4, c.T('signaling'), YEL)])
    tm = c.T('media')
    if c.on(tm): label(c, 540, 960, 'add camera tracks with addTrack()', tm, WHITE, INK, 32)


def trap(c):
    head(c, 'INTERVIEW TRAP', 'Interview', size=84)
    th = c.T('hundred')
    if c.on(th):
        cx, cy = 300, 760
        for k in range(12):
            ang = 2 * math.pi * k / 12
            x, y = cx + 190 * math.cos(ang), cy + 190 * math.sin(ang)
            for j in range(k + 1, 12):
                if c.on(th + 0.3):
                    ang2 = 2 * math.pi * j / 12
                    c.pen.line([(x, y), (cx + 190 * math.cos(ang2), cy + 190 * math.sin(ang2))], mix(PAPER, RED, 0.5), 2, False)
            c.pen.circ(x, y, 18, fill=WHITE, outline=INK, w=3)
        txt(c, 300, 1010, 'mesh: chaos', th, 'intx', 34, RED)
    tn = c.T('ninety')
    if c.on(tn): txt(c, 300, 1070, '99 uploads each', tn, 'ints', 30, INK)
    ts = c.T('SFU')
    if c.on(ts):
        cx, cy = 790, 760
        node(c, cx, cy, 160, 90, 'SFU', ts, fill=YEL, size=34)
        for k in range(10):
            ang = 2 * math.pi * k / 10
            x, y = cx + 190 * math.cos(ang), cy + 190 * math.sin(ang)
            c.pen.line([(cx + 70 * math.cos(ang), cy + 50 * math.sin(ang)), (x, y)], GRN, 4, False)
            c.pen.circ(x, y, 18, fill=WHITE, outline=INK, w=3)
        txt(c, 790, 1010, 'one upload each', ts + 0.4, 'intx', 34, GRN)
    tf = c.T('forwards')
    if c.on(tf): label(c, 540, 1180, 'SFU = Selective Forwarding Unit', tf, WHITE, INK, 32)


SCENES = [
    (hook, "On a Google Meet call, open a new tab, and type chrome, colon, slash slash, webrtc internals. You'll see a live peer connection, connected, with graphs of bytes flowing in real time."),
    (detour, "For video, a server in the middle is a detour. Every frame would go up to the server, and back down to your friend. WebRTC lets two browsers send audio, video, and data, directly to each other."),
    (party, "It's like being introduced at a party. A friend tells each of you the other's name, and table. After that, you talk directly. The friend isn't in the conversation anymore."),
    (signal, "That friend is the signaling server. The two browsers swap an offer and an answer, describing codecs and formats, plus possible network addresses, called ICE candidates. WebRTC doesn't define how they travel. Usually, it's over a WebSocket."),
    (nat, "The hard part is routers. A STUN server tells each browser its public address. When a direct path is blocked by a strict firewall, a TURN server relays the traffic. Then it's not peer to peer anymore, but it still works."),
    (code_, "In code: create a peer connection with your ICE servers. Open a data channel. Create an offer, set it as your local description, and send it through your signaling channel. For calls, you add camera and media tracks the same way."),
    (trap, "Interview trap: should a hundred person call use pure peer to peer? No. Every person would upload ninety nine video streams. Big calls use a server called an SFU. Each person uploads once, and the SFU forwards streams to everyone else."),
    (scene_next('S6 · E07', 'THE SHOWDOWN', 'which one do you pick?', 'showdown', 'pick'),
     "Next: the showdown. Five tools, one question: which one do you pick? Comment NOTES for the cheat sheet."),
]
