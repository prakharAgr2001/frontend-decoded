# Season 3 · Instagram captions (1 per day, 7:00 PM IST, posted by the daily Action after Season 2)

Common hashtags (added automatically by publish/build_queue.py):
#techexplained #frontend #webdevelopment #javascript #softwareengineer #systemdesign #codinginterview #webdev #programming #techreels

| # | File |
|---|---|
| E01 | S3E01_100_Ms_Money.mp4 |
| E02 | S3E02_Core_Web_Vitals.mp4 |
| E03 | S3E03_Lcp.mp4 |
| E04 | S3E04_Cls.mp4 |
| E05 | S3E05_Inp.mp4 |
| E06 | S3E06_Ttfb_Fcp_Tbt.mp4 |
| E07 | S3E07_Lab_Vs_Field.mp4 |
| E08 | S3E08_Iq_Metrics.mp4 |
| E09 | S3E09_Critical_Rendering_Path.mp4 |
| E10 | S3E10_Async_Vs_Defer.mp4 |
| E11 | S3E11_Resource_Hints.mp4 |
| E12 | S3E12_Code_Splitting.mp4 |
| E13 | S3E13_Lazy_Routes.mp4 |
| E14 | S3E14_Tree_Shaking.mp4 |
| E15 | S3E15_Bundle_Diet.mp4 |
| E16 | S3E16_Minify_Brotli.mp4 |
| E17 | S3E17_Iq_Loading.mp4 |
| E18 | S3E18_Responsive_Images.mp4 |
| E19 | S3E19_Lcp_Image_Priority.mp4 |
| E20 | S3E20_Web_Fonts.mp4 |
| E21 | S3E21_Third_Party_Cost.mp4 |
| E22 | S3E22_Iq_Assets.mp4 |
| E23 | S3E23_Debounce.mp4 |
| E24 | S3E24_Throttle.mp4 |
| E25 | S3E25_Virtualization.mp4 |
| E26 | S3E26_Web_Workers.mp4 |
| E27 | S3E27_Why_React_Re_Renders.mp4 |
| E28 | S3E28_Memo_Myths.mp4 |
| E29 | S3E29_Usetransition_Compiler.mp4 |
| E30 | S3E30_Chunking_Long_Tasks.mp4 |
| E31 | S3E31_Performance_Budgets.mp4 |
| E32 | S3E32_Iq_Runtime.mp4 |
| E33 | S3E33_Finale_Made_Fast.mp4 |

---

**E01 · 100 ms = money**
A tenth of a second. Barely a blink. And it shows up in your sales numbers ⏱️
Why speed matters, how fast feels instant, and the interview trap: averages hide your slowest users. Measure p75.
💬 Comment NOTES for the cheat sheet.

**E02 · Core Web Vitals**
Google grades your site on three numbers from real Chrome users 📊
LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, judged at the 75th percentile. And what happened to FID.
💬 Comment NOTES for the cheat sheet.

**E03 · LCP**
The page isn't 'loaded' until the big photo and headline show up 📰
Largest Contentful Paint, its 4 parts, how to see it in DevTools, and why lazy-loading the hero makes it worse.
💬 Comment NOTES for the cheat sheet.

**E04 · CLS**
You go to tap Cancel, an ad loads, and you hit Buy instead 😬
Cumulative Layout Shift: how it's scored, the usual culprits, and the fix: reserve space before content arrives.
💬 Comment NOTES for the cheat sheet.

**E05 · INP**
You tap Add to cart. Nothing. You tap again. Now there are two 🛒
Interaction to Next Paint: input delay, processing, presentation. Paint feedback first, then do the heavy work.
💬 Comment NOTES for the cheat sheet.

**E06 · TTFB · FCP · TBT**
When the vitals are bad, these three tell you why 🎬
First byte, first paint, and Total Blocking Time, Lighthouse's stand-in for INP. Plus a TBT puzzle to solve.
💬 Comment NOTES for the cheat sheet.

**E07 · Lab vs field**
Lighthouse says 100. Search Console says failing. Both are right 🤔
One simulated run vs 28 days of real users. Why they disagree, how to add RUM, and why fixes take weeks to show.
💬 Comment NOTES for the cheat sheet.

**E08 · IQ: measuring performance**
Four interview questions on web vitals. Pause and answer before the reveal 🧠
Thresholds, lab vs field, a slow LCP with a fast image, and a banner that wrecks CLS. Comment your score.
💬 Comment NOTES for the cheat sheet.

**E09 · Critical rendering path**
The server answered in 100 ms. So why is the screen white for 2 seconds? ⬜
CSS blocks rendering, plain scripts block parsing. Inline critical CSS, defer the rest. And the CSS trap most people miss.
💬 Comment NOTES for the cheat sheet.

**E10 · async vs defer**
Two words on a script tag. Mix them up and your app breaks 💥
async runs on arrival in any order; defer runs after parsing, in order. Which to use, and why modules are deferred by default.
💬 Comment NOTES for the cheat sheet.

**E11 · Resource hints**
Tell the browser what's coming before it asks 📞
preconnect, dns-prefetch, preload, prefetch: what each does, how to see priorities, and why preloading everything backfires.
💬 Comment NOTES for the cheat sheet.

**E12 · Code splitting**
You opened a blog post and downloaded the admin dashboard's code 🧳
Dynamic import(), where to split, how the Coverage tab exposes unused JS, and the tiny-chunk waterfall trap.
💬 Comment NOTES for the cheat sheet.

