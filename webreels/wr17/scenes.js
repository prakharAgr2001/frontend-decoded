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
// WR17: Ariane 5 flight 501 (4 Jun 1996): 64-bit float -> 16-bit int overflow, ~37 s after ignition
const ROCKET = `<svg viewBox="0 0 120 400" width="120"><path d="M60 0 Q90 50 90 120 L90 330 L30 330 L30 120 Q30 50 60 0Z" fill="#eeeae0"/><rect x="30" y="200" width="60" height="18" fill="#c33"/>
 <path d="M30 260 L5 340 L30 330Z M90 260 L115 340 L90 330Z" fill="#bbb"/><rect x="40" y="330" width="40" height="22" fill="#666"/></svg>`;
const SCENES = [
 { // 0 hook: launch, T+ timer, boom
  noFlash: true,
  html: `<div class="abs center big" id="tm" style="top:360px;font-size:120px">T+ 00s</div>
   <div class="abs" id="rk" style="left:480px;top:900px">${ROCKET}<div class="fl"></div></div><div class="boom" id="bm"></div>
   <div class="abs center h2" id="fit" style="top:1300px;opacity:0">because a number <span class="mark" id="mk">didn't fit</span></div>`,
  draw(S) { const te = TT(S, 'exploded', .3), p = S.P(0, te, x => x); S.$('#tm').textContent = 'T+ ' + String(Math.round(37 * p)).padStart(2, '0') + 's';
    S.$('#rk').style.transform = `translateY(${-500 * p * p}px) rotate(${S.on(te - .4) ? 30 * S.P(te - .4, .4) : 0}deg)`; S.$('#rk').style.opacity = S.on(te) ? 0 : 1;
    const b = S.P(te, .6, eo); S.$('#bm').style.transform = `scale(${b * 3})`; S.$('#bm').style.opacity = S.on(te) ? 1 - S.P(te + .4, 1) : 0; if (S.on(te)) S.sfx(te, 'thud'); if (S.t > te && S.t < te + .1) flash(.8);
    POP(S, '#fit', TT(S, 'number', .7) - .2, null); MK(S, '#mk', TT(S, 'fit', .85)); }},
 { // 1 first flight
  html: `<div class="abs center kick" style="top:400px">4 June 1996 · first flight</div><div class="abs center big" id="cd" style="top:540px;font-size:260px">3</div>
   <div class="abs" style="left:480px;top:900px">${ROCKET}</div><div class="abs center" style="top:1320px"><span class="pill">ARIANE 5</span></div>`,
  draw(S) { const k = Math.min(3, Math.floor(S.t / (S.dur / 4))); S.$('#cd').textContent = ['3', '2', '1', 'GO'][k]; if (k !== this.k) S.sfx(S.t, k === 3 ? 'whoosh' : 'tick'); this.k = k; }},
 { // 2 copied code
  html: `<div class="tile cp" id="a4" style="left:90px;top:520px"><div class="lab">ARIANE 4</div><div class="cd">navigation.ada</div><div class="lab">slower rocket</div></div>
   <div class="tile cp" id="a5" style="left:590px;top:520px;opacity:0"><div class="lab">ARIANE 5</div><div class="cd">navigation.ada</div><div class="lab">faster rocket</div></div>
   <div class="abs center" id="cv" style="top:1000px;font:700 60px Mono;color:var(--yel)">Ctrl+C ➜ Ctrl+V</div>`,
  draw(S) { const tc = TT(S, 'copied', .4); const p = S.P(tc, .6, eio), g = S.$('#a5'); g.style.opacity = p; g.style.transform = `translateX(${-500 * (1 - p)}px)`; if (S.on(tc)) S.sfx(tc, 'whoosh'); }},
 { // 3 squeeze 64 -> 16
  html: `<div class="abs center kick" style="top:380px">sideways speed value</div>
   <div class="box64"><span class="lab">64-bit</span><div class="sws">${'<span class="b"></span>'.repeat(64)}</div></div>
   <div class="abs center" style="top:900px;font-size:80px;color:var(--mute)">↓ squeezed into</div>
   <div class="box16"><span class="lab">16-bit</span><div class="sws">${'<span class="b"></span>'.repeat(16)}</div></div>
   <div class="abs center num" id="mx" style="top:1320px;color:var(--yel);opacity:0">max 32,767</div>`,
  draw(S) { const ts = TT(S, 'squeezed', .35); S.$('.box16').style.transform = `scaleX(${1 - .08 * Math.sin(S.P(ts, .5) * Math.PI)})`; S.$$('.box16 .b').forEach((b, i) => b.style.background = S.on(ts + i * .03) ? 'var(--yel)' : '#2a2a31');
    POP(S, '#mx', TT(S, 'Max', .75), 'thud'); }},
 { // 4 overflow
  html: `<div class="abs center kick" style="top:400px">value in the 16-bit box</div><div class="abs center big" id="v" style="top:520px;font-size:170px">0</div>
   <div class="abs" style="left:110px;right:110px;top:800px;height:50px;border-radius:25px;background:#2a2a31;overflow:hidden"><div id="b" style="height:100%;background:var(--yel)"></div></div>
   <div class="stamp" id="ov" style="left:260px;top:960px;font-size:100px">OVERFLOW</div>`,
  draw(S) { const to = TT(S, 'overflowed', .7), p = S.P(0, to, x => x); const val = Math.round(40000 * p); const shown = val > 32767 ? val - 65536 : val;
    S.$('#v').textContent = fmt(shown).replace('-', '−'); S.$('#v').style.color = val > 32767 ? 'var(--red)' : 'var(--paper)'; S.$('#b').style.width = Math.min(100, 100 * val / 32767) + '%';
    if (p < 1 && Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); STAMP(S, '#ov', to); if (S.t > to && S.t < to + .1) flash(.5); }},
 { // 5 backup fails too
  html: `${['MAIN', 'BACKUP'].map((n, i) => `<div class="tile cpu" id="u${i}" style="left:${90 + i * 500}px;top:560px"><div class="lab">${n} COMPUTER</div><div class="cd" style="font-size:32px">same code</div><div class="st">✓</div></div>`).join('')}`,
  draw(S) { const tb = TT(S, 'backup', .2), tf = TT(S, 'failed', .7); [[0, tb - .4], [1, tf]].forEach(([i, at]) => { const u = S.$('#u' + i), x = u.querySelector('.st'); x.textContent = S.on(at) ? '✗' : '✓'; x.style.color = S.on(at) ? 'var(--red)' : 'var(--grn)';
      u.style.boxShadow = S.on(at) ? '0 0 0 4px var(--red),0 0 70px rgba(255,59,59,.45)' : ''; if (S.on(at)) S.sfx(at, 'buzz'); }); }},
 { // 6 lesson
  noFlash: true,
  html: `<div class="redbg" id="rb"></div><div class="abs center" style="top:470px;font:900 110px Roboto;letter-spacing:6px" id="sd">SELF-DESTRUCT</div>
   <div class="abs center h" id="ls" style="top:760px;font-size:90px;opacity:0">Reused code carries<br><span class="mark" id="mk">old assumptions</span></div>`,
  draw(S) { if (S.t < .08) flash(.6); S.sfx(0, 'thud'); const tr = TT(S, 'Reused', .4); S.$('#rb').style.opacity = 1 - .85 * S.P(tr - .2, .5); S.$('#sd').style.opacity = 1 - .7 * S.P(tr - .2, .5); IN(S, '#ls', tr); MK(S, '#mk', TT(S, 'old', .8)); }},
 ctaScene(),
];
