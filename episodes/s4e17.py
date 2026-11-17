from engine.lib import *

EP = dict(id='S4E17', tag='S4 · E17', short='IQ: SERVER STATE')

SCENES = [
    (scene_iq_intro('SERVER STATE'),
     "Four interview questions on server state and caching. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'How is server state different from client state?',
              [('owned', 'owned by the server, you hold a copy'), ('async', 'async: loading and errors'), ('stale', 'goes stale, others change it'),
               ('caching', 'needs caching, dedupe, refetching')]),
     "Question one. How is server state different from client state? [[3]] Answer: it's owned by the server, and you only hold a copy. It's async, so it has loading and error states. It goes stale, because others can change it. So it needs caching, deduplication, and refetching."),
    (scene_iq(2, 'In React Query, what is the difference between staleTime and gcTime?',
              [('fresh', 'staleTime: how long data stays fresh'), ('zero', 'default 0: always refetch in background'),
               ('memory', 'gcTime: unused data kept in memory'), ('five', 'default 5 minutes')]),
     "Question two. In React Query, what's the difference between stale time and G C time? [[3]] Answer: stale time is how long data stays fresh, with no refetch. The default is zero, so it refetches in the background. G C time is how long unused data stays in memory. The default is five minutes."),
    (scene_iq(3, 'After a mutation, how do you keep every screen in sync?',
              [('invalidate', 'invalidateQueries by key prefix'), ('setQueryData', 'or setQueryData from the response'), ('folders', 'design keys like folders'),
               ('focus', 'other tabs: refetch on focus / BroadcastChannel')]),
     "Question three. After a mutation, how do you keep every screen in sync? [[3]] Answer: invalidate the matching queries by key prefix. Or write the server's response into the cache with setQueryData. Design your keys like folders. And for other tabs, refetch on focus, or use a BroadcastChannel."),
    (scene_iq(4, 'Walk through an optimistic like, with rollback.',
              [('cancel', 'cancel in-flight queries'), ('snapshot', 'snapshot the old value, write the new one'), ('restore', 'onError: restore + toast'),
               ('refetch', 'onSettled: refetch the truth')]),
     "Question four. Walk through an optimistic like, with rollback. [[3]] Answer: cancel any queries in flight. Take a snapshot of the old value, then write the liked version. On error, restore the snapshot and show a toast. And on settled, refetch the truth."),
    (scene_next('S4 · E18', 'URL STATE', 'the state you can share', 'URL', 'share'),
     "Got all four? Tell me your score below. Next: URL state, the state you can share. Comment NOTES for the cheat sheet."),
]
