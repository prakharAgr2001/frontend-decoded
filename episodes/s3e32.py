from engine.lib import *

EP = dict(id='S3E32', tag='S3 · E32', short='IQ: RUNTIME', hook='4 questions on runtime perf')

SCENES = [
    (scene_iq_intro('RUNTIME PERFORMANCE'),
     "Four interview questions on runtime performance. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Debounce vs throttle: when do you use each?',
              [('silence', 'debounce: after silence, once (search)'), ('interval', 'throttle: once per interval (scroll)'),
               ('frame', 'visual updates: requestAnimationFrame'), ('visible', 'visibility: IntersectionObserver')]),
     "Question one. Debounce versus throttle: when do you use each? [[3]] Answer: debounce runs once after silence, like a search box. Throttle runs at most once per interval, like a scroll progress bar. For visual updates, use request animation frame. And to check if something's visible, use an intersection observer."),
    (scene_iq(2, 'A table with 10,000 rows is slow. What are your options?',
              [('Virtualize', 'Virtualize: render visible rows only'), ('content', 'content-visibility: auto for long pages'), ('Paginate', 'Paginate or load more'),
               ('find', 'Trade-offs: find-in-page, a11y, heights')]),
     "Question two. A table with ten thousand rows is slow. What are your options? [[3]] Answer: Virtualize it, rendering only the visible rows. Use content visibility auto for long pages of content. Or paginate, and load more on demand. And know the trade offs: find in page, accessibility, and variable heights."),
    (scene_iq(3, 'Why does a component re-render, and how do you cut wasted renders?',
              [('parent', 'state · context · parent re-render'), ('down', 'move state down / pass children'), ('measured', 'memo + stable props, where measured slow'),
               ('Compiler', 'or let the React Compiler do it')]),
     "Question three. Why does a component re-render, and how do you cut wasted renders? [[3]] Answer: its state, a context, or its parent changed. Move state down, or pass components as children. Use memo with stable props, only where it's measured slow. Or let the React Compiler memoize for you."),
    (scene_iq(4, 'A click handler takes 400 ms. How do you fix INP?',
              [('feedback', 'Paint feedback first, then yield'), ('slices', 'Chunk work into ~10 ms slices'), ('Worker', 'Move CPU work to a Web Worker'),
               ('transition', 'useTransition for non-urgent updates')]),
     "Question four. A click handler takes four hundred milliseconds. How do you fix INP? [[3]] Answer: paint feedback first, then yield. Chunk the rest into ten millisecond slices. Move heavy CPU work into a Web Worker. And in React, wrap non urgent updates in a transition."),
    (scene_next('S3 · E33', 'SEASON FINALE', 'one product page, made fast', 'finale', 'fast'),
     "Got all four? Tell me your score below. Next: the season finale. One product page, made fast, using everything from this season. Comment NOTES for the cheat sheet."),
]
