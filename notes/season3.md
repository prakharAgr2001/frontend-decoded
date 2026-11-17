# Frontend Decoded · Season 3 cheat sheets (DM these for "Comment NOTES")

## E01 · 100 ms = money
- Google research: 53% of mobile visits are abandoned if a page takes > 3 s. Often-quoted Amazon finding: +100 ms ≈ −1% sales.
- Response-time limits (Nielsen): 0.1 s feels instant · 1 s keeps flow · 10 s loses attention.
- Two jobs: **be fast** (send less, do less on the main thread) and **feel fast** (useful content early, instant feedback).
- Try: DevTools → Network → throttling "Slow 4G" → reload. Trap: averages hide slow users → report **p75**.

## E02 · Core Web Vitals
- **LCP** (loading) ≤ 2.5 s · **INP** (responsiveness) ≤ 200 ms · **CLS** (visual stability) ≤ 0.1.
- Graded at the **75th percentile** of real Chrome visits (CrUX), mobile and desktop separately.
- See it: PageSpeed Insights → "Discover what your real users are experiencing". Trap: INP replaced FID in March 2024.

## E03 · LCP
- Time until the largest image / text block in the viewport renders. Candidates: `<img>`, video poster, CSS background image, text blocks.
- 4 parts: TTFB → resource load delay → load duration → render delay. Usually the *delay* (image found late) is the problem.
- See it: Performance panel → LCP marker + LCP breakdown insight. Trap: `loading="lazy"` on the hero makes LCP worse.

## E04 · CLS
- Sum of unexpected shifts; each = impact × distance; grouped into bursts (session windows); your worst burst = CLS.
- Culprits: images without width/height, ads/embeds without reserved space, injected banners, font swaps. Fix: reserve space (`width/height`, `aspect-ratio`, `min-height`).
- See it: Rendering → Layout Shift Regions. Trap: shifts within 500 ms of a tap/keypress are excluded; `transform` animations never shift layout.

## E05 · INP
- Input → next paint. Parts: input delay (main thread busy) + processing (handlers) + presentation delay (style/layout/paint).
- Roughly your *worst* interaction of the visit, not an average. Fix: feedback first, `await scheduler.yield()`, heavy work after; break long tasks.
- See it: Performance panel live metrics → interactions list. Trap: scroll and hover are not counted — only click, tap, key press.

## E06 · TTFB · FCP · TBT
- TTFB (first byte, good ≤ 0.8 s) → FCP (first anything, ≤ 1.8 s) → LCP. Slow TTFB = server, distance, redirects → CDN, caching.
- **TBT** = sum over long tasks of (duration − 50 ms) between FCP and interactive. Lab stand-in for INP; Lighthouse weight 30% (largest).
- Puzzle: tasks 70, 140, 40 ms → TBT = 20 + 90 + 0 = **110 ms**.

## E07 · Lab vs field
- Lab (Lighthouse): one run, simulated mid-range phone, throttled, clean browser → repeatable, for debugging.
- Field (CrUX / RUM): real users, 28 days, p75. They disagree: lab has no INP, only first screen, one device.
- RUM: `import { onLCP, onINP, onCLS } from 'web-vitals'` + `navigator.sendBeacon`. Trap: CrUX is a 28-day rolling window → fixes fade in over weeks.

## E08 · IQ: measuring performance
- CWV + thresholds at p75 · Lighthouse 98 but poor INP (no interactions, TBT is a proxy, real devices, 28 days) · slow LCP with fast image download (TTFB, load delay → in HTML + preload/fetchpriority, render delay) · banner CLS (reserve, overlay, transform).

## E09 · Critical rendering path
- HTML → DOM, CSS → CSSOM → render tree → first pixels. CSS is **render-blocking**; plain `<script>` is **parser-blocking**.
- Shrink it: inline critical CSS, load the rest non-blocking, `media="print"` for non-critical sheets, `defer` scripts.
- See it: Lighthouse "Render blocking requests"; Performance panel request details "Render blocking". Trap: a script after a stylesheet waits for that CSS → CSS can block parsing too.

## E10 · async vs defer
- plain: stop parsing, fetch, run. **async**: fetch in parallel, run on arrival, no order. **defer**: fetch in parallel, run after parsing, in document order, before DOMContentLoaded.
- defer → app code; async → independent scripts (analytics). `type="module"` is deferred by default.
- Trap: async scripts that depend on each other break randomly; `defer` does nothing on inline scripts.

