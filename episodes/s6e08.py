from engine.lib import *

EP = dict(id='S6E08', tag='S6 · E08', short='IQ: TRANSPORTS')

SCENES = [
    (scene_iq_intro('REAL-TIME TRANSPORTS'),
     "Four interview questions on real time transports. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'You poll every 2 s with setInterval. The server slows to 5 s per response. What happens?',
              [('overlap', 'Requests overlap and pile up'), ('order', 'Responses can land out of order'), ('finishes', 'Fix: setTimeout after each one finishes'),
               ('back', '+ back off, pause when hidden')]),
     "Question one. You poll every two seconds with set interval. The server slows to five seconds per response. What happens? [[3]] Answer: requests overlap and pile up, making the slow server slower. Responses can land out of order. Schedule the next poll only after the last one finishes, back off when the server struggles, and pause when the tab is hidden."),
    (scene_iq(2, 'Your SSE dashboard works in 6 tabs. Why does the 7th tab never load?',
              [('about', 'HTTP/1.1: ~6 connections per site'), ('holds', 'Each EventSource holds one open'), ('multiplexes', 'Fix: HTTP/2 multiplexes streams'),
               ('share', 'or share one stream across tabs')]),
     "Question two. Your SSE dashboard works in six tabs. Why does the seventh tab never load? [[3]] Answer: on HTTP one point one, browsers allow about six connections per site, and each EventSource holds one open. Serve it over HTTP two, which multiplexes streams on one connection, or share one stream across tabs."),
    (scene_iq(3, 'Live cricket scores for a million viewers. WebSockets or SSE?',
              [('listen', 'SSE: viewers only listen'), ('reconnect', 'Built-in reconnect + Last-Event-ID'), ('proxies', 'Plain HTTP: proxies, CDNs, HTTP/2'),
               ('nothing', 'WebSockets add nothing here')]),
     "Question three. Live cricket scores for a million viewers. WebSockets, or SSE? [[3]] Answer: server sent events. Viewers only listen. You get built in reconnect with the last event ID, and it's plain HTTP, so it works with proxies and HTTP two. A two way socket adds nothing here."),
    (scene_iq(4, 'In a WebRTC call, how does the offer reach the other browser?',
              [('defines', 'WebRTC defines no signaling'), ('channel', 'Your app sends it: usually a WebSocket'), ('STUN', 'STUN finds public addresses'),
               ('TURN', 'TURN relays if direct fails')]),
     "Question four. In a WebRTC call, how does the offer reach the other browser? [[3]] Answer: WebRTC defines no signaling. Your app delivers it, over any channel, usually a WebSocket. Then STUN helps each side find its public address, and TURN relays the media if a direct path fails."),
    (scene_next('S6 · E09', 'HEARTBEATS', 'is anyone still there?', 'heartbeats', 'there'),
     "Got all four? Tell me your score below. Next: heartbeats, and how a connection can die without telling anyone. Is anyone still there? Comment NOTES for the cheat sheet."),
]
