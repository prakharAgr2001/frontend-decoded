// WR13: Knight Capital, 1 Aug 2012: ~$440M lost in 45 min (SEC 2013 order)
const RACK = i => `<div class="rack" id="r${i}"><div class="led"></div><div class="slot"></div><div class="slot"></div><div class="slot"></div><div class="rk">SERVER ${i + 1}</div><div class="badge"></div></div>`;
const SCENES = [
 { // 0 hook: money draining + clock
  html: `<div class="abs center kick" style="top:380px">lost in</div>
   <div class="abs center big" id="clk" style="top:440px;font-size:130px">00:00</div>
   <div class="abs center big" id="m" style="top:700px;font-size:120px;color:var(--red)">−$0</div>
   <div class="abs center h" id="oc" style="top:1000px;font-size:100px;opacity:0">because of <span class="mark" id="mk">old code</span></div>`,
  draw(S) { const tb = TT(S, 'Because', .6), p = S.P(0, tb, x => x); S.$('#m').textContent = '−$' + fmt(440e6 * eo(p)); const mn = Math.floor(45 * p);
    S.$('#clk').textContent = String(mn).padStart(2, '0') + ':' + String(Math.floor((45 * p * 60) % 60)).padStart(2, '0'); if (p < 1 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick');
    POP(S, '#oc', tb, 'thud'); MK(S, '#mk', TT(S, 'old', .8)); }},
 { // 1 deploy to eight servers
  html: `<div class="abs center kick" style="top:380px">August 2012 · deploy day</div><div class="racks">${[...Array(8)].map((_, i) => RACK(i)).join('')}</div>
   <div class="abs center" style="top:1330px"><span class="pill">NEW CODE ➜ 8 SERVERS</span></div>`,
  draw(S) { S.$$('.rack').forEach((r, i) => { const p = S.P(.2 + i * .12, .3, back); r.style.opacity = clamp(p); r.style.transform = `translateY(${40 * (1 - clamp(p))}px)`; if (S.on(.2 + i * .12)) S.sfx(.2 + i * .12, 'pop'); }); }},
 { // 2 seven get it, one doesn't
  html: `<div class="racks">${[...Array(8)].map((_, i) => RACK(i)).join('')}</div>`,
  draw(S) { const t1 = TT(S, 'One', .6); S.$$('.rack').forEach((r, i) => { const b = r.querySelector('.badge');
      if (i < 7) { const at = .1 + i * .1; b.textContent = S.on(at) ? '✓' : ''; b.className = 'badge g'; if (S.on(at)) S.sfx(at, 'click'); }
      else { b.textContent = S.on(t1) ? '✗' : ''; b.className = 'badge r'; r.style.boxShadow = S.on(t1) ? '0 0 0 4px var(--red),0 0 70px rgba(255,59,59,.5)' : ''; } });
    if (S.on(t1)) S.sfx(t1, 'buzz'); SHAKE(S, '#r7', t1); }},
 { // 3 reused switch wakes dead code
  html: `${WIN('server 8 · router.js', `<span class="k">if</span> (order.<span class="v">flag</span>) {\n  <span class="c">// new feature</span>\n  <span class="f">retailProgram</span>(order)  <span class="m">← missing</span>\n}\n\n<span class="c">// old code, unused since 2003</span>\n<span class="k">if</span> (order.<span class="v">flag</span>) <span class="f" id="pp">powerPeg</span>(order)`)}
   <div class="abs" id="sk" style="left:820px;top:1080px;font-size:150px;opacity:0">${EMO('skull')}</div>`,
  init(el) { el.querySelector('.win').style.top = '420px'; },
  draw(S) { const td = TT(S, 'dead', .8), tw = TT(S, 'woke', .6); const g = S.$('#pp'); g.style.background = S.on(tw) ? 'rgba(255,59,59,.35)' : ''; g.style.color = S.on(tw) ? '#fff' : '';
    if (S.on(tw)) S.sfx(tw, 'whoosh'); POP(S, '#sk', td - .2, 'thud'); }},
 { // 4 order storm
  html: `<div class="abs center kick" style="top:370px">orders / second</div><div class="tape" id="tp"></div><div class="abs center big" id="ops" style="top:1380px;font-size:90px;color:var(--yel)">0</div>`,
  draw(S) { const n = Math.floor(S.t * 22); let h = ''; for (let i = n; i > n - 14 && i >= 0; i--) { const b = i % 2 === 0; h += `<div class="ord ${b ? 'b' : 's'}"><b>${b ? 'BUY' : 'SELL'}</b><span>${['ABC', 'XYZ', 'QRS', 'MNO', 'DEF'][i % 5]}</span><span>${b ? 'HIGH ▲' : 'LOW ▼'}</span><span>${fmt(100 + R(i) * 900)}</span></div>`; }
    S.$('#tp').innerHTML = h; COUNT(S, '#ops', 0, 4000, 0, S.dur * .8); S.sfx(Math.floor(S.t * 22) / 22, 'tick'); }},
 { // 5 no kill switch
  html: `<div class="abs" id="ks" style="left:290px;top:420px;width:500px;height:500px;border-radius:50%;background:radial-gradient(#5a1a1a,#2a0e0e);box-shadow:0 0 0 18px #333;display:flex;align-items:center;justify-content:center;font:900 64px Roboto;color:#777;text-align:center">KILL<br>SWITCH</div>
   <div class="abs" id="x" style="left:290px;top:400px;width:500px;text-align:center;font:900 520px/1 Roboto;color:var(--red);opacity:0">✗</div>
   <div class="abs center big" id="tm" style="top:1030px;font-size:110px">45 min</div>
   <div class="stamp" id="gone" style="left:230px;top:1200px;font-size:100px">−$440M</div>`,
  draw(S) { POP(S, '#x', TT(S, 'switch', .2), 'buzz', 1.3); POP(S, '#tm', TT(S, '45', .45), 'tick'); STAMP(S, '#gone', TT(S, 'gone', .85), -6); }},
 { // 6 lesson checklist
  html: `<div class="abs center h2" style="top:400px">the lesson</div>
   <div class="tile chk" id="c1" style="left:110px;right:110px;top:560px;height:200px"><b>✓</b>Delete dead code</div>
   <div class="tile chk" id="c2" style="left:110px;right:110px;top:810px;height:200px"><b>✓</b>Verify every server got the deploy</div>`,
  draw(S) { IN(S, '#c1', TT(S, 'Delete', .1) - .1); IN(S, '#c2', TT(S, 'check', .5) - .1); if (S.on(TT(S, 'Delete', .1))) S.sfx(TT(S, 'Delete', .1), 'ding'); if (S.on(TT(S, 'check', .5))) S.sfx(TT(S, 'check', .5), 'ding'); }},
 ctaScene(),
];
