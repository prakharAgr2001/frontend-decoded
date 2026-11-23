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
// WR29: Zune 30GB leap-year freeze, 31 Dec 2008 (clock-driver loop never ends on day 366). Generic player drawn, no product design copied.
const PLAYER = `<div class="pl"><div class="scr" id="sc"><div class="ld"><i></i><i></i><i></i></div><span>loading…</span></div><div class="wheel"></div></div>`;
const CODE = `<span class="k">while</span> (days > 365) {
  <span class="k">if</span> (<span class="f">isLeap</span>(year)) {
    <span class="k">if</span> (days > 366) {
      days -= 366; year++
    }
    <span class="c" id="c1">// days == 366 ? nothing.</span>
  } <span class="k">else</span> {
    days -= 365; year++
  }
}`;
const SCENES = [
 { // 0 hook: many players frozen
  html: `<div class="abs center kick" style="top:380px">31 December 2008</div><div class="grid">${[...Array(12)].map(() => `<div class="mini"><div class="ms2"></div></div>`).join('')}</div>`,
  draw(S) { const tf = TT(S, 'froze', .4); S.$$('.mini').forEach((m, i) => { const f = S.on(tf + i * .04); m.classList.toggle('fz', f); }); if (S.on(tf)) S.sfx(tf, 'thud'); if (S.t > tf && S.t < tf + .08) flash(.4); }},
 { // 1 stuck on loading
  html: `${PLAYER}<div class="abs center lab" style="top:1380px;font-size:40px">30 GB model · stuck</div>`,
  draw(S) { S.$$('.ld i').forEach((d, i) => d.style.opacity = .3 + .7 * (Math.floor(S.t * 3) % 3 === i)); }},
 { // 2 loop code
  html: `${WIN('clock_driver.c (simplified)', CODE)}`,
  init(el) { el.querySelector('.win').style.top = '420px'; el.querySelector('.wb').style.fontSize = '34px'; },
  draw(S) {}},
 { // 3 day 366
  html: `<div class="abs center kick" style="top:400px">2008 was a leap year</div><div class="abs center big" id="d" style="top:500px;font-size:220px">day 360</div>
   <div class="rules"><div class="rule" id="r1">days > 366 ? <b>no</b></div><div class="rule" id="r2">days > 365 ? <b>yes, keep looping</b></div></div>`,
  draw(S) { const t = TT(S, '366', .5), n = Math.min(366, 360 + Math.floor(6 * S.P(0, t, x => x))); S.$('#d').textContent = 'day ' + n; S.$('#d').style.color = n === 366 ? 'var(--red)' : 'var(--paper)'; IN(S, '#r1', t + .2); IN(S, '#r2', t + .6); }},
 { // 4 infinite loop
  html: `<svg class="abs" style="left:290px;top:480px" width="500" height="500" viewBox="0 0 100 100"><circle cx="50" cy="50" r="38" fill="none" stroke="#2a2a31" stroke-width="8"/><circle id="sp" cx="50" cy="50" r="38" fill="none" stroke="#ff3b3b" stroke-width="8" stroke-dasharray="60 180" stroke-linecap="round"/></svg>
   <div class="abs center big" style="top:640px;font-size:150px">∞</div><div class="abs center big" id="it" style="top:1080px;font-size:80px;color:var(--mute)">loop #0</div>`,
  draw(S) { S.$('#sp').setAttribute('transform', `rotate(${S.t * 720} 50 50)`); S.$('#it').textContent = 'loop #' + fmt(Math.pow(10, 1 + 5 * S.t / S.dur)); if (Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); }},
 { // 5 wait until tomorrow
  html: `<div class="cal"><div class="ch">DEC 2008</div><div class="cday" id="cd">31</div></div><div class="abs center h2" id="w" style="top:1150px;opacity:0">official fix: <span class="mark" id="mk">wait</span></div>`,
  draw(S) { const tt = TT(S, 'tomorrow', .7); IN(S, '#w', TT(S, 'fix', .3)); MK(S, '#mk', TT(S, 'Wait', .5)); const n = S.on(tt); S.$('#cd').textContent = n ? '1' : '31'; S.$('.ch').textContent = n ? 'JAN 2009' : 'DEC 2008'; if (S.on(tt)) S.sfx(tt, 'ding'); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:470px;font-size:96px">One missing<br><span class="mark" id="mk">edge case</span></div><div class="abs center h2" id="l2" style="top:820px;opacity:0">every device · same day</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'edge', .3)); IN(S, '#l2', TT(S, 'Every', .6) - .2); }},
 ctaScene(),
];
