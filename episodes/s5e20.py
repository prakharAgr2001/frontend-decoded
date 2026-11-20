from engine.lib import *

EP = dict(id='S5E20', tag='S5 · E20', short='IQ: ASYNC EDGE CASES', hook='4 async edge-case questions')

SCENES = [
    (scene_iq_intro('ASYNC EDGE CASES'),
     "Four interview questions on async edge cases. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Promise.all or Promise.allSettled: when do you use each?',
              [('need', 'all: you need every result · fail fast'), ('independent', 'allSettled: independent requests'),
               ('rest', 'one failure keeps the rest')]),
     "Question one. Promise dot all, or Promise dot all settled. When do you use each? [[3]] Answer: use all when you need every result, and one failure should fail the whole thing, fast. Use all settled when the requests are independent, like dashboard widgets, so one failure doesn't throw away the rest."),
    (scene_iq(2, 'A user types fast in search and sees results for an older query. How do you fix it?',
              [('race', 'A race condition'), ('Abort', 'Abort the previous request (or ignore stale)'), ('debounce', 'Debounce → fewer requests'),
               ('key', 'Key cached results by the query')]),
     "Question two. A user types fast in a search box, and sees results for an older query. How do you fix it? [[3]] Answer: it's a race condition. Abort the previous request with an AbortController, or ignore stale responses. Add debounce, to send fewer requests. And key cached results by the query string."),
    (scene_iq(3, 'Your checkout POST timed out. Should the client retry it?',
              [('blindly', 'Not blindly: the order may exist'), ('idempotency', 'Retry with an Idempotency-Key'), ('status', 'Or check the order status first'),
               ('jitter', 'Back off, with jitter')]),
     "Question three. Your checkout POST timed out. Should the client retry it? [[3]] Answer: not blindly. The order might already exist. Retry only with an idempotency key, so the server can spot the duplicate. Or check the order status first. And back off, with jitter."),
    (scene_iq(4, 'A page shows one big spinner until its slowest section loads. How do you fix it?',
              [('Suspense', 'One Suspense boundary wraps everything'), ('Split', 'Split into a few grouped boundaries'),
               ('Critical', 'Critical content first, matching skeletons'), ('streaming', 'Slow sections stream in below')]),
     "Question four. A page shows one big spinner, until its slowest section loads. How do you fix it? [[3]] Answer: there's one Suspense boundary around everything. Split it into a few boundaries, grouped by what belongs together. Critical content first, with matching skeletons, and the slow sections streaming in below."),
    (scene_next('S5 · E21', 'SEASON FINALE', 'one search page, every fix', 'finale', 'search'),
     "Got all four? Tell me your score below. Next: the season finale. One search page, and every fix from this season. Comment NOTES for the cheat sheet."),
]
