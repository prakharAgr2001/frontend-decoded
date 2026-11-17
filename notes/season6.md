# Frontend Decoded · Season 6 cheat sheets (DM these for "Comment NOTES")

## E01 · How did it arrive?
- HTTP is request → response: the server can't speak first. "Real-time" = the server can push the moment something happens.
- See it: WhatsApp Web → DevTools → Network → filter **WS** → click the connection → **Messages**. ↓ red = received, ↑ green = sent.
- Five transports: short polling · long polling · Server-Sent Events · WebSockets · WebRTC.
- Trap: "real-time means WebSockets" → no. Pick by **who talks** and **how often** (a badge can poll; AI answers stream over SSE).

## E02 · Short polling
- Ask on a fixed timer ("anything new?"). Cost = latency (up to one interval) + load (10,000 tabs ÷ 5 s = 2,000 req/s, mostly empty).
- Fine for rare updates where seconds of delay are OK: dashboards, build status, unread badges. Works through every proxy.
- Trap: `setInterval(fetch)` overlaps when the server slows → schedule the next poll with `setTimeout` *after* the response; skip work when `document.hidden`.

## E03 · Long polling
- Server holds the request open until there's news (or ~30 s timeout → empty response), client immediately asks again.
- Near-instant, plain HTTP. Costs: full request + headers per message, one open request per user.
- Trap: messages in the gap between polls → send a cursor (`?since=<last id>`) so the server returns everything after it.

## E04 · Server-Sent Events
- One HTTP response that never ends: `Content-Type: text/event-stream`. Format: `id:`, `event:`, `data:` lines, blank line ends an event.
- `new EventSource('/stream')` → `onmessage`. Auto-reconnects and sends **Last-Event-ID** so the server can resume.
- Limits: one-way (send with normal `fetch` POST), text only.
- Trap: HTTP/1.1 ≈ 6 connections per origin; each open stream holds one → 7th tab hangs. HTTP/2 multiplexes streams on one connection.

## E05 · WebSockets
- Starts as HTTP `GET` with `Upgrade: websocket` → `101 Switching Protocols` → same TCP connection carries frames both ways.
- Frame header 2–14 bytes vs hundreds of bytes of HTTP headers. `wss://` = over TLS.
- API: `onopen`, `send`, `onmessage`, `onclose`. Each message is a task (S1E15) → batch bursts, render once per frame (`requestAnimationFrame`).
- Trap: WebSockets do **not** reconnect by themselves. Reconnect, catch up and resend are your job (E10).

## E06 · WebRTC
- Browser ↔ browser audio, video, data. See it: on a Meet call open `chrome://webrtc-internals`.
- Signaling (your choice, usually a WebSocket) swaps **offer/answer (SDP)** + **ICE candidates**. STUN = "what's my public address", TURN = relay when direct fails.
- Code: `new RTCPeerConnection({ iceServers })` → `createDataChannel` / `addTrack` → `createOffer` → `setLocalDescription` → send via signaling.
- Trap: 100-person mesh = 99 uploads each. Big calls use an **SFU** (Selective Forwarding Unit): upload once, server forwards.

## E07 · The showdown
1. Audio/video/peer data → **WebRTC**. 2. Client sends often, low latency (chat, games, cursors) → **WebSockets**.
3. Server pushes, client listens (scores, notifications, AI answers) → **SSE**. 4. Rare updates / delay OK → **polling** (long polling if faster).
- SSE: one-way, built-in reconnect, text, plain HTTP. WS: two-way, binary, DIY reconnect, leaves HTTP after upgrade. Polling: most compatible, most wasteful.
- Trap: "chat needs WebSockets" → not necessarily: SSE down + POST up is valid and stays plain HTTP (caching, auth, load balancing).

## E08 · IQ: transports
- setInterval poll vs slow server (overlap, out of order → setTimeout after response, backoff, pause when hidden) · 7th SSE tab (HTTP/1.1 6-connection limit → HTTP/2 or share one stream) · million-viewer scores (SSE) · WebRTC offer delivery (no built-in signaling; STUN/TURN).

## E09 · Heartbeats
- A dead TCP connection doesn't announce itself (sleep, Wi-Fi drop) → **half-open** connection; app shows "online" forever. Proxies also kill idle connections.
- App-level ping/pong: every message resets a timer; silence > interval + margin (e.g. 35 s for 30 s pings) → `ws.close()` → reconnect.
- Browsers answer protocol ping frames silently, and JS can't send them → apps send their own `{type:'ping'}`.
- Trap: interval must be under the shortest idle timeout on the path (often 20–30 s), but not so fast it drains batteries.

