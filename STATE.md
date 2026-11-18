# State

- **Season 1 (How the browser really works): complete.** S1E01–S1E25 specs in `episodes/`, all rendered and delivered in chat.
- **Next:** Season 2 · Rendering strategies (S2E01–S2E21, see `REGISTRY.md`).
- Recurring analogies used so far (don't reuse for a different concept): parcel journey (URL→pixels), phone contacts (DNS), phone call (TCP),
  postcard (HTTP), multi-lane road (HTTP versions), kirana store (CDN), recipe (DOM/CSSOM), building a house (pipeline), moving wall vs sliding picture (reflow),
  tailor (thrashing), sticker (compositing), one-chef kitchen (main thread), plates (call stack), VIP club line (microtasks), bank counter (long tasks),
  stone in a pond (event phases), receptionist (delegation).
- Pending callbacks for Season 2: hydration ↔ S1E14 main thread; SSR TTFB ↔ S1E01; streaming ↔ S1E05.
- DM cheat sheets for the "Comment NOTES" CTA: `notes/season1.md`.

## Instagram publishing (S1)
- Page: @tech.explained.dev. Secrets `IG_TOKEN` (system-user token, no expiry) + `IG_USER_ID` set in GitHub.
- `publish/make_covers.py` → `covers/S1Exx.jpg`; `publish/prep_videos.py` → `videos/S1Exx.mp4` (crf 27; cover sent as cover_url from public repo).
- `publish/build_queue.py` → `publish/queue.json` (captions from notes/season1_captions.md, rebranded).
- `.github/workflows/post-reel.yml`: daily 19:00 IST posts next unposted reel; manual run supports episode/count/dry_run.
- `.github/workflows/notes-bot.yml` (every 10 min): "NOTES" comment → DM with that reel's cheat sheet as plain text (from `cheatsheets/SxEyy.md`, no link) via InstantDM API (secret `INSTANTDM_KEY`, 1 credit/DM).
