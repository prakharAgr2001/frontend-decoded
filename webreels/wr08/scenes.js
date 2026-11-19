// WR08: Netflix removed client-side React from its logged-out landing page (2017; Addy Osmani case study)
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const PAGE = (top, extra = '') => `<div class="br" style="top:${top}px"><div class="bar"><span>netflix.com</span></div><div class="hero"><div class="t">Unlimited films,<br>series and more</div><div class="in"><span></span><b>Get started ›</b></div></div>${extra}</div>`;
const SCENES = [
 { // 0 delete React -> 50% faster
  html: `<div class="edit" style="top:380px"><div id="l0" style="color:#c792ea">import React from 'react';</div><div style="color:#888">// netflix.com landing page</div></div>
   <div class="abs center big" id="f50" style="top:720px;font-size:170px;color:var(--grn);opacity:0">50% faster</div>`,
  draw(S) { const td = S.T('deleted'), p = S.P(td - .1, .3); const l = S.$('#l0'); l.style.textDecoration = p > 0 ? 'line-through' : ''; l.style.color = p > 0 ? 'var(--red)' : '#c792ea'; l.style.opacity = 1 - .6 * p; if (S.on(td)) S.sfx(td, 'swish');
    const tf = S.T('fifty'), o = S.P(tf - .2, .25, back); S.$('#f50').style.opacity = clamp(o); S.$('#f50').style.transform = `scale(${.8 + .2 * clamp(o)})`; if (S.on(tf - .2)) S.sfx(tf - .2, 'thud'); }},
 { // 1 wait, what?
  html: `<div class="abs center" style="top:420px;font-size:260px" id="th">${EMO('thinking-face')}</div><div class="abs center h2" style="top:820px">Netflix is <i style="color:var(--yel)">built</i> with React…</div>`,
  draw(S) { const p = S.P(0, .3, back); S.$('#th').style.transform = `scale(${clamp(p)}) rotate(${6 * Math.sin(S.t * 5)}deg)`; S.sfx(0.02, 'pop'); }},
 { // 2 looked ready, but dead
  html: `${PAGE(360)}<div class="cmp" style="top:1000px"><div class="l"><span class="mono" style="font-size:34px">react + app code</span><span id="ph">downloading</span></div><div class="t"><i id="pb" style="background:var(--yel)"></i></div></div>
   <div class="tap" id="tp" style="left:680px;top:690px;opacity:0"></div><div class="abs center" id="nope" style="top:870px;font:800 40px Roboto;color:var(--red);opacity:0">👆 tap… nothing happens</div>`,
  draw(S) { const td = S.T('downloading'), tr = S.T('running'); const p = S.P(td - .2, tr - td + .2, x => x); const q = S.P(tr, 1.2, x => x);
    S.$('#pb').style.width = (100 * (S.on(tr) ? q : p)) + '%'; S.$('#ph').textContent = S.on(tr) ? 'running…' : 'downloading…'; S.$('#pb').style.background = S.on(tr) ? 'var(--red)' : 'var(--yel)';
    const ta = S.T('ready'); const u = ((S.t - ta) / .6) % 1; S.$('#tp').style.opacity = S.on(ta) ? 1 - u : 0; S.$('#tp').style.transform = `scale(${.5 + u})`; S.$('#nope').style.opacity = S.on(ta + .3) ? 1 : 0; if (S.on(ta)) S.sfx(ta + Math.floor((S.t - ta) / .6) * .6, 'click'); }},
 { // 3 hydration
  html: `${PAGE(360)}<div class="abs center h" style="top:1020px;font-size:120px"><span class="mark" id="mk">Hydration</span> ${EMO('droplet')}</div>`,
  draw(S) { const th = S.T('hydration'); const p = S.P(th - .4, .6); S.$('.br').style.filter = `grayscale(${1 - p}) brightness(${.6 + .4 * p})`; S.$('#mk').style.setProperty('--m', S.P(th - .1, .3)); if (S.on(th)) S.sfx(th, 'ding'); }},
 { // 4 server React, browser plain JS
  html: `<div class="box b0" style="left:90px;top:420px"><div style="font-size:90px">🖥️</div><div class="h3">Server</div><div class="d">React builds<br>the page HTML</div></div>
   <div class="box b1" style="left:570px;top:420px"><div style="font-size:90px">🌐</div><div class="h3">Your browser</div><div class="d">plain<br>JavaScript</div></div>
   <div class="abs center" style="top:920px;font:700 40px Roboto;color:var(--grn)" id="ok">React where it's needed. Not everywhere.</div>`,
  draw(S) { [['server', 0], ['browser', 1]].forEach(([w, i]) => { const at = S.T(w) - .2, p = S.P(at, .3, back); const b = S.$('.b' + i); b.style.opacity = clamp(p); b.style.transform = `translateY(${(1 - clamp(p)) * 60}px)`; if (S.on(at)) S.sfx(at, 'pop'); });
    S.$('#ok').style.opacity = S.P(S.T('plain'), .3); }},
 { // 5 200 KB gone
  html: `<div class="abs" style="left:120px;right:120px;top:400px;text-align:center;line-height:0">${['react', 'react-dom', 'lodash', 'utils', 'state', 'app'].map(n => `<span class="kbk">${n}</span>`).join('')}</div>
   <div class="abs center big" id="kb" style="top:800px;font-size:150px;color:var(--red)">−0 KB</div>`,
  draw(S) { const tg = S.T('gone'), p = S.P(tg - .6, .7, x => x); S.$$('.kbk').forEach((k, i) => { const q = clamp((p - i * .1) * 3); k.style.opacity = 1 - q; k.style.transform = `translateY(${-160 * q}px) rotate(${(R(i) - .5) * 60 * q}deg)`; });
    S.$('#kb').textContent = '−' + Math.round(200 * S.P(0, S.T('kilobytes') + .2, eo)) + ' KB'; if (S.on(tg)) S.sfx(tg, 'whoosh'); }},
 { // 6 TTI halved (drop)
  html: `<div class="abs center kick" style="top:440px">time until you can click</div>
   <div class="cmp" style="top:560px"><div class="l"><span>before</span><span></span></div><div class="t"><i style="background:var(--red);width:100%"></i></div></div>
   <div class="cmp" style="top:760px"><div class="l"><span>after</span><span id="aft"></span></div><div class="t"><i id="ab" style="background:var(--grn)"></i></div></div>
   <div class="abs center big" id="hf" style="top:960px;font-size:170px;color:var(--grn);opacity:0">½</div>`,
  draw(S) { if (S.t < .07) flash(.5); const th = S.T('half'), p = S.P(th - .5, .6, eio); S.$('#ab').style.width = (100 - 50 * p) + '%'; S.$('#aft').textContent = Math.round(100 - 50 * p) + '%';
    const o = S.P(th - .1, .25, back); S.$('#hf').style.opacity = clamp(o); S.$('#hf').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(th - .1)) S.sfx(th - .1, 'thud'); }},
 { // 7 prefetch next step
  html: `${PAGE(340)}<div class="abs" style="left:120px;right:120px;top:960px;padding:24px 30px;border-radius:18px;background:#16161a;box-shadow:0 0 0 1px rgba(255,255,255,.08)">
     <div style="font:600 32px Roboto;color:var(--mute);display:flex;justify-content:space-between"><span>🤫 quietly loading React for step 2</span><span id="pp">0%</span></div>
     <div style="height:20px;border-radius:10px;background:#2a2a31;margin-top:18px;overflow:hidden"><i id="pf" style="display:block;height:100%;background:var(--grn)"></i></div></div>`,
  draw(S) { const tq = S.T('quietly'), p = S.P(tq - .2, S.dur - tq, x => x); S.$('#pf').style.width = (100 * p) + '%'; S.$('#pp').textContent = Math.round(100 * p) + '%'; }},
 { // 8 lesson
  html: `<div class="abs center h2" style="top:520px">Ship <span class="mark" id="m0">less JavaScript.</span></div><div class="abs center h2" style="top:700px" id="l1">Hydrate only <span class="mark" id="m1">what needs it.</span></div>`,
  draw(S) { S.$('#m0').style.setProperty('--m', S.P(S.T('less') - .1, .3)); const th = S.T('hydrate'); S.$('#l1').style.opacity = S.P(th - .2, .2); S.$('#m1').style.setProperty('--m', S.P(S.T('needs') - .2, .3)); if (S.on(th)) S.sfx(th, 'ding'); }},
 ctaScene(),
];
