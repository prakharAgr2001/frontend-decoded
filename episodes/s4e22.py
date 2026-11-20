from engine.lib import *

EP = dict(id='S4E22', tag='S4 · E22', short='IQ: URL · FORMS · FSM', hook='URL, forms, machines, Immer')

SCENES = [
    (scene_iq_intro('URL · FORMS · MACHINES', kw='questions'),
     "Four interview questions on URL state, forms, state machines, and Immer. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'What belongs in the URL, and what does not?',
              [('shareable', 'shareable: search, filters, page, tab'), ('replace', 'replace while typing, push on commit'),
               ('secrets', 'never: secrets, personal data, huge objects'), ('validate', 'values are strings: parse + validate')]),
     "Question one. What belongs in the URL, and what doesn't? [[3]] Answer: anything shareable, like search, filters, the page, or the tab. Use replace while typing, and push on commit. Never put secrets, personal data, or huge objects there. And every value is a string, so parse and validate it."),
    (scene_iq(2, 'Controlled vs uncontrolled inputs: what are the trade-offs?',
              [('React', 'controlled: React holds it, renders per key'), ('DOM', 'uncontrolled: the DOM holds it, read on submit'),
               ('refs', 'React Hook Form: refs + subscriptions'), ('inside', 'focus lost? component defined inside another')]),
     "Question two. Controlled versus uncontrolled inputs: what are the trade offs? [[3]] Answer: controlled means React holds the value, and every key press renders. Uncontrolled means the DOM holds it, and you read it on submit. React Hook Form uses refs, plus subscriptions. And if focus is lost on each key, a component was defined inside another."),
    (scene_iq(3, 'isLoading and isError are both true. How would you redesign it?',
              [('single', 'one status field, not booleans'), ('events', 'states + events + allowed transitions'), ('ignored', 'invalid events are ignored'),
               ('XState', 'complex flows: XState')]),
     "Question three. Is loading and is error are both true. How would you redesign it? [[3]] Answer: use a single status field, not separate booleans. Model the states, the events, and the allowed transitions. Invalid events are simply ignored. And for complex flows, reach for XState."),
    (scene_iq(4, 'How does Immer let you mutate safely?',
              [('Proxy', 'the draft is a Proxy that records writes'), ('copies', 'copies only the changed paths'), ('reused', 'untouched branches are reused'),
               ('frozen', 'result frozen in development')]),
     "Question four. How does Immer let you mutate safely? [[3]] Answer: the draft is a Proxy that records your writes. Immer copies only the changed paths. Untouched branches are reused. And the result is frozen in development."),
    (scene_next('S4 · E23', 'SEASON FINALE', 'one food order, every kind of state', 'finale', 'order'),
     "Got all four? Tell me your score below. Next: the season finale. One food order, and every kind of state it touches. Comment NOTES for the cheat sheet."),
]
