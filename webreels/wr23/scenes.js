// ---- story kit (shared by WR12+; copied into each scenes.js by webreels/_kit/build.sh) ----
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const TT = (S, w, f = .3, n = 1) => { try { return S.T(w, n); } catch (e) { return S.dur * f; } };
const MK = (S, sel, at) => S.$(sel).style.setProperty('--m', S.P(at - .1, .35));
function POP(S, sel, at, snd = 'pop', from = .7) { const e = S.$(sel), p = S.P(at, .3, back); e.style.opacity = clamp(p); e.style.transform = `scale(${from + (1 - from) * clamp(p)})`; if (snd && S.on(at)) S.sfx(at, snd); return p; }
function STAMP(S, sel, at, rot = -8) { const e = S.$(sel), p = S.P(at, .22, back); e.style.opacity = clamp(p * 2); e.style.transform = `rotate(${rot}deg) scale(${1.6 - .6 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'thud'); }
function TYPE(S, sel, txt, at, d) { const k = Math.floor(txt.length * S.P(at, d, x => x)); S.$(sel).innerHTML = txt.slice(0, k).replace(/</g, '&lt;') + (k < txt.length && S.on(at) ? '<span class="caret"></span>' : ''); if (S.on(at) && k < txt.length && Math.floor(S.t * 20) % 2) S.sfx(S.t, 'click'); }
function COUNT(S, sel, a, b, at, d, f = fmt, e = eio) { S.$(sel).textContent = f(a + (b - a) * S.P(at, d, e)); }
function SHAKE(S, sel, at, amp = 12, len = .6) { const k = S.on(at) ? Math.max(0, 1 - (S.t - at) / len) : 0; S.$(sel).style.translate = `${amp * k * Math.sin(S.t * 80)}px ${amp * .5 * k * Math.cos(S.t * 63)}px`; }
function IN(S, sel, at, dy = 60) { const e = S.$(sel), p = S.P(at, .35); e.style.opacity = p; e.style.transform = `translateY(${dy * (1 - p)}px)`; return p; }
const SWITCHES = (n, cols, w = 84) => `<div class="sws" style="width:${cols * (w + 18)}px">${'<span class="sw"></span>'.repeat(n)}</div>`;
function SETSW(S, on) { S.$$('.sw').forEach((s, i) => s.classList.toggle('on', i < on)); }
const WIN = (title, body, cls = '') => `<div class="win ${cls}"><div class="wt"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span>${title}</span></div><div class="wb">${body}</div></div>`;
// ---- end kit ----
// WR23: Hinge "Your Turn Limits" (test May 2024, global Sep 2024): 8+ matches waiting -> reply or end a chat before matching again
const IMG = n => `url(../../webreels/wr10/img/p${n}.jpg)`;
const NAMES = ['Maya', 'Leo', 'Ava', 'Noah', 'Sara', 'Kabir', 'Zoya', 'Arjun', 'Ira'];
const PICS = [1, 4, 7, 3, 10, 5, 11, 6, 12];
const ROW = (i, msg) => `<div class="row" id="w${i}"><div class="av" style="background-image:${IMG(PICS[i])}"></div><div class="tx"><b>${NAMES[i]}</b><span>${msg}</span></div><div class="yt">Your turn</div></div>`;
const MSGS = ['so… pizza or tacos?', 'haha same! when are you free?', 'that hike looks unreal', 'ok your turn: worst date ever?', 'coffee this weekend?', 'did you finish the show?', 'favourite song right now?', 'you still there? 👀', 'hey!'];
const SCENES = [
 { // 0 hook: chats pile up, lock
  html: `<div class="phone"><div class="hd">Matches</div><div class="list">${[0, 1, 2, 3, 4, 5, 6, 7].map(i => ROW(i, MSGS[i])).join('')}</div>
   <div class="lock" id="lk"><div class="lki">🔒</div><b>Reply to your matches<br>to keep matching</b></div></div>
   <div class="abs center" id="cnt" style="top:330px;font:800 64px Roboto">ghosted: <span id="g" class="y">0</span></div>`,
  draw(S) { const ts = TT(S, 'stops', .6); S.$$('.row').forEach((r, i) => { const at = .1 + i * (ts - .4) / 8; const p = S.P(at, .25, back); r.style.opacity = clamp(p); r.style.transform = `translateX(${(1 - clamp(p)) * 200}px)`; if (S.on(at)) S.sfx(at, 'pop'); });
    S.$('#g').textContent = Math.min(8, Math.floor(8 * S.P(.1, ts - .3, x => x) + .001)); const l = S.$('#lk'), p = S.P(ts, .3, back); l.style.opacity = clamp(p); l.style.transform = `scale(${.8 + .2 * clamp(p)})`; if (S.on(ts)) S.sfx(ts, 'thud'); }},
 { // 1 feature name
  html: `<div class="abs center kick" style="top:470px">a real feature</div><div class="abs center h" style="top:560px;font-size:120px"><span class="mark" id="mk">Your Turn Limits</span></div>
   <div class="abs center lab" style="top:780px;font-size:40px">tested May 2024 · launched worldwide Sept 2024</div>`,
  draw(S) { const t = TT(S, 'Your', .6); MK(S, '#mk', t); if (S.on(t)) S.sfx(t, 'ding'); }},
 { // 2 44%
  html: `<svg class="abs" style="left:290px;top:400px" width="500" height="500"><circle cx="250" cy="250" r="200" stroke="#2a2a31" stroke-width="60" fill="none"/><circle id="arc" cx="250" cy="250" r="200" stroke="#ff3b3b" stroke-width="60" fill="none" transform="rotate(-90 250 250)" stroke-dasharray="1257" stroke-dashoffset="1257"/></svg>
   <div class="abs center big" id="pc" style="top:580px;font-size:140px">0%</div>
   <div class="abs center h2" style="top:980px">say: <span class="mark" id="mk">matches never reply</span></div>`,
  draw(S) { const p = S.P(TT(S, '44', .2) - .2, 1, eo); S.$('#arc').setAttribute('stroke-dashoffset', 1257 * (1 - .44 * p)); S.$('#pc').textContent = Math.round(44 * p) + '%'; MK(S, '#mk', TT(S, 'never', .8)); }},
 { // 3 counter hits 8
  html: `<div class="abs center kick" style="top:420px">people waiting on your reply</div><div class="dots">${[...Array(10)].map((_, i) => `<i style="background-image:${IMG(PICS[i % 9])}"></i>`).join('')}</div>
   <div class="abs" style="left:110px;right:110px;top:1000px;height:8px;background:var(--red);box-shadow:0 0 30px var(--red);border-radius:4px"></div><div class="abs lab" style="right:110px;top:940px;color:var(--red);letter-spacing:3px">LIMIT · 8</div>
   <div class="abs center big" id="n" style="top:1080px;font-size:160px">0</div>`,
  draw(S) { const te = TT(S, 'eight', .5), n = Math.min(8, Math.floor(8 * S.P(0, te + .2, x => x) + .001)); S.$$('.dots i').forEach((d, i) => d.style.opacity = i < n ? 1 : .12); S.$('#n').textContent = n; S.$('#n').style.color = n >= 8 ? 'var(--red)' : 'var(--paper)';
    if (n !== this.n) S.sfx(S.t, n >= 8 ? 'thud' : 'click'); this.n = n; }},
 { // 4 no new matches: like disabled, two choices
  html: `<div class="card"><div class="ph" style="background-image:${IMG(9)}"></div><div class="hb" id="hb">♥</div><div class="dim" id="dm">No new matches until you reply</div></div>
   <div class="abs" style="left:110px;right:110px;top:1240px;display:flex;gap:30px"><div class="btn g" id="b1">Reply</div><div class="btn" id="b2">End chat</div></div>`,
  draw(S) { const tn = TT(S, 'no', .1); S.$('#dm').style.opacity = S.P(tn, .3); S.$('#hb').style.filter = S.on(tn) ? 'grayscale(1)' : ''; S.$('#hb').style.opacity = S.on(tn) ? .4 : 1; if (S.on(tn)) S.sfx(tn, 'buzz');
    IN(S, '#b1', TT(S, 'Reply', .5) - .1, 40); IN(S, '#b2', TT(S, 'end', .8) - .1, 40); }},
 { // 5 +20%
  html: `<div class="abs center kick" style="top:420px">replies on the app · test result</div>
   <div class="cmp" style="top:620px"><div class="l"><span>before</span><span>100</span></div><div class="t"><i id="b0" style="background:#666"></i></div></div>
   <div class="cmp" style="top:820px"><div class="l"><span>with the limit</span><span id="v">100</span></div><div class="t"><i id="b1" style="background:var(--grn)"></i></div></div>
   <div class="abs center big" id="up" style="top:1080px;font-size:170px;color:var(--grn);opacity:0">+20%</div>`,
  draw(S) { S.$('#b0').style.width = 100 / 1.2 * S.P(0, .5) + '%'; const t = TT(S, '20', .6), p = S.P(t - .6, .6, eio); S.$('#b1').style.width = (100 / 1.2) * (1 + .2 * p) * S.P(0, .5) + '%'; S.$('#v').textContent = Math.round(100 + 20 * p); POP(S, '#up', t - .1, 'ding'); }},
 { // 6 rate limiter for your love life
  html: `<div class="abs center h2" style="top:380px">it's a <span class="mark" id="mk">rate limiter</span></div>
   <div class="rl"><div class="in" id="in"></div><div class="gate"><b>max 8</b><span>in flight</span></div><div class="out" id="out"></div></div>
   <div class="abs center h" id="ll" style="top:1180px;font-size:96px;opacity:0">for your love life ${EMO('red-heart')}</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'rate', .2)); const k = Math.floor(S.t * 6); S.$('#in').innerHTML = [...Array(5)].map((_, i) => `<i style="background-image:${IMG(PICS[(k + i) % 9])};opacity:${1 - i * .15}"></i>`).join('');
    S.$('#out').innerHTML = [...Array(8)].map((_, i) => `<i style="background-image:${IMG(PICS[i % 9])}"></i>`).join(''); POP(S, '#ll', TT(S, 'love', .75) - .3, 'pop'); }},
 ctaScene(),
];
