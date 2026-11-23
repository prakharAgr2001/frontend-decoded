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
// WR27: leap second, 30 June 2012: Linux kernel bug -> CPU spin; Reddit, LinkedIn affected; Amadeus Altea (Qantas/Virgin Australia) manual check-in
const CLK = `<div class="clk2"><span id="hh">23:59:</span><span id="ss">58</span></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" style="top:380px;font-size:200px">+1 sec</div>
   <div class="sites">${['reddit', 'LinkedIn', 'airline'].map((s, i) => `<div class="site" id="w${i}"><b>${s}</b><span class="x">DOWN</span></div>`).join('')}</div>`,
  draw(S) { [TT(S, 'Reddit', .4), TT(S, 'LinkedIn', .6), TT(S, 'airline', .85)].forEach((t, i) => { const d = S.on(t); S.$('#w' + i).classList.toggle('dn', d); if (S.on(t)) S.sfx(t, 'thud'); }); }},
 { // 1 23:59:60
  html: `<div class="abs center kick" style="top:420px">30 June 2012 · UTC</div>${CLK}<div class="abs center lab" style="top:1000px;font-size:40px">a minute with 61 seconds</div>`,
  draw(S) { const k = Math.min(3, Math.floor(S.P(0, S.dur - .4, x => x) * 4)); const s = ['58', '59', '60', '00'][k]; S.$('#ss').textContent = s; S.$('#ss').style.color = s === '60' ? 'var(--red)' : 'var(--grn)'; S.$('#hh').textContent = s === '00' ? '00:00:' : '23:59:';
    if (k !== this.k) S.sfx(S.t, s === '60' ? 'thud' : 'tick'); this.k = k; }},
 { // 2 linux bug
  html: `${WIN('kernel', `<span class="m">clock:</span> inserting leap second\n<span class="r">timer: confused</span>\n<span class="r">threads: waking up… again… again…</span>`)}`,
  init(el) { el.querySelector('.win').style.top = '520px'; },
  draw(S) { SHAKE(S, '.win', .6, 8, 1.5); if (S.t < .1) S.sfx(0, 'buzz'); }},
 { // 3 100% CPU doing nothing
  html: `<div class="cpus">${[...Array(6)].map((_, i) => `<div class="cpu"><div class="lab">CPU ${i + 1}</div><div class="bar"><i></i></div><b>0%</b></div>`).join('')}</div><div class="abs center h2" id="dn" style="top:1250px;opacity:0">…doing nothing</div>`,
  draw(S) { const t = TT(S, '100', .45); S.$$('.cpu').forEach((c, i) => { const v = Math.min(100, 8 + 92 * S.P(i * .06, t, eo)); c.querySelector('i').style.width = v + '%'; c.querySelector('b').textContent = Math.round(v) + '%'; c.querySelector('i').style.background = v > 95 ? 'var(--red)' : 'var(--yel)'; });
    IN(S, '#dn', TT(S, 'nothing', .85) - .2); }},
 { // 4 airline manual check-in
  html: `<div class="board"><div class="bh">DEPARTURES</div>${['SYD 07:10', 'MEL 07:25', 'BNE 07:40', 'PER 08:05'].map((f, i) => `<div class="fr"><span>${f}</span><b id="f${i}">ON TIME</b></div>`).join('')}</div>
   <div class="abs center" id="mn" style="top:1180px;font:800 60px Roboto;opacity:0">${EMO('warning')} check-in: manual</div>`,
  draw(S) { const tm = TT(S, 'manual', .3), td = TT(S, 'delayed', .8); POP(S, '#mn', tm - .2, 'buzz'); [0, 1, 2, 3].forEach(i => { const d = S.on(td - .3 + i * .15); S.$('#f' + i).textContent = d ? 'DELAYED' : 'ON TIME'; S.$('#f' + i).style.color = d ? 'var(--red)' : 'var(--grn)'; if (S.on(td - .3 + i * .15)) S.sfx(td - .3 + i * .15, 'click'); }); }},
 { // 5 smear
  html: `<div class="abs center kick" style="top:420px">today: leap smear</div><div class="smear"><div class="lab">spike: +1 s at midnight</div><div class="sp" id="sp"></div><div class="lab" style="margin-top:60px">smear: tiny slow-down all day</div><div class="sm" id="sm"></div></div>`,
  draw(S) { const p = S.P(TT(S, 'smear', .5) - .3, 1.2, eio); S.$('#sm').style.width = 100 * p + '%'; S.$('#sp').style.opacity = 1 - .6 * p; }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:520px;font-size:96px"><span class="mark" id="mk">Time</span> is the<br>hardest bug<br>in computing.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'Time', .1)); }},
 ctaScene(),
];
