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
// DSA02 (sample v2): longest substring without repeating characters. Company/salary sources are in spec.py. No logos.
const W = 'chaichai'.split(''), BW = 96, GAP = 10, X0 = 122;
const bx = i => X0 + i * (BW + GAP);
const ROW = (id, top) => `<div class="row" id="${id}" style="top:${top}px">${W.map((c, i) => `<div class="b" style="left:${bx(i) - X0}px"><b>${c}</b><span>${i}</span></div>`).join('')}<div class="frame"></div></div>`;
function FRAME(S, id, l, r, col = 'var(--grn)', show = 1) { const f = S.$(`#${id} .frame`); f.style.left = (bx(l) - X0 - 10) + 'px'; f.style.width = ((r - l + 1) * (BW + GAP) - GAP + 20) + 'px'; f.style.borderColor = col; f.style.boxShadow = `0 0 40px ${col}`; f.style.opacity = show; }
function LIT(S, id, from, to, cls = 'on') { S.$$(`#${id} .b`).forEach((b, i) => b.classList.toggle(cls, i >= from && i <= to)); }
const PTR = (id, txt, col) => `<div class="pt" id="${id}" style="--c:${col}"><i></i>${txt}</div>`;
function PT(S, id, i, top) { const p = S.$('#' + id); p.style.left = (bx(i) + BW / 2 - 70) + 'px'; p.style.top = top + 'px'; }
const SCENES = [
 { // 0 hook: offer card + Amazon report chip
  html: `<div class="offer" id="of"><div class="ok">OFFER</div><div class="role">Software Development Engineer I</div><div class="co">Amazon · India</div><div class="ctc"><span id="ct">₹0</span><small> LPA total comp</small></div></div>
   <div class="abs center" id="ch" style="top:1020px;opacity:0"><span class="tag">ASKED IN AMAZON INTERVIEWS · 2025</span></div>
   <div class="abs center h2" id="q" style="top:1130px;opacity:0">this <span class="mark" id="mk">exact question</span></div>
   <div class="abs center lab" style="top:1330px;font-size:22px">salary: AmbitionBox / Levels.fyi ranges · illustration</div>`,
  draw(S) { const p = S.P(0, .5, back); S.$('#of').style.transform = `translateY(${120 * (1 - clamp(p))}px) rotate(${-3 + 3 * clamp(p)}deg)`; S.$('#of').style.opacity = clamp(p);
    COUNT(S, '#ct', 0, 28, .2, .9, v => '₹' + Math.round(v)); if (S.on(1.1)) S.sfx(1.1, 'ding'); const ta = TT(S, 'Amazon', .25); POP(S, '#ch', ta + .3, 'pop'); IN(S, '#q', TT(S, 'exact', .5) - .2); MK(S, '#mk', TT(S, 'question', .6)); }},
 { // 1 problem statement
  html: `<div class="abs center kick" style="top:420px">the question</div><div class="qcard" id="qc">Find the <b>longest part</b> of a string<br>with <b>no repeated letter</b>.</div>`,
  draw(S) { IN(S, '#qc', .05, 60); }},
 { // 2 example chaichai → 4
  html: `${ROW('r2', 620)}<div class="abs center big" id="an" style="top:900px;font-size:150px;color:var(--grn);opacity:0">= 4</div>`,
  draw(S) { S.$$('#r2 .b').forEach((b, i) => { const p = S.P(.05 + i * .07, .3, back); b.style.opacity = clamp(p); b.style.transform = `translateY(${40 * (1 - clamp(p))}px)`; });
    const tf = TT(S, 'four', .45); POP(S, '#an', tf, 'ding'); const k = ['C', 'H', 'A', 'I'].map((l, j) => TT(S, l, .6 + j * .08)); let n = -1; k.forEach((t, j) => { if (S.on(t - .05)) n = j; });
    LIT(S, 'r2', 0, n); FRAME(S, 'r2', 0, Math.max(0, n), 'var(--grn)', n >= 0 ? 1 : 0); }},
 { // 3 brute force rejected
  html: `${ROW('r3', 520)}<div class="abs center big" id="ck" style="top:820px;font-size:130px;color:var(--red)">0</div><div class="abs center lab" style="top:990px;font-size:40px">parts to check in a 5,000-letter string</div>
   <div class="stamp" id="rj" style="left:250px;top:1110px;font-size:110px">REJECTED</div>`,
  draw(S) { const k = Math.floor(S.t * 10), a = k % 8, b = Math.min(7, a + (k * 3) % 5); FRAME(S, 'r3', a, b, 'var(--red)', 1); if (k !== this.k) { S.sfx(S.t, 'tick'); this.k = k; }
    COUNT(S, '#ck', 0, 12502500, .3, TT(S, 'millions', .6) - .1, v => fmt(v), x => x * x * x); STAMP(S, '#rj', TT(S, 'Rejected', .9)); if (S.t > TT(S, 'Rejected', .9)) S.$('#r3 .frame').style.opacity = 0; }},
 { // 4 sliding window intro
  html: `<div class="abs center h" style="top:380px;font-size:110px"><span class="mark" id="mk">Sliding window</span></div>${ROW('r4', 700)}${PTR('pl', 'LEFT', '#ffd23f')}${PTR('pr', 'RIGHT', '#4c9dff')}`,
  draw(S) { MK(S, '#mk', TT(S, 'sliding', .3)); FRAME(S, 'r4', 0, 0, 'var(--grn)', S.on(TT(S, 'window', .45)) ? 1 : 0); PT(S, 'pl', 0, 880); PT(S, 'pr', 0, 990);
    S.$('#pl').style.opacity = S.P(TT(S, 'left', .8) - .1, .3); S.$('#pr').style.opacity = S.P(TT(S, 'right', .95) - .1, .3); }},
 { // 5 right grows to 4
  html: `${ROW('r5', 600)}${PTR('pl5', 'LEFT', '#ffd23f')}${PTR('pr5', 'RIGHT', '#4c9dff')}<div class="abs center big" id="sz" style="top:1120px;font-size:120px">window: 1</div>`,
  draw(S) { const ts = ['C', 'H', 'A', 'I'].map((l, j) => TT(S, l, .4 + j * .1)); let r = 0; ts.forEach((t, j) => { if (S.on(t - .1)) r = j; }); FRAME(S, 'r5', 0, r); LIT(S, 'r5', 0, r); PT(S, 'pl5', 0, 780); PT(S, 'pr5', r, 890);
    S.$('#sz').textContent = 'window: ' + (r + 1); S.$('#sz').style.color = r === 3 ? 'var(--grn)' : 'var(--paper)'; if (r !== this.r) { S.sfx(S.t, 'click'); this.r = r; } }},
 { // 6 repeat → left jumps
  html: `${ROW('r6', 600)}${PTR('pl6', 'LEFT', '#ffd23f')}${PTR('pr6', 'RIGHT', '#4c9dff')}<svg class="abs" width="1080" height="1500" style="left:0;top:0"><path id="arc" d="" stroke="#ffd23f" stroke-width="6" fill="none" stroke-dasharray="14 10"/></svg>
   <div class="abs center" id="rp" style="top:420px;font:900 90px Roboto;color:var(--red);opacity:0">REPEAT!</div>`,
  draw(S) { const tr = TT(S, 'Repeat', .35), tj = TT(S, 'jumps', .7); const rep = S.on(tr - .2), jp = S.P(tj - .2, .5, eio);
    const l = jp >= 1 ? 1 : 0; FRAME(S, 'r6', jp > 0 ? 1 : 0, 4, rep && jp < 1 ? 'var(--red)' : 'var(--grn)'); LIT(S, 'r6', 0, 3); S.$$('#r6 .b').forEach((b, i) => { b.classList.toggle('bad', rep && (i === 0 || i === 4) && jp < 1); b.classList.toggle('on', i >= (jp > 0 ? 1 : 0) && i <= (rep ? 4 : 3)); });
    PT(S, 'pr6', 4, 890); const lx = bx(0) + BW / 2 - 70 + jp * (BW + GAP); S.$('#pl6').style.left = lx + 'px'; S.$('#pl6').style.top = 780 - 60 * Math.sin(jp * Math.PI) + 'px';
    S.$('#arc').setAttribute('d', jp > 0 && jp < 1 ? `M${bx(0) + 52} 770 Q${bx(0) + 110} 640 ${bx(1) + 52} 770` : ''); POP(S, '#rp', tr - .2, 'buzz'); if (S.on(tj - .2)) S.sfx(tj - .2, 'whoosh'); }},
 { // 7 last-seen map
  html: `<div class="abs center h2" style="top:400px">last seen at…</div><div class="map">${['c', 'h', 'a', 'i'].map((c, i) => `<div class="mr" id="m${i}"><b>${c}</b><span>→</span><i id="mv${i}">${[0, 1, 2, 3][i]}</i></div>`).join('')}</div>
   <div class="abs center lab" id="ins" style="top:1280px;font-size:44px;opacity:0">jump = one lookup ⚡ instant</div>`,
  draw(S) { [0, 1, 2, 3].forEach(i => IN(S, '#m' + i, .2 + i * .15, 30)); const tl = TT(S, 'last', .45); S.$('#mv0').textContent = S.on(tl) ? '4' : '0'; S.$('#m0').classList.toggle('hl', S.on(tl)); if (S.on(tl)) S.sfx(tl, 'pop'); IN(S, '#ins', TT(S, 'instant', .85) - .2); }},
 { // 8 each letter once → O(n)
  html: `${ROW('r8', 560)}<div class="abs center big" id="tc" style="top:820px;font-size:90px">touched: 0 / 8</div><div class="abs center big" id="on" style="top:1020px;font-size:200px;color:var(--grn);opacity:0">O(n)</div>`,
  draw(S) { const n = Math.min(8, Math.floor(8 * S.P(.1, TT(S, 'once', .5), x => x) + .001)); LIT(S, 'r8', 0, n - 1); FRAME(S, 'r8', 0, 0, 'var(--grn)', 0); S.$('#tc').textContent = `touched: ${n} / 8`; if (n !== this.n) { S.sfx(S.t, 'click'); this.n = n; } POP(S, '#on', TT(S, 'O', .75) - .1, 'ding'); }},
 { // 9 notes CTA
  html: `<div class="abs center kick" style="top:420px">want 5 more like this?</div><div class="abs center" style="top:520px"><span class="notes">NOTES</span></div><div class="abs center h2" style="top:830px">comment it, get the list<br>with the same pattern</div>
   <div class="abs center" style="top:1160px"><span class="pill">Follow @tech.explained.dev</span></div>`,
  draw(S) { POP(S, '.notes', 0, 'pop'); S.$('.notes').style.transform += ` scale(${1 + .03 * Math.sin(S.t * 6)})`; }},
];
