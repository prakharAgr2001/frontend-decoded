// WR32: Pixar Toy Story 2 near-deletion (1998), saved from a technical director's home computer. No characters, logos or film imagery drawn: only generic files.
const FILES = ['scene_014/', 'scene_015/', 'models/', 'textures/', 'lighting/', 'shots/', 'sets/', 'animation/', 'renders/', 'sound/'];
const SCENES = [
 { // 0 hook
  html: `<div class="abs center kick" style="top:400px">an animated movie, years of work</div>${WIN('terminal', `<span class="g">$</span> <span id="cmd"></span>`)}
   <div class="abs center h2" id="oc" style="top:1000px;opacity:0;font-size:60px">almost deleted,<br><span class="mark" id="mk">with one command</span></div>`,
  init(el) { el.querySelector('.win').style.top = '520px'; },
  draw(S) { TYPE(S, '#cmd', 'delete everything in /film', .3, 1.2); const t = TT(S, 'command', .8); IN(S, '#oc', t - .5); MK(S, '#mk', t); if (S.on(t)) S.sfx(t, 'thud'); }},
 { // 1 files start vanishing
  html: `<div class="abs center kick" style="top:400px">1998 · the film's files</div><div class="files">${FILES.map((f, i) => `<div class="fl" id="f${i}">📁 ${f}</div>`).join('')}</div>`,
  draw(S) { const t = TT(S, 'starts', .5); S.$$('.fl').forEach((f, i) => { const g = S.on(t + i * .12); f.classList.toggle('gone', g); if (g && !S.on(t + i * .12 + .05)) S.sfx(t + i * .12, 'click'); }); }},
 { // 2 vanishing counter
  html: `<div class="abs center big" id="p" style="top:460px;font-size:220px;color:var(--red)">0%</div><div class="abs center lab" style="top:720px;font-size:44px">of the film deleted</div>
   ${['Characters', 'Scenes', 'Years of work'].map((w, i) => `<div class="wd" id="w${i}" style="top:${880 + i * 150}px">${w}</div>`).join('')}`,
  draw(S) { COUNT(S, '#p', 0, 90, 0, S.dur - .2, v => Math.round(v) + '%'); [TT(S, 'Characters', .1), TT(S, 'Scenes', .35), TT(S, 'Years', .6)].forEach((t, i) => { const w = S.$('#w' + i); w.style.opacity = S.on(t) ? 1 - .8 * S.P(t + .3, .6) : 0; w.style.filter = `blur(${8 * S.P(t + .3, .6)}px)`; if (S.on(t)) S.sfx(t, 'whoosh'); }); }},
 { // 3 backups failing
  html: `<div class="abs center big" style="top:440px;font-size:200px;color:var(--red)">90%</div><div class="abs center h2" style="top:680px">gone</div>
   <div class="tile" id="bk" style="left:150px;right:150px;top:860px;height:220px;display:flex;align-items:center;justify-content:space-between;padding:0 50px;font:700 50px Roboto;opacity:0"><span>backups</span><b style="color:var(--red)">✗ failing</b></div>`,
  draw(S) { IN(S, '#bk', TT(S, 'backups', .6) - .2); if (S.on(TT(S, 'failing', .85))) S.sfx(TT(S, 'failing', .85), 'buzz'); }},
 { // 4 a copy at home
  html: `<div class="house"><div class="roof"></div><div class="body"><div class="pc" id="pc"><div class="mon"></div><div class="stand"></div></div></div></div>
   <div class="abs center h2" id="cp" style="top:1250px;opacity:0">a copy, <span class="mark" id="mk">at home</span></div>`,
  draw(S) { const t = TT(S, 'copy', .7); IN(S, '#cp', t - .2); MK(S, '#mk', TT(S, 'home', .85)); S.$('.mon').style.boxShadow = S.on(t) ? '0 0 80px rgba(61,220,132,.7)' : ''; S.$('.mon').style.background = S.on(t) ? 'var(--grn)' : '#333'; if (S.on(t)) S.sfx(t, 'ding'); }},
 { // 5 working from home
  html: `<div class="tile" style="left:150px;right:150px;top:460px;height:600px;padding:50px"><div class="lab">her home computer</div><div class="files sm">${FILES.slice(0, 6).map(f => `<div class="fl ok">📁 ${f}</div>`).join('')}</div></div>
   <div class="abs center lab" style="top:1120px;font-size:40px">she'd been working from home</div>`,
  draw(S) { S.$$('.fl.ok').forEach((f, i) => f.style.opacity = S.on(.2 + i * .15) ? 1 : 0); }},
 { // 6 carried in blankets, saved
  html: `<div class="car" id="cr"><div class="bl"></div><div class="lab" style="text-align:center;margin-top:20px">computer, wrapped in blankets</div></div>
   <div class="stamp g" id="sv" style="left:300px;top:1100px;font-size:96px">SAVED</div>`,
  draw(S) { const p = S.P(0, TT(S, 'saved', .85) - .2, eio); S.$('#cr').style.transform = `translateX(${-700 + 700 * p}px)`; STAMP(S, '#sv', TT(S, 'saved', .85), -6); if (S.t > TT(S, 'saved', .85) && S.t < TT(S, 'saved', .85) + .1) flash(.4); }},
 ctaScene(),
];
