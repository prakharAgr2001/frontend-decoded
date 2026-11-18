# Season 2 · Instagram captions (1 per day, 7:00 PM IST, posted by the daily Action after Season 1)

Common hashtags (added automatically by publish/build_queue.py):
#techexplained #frontend #webdevelopment #javascript #softwareengineer #systemdesign #codinginterview #webdev #programming #techreels

| # | File |
|---|---|
| E01 | S2E01_White_Screen_First.mp4 |
| E02 | S2E02_Client_Side_Rendering.mp4 |
| E03 | S2E03_Client_Side_Routing.mp4 |
| E04 | S2E04_Server_Side_Rendering.mp4 |
| E05 | S2E05_Static_Site_Generation.mp4 |
| E06 | S2E06_Incremental_Static_Regen.mp4 |
| E07 | S2E07_Iq_Csr_Ssr_Ssg_Isr.mp4 |
| E08 | S2E08_Hydration.mp4 |
| E09 | S2E09_Hydration_Mismatch.mp4 |
| E10 | S2E10_Visible_Not_Clickable.mp4 |
| E11 | S2E11_Selective_Hydration.mp4 |
| E12 | S2E12_Iq_Hydration.mp4 |
| E13 | S2E13_Streaming_Ssr.mp4 |
| E14 | S2E14_Server_Components.mp4 |
| E15 | S2E15_Server_Actions.mp4 |
| E16 | S2E16_Islands_Architecture.mp4 |
| E17 | S2E17_Resumability.mp4 |
| E18 | S2E18_Edge_Rendering.mp4 |
| E19 | S2E19_Case_Study_A_Store.mp4 |
| E20 | S2E20_Iq_Modern_Rendering.mp4 |
| E21 | S2E21_Finale_Three_Sites.mp4 |

---

**E01 · White screen first**
Same phone, same network. One site shows products in a second, the other shows a white screen ⬜
Season 2 of Tech, Explained: rendering strategies. It all comes down to one question: who builds the HTML?
💬 Comment NOTES for the cheat sheet.

**E02 · Client-side rendering**
View Source on a React app and the content isn't there. Just one empty div 🔍
That's CSR: the server sends a shell, your user's phone builds the page. Great for dashboards, risky for link previews.
💬 Comment NOTES for the cheat sheet.

**E03 · Client-side routing**
Click a video on YouTube: the URL changes, the page changes, but there's no new page load 📺
Intercept the click, pushState, fetch JSON, swap the view. Plus the refresh-404 trap every SPA hits.
💬 Comment NOTES for the cheat sheet.

**E04 · Server-side rendering**
View Source on Amazon: titles and prices are already in the HTML, before any JS runs ☕
SSR = a chai stall. Fresh for every customer, but you wait while it's made. Higher TTFB, faster first paint.
💬 Comment NOTES for the cheat sheet.

**E05 · Static site generation**
Why do docs pages load in a blink from anywhere in the world? 🥛
Built once at build time, copied to the CDN, served as is. Perfect until 50,000 prices change every hour.
💬 Comment NOTES for the cheat sheet.

**E06 · Incremental static regeneration**
One price changes. Do you rebuild 50,000 pages? 🍞
ISR: serve the static page, rebuild it in the background after it expires. And the trap: who still sees the old price?
💬 Comment NOTES for the cheat sheet.

**E07 · Interview: CSR · SSR · SSG · ISR**
4 rendering questions interviewers love. Pause before each answer ⏸️
Empty root div, refresh 404s, TTFB vs first paint, and picking a strategy per page.
💬 Comment NOTES for the cheat sheet.

**E08 · Hydration**
The button is on screen. You tap it. Nothing happens 🍜
Server HTML is the noodle cake, JavaScript is the hot water. Hydration is the wait, and it runs on the main thread.
💬 Comment NOTES for the cheat sheet.

**E09 · Hydration mismatch**
"Hydration failed because the server rendered HTML didn't match the client." What it means 🔴
Dates, Math.random, localStorage in render. The fix is useEffect, and the typeof window trick makes it worse.
💬 Comment NOTES for the cheat sheet.

**E10 · Visible, not clickable**
You tap, nothing. Tap again, harder. Still nothing 😤
The uncanny valley: the page looks ready but JS is still loading. FCP vs TTI vs TBT, and why a green Lighthouse score can lie.
💬 Comment NOTES for the cheat sheet.

**E11 · Selective hydration**
Should your Add to cart tap wait for the recommendations carousel to hydrate? 🙋
React 18 hydrates each Suspense boundary on its own, and the part you click jumps the queue.
💬 Comment NOTES for the cheat sheet.

**E12 · Interview: hydration**
4 hydration questions. Answer before the reveal ⏸️
What hydration is, mismatch causes, dead buttons, and how Suspense helps.
💬 Comment NOTES for the cheat sheet.

**E13 · Streaming SSR**
Header instantly, the rest a moment later, with zero fetches from the browser 🍛
Streaming sends HTML in chunks like a thali, dish by dish. Plus why you can't send a 404 after the shell.
💬 Comment NOTES for the cheat sheet.

**E14 · Server components**
Those ?_rsc= requests on nextjs.org aren't HTML or JSON. So what are they? 🧑‍🍳
React Server Components run only on the server and never ship their code. Only the dish leaves the kitchen.
💬 Comment NOTES for the cheat sheet.

**E15 · Server actions**
A form POSTs to your server, and you never wrote an API route 🛎️
'use server' turns a function call into a request. It's still a public endpoint, so check auth inside it.
💬 Comment NOTES for the cheat sheet.

**E16 · Islands architecture**
A sea of static HTML with small islands of JavaScript 🏝️
Only the interactive widgets hydrate, each on its own: client:load, client:visible, client:idle. And the shared-state trap.
💬 Comment NOTES for the cheat sheet.

**E17 · Resumability**
Hydration re-runs your whole app to rediscover what the server already knew. What if the browser just continued? 🎮
Resumability is loading a game save instead of replaying every level.
💬 Comment NOTES for the cheat sheet.

**E18 · Edge rendering**
Your server is in Virginia. Your user is in Bengaluru. That's ~250 ms before the HTML starts cooking 🌍
Edge rendering cooks it next door, unless your database is still across the planet.
💬 Comment NOTES for the cheat sheet.

**E19 · Case study: a store**
Design the rendering for an online store. Most candidates get it wrong in the first sentence 🛒
3 questions per page: SEO? Same for everyone? How often does the data change? One store, four strategies.
💬 Comment NOTES for the cheat sheet.

**E20 · Interview: modern rendering**
4 questions on streaming, server components, server actions and islands ⏸️
Pause, answer, then check the reveal. Tell us your score.
💬 Comment NOTES for the cheat sheet.

**E21 · Finale: three sites**
A blog, Amazon and Gmail: three sites you use every day, three ways to render a page 🏁
21 episodes, one question: who builds the HTML, and when? Next season: web performance.
💬 Comment NOTES for the cheat sheet.
