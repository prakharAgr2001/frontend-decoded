# Frontend Decoded · Season 5 cheat sheets (DM these for "Comment NOTES")

## E01 · REST
- Everything is a **resource** with its own URL (`/users/42`, `/posts/7/comments`). Act on it with verbs.
- GET read · POST create · PUT replace whole · PATCH change some fields · DELETE remove. Status: 200 OK · 201 Created · 404 Not Found.
- `fetch` does **not** throw on 404/500 → always check `res.ok`. Try: open `api.github.com/users/torvalds` in a tab.
- Trap: PUT vs POST is about **idempotency** — 5× PUT = one user, 5× POST = maybe 5 orders.

## E02 · GraphQL
- One endpoint (`POST /graphql`); the query is shaped like the answer; the response mirrors it. A schema defines types + fields.
- Fixes over-fetching (too much per call) and under-fetching (too many calls).
- Costs: one URL + POST → no free HTTP/CDN caching; deeply nested queries can be very expensive (add depth/complexity limits).
- See it: instagram.com → Network → filter `graphql`. Trap: errors often arrive as **200 OK** with an `errors` array → check it.

## E03 · REST vs GraphQL vs tRPC
- REST: many clients, public APIs, simplest caching. GraphQL: many screens picking their own fields. tRPC: one TypeScript team owns client + server (monorepo), end-to-end types, no schema/codegen.
- In the wild: GitHub (REST + GraphQL), Shopify Storefront (GraphQL), T3-stack apps (tRPC).
- Trap: GraphQL is not "faster" — fewer round trips, but careless queries are slow and you lose easy caching. Choose by clients + teams.

## E04 · Backend for Frontend (BFF)
- A small server owned by the frontend team: app makes **one call**; BFF fans out to services (in parallel, close to them), trims fields, returns screen-shaped data.
- Usually one BFF per experience (mobile vs web). Bonus: keeps tokens on the server, browser gets an `httpOnly` cookie.
- Trap: no business rules (pricing etc.) in the BFF — they get copied per BFF and drift. BFF = shaping only.

## E05 · IQ: API design
- Idempotent: GET, PUT, DELETE (POST no, PATCH not guaranteed) → matters for retries; POST needs an `Idempotency-Key`.
- GraphQL N+1 (1 query for posts + 1 per author) → batch with **DataLoader**.
- Mobile screen needing 4 services → BFF. When not GraphQL: CDN caching critical, simple CRUD, one TS team (tRPC).

## E06 · The offset bug
- `?limit=10&offset=10` → `LIMIT 10 OFFSET 10`. New item on top shifts rows → **duplicates**; deletes shift up → **skipped** items.
- Deep offsets are slow: DB still reads and discards every skipped row.
- Trap: offset is fine for rarely-changing data and jump-to-page UIs (admin tables, search results). It breaks on fast-changing feeds.

## E07 · Cursor pagination
- "10 items older than this one": response has `items` + opaque `nextCursor`; client sends `?after=<cursor>`; `null` = end.
- Server: `WHERE created_at < :cursor ORDER BY created_at DESC LIMIT 10` — with an index, page 1000 ≈ page 1.
- See it: `reddit.com/r/javascript.json` → `"after": "t3_…"`.
- Trap: ties on the sort key skip rows → sort by `(created_at, id)` and put both in the cursor. Cost: no jump to page 50.

## E08 · Infinite scroll vs pages
- Infinite: great for browsing on phones; footer unreachable, back button loses place, memory grows. Pages: hunting, shareable "page 3" URL, crawlable. Middle: **Load more**.
- Build: `IntersectionObserver` on a sentinel with `rootMargin: '600px'`; long lists → virtualization (S3E25).
- Trap: back button → top of feed. Keep loaded pages + scroll position (query cache or URL) and restore; don't refetch from page 1.

## E09 · IQ: pagination
- Duplicates on page 2 = offset + inserts → cursor. Missing items with timestamp cursor = ties → `(created_at, id)`.
- Jump to page 50 → offset (cap the depth). Infinite scroll without scroll listeners → IntersectionObserver + rootMargin (+ virtualization).

## E10 · Waterfalls
- Request 2 waits for request 1 → staircase in the Network waterfall; each step costs a round trip (~100–300 ms on mobile).
- React: parent fetches in an effect → renders child → child fetches = **fetch-on-render**. Fix: start early (route loader, hoist, prefetch) = fetch-then-render.
- Trap: true dependency (needs user id) → move the join to the server (one endpoint / BFF) so it happens next to the DB.

