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