## E11 · Resource hints
- `preconnect` (DNS+TCP+TLS early) · `dns-prefetch` (DNS only) · `preload` (this page, late-discovered, high priority, needs `as`) · `prefetch` (next page, lowest priority).
- See it: Network → Priority column. Trap: preloading everything steals bandwidth; Chrome warns about unused preloads; font preload needs `crossorigin` or it downloads twice.

## E12 · Code splitting
- Dynamic `import()` → separate chunk loaded on demand. Split by route, heavy feature, below the fold; shared libs in a vendor chunk.
- See it: DevTools → Coverage (red = downloaded, never ran). Trap: too many tiny chunks → request waterfalls.

## E13 · Lazy routes
- `const Orders = lazy(() => import('./pages/Orders'))` inside `<Suspense fallback>`. Hide the delay: prefetch on hover / in viewport (Next.js `<Link>` does this in production).
- Rules: never lazy-load the landing route; fallbacks must hold layout. Trap: after a deploy, old tabs hit `ChunkLoadError` → keep old chunks, catch + reload.

## E14 · Tree shaking
- Bundler follows imports from the entry, keeps used exports, drops the rest. Needs **ES modules** (static); CommonJS `require` usually can't be shaken.
- Side effects: mark `"sideEffects": false` (or a list) in package.json. `import _ from 'lodash'` ≈ 70 KB vs `import { debounce } from 'lodash-es'`.
- Trap: barrel files (`export * from …`) can pull whole libraries in → import from the file directly.

## E15 · Bundle diet
- 100 KB of JS ≠ 100 KB of image: JS is downloaded, parsed, compiled and executed on the main thread.
- Measure (bundle analyzer), then: moment → date-fns / Intl, drop unneeded polyfills, dedupe versions, check bundlephobia, use the platform (fetch, `<dialog>`).
- Trap: "200 KB gzipped" — the browser parses the uncompressed size (~700 KB). Compression saves network, not CPU.

## E16 · Minify + Brotli
- Minify: strip whitespace/comments, rename locals. Compress: gzip, Brotli (≈ 15–20% smaller than gzip on text).
- `accept-encoding: gzip, deflate, br, zstd` → `content-encoding: br`. See it: Network → big request rows show transferred vs real size.
- Trap: don't compress JPEG/PNG/MP4/WOFF2 — already compressed. Compress text: HTML, CSS, JS, JSON, SVG.

## E17 · IQ: loading + bundles
- When scripts run (plain/async/defer/module) · preconnect vs preload vs prefetch · why tree shaking keeps code (CJS, side effects, barrels, dynamic access) · cutting a 1.5 MB bundle (measure → split → replace → minify + Brotli → budget).

## E18 · Responsive images
- `srcset` (files + `w` widths) + `sizes` (display width) → browser picks the smallest sharp file, including DPR. `<picture>` for AVIF/WebP + JPEG fallback and art direction (`media`).
- See it: Elements → hover `<img>`: rendered vs intrinsic size; Lighthouse "Properly size images". Trap: no `sizes` → assumes `100vw` → biggest file.

## E19 · LCP image priority
- Images start Low and are boosted only after layout. `fetchpriority="high"` on the hero (Chrome team test on Google Flights: LCP 2.6 s → 1.9 s).
- Must be discoverable by the preload scanner: plain `<img>` in HTML, or `<link rel="preload" as="image" fetchpriority="high">`. Never lazy, don't wait for client JS.
- Trap: high priority on everything = nothing is high priority.

## E20 · Web fonts
- FOIT (invisible text while loading) vs FOUT (fallback, then swap). `font-display`: block · swap · optional.
- Swap can cause CLS → matched fallback with `size-adjust`, `ascent-override`. Arrive sooner: self-host, preload 1–2 files, woff2, subset.
- IQ: safest for CWV is often `optional` (no invisible text, no late shift) — trade-off: slow first visits may never show the brand font.

## E21 · Third-party cost
- Third-party JS runs on *your* main thread: long tasks (INP), late banners (CLS), extra origins (connections).
- Measure: DevTools request blocking → compare. Tame: facades, delay until interaction, self-host, Partytown (web worker). See it: Performance "3rd parties" insight.
- Trap: `async` only avoids parser blocking; the script still runs on the main thread.

