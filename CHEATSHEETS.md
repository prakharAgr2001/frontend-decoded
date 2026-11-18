# Tech, Explained · cheat sheets

Key ideas, DevTools tricks and interview traps from every reel. Find your episode below (S = season, E = episode).

- [Season 1](#season-1)
- [Season 2](#season-2)
- [Season 3](#season-3)
- [Season 4](#season-4)
- [Season 5](#season-5)
- [Season 6](#season-6)

## Season 1

### S1 · E01 · URL to pixels
- 5 journeys: **DNS** (name → IP) → **TCP** (connection) → **TLS** (encrypt + verify) → **HTTP** (request) → **render** (HTML → pixels).
- See it: DevTools → Network → first request → Timing (DNS Lookup, Initial connection, SSL, Waiting, Content Download).
- Trap: DNS isn't done every visit — browser, OS and resolver cache it. First load is usually slowest.

### S1 · E02 · DNS
- Phonebook of the internet: domain → IP address.
- Resolver walks root → TLD (.com) → authoritative name servers. Answers carry a **TTL**; cached until it expires.
- Try: `nslookup google.com`. Trap: after a server move some users hit the old IP until TTL expires → lower TTL before migrating.

### S1 · E03 · TCP handshake
- SYN → SYN-ACK → ACK = 1 round trip before any data (e.g. ~200 ms India ↔ US).
- Keep-alive reuses connections; later requests show 0 ms "Initial connection".
- Trap: TCP guarantees order, so one lost packet blocks everything behind it (head-of-line blocking) → why HTTP/3 exists.

### S1 · E04 · HTTPS & the padlock
- HTTPS = HTTP over TLS. 3 promises: **encryption, integrity, authentication**.
- Certificate chain: root CA (trusted by browser) → intermediate → site. TLS 1.3 handshake = 1 round trip (TLS 1.2 = 2).
- Trap: padlock = private connection, **not** a safe site. Phishing sites have valid certs.

### S1 · E05 · HTTP/1.1 vs 2 vs 3
- 1.1: one request per connection at a time → ~6 connections per site.
- 2: multiplexing + header compression on ONE TCP connection — but a lost packet stalls all streams.
- 3: QUIC over UDP, independent streams, survives Wi-Fi → mobile switches. Trap: HTTP/2 isn't always faster on lossy networks.

### S1 · E06 · CDNs
- Copies of files on edge servers near users; hit = fast, miss = fetch once from origin then cache.
- Headers: `x-cache`, `cf-cache-status`, `age`.
- Trap: users see old assets after deploy → versioned (hashed) file names + purge.

### S1 · E08 · DOM & CSSOM
- HTML → DOM tree; CSS → CSSOM tree. CSS blocks rendering; classic `<script>` blocks parsing.
- View Source = what arrived; Elements = live DOM.
- Trap: DOM ≠ HTML (browser fixes markup, JS mutates it).

### S1 · E09 · Layout → Paint → Composite
- Render tree (visible nodes) → Layout (size/position) → Paint (pixels) → Composite (GPU stacks layers).
- Performance panel: purple = layout, green = paint.
- Q: `display:none` removes from render tree (no space); `visibility:hidden` keeps the space.

### S1 · E10 · Reflow vs repaint
- Geometry (width/height/top) → layout + paint + composite. Color → paint + composite. transform/opacity → composite only.
- Reflow spreads to siblings/parents. DevTools → Rendering → Paint flashing.
- Trap: reading `offsetHeight` right after a style write forces synchronous layout.

### S1 · E11 · Layout thrashing
- Read/write/read/write in a loop → a layout per read. Fix: batch all reads, then all writes; schedule writes in `requestAnimationFrame`.
- Shows as "Forced reflow is a likely performance bottleneck" in Performance.
- Q: layout-forcing reads: offsetHeight/Top, clientWidth, scrollTop, getBoundingClientRect().

### S1 · E12 · Smooth animation
- Animate `transform`/`opacity` (compositor, GPU layer) not `left/top/width` (layout every frame).
- `will-change: transform` hints a layer — each layer costs GPU memory, don't overuse.
- Check: Rendering → Frame Rendering Stats.

### S1 · E14 · One-chef kitchen
- JS runs on one main thread that also does style, layout, paint. A 3 s loop freezes everything.
- Waiting (timers, fetch, events) happens in browser Web APIs; results come back through queues.
- Trap: `setTimeout(fn, 0)` = "as soon as possible", not "now".

### S1 · E15 · Call stack & task queue
- `log A; setTimeout(log B, 0); log C` → A, C, B.
- Stack runs sync code; Web APIs hold timers; callbacks wait in the task queue; event loop moves a task when the stack is empty.
- Q: no true 0 ms — deeply nested timers clamp to ≥ 4 ms.

### S1 · E16 · Microtasks vs tasks
- Tasks: timers, events. Microtasks: promise callbacks, `queueMicrotask`.
- After each task the loop drains ALL microtasks (incl. new ones), then may render, then next task. `1,timeout 2,promise 3,4` → 1 4 3 2.
- Trap: microtask starvation freezes the page.

### S1 · E17 · 16 ms frame budget
- 60 Hz ≈ 16.7 ms per frame (120 Hz ≈ 8.3 ms). Keep your JS ≲ 10 ms.
- `requestAnimationFrame` runs right before paint, once per frame, pauses in background tabs. Use its timestamp (time-based motion).
- `setInterval` drifts against frames.

### S1 · E18 · Long tasks
- > 50 ms = long task; blocks input. 100 ms feels instant (50 task + 50 input/paint).
- Fix: chunk work and yield (`await scheduler.yield()` or `setTimeout`).
- Metric: **INP** (Interaction to Next Paint), Core Web Vital since 2024 (replaced FID).

### S1 · E20 · Bubbling & capturing
- Phases: capture ↓ → target → bubble ↑. Listeners default to bubble; `{ capture: true }` for capture.
- `stopPropagation` (stop the journey) ≠ `preventDefault` (stop default action).
- `target` = clicked element, `currentTarget` = element whose listener runs. focus/blur/mouseenter/mouseleave don't bubble.

### S1 · E21 · Event delegation
- One listener on the parent + `e.target.closest('.row')`.
- Fewer listeners, works for rows added later, no listener leaks. DevTools → Event Listeners → Ancestors.
- Trap: needs bubbling events; a child's `stopPropagation` hides it.

### S1 · E22 · Memory leaks
- GC frees what's unreachable from roots; a leak is unneeded but still reachable memory.
- Suspects: listeners not removed, intervals after unmount, ever-growing caches, detached DOM nodes. Use useEffect cleanup, WeakMap.
- Memory panel: compare heap snapshots, filter "Detached". Closures keep captured variables alive.

### S1 · E23 · Observers
- IntersectionObserver (lazy load, infinite scroll, autoplay, impressions), ResizeObserver, MutationObserver, PerformanceObserver.
- Better than scroll listeners: browser computes intersections, no forced layout in your code, fires only on threshold crossings.

## Season 2

### S2 · E01 · White screen first
- Every strategy answers one question: **who builds the HTML, and when?** Server (before sending) or browser (after arriving).
- Server-rendered: HTML has content → paint now, JS later. Client-rendered: empty HTML → download JS → run → fetch → paint.
- See it: DevTools → Performance → ✓ Screenshots, Network = Slow 4G → reload → filmstrip.
- Trap: a white screen isn't always the network. Big bundles take seconds to parse/run on cheap CPUs → throttle CPU (4x) too.

### S2 · E02 · Client-side rendering (CSR)
- Server sends `<div id="root"></div>` + a bundle; JS builds the DOM in the browser.
- View Source = what the server sent (empty). Elements = live DOM after JS (full).
- + static hosting, instant after first load. − slow first paint, crawlers/previews without JS see nothing.
- Trap: Google can render JS (sometimes deferred), but WhatsApp/LinkedIn link previews read raw HTML → blank preview.

### S2 · E03 · Client-side routing
- JS intercepts link clicks, `history.pushState()` updates the URL, fetches data, swaps part of the page. `popstate` = Back button.
- See it: YouTube → Network → Doc filter: no new document on video click; Fetch/XHR shows JSON (`next?…`, `player?…`).
- Trap: refreshing `/products/42` → 404, because the server only has `index.html`. Fix: rewrite all routes to `index.html` (`try_files $uri /index.html;`).

### S2 · E04 · Server-side rendering (SSR)
- Every request: server fetches data + builds full HTML → browser paints immediately; JS loads after to make it interactive.
- TTFB goes up (server is cooking), first paint comes sooner.
- See it: View Source on Amazon shows titles/prices; Network → document → Timing → "Waiting for server response" ≈ render time.
- Trap: SSR isn't always faster — slow DB or far server = huge TTFB, and still not interactive until JS. SSR moves work, doesn't delete it.

### S2 · E05 · Static site generation (SSG)
- HTML built once at **build time**, copied to CDN edges, served as-is. Great for docs, blogs, marketing.
- Headers: cache HIT, large `age` → built long before you asked.
- Trap: 50k products + hourly prices → slow builds + stale until next deploy. Not on its own.

### S2 · E06 · Incremental static regeneration (ISR)
- Static page + expiry. After it expires, the next visitor still gets the old page; a rebuild of that page runs in the background.
- Next.js: `export const revalidate = 60;` · on-demand: `revalidatePath('/product/42')`.
- Same idea in HTTP: `Cache-Control: s-maxage=60, stale-while-revalidate`.
- Trap: the first visitor after expiry still sees the OLD page; pages nobody visits stay stale.

### S2 · E08 · Hydration
- Server HTML = a picture. Hydration = React re-runs components in the browser and attaches handlers to the existing DOM.
- `renderToString(<App />)` on the server · `hydrateRoot(root, <App />)` in the browser.
- Runs on the main thread → one long task; taps wait.
- Trap: it does NOT rebuild the DOM, but it DOES run every component again → CPU cost.

### S2 · E09 · Hydration mismatch
- Rule: server HTML must equal the browser's first render.
- Causes: `Date`, `Math.random()`, `window`/`localStorage` in render, timezone/locale, invalid nesting (`<div>` in `<p>`), extensions.
- Fix: same placeholder on both sides → fill browser-only values in `useEffect`. Tiny diffs: `suppressHydrationWarning`.
- Trap: `typeof window` checks in render CAUSE mismatches.

### S2 · E10 · Visible but not clickable
- The uncanny valley: visible (FCP) but not interactive (JS loading/hydrating).
- FCP = first see something · TTI = reliably responds · TBT = blocked time in between. Field: INP.
- See it: Performance, CPU 4x slowdown → gap between first content screenshot and end of long tasks.
- Trap: green Lighthouse (one lab device) ≠ real users on cheap phones → check field INP.

### S2 · E11 · Selective hydration
- Classic hydration is all-or-nothing. React 18 hydrates each `<Suspense>` boundary independently, yielding between chunks.
- Clicking an un-hydrated part → React hydrates it first, then replays the click.
- Trap: it doesn't make JS smaller — same code downloads and runs; only order + chunking change.

### S2 · E13 · Streaming SSR
- Send the shell + fallbacks first; stream the slow parts later with a tiny script that swaps them in.
- React: `renderToPipeableStream(<App />, { onShellReady() { stream.pipe(res) } })`.
- Works because HTTP bodies arrive in pieces (chunked in 1.1, DATA frames in 2/3).
- See it: Timing → long "Content Download"; View Source → `<div hidden id="S:0">` + `$RC(...)` scripts.
- Trap: once the first chunk is out, status/headers are sent → no 404/redirect later. Decide before the shell.

### S2 · E14 · React Server Components (RSC)
- Run only on the server; can be `async` and read the DB; their code never ships. Only output (RSC payload) does.
- Interactive parts = `'use client'` components; only those ship JS.
- See it: nextjs.org → Network → `?_rsc=` requests on navigation.
- RSC ≠ SSR: SSR = HTML for first load, then everything hydrates. RSC never hydrates, refetchable on navigation. Frameworks use both.
- Trap: no `useState`/`onClick` in server components → pass data as props to a client component.

### S2 · E15 · Server Actions
- `'use server'` function called like a normal function → React sends a POST (`Next-Action: <id>` header).
- Works with `<form action={fn}>` even before JS loads (progressive enhancement).
- Trap: it's a PUBLIC POST endpoint. Always check auth and validate inputs inside the action.

### S2 · E16 · Islands architecture
- Static HTML by default; only interactive widgets hydrate, each independently (`<astro-island>` in Elements).
- Astro: `client:load`, `client:visible` (IntersectionObserver), `client:idle`.
- Trap: islands are separate apps → props can't cross. Share via a store (nanostores), custom events, or rethink boundaries.

### S2 · E17 · Resumability
- Qwik: server serializes state + event wiring into HTML; browser resumes without re-running components.
- Handlers are URLs to small chunks (`on:click="q-…js#s_…"`); one tiny global listener loads code on interaction.
- Trap: first interaction must fetch code → slow on bad networks; mitigate by prefetching likely handlers.

### S2 · E18 · Edge rendering
- Run SSR in many small data centers near users (where CDNs live). Lighter runtimes: no full Node, small memory/CPU limits.
- Great for personalization, redirects, A/B tests, auth checks.
- Trap: edge render + single-region DB = every query crosses the planet. Only helps when data is close or cached.

### S2 · E19 · Case study: an online store
- 3 questions per page: SEO? Same for everyone? How often does data change?
- `/blog` SSG · `/` ISR · `/product/:id` ISR + client islands (price/stock/cart) · `/search` streaming SSR · cart/checkout/account CSR.
- Trap: one strategy for the whole app. Choose per route, even per component.

### S2 · E21 · Finale
- Blog = SSG (+ ISR, islands). Amazon = SSR (fast paint, then JS makes it interactive). Gmail = CSR + client routing (slow start, instant after).
- Modern toolbox (streaming, RSC, actions, edge, resumability) = less work on the user's phone without losing interactivity.

## Season 3

### S3 · E01 · 100 ms = money
- Google research: 53% of mobile visits are abandoned if a page takes > 3 s. Often-quoted Amazon finding: +100 ms ≈ −1% sales.
- Response-time limits (Nielsen): 0.1 s feels instant · 1 s keeps flow · 10 s loses attention.
- Two jobs: **be fast** (send less, do less on the main thread) and **feel fast** (useful content early, instant feedback).
- Try: DevTools → Network → throttling "Slow 4G" → reload. Trap: averages hide slow users → report **p75**.

### S3 · E02 · Core Web Vitals
- **LCP** (loading) ≤ 2.5 s · **INP** (responsiveness) ≤ 200 ms · **CLS** (visual stability) ≤ 0.1.
- Graded at the **75th percentile** of real Chrome visits (CrUX), mobile and desktop separately.
- See it: PageSpeed Insights → "Discover what your real users are experiencing". Trap: INP replaced FID in March 2024.

### S3 · E03 · LCP
- Time until the largest image / text block in the viewport renders. Candidates: `<img>`, video poster, CSS background image, text blocks.
- 4 parts: TTFB → resource load delay → load duration → render delay. Usually the *delay* (image found late) is the problem.
- See it: Performance panel → LCP marker + LCP breakdown insight. Trap: `loading="lazy"` on the hero makes LCP worse.

### S3 · E04 · CLS
- Sum of unexpected shifts; each = impact × distance; grouped into bursts (session windows); your worst burst = CLS.
- Culprits: images without width/height, ads/embeds without reserved space, injected banners, font swaps. Fix: reserve space (`width/height`, `aspect-ratio`, `min-height`).
- See it: Rendering → Layout Shift Regions. Trap: shifts within 500 ms of a tap/keypress are excluded; `transform` animations never shift layout.

### S3 · E05 · INP
- Input → next paint. Parts: input delay (main thread busy) + processing (handlers) + presentation delay (style/layout/paint).
- Roughly your *worst* interaction of the visit, not an average. Fix: feedback first, `await scheduler.yield()`, heavy work after; break long tasks.
- See it: Performance panel live metrics → interactions list. Trap: scroll and hover are not counted — only click, tap, key press.

### S3 · E06 · TTFB · FCP · TBT
- TTFB (first byte, good ≤ 0.8 s) → FCP (first anything, ≤ 1.8 s) → LCP. Slow TTFB = server, distance, redirects → CDN, caching.
- **TBT** = sum over long tasks of (duration − 50 ms) between FCP and interactive. Lab stand-in for INP; Lighthouse weight 30% (largest).
- Puzzle: tasks 70, 140, 40 ms → TBT = 20 + 90 + 0 = **110 ms**.

### S3 · E07 · Lab vs field
- Lab (Lighthouse): one run, simulated mid-range phone, throttled, clean browser → repeatable, for debugging.
- Field (CrUX / RUM): real users, 28 days, p75. They disagree: lab has no INP, only first screen, one device.
- RUM: `import { onLCP, onINP, onCLS } from 'web-vitals'` + `navigator.sendBeacon`. Trap: CrUX is a 28-day rolling window → fixes fade in over weeks.

### S3 · E08 · IQ: measuring performance
- CWV + thresholds at p75 · Lighthouse 98 but poor INP (no interactions, TBT is a proxy, real devices, 28 days) · slow LCP with fast image download (TTFB, load delay → in HTML + preload/fetchpriority, render delay) · banner CLS (reserve, overlay, transform).

### S3 · E09 · Critical rendering path
- HTML → DOM, CSS → CSSOM → render tree → first pixels. CSS is **render-blocking**; plain `<script>` is **parser-blocking**.
- Shrink it: inline critical CSS, load the rest non-blocking, `media="print"` for non-critical sheets, `defer` scripts.
- See it: Lighthouse "Render blocking requests"; Performance panel request details "Render blocking". Trap: a script after a stylesheet waits for that CSS → CSS can block parsing too.

### S3 · E10 · async vs defer
- plain: stop parsing, fetch, run. **async**: fetch in parallel, run on arrival, no order. **defer**: fetch in parallel, run after parsing, in document order, before DOMContentLoaded.
- defer → app code; async → independent scripts (analytics). `type="module"` is deferred by default.
- Trap: async scripts that depend on each other break randomly; `defer` does nothing on inline scripts.

### S3 · E11 · Resource hints
- `preconnect` (DNS+TCP+TLS early) · `dns-prefetch` (DNS only) · `preload` (this page, late-discovered, high priority, needs `as`) · `prefetch` (next page, lowest priority).
- See it: Network → Priority column. Trap: preloading everything steals bandwidth; Chrome warns about unused preloads; font preload needs `crossorigin` or it downloads twice.

### S3 · E12 · Code splitting
- Dynamic `import()` → separate chunk loaded on demand. Split by route, heavy feature, below the fold; shared libs in a vendor chunk.
- See it: DevTools → Coverage (red = downloaded, never ran). Trap: too many tiny chunks → request waterfalls.

### S3 · E13 · Lazy routes
- `const Orders = lazy(() => import('./pages/Orders'))` inside `<Suspense fallback>`. Hide the delay: prefetch on hover / in viewport (Next.js `<Link>` does this in production).
- Rules: never lazy-load the landing route; fallbacks must hold layout. Trap: after a deploy, old tabs hit `ChunkLoadError` → keep old chunks, catch + reload.

### S3 · E14 · Tree shaking
- Bundler follows imports from the entry, keeps used exports, drops the rest. Needs **ES modules** (static); CommonJS `require` usually can't be shaken.
- Side effects: mark `"sideEffects": false` (or a list) in package.json. `import _ from 'lodash'` ≈ 70 KB vs `import { debounce } from 'lodash-es'`.
- Trap: barrel files (`export * from …`) can pull whole libraries in → import from the file directly.

### S3 · E15 · Bundle diet
- 100 KB of JS ≠ 100 KB of image: JS is downloaded, parsed, compiled and executed on the main thread.
- Measure (bundle analyzer), then: moment → date-fns / Intl, drop unneeded polyfills, dedupe versions, check bundlephobia, use the platform (fetch, `<dialog>`).
- Trap: "200 KB gzipped" — the browser parses the uncompressed size (~700 KB). Compression saves network, not CPU.

### S3 · E16 · Minify + Brotli
- Minify: strip whitespace/comments, rename locals. Compress: gzip, Brotli (≈ 15–20% smaller than gzip on text).
- `accept-encoding: gzip, deflate, br, zstd` → `content-encoding: br`. See it: Network → big request rows show transferred vs real size.
- Trap: don't compress JPEG/PNG/MP4/WOFF2 — already compressed. Compress text: HTML, CSS, JS, JSON, SVG.

### S3 · E17 · IQ: loading + bundles
- When scripts run (plain/async/defer/module) · preconnect vs preload vs prefetch · why tree shaking keeps code (CJS, side effects, barrels, dynamic access) · cutting a 1.5 MB bundle (measure → split → replace → minify + Brotli → budget).

### S3 · E18 · Responsive images
- `srcset` (files + `w` widths) + `sizes` (display width) → browser picks the smallest sharp file, including DPR. `<picture>` for AVIF/WebP + JPEG fallback and art direction (`media`).
- See it: Elements → hover `<img>`: rendered vs intrinsic size; Lighthouse "Properly size images". Trap: no `sizes` → assumes `100vw` → biggest file.

### S3 · E19 · LCP image priority
- Images start Low and are boosted only after layout. `fetchpriority="high"` on the hero (Chrome team test on Google Flights: LCP 2.6 s → 1.9 s).
- Must be discoverable by the preload scanner: plain `<img>` in HTML, or `<link rel="preload" as="image" fetchpriority="high">`. Never lazy, don't wait for client JS.
- Trap: high priority on everything = nothing is high priority.

### S3 · E20 · Web fonts
- FOIT (invisible text while loading) vs FOUT (fallback, then swap). `font-display`: block · swap · optional.
- Swap can cause CLS → matched fallback with `size-adjust`, `ascent-override`. Arrive sooner: self-host, preload 1–2 files, woff2, subset.
- IQ: safest for CWV is often `optional` (no invisible text, no late shift) — trade-off: slow first visits may never show the brand font.

### S3 · E21 · Third-party cost
- Third-party JS runs on *your* main thread: long tasks (INP), late banners (CLS), extra origins (connections).
- Measure: DevTools request blocking → compare. Tame: facades, delay until interaction, self-host, Partytown (web worker). See it: Performance "3rd parties" insight.
- Trap: `async` only avoids parser blocking; the script still runs on the main thread.

### S3 · E22 · IQ: images, fonts, third parties
- Why `sizes` · slow hero LCP checklist (HTML, fetchpriority/preload, not lazy, right size/format/CDN) · no FOIT + no font CLS · adding a chat widget safely (measure, facade, after interaction, reserve space).

### S3 · E23 · Debounce
- Run once after the user stops (e.g. 300 ms of quiet). Search boxes, autosave, resize.
- `clearTimeout(timer); timer = setTimeout(() => fn(...args), wait);`
- Trap: debounce doesn't fix race conditions → AbortController or ignore stale responses.

### S3 · E24 · Throttle
- At most once per interval, steadily during the storm (scroll progress, drag). Debounce = after silence; throttle = regular.
- Better for visuals: `requestAnimationFrame`; for visibility: `IntersectionObserver`.
- Trap: naive throttle drops the last call → add a trailing call.

### S3 · E25 · Virtualization
- Render only visible rows + overscan; a tall spacer keeps the scrollbar right; rows are recycled. Libraries: TanStack Virtual, react-window.
- Lighter option: `content-visibility: auto` + `contain-intrinsic-size` (stays in DOM). See it: Performance monitor → DOM Nodes stays flat.
- Trap: Ctrl+F misses unrendered rows, screen readers, unknown heights → jumpy scrollbar.

### S3 · E26 · Web Workers
- JS on another thread; no DOM; talk via `postMessage` / `onmessage`. Good for parsing, image processing, search indexes, crypto, diffing.
- See it: Performance panel shows a separate Worker track.
- Trap: postMessage copies data (structured clone) → transfer `ArrayBuffer`s: `postMessage(buf, [buf])`.

### S3 · E27 · Why React re-renders
- State change · context change · **parent re-render** (props changing is *not* the trigger). Render ≠ DOM update (commit applies only real changes).
- Fix structurally: move state down, pass components as children. See it: React DevTools "Highlight updates" + Profiler "Why did this render?".
- IQ: same value via `Object.is` → bail out; a new object with the same contents re-renders.

### S3 · E28 · Memo myths
- `React.memo` (shallow props), `useMemo` (value), `useCallback` (function identity). Memo isn't free: storage + comparison every render.
- Inline objects/arrow functions break memo → stabilize with useMemo/useCallback. Memoize on evidence (Profiler ranked view).
- Trap: useMemo is a performance hint, never a correctness guarantee — React may discard the cache.

### S3 · E29 · useTransition + React Compiler
- `startTransition(() => setFilter(v))` marks non-urgent updates; renders are interruptible; `isPending` for subtle feedback. `useDeferredValue` when you don't own the setter.
- React Compiler (v1.0, late 2025) auto-memoizes at build time; DevTools shows a "Memo" badge.
- Trap: transitions don't make work faster, only interruptible → still virtualize / do less.

### S3 · E30 · Chunking long tasks
- Slice by time (~10 ms), not item count; `await scheduler.yield()` continues near the front of the queue (setTimeout goes to the back).
- `scheduler.postTask(fn, { priority: 'user-blocking' | 'user-visible' | 'background' })`. See it: many small tasks with gaps instead of one red-cornered block.
- Trap: `await Promise.resolve()` is a microtask — it does not yield to rendering or input.

### S3 · E31 · Performance budgets
- Agreed limits, e.g. JS ≤ 170 KB compressed, LCP ≤ 2.5 s, TBT ≤ 200 ms. Kinds: quantity, milestone timings, rule-based scores.
- Enforce in CI: Lighthouse CI assertions, size-limit → fail the PR.
- IQ: start from current field data, set slightly better, ratchet down, test on a real mid-range phone.

### S3 · E32 · IQ: runtime
- Debounce vs throttle (+ rAF, IntersectionObserver) · 10k-row table (virtualize, content-visibility, paginate, trade-offs) · re-renders (causes, move state down, memo where measured, Compiler) · 400 ms click handler (feedback + yield, chunk, worker, transition).

### S3 · E33 · Finale: one product page, made fast
- Measure (CWV, field vs lab) → loading (CDN TTFB, critical CSS, defer, preconnect) → bundle (split, lazy, diet, Brotli) → hero (AVIF srcset, fetchpriority) → shifts (reserve space, font fallback) → third parties (facade, delay) → interactions (feedback first, transition, virtualize, worker, chunking) → budget in CI.

## Season 4

### S4 · E01 · What is state
- State = data your UI remembers right now that can change while the page is open. Rule: if it changes and the screen must show it, it's state.
- React's idea: **UI = f(state)**. Don't edit the screen; change state (`setX`) and React re-renders, touching only what differs in the DOM.
- Trap: don't store what you can compute. `const total = items.reduce(...)`, not `useState(total)` → two sources of truth drift.
- See it: React DevTools → Components → select a component → hooks panel shows live state.

### S4 · E02 · The 5 types of state
| Type | Examples | Home |
|---|---|---|
| Local UI | isOpen, activeTab, hovered | `useState` |
| Shared client | cart, theme, user | context / store |
| Server | menu, prices, orders | server cache (React Query, SWR, RTK Query) |
| URL | `?q=`, filters, page | the address bar |
| Form | values, touched, errors | form library |
- 3 questions: from the server? → cache. Survive refresh/share? → URL. Distant components? → context/store. Otherwise local.
- Classic mistake: server data copied into a global store = hand-written loading flags, refetching, cache rules.

### S4 · E03 · Colocation
- Keep state as close as possible to where it's used — and no higher. Lift only to the **closest common parent**.
- State at the top → every update re-renders from the top (S3·E27). Move it down, or pass heavy parts as `children`.
- Bonus: delete a component and its state goes too. Global only for truly app-wide values (user, theme, locale) — and even then, not one giant object.

### S4 · E04 · The context trap
- `useContext` subscribes to the **whole** value. Any change → every consumer re-renders.
- Trap 1: `value={{ user, cart }}` is a new object every render → `useMemo` it.
- Trap 2: one big context → split by concern (UserCtx, ThemeCtx, CartCtx) and split state from dispatch.
- `React.memo` does NOT stop context re-renders. Context = delivery, not a state manager; hot state → store with selectors.
- See it: React Profiler → "Why did this render? Context changed".

### S4 · E05 · IQ: state basics
- Props vs state (passed/read-only vs owned/changes; derive computables; `useRef` for non-visual) · 5 types + homes · search re-renders page (state too high → move down / children) · context fan-out (memo value, split, separate dispatch, store+selectors; memo won't help).

### S4 · E06 · Redux from scratch
- 3 ideas: one store · actions describe what happened (`{ type: 'cart/added', item }`) · reducers are pure `(state, action) → newState`.
- `createStore` ≈ 10 lines: `state`, `subs`, `getState`, `subscribe`, `dispatch` (run reducer → save → notify).
- One-way flow: UI → dispatch → reducer → new state → subscribers re-render. Redux DevTools = action log + time travel.
- Trap: mutate + return same reference → `Object.is(prev, next)` true → UI never updates, time travel breaks.

### S4 · E07 · Redux Toolkit
- Official way today. `createSlice` generates action types + creators; reducers can "mutate" because **Immer** gives a draft.
- `configureStore`: DevTools wired, dev checks for mutation + non-serializable values (Dates, functions).
- RTK Query = server-state cache inside Redux. Is Redux dead? No — big apps, many writers, logged/replayable changes. Overkill for small apps.

### S4 · E08 · Zustand · Jotai · MobX
- **Zustand**: `create((set) => ({...}))`, no Provider, read slices `useCart(s => s.items.length)`.
- **Jotai**: atoms + derived atoms (`atom(get => ...)`), re-render only on atoms you read.
- **MobX**: `makeAutoObservable` + `observer`, mutate directly, spreadsheet-style auto updates.
- Trap: module-level store on the server (SSR) is shared across requests → user data leaks. Create a store per request, pass via context.

### S4 · E09 · Selectors
- Selector picks the slice a component needs; component re-renders only when the result changes (`===` after every dispatch).
- Trap: `filter`/`map`/object literals return new references every time → always re-render. Use `createSelector` (memoized), separate selectors, or `shallowEqual` / `useShallow`.
- Selectors are where derived data lives (totals, counts, filtered lists).

### S4 · E10 · IQ: Redux & stores
- Redux flow · why RTK can `push` (Immer draft → new immutable copy; only in createSlice/createReducer) · context vs Zustand vs Redux (rarely-changing / low boilerplate / big teams; server data → query cache) · filter selector re-renders (new array → memoize/shallow).

### S4 · E11 · Server state
- Lives on a server, you hold a copy, others can change it → stale on arrival. Async, can fail, shared across users and tabs.
- Needs: caching, dedupe, refetch when stale, background updates, pagination, garbage collection.
- `useEffect` fetch: no cache, duplicate requests, races. Server Components (S2·E14) remove the client copy for read-only data; interactive data still needs a client cache.

### S4 · E12 · React Query
- `useQuery({ queryKey, queryFn })` → `data`, `isPending`, `error`. Key = cache address; same key = one request (dedupe).
- Stale-while-revalidate: show cache now, refetch in background, swap if changed.
- `staleTime` (fresh window, default 0) vs `gcTime` (unused data kept, default 5 min). Refetch on focus, reconnect, mount-when-stale.
- Trap: `isPending` (no data yet → skeleton) vs `isFetching` (any request incl. background → don't flash a spinner).

### S4 · E13 · Cache invalidation
- After a mutation: `qc.invalidateQueries({ queryKey: ['addresses'] })` → marks matching queries stale, refetches active ones.
- Keys are folders: prefix match (`['addresses']` hits `['addresses', 7]`); `exact: true` for one key.
- Or `setQueryData` with the server's response (skip a round trip). Too little = screens lie; too much = refetch the world.
- Other tabs: refetch on window focus; `BroadcastChannel`; server push (S6).

### S4 · E14 · Normalization
- Store each entity once, keyed by id; everything else references the id: `users.byId[7]`, `posts.byId[101].author = 7`.
- Wins: one source of truth, updates in one place, O(1) lookups, no deep spreads.
- Tools: RTK `createEntityAdapter`; Apollo/Relay normalize automatically (`__typename` + id). React Query caches per query (invalidate instead).

### S4 · E15 · Optimistic UI
- Update the UI as if success, send the request, fix on failure. Feels instant on slow networks.
- React Query: `onMutate` → `cancelQueries` → `setQueryData`. React 19: `useOptimistic` (value lives while the action runs).
- Use for likes, toggles, reorder, chat. Not for payments, last-item stock, anything where false success costs the user.
- Trap: cancel in-flight refetches first, or an old response overwrites your optimistic value.

### S4 · E16 · Rollback
- `onMutate`: snapshot `prev` and return it · `onError`: restore `ctx.prev` + toast with Retry · `onSettled`: invalidate (server truth wins).
- Races: like/unlike/like out of order → stale snapshot. Fix: send intent (`PUT { liked: true }`, idempotent) not toggle, serialize per item, always settle with a refetch.

### S4 · E17 · IQ: server state
- Server vs client state · `staleTime` vs `gcTime` · syncing after mutations (invalidate by prefix / setQueryData / focus / BroadcastChannel) · optimistic like with rollback (cancel → snapshot → write → onError restore → onSettled refetch).

### S4 · E18 · URL state
- If it should be shareable, bookmarkable, or reachable with Back → put it in the URL (path + query).
- `useSearchParams`: read from and write to the URL; it's the single source of truth (no useState copy).
- `replace` while typing, `push` for committed choices. Not in the URL: secrets/PII (logs, history, referrers), huge objects, ephemeral UI. Values are strings → parse + validate.

### S4 · E19 · Form state
- Controlled (`value` + `onChange`, a render per keystroke) vs uncontrolled (DOM holds value, `FormData` / refs on submit).
- Form state = values, touched, dirty, errors, isSubmitting. React Hook Form: `register` (refs), schema resolver (zod), subscribe-only re-renders.
- Errors: validate on blur/submit first, then on change ("reward early, punish late"). React 19: `useActionState`, `<form action>`.
- Trap: input loses focus each keystroke → component defined inside another (new type every render). Define outside, stable keys.

### S4 · E20 · State machines
- Boolean soup: 3 booleans = 8 combos, ~4 valid. Use one `status` + explicit transitions.
- `machine = { idle: { SUBMIT: 'submitting' }, submitting: { OK, FAIL }, error: { RETRY } }`; unknown events are ignored.
- XState for complex flows (nested/parallel states, guards, timers, visual editor). Double payment: machine ignores SUBMIT + disable button + idempotency key.

### S4 · E21 · Immer
- React compares by reference; mutation = same object = no re-render. Nested spreads are error-prone.
- `produce(state, draft => { draft.user.address.city = 'Pune' })`: Proxy records writes, copy-on-write, structural sharing, frozen in dev.
- Used in RTK `createSlice`, `useImmer`, Zustand immer middleware. Trap: `d => d.count = 5` mutates AND returns → throws; use braces.

### S4 · E22 · IQ: URL · forms · machines · Immer
- What goes in the URL (and what doesn't) · controlled vs uncontrolled (+ focus-loss bug) · isLoading && isError → status machine · how Immer mutates safely.

### S4 · E23 · Finale: one food order
- URL (search + filters) · local (dropdown) · server cache (menu) · store + selectors (cart, badge, derived total) · context (theme, user) · form library (address) + invalidation · state machine (payment) · normalized orders · optimistic like + rollback · Immer updates.

## Season 5

### S5 · E01 · REST
- Everything is a **resource** with its own URL (`/users/42`, `/posts/7/comments`). Act on it with verbs.
- GET read · POST create · PUT replace whole · PATCH change some fields · DELETE remove. Status: 200 OK · 201 Created · 404 Not Found.
- `fetch` does **not** throw on 404/500 → always check `res.ok`. Try: open `api.github.com/users/torvalds` in a tab.
- Trap: PUT vs POST is about **idempotency** — 5× PUT = one user, 5× POST = maybe 5 orders.

### S5 · E02 · GraphQL
- One endpoint (`POST /graphql`); the query is shaped like the answer; the response mirrors it. A schema defines types + fields.
- Fixes over-fetching (too much per call) and under-fetching (too many calls).
- Costs: one URL + POST → no free HTTP/CDN caching; deeply nested queries can be very expensive (add depth/complexity limits).
- See it: instagram.com → Network → filter `graphql`. Trap: errors often arrive as **200 OK** with an `errors` array → check it.

### S5 · E03 · REST vs GraphQL vs tRPC
- REST: many clients, public APIs, simplest caching. GraphQL: many screens picking their own fields. tRPC: one TypeScript team owns client + server (monorepo), end-to-end types, no schema/codegen.
- In the wild: GitHub (REST + GraphQL), Shopify Storefront (GraphQL), T3-stack apps (tRPC).
- Trap: GraphQL is not "faster" — fewer round trips, but careless queries are slow and you lose easy caching. Choose by clients + teams.

### S5 · E04 · Backend for Frontend (BFF)
- A small server owned by the frontend team: app makes **one call**; BFF fans out to services (in parallel, close to them), trims fields, returns screen-shaped data.
- Usually one BFF per experience (mobile vs web). Bonus: keeps tokens on the server, browser gets an `httpOnly` cookie.
- Trap: no business rules (pricing etc.) in the BFF — they get copied per BFF and drift. BFF = shaping only.

### S5 · E05 · IQ: API design
- Idempotent: GET, PUT, DELETE (POST no, PATCH not guaranteed) → matters for retries; POST needs an `Idempotency-Key`.
- GraphQL N+1 (1 query for posts + 1 per author) → batch with **DataLoader**.
- Mobile screen needing 4 services → BFF. When not GraphQL: CDN caching critical, simple CRUD, one TS team (tRPC).

### S5 · E06 · The offset bug
- `?limit=10&offset=10` → `LIMIT 10 OFFSET 10`. New item on top shifts rows → **duplicates**; deletes shift up → **skipped** items.
- Deep offsets are slow: DB still reads and discards every skipped row.
- Trap: offset is fine for rarely-changing data and jump-to-page UIs (admin tables, search results). It breaks on fast-changing feeds.

### S5 · E07 · Cursor pagination
- "10 items older than this one": response has `items` + opaque `nextCursor`; client sends `?after=<cursor>`; `null` = end.
- Server: `WHERE created_at < :cursor ORDER BY created_at DESC LIMIT 10` — with an index, page 1000 ≈ page 1.
- See it: `reddit.com/r/javascript.json` → `"after": "t3_…"`.
- Trap: ties on the sort key skip rows → sort by `(created_at, id)` and put both in the cursor. Cost: no jump to page 50.

### S5 · E08 · Infinite scroll vs pages
- Infinite: great for browsing on phones; footer unreachable, back button loses place, memory grows. Pages: hunting, shareable "page 3" URL, crawlable. Middle: **Load more**.
- Build: `IntersectionObserver` on a sentinel with `rootMargin: '600px'`; long lists → virtualization (S3E25).
- Trap: back button → top of feed. Keep loaded pages + scroll position (query cache or URL) and restore; don't refetch from page 1.

### S5 · E09 · IQ: pagination
- Duplicates on page 2 = offset + inserts → cursor. Missing items with timestamp cursor = ties → `(created_at, id)`.
- Jump to page 50 → offset (cap the depth). Infinite scroll without scroll listeners → IntersectionObserver + rootMargin (+ virtualization).

### S5 · E10 · Waterfalls
- Request 2 waits for request 1 → staircase in the Network waterfall; each step costs a round trip (~100–300 ms on mobile).
- React: parent fetches in an effect → renders child → child fetches = **fetch-on-render**. Fix: start early (route loader, hoist, prefetch) = fetch-then-render.
- Trap: true dependency (needs user id) → move the join to the server (one endpoint / BFF) so it happens next to the DB.

### S5 · E11 · Parallel requests
- Independent requests: start all, then `await Promise.all([...])` → total ≈ slowest, not the sum. HTTP/2 multiplexes; HTTP/1.1 ≈ 6 connections per host.
- `Promise.all` rejects on the first failure (good results lost). `Promise.allSettled` → `{status, value | reason}` for each.
- Trap: `await a(); await b(); await c();` is sequential. Create the promises first, then await them together.

### S5 · E12 · Race conditions
- Responses arrive in **network order**, not request order → an old, slow response can overwrite a newer one.
- React fix: `let ignore = false; … if (!ignore) setX(d); return () => { ignore = true; }`.
- Trap: debounce doesn't fix races (S3E23) — ignore or cancel stale requests; React Query keys data by query.

### S5 · E13 · AbortController
- `const c = new AbortController(); fetch(url, { signal: c.signal }); c.abort();` → really stops the request.
- In effects: abort in the cleanup; ignore `AbortError` (a cancel isn't a failure). `AbortSignal.timeout(5000)` for timeouts.
- See it: Network shows aborted requests as **(canceled)**. Trap: abort doesn't undo a POST already on the server → idempotency key + status check.

### S5 · E14 · Retries + backoff
- Exponential backoff: 1 s, 2 s, 4 s, 8 s… capped. Add **jitter** (random delay) to avoid the thundering herd.
- Retry network errors, timeouts/408, 429 (after Retry-After), 5xx like 503. Don't retry 400/401/404.
- React Query: queries retry 3× with `min(1000·2^n, 30000)` by default; mutations retry 0×. Trap: retry a POST only with an idempotency key.

### S5 · E15 · Deduplication
- Several components ask for the same thing → share the **in-flight promise** (Map of key → promise, delete on settle).
- React Query dedups by query key. Dedup ≠ cache: dedup shares a request in flight; cache keeps the answer afterwards.
- Trap: double fetch in dev = React **StrictMode** (mount → unmount → mount). Production fetches once.

### S5 · E16 · 429 Too Many Requests
- Rate limits: N requests per user / IP / key per window. Token bucket: each request spends a token; tokens refill steadily.
- See it: `api.github.com` headers `x-ratelimit-limit: 60`, `x-ratelimit-remaining`, `x-ratelimit-reset` (unauthenticated).
- On 429: read `Retry-After` and wait. Be a good client: debounce, dedupe, cache.
- Trap: per-IP limits block whole offices behind one NAT → limit per user / API key.

### S5 · E17 · Skeleton screens
- Skeletons show layout before data → feels faster; must **match** the real layout or you get CLS (S3E04).
- Don't flash: show only if loading takes > ~200 ms. Skeleton on first load (`isPending`); on refetch keep old data (`isFetching` → small spinner).
- See it: YouTube with Slow 4G. Trap: actions (saving) → spinner on the button; skeletons are for content.

### S5 · E18 · Partial failure
- An error thrown during render with no boundary unmounts the whole tree. Wrap each widget in an **ErrorBoundary** with fallback + retry.
- Data: `Promise.allSettled`. Decide what's critical (price → error page) vs optional (recommendations → hide).
- Trap: boundaries don't catch event-handler or async errors → put the error in state and throw during render, or `throwOnError` in your data library.

### S5 · E19 · Suspense boundaries
- A suspending component shows the nearest `<Suspense fallback>` until everything inside is ready. Streaming (S2E13) sends the shell then each boundary; selective hydration (S2E11).
- One boundary = waits for the slowest; one per component = popcorn + jumps. Group: critical first, own boundary for heavy parts, below-the-fold together.
- Pair each Suspense boundary with an ErrorBoundary. Trap: `useEffect` fetching never suspends → use `use(promise)`, a framework loader, or `useSuspenseQuery`.

### S5 · E20 · IQ: async edge cases
- all vs allSettled · search race (abort / ignore stale, debounce, key by query) · POST timeout (idempotency key, status check, backoff + jitter) · one big spinner (split Suspense boundaries, skeletons, streaming).

### S5 · E21 · Finale: one search page
- REST + BFF → cursor pagination + infinite scroll → debounce + AbortController (no races) → parallel, no waterfalls → retries/jitter, dedup, Retry-After → matching skeletons, isolated failures, grouped Suspense.
- Next: Season 6 · Real-time (polling → SSE → WebSockets → CRDTs).

## Season 6

### S6 · E01 · How did it arrive?
- HTTP is request → response: the server can't speak first. "Real-time" = the server can push the moment something happens.
- See it: WhatsApp Web → DevTools → Network → filter **WS** → click the connection → **Messages**. ↓ red = received, ↑ green = sent.
- Five transports: short polling · long polling · Server-Sent Events · WebSockets · WebRTC.
- Trap: "real-time means WebSockets" → no. Pick by **who talks** and **how often** (a badge can poll; AI answers stream over SSE).

### S6 · E02 · Short polling
- Ask on a fixed timer ("anything new?"). Cost = latency (up to one interval) + load (10,000 tabs ÷ 5 s = 2,000 req/s, mostly empty).
- Fine for rare updates where seconds of delay are OK: dashboards, build status, unread badges. Works through every proxy.
- Trap: `setInterval(fetch)` overlaps when the server slows → schedule the next poll with `setTimeout` *after* the response; skip work when `document.hidden`.

### S6 · E03 · Long polling
- Server holds the request open until there's news (or ~30 s timeout → empty response), client immediately asks again.
- Near-instant, plain HTTP. Costs: full request + headers per message, one open request per user.
- Trap: messages in the gap between polls → send a cursor (`?since=<last id>`) so the server returns everything after it.

### S6 · E04 · Server-Sent Events
- One HTTP response that never ends: `Content-Type: text/event-stream`. Format: `id:`, `event:`, `data:` lines, blank line ends an event.
- `new EventSource('/stream')` → `onmessage`. Auto-reconnects and sends **Last-Event-ID** so the server can resume.
- Limits: one-way (send with normal `fetch` POST), text only.
- Trap: HTTP/1.1 ≈ 6 connections per origin; each open stream holds one → 7th tab hangs. HTTP/2 multiplexes streams on one connection.

### S6 · E05 · WebSockets
- Starts as HTTP `GET` with `Upgrade: websocket` → `101 Switching Protocols` → same TCP connection carries frames both ways.
- Frame header 2–14 bytes vs hundreds of bytes of HTTP headers. `wss://` = over TLS.
- API: `onopen`, `send`, `onmessage`, `onclose`. Each message is a task (S1E15) → batch bursts, render once per frame (`requestAnimationFrame`).
- Trap: WebSockets do **not** reconnect by themselves. Reconnect, catch up and resend are your job (E10).

### S6 · E06 · WebRTC
- Browser ↔ browser audio, video, data. See it: on a Meet call open `chrome://webrtc-internals`.
- Signaling (your choice, usually a WebSocket) swaps **offer/answer (SDP)** + **ICE candidates**. STUN = "what's my public address", TURN = relay when direct fails.
- Code: `new RTCPeerConnection({ iceServers })` → `createDataChannel` / `addTrack` → `createOffer` → `setLocalDescription` → send via signaling.
- Trap: 100-person mesh = 99 uploads each. Big calls use an **SFU** (Selective Forwarding Unit): upload once, server forwards.

### S6 · E07 · The showdown
1. Audio/video/peer data → **WebRTC**. 2. Client sends often, low latency (chat, games, cursors) → **WebSockets**.
3. Server pushes, client listens (scores, notifications, AI answers) → **SSE**. 4. Rare updates / delay OK → **polling** (long polling if faster).
- SSE: one-way, built-in reconnect, text, plain HTTP. WS: two-way, binary, DIY reconnect, leaves HTTP after upgrade. Polling: most compatible, most wasteful.
- Trap: "chat needs WebSockets" → not necessarily: SSE down + POST up is valid and stays plain HTTP (caching, auth, load balancing).

### S6 · E08 · IQ: transports
- setInterval poll vs slow server (overlap, out of order → setTimeout after response, backoff, pause when hidden) · 7th SSE tab (HTTP/1.1 6-connection limit → HTTP/2 or share one stream) · million-viewer scores (SSE) · WebRTC offer delivery (no built-in signaling; STUN/TURN).

### S6 · E09 · Heartbeats
- A dead TCP connection doesn't announce itself (sleep, Wi-Fi drop) → **half-open** connection; app shows "online" forever. Proxies also kill idle connections.
- App-level ping/pong: every message resets a timer; silence > interval + margin (e.g. 35 s for 30 s pings) → `ws.close()` → reconnect.
- Browsers answer protocol ping frames silently, and JS can't send them → apps send their own `{type:'ping'}`.
- Trap: interval must be under the shortest idle timeout on the path (often 20–30 s), but not so fast it drains batteries.

### S6 · E10 · Reconnect
- See it: WhatsApp Web, Wi-Fi off → "Computer not connected" banner; on → missed messages appear.
- Naive instant reconnect → **thundering herd** after a server restart. Fix: exponential backoff (1, 2, 4, 8 … cap 30 s) + random **jitter** (S5E14).
- On open: resync `since=<last seq>`, then flush the outbox. Listen to `online` / `offline` / `visibilitychange`.
- `AbortController` (S5E13): one `abort()` removes the old socket's listeners and cancels its catch-up fetch.
- Trap: don't retry every close. 1000 = normal close; auth failures need re-login, not retries. Retry network errors (1006).

### S6 · E11 · Ordering
- One socket = TCP order. Many paths (devices, reconnects, HTTP + socket) = no order guarantee. Sender clocks lie.
- Server assigns a **sequence number per chat**. Client: drop `seq <= last`, buffer gaps and fetch missing ranges, apply in order.
- Trap: `async` onmessage handler that awaits (decrypt) can finish message 2 before 1 → queue and process one at a time.

### S6 · E12 · Acks & dedup
- WhatsApp ticks: 1 grey = server got it, 2 grey = delivered to the device, 2 blue = read. Clock = pending (optimistic UI, S4E15).
- Lost ack → retry → duplicate. Fix: client-generated id (`crypto.randomUUID()`), outbox until acked, server drops repeat ids, client merges its own echo.
- Guarantee: **at-least-once + dedup** ≈ exactly-once.
- Trap: generate the id on the **client**: a server id doesn't exist until the first attempt succeeds.

### S6 · E13 · Scaling WebSockets
- Sockets are stateful: Alice on server A, Bob on server B. Fix: **pub/sub** (Redis, Kafka, NATS): A publishes to `user:bob`, B is subscribed and pushes down Bob's socket.
- Keep socket servers dumb, scale out; load balancer must support Upgrade + long idle timeouts.
- Deploys drop every socket on a server → drain gradually, clients reconnect with jitter.
- Trap: sticky sessions only route reconnects to the same server; they don't deliver cross-server messages.

### S6 · E14 · Presence
- Online/offline from connections + heartbeats + **TTL** (`SET presence:riya online EX 60`, renewed by each heartbeat).
- Count connections, not users (laptop closed, phone open = online). Debounce offline to avoid flapping.
- Fan-out: only to users currently viewing; throttle "typing…" (~1 event / 3 s, auto-expires).
- Trap: don't store presence in the main database → in-memory store with TTLs.

### S6 · E15 · IQ: staying alive
- Laptop sleeps, "online" for hours (half-open → heartbeats + TTL) · restart crash loop (herd → backoff + jitter, drain) · own message twice (lost ack → client UUID, dedup) · cross-server delivery (pub/sub, not sticky sessions).

### S6 · E16 · Edit conflicts
- See it: Google Docs with a friend: coloured named cursors in the same sentence.
- Whole-document saves = **last save wins** → lost words. Send **operations** (`insert 'h' @1`) instead.
- Positions shift: "cat" + insert h@1 → "chat"; concurrent delete @2 applied blindly → "cht". Adjusted to delete @3 → "cha".
- Forms: optimistic concurrency → `PUT` with `If-Match: <etag>` → `412` = conflict, merge or ask.
- Trap: locking works and users hate it (forgotten tab blocks everyone). Locks for forms/tickets, not live text.

### S6 · E17 · OT vs CRDT
- **OT**: central server orders ops and transforms late ones against earlier ones. Lean docs, needs a server.
- **CRDT**: every character gets a permanent unique id; inserts reference ids; merges in any order, peer-to-peer and offline. Costs metadata + tombstones.
- See it: Google Docs offline mode → edit → reconnect → merged.
- Trap: don't write your own. Use **Yjs** or **Automerge**; spend time on presence, cursors, undo.

### S6 · E18 · IQ: collaboration
- Typing for 200 (throttle ~3 s, viewers only, auto-expire, not in DB) · profile form lost updates (ETag + If-Match → 412 → merge) · "cat" puzzle ("cha": delete @2 → @3) · offline notes app with no server (CRDT library).

### S6 · E19 · Finale: one chat app
- Transports: WebSocket for chat, SSE for notifications, WebRTC for calls (socket = signaling), polling for the admin dashboard.
- Send: client UUID + outbox → optimistic bubble → server seq + ack → tick; retries deduped.
- Survive: heartbeats 25 s → backoff + jitter → resync since last seq → flush outbox.
- Scale: dumb socket servers + pub/sub; presence with TTL to viewers only; typing throttled. Shared notes: CRDT library.
- Next: Season 7 · Caching.
