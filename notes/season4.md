# Frontend Decoded · Season 4 cheat sheets (DM these for "Comment NOTES")

## E01 · What is state
- State = data your UI remembers right now that can change while the page is open. Rule: if it changes and the screen must show it, it's state.
- React's idea: **UI = f(state)**. Don't edit the screen; change state (`setX`) and React re-renders, touching only what differs in the DOM.
- Trap: don't store what you can compute. `const total = items.reduce(...)`, not `useState(total)` → two sources of truth drift.
- See it: React DevTools → Components → select a component → hooks panel shows live state.

## E02 · The 5 types of state
| Type | Examples | Home |
|---|---|---|
| Local UI | isOpen, activeTab, hovered | `useState` |
| Shared client | cart, theme, user | context / store |
| Server | menu, prices, orders | server cache (React Query, SWR, RTK Query) |
| URL | `?q=`, filters, page | the address bar |
| Form | values, touched, errors | form library |
- 3 questions: from the server? → cache. Survive refresh/share? → URL. Distant components? → context/store. Otherwise local.
- Classic mistake: server data copied into a global store = hand-written loading flags, refetching, cache rules.

## E03 · Colocation
- Keep state as close as possible to where it's used — and no higher. Lift only to the **closest common parent**.
- State at the top → every update re-renders from the top (S3·E27). Move it down, or pass heavy parts as `children`.
- Bonus: delete a component and its state goes too. Global only for truly app-wide values (user, theme, locale) — and even then, not one giant object.

## E04 · The context trap
- `useContext` subscribes to the **whole** value. Any change → every consumer re-renders.
- Trap 1: `value={{ user, cart }}` is a new object every render → `useMemo` it.
- Trap 2: one big context → split by concern (UserCtx, ThemeCtx, CartCtx) and split state from dispatch.
- `React.memo` does NOT stop context re-renders. Context = delivery, not a state manager; hot state → store with selectors.
- See it: React Profiler → "Why did this render? Context changed".

