// WR30: Instagram acquisition, April 2012: 13 employees, $1B, ~30M users. No logos.
const PPL = n => `<div class="ppl">${[...Array(n)].map(() => '<i></i>').join('')}</div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="n" style="top:360px;font-size:220px">0</div><div class="abs center lab" style="top:620px;font-size:44px">employees</div>${PPL(13)}
   <div class="abs center big" id="b" style="top:1180px;font-size:130px;color:var(--grn);opacity:0">$1,000,000,000</div>`,
  draw(S) { const n = Math.min(13, Math.floor(13 * S.P(.1, 1.2, x => x) + .001)); S.$('#n').textContent = n; S.$$('.ppl i').forEach((d, i) => d.style.opacity = i < n ? 1 : 0); if (n !== this.n) S.sfx(S.t, 'pop'); this.n = n;
    POP(S, '#b', TT(S, 'billion', .7) - .3, 'ding'); }},
 { // 1 30M users
  html: `<div class="abs center kick" style="top:420px">April 2012</div><div class="abs center big" id="u" style="top:520px;font-size:170px">0</div><div class="abs center lab" style="top:720px;font-size:44px">users</div>
   <div class="feed">${[...Array(15)].map((_, i) => `<i style="background:hsl(${R(i) * 360},45%,${45 + R(i + 3) * 20}%)"></i>`).join('')}</div>`,
  draw(S) { COUNT(S, '#u', 0, 30e6, 0, S.dur - .4, v => '~' + fmt(v)); S.$$('.feed i').forEach((d, i) => d.style.opacity = S.on(i * .1) ? 1 : 0); }},
 { // 2 no giant team: small team + simple tools
  html: `<div class="abs center h2" style="top:400px">no giant team</div>
   <div class="stack">${['Web app', 'Database', 'Cache', 'Photo storage'].map((x, i) => `<div class="blk" id="k${i}">${x}</div>`).join('')}</div><div class="abs center lab" style="top:1300px;font-size:40px">simple, proven tools</div>`,
  draw(S) { const t = TT(S, 'simple', .5); [0, 1, 2, 3].forEach(i => { IN(S, '#k' + i, t - .4 + i * .2, 40); if (S.on(t - .4 + i * .2)) S.sfx(t - .4 + i * .2, 'pop'); }); }},
 { // 3 rule
  html: `<div class="tile" id="rl" style="left:110px;right:110px;top:560px;height:400px;display:flex;align-items:center;justify-content:center;text-align:center;font:800 86px/1.2 Roboto;box-shadow:0 0 0 5px var(--yel)">Do the simple<br>thing first.</div>`,
  draw(S) { POP(S, '#rl', TT(S, 'simple', .5) - .2, 'thud'); }},
 { // 4 add servers as you grow
  html: `<div class="abs center kick" style="top:400px">users ↑ · servers ↑</div><div class="srvg">${[...Array(48)].map(() => '<i></i>').join('')}</div>
   <div class="abs center lab" id="fx" style="top:1200px;font-size:44px;opacity:0">${EMO('pushpin')} fix what actually breaks</div>`,
  draw(S) { const n = Math.floor(48 * S.P(0, TT(S, 'Fix', .6), x => x)); S.$$('.srvg i').forEach((d, i) => d.classList.toggle('on', i < n)); IN(S, '#fx', TT(S, 'Fix', .6) - .1); if (n !== this.n && n % 4 === 0) S.sfx(S.t, 'click'); this.n = n; }},
 { // 5 13 people, billion
  html: `${PPL(13)}<div class="abs center h" style="top:440px;font-size:110px">13 people</div><div class="abs center h" id="ba" style="top:1180px;font-size:100px;opacity:0"><span class="mark" id="mk">$1B app</span></div>`,
  init(el) { el.querySelectorAll('.ppl i').forEach(i => i.style.opacity = 1); },
  draw(S) { const t = TT(S, 'billion', .6); POP(S, '#ba', t - .2, 'ding'); MK(S, '#mk', t); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:520px;font-size:96px"><span class="mark" id="mk">Simple</span> scales<br>further than<br>you think.</div>`,
  draw(S) { MK(S, '#mk', .1); }},
 ctaScene(),
];