## E10 · Reconnect
- See it: WhatsApp Web, Wi-Fi off → "Computer not connected" banner; on → missed messages appear.
- Naive instant reconnect → **thundering herd** after a server restart. Fix: exponential backoff (1, 2, 4, 8 … cap 30 s) + random **jitter** (S5E14).
- On open: resync `since=<last seq>`, then flush the outbox. Listen to `online` / `offline` / `visibilitychange`.
- `AbortController` (S5E13): one `abort()` removes the old socket's listeners and cancels its catch-up fetch.
- Trap: don't retry every close. 1000 = normal close; auth failures need re-login, not retries. Retry network errors (1006).

## E11 · Ordering
- One socket = TCP order. Many paths (devices, reconnects, HTTP + socket) = no order guarantee. Sender clocks lie.
- Server assigns a **sequence number per chat**. Client: drop `seq <= last`, buffer gaps and fetch missing ranges, apply in order.
- Trap: `async` onmessage handler that awaits (decrypt) can finish message 2 before 1 → queue and process one at a time.

## E12 · Acks & dedup
- WhatsApp ticks: 1 grey = server got it, 2 grey = delivered to the device, 2 blue = read. Clock = pending (optimistic UI, S4E15).
- Lost ack → retry → duplicate. Fix: client-generated id (`crypto.randomUUID()`), outbox until acked, server drops repeat ids, client merges its own echo.
- Guarantee: **at-least-once + dedup** ≈ exactly-once.
- Trap: generate the id on the **client**: a server id doesn't exist until the first attempt succeeds.

## E13 · Scaling WebSockets
- Sockets are stateful: Alice on server A, Bob on server B. Fix: **pub/sub** (Redis, Kafka, NATS): A publishes to `user:bob`, B is subscribed and pushes down Bob's socket.
- Keep socket servers dumb, scale out; load balancer must support Upgrade + long idle timeouts.
- Deploys drop every socket on a server → drain gradually, clients reconnect with jitter.
- Trap: sticky sessions only route reconnects to the same server; they don't deliver cross-server messages.

## E14 · Presence
- Online/offline from connections + heartbeats + **TTL** (`SET presence:riya online EX 60`, renewed by each heartbeat).
- Count connections, not users (laptop closed, phone open = online). Debounce offline to avoid flapping.
- Fan-out: only to users currently viewing; throttle "typing…" (~1 event / 3 s, auto-expires).
- Trap: don't store presence in the main database → in-memory store with TTLs.

## E15 · IQ: staying alive
- Laptop sleeps, "online" for hours (half-open → heartbeats + TTL) · restart crash loop (herd → backoff + jitter, drain) · own message twice (lost ack → client UUID, dedup) · cross-server delivery (pub/sub, not sticky sessions).

## E16 · Edit conflicts
- See it: Google Docs with a friend: coloured named cursors in the same sentence.
- Whole-document saves = **last save wins** → lost words. Send **operations** (`insert 'h' @1`) instead.
- Positions shift: "cat" + insert h@1 → "chat"; concurrent delete @2 applied blindly → "cht". Adjusted to delete @3 → "cha".
- Forms: optimistic concurrency → `PUT` with `If-Match: <etag>` → `412` = conflict, merge or ask.
- Trap: locking works and users hate it (forgotten tab blocks everyone). Locks for forms/tickets, not live text.

## E17 · OT vs CRDT
- **OT**: central server orders ops and transforms late ones against earlier ones. Lean docs, needs a server.
- **CRDT**: every character gets a permanent unique id; inserts reference ids; merges in any order, peer-to-peer and offline. Costs metadata + tombstones.
- See it: Google Docs offline mode → edit → reconnect → merged.
- Trap: don't write your own. Use **Yjs** or **Automerge**; spend time on presence, cursors, undo.

## E18 · IQ: collaboration
- Typing for 200 (throttle ~3 s, viewers only, auto-expire, not in DB) · profile form lost updates (ETag + If-Match → 412 → merge) · "cat" puzzle ("cha": delete @2 → @3) · offline notes app with no server (CRDT library).

## E19 · Finale: one chat app
- Transports: WebSocket for chat, SSE for notifications, WebRTC for calls (socket = signaling), polling for the admin dashboard.
- Send: client UUID + outbox → optimistic bubble → server seq + ack → tick; retries deduped.
- Survive: heartbeats 25 s → backoff + jitter → resync since last seq → flush outbox.
- Scale: dumb socket servers + pub/sub; presence with TTL to viewers only; typing throttled. Shared notes: CRDT library.
- Next: Season 7 · Caching.
