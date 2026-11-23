// WR26: WhatsApp at acquisition (2014): ~450M users, ~32 engineers, Erlang, ~2M connections per server
const PPL = n => `<div class="ppl">${[...Array(n)].map(() => '<i></i>').join('')}</div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="u" style="top:360px;font-size:170px;color:var(--grn)">0</div><div class="abs center lab" style="top:560px;font-size:44px">users</div>
   <div class="abs center h2" id="w" style="top:700px;opacity:0">with just <span class="mark" id="mk">32 engineers</span></div>${PPL(32)}`,
  draw(S) { COUNT(S, '#u', 0, 450e6, 0, 1.6, v => fmt(v)); if (S.t < 1.6 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick'); const t = TT(S, '32', .6); IN(S, '#w', t - .3); MK(S, '#mk', t);
    S.$$('.ppl i').forEach((d, i) => { d.style.opacity = S.on(t + i * .03) ? 1 : 0; }); }},
 { // 1 19 billion
  html: `<div class="abs center kick" style="top:440px">2014 · Facebook buys WhatsApp</div><div class="abs center big" id="b" style="top:560px;font-size:200px;color:var(--yel)">$0B</div>`,
  draw(S) { COUNT(S, '#b', 0, 19, .2, 1, v => '$' + Math.round(v) + 'B'); if (S.on(1.2)) S.sfx(1.2, 'ding'); }},
 { // 2 Erlang
  html: `<div class="abs center kick" style="top:400px">the secret</div><div class="abs center h" style="top:480px;font-size:150px"><span class="mark" id="mk">Erlang</span></div>
   <div class="tile" id="sw" style="left:190px;right:190px;top:780px;height:420px;padding:40px;opacity:0"><div class="lab">built for</div><div class="jacks">${[...Array(24)].map(() => '<i></i>').join('')}</div><div class="lab" style="text-align:center;margin-top:20px">telephone switches</div></div>`,
  draw(S) { MK(S, '#mk', TT(S, 'Erlang', .3)); IN(S, '#sw', TT(S, 'telephone', .7) - .3); S.$$('.jacks i').forEach((j, i) => j.classList.toggle('on', R(i + Math.floor(S.t * 4)) > .5)); }},
 { // 3 2M connections per server
  html: `<div class="tile" style="left:390px;top:840px;width:300px;height:360px;display:flex;align-items:center;justify-content:center;font:800 40px Roboto;box-shadow:0 0 0 4px var(--yel)">1 SERVER</div>
   <svg id="cn" class="abs" width="1080" height="1500" style="left:0;top:0"></svg><div class="abs center big" id="n" style="top:400px;font-size:140px">0</div><div class="abs center lab" style="top:560px;font-size:40px">connections at once</div>`,
  draw(S) { const p = S.P(0, S.dur - .4, eo); S.$('#n').textContent = fmt(2e6 * p); let h = ''; const k = Math.floor(120 * p);
    for (let i = 0; i < k; i++) { const a = R(i) * Math.PI * 2, r = 300 + R(i + 9) * 110; const x = 540 + Math.cos(a) * r, y = 1020 + Math.sin(a) * r * .75; h += `<line x1="540" y1="1020" x2="${x}" y2="${y}" stroke="#3ddc84" stroke-opacity=".35" stroke-width="2"/><circle cx="${x}" cy="${y}" r="7" fill="#3ddc84"/>`; }
    S.$('#cn').innerHTML = h; if (Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); }},
 { // 4 fewer x3
  html: `${['servers', 'engineers', 'things to break'].map((w, i) => `<div class="few" id="f${i}" style="top:${470 + i * 250}px">Fewer <span>${w}</span></div>`).join('')}`,
  draw(S) { ['servers', 'engineers', 'things'].forEach((w, i) => { const t = TT(S, w, .2 + i * .3); IN(S, '#f' + i, t - .3, 40); if (S.on(t - .3)) S.sfx(t - .3, 'pop'); }); }},
 { // 5 14M per engineer
  html: `<div class="abs" style="left:440px;top:480px;font-size:200px">${EMO('robot')}</div><div class="abs center lab" style="top:740px;font-size:40px">1 engineer</div>
   <div class="abs center big" id="n" style="top:860px;font-size:150px;color:var(--grn)">0</div><div class="abs center lab" style="top:1040px;font-size:40px">users each</div>`,
  draw(S) { COUNT(S, '#n', 0, 14e6, TT(S, '14', .3) - .4, 1, v => '~' + fmt(v)); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:520px;font-size:96px">The <span class="mark" id="mk">right tool</span><br>can replace<br>a whole team.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'right', .2)); }},
 ctaScene(),
];