## E22 · IQ: images, fonts, third parties
- Why `sizes` · slow hero LCP checklist (HTML, fetchpriority/preload, not lazy, right size/format/CDN) · no FOIT + no font CLS · adding a chat widget safely (measure, facade, after interaction, reserve space).

## E23 · Debounce
- Run once after the user stops (e.g. 300 ms of quiet). Search boxes, autosave, resize.
- `clearTimeout(timer); timer = setTimeout(() => fn(...args), wait);`
- Trap: debounce doesn't fix race conditions → AbortController or ignore stale responses.

## E24 · Throttle
- At most once per interval, steadily during the storm (scroll progress, drag). Debounce = after silence; throttle = regular.
- Better for visuals: `requestAnimationFrame`; for visibility: `IntersectionObserver`.
- Trap: naive throttle drops the last call → add a trailing call.

## E25 · Virtualization
- Render only visible rows + overscan; a tall spacer keeps the scrollbar right; rows are recycled. Libraries: TanStack Virtual, react-window.
- Lighter option: `content-visibility: auto` + `contain-intrinsic-size` (stays in DOM). See it: Performance monitor → DOM Nodes stays flat.
- Trap: Ctrl+F misses unrendered rows, screen readers, unknown heights → jumpy scrollbar.

## E26 · Web Workers
- JS on another thread; no DOM; talk via `postMessage` / `onmessage`. Good for parsing, image processing, search indexes, crypto, diffing.
- See it: Performance panel shows a separate Worker track.
- Trap: postMessage copies data (structured clone) → transfer `ArrayBuffer`s: `postMessage(buf, [buf])`.

## E27 · Why React re-renders
- State change · context change · **parent re-render** (props changing is *not* the trigger). Render ≠ DOM update (commit applies only real changes).
- Fix structurally: move state down, pass components as children. See it: React DevTools "Highlight updates" + Profiler "Why did this render?".
- IQ: same value via `Object.is` → bail out; a new object with the same contents re-renders.

## E28 · Memo myths
- `React.memo` (shallow props), `useMemo` (value), `useCallback` (function identity). Memo isn't free: storage + comparison every render.
- Inline objects/arrow functions break memo → stabilize with useMemo/useCallback. Memoize on evidence (Profiler ranked view).
- Trap: useMemo is a performance hint, never a correctness guarantee — React may discard the cache.

## E29 · useTransition + React Compiler
- `startTransition(() => setFilter(v))` marks non-urgent updates; renders are interruptible; `isPending` for subtle feedback. `useDeferredValue` when you don't own the setter.
- React Compiler (v1.0, late 2025) auto-memoizes at build time; DevTools shows a "Memo" badge.
- Trap: transitions don't make work faster, only interruptible → still virtualize / do less.

## E30 · Chunking long tasks
- Slice by time (~10 ms), not item count; `await scheduler.yield()` continues near the front of the queue (setTimeout goes to the back).
- `scheduler.postTask(fn, { priority: 'user-blocking' | 'user-visible' | 'background' })`. See it: many small tasks with gaps instead of one red-cornered block.
- Trap: `await Promise.resolve()` is a microtask — it does not yield to rendering or input.

## E31 · Performance budgets
- Agreed limits, e.g. JS ≤ 170 KB compressed, LCP ≤ 2.5 s, TBT ≤ 200 ms. Kinds: quantity, milestone timings, rule-based scores.
- Enforce in CI: Lighthouse CI assertions, size-limit → fail the PR.
- IQ: start from current field data, set slightly better, ratchet down, test on a real mid-range phone.

## E32 · IQ: runtime
- Debounce vs throttle (+ rAF, IntersectionObserver) · 10k-row table (virtualize, content-visibility, paginate, trade-offs) · re-renders (causes, move state down, memo where measured, Compiler) · 400 ms click handler (feedback + yield, chunk, worker, transition).

## E33 · Finale: one product page, made fast
- Measure (CWV, field vs lab) → loading (CDN TTFB, critical CSS, defer, preconnect) → bundle (split, lazy, diet, Brotli) → hero (AVIF srcset, fetchpriority) → shifts (reserve space, font fallback) → third parties (facade, delay) → interactions (feedback first, transition, virtualize, worker, chunking) → budget in CI.
