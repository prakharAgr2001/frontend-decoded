from engine.lib import *

EP = dict(id='S2E12', tag='S2 · E12', short='IQ: HYDRATION', hook='4 hydration questions')

SCENES = [
    (scene_iq_intro('HYDRATION'),
     "Four interview questions on hydration. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'What is hydration, in one sentence?',
              [('runs', 'React runs your components in the browser'), ('attaches', 'and attaches handlers + state'), ('existing', 'to the existing server HTML')]),
     "Question one. What is hydration, in one sentence? [[3]] Answer: React runs your components in the browser, and attaches event handlers and state to the existing server HTML, instead of rebuilding it."),
    (scene_iq(2, 'Name three causes of a hydration mismatch.',
              [('Dates', 'dates / Math.random() in render'), ('window', 'window or localStorage in render'), ('nesting', 'invalid nesting, like <div> in <p>'),
               ('extensions', 'bonus: browser extensions')]),
     "Question two. Name three causes of a hydration mismatch. [[3]] Answer: dates or random numbers in render. Reading window or localStorage in render. And invalid HTML nesting, like a div inside a paragraph. Browser extensions that edit the page are a bonus fourth."),
    (scene_iq(3, 'The page looks ready, but taps do nothing. What is happening, and which metrics show it?',
              [('loading', 'JS still loading or hydrating'), ('Blocking', 'lab: Total Blocking Time'), ('field', 'field: Interaction to Next Paint (INP)')]),
     "Question three. The page looks ready, but taps do nothing. What's happening, and which metrics show it? [[3]] Answer: the JavaScript is still loading or hydrating. In the lab, Total Blocking Time. In the field, Interaction to Next Paint."),
    (scene_iq(4, 'How do Suspense boundaries improve hydration?',
              [('chunks', 'split hydration into independent chunks'), ('yield', 'main thread can yield between them'), ('clicked', 'clicked part hydrates first, click replayed')]),
     "Question four. How do Suspense boundaries improve hydration? [[3]] Answer: they split hydration into independent chunks, so the main thread can yield between them. And the part the user clicked hydrates first, with the click replayed."),
    (scene_next('S2 · E13', 'STREAMING SSR', 'send the page before it’s finished', 'streaming', 'finished'),
     "Got all four? Tell me your score below. Next: streaming server rendering. Send the page before it's finished. Comment NOTES for the cheat sheet."),
]
