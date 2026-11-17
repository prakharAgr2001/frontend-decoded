from engine.lib import *
from engine.s6_extra import *

EP = dict(id='S6E19', tag='S6 · E19', short='FINALE: ONE CHAT APP', tail=3.0)


def mini(c, stage):
    """small chat phone that grows features scene by scene (top of every scene)"""
    x0, y0, x1, y1 = 360, 300, 720, 560
    card(c.pen, x0, y0, x1, y1, 30, INK, 8, 4)
    c.pen.rr(x0 + 12, y0 + 12, x1 - 12, y1 - 12, 22, fill=WHITE)
    c.pen.text(x0 + 40, y0 + 50, 'Riya', 'intx', 26, INK, 'lm')
    if stage >= 4: c.pen.text(x0 + 110, y0 + 52, 'online', 'ints', 20, GRN, 'lm')
    if stage >= 1: bubble(c, x0 + 30, x0 + 230, y0 + 120, 'Hi!', 0.0, mine=False, size=24)
    if stage >= 2: bubble(c, x1 - 200, x1 - 30, y0 + 200, 'Hey', 0.0, mine=True, n_ticks=2, tick_col=BLUE, size=24)


def intro(c):
    stamp(c.cv, 540, 420, 'SEASON 6 FINALE', 96, c.P(0.1, 0.45), -4, RED); c.sfx(0.1, 'thud')
    title(c, 'ONE CHAT APP.', 640, c.T('chat'), 110)
    title(c, 'REAL TIME, END TO END.', 800, c.T('end'), 84, hlcol=YEL)
    te = c.T('every')
    if c.on(te): txt(c, 540, 960, 'every episode, in one build', te, 'ints', 36, MUTE)


def transports(c):
    mini(c, 0)
    chaps(c, [('E05', 'messages: a WebSocket', 'WebSocket'), ('E04', 'notifications: SSE', 'notifications'),
              ('E06', 'voice calls: WebRTC', 'calls'), ('E02', 'admin dashboard: polling', 'dashboard')], 680, 115)


def send(c):
    mini(c, 1)
    chaps(c, [('E12', 'client id + outbox', 'UUID'), ('S4 · E15', 'optimistic bubble', 'instantly'), ('E11', 'server sequence number', 'sequence'),
              ('E12', 'ack: the clock becomes a tick', 'tick'), ('E12', 'dedup: retries are safe', 'duplicate')], 650, 105)


def survive(c):
    mini(c, 2)
    tb = c.T('break')
    if c.on(tb): stamp(c.cv, 860, 330, 'OFFLINE', 46, c.P(tb, 0.35), 8, RED); c.sfx(tb, 'thud')
    chaps(c, [('E09', 'heartbeats every 25 s', 'Heartbeats'), ('E10', 'backoff + jitter', 'jitter'), ('E10', 'resync since the last seq', 'since'),
              ('E10', 'flush the outbox', 'flush')], 680, 115)


def scale(c):
    mini(c, 4)
    tm = c.T('million')
    if c.on(tm): counter(c, 540, 640, 1, 1000000, tm, tm + 1.0, '{:,.0f}', 70, RED, ' users')
    chaps(c, [('E13', 'dumb socket servers + pub/sub', 'pub'), ('E14', 'presence with a TTL', 'presence'), ('E14', 'typing, throttled', 'throttled')], 780, 115)


def collab(c):
    mini(c, 4)
    chaps(c, [('E16', 'no last-save-wins', 'overwrites'), ('E17', 'shared notes: a CRDT library', 'CRDT'), ('E17', 'merges even offline', 'offline')], 700, 120)


NAMES = ['HOOK', 'SHORT POLL', 'LONG POLL', 'SSE', 'WEBSOCKET', 'WEBRTC', 'SHOWDOWN', 'IQ', 'HEARTBEAT', 'RECONNECT', 'ORDERING', 'ACKS',
         'SCALING', 'PRESENCE', 'IQ', 'CONFLICTS', 'OT/CRDT', 'IQ', 'FINALE']


def wrap(c):
    tt = c.T('Nineteen')
    season_map(c, NAMES, tt, 5, 340, 'FINALE', 0.05)
    tn = c.T('caching')
    if c.on(tn):
        darkcard(c.pen, 90, 820, 990, 1100)
        c.pen.text(540, 870, 'NEXT · SEASON 7', 'int', 32, YEL)
        c.pen.text(540, 960, 'CACHING', 'osw', 110 * c.B(tn, 0.45), WHITE)
        c.sfx(tn, 'thud')
        txt(c, 540, 1050, 'the fastest request is the one you never make', c.T('fastest'), 'ints', 30, (200, 205, 215))
    tc = c.T('Comment')
    if c.on(tc):
        c.sfx(tc, 'pop'); pn = c.B(tc, 0.4)
        c.pen.rr(540 - 380 * pn, 1170, 540 + 380 * pn, 1260, 45, fill=YEL, outline=INK, w=4)
        c.pen.text(540, 1215, 'Comment NOTES for the season cheat sheet', 'int', 30 * pn, INK)


SCENES = [
    (intro, "Season six finale. One chat app, real time, end to end, using every episode."),
    (transports, "Start with transports. Chat messages go over a WebSocket. Web notifications stream over server sent events. Voice calls use WebRTC, with the socket as the signaling channel. And the admin dashboard? Polling is fine."),
    (send, "Now send a message. The client gives it a UUID, shows it instantly with a clock, and keeps it in an outbox. The server stamps a sequence number, and acks. The clock becomes a tick. And a retry can never duplicate it."),
    (survive, "Now break the network. Heartbeats every twenty five seconds catch the silent drop. Reconnect with backoff and jitter. On open, fetch everything since the last sequence number, and flush the outbox."),
    (scale, "Now grow to a million users. Dumb socket servers, connected by pub sub. Presence with a time to live, sent only to people who are looking. Typing indicators, throttled."),
    (collab, "And shared notes inside a chat? Last save wins overwrites people. So use a CRDT library, and edits merge, even offline."),
    (wrap, "Nineteen episodes. From are we there yet, to edits that merge across the world. Next season: caching, because the fastest request is the one you never make. Comment NOTES for the season cheat sheet, and follow for season seven."),
]
