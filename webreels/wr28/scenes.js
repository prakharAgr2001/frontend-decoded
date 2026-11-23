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
// WR28: Flipkart Big Billion Day, 6 Oct 2014: ~$100M (~₹600 crore) GMV in 10 hours; site trouble, out-of-stock; founders' apology email next day. No logos.
const PROD = (n, p) => `<div class="pr"><div class="pi"></div><b>${n}</b><span>${p}</span><i class="so">SOLD OUT</i></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="m" style="top:380px;font-size:170px;color:var(--grn)">₹0</div><div class="abs center lab" style="top:580px;font-size:44px" id="hr">in 0 hours</div>
   <div class="mail" id="ml"><div class="mh">From: The founders</div><div class="ms">We're truly sorry</div></div>`,
  draw(S) { const p = S.P(0, TT(S, 'Then', .55) - .2, x => x); S.$('#m').textContent = '₹' + Math.round(600 * eo(p)) + ' crore'; S.$('#hr').textContent = 'in ' + Math.round(10 * p) + ' hours'; if (p < 1 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick');
    IN(S, '#ml', TT(S, 'apologised', .8) - .2, 80); if (S.on(TT(S, 'apologised', .8) - .2)) S.sfx(TT(S, 'apologised', .8) - .2, 'whoosh'); }},
 { // 1 sale day
  html: `<div class="abs center kick" style="top:420px">6 October 2014 · 8 AM</div><div class="abs center h" style="top:520px;font-size:120px"><span class="mark" id="mk">BIG SALE</span></div><div class="abs center h2" style="top:760px">billed as India's biggest sale</div>`,
  draw(S) { MK(S, '#mk', .2); if (S.t < .1) S.sfx(0, 'pop'); }},
 { // 2 traffic above plan
  html: `<svg class="abs" width="1080" height="1300" style="left:0;top:0"><line x1="110" y1="800" x2="970" y2="800" stroke="var(--grn)" stroke-width="6" stroke-dasharray="20 14"/><path id="tr" d="" stroke="var(--red)" stroke-width="10" fill="none"/></svg>
   <div class="abs lab" style="left:110px;top:820px;color:var(--grn)">planned capacity</div><div class="abs center kick" style="top:420px">traffic</div>`,
  draw(S) { const p = S.P(0, S.dur - .3, x => x); let d = 'M110 1150'; for (let i = 1; i <= 40 * p; i++) { const x = 110 + i * 21.5, y = 1150 - 700 * Math.pow(i / 40, 1.6) - 30 * Math.sin(i); d += ` L${x} ${y}`; } S.$('#tr').setAttribute('d', d); if (Math.floor(S.t * 8) % 2) S.sfx(S.t, 'tick'); }},
 { // 3 failures
  html: `<div class="prods">${[['Phone', '₹9,999'], ['Laptop', '₹24,999'], ['TV', '₹14,999'], ['Watch', '₹999']].map(x => PROD(...x)).join('')}</div>
   <div class="err" id="e1">Something went wrong. Please try again.</div>`,
  draw(S) { const tf = TT(S, 'failed', .1), ts = TT(S, 'seconds', .45); POP(S, '#e1', tf, 'buzz'); S.$$('.pr').forEach((p, i) => { const s = S.on(ts - .3 + i * .15); p.classList.toggle('out', s); if (S.on(ts - .3 + i * .15)) S.sfx(ts - .3 + i * .15, 'click'); }); }},
 { // 4 apology email
  html: `<div class="mail big2" id="ml"><div class="mh">To: every customer</div><div class="ms">Yesterday was a big day for us…</div><div class="mb"><i></i><i></i><i style="width:60%"></i></div><div class="ms y" id="sr" style="opacity:0">we are truly sorry.</div></div>`,
  draw(S) { IN(S, '#ml', .1, 80); POP(S, '#sr', TT(S, 'sorry', .8) - .2, 'ding'); }},
 { // 5 lesson
  html: `<div class="abs center h" style="top:500px;font-size:90px">A sale is a<br><span class="mark" id="mk">load test</span></div><div class="abs center h2" id="l2" style="top:780px;opacity:0">you run on real customers.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'load', .3)); IN(S, '#l2', TT(S, 'real', .7) - .2); }},
 ctaScene(),
];
