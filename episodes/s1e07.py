from engine.lib import *

EP = dict(id='S1E07', tag='S1 · E07', short='IQ: URL TO PIXELS')

SCENES = [
    (scene_iq_intro('URL TO PIXELS'),
     "Four interview questions on how a page travels from a URL to your screen. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Walk me through what happens when you type a URL and press Enter.',
              [('DNS', 'DNS → name to IP address'), ('TCP', 'TCP → open a connection'), ('TLS', 'TLS → encrypt + verify the site'),
               ('HTTP', 'HTTP → request the page'), ('parses', 'Browser → parse, layout, paint')]),
     "Question one. Walk me through what happens when you type a URL and press Enter. [[3]] Answer: DNS turns the name into an IP. TCP opens a connection. TLS secures it. HTTP requests the page. Then the browser parses it, lays it out, and paints it."),
    (scene_iq(2, 'Why is the first visit to a site slower than the second?',
              [('pays', 'First visit pays full price'), ('lookup', 'DNS lookup + every handshake'), ('cached', 'Repeat: DNS answer is cached'),
               ('reused', 'Connections get reused'), ('files', 'Files come from the browser cache')]),
     "Question two. Why is the first visit to a site slower than the second? [[3]] Answer: the first visit pays full price. A DNS lookup, fresh handshakes, and every file downloaded. On a repeat visit, DNS is cached, connections are reused, and files come from the browser cache."),
    (scene_iq(3, 'HTTP/2 already multiplexes requests. So why did we need HTTP/3?',
              [('TCP', 'HTTP/2 still rides on TCP'), ('stalls', 'One lost packet stalls every stream'), ('QUIC', 'HTTP/3 → QUIC over UDP'),
               ('independent', 'Streams are independent'), ('survive', 'Survives Wi-Fi → 4G switches')]),
     "Question three. HTTP two already multiplexes requests. So why did we need HTTP three? [[3]] Answer: HTTP two still runs on TCP, so one lost packet stalls every stream. HTTP three uses QUIC over UDP, where streams are independent, and connections survive network changes."),
    (scene_iq(4, 'You shipped a fix, but some users still see the old version. Name two possible reasons.',
              [('CDN', 'A CDN edge serves a cached copy'), ('browser', "The user's browser cached the old file"),
               ('versioned', 'Fix → versioned file names'), ('purge', 'Fix → purge the CDN cache')]),
     "Question four. You shipped a fix, but some users still see the old version. Name two possible reasons. [[3]] Answer: a CDN edge is still serving a cached copy, or the user's browser cached the old file. Fix it with versioned file names, and purge the CDN when you need to."),
    (scene_next('S1 · E08', 'DOM & CSSOM', 'how the browser reads your code', 'DOM', 'reads'),
     "Got all four? Tell me your score below. Next: the DOM and CSSOM, how the browser reads your code. Comment NOTES for the cheat sheet."),
]