## E11 · Parallel requests
- Independent requests: start all, then `await Promise.all([...])` → total ≈ slowest, not the sum. HTTP/2 multiplexes; HTTP/1.1 ≈ 6 connections per host.
- `Promise.all` rejects on the first failure (good results lost). `Promise.allSettled` → `{status, value | reason}` for each.
- Trap: `await a(); await b(); await c();` is sequential. Create the promises first, then await them together.

## E12 · Race conditions
- Responses arrive in **network order**, not request order → an old, slow response can overwrite a newer one.
- React fix: `let ignore = false; … if (!ignore) setX(d); return () => { ignore = true; }`.
- Trap: debounce doesn't fix races (S3E23) — ignore or cancel stale requests; React Query keys data by query.

## E13 · AbortController
- `const c = new AbortController(); fetch(url, { signal: c.signal }); c.abort();` → really stops the request.
- In effects: abort in the cleanup; ignore `AbortError` (a cancel isn't a failure). `AbortSignal.timeout(5000)` for timeouts.
- See it: Network shows aborted requests as **(canceled)**. Trap: abort doesn't undo a POST already on the server → idempotency key + status check.

## E14 · Retries + backoff
- Exponential backoff: 1 s, 2 s, 4 s, 8 s… capped. Add **jitter** (random delay) to avoid the thundering herd.
- Retry network errors, timeouts/408, 429 (after Retry-After), 5xx like 503. Don't retry 400/401/404.
- React Query: queries retry 3× with `min(1000·2^n, 30000)` by default; mutations retry 0×. Trap: retry a POST only with an idempotency key.

## E15 · Deduplication
- Several components ask for the same thing → share the **in-flight promise** (Map of key → promise, delete on settle).
- React Query dedups by query key. Dedup ≠ cache: dedup shares a request in flight; cache keeps the answer afterwards.
- Trap: double fetch in dev = React **StrictMode** (mount → unmount → mount). Production fetches once.

## E16 · 429 Too Many Requests
- Rate limits: N requests per user / IP / key per window. Token bucket: each request spends a token; tokens refill steadily.
- See it: `api.github.com` headers `x-ratelimit-limit: 60`, `x-ratelimit-remaining`, `x-ratelimit-reset` (unauthenticated).
- On 429: read `Retry-After` and wait. Be a good client: debounce, dedupe, cache.
- Trap: per-IP limits block whole offices behind one NAT → limit per user / API key.

## E17 · Skeleton screens
- Skeletons show layout before data → feels faster; must **match** the real layout or you get CLS (S3E04).
- Don't flash: show only if loading takes > ~200 ms. Skeleton on first load (`isPending`); on refetch keep old data (`isFetching` → small spinner).
- See it: YouTube with Slow 4G. Trap: actions (saving) → spinner on the button; skeletons are for content.

## E18 · Partial failure
- An error thrown during render with no boundary unmounts the whole tree. Wrap each widget in an **ErrorBoundary** with fallback + retry.
- Data: `Promise.allSettled`. Decide what's critical (price → error page) vs optional (recommendations → hide).
- Trap: boundaries don't catch event-handler or async errors → put the error in state and throw during render, or `throwOnError` in your data library.

## E19 · Suspense boundaries
- A suspending component shows the nearest `<Suspense fallback>` until everything inside is ready. Streaming (S2E13) sends the shell then each boundary; selective hydration (S2E11).
- One boundary = waits for the slowest; one per component = popcorn + jumps. Group: critical first, own boundary for heavy parts, below-the-fold together.
- Pair each Suspense boundary with an ErrorBoundary. Trap: `useEffect` fetching never suspends → use `use(promise)`, a framework loader, or `useSuspenseQuery`.

## E20 · IQ: async edge cases
- all vs allSettled · search race (abort / ignore stale, debounce, key by query) · POST timeout (idempotency key, status check, backoff + jitter) · one big spinner (split Suspense boundaries, skeletons, streaming).

## E21 · Finale: one search page
- REST + BFF → cursor pagination + infinite scroll → debounce + AbortController (no races) → parallel, no waterfalls → retries/jitter, dedup, Retry-After → matching skeletons, isolated failures, grouped Suspense.
- Next: Season 6 · Real-time (polling → SSE → WebSockets → CRDTs).
