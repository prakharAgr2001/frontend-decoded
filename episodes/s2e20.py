from engine.lib import *

EP = dict(id='S2E20', tag='S2 · E20', short='IQ: MODERN RENDERING', hook='RSC · actions · islands · edge')

SCENES = [
    (scene_iq_intro('MODERN RENDERING'),
     "Four interview questions on modern rendering. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'With streaming SSR, why can’t you return a 404 after the shell is sent?',
              [('headers', 'status + headers go out with the first chunk'), ('before', 'decide before the shell, or error in-page')]),
     "Question one. With streaming SSR, why can't you return a 404 after the shell is sent? [[3]] Answer: the status code and headers go out with the first chunk. So decide before the shell, or render an error inside the page."),
    (scene_iq(2, 'Server component vs client component: which can use useState, and which can query the database?',
              [('handlers', "useState / onClick → client ('use client')"), ('secrets', 'database / secrets → server component'), ('ships', 'only client code ships to the browser')]),
     "Question two. Server component versus client component. Which can use useState, and which can query the database? [[3]] Answer: useState and click handlers need a client component. Database access and secrets belong in a server component. And only client component code ships to the browser."),
    (scene_iq(3, 'Is a Server Action safe because there is no API route?',
              [('public', 'no: it is a public POST endpoint'), ('auth', 'check auth inside the action'), ('validate', 'validate every argument')]),
     "Question three. Is a server action safe because there's no API route? [[3]] Answer: no. It's a public POST endpoint. Check auth inside the action, and validate every argument."),
    (scene_iq(4, 'Islands vs resumability, in one line each.',
              [('only', 'islands: hydrate only the interactive parts'), ('skip', 'resumability: no hydration, code on demand')]),
     "Question four. Islands versus resumability, in one line each. [[3]] Answer: islands hydrate only the interactive parts, each on its own. Resumability skips hydration completely, and loads each handler's code only when you interact."),
    (scene_next('S2 · E21', 'SEASON FINALE', 'Amazon vs Gmail vs a blog', 'finale', 'Gmail'),
     "Got all four? Tell me your score below. Next: the season finale. Amazon versus Gmail versus a blog. Comment NOTES for the cheat sheet."),
]
