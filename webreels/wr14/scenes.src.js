// WR14: England, Sep-Oct 2020: ~16,000 positive cases missed, old .XLS row limit (65,536 rows)
const GRID = (rows, top, h = 760) => `<div class="sheet" style="top:${top}px;height:${h}px"><div class="sh-h"><span></span>${'ABCDE'.split('').map(c => `<span>${c}</span>`).join('')}</div>
  <div class="sh-b">${rows.map(r => `<div class="sh-r ${r[1] || ''}"><span>${r[0]}</span>${[0, 1, 2, 3, 4].map(j => `<span>${r[2] ? r[2][j] || '' : ''}</span>`).join('')}</div>`).join('')}</div></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="n" style="top:380px;font-size:190px;color:var(--red)">0</div>
   <div class="abs center h2" style="top:600px">Covid cases <span class="mark" id="mk">went missing</span></div>
   ${GRID([...Array(8)].map((_, i) => [65529 + i, '', ['+', 'lab', 'pos', '…', '']]), 800, 560)}
   <div class="abs center lab" id="cause" style="top:1420px;font-size:40px;opacity:0">because of a spreadsheet file</div>`,
  draw(S) { COUNT(S, '#n', 0, 16000, 0, 1.4); MK(S, '#mk', TT(S, 'missing', .3)); IN(S, '#cause', TT(S, 'Because', .6)); if (S.t < 1.4 && Math.floor(S.t * 14) % 2) S.sfx(S.t, 'tick'); }},
 { // 1 CSV files into Excel templates
  html: `<div class="abs center kick" style="top:380px">2020 · England</div>
   ${[0, 1, 2, 3].map(i => `<div class="file" id="f${i}" style="top:${520 + i * 110}px">lab_results_${i + 1}.csv</div>`).join('')}
   <div class="tile tpl" style="left:620px;top:560px;width:360px;height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:150px;color:var(--grn)">▦</div><div class="lab">template</div></div>`,
  draw(S) { S.$$('.file').forEach((f, i) => { const at = .2 + i * .35, p = S.P(at, .6, eio); f.style.transform = `translateX(${480 * p}px) scale(${1 - .5 * p})`; f.style.opacity = 1 - p; if (S.on(at)) S.sfx(at, 'whoosh'); }); }},
 { // 2 the XLS limit
  html: `<div class="abs center" style="top:370px"><span class="pill" style="background:var(--red);color:#fff">.XLS · a format from 1987</span></div>
   ${GRID([...Array(8)].map((_, i) => [65529 + i, i === 7 ? 'last' : '']), 480, 720)}
   <div class="abs center num" id="mx" style="top:1260px;color:var(--yel)">max 65,536 rows</div>`,
  draw(S) { const b = S.$('.sh-b'); b.style.transform = `translateY(${-30 * (1 - S.P(0, .8))}px)`; POP(S, '#mx', TT(S, 'Max', .5), 'thud'); }},
 { // 3 rows per case
  html: `<div class="abs center h2" style="top:400px">each test = many rows</div>
   <div class="abs center big" style="top:600px;font-size:110px">65,536 rows</div><div class="abs center" style="top:760px;font-size:80px;color:var(--mute)">↓</div>
   <div class="abs center big" id="c" style="top:880px;font-size:150px;color:var(--yel)">≈ 1,400</div><div class="abs center h2" style="top:1060px">cases per file</div>`,
  draw(S) { POP(S, '#c', TT(S, '1400', .4), 'ding'); }},
 { // 4 cut off silently
  html: `${GRID([...Array(10)].map((_, i) => [i < 5 ? 65532 + i : '—', i < 5 ? '' : 'cut', i < 5 ? [] : ['case', 'positive', 'lab', '', '']]), 420, 800)}
   <div class="stamp g" id="ok" style="left:260px;top:1270px;font-size:60px">✓ SAVED · NO ERROR</div>`,
  draw(S) { const tc = TT(S, 'Cut', .25); S.$$('.sh-r.cut').forEach((r, i) => { const p = S.P(tc + i * .1, .5, eio); r.style.transform = `translate(${-40 * p}px,${300 * p}px) rotate(${-8 * p}deg)`; r.style.opacity = 1 - p; });
    if (S.on(tc)) S.sfx(tc, 'swish'); STAMP(S, '#ok', TT(S, 'error', .8), -4); }},
 { // 5 missed the count
  html: `<div class="abs center kick" style="top:380px">daily positive cases · reported vs real</div>
   <div class="bars">${[...Array(8)].map((_, i) => `<div class="bc"><i class="real" style="height:${40 + i * 7}%"></i><i class="rep" style="height:${(40 + i * 7) * (i > 2 ? .6 : 1)}%"></i></div>`).join('')}</div>
   <div class="abs center big" id="mi" style="top:1290px;font-size:110px;color:var(--red)">0 missed</div>`,
  draw(S) { S.$$('.bc').forEach((b, i) => { const p = S.P(i * .1, .4, eo); b.style.transform = `scaleY(${p})`; b.querySelector('.real').style.opacity = S.on(TT(S, 'missed', .4)) ? 1 : 0; });
    COUNT(S, '#mi', 0, 15841, TT(S, 'missed', .4), 1.2, v => fmt(v) + ' missed'); }},
 { // 6 the bug
  html: `<div class="abs center h" style="top:470px;font-size:100px">The bug:</div><div class="abs center h" style="top:610px;font-size:100px"><span class="mark" id="mk">a hard limit</span></div>
   <div class="abs center h2" id="nb" style="top:780px;opacity:0">nobody checked.</div>
   <div class="abs" style="left:110px;right:110px;top:1050px;height:10px;background:var(--red);box-shadow:0 0 40px var(--red);border-radius:5px"></div>`,
  draw(S) { MK(S, '#mk', TT(S, 'hard', .2)); POP(S, '#nb', TT(S, 'nobody', .6), 'thud'); }},
 ctaScene(),
];
