from engine.lib import *

EP = dict(id='S3E17', tag='S3 · E17', short='IQ: LOADING')

SCENES = [
    (scene_iq_intro('LOADING + BUNDLES'),
     "Four interview questions on loading and bundles. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'When does a plain, an async and a defer script run?',
              [('blocks', 'plain: blocks the parser, runs now'), ('arrives', 'async: runs on arrival, no order'), ('parsing', 'defer: after parsing, in order'),
               ('modules', 'modules are deferred by default')]),
     "Question one. When does a plain script, an async script, and a defer script run? [[3]] Answer: a plain script blocks the parser and runs immediately. Async runs as soon as it arrives, in no particular order. Defer runs after parsing, in document order. And modules are deferred by default."),
    (scene_iq(2, 'Preconnect vs preload vs prefetch?',
              [('origin', 'preconnect: DNS + TCP + TLS to an origin'), ('page', 'preload: this page, found late, high priority'),
               ('next', 'prefetch: next page, lowest priority'), ('steal', 'too many preloads steal bandwidth')]),
     "Question two. What's the difference between preconnect, preload and prefetch? [[3]] Answer: preconnect warms up the connection to an origin. Preload fetches something this page needs but finds late, at high priority. Prefetch fetches something for the next page, at lowest priority. And too many preloads steal bandwidth."),
    (scene_iq(3, "Why might tree shaking keep a function you never use?",
              [('CommonJS', 'it comes from CommonJS (require)'), ('effects', 'the package has side effects / no flag'), ('barrel', 'a barrel file re-exports it'),
               ('dynamic', "it's accessed dynamically: lib[name]")]),
     "Question three. Why might tree shaking keep a function you never use? [[3]] Answer: it comes from CommonJS. Or the package may have side effects, and doesn't say otherwise. Or a barrel file re exports it. Or your code accesses it dynamically, by name."),
    (scene_iq(4, 'Your bundle is 1.5 MB. Walk me through cutting it.',
              [('Measure', '1 · Measure: analyzer + Coverage'), ('Split', '2 · Split routes + heavy features'), ('Replace', '3 · Replace heavy deps, drop polyfills'),
               ('Minify', '4 · Minify + Brotli, then set a budget')]),
     "Question four. Your bundle is one and a half megabytes. Walk me through cutting it. [[3]] Answer: Measure first, with a bundle analyzer and the Coverage tab. Split routes and heavy features with dynamic import. Replace heavy dependencies, and drop polyfills you don't need. Minify, serve Brotli, and set a budget so it never creeps back."),
    (scene_next('S3 · E18', 'RESPONSIVE IMAGES', 'stop sending posters to phones', 'responsive', 'posters'),
     "Got all four? Tell me your score below. Next: responsive images, and why you should stop sending posters to phones. Comment NOTES for the cheat sheet."),
]
