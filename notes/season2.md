# Frontend Decoded · Season 2 cheat sheets (DM these for "Comment NOTES")

## E01 · White screen first
- Every strategy answers one question: **who builds the HTML, and when?** Server (before sending) or browser (after arriving).
- Server-rendered: HTML has content → paint now, JS later. Client-rendered: empty HTML → download JS → run → fetch → paint.
- See it: DevTools → Performance → ✓ Screenshots, Network = Slow 4G → reload → filmstrip.
- Trap: a white screen isn't always the network. Big bundles take seconds to parse/run on cheap CPUs → throttle CPU (4x) too.

## E02 · Client-side rendering (CSR)
- Server sends `<div id="root"></div>` + a bundle; JS builds the DOM in the browser.
- View Source = what the server sent (empty). Elements = live DOM after JS (full).
- + static hosting, instant after first load. − slow first paint, crawlers/previews without JS see nothing.
- Trap: Google can render JS (sometimes deferred), but WhatsApp/LinkedIn link previews read raw HTML → blank preview.

## E03 · Client-side routing
- JS intercepts link clicks, `history.pushState()` updates the URL, fetches data, swaps part of the page. `popstate` = Back button.
- See it: YouTube → Network → Doc filter: no new document on video click; Fetch/XHR shows JSON (`next?…`, `player?…`).
- Trap: refreshing `/products/42` → 404, because the server only has `index.html`. Fix: rewrite all routes to `index.html` (`try_files $uri /index.html;`).

## E04 · Server-side rendering (SSR)
- Every request: server fetches data + builds full HTML → browser paints immediately; JS loads after to make it interactive.
- TTFB goes up (server is cooking), first paint comes sooner.
- See it: View Source on Amazon shows titles/prices; Network → document → Timing → "Waiting for server response" ≈ render time.
- Trap: SSR isn't always faster — slow DB or far server = huge TTFB, and still not interactive until JS. SSR moves work, doesn't delete it.

## E05 · Static site generation (SSG)
- HTML built once at **build time**, copied to CDN edges, served as-is. Great for docs, blogs, marketing.
- Headers: cache HIT, large `age` → built long before you asked.
- Trap: 50k products + hourly prices → slow builds + stale until next deploy. Not on its own.

## E06 · Incremental static regeneration (ISR)
- Static page + expiry. After it expires, the next visitor still gets the old page; a rebuild of that page runs in the background.
- Next.js: `export const revalidate = 60;` · on-demand: `revalidatePath('/product/42')`.
- Same idea in HTTP: `Cache-Control: s-maxage=60, stale-while-revalidate`.
- Trap: the first visitor after expiry still sees the OLD page; pages nobody visits stay stale.

## E08 · Hydration
- Server HTML = a picture. Hydration = React re-runs components in the browser and attaches handlers to the existing DOM.
- `renderToString(<App />)` on the server · `hydrateRoot(root, <App />)` in the browser.
- Runs on the main thread → one long task; taps wait.
- Trap: it does NOT rebuild the DOM, but it DOES run every component again → CPU cost.

## E09 · Hydration mismatch
- Rule: server HTML must equal the browser's first render.
- Causes: `Date`, `Math.random()`, `window`/`localStorage` in render, timezone/locale, invalid nesting (`<div>` in `<p>`), extensions.
- Fix: same placeholder on both sides → fill browser-only values in `useEffect`. Tiny diffs: `suppressHydrationWarning`.
- Trap: `typeof window` checks in render CAUSE mismatches.

## E10 · Visible but not clickable
- The uncanny valley: visible (FCP) but not interactive (JS loading/hydrating).
- FCP = first see something · TTI = reliably responds · TBT = blocked time in between. Field: INP.
- See it: Performance, CPU 4x slowdown → gap between first content screenshot and end of long tasks.
- Trap: green Lighthouse (one lab device) ≠ real users on cheap phones → check field INP.

## E11 · Selective hydration
- Classic hydration is all-or-nothing. React 18 hydrates each `<Suspense>` boundary independently, yielding between chunks.
- Clicking an un-hydrated part → React hydrates it first, then replays the click.
- Trap: it doesn't make JS smaller — same code downloads and runs; only order + chunking change.

## E13 · Streaming SSR
- Send the shell + fallbacks first; stream the slow parts later with a tiny script that swaps them in.
- React: `renderToPipeableStream(<App />, { onShellReady() { stream.pipe(res) } })`.
- Works because HTTP bodies arrive in pieces (chunked in 1.1, DATA frames in 2/3).
- See it: Timing → long "Content Download"; View Source → `<div hidden id="S:0">` + `$RC(...)` scripts.
- Trap: once the first chunk is out, status/headers are sent → no 404/redirect later. Decide before the shell.

## E14 · React Server Components (RSC)
- Run only on the server; can be `async` and read the DB; their code never ships. Only output (RSC payload) does.
- Interactive parts = `'use client'` components; only those ship JS.
- See it: nextjs.org → Network → `?_rsc=` requests on navigation.
- RSC ≠ SSR: SSR = HTML for first load, then everything hydrates. RSC never hydrates, refetchable on navigation. Frameworks use both.
- Trap: no `useState`/`onClick` in server components → pass data as props to a client component.

## E15 · Server Actions
- `'use server'` function called like a normal function → React sends a POST (`Next-Action: <id>` header).
- Works with `<form action={fn}>` even before JS loads (progressive enhancement).
- Trap: it's a PUBLIC POST endpoint. Always check auth and validate inputs inside the action.

## E16 · Islands architecture
- Static HTML by default; only interactive widgets hydrate, each independently (`<astro-island>` in Elements).
- Astro: `client:load`, `client:visible` (IntersectionObserver), `client:idle`.
- Trap: islands are separate apps → props can't cross. Share via a store (nanostores), custom events, or rethink boundaries.

## E17 · Resumability
- Qwik: server serializes state + event wiring into HTML; browser resumes without re-running components.
- Handlers are URLs to small chunks (`on:click="q-…js#s_…"`); one tiny global listener loads code on interaction.
- Trap: first interaction must fetch code → slow on bad networks; mitigate by prefetching likely handlers.

## E18 · Edge rendering
- Run SSR in many small data centers near users (where CDNs live). Lighter runtimes: no full Node, small memory/CPU limits.
- Great for personalization, redirects, A/B tests, auth checks.
- Trap: edge render + single-region DB = every query crosses the planet. Only helps when data is close or cached.

## E19 · Case study: an online store
- 3 questions per page: SEO? Same for everyone? How often does data change?
- `/blog` SSG · `/` ISR · `/product/:id` ISR + client islands (price/stock/cart) · `/search` streaming SSR · cart/checkout/account CSR.
- Trap: one strategy for the whole app. Choose per route, even per component.

## E21 · Finale
- Blog = SSG (+ ISR, islands). Amazon = SSR (fast paint, then JS makes it interactive). Gmail = CSR + client routing (slow start, instant after).
- Modern toolbox (streaming, RSC, actions, edge, resumability) = less work on the user's phone without losing interactivity.
