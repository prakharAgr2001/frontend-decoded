# Season 5 · Instagram captions (Data fetching & APIs · 1 per day, posted automatically by the daily workflow)

Common hashtags are added automatically by `publish/build_queue.py`.

| # | File |
|---|---|
| E01 | S5E01_Rest.mp4 |
| E02 | S5E02_Graphql.mp4 |
| E03 | S5E03_Rest_Vs_Graphql_Vs_Trpc.mp4 |
| E04 | S5E04_Backend_For_Frontend.mp4 |
| E05 | S5E05_Iq_Api_Design.mp4 |
| E06 | S5E06_The_Offset_Bug.mp4 |
| E07 | S5E07_Cursor_Pagination.mp4 |
| E08 | S5E08_Infinite_Scroll_Vs_Pages.mp4 |
| E09 | S5E09_Iq_Pagination.mp4 |
| E10 | S5E10_Waterfalls.mp4 |
| E11 | S5E11_Parallel_Requests.mp4 |
| E12 | S5E12_Race_Conditions.mp4 |
| E13 | S5E13_Abortcontroller.mp4 |
| E14 | S5E14_Retries_Backoff.mp4 |
| E15 | S5E15_Deduplication.mp4 |
| E16 | S5E16_429_Slow_Down.mp4 |
| E17 | S5E17_Skeleton_Screens.mp4 |
| E18 | S5E18_Partial_Failure.mp4 |
| E19 | S5E19_Suspense_Boundaries.mp4 |
| E20 | S5E20_Iq_Async_Edge_Cases.mp4 |
| E21 | S5E21_Finale_One_Search_Page.mp4 |

---

**E01 · REST**
Open any app's Network tab. Almost every row speaks the same language 📡
Season 5 of Frontend Decoded: data fetching & APIs. First up, REST: one URL per resource, five verbs, and why fetch doesn't throw on a 404.
Interview trap: PUT vs POST isn't create vs update. It's idempotency.
💬 Comment NOTES for the cheat sheet.

**E02 · GraphQL**
Your profile page makes 3 requests and downloads 40 fields it never shows 🥪
GraphQL lets the client ask for exactly the shape it needs, in one request to one endpoint.
Trap: a GraphQL response can be 200 OK and still have failed. Check the errors array.
💬 Comment NOTES for the cheat sheet.

**E03 · REST vs GraphQL vs tRPC**
A public API, a 40-screen mobile app, and a 2-dev TypeScript repo should NOT pick the same API style 🤔
Fixed menu, order form, or shouting to your sibling: when to use each.
Trap: GraphQL isn't "faster" than REST.
💬 Comment NOTES for the cheat sheet.

**E04 · Backend for Frontend**
Your home screen needs 5 services. Should the phone really make 5 calls on a patchy network? ✈️
A BFF is a small server, owned by the frontend team, that turns 5 calls into 1 screen-shaped response.
Trap: never put pricing rules in it.
💬 Comment NOTES for the cheat sheet.

**E05 · IQ: API design**
4 API design questions they actually ask in frontend interviews 🎯
Idempotency, the GraphQL N+1 problem, BFFs, and when NOT to pick GraphQL. Pause and answer before each reveal.
Tell me your score below 👇
💬 Comment NOTES for the cheat sheet.

**E06 · The offset bug**
You load page 2 of a feed, and the first post is the one you just saw. Nobody wrote a bug 🐛
Offset pagination breaks the moment someone posts while you scroll. And deep pages get slower and slower.
💬 Comment NOTES for the cheat sheet.

**E07 · Cursor pagination**
Instead of "skip 10", ask for "10 posts older than this one" 🔖
Cursor pagination: no duplicates, and page 1000 is as fast as page 1. See it live in any Reddit .json URL.
Trap: two posts with the same timestamp.
💬 Comment NOTES for the cheat sheet.

**E08 · Infinite scroll vs pages**
Instagram scrolls forever. Amazon still shows page numbers. Both are right 🍣📖
When infinite scroll wins, when pages win, how to build it with one IntersectionObserver, and the back-button trap.
💬 Comment NOTES for the cheat sheet.

**E09 · IQ: pagination**
4 pagination questions that trip up even senior frontend devs 🎯
Duplicates, missing posts, jump-to-page-50, and infinite scroll without a scroll listener.
Tell me your score below 👇
💬 Comment NOTES for the cheat sheet.

**E10 · Waterfalls**
Every request is fast. The page still takes 3 seconds. Why? 🌊
Request waterfalls: when each fetch waits for the one before it. Spot the staircase in DevTools and fix fetch-on-render.
💬 Comment NOTES for the cheat sheet.

**E11 · Parallel requests**
3 independent requests. Why are you waiting for one before starting the next? 🍜
Promise.all makes total time = the slowest request. Plus its sharp edge, and the method most people forget.
Trap: three awaits on three lines are NOT parallel.
💬 Comment NOTES for the cheat sheet.

**E12 · Race conditions**
You click Riya, then Arjun. The header says Arjun, but the posts are Riya's 😬
Responses arrive in network order, not the order you asked. Here's the 4-line fix in React.
Trap: debounce does NOT fix this.
💬 Comment NOTES for the cheat sheet.

**E13 · AbortController**
Ignoring a stale response isn't enough. The request is still downloading in the background 🛑
AbortController cancels it for real. Watch the "(canceled)" rows in DevTools.
Trap: aborting a payment doesn't un-charge the card.
💬 Comment NOTES for the cheat sheet.

**E14 · Retries + backoff**
Your server blinks for 1 second. 10,000 phones retry instantly, and now it's an outage 💥
Exponential backoff + jitter: how to try again politely, and what you should never retry.
💬 Comment NOTES for the cheat sheet.

**E15 · Deduplication**
Your Network tab shows /api/me three times, at the same millisecond 🍕
Request deduplication: one request, shared by every component that needs it.
Trap: why your effect fetches twice in development (it's not a bug).
💬 Comment NOTES for the cheat sheet.

**E16 · 429: Slow down**
One user opens 10 tabs. Every request comes back 429 Too Many Requests 🚦
Rate limits, the token bucket, GitHub's live rate-limit headers, and why you should always read Retry-After.
💬 Comment NOTES for the cheat sheet.

**E17 · Skeleton screens**
Two apps load in exactly 1.5 seconds. Users swear one is faster 🦴
Why skeletons beat spinners, how they cause layout shift, and when NOT to use them.
💬 Comment NOTES for the cheat sheet.

**E18 · Partial failure**
One widget's API goes down, and your whole dashboard turns into a white screen ⚡
Error boundaries, Promise.allSettled, and deciding what's critical.
Trap: why your error boundary doesn't catch a failed fetch.
💬 Comment NOTES for the cheat sheet.

**E19 · Suspense boundaries**
One giant spinner, or 5 pieces popping in like popcorn? Neither 🍿
Where to put Suspense boundaries so the page loads in sensible groups.
Trap: why your Suspense fallback never shows.
💬 Comment NOTES for the cheat sheet.

**E20 · IQ: async edge cases**
4 async questions that separate juniors from seniors in frontend interviews 🎯
all vs allSettled, search races, retrying a checkout POST, and the one-big-spinner page.
Tell me your score below 👇
💬 Comment NOTES for the cheat sheet.

**E21 · Finale: one search page**
Season 5 finale: one food search page, and every data-fetching fix from this season 🔍
REST + BFF, cursors, aborts, parallel loads, retries, dedup, skeletons and Suspense, all in one reel.
💬 Comment NOTES for the full season cheat sheet.
