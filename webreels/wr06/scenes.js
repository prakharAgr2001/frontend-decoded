// WR06: a tenth of a second costs Amazon money (Greg Linden ~2006; Google 0.5 s -> -20% searches; Core Web Vitals)
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const SCENES = [
 { // 0 0.1 s
  html: `<svg class="abs" style="left:290px;top:330px" width="500" height="500"><circle cx="250" cy="250" r="210" stroke="#2a2a31" stroke-width="26" fill="none"/><circle id="arc" cx="250" cy="250" r="210" stroke="#ffd23f" stroke-width="26" fill="none" stroke-linecap="round" transform="rotate(-90 250 250)" stroke-dasharray="1320" stroke-dashoffset="1320"/></svg>
   <div class="abs center big" id="sec" style="top:500px;font-size:140px">0.0s</div>
   <div class="abs center h" id="mo" style="top:960px;font-size:100px;opacity:0">= lost ${EMO('money-with-wings')}</div>`,
  draw(S) { const p = S.P(0, S.T('second'), eio); S.$('#sec').textContent = (0.1 * p).toFixed(2).replace(/0$/, '') + 's'; S.$('#arc').setAttribute('stroke-dashoffset', 1320 * (1 - p * .1 / 1));
    const tm = S.T('money'), o = S.P(tm - .2, .25, back); S.$('#mo').style.opacity = clamp(o); S.$('#mo').style.transform = `scale(${.8 + .2 * clamp(o)})`; if (S.on(tm - .2)) S.sfx(tm - .2, 'thud'); S.sfx(0.05, 'tick'); }},
 { // 1 sneaky test, slow pages
  html: `<div class="abs center kick" style="top:380px">~2006 · Amazon's own test</div>
   <div class="shop"><div class="bar"></div><div class="pb"></div><div class="img"></div>${[0, 1, 2, 3].map(i => `<div class="ln" style="top:${130 + i * 70}px;right:${40 + i * 60}px"></div>`).join('')}<div class="btn"></div></div>
   <div class="abs" id="sn" style="left:760px;top:1150px;font-size:130px;opacity:0">${EMO('snail')}</div>
   <div class="abs" id="pur" style="left:120px;top:1200px;padding:12px 28px;border:6px solid var(--red);border-radius:14px;font:900 50px Roboto;color:var(--red);transform:rotate(-8deg);opacity:0">ON PURPOSE</div>`,
  draw(S) { const ts = S.T('slowed'); const sp = S.on(ts) ? .12 : 1; const ph = ((S.t * sp * 1.2) % 1); S.$('.pb').style.width = (100 * ph) + '%';
    S.$$('.shop .ln,.shop .img,.shop .btn').forEach((e, i) => e.style.opacity = S.on(ts) ? .35 + .3 * Math.sin(S.t * 3 + i) : 1);
    S.$('#sn').style.opacity = S.P(ts, .3); if (S.on(ts)) S.sfx(ts, 'swish'); const tp = S.T('purpose'); const o = S.P(tp - .2, .2, back); S.$('#pur').style.opacity = clamp(o); S.$('#pur').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tp - .2)) S.sfx(tp - .2, 'thud'); }},
 { // 2 100 ms vs a blink
  html: `<div class="abs center big" style="top:380px;font-size:170px;color:var(--yel)">100 ms</div>
   <div class="cmp" style="top:720px"><div class="l"><span>⚡ the delay</span><span>100 ms</span></div><div class="t"><i id="b0" style="background:var(--yel)"></i></div></div>
   <div class="cmp" style="top:930px"><div class="l"><span>${EMO('eye')} one blink</span><span>~300 ms</span></div><div class="t"><i id="b1" style="background:#888"></i></div></div>`,
  draw(S) { const tb = S.T('blink'); S.$('#b0').style.width = (33 * S.P(0, .5)) + '%'; S.$('#b1').style.width = (100 * S.P(tb - .3, .5)) + '%'; }},
 { // 3 sales drop staircase (drop)
  html: `<div class="abs center h2" style="top:340px">every +100 ms</div>
   <div class="stair">${[0, 1, 2, 3, 4].map(i => `<div style="height:${100 - i * 9}%"><b>−${i}%</b><span>+${i * 100} ms</span></div>`).join('')}</div>`,
  draw(S) { const td = S.T('dropped'); S.$$('.stair div').forEach((d, i) => { const at = td + i * .35, p = S.P(at, .25, back); d.style.transform = `scaleY(${clamp(p)})`; d.style.transformOrigin = 'bottom'; d.querySelector('b').style.opacity = i && S.on(at) ? 1 : 0; if (S.on(at)) S.sfx(at, 'thud'); });
    if (S.t < .07) flash(.4); }},
 { // 4 Google too
  html: `<div class="search">🔍 <span id="q" style="margin-left:20px"></span><span style="margin-left:auto;color:var(--red);font-weight:800" id="dl"></span></div>
   <div class="cmp" style="top:720px"><div class="l"><span>Normal speed</span><span>100%</span></div><div class="t"><i id="g0" style="background:var(--grn)"></i></div></div>
   <div class="cmp" style="top:930px"><div class="l"><span>+0.5 s slower</span><span id="gv">100%</span></div><div class="t"><i id="g1" style="background:var(--red)"></i></div></div>
   <div class="abs center big" id="m20" style="top:1170px;font-size:130px;color:var(--red);opacity:0">−20%</div>`,
  draw(S) { const txt = 'cheap flights to goa'; S.$('#q').textContent = txt.slice(0, Math.floor(txt.length * S.P(0, 1.2, x => x)));
    const th = S.T('Half'), p = S.P(th, .7, eio); S.$('#dl').textContent = S.on(th) ? '+0.5s' : ''; S.$('#g0').style.width = '100%'; S.$('#g1').style.width = (100 - 20 * p) + '%'; S.$('#gv').textContent = Math.round(100 - 20 * p) + '%';
    const tt = S.T('twenty'), o = S.P(tt - .1, .2); S.$('#m20').style.opacity = o; if (S.on(tt)) S.sfx(tt, 'thud'); }},
 { // 5 billions
  html: `<div class="abs center big" style="top:400px;font-size:200px;color:var(--yel)">1%</div><div class="abs center h2" style="top:650px">of Amazon's sales</div>
   <div class="abs center h" id="bn" style="top:840px;font-size:130px;opacity:0">= <span class="mark">billions</span> ${EMO('money-with-wings')}</div>`,
  draw(S) { const tb = S.T('billions'); const o = S.P(tb - .3, .3, back); S.$('#bn').style.opacity = clamp(o); S.$('#bn').style.transform = `scale(${.8 + .2 * clamp(o)})`; if (S.on(tb - .3)) S.sfx(tb - .3, 'ding'); }},
 { // 6 Google grades with three numbers
  html: `<div class="abs center kick" style="top:360px">Google's report card for every site</div>
   ${[0, 1, 2].map(i => `<div class="gauge g" style="top:${450 + i * 290}px"><div class="k">?</div><div class="tr"><i></i></div></div>`).join('')}`,
  draw(S) { const tt = S.T('three'); S.$$('.g').forEach((g, i) => { const at = tt - .2 + i * .12, p = S.P(at, .25, back); g.style.opacity = clamp(p); g.style.transform = `translateX(${(1 - clamp(p)) * 120}px)`; if (S.on(at)) S.sfx(at, 'pop'); }); }},
 { // 7 loads / reacts / jumps
  html: `${[['LCP', 'how fast it loads', 'hourglass-not-done'], ['INP', 'how fast it reacts to a tap', 'backhand-index-pointing-down'], ['CLS', 'does it jump around?', 'face-with-open-mouth']].map((g, i) =>
     `<div class="gauge v${i}" style="top:${400 + i * 290}px"><div class="ic" style="font-size:80px">${EMO(g[2])}</div><div class="k">${g[0]}</div><div class="d">${g[1]}</div><div class="tr"><i></i></div></div>`).join('')}`,
  draw(S) { [['loads', 0], ['reacts', 1], ['jumps', 2]].forEach(([w, i]) => { const at = S.T(w) - .2, on = S.on(at), g = S.$('.v' + i); g.style.opacity = on ? 1 : .25; g.querySelector('.tr i').style.width = (100 * S.P(at, .5, eo)) + '%'; if (on) S.sfx(at, 'click');
      if (i === 2 && on) g.style.transform = `translateY(${Math.round(Math.sin((S.t - at) * 14) * 26 * Math.max(0, 1 - (S.t - at) / 1.2))}px)`; }); }},
 { // 8 name
  html: `<div class="abs center kick" style="top:560px">They're called</div><div class="h abs center" style="top:660px;font-size:112px"><span class="mark" id="mk">Core Web Vitals</span></div>`,
  draw(S) { const tc = S.T('Core'); S.$('#mk').style.setProperty('--m', S.P(tc - .1, .35)); if (S.on(tc)) S.sfx(tc, 'ding'); }},
 ctaScene(),
];
