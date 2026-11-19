// WR10 v3: Hinge-style UI. Most Compatible ~ Gale–Shapley (1962). Hinge: 8x more likely to go on a date (early tests). Photos: Unsplash (stock, illustrative).
const IMG = n => `url(../../webreels/wr10/img/p${n}.jpg)`;
const HEART = `<svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.3 3 4.5 6.7 4.5c2.1 0 3.6 1.2 4.3 2.6.7-1.4 2.2-2.6 4.3-2.6 3.7 0 5.8 3.8 4.3 7.3C19.5 16.4 12 21 12 21z"/></svg>`;
const HEARTF = HEART.replace('fill="none"', 'fill="#e8455f"').replace('stroke="#111"', 'stroke="#e8455f"');
const P = { you: 9, maya: 1, leo: 4, ava: 7, noah: 3, sara: 10 };
const SB = `<div class="sb"><span>9:41</span><span>●●● ▮</span></div>`;
const PROFILE = (name, img, prompt, ans, mc = false, extra = '') => `${SB}<div class="feed">${mc ? '<div class="mc">✦ Most Compatible</div>' : ''}<div class="nm">${name}</div><div class="sub">Active today</div>
  <div class="ph" style="background-image:${IMG(img)}"><div class="hbtn">${HEART}</div></div><div class="pr"><div class="q">${prompt}</div><div class="a">${ans}</div><div class="hbtn">${HEART}</div></div>${extra}</div>`;
