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
// WR31: Gmail announced 1 April 2004 with 1 GB free (Hotmail: 2 MB), search instead of folders, invite-only until Feb 2007. No logos.
const SCENES = [
 { // 0 hook
  html: `<div class="cal"><div class="ch">APRIL 2004</div><div class="cday">1</div></div><div class="abs center h2" style="top:1100px">a new email service launches</div>
   <div class="stamp" id="j" style="left:250px;top:1250px;font-size:84px">A JOKE?</div>`,
  draw(S) { POP(S, '.cal', 0, 'pop'); STAMP(S, '#j', TT(S, 'joke', .75)); }},
 { // 1 a few MB
  html: `<div class="abs center kick" style="top:420px">2004 · free inbox storage</div><div class="bx" style="top:540px"><span>Hotmail (free)</span><div class="tr"><i id="h" style="background:var(--red)"></i></div><b id="hv">2 MB</b></div>
   <div class="abs center lab" style="top:780px;font-size:40px">≈ a few hundred emails, then "inbox full"</div>`,
  draw(S) { S.$('#h').style.width = .2 * S.P(TT(S, 'Hotmail', .6) - .3, .4) + '%'; }},
 { // 2 1 GB, 500x
  html: `<div class="bx" style="top:480px"><span>Hotmail (free)</span><div class="tr"><i style="width:.2%;background:var(--red)"></i></div><b>2 MB</b></div>
   <div class="bx" style="top:700px"><span>Gmail (free)</span><div class="tr"><i id="g" style="background:var(--grn)"></i></div><b>1 GB</b></div>
   <div class="abs center big" id="x" style="top:1000px;font-size:180px;color:var(--yel);opacity:0">500x</div><div class="abs center lab" style="top:1220px;font-size:44px">free</div>`,
  draw(S) { S.$('#g').style.width = 100 * S.P(TT(S, 'gigabyte', .3) - .3, 1, eo) + '%'; POP(S, '#x', TT(S, '500', .75) - .2, 'thud'); }},
 { // 3 search instead of folders
  html: `<div class="fold" id="fd">${['Work', 'Family', 'Bills', 'Old', 'Misc'].map(f => `<div>📁 ${f}</div>`).join('')}</div>
   <div class="srch" id="sr"><span id="q"></span><b>Search</b></div><div class="abs center h2" id="t" style="top:1200px;opacity:0">search, <span class="mark" id="mk">not folders</span></div>`,
  draw(S) { const ts = TT(S, 'search', .3); S.$('#fd').style.opacity = 1 - .8 * S.P(ts, .4); S.$('#fd').style.filter = S.on(ts) ? 'grayscale(1)' : ''; IN(S, '#sr', ts - .1, 40); TYPE(S, '#q', 'flight ticket march', ts + .1, .9); IN(S, '#t', TT(S, 'folders', .8) - .3); MK(S, '#mk', TT(S, 'folders', .8)); }},
 { // 4 invite only
  html: `<div class="inv" id="iv"><div class="lab">YOU'RE INVITED</div><div style="font:800 64px Roboto;margin:24px 0">Join the new email</div><div class="lab">invite-only · 2004 → 2007</div></div><div class="stamp g" id="rl" style="left:330px;top:1150px">IT WAS REAL</div>`,
  draw(S) { IN(S, '#iv', .1, 80); STAMP(S, '#rl', TT(S, 'real', .2), -6); }},
 { // 5 lesson
  html: `<div class="abs center h" style="top:470px;font-size:84px"><span class="mark" id="m1">Cheap storage</span><br>+ <span class="mark" id="m2">great search</span></div><div class="abs center h2" id="l2" style="top:780px;opacity:0">changed how we keep<br>everything.</div>`,
  draw(S) { MK(S, '#m1', TT(S, 'storage', .2)); MK(S, '#m2', TT(S, 'search', .45)); IN(S, '#l2', TT(S, 'changed', .7) - .2); }},
 ctaScene(),
];
