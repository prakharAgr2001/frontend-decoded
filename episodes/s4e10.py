from engine.lib import *

EP = dict(id='S4E10', tag='S4 · E10', short='IQ: STORES')

SCENES = [
    (scene_iq_intro('REDUX & STORES'),
     "Four interview questions on Redux, stores and selectors. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, "Walk me through Redux's data flow.",
              [('dispatches', 'UI dispatches an action'), ('pure', 'pure reducer: (state, action) → new state'),
               ('saves', 'store saves it, notifies subscribers'), ('selector', 'components re-render if their selector changed')]),
     "Question one. Walk me through Redux's data flow. [[3]] Answer: the UI dispatches an action. A pure reducer takes the state and the action, and returns a new state. The store saves it, and notifies its subscribers. And each component re-renders only if its selector result changed."),
    (scene_iq(2, 'Redux says never mutate. So why can Redux Toolkit write state.items.push()?',
              [('Immer', 'Immer gives the reducer a draft'), ('records', 'it records your changes'), ('copy', 'and builds a new immutable copy'),
               ('inside', 'only inside createSlice / createReducer')]),
     "Question two. Redux says never mutate. So why can Redux Toolkit write state dot items dot push? [[3]] Answer: Immer hands the reducer a draft. It records every change you make, and builds a new immutable copy from them. And it only works inside create slice, or create reducer."),
    (scene_iq(3, 'Context, Zustand or Redux: how do you choose?',
              [('rarely', 'context: values that rarely change'), ('boilerplate', 'Zustand: shared state, little boilerplate'),
               ('teams', 'Redux: big teams, strict flow, DevTools'), ('neither', 'server data: neither → a query cache')]),
     "Question three. Context, Zustand, or Redux: how do you choose? [[3]] Answer: context, for values that rarely change. Zustand, for shared client state with little boilerplate. Redux, for big teams that want a strict flow and great DevTools. And for server data, neither. Use a query cache."),
    (scene_iq(4, 'A selector uses filter(), and the list re-renders on every dispatch. Why?',
              [('array', 'filter() returns a new array every time'), ('equality', '=== check always fails'), ('createSelector', 'memoize with createSelector'),
               ('shallow', 'or compare with shallowEqual')]),
     "Question four. A selector uses filter, and the list re-renders on every dispatch. Why? [[3]] Answer: filter returns a new array every time, so the equality check always fails. Memoize it with createSelector, or compare with shallow equal."),
    (scene_next('S4 · E11', 'SERVER STATE', "the data you don't own", 'server', 'own'),
     "Got all four? Tell me your score below. Next: server state, the data you don't actually own. Comment NOTES for the cheat sheet."),
]
