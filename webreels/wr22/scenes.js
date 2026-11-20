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
// WR22: gene symbols auto-converted to dates by spreadsheets; ~1 in 5 papers affected (2016 study); HGNC renamed them in 2020
const CELL = (id) => `<div class="cellw"><div class="fx">fx <span id="${id}f"></span></div><div class="cel"><span class="rh">A1</span><span id="${id}"></span></div></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center h" style="top:330px;font-size:84px">Scientists <span class="mark" id="mk">renamed</span><br>human genes</div>${CELL('c0')}
   <div class="abs center lab" id="why" style="top:1180px;font-size:44px;opacity:0">because spreadsheets kept turning them into dates</div>`,
  draw(S) { MK(S, '#mk', .1); const td = TT(S, 'dates', .7); const conv = S.on(td - .4); TYPE(S, '#c0', conv ? '1-Sep' : 'SEPT1', conv ? 99 : .3, .8);
    if (conv) S.$('#c0').textContent = '1-Sep'; S.$('#c0').style.color = conv ? 'var(--red)' : '#111'; if (S.on(td - .4)) S.sfx(td - .4, 'buzz'); SHAKE(S, '.cel', td - .4); IN(S, '#why', TT(S, 'Because', .45)); }},
 { // 1 the genes
  html: `<div class="abs center kick" style="top:420px">real human gene names</div><div class="chips">${['SEPT1', 'MARCH1', 'SEPT2', 'MARCH5'].map(g => `<span class="gc">${g}</span>`).join('')}</div>`,
  draw(S) { S.$$('.gc').forEach((c, i) => { const p = S.P(.1 + i * .2, .3, back); c.style.opacity = clamp(p); c.style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(.1 + i * .2)) S.sfx(.1 + i * .2, 'pop'); }); }},
 { // 2 typed -> converted
  html: `${CELL('c2')}<div class="tip" id="tp">✨ Converted to a date for you</div><div class="abs center h2" id="sp" style="top:1180px;opacity:0">SEPT1 ➜ <span class="r">1st of September</span></div>`,
  draw(S) { const th = TT(S, 'helpfully', .35); const conv = S.on(th); S.$('#c2').textContent = conv ? '01-Sep' : 'SEPT1'.slice(0, Math.ceil(5 * S.P(.1, .8, x => x))); S.$('#c2').style.color = conv ? 'var(--red)' : '#111';
    IN(S, '#tp', th, 30); if (conv) S.sfx(th, 'swish'); POP(S, '#sp', TT(S, 'September', .8) - .3, 'thud'); }},
 { // 3 1 in 5 papers
  html: `<div class="abs center kick" style="top:400px">published papers with gene lists</div><div class="papers">${[...Array(20)].map(() => '<div class="pp"><i></i><i></i><i></i></div>').join('')}</div>
   <div class="abs center big" id="r" style="top:1330px;font-size:110px;color:var(--red);opacity:0">1 in 5 had errors</div>`,
  draw(S) { const to = TT(S, 'five', .5); S.$$('.pp').forEach((p, i) => { const bad = i % 5 === 2 && S.on(to - .3 + (i / 5) * .12); p.classList.toggle('bad', bad); }); POP(S, '#r', to - .2, 'thud'); }},
 { // 4 renamed
  html: `<div class="abs center kick" style="top:400px">2020 · official gene names</div>
   ${[['SEPT1', 'SEPTIN1'], ['MARCH1', 'MARCHF1']].map((g, i) => `<div class="rn" id="g${i}" style="top:${540 + i * 300}px"><span class="old">${g[0]}</span><span class="ar">➜</span><span class="nw">${g[1]}</span></div>`).join('')}`,
  draw(S) { const tr = TT(S, 'renamed', .3); [0, 1].forEach(i => { const at = tr + i * .5, g = S.$('#g' + i); g.querySelector('.nw').style.opacity = S.P(at, .3); g.querySelector('.old').style.textDecoration = S.on(at) ? 'line-through' : ''; if (S.on(at)) S.sfx(at, 'ding'); }); }},
 { // 5 lesson
  html: `<div class="abs center h" style="top:470px;font-size:84px">When a tool guesses<br>your data type,</div><div class="abs center h" id="l2" style="top:720px;font-size:84px;opacity:0">it can <span class="mark" id="mk">quietly change</span><br>your data.</div>
   <div class="abs center" id="tx" style="top:1060px;font:600 44px Mono;color:var(--mute);opacity:0">tip: import IDs as <span class="y">Text</span></div>`,
  draw(S) { const tq = TT(S, 'quietly', .6); IN(S, '#l2', tq - .3); MK(S, '#mk', tq); IN(S, '#tx', S.dur - 1.2); }},
 ctaScene(),
];