const mini = (id, name, img, x, y) => `<div class="mini" id="${id}" style="left:${x}px;top:${y}px"><div class="ph" style="background-image:${IMG(img)}"></div><div class="nm">${name}</div></div>`;
const fly = (S, el, at, d, a, b) => { const p = S.P(at, d, eio); el.style.opacity = S.on(at) && p < 1 ? 1 : (p >= 1 ? 1 : 0); el.style.left = (a[0] + (b[0] - a[0]) * p) + 'px'; el.style.top = (a[1] + (b[1] - a[1]) * p - 80 * Math.sin(p * Math.PI)) + 'px'; el.style.transform = `scale(${.8 + .4 * Math.sin(p * Math.PI)})`; };
const SCENES = [
 { // 0 hook: real-looking Most Compatible profile, NOT RANDOM, Nobel
  html: `<div class="hp" id="ph0" style="left:240px;top:330px">${PROFILE('Maya', P.maya, 'My simple pleasures', 'Sunday coffee and a very long walk', true)}<div class="xbtn">✕</div></div>
   <div class="stamp" id="nr" style="left:160px;top:640px;opacity:0;z-index:20;background:rgba(17,17,17,.6)">NOT RANDOM</div>
   <div class="abs center" id="nb" style="top:1250px;z-index:20;opacity:0"><span style="display:inline-block;padding:20px 36px;border-radius:24px;background:#111;box-shadow:0 0 0 3px var(--yel);font:800 44px Inter">🏅 Nobel Prize-winning algorithm</span></div>
   <div class="abs" style="right:40px;top:1520px;font:500 18px Inter;color:#666">photos: Unsplash · illustrative</div>`,
  draw(S) { const feed = S.$('.feed'); feed.style.transform = `translateY(${-50 * S.P(0, S.dur, x => x)}px)`; const tc = S.T('compatible'); S.$('.mc').style.boxShadow = S.on(tc - .3) ? `0 0 0 ${4 + 2 * Math.sin(S.t * 10)}px var(--yel)` : '';
    const tr = S.T('random'), o = S.P(tr - .2, .2, back); S.$('#nr').style.opacity = clamp(o); S.$('#nr').style.transform = `rotate(-10deg) scale(${1.5 - .5 * clamp(o)})`; if (S.on(tr - .2)) S.sfx(tr - .2, 'thud');
    const tn = S.T('Nobel'), q = S.P(tn - .2, .25, back); S.$('#nb').style.opacity = clamp(q); S.$('#nb').style.transform = `translateY(${(1 - clamp(q)) * 80}px)`; if (S.on(tn - .2)) S.sfx(tn - .2, 'ding'); }},
 { // 1 love triangle with flying likes
  html: `${mini('cy', 'You', P.you, 90, 380)}${mini('cm', 'Maya', P.maya, 710, 380)}${mini('cl', 'Leo', P.leo, 400, 900)}
   <div class="flyh" id="h1">${HEARTF}</div><div class="flyh" id="h2">${HEARTF}</div><div class="flyh" id="h3">${HEARTF}</div>
   <div class="abs center" id="sad" style="top:1440px;font:800 46px Inter;opacity:0">💔 nobody ends up happy</div>`,
  draw(S) { const t1 = S.T('like') - .1, t2 = S.T('likes', 1) - .1, t3 = S.T('likes', 2) - .1;
    fly(S, S.$('#h1'), t1, .7, [330, 520], [680, 520]); fly(S, S.$('#h2'), t2, .7, [800, 720], [620, 900]); fly(S, S.$('#h3'), t3, .7, [420, 980], [250, 720]);
    [t1, t2, t3].forEach(t => { if (S.on(t)) S.sfx(t, 'pop'); });
    const tn = S.T('nobody'); const g = S.on(tn - .2); S.$$('.mini').forEach(m => m.style.filter = g ? 'grayscale(1) brightness(.7)' : ''); S.$$('.flyh').forEach(h => h.style.opacity = g ? 0 : h.style.opacity);
    S.$('#sad').style.opacity = S.P(tn - .2, .2); if (S.on(tn - .2)) S.sfx(tn - .2, 'thud'); }},
 { // 2 1962 paper + Nobel medal
  html: `<div class="paper" id="pp"><div style="font:700 30px Mono;color:#8a6d1a;letter-spacing:3px">1962 · GALE &amp; SHAPLEY</div><div style="font:600 52px/1.15 Serif;margin-top:20px">College Admissions and the Stability of Marriage</div></div>
   <div class="medal" id="md" style="left:700px;top:300px;opacity:0">NOBEL<br>2012</div>
   <div class="abs center h" style="top:1000px;font-size:76px"><span class="mark" id="mk">the stable marriage problem</span></div>`,
  draw(S) { const p = S.P(0, .35, eo); S.$('#pp').style.transform = `translateY(${(1 - p) * 80}px) rotate(-2deg)`; S.$('#pp').style.opacity = p; S.sfx(.02, 'swish');
    const tc = S.T('cracked'), m = S.P(tc - .2, .3, back); S.$('#md').style.opacity = clamp(m); S.$('#md').style.transform = `scale(${clamp(m)}) rotate(${8 * Math.sin(S.t * 3)}deg)`; if (S.on(tc - .2)) S.sfx(tc - .2, 'ding');
    const ts = S.T('stable'); S.$('#mk').style.setProperty('--m', S.P(ts - .1, .4)); S.$('#mk').parentNode.style.opacity = S.on(ts - .2) ? 1 : 0; }},
 { // 3 rank, then shoot your shot (like sheet)
  html: `<div class="hp" style="left:240px;top:300px">${SB}<div class="feed"><div class="nm" style="font-size:46px">Your ranking</div><div class="sub">who you like most</div><div id="rl">
     ${[['Maya', P.maya], ['Ava', P.ava], ['Sara', P.sara]].map((r, i) => `<div class="rk" id="r${i}"><em>${i + 1}</em><i style="background-image:${IMG(r[1])}"></i>${r[0]}</div>`).join('')}</div></div>
     <div class="sheet" id="sh"><div class="th" style="background-image:${IMG(P.maya)}"></div><div class="cm">Add a comment</div><div class="row"><b style="background:#111;color:#fff" id="sl">Send like</b><b style="background:#6b3fa0;color:#fff">🌹 Rose</b></div></div></div>
   <div class="tap" id="tp" style="left:380px;top:1290px;opacity:0;z-index:20"></div>`,
  draw(S) { const tr = S.T('ranks'); S.$$('.rk').forEach((r, i) => { const p = S.P(tr - .4 + i * .15, .25, back); r.style.opacity = clamp(p); r.style.transform = `translateX(${(1 - clamp(p)) * 200}px)`; if (S.on(tr - .4 + i * .15)) S.sfx(tr - .4 + i * .15, 'click'); });
    const ts = S.T('shoot'), q = S.P(ts - .4, .35, eo); S.$('#sh').style.transform = `translateY(${(1 - q) * 700}px)`; if (S.on(ts - .4)) S.sfx(ts - .4, 'swish');
    const tn = S.T('one', 2); const u = S.P(tn - .2, .4, x => x); S.$('#tp').style.opacity = S.on(tn - .2) ? 1 - u : 0; S.$('#tp').style.transform = `scale(${.5 + u})`; S.$('#sl').style.background = S.on(tn) ? '#e8455f' : '#111'; S.$('#sl').textContent = S.on(tn) ? 'Like sent ✓' : 'Send like'; if (S.on(tn - .2)) S.sfx(tn - .2, 'pop'); }},
 { // 4 Maya's "Likes You": you, then better offer Noah -> trade up; you move to #2
  html: `<div class="hp" style="left:240px;top:300px">${SB}<div class="feed"><div class="nm" style="font-size:46px">Maya's likes</div><div class="sub">people who liked her</div>
     <div class="lk" id="lyou"><i style="background-image:${IMG(P.you)}"></i><div>You<small>liked your photo</small></div></div>
     <div class="lk" id="lnoah"><i style="background-image:${IMG(P.noah)}"></i><div>Noah<small>her #1 · sent a rose 🌹</small></div></div></div></div>
   <div class="abs" id="tu" style="left:560px;top:860px;z-index:20;opacity:0"><span style="display:inline-block;padding:16px 30px;border-radius:20px;background:var(--grn);color:#111;font:900 40px Inter">trades up ↑</span></div>
   <div class="abs center" id="n2" style="top:1470px;z-index:20;font:800 44px Inter;opacity:0">you → your <span style="color:var(--yel)">#2: Ava</span> ${'❤️'}</div>`,
  draw(S) { const tb = S.T('better'); const n = S.P(tb - .4, .3, back); S.$('#lnoah').style.opacity = clamp(n); S.$('#lnoah').style.transform = `translateY(${(1 - clamp(n)) * 80}px)`; if (S.on(tb - .4)) S.sfx(tb - .4, 'pop');
    const tt = S.T('trade'); const on = S.on(tt - .1); S.$('#lnoah').style.boxShadow = on ? '0 0 0 5px #3ddc84' : '0 0 0 2px #eee'; S.$('#tu').style.opacity = S.P(tt - .1, .2); if (on) S.sfx(tt - .1, 'ding');
    const out = S.P(tt + .2, .4, eo); S.$('#lyou').style.transform = `translateX(${-700 * out}px) rotate(${-10 * out}deg)`; S.$('#lyou').style.opacity = 1 - out;
    S.$('#n2').style.opacity = S.P(S.T('two') - .4, .2); }},
 { // 5 stable pairs: It's a match cards
  html: `${[[P.noah, P.maya], [P.you, P.ava], [P.leo, P.sara]].map((p, i) => `<div class="mt m${i}" style="top:${360 + i * 280}px"><div class="av2"><i style="background-image:${IMG(p[0])}"></i><i style="background-image:${IMG(p[1])}"></i></div><div class="tx">It's a match</div></div>`).join('')}
   <div class="stamp" id="st" style="left:280px;top:1250px;opacity:0;color:var(--grn);border-color:var(--grn)">STABLE ✓</div>`,
  draw(S) { S.$$('.mt').forEach((m, i) => { const p = S.P(i * .25, .3, back); m.style.opacity = clamp(p); m.style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(i * .25)) S.sfx(i * .25, 'pop'); });
    const ts = S.T('stable'), o = S.P(ts - .2, .2, back); S.$('#st').style.opacity = clamp(o); S.$('#st').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(ts - .2)) S.sfx(ts - .2, 'thud'); }},
 { // 6 Hinge's version: you see Ava, Ava sees you
  html: `<div class="hp" id="pa" style="left:20px;top:380px;transform:scale(.82);transform-origin:0 0">${PROFILE('Ava', P.ava, 'A perfect first date', 'Tacos, then a bookstore', true)}</div>
   <div class="hp" id="pb" style="left:560px;top:380px;transform:scale(.82);transform-origin:0 0">${PROFILE('You', P.you, 'I geek out on', 'Bad puns and good maps', true)}</div>
   <div class="abs center" style="top:300px" id="lb"><span class="kick">your pick ⇄ their pick</span></div>`,
  draw(S) { const tp = S.T('picks'); S.$('#pa').style.opacity = S.P(tp - .5, .3); const tt = S.T('too'); S.$('#pb').style.opacity = S.P(tt - .8, .3); if (S.on(tt - .8)) S.sfx(tt - .8, 'whoosh');
    S.$$('.mc').forEach(m => m.style.boxShadow = S.on(tt - .3) ? `0 0 0 ${4 + 2 * Math.sin(S.t * 10)}px var(--yel)` : ''); }},
 { // 7 8x (drop)
  html: `<div class="abs center big" id="x8" style="top:330px;font-size:300px;color:var(--yel)">0×</div><div class="abs center h2" style="top:700px">more likely to go on a <span class="mark" id="mk">date</span></div>
   <div class="mt" id="dc" style="top:900px;opacity:0"><div class="av2"><i style="background-image:${IMG(P.you)}"></i><i style="background-image:${IMG(P.ava)}"></i></div><div><div class="tx" style="font-size:46px">Saturday, 8 pm</div><div style="font:600 26px Inter;color:#888">tacos, then a bookstore 🌮📚</div></div></div>
   <div class="abs center" style="top:1170px;font:500 24px Inter;color:var(--mute)">source: Hinge, early tests</div>`,
  draw(S) { if (S.t < .07) flash(.5); const te = S.T('eight'), p = S.P(te - .3, .45, eo); S.$('#x8').textContent = Math.round(8 * p) + '×'; S.$('#x8').style.transform = `scale(${1 + .15 * Math.max(0, 1 - Math.abs(S.t - te) * 4)})`; if (S.on(te)) S.sfx(te, 'thud');
    const td = S.T('date'); S.$('#mk').style.setProperty('--m', S.P(td - .2, .3)); const o = S.P(td, .3, back); S.$('#dc').style.opacity = clamp(o); S.$('#dc').style.transform = `translateY(${(1 - clamp(o)) * 60}px)`; if (S.on(td)) S.sfx(td, 'pop'); }},
 ctaScene(),
];