**E13 · Lazy routes**
50 pages in the app. The visitor only needs one 🏨
React.lazy + Suspense, prefetch on hover, never lazy-load the landing route, and the ChunkLoadError after every deploy.
💬 Comment NOTES for the cheat sheet.

**E14 · Tree shaking**
You imported one function and shipped the whole library 🌳
How bundlers drop dead code, why it needs ES modules, sideEffects in package.json, and the barrel-file trap.
💬 Comment NOTES for the cheat sheet.

**E15 · Bundle diet**
100 KB of JavaScript costs far more than 100 KB of image 🎒
Measure, swap heavy libraries, drop polyfills, dedupe. And why 'gzipped size' isn't the real cost.
💬 Comment NOTES for the cheat sheet.

**E16 · Minify + Brotli**
400 KB on your laptop, ~60 KB over the wire. Same file 🗜️
Minification, gzip vs Brotli, Accept-Encoding vs Content-Encoding, and why compressing JPEGs is wasted CPU.
💬 Comment NOTES for the cheat sheet.

**E17 · IQ: loading + bundles**
Four interview questions on loading and bundles. Pause, answer, then check 🧠
Script timing, resource hints, why tree shaking keeps code, and how you'd cut a 1.5 MB bundle. Comment your score.
💬 Comment NOTES for the cheat sheet.

**E18 · Responsive images**
Your user downloaded a poster to look at a stamp 🖼️
srcset + sizes, the math the browser does, AVIF/WebP with <picture>, and what happens when you forget sizes.
💬 Comment NOTES for the cheat sheet.

**E19 · LCP image priority**
The hero image is small and compressed. It still shows up last 🛫
fetchpriority="high", the preload scanner, and why marking every image high priority means nothing is.
💬 Comment NOTES for the cheat sheet.

**E20 · Web fonts**
The layout's there but the text is invisible, waiting for a font 🔤
FOIT vs FOUT, font-display block/swap/optional, matched fallbacks to stop layout shift, and how to load fonts sooner.
💬 Comment NOTES for the cheat sheet.

**E21 · Third-party cost**
Your code is lean. The chat widget, analytics and tag manager aren't 🎉
They run on your main thread. Measure with request blocking, use facades, delay tags. And why async isn't free.
💬 Comment NOTES for the cheat sheet.

**E22 · IQ: images, fonts, third parties**
Four interview questions on assets. Pause and answer each one 🧠
Why srcset needs sizes, a slow hero LCP, invisible text vs font shifts, and adding a chat widget safely.
💬 Comment NOTES for the cheat sheet.

**E23 · Debounce**
13 keystrokes, 13 requests, 12 of them wasted 🔍
Run once after the user stops typing: the closure, where to use it, and why debounce alone doesn't fix race conditions.
💬 Comment NOTES for the cheat sheet.

**E24 · Throttle**
Your scroll handler fires dozens of times a second 🚇
At most once per interval. Debounce vs throttle, requestAnimationFrame, IntersectionObserver, and the lost final event.
💬 Comment NOTES for the cheat sheet.

**E25 · Virtualization**
10,000 rows, 100,000+ DOM nodes, and every scroll stutters 🚆
Render only what's visible, content-visibility: auto, and what breaks: Ctrl+F, screen readers, variable heights.
💬 Comment NOTES for the cheat sheet.

**E26 · Web Workers**
Parsing a big CSV and even the spinner freezes 👩‍🍳
A second thread for heavy work, no DOM access, postMessage both ways. And why postMessage isn't free.
💬 Comment NOTES for the cheat sheet.

**E27 · Why React re-renders**
You typed one letter and the whole page re-rendered ⚛️
State, context, or the parent re-rendering. The props myth, render vs commit, and moving state down.
💬 Comment NOTES for the cheat sheet.

**E28 · Memo myths**
Wrapped everything in useMemo and useCallback. Got slower 🧊
What React.memo, useMemo and useCallback really cost, how inline props break memo, and when to memoize.
💬 Comment NOTES for the cheat sheet.

**E29 · useTransition + React Compiler**
Every keystroke freezes the input while the list re-renders ⌨️
Urgent vs non-urgent updates, useDeferredValue, and the React Compiler doing your memoization for you.
💬 Comment NOTES for the cheat sheet.

**E30 · Chunking long tasks**
Split long tasks, yes. But how big, and how do you hand control back? 🌱
Slice by time, scheduler.yield vs setTimeout, postTask priorities, and why await Promise.resolve() doesn't yield.
💬 Comment NOTES for the cheat sheet.

**E31 · Performance budgets**
Fast at launch, twice as slow a year later. No single change did it 📉
Budgets for KB and timings, enforced in CI with Lighthouse CI or size-limit, and how to pick the numbers.
💬 Comment NOTES for the cheat sheet.

**E32 · IQ: runtime performance**
Four interview questions on runtime performance. Pause before each reveal 🧠
Debounce vs throttle, a 10k-row table, wasted re-renders, and a 400 ms click handler. Comment your score.
💬 Comment NOTES for the cheat sheet.

**E33 · Finale: one product page, made fast**
Season 3 finale: one slow product page, every fix from this season ⚡
Measure, loading, bundle, hero image, layout shifts, third parties, interactions, budgets. All three vitals pass. Next: state management.
💬 Comment NOTES for the cheat sheet.
