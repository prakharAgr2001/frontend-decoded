# Tech, Explained · Season 1 cheat sheets

## E01 · URL to pixels
- 5 journeys: **DNS** (name → IP) → **TCP** (connection) → **TLS** (encrypt + verify) → **HTTP** (request) → **render** (HTML → pixels).
- See it: DevTools → Network → first request → Timing (DNS Lookup, Initial connection, SSL, Waiting, Content Download).
- Trap: DNS isn't done every visit — browser, OS and resolver cache it. First load is usually slowest.

## E02 · DNS
- Phonebook of the internet: domain → IP address.
- Resolver walks root → TLD (.com) → authoritative name servers. Answers carry a **TTL**; cached until it expires.
- Try: `nslookup google.com`. Trap: after a server move some users hit the old IP until TTL expires → lower TTL before migrating.

## E03 · TCP handshake
- SYN → SYN-ACK → ACK = 1 round trip before any data (e.g. ~200 ms India ↔ US).
- Keep-alive reuses connections; later requests show 0 ms "Initial connection".
- Trap: TCP guarantees order, so one lost packet blocks everything behind it (head-of-line blocking) → why HTTP/3 exists.

## E04 · HTTPS & the padlock
- HTTPS = HTTP over TLS. 3 promises: **encryption, integrity, authentication**.
- Certificate chain: root CA (trusted by browser) → intermediate → site. TLS 1.3 handshake = 1 round trip (TLS 1.2 = 2).
- Trap: padlock = private connection, **not** a safe site. Phishing sites have valid certs.

## E05 · HTTP/1.1 vs 2 vs 3
- 1.1: one request per connection at a time → ~6 connections per site.
- 2: multiplexing + header compression on ONE TCP connection — but a lost packet stalls all streams.
- 3: QUIC over UDP, independent streams, survives Wi-Fi → mobile switches. Trap: HTTP/2 isn't always faster on lossy networks.

## E06 · CDNs
- Copies of files on edge servers near users; hit = fast, miss = fetch once from origin then cache.
- Headers: `x-cache`, `cf-cache-status`, `age`.
- Trap: users see old assets after deploy → versioned (hashed) file names + purge.

## E08 · DOM & CSSOM
- HTML → DOM tree; CSS → CSSOM tree. CSS blocks rendering; classic `<script>` blocks parsing.
- View Source = what arrived; Elements = live DOM.
- Trap: DOM ≠ HTML (browser fixes markup, JS mutates it).

## E09 · Layout → Paint → Composite
- Render tree (visible nodes) → Layout (size/position) → Paint (pixels) → Composite (GPU stacks layers).
- Performance panel: purple = layout, green = paint.
- Q: `display:none` removes from render tree (no space); `visibility:hidden` keeps the space.

## E10 · Reflow vs repaint
- Geometry (width/height/top) → layout + paint + composite. Color → paint + composite. transform/opacity → composite only.
- Reflow spreads to siblings/parents. DevTools → Rendering → Paint flashing.
- Trap: reading `offsetHeight` right after a style write forces synchronous layout.

## E11 · Layout thrashing
- Read/write/read/write in a loop → a layout per read. Fix: batch all reads, then all writes; schedule writes in `requestAnimationFrame`.
- Shows as "Forced reflow is a likely performance bottleneck" in Performance.
- Q: layout-forcing reads: offsetHeight/Top, clientWidth, scrollTop, getBoundingClientRect().

## E12 · Smooth animation
- Animate `transform`/`opacity` (compositor, GPU layer) not `left/top/width` (layout every frame).
- `will-change: transform` hints a layer — each layer costs GPU memory, don't overuse.
- Check: Rendering → Frame Rendering Stats.

## E14 · One-chef kitchen
- JS runs on one main thread that also does style, layout, paint. A 3 s loop freezes everything.
- Waiting (timers, fetch, events) happens in browser Web APIs; results come back through queues.
- Trap: `setTimeout(fn, 0)` = "as soon as possible", not "now".

## E15 · Call stack & task queue
- `log A; setTimeout(log B, 0); log C` → A, C, B.
- Stack runs sync code; Web APIs hold timers; callbacks wait in the task queue; event loop moves a task when the stack is empty.
- Q: no true 0 ms — deeply nested timers clamp to ≥ 4 ms.

## E16 · Microtasks vs tasks
- Tasks: timers, events. Microtasks: promise callbacks, `queueMicrotask`.
- After each task the loop drains ALL microtasks (incl. new ones), then may render, then next task. `1,timeout 2,promise 3,4` → 1 4 3 2.
- Trap: microtask starvation freezes the page.

## E17 · 16 ms frame budget
- 60 Hz ≈ 16.7 ms per frame (120 Hz ≈ 8.3 ms). Keep your JS ≲ 10 ms.
- `requestAnimationFrame` runs right before paint, once per frame, pauses in background tabs. Use its timestamp (time-based motion).
- `setInterval` drifts against frames.

## E18 · Long tasks
- > 50 ms = long task; blocks input. 100 ms feels instant (50 task + 50 input/paint).
- Fix: chunk work and yield (`await scheduler.yield()` or `setTimeout`).
- Metric: **INP** (Interaction to Next Paint), Core Web Vital since 2024 (replaced FID).

## E20 · Bubbling & capturing
- Phases: capture ↓ → target → bubble ↑. Listeners default to bubble; `{ capture: true }` for capture.
- `stopPropagation` (stop the journey) ≠ `preventDefault` (stop default action).
- `target` = clicked element, `currentTarget` = element whose listener runs. focus/blur/mouseenter/mouseleave don't bubble.

## E21 · Event delegation
- One listener on the parent + `e.target.closest('.row')`.
- Fewer listeners, works for rows added later, no listener leaks. DevTools → Event Listeners → Ancestors.
- Trap: needs bubbling events; a child's `stopPropagation` hides it.

## E22 · Memory leaks
- GC frees what's unreachable from roots; a leak is unneeded but still reachable memory.
- Suspects: listeners not removed, intervals after unmount, ever-growing caches, detached DOM nodes. Use useEffect cleanup, WeakMap.
- Memory panel: compare heap snapshots, filter "Detached". Closures keep captured variables alive.

## E23 · Observers
- IntersectionObserver (lazy load, infinite scroll, autoplay, impressions), ResizeObserver, MutationObserver, PerformanceObserver.
- Better than scroll listeners: browser computes intersections, no forced layout in your code, fires only on threshold crossings.