## E05 · IQ: state basics
- Props vs state (passed/read-only vs owned/changes; derive computables; `useRef` for non-visual) · 5 types + homes · search re-renders page (state too high → move down / children) · context fan-out (memo value, split, separate dispatch, store+selectors; memo won't help).

## E06 · Redux from scratch
- 3 ideas: one store · actions describe what happened (`{ type: 'cart/added', item }`) · reducers are pure `(state, action) → newState`.
- `createStore` ≈ 10 lines: `state`, `subs`, `getState`, `subscribe`, `dispatch` (run reducer → save → notify).
- One-way flow: UI → dispatch → reducer → new state → subscribers re-render. Redux DevTools = action log + time travel.
- Trap: mutate + return same reference → `Object.is(prev, next)` true → UI never updates, time travel breaks.

## E07 · Redux Toolkit
- Official way today. `createSlice` generates action types + creators; reducers can "mutate" because **Immer** gives a draft.
- `configureStore`: DevTools wired, dev checks for mutation + non-serializable values (Dates, functions).
- RTK Query = server-state cache inside Redux. Is Redux dead? No — big apps, many writers, logged/replayable changes. Overkill for small apps.

## E08 · Zustand · Jotai · MobX
- **Zustand**: `create((set) => ({...}))`, no Provider, read slices `useCart(s => s.items.length)`.
- **Jotai**: atoms + derived atoms (`atom(get => ...)`), re-render only on atoms you read.
- **MobX**: `makeAutoObservable` + `observer`, mutate directly, spreadsheet-style auto updates.
- Trap: module-level store on the server (SSR) is shared across requests → user data leaks. Create a store per request, pass via context.

## E09 · Selectors
- Selector picks the slice a component needs; component re-renders only when the result changes (`===` after every dispatch).
- Trap: `filter`/`map`/object literals return new references every time → always re-render. Use `createSelector` (memoized), separate selectors, or `shallowEqual` / `useShallow`.
- Selectors are where derived data lives (totals, counts, filtered lists).

## E10 · IQ: Redux & stores
- Redux flow · why RTK can `push` (Immer draft → new immutable copy; only in createSlice/createReducer) · context vs Zustand vs Redux (rarely-changing / low boilerplate / big teams; server data → query cache) · filter selector re-renders (new array → memoize/shallow).

## E11 · Server state
- Lives on a server, you hold a copy, others can change it → stale on arrival. Async, can fail, shared across users and tabs.
- Needs: caching, dedupe, refetch when stale, background updates, pagination, garbage collection.
- `useEffect` fetch: no cache, duplicate requests, races. Server Components (S2·E14) remove the client copy for read-only data; interactive data still needs a client cache.

## E12 · React Query
- `useQuery({ queryKey, queryFn })` → `data`, `isPending`, `error`. Key = cache address; same key = one request (dedupe).
- Stale-while-revalidate: show cache now, refetch in background, swap if changed.
- `staleTime` (fresh window, default 0) vs `gcTime` (unused data kept, default 5 min). Refetch on focus, reconnect, mount-when-stale.
- Trap: `isPending` (no data yet → skeleton) vs `isFetching` (any request incl. background → don't flash a spinner).

## E13 · Cache invalidation
- After a mutation: `qc.invalidateQueries({ queryKey: ['addresses'] })` → marks matching queries stale, refetches active ones.
- Keys are folders: prefix match (`['addresses']` hits `['addresses', 7]`); `exact: true` for one key.
- Or `setQueryData` with the server's response (skip a round trip). Too little = screens lie; too much = refetch the world.
- Other tabs: refetch on window focus; `BroadcastChannel`; server push (S6).

## E14 · Normalization
- Store each entity once, keyed by id; everything else references the id: `users.byId[7]`, `posts.byId[101].author = 7`.
- Wins: one source of truth, updates in one place, O(1) lookups, no deep spreads.
- Tools: RTK `createEntityAdapter`; Apollo/Relay normalize automatically (`__typename` + id). React Query caches per query (invalidate instead).

## E15 · Optimistic UI
- Update the UI as if success, send the request, fix on failure. Feels instant on slow networks.
- React Query: `onMutate` → `cancelQueries` → `setQueryData`. React 19: `useOptimistic` (value lives while the action runs).
- Use for likes, toggles, reorder, chat. Not for payments, last-item stock, anything where false success costs the user.
- Trap: cancel in-flight refetches first, or an old response overwrites your optimistic value.

## E16 · Rollback
- `onMutate`: snapshot `prev` and return it · `onError`: restore `ctx.prev` + toast with Retry · `onSettled`: invalidate (server truth wins).
- Races: like/unlike/like out of order → stale snapshot. Fix: send intent (`PUT { liked: true }`, idempotent) not toggle, serialize per item, always settle with a refetch.

## E17 · IQ: server state
- Server vs client state · `staleTime` vs `gcTime` · syncing after mutations (invalidate by prefix / setQueryData / focus / BroadcastChannel) · optimistic like with rollback (cancel → snapshot → write → onError restore → onSettled refetch).

## E18 · URL state
- If it should be shareable, bookmarkable, or reachable with Back → put it in the URL (path + query).
- `useSearchParams`: read from and write to the URL; it's the single source of truth (no useState copy).
- `replace` while typing, `push` for committed choices. Not in the URL: secrets/PII (logs, history, referrers), huge objects, ephemeral UI. Values are strings → parse + validate.

## E19 · Form state
- Controlled (`value` + `onChange`, a render per keystroke) vs uncontrolled (DOM holds value, `FormData` / refs on submit).
- Form state = values, touched, dirty, errors, isSubmitting. React Hook Form: `register` (refs), schema resolver (zod), subscribe-only re-renders.
- Errors: validate on blur/submit first, then on change ("reward early, punish late"). React 19: `useActionState`, `<form action>`.
- Trap: input loses focus each keystroke → component defined inside another (new type every render). Define outside, stable keys.

## E20 · State machines
- Boolean soup: 3 booleans = 8 combos, ~4 valid. Use one `status` + explicit transitions.
- `machine = { idle: { SUBMIT: 'submitting' }, submitting: { OK, FAIL }, error: { RETRY } }`; unknown events are ignored.
- XState for complex flows (nested/parallel states, guards, timers, visual editor). Double payment: machine ignores SUBMIT + disable button + idempotency key.

## E21 · Immer
- React compares by reference; mutation = same object = no re-render. Nested spreads are error-prone.
- `produce(state, draft => { draft.user.address.city = 'Pune' })`: Proxy records writes, copy-on-write, structural sharing, frozen in dev.
- Used in RTK `createSlice`, `useImmer`, Zustand immer middleware. Trap: `d => d.count = 5` mutates AND returns → throws; use braces.

## E22 · IQ: URL · forms · machines · Immer
- What goes in the URL (and what doesn't) · controlled vs uncontrolled (+ focus-loss bug) · isLoading && isError → status machine · how Immer mutates safely.

## E23 · Finale: one food order
- URL (search + filters) · local (dropdown) · server cache (menu) · store + selectors (cart, badge, derived total) · context (theme, user) · form library (address) + invalidation · state machine (payment) · normalized orders · optimistic like + rollback · Immer updates.
