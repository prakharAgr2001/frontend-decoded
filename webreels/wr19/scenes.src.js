// WR19: GPS week-number rollover (10-bit week counter: 1999 and 6 April 2019)
const GPSDEV = `<div class="gps"><div class="scr"><div class="lab" style="color:#9fb">GPS · DATE</div><div class="dd" id="dd">06 Apr 2019</div><div class="lab" id="wk" style="color:#9fb">week 1023</div></div></div>`;
const SAT = `<svg viewBox="0 0 200 100" width="260"><rect x="80" y="30" width="40" height="40" rx="6" fill="#d9d4c7"/><rect x="5" y="40" width="70" height="20" fill="#4c9dff"/><rect x="125" y="40" width="70" height="20" fill="#4c9dff"/></svg>`;
const SCENES = [
 { // 0 hook
  html: `${GPSDEV}<div class="abs center h" style="top:1040px;font-size:90px">jumped back<br><span class="mark" id="mk">nearly 20 years</span></div>`,
  draw(S) { const tj = TT(S, 'jumped', .3); const j = S.on(tj + .2); S.$('#dd').textContent = j ? '22 Aug 1999' : '06 Apr 2019'; S.$('#wk').textContent = j ? 'week 0' : 'week 1023';
    S.$('#dd').style.color = j ? 'var(--red)' : '#dfffe8'; if (S.on(tj + .2)) S.sfx(tj + .2, 'thud'); SHAKE(S, '.gps', tj + .2); MK(S, '#mk', TT(S, 'nearly', .6)); }},
 { // 1 satellites count weeks in 10 bits
  html: `<div class="abs" id="st" style="left:410px;top:420px">${SAT}</div><div class="abs center kick" style="top:640px">week counter</div>
   <div class="abs center" style="top:720px">${SWITCHES(10, 5)}</div><div class="abs center h2" style="top:1050px">just <span class="mark" id="mk">10 bits</span></div>`,
  draw(S) { S.$('#st').style.transform = `translateY(${10 * Math.sin(S.t * 2)}px)`; MK(S, '#mk', TT(S, '10', .6)); SETSW(S, Math.round(10 * S.P(TT(S, '10', .6), 1, x => x))); }},
 { // 2 counts to 1023 then zero
  html: `<div class="abs center" style="top:480px">${SWITCHES(10, 5)}</div><div class="abs center big" id="n" style="top:850px;font-size:200px">0</div>`,
  draw(S) { const tz = TT(S, 'zero', .8), p = S.P(0, tz - .4, x => x); const v = S.on(tz - .2) ? 0 : Math.round(1023 * p);
    S.$$('.sw').forEach((s, i) => s.classList.toggle('on', (v >> (9 - i)) & 1)); S.$('#n').textContent = fmt(v); S.$('#n').style.color = v === 1023 ? 'var(--yel)' : S.on(tz - .2) ? 'var(--red)' : 'var(--paper)';
    if (S.on(tz - .2)) S.sfx(tz - .2, 'thud'); else if (Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick'); }},
 { // 3 timeline
  html: `<div class="abs center kick" style="top:420px">1,024 weeks ≈ 19.6 years</div><div class="tl"><i id="ln"></i>
   ${[['1980', 'start', 0], ['1999', 'reset 1', 50], ['2019', 'reset 2', 100]].map((d, i) => `<div class="tp" id="p${i}" style="left:${d[2]}%"><b>${d[0]}</b><span>${d[1]}</span></div>`).join('')}</div>`,
  draw(S) { S.$('#ln').style.width = 100 * S.P(0, S.dur - .5, eio) + '%'; [0, 1, 2].forEach(i => POP(S, '#p' + i, i === 0 ? 0 : i === 1 ? TT(S, '1999', .6) - .2 : S.dur - .5, 'pop')); }},
 { // 4 6 April 2019
  html: `<div class="cal"><div class="ch">APRIL 2019</div><div class="cday" id="cd">6</div></div><div class="abs center big" id="w" style="top:1150px;font-size:120px">week 1023</div>`,
  draw(S) { const tr = TT(S, 'reset', .7); S.$('#w').textContent = S.on(tr) ? 'week 0' : 'week 1023'; S.$('#w').style.color = S.on(tr) ? 'var(--red)' : 'var(--paper)'; if (S.on(tr)) S.sfx(tr, 'thud'); POP(S, '.cal', 0, 'pop'); }},
 { // 5 devices show 1999
  html: `${GPSDEV}<div class="abs center" style="top:1040px;font:800 60px Roboto;color:var(--red)">${EMO('warning')} wrong date</div>`,
  draw(S) { S.$('#dd').textContent = '22 Aug 1999'; S.$('#dd').style.color = 'var(--red)'; S.$('#wk').textContent = 'week 0'; S.$('.scr').style.opacity = .7 + .3 * Math.sin(S.t * 18); if (S.t < .1) S.sfx(0, 'buzz'); }},
 { // 6 13 bits
  html: `<div class="abs center kick" style="top:420px">newer GPS signals</div><div class="abs center" style="top:520px">${SWITCHES(13, 7)}</div>
   <div class="abs center h2" style="top:960px"><span class="mark" id="mk">13 bits</span></div><div class="abs center big" id="y" style="top:1120px;font-size:130px;color:var(--grn)">0 years</div>`,
  draw(S) { MK(S, '#mk', TT(S, '13', .3)); SETSW(S, Math.round(13 * S.P(TT(S, '13', .3), 1, x => x))); COUNT(S, '#y', 0, 157, TT(S, '157', .7) - .6, .8, v => '~' + Math.round(v) + ' years'); }},
 ctaScene(),
];
