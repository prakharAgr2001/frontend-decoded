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
// WR33: Heartbleed (2014): OpenSSL heartbeat trusted the client's length field; up to 64 KB of server memory leaked. ~half a million servers (Netcraft ~17%). No logo drawn.
const MEM = 'BIRD|user=priya&pass=sunflower22|session=8f3a…|GET /account|-----PRIVATE KEY-----MIIEv…|cookie=sid91c…|user=arjun&pass=…|';
const SCENES = [
 { // 0 hook
  html: `<div class="abs center h" style="top:400px;font-size:96px">One <span class="mark" id="mk">missing check</span></div>
   <div class="sites">${[...Array(24)].map(() => '<div class="st"><span class="lk">🔒</span></div>').join('')}</div>`,
  draw(S) { MK(S, '#mk', .1); const t = TT(S, 'exposed', .45); S.$$('.st').forEach((s, i) => { const o = S.on(t + R(i) * 1.2); s.classList.toggle('open', o); s.querySelector('.lk').textContent = o ? '🔓' : '🔒'; }); if (S.on(t)) S.sfx(t, 'buzz'); }},
 { // 1 Heartbleed / OpenSSL
  html: `<div class="abs center kick" style="top:440px">2014</div><div class="abs center h" style="top:520px;font-size:140px"><span class="mark" id="mk">Heartbleed</span></div>
   <div class="abs center lab" style="top:800px;font-size:44px">a bug in OpenSSL</div><div class="addr"><span>🔒</span> https://yourbank.example</div><div class="abs center lab" style="top:1180px;font-size:36px">the code behind this lock</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'Heartbleed', .3)); IN(S, '.addr', TT(S, 'lock', .8) - .3, 40); }},
 { // 2 heartbeat request
  html: `<div class="node c">YOU</div><div class="node s">SERVER</div><div class="msg" id="m1">are you there? send back <b>"BIRD"</b> · <span class="y">length: 4</span></div><div class="msg back" id="m2">"BIRD"</div>`,
  draw(S) { const p = S.P(0, 1.2, eio); S.$('#m1').style.transform = `translateY(${-60 + 200 * p}px)`; S.$('#m1').style.opacity = clamp(S.P(0, .3)); if (S.t < .1) S.sfx(0, 'whoosh');
    const t4 = TT(S, '4', .85); IN(S, '#m2', t4, 40); }},
 { // 3 the lie: ask 64 KB
  html: `<div class="node c">YOU</div><div class="node s">SERVER</div><div class="msg" id="m1">send back <b>"BIRD"</b> · <span class="r" id="ln">length: 4</span></div>
   <div class="abs center h2" id="nc" style="top:1250px;opacity:0">the server <span class="mark" id="mk">never checked</span></div>`,
  init(el) { el.querySelector('#m1').style.transform = 'translateY(140px)'; },
  draw(S) { const t = TT(S, 'checked', .3); IN(S, '#nc', t - .3); MK(S, '#mk', t); const t64 = TT(S, '64', .55); S.$('#ln').textContent = S.on(t64) ? 'length: 65,535' : 'length: 4'; if (S.on(t64)) S.sfx(t64, 'thud'); SHAKE(S, '#m1', t64); }},
 { // 4 memory leak stream
  html: `<div class="abs center kick" style="top:400px">what came back</div><div class="leak" id="lk"></div>`,
  draw(S) { const n = Math.floor(S.P(0, S.dur - .3, x => x) * MEM.length * 3); let s = (MEM + MEM + MEM).slice(0, n); s = s.replace(/</g, '&lt;').replace(/(pass=[^&|]*)/g, '<span class="r">$1</span>').replace(/(PRIVATE KEY)/g, '<span class="r">$1</span>').replace(/^BIRD/, '<span class="g">BIRD</span>');
    S.$('#lk').innerHTML = s; if (Math.floor(S.t * 14) % 2) S.sfx(S.t, 'tick'); }},
 { // 5 half a million servers
  html: `<div class="abs center big" id="n" style="top:440px;font-size:170px;color:var(--red)">0</div><div class="abs center lab" style="top:660px;font-size:44px">secure servers open</div>
   <div class="sv">${[...Array(100)].map((_, i) => `<i class="${i < 17 ? 'o' : ''}"></i>`).join('')}</div><div class="abs center lab" style="top:1360px">≈ 1 in 6 secure websites (Netcraft)</div>`,
  draw(S) { COUNT(S, '#n', 0, 500000, 0, 1.2, v => '~' + fmt(v)); S.$$('.sv i.o').forEach((d, i) => d.style.background = S.on(1 + i * .05) ? 'var(--red)' : ''); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:470px;font-size:90px">Never trust a<br><span class="mark" id="mk">length</span> the user<br>sends you.</div>
   ${WIN('fix', `<span class="k">if</span> (claimed > actual) <span class="k">return</span> <span class="r">drop</span>()`)}`,
  init(el) { el.querySelector('.win').style.top = '920px'; },
  draw(S) { MK(S, '#mk', TT(S, 'length', .4)); }},
 ctaScene(),
];
