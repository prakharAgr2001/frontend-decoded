from engine.lib import *

EP = dict(id='S4E05', tag='S4 · E05', short='IQ: STATE BASICS', hook='4 questions on state basics')

SCENES = [
    (scene_iq_intro('STATE BASICS'),
     "Four interview questions on state basics. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, "Props vs state: and when should a value NOT be state?",
              [('passed', 'props: passed in by the parent, read-only'), ('owned', 'state: owned, changes over time'),
               ('calculate', 'computable? derive it, never store it'), ('ref', 'changes but never shown? useRef')]),
     "Question one. What's the difference between props and state, and when should a value not be state? [[3]] Answer: props are passed in by the parent, and are read only. State is owned by the component, and changes over time. If you can calculate it from other state or props, derive it. And if it changes but never affects the screen, use a ref."),
    (scene_iq(2, 'Name the five types of state, and where each one lives.',
              [('local', 'local UI → useState'), ('Shared', 'shared client → context / store'), ('cache', 'server → a server cache'),
               ('address', 'URL → the address bar'), ('library', 'form → a form library')]),
     "Question two. Name the five types of state, and where each one lives. [[3]] Answer: local UI state, in use state. Shared client state, in context or a store. Server state, in a server cache. URL state, in the address bar. And form state, in a form library."),
    (scene_iq(3, 'Typing in a search box re-renders the whole page. Why, and how do you fix it?',
              [('high', 'the state lives too high'), ('children', 'parent renders → all children render'), ('down', 'move it down, into <Search>'),
               ('pass', 'or pass heavy parts as children')]),
     "Question three. Typing in a search box re-renders the whole page. Why, and how do you fix it? [[3]] Answer: the search state lives too high, in a parent of everything. When a parent renders, all its children render. Move the state down, into the search component. Or pass the heavy parts in as children."),
    (scene_iq(4, 'A context value changes and 50 components re-render. How do you fix it?',
              [('memoize', 'useMemo the Provider value'), ('Split', 'split one big context by concern'), ('Separate', 'separate state from dispatch'),
               ('selectors', 'hot state → a store with selectors'), ('help', "React.memo won't help consumers")]),
     "Question four. A context value changes, and fifty components re-render. How do you fix it? [[3]] Answer: memoize the provider value, so it isn't a new object every render. Split one big context by concern. Separate state from dispatch. For state that changes often, use a store with selectors. And no, wrapping consumers in memo won't help."),
    (scene_next('S4 · E06', 'REDUX FROM SCRATCH', 'the whole idea in 10 lines', 'Redux', 'lines'),
     "Got all four? Tell me your score below. Next: Redux from scratch, the whole idea in ten lines. Comment NOTES for the cheat sheet."),
]
