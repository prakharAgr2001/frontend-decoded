from engine.lib import *

EP = dict(id='S5E05', tag='S5 · E05', short='IQ: API DESIGN')

SCENES = [
    (scene_iq_intro('API DESIGN'),
     "Four interview questions on API design. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Which HTTP methods are idempotent, and why does that matter?',
              [('PUT', 'GET · PUT · DELETE: idempotent'), ('POST', 'POST: no · PATCH: not guaranteed'),
               ('retries', 'Matters for automatic retries'), ('key', 'POST → send an Idempotency-Key')]),
     "Question one. Which HTTP methods are idempotent, and why does that matter? [[3]] Answer: GET, PUT and DELETE are idempotent. POST is not, and PATCH isn't guaranteed. It matters for retries. You can safely repeat an idempotent call after a timeout. For a POST, send an idempotency key."),
    (scene_iq(2, 'A GraphQL query for 100 posts and their authors makes 101 database calls. Why? Fix?',
              [('plus', 'The N+1 problem'), ('per', '1 call for posts + 1 per author'), ('DataLoader', 'Fix: batch with DataLoader'),
               ('single', 'all authors in a single query')]),
     "Question two. A GraphQL query for a hundred posts and their authors makes a hundred and one database calls. Why? And what's the fix? [[3]] Answer: that's the N plus one problem. One call for the posts, then one per author. Batch the lookups with DataLoader, so all the authors load in a single query."),
    (scene_iq(3, 'Your mobile home screen needs data from four services. What do you propose?',
              [('backend', 'A backend for frontend (BFF)'), ('parallel', 'It calls the services in parallel'),
               ('trims', 'Trims fields → one small payload'), ('owned', 'Owned by the mobile team')]),
     "Question three. Your mobile home screen needs data from four services. What do you propose? [[3]] Answer: a backend for frontend. The app makes one call. The BFF calls the services in parallel, close to them, trims the fields, and returns one small payload. And it's owned by the mobile team."),
    (scene_iq(4, 'When would you NOT choose GraphQL?',
              [('CDN', 'CDN / HTTP caching matters a lot'), ('CRUD', 'Simple CRUD API → REST'),
               ('TypeScript', 'One TS team owns both ends → tRPC')]),
     "Question four. When would you not choose GraphQL? [[3]] Answer: when HTTP caching at the CDN matters a lot. When the API is simple CRUD, where REST is enough. Or when one TypeScript team owns both ends, and tRPC is simpler."),
    (scene_next('S5 · E06', 'THE OFFSET BUG', 'why page two repeats a post', 'offset', 'repeats'),
     "Got all four? Tell me your score below. Next: the offset pagination bug, and why page two repeats a post. Comment NOTES for the cheat sheet."),
]
