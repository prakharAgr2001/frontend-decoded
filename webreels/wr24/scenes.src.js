// WR24: Pokémon GO launch (July 2016): traffic 50x target, 10x worst-case estimate (Google Cloud blog). No game characters drawn.
const BARS = `<div class="chart"><div class="col"><i id="b1"></i><span>target</span></div><div class="col"><i id="b5"></i><span>worst case</span></div><div class="col"><i id="b50"></i><span>actual</span></div></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="x" style="top:380px;font-size:260px;color:var(--red)">1x</div>
   <div class="abs center h2" style="top:680px">more players <span class="mark" id="mk">than planned</span></div>
   <div class="crowd" id="cr">${[...Array(150)].map(() => '<i></i>').join('')}</div>`,
  draw(S) { const p = S.P(0, TT(S, 'planned', .5), x => x); S.$('#x').textContent = Math.max(1, Math.round(50 * p)) + 'x'; MK(S, '#mk', TT(S, 'planned', .5));
    S.$$('#cr i').forEach((d, i) => d.style.opacity = i < 150 * p ? 1 : .08); if (p < 1 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick'); }},
 { // 1 launch
  html: `<div class="abs center kick" style="top:420px">July 2016</div><div class="phoneg"><div class="map"></div><div class="pin" id="pn"></div><div class="lbl">LAUNCH DAY</div></div>`,
  draw(S) { const p = S.P(0, .5, back); S.$('.phoneg').style.transform = `scale(${.8 + .2 * clamp(p)})`; S.$('.phoneg').style.opacity = clamp(p); S.$('#pn').style.transform = `translateY(${-20 * Math.abs(Math.sin(S.t * 4))}px)`; if (S.t < .1) S.sfx(0, 'whoosh'); }},
 { // 2 plan 1x / 5x
  html: `<div class="abs center h2" style="top:380px">the plan</div>${BARS}`,
  draw(S) { const t1 = TT(S, '1x', .3), t5 = TT(S, '5x', .75); S.$('#b1').style.height = 1.6 * S.P(t1 - .2, .4, eo) + '%'; S.$('#b5').style.height = 8 * S.P(t5 - .2, .4, eo) + '%'; S.$('#b50').style.height = '0%'; }},
 { // 3 15 minutes
  html: `<div class="abs center big" id="tm" style="top:420px;font-size:200px">00:00</div><div class="abs center lab" style="top:700px;font-size:40px">after launch</div>
   <div class="abs" style="left:110px;right:110px;top:860px;height:50px;border-radius:25px;background:#2a2a31;overflow:hidden"><div id="b" style="height:100%;background:var(--yel)"></div></div>
   <div class="abs lab" style="left:110px;top:930px">0</div><div class="abs lab" style="right:110px;top:930px;color:var(--grn)">target</div><div class="stamp" id="st" style="left:300px;top:1050px">PASSED</div>`,
  draw(S) { const p = S.P(0, S.dur - .5, x => x), m = 15 * p; S.$('#tm').textContent = String(Math.floor(m)).padStart(2, '0') + ':' + String(Math.floor(m * 60) % 60).padStart(2, '0');
    S.$('#b').style.width = Math.min(100, 110 * p) + '%'; if (Math.floor(S.t * 8) % 2) S.sfx(S.t, 'tick'); STAMP(S, '#st', S.dur - .5); }},
 { // 4 50x
  html: `<div class="abs center h2" style="top:380px">reality</div>${BARS}<div class="abs center big" id="tx" style="top:1360px;font-size:90px;color:var(--red);opacity:0">10x the worst case</div>`,
  init(el) { el.querySelector('#b1').style.height = '1.6%'; el.querySelector('#b5').style.height = '8%'; },
  draw(S) { const t = TT(S, '50x', .2), p = S.P(t - .2, .9, eo); S.$('#b50').style.height = 80 * p + '%'; if (S.on(t - .2)) S.sfx(t - .2, 'whoosh'); if (S.t > t + .7 && S.t < t + .8) flash(.5); SHAKE(S, '.chart', t + .7); POP(S, '#tx', TT(S, 'Ten', .7) - .1, 'thud'); }},
 { // 5 errors
  html: `<div class="errs">${[...Array(8)].map((_, i) => `<div class="err" style="top:${430 + i * 120}px;left:${120 + (i % 3) * 40}px">${['Unable to log in', 'Server busy, try again', 'Connection error', 'Unable to log in', 'Please wait…', 'Server busy, try again', 'Connection error', 'Unable to log in'][i]}</div>`).join('')}</div>`,
  draw(S) { S.$$('.err').forEach((e, i) => { const at = i * .28; const p = S.P(at, .25, back); e.style.opacity = clamp(p); e.style.transform = `scale(${.8 + .2 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'buzz'); }); }},
 { // 6 adding machines
  html: `<div class="abs center kick" style="top:400px">servers</div><div class="srvg">${[...Array(84)].map(() => '<i></i>').join('')}</div><div class="abs center big" id="n" style="top:1320px;font-size:100px;color:var(--grn)">+0</div>`,
  draw(S) { const n = Math.floor(84 * S.P(.2, S.dur - .6, x => x)); S.$$('.srvg i').forEach((d, i) => d.classList.toggle('on', i < n)); S.$('#n').textContent = 'adding machines…'; if (n !== this.n && n % 4 === 0) S.sfx(S.t, 'pop'); this.n = n; }},
 { // 7 lesson
  html: `<div class="abs center h" style="top:470px;font-size:84px">Plan for the<br><span class="mark" id="mk">worst case</span></div><div class="abs center h2" id="l2" style="top:800px;opacity:0">then build so you can<br>grow past it.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'worst', .2)); IN(S, '#l2', TT(S, 'build', .6) - .2); }},
 ctaScene(),
];
