// WR10 v2: Hinge Most Compatible ~ Gale–Shapley (1962). Hinge: 8x more likely to go on a date (early tests).
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const COL = ['#ff7a8a', '#6fb3ff', '#b48cff', '#ffb35c', '#5fe08f', '#ff7ac8'];
const NAMES = ['Aarav', 'Diya', 'Kabir', 'Meera', 'Rohan', 'Isha', 'Vivaan', 'Anya', 'Arjun', 'Sara', 'Dev', 'Tara'];
const av = (id, col, name, x, y) => `<div class="av" id="${id}" style="left:${x}px;top:${y}px;background:${col}"><b class="l"></b><b class="r"></b><u></u><span>${name}</span></div>`;
const put = (S, id, x, y, s = 1) => { const e = S.$('#' + id); e.style.left = x + 'px'; e.style.top = y + 'px'; e.style.transform = `scale(${s})`; };
const walk = (S, at, d, a, b) => { const p = S.P(at, d, eio); return [a[0] + (b[0] - a[0]) * p, a[1] + (b[1] - a[1]) * p - 30 * Math.abs(Math.sin(p * Math.PI * 3))]; };
// room: left people A B C at x=80, right X Y Z at x=850
const ROOM = `${av('A', COL[0], 'A', 80, 420)}${av('B', COL[1], 'B', 80, 720)}${av('C', COL[2], 'C', 80, 1020)}${av('X', COL[3], 'X', 850, 420)}${av('Y', COL[4], 'Y', 850, 720)}${av('Z', COL[5], 'Z', 850, 1020)}`;
const SCENES = [
 { // 0 hook: 8x, math picked them
  html: `<div class="stack">${[0, 1, 2].map(i => `<div class="pc2" id="c${i}" style="background:linear-gradient(135deg,${COL[i + 3]},${COL[i]});transform:rotate(${(i - 1) * 6}deg) translateY(${i * 10}px)"><div>${NAMES[i * 3]}</div></div>`).join('')}</div>
   <div class="abs center big" id="x8" style="top:250px;font-size:220px;color:var(--yel);opacity:0">8×</div>
   <div class="abs center" id="mt" style="top:1190px;font:900 64px Roboto;opacity:0">and <span style="color:var(--yel)">math</span> picked them 🧮</div>`,
  draw(S) { const te = S.T('eight'), o = S.P(te - .2, .25, back); S.$('#x8').style.opacity = clamp(o); S.$('#x8').style.transform = `scale(${1.6 - .6 * clamp(o)})`; if (S.on(te - .2)) { S.sfx(te - .2, 'thud'); if (S.t - te + .2 < .07) flash(.4); }
    S.$('#c2').style.boxShadow = S.on(te) ? `0 0 0 8px var(--yel),0 0 ${50 + 20 * Math.sin(S.t * 8)}px rgba(255,210,63,.7)` : '';
    const tm = S.T('math'); S.$('#mt').style.opacity = S.P(tm - .2, .2); S.$('.stack').style.transform = `rotate(${2 * Math.sin(S.t * 2)}deg)`; }},
 { // 1 swipe forever -> matchmaker
  html: `<div class="stack">${Array.from({ length: 12 }, (_, i) => `<div class="pc2 sw" style="background:linear-gradient(135deg,${COL[i % 6]},${COL[(i + 2) % 6]});z-index:${20 - i}"><div>${NAMES[i]}</div></div>`).join('')}</div>
   <div class="abs center" id="cnt" style="top:300px;font:900 60px Roboto">swipes: <span style="color:var(--red)" id="n">0</span></div>
   <div class="stamp" id="mm" style="left:250px;top:1180px;opacity:0;color:var(--yel);border-color:var(--yel)">MATCHMAKER 💘</div>`,
  draw(S) { const tm = S.T('matchmaker'); const k = S.on(tm - .3) ? 99 : S.t / .16; S.$$('.sw').forEach((c, i) => { const u = clamp(k - i); c.style.transform = `translateX(${(i % 2 ? 1 : -1) * 900 * u}px) rotate(${(i % 2 ? 1 : -1) * 30 * u}deg)`; if (u > 0 && u < 1 && i < 12) S.sfx(i * .16, 'swish'); });
    S.$('#n').textContent = S.on(tm - .3) ? '∞' : fmt(Math.min(999, Math.floor(k * 83))); const o = S.P(tm - .3, .2, back); S.$('#mm').style.opacity = clamp(o); S.$('#mm').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tm - .3)) S.sfx(tm - .3, 'thud'); }},
 { // 2 1962 + Nobel
  html: `<div class="abs center big" id="yr" style="top:330px;font-size:240px;color:var(--yel)">2026</div>
   <div class="medal" id="md" style="left:390px;top:700px;opacity:0">NOBEL<br>PRIZE</div><div class="abs" id="sh" style="left:390px;top:700px;width:300px;height:300px;border-radius:50%;overflow:hidden;opacity:0"><i style="position:absolute;top:0;bottom:0;width:60px;background:rgba(255,255,255,.6);transform:skewX(-20deg)" id="sw"></i></div>
   <div class="abs center" id="lit" style="top:1080px;font:900 56px Roboto;opacity:0">literally. 🏅</div>`,
  draw(S) { const ty = S.T('1962'), p = S.P(0, ty + .1, eio); S.$('#yr').textContent = Math.round(2026 - 64 * p); if (S.t < ty) S.sfx(Math.floor(S.t * 8) / 8, 'tick');
    const tn = S.T('Nobel'), d = S.P(tn - .4, .45, back); S.$('#md').style.opacity = clamp(d * 3); S.$('#md').style.transform = `translateY(${-400 * (1 - clamp(d))}px) rotate(${10 * Math.sin(S.t * 3)}deg)`; if (S.on(tn - .1)) S.sfx(tn - .1, 'ding');
    S.$('#sh').style.opacity = S.on(tn) ? 1 : 0; S.$('#sw').style.left = (-80 + 420 * ((S.t - tn) % 1)) + 'px'; S.$('#lit').style.opacity = S.P(S.T('literally') - .1, .2); }},
 { // 3 room: ranks + ask top choice
  html: `${ROOM}<div class="abs center kick" style="top:330px" id="rk">everyone ranks everyone</div>
   <div class="bub" id="b1" style="left:250px;top:560px;opacity:0">date? 🌹</div><div class="bub" id="b2" style="left:250px;top:1160px;opacity:0">date? 🌹</div>`,
  draw(S) { const tr = S.T('ranks'); S.$('#rk').style.opacity = S.P(tr - .3, .2); const ta = S.T('asks');
    let [x, y] = walk(S, ta - .3, .9, [80, 420], [660, 720]); put(S, 'A', x, y); [x, y] = walk(S, ta - .1, .9, [80, 1020], [660, 1020]); put(S, 'C', x, y);
    S.$('#b1').style.opacity = S.P(ta + .7, .2); S.$('#b1').style.left = '520px'; S.$('#b1').style.top = '660px'; S.$('#b2').style.opacity = S.P(ta + .8, .2); S.$('#b2').style.left = '520px'; S.$('#b2').style.top = '960px'; if (S.on(ta - .3)) S.sfx(ta - .3, 'whoosh'); }},
 { // 4 better offer, switch, dumped
  html: `${ROOM}<div class="bub" id="bo" style="left:480px;top:600px;opacity:0">ooh, better offer 😏</div><div class="abs" id="hb" style="font-size:90px;opacity:0">${EMO('red-heart')}</div>`,
  draw(S) { put(S, 'C', 660, 1020); const ts = S.T('switch'), td = S.T('dumped'), tn = S.T('next');
    let [bx, by] = walk(S, 0, ts - .2, [80, 720], [660, 720]); put(S, 'B', bx, by); S.$('#bo').style.opacity = S.P(ts - .6, .2) * (1 - S.P(td, .2));
    // A gets bumped back, sad, then walks to X
    const kick = S.P(ts - .1, .35, eo); let ax = 660 - 480 * kick, ay = 720 + 40 * kick; if (S.on(tn - .3)) { const q = S.P(tn - .3, .9, eio); ax = 180 + (680 - 180) * q; ay = 760 + (440 - 760) * q - 30 * Math.abs(Math.sin(q * 9)); }
    put(S, 'A', ax, ay); S.$('#A').classList.toggle('sad', S.on(ts - .1) && !S.on(tn + .5)); S.$('#A').style.filter = S.on(ts - .1) && !S.on(tn - .3) ? 'saturate(.4)' : '';
    if (S.on(ts - .1)) S.sfx(ts - .1, 'thud'); const h = S.$('#hb'); h.style.opacity = S.on(ts) ? 1 : 0; h.style.left = '770px'; h.style.top = (600 - 40 * ((S.t * 1.5) % 1)) + 'px'; h.innerHTML = S.on(ts) ? EMO('red-heart') : '';
    S.$('#dp') }},
 { // 5 stable: everyone paired, hearts + confetti
  html: `${ROOM}<div class="stamp" id="st" style="left:300px;top:1240px;opacity:0;color:var(--grn);border-color:var(--grn)">STABLE ✓</div><div id="hs"></div>`,
  init(el) { el.querySelector('#hs').innerHTML = Array.from({ length: 14 }, () => `<div class="abs hh" style="font-size:60px">${EMO('red-heart')}</div>`).join(''); },
  draw(S) { put(S, 'A', 680, 420); put(S, 'B', 680, 720); put(S, 'C', 680, 1020); const tn = S.T('nobody');
    const o = S.P(tn - .2, .25, back); S.$('#st').style.opacity = clamp(o); S.$('#st').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tn - .2)) S.sfx(tn - .2, 'ding');
    S.$$('.hh').forEach((h, i) => { const u = ((S.t * .6 + R(i)) % 1); h.style.left = (100 + R(i + 9) * 880) + 'px'; h.style.top = (1400 - 1100 * u) + 'px'; h.style.opacity = S.on(tn - .2) ? 1 - u : 0; }); }},
 { // 6 Hinge pairs you, they get you too
  html: `${av('U', '#ffd23f', 'you', 150, 640)}${av('M', COL[0], NAMES[3], 780, 640)}<div class="abs" id="beam" style="left:300px;top:705px;height:20px;border-radius:10px;background:linear-gradient(90deg,#ffd23f,#ff7a8a);width:0"></div>
   <div class="abs center kick" style="top:420px">every day · one person</div><div class="abs center" id="hr" style="top:930px;font-size:150px;opacity:0">${EMO('red-heart')}</div>`,
  draw(S) { const tp = S.T('pairs'); S.$('#beam').style.width = (480 * S.P(tp - .2, .6, eo)) + 'px'; if (S.on(tp)) S.sfx(tp, 'whoosh'); const tt = S.T('too'), o = S.P(tt - .3, .3, back);
    S.$('#hr').style.opacity = clamp(o); S.$('#hr').style.transform = `scale(${.6 + .4 * clamp(o) + .08 * Math.sin(S.t * 12)})`; if (S.on(tt - .3)) S.sfx(tt - .3, 'pop'); }},
 { // 7 Most Compatible = 8x (drop)
  html: `<div class="abs center" style="top:330px"><span style="display:inline-block;padding:14px 34px;border-radius:30px;background:#fff;color:#111;font:900 50px Roboto">✨ MOST COMPATIBLE</span></div>
   <div class="abs center big" id="x8" style="top:480px;font-size:300px;color:var(--yel)">0×</div><div class="abs center h2" style="top:850px">more likely to become a <span class="mark" id="mk">date</span></div>`,
  draw(S) { if (S.t < .07) flash(.5); const te = S.T('eight'), p = S.P(te - .3, .45, eo); S.$('#x8').textContent = Math.round(8 * p) + '×'; S.$('#x8').style.transform = `scale(${1 + .15 * Math.max(0, 1 - Math.abs(S.t - te) * 4)})`; if (S.on(te)) S.sfx(te, 'thud');
    S.$('#mk').style.setProperty('--m', S.P(S.T('date') - .2, .3)); }},
 ctaScene(),
];
