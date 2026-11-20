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
// WR16: Mars Climate Orbiter (1999): pound-force seconds vs newton-seconds
const SAT = `<svg viewBox="0 0 200 100" width="200"><rect x="80" y="30" width="40" height="40" rx="6" fill="#d9d4c7"/><rect x="5" y="40" width="70" height="20" fill="#4c9dff"/><rect x="125" y="40" width="70" height="20" fill="#4c9dff"/><circle cx="100" cy="22" r="10" fill="none" stroke="#d9d4c7" stroke-width="4"/></svg>`;
const MARS = (x, y, r) => `<div class="mars" style="left:${x - r}px;top:${y - r}px;width:${2 * r}px;height:${2 * r}px"></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="m" style="top:360px;font-size:120px;color:var(--red)">$0</div>
   <div class="abs center h2" style="top:520px">spacecraft, lost</div>
   <div class="abs" id="sat" style="left:440px;top:760px">${SAT}</div>
   <div class="abs center h" id="u" style="top:1080px;font-size:110px;opacity:0">because of <span class="mark" id="mk">units</span></div>`,
  draw(S) { COUNT(S, '#m', 0, 125e6, 0, 1.3, v => '$' + fmt(v)); const tu = TT(S, 'units', .7); POP(S, '#u', tu - .3, 'thud'); MK(S, '#mk', tu);
    S.$('#sat').style.transform = `rotate(${S.t * 25}deg) translateX(${10 * Math.sin(S.t)}px)`; if (S.t < 1.3 && Math.floor(S.t * 14) % 2) S.sfx(S.t, 'tick'); }},
 { // 1 trip to Mars
  html: `<div class="abs center kick" style="top:380px">1999 · Mars Climate Orbiter</div>
   <div class="earth" style="left:110px;top:1080px"></div>${MARS(860, 640, 110)}
   <svg class="abs" width="1080" height="1500" style="left:0;top:0"><path id="pt" d="M190 1080 Q300 600 760 650" stroke="#555" stroke-width="5" stroke-dasharray="14 14" fill="none"/></svg>
   <div class="abs" id="ms" style="width:80px">${SAT.replace('width="200"', 'width="80"')}</div><div class="abs center big" id="mo" style="top:1300px;font-size:90px">month 0</div>`,
  draw(S) { const p = S.P(0, S.dur - .3, eio), path = S.$('#pt'), pt = path.getPointAtLength(path.getTotalLength() * p); S.$('#ms').style.left = pt.x - 40 + 'px'; S.$('#ms').style.top = pt.y - 20 + 'px';
    S.$('#mo').textContent = 'month ' + Math.round(10 * p); }},
 { // 2 pounds vs newtons
  html: `<div class="tile team" id="ta" style="left:90px;top:520px"><div class="lab">TEAM A software</div><div class="u">pounds</div><div class="lab">lbf · s</div></div>
   <div class="tile team" id="tb" style="left:590px;top:520px"><div class="lab">NAVIGATION</div><div class="u">newtons</div><div class="lab">N · s</div></div>
   <div class="abs" id="pk" style="left:470px;top:640px;font:700 60px Mono;color:var(--yel)">➜</div>
   <div class="abs center" id="ne" style="top:1040px;font:900 160px Roboto;color:var(--red);opacity:0">≠</div>`,
  draw(S) { IN(S, '#ta', TT(S, 'pounds', .3) - .3); IN(S, '#tb', TT(S, 'newtons', .7) - .3); const p = (S.t * .9) % 1; S.$('#pk').style.transform = `translateX(${60 * p}px)`; POP(S, '#ne', TT(S, 'newtons', .7) + .3, 'buzz'); }},
 { // 3 4.45x, trajectory drifts
  html: `<div class="abs center num" style="top:380px">1 pound of force = <span class="y">4.45</span> N</div>
   <svg class="abs" width="1080" height="1300" style="left:0;top:0"><path d="M100 1250 Q500 900 900 620" stroke="var(--grn)" stroke-width="8" fill="none" stroke-dasharray="20 14"/><path id="real" d="M100 1250 Q500 1040 900 900" stroke="var(--red)" stroke-width="10" fill="none"/></svg>
   <div class="abs lab" style="left:740px;top:560px;color:var(--grn)">planned</div><div class="abs lab" style="left:760px;top:980px;color:var(--red)">actual</div>`,
  draw(S) { const r = S.$('#real'), L = r.getTotalLength(), p = S.P(TT(S, 'correction', .6) - .4, 1, eo); r.style.strokeDasharray = L; r.style.strokeDashoffset = L * (1 - p); }},
 { // 4 too low, lost
  html: `${MARS(540, 1500, 700)}<div class="atmo"></div><div class="abs" id="o" style="width:120px">${SAT.replace('width="200"', 'width="120"')}</div>
   <div class="abs" style="left:110px;top:640px;font:600 30px Roboto;color:var(--grn)">safe height</div><div class="abs" style="left:110px;right:110px;top:690px;border-top:4px dashed var(--grn)"></div>
   <div class="stamp" id="lost" style="left:380px;top:480px;font-size:96px">LOST</div>`,
  draw(S) { const p = S.P(0, S.dur * .8, x => x), x = 1000 - 860 * p, y = 520 + 460 * p * p; S.$('#o').style.left = x + 'px'; S.$('#o').style.top = y + 'px';
    S.$('#o').style.filter = p > .6 ? `drop-shadow(0 0 ${40 * (p - .6) / .4}px #ff7a1a) brightness(${1 + p})` : ''; S.$('#o').style.opacity = 1 - S.P(S.dur * .75, .3); STAMP(S, '#lost', TT(S, 'lost', .8)); }},
 { // 5 no crash, no check
  html: `${WIN('build log', `<span class="g">✓ compiled</span>\n<span class="g">✓ 0 errors</span>\n<span class="g">✓ 0 warnings</span>`)}
   <div class="abs center" style="top:900px"><span class="chip">pounds</span><span id="q" style="font:900 90px Roboto;color:var(--red);margin:0 40px;opacity:0">?</span><span class="chip">newtons</span></div>`,
  init(el) { el.querySelector('.win').style.top = '440px'; },
  draw(S) { POP(S, '#q', TT(S, 'check', .8), 'buzz', 2); }},
 { // 6 name the unit
  html: `<div class="abs center kick" style="top:420px">put the unit in the name</div>
   <div class="tile" style="left:110px;right:110px;top:540px;height:220px;display:flex;align-items:center;justify-content:center;font:500 64px Mono" id="bad"><span><span class="k">let</span> <span class="v">delay</span> = 300</span></div>
   <div class="tile" style="left:110px;right:110px;top:820px;height:220px;display:flex;align-items:center;justify-content:center;font:500 64px Mono;box-shadow:0 0 0 4px var(--grn)" id="good"><span><span class="k">let</span> <span class="v">delayMs</span> = 300</span></div>`,
  draw(S) { const tn = TT(S, 'delay', .5), tm = TT(S, 'milliseconds', .85); S.$('#bad').style.opacity = S.on(tm) ? .35 : 1; S.$('#bad').style.textDecoration = S.on(tm) ? 'line-through' : ''; IN(S, '#good', tm - .3); if (S.on(tm)) S.sfx(tm, 'ding'); }},
 ctaScene(),
];
