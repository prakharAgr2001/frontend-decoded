from engine.lib import *

EP = dict(id='S1E24', tag='S1 · E24', short='IQ: EVENTS & MEMORY')

SCENES = [
    (scene_iq_intro('EVENTS, MEMORY & OBSERVERS'),
     "Four interview questions on events, memory and observers. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'What is the difference between event.target and event.currentTarget?',
              [('clicked', 'target = what was actually clicked'), ('running', 'currentTarget = whose listener is running'), ('ancestor', 'often an ancestor (delegation)')]),
     "Question one. What's the difference between event dot target and event dot currentTarget? [[3]] Answer: target is the element that was actually clicked. currentTarget is the element whose listener is running right now, often an ancestor."),
    (scene_iq(2, 'What is event delegation, and why use it?',
              [('parent', 'one listener on a parent'), ('bubbling', 'catches children via bubbling'), ('Fewer', 'fewer listeners, less memory'), ('later', 'elements added later just work')]),
     "Question two. What is event delegation, and why use it? [[3]] Answer: one listener on a parent handles events from all its children, thanks to bubbling. Fewer listeners, and elements added later work automatically."),
    (scene_iq(3, 'Name three common causes of memory leaks in a single page app.',
              [('Listeners', 'listeners never removed'), ('intervals', 'timers / intervals after unmount'), ('detached', 'detached DOM nodes still referenced'),
               ('caches', 'bonus: caches that only grow')]),
     "Question three. Name three common causes of memory leaks in a single page app. [[3]] Answer: listeners that are never removed. Timers and intervals still running after unmount. And detached DOM nodes still referenced in code. Global caches that only grow are a bonus fourth."),
    (scene_iq(4, 'Why prefer IntersectionObserver over a scroll listener?',
              [('computes', 'browser computes visibility itself'), ('forced', 'no forced layout on every scroll'), ('crosses', 'fires only when the threshold is crossed')]),
     "Question four. Why prefer IntersectionObserver over a scroll listener? [[3]] Answer: the browser computes visibility itself, so you avoid forced layout on every scroll. And your callback only runs when visibility crosses your threshold."),
    (scene_next('S1 · E25', 'SEASON FINALE', 'loading YouTube, frame by frame', 'finale', 'frame'),
     "Got all four? Tell me your score below. Next: the season finale. Loading YouTube, frame by frame. Comment NOTES for the cheat sheet."),
]
