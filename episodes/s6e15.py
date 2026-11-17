from engine.lib import *

EP = dict(id='S6E15', tag='S6 · E15', short='IQ: STAYING ALIVE')

SCENES = [
    (scene_iq_intro('KEEPING CONNECTIONS ALIVE', kw='questions'),
     "Four interview questions on keeping real time connections alive. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, "A user's laptop sleeps. Your app still shows them online for hours. Why, and what's the fix?",
              [('TCP', 'Half-open TCP: no close ever arrives'), ('heartbeats', 'Heartbeats + a timeout on both sides'), ('TTL', 'Presence entry with a TTL')]),
     "Question one. A user's laptop sleeps. Your app still shows them online for hours. Why, and what's the fix? [[3]] Answer: the TCP connection is half open, and no close ever arrives. Add heartbeats with a timeout on both sides, and store presence with a TTL, so it expires on its own."),
    (scene_iq(2, 'Your chat server restarts, and crashes again within seconds. What happened?',
              [('herd', 'Thundering herd: every client at once'), ('exponential', 'Exponential backoff, with a cap'), ('jitter', '+ random jitter'),
               ('drain', 'Drain deploys gradually')]),
     "Question two. Your chat server restarts, and crashes again within seconds. What happened? [[3]] Answer: a thundering herd. Every client reconnected at the same moment. Use exponential backoff with a cap, add random jitter, and drain servers gradually during deploys."),
    (scene_iq(3, 'Users sometimes see their own message twice. Where is the bug?',
              [('lost', 'A retry after a lost ack'), ('UUID', 'Fix: client-made id (UUID) per message'), ('drops', 'Server drops repeat ids'),
               ('echo', 'Client merges its own echo by id')]),
     "Question three. Users sometimes see their own message twice. Where is the bug? [[3]] Answer: a retry after a lost ack, or an echo that wasn't matched. Give every message a client made id, a UUID. The server drops repeat ids, and the client merges its own echo by id, instead of adding it."),
    (scene_iq(4, 'Alice is on server A, Bob on server B. How does her message reach him?',
              [('publishes', 'A publishes to channel user:bob'), ('subscribed', 'B is subscribed, pushes to his socket'), ('sticky', 'Sticky sessions do not solve this')]),
     "Question four. Alice is on server A, Bob on server B. How does her message reach him? [[3]] Answer: through pub sub. Server A publishes to Bob's channel. Server B is subscribed, and pushes it down Bob's socket. Sticky sessions don't solve this."),
    (scene_next('S6 · E16', 'EDIT CONFLICTS', 'two people, one sentence', 'edit', 'sentence'),
     "Got all four? Tell me your score below. Next: edit conflicts, when two people type in the same sentence. Comment NOTES for the cheat sheet."),
]
