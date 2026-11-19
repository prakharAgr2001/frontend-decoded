// WR08 v2: Netflix landing page — client-side React swapped for plain JS (2017). TTI −50%, −200 KB; React prefetched for next steps.
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const PAGE = (top, id = 'pg') => `<div class="br" id="${id}" style="top:${top}px"><div class="bar"><span>netflix.com</span></div><div class="hero"><div class="t">Unlimited films,<br>series and more</div><div class="in"><span class="em"></span><b class="go">Get started ›</b></div></div></div>`;
const tapAt = (S, el, at, period = .6) => { const u = ((S.t - at) / period) % 1; el.style.opacity = S.on(at) ? 1 - u : 0; el.style.transform = `scale(${.5 + u})`; if (S.on(at)) S.sfx(at + Math.floor((S.t - at) / period) * period, 'click'); };
const SCENES = [
 { // 0 hook: 50% faster by throwing code away
  html: `<div class="abs center big" id="f50" style="top:330px;font-size:150px;color:var(--grn)">50% faster</div>
   <div class="abs center h2" id="by" style="top:560px;opacity:0">by throwing code <span class="mark">away</span></div>
   <div class="can"></div>${['react.js', 'lodash.js', 'app.js'].map((n, i) => `<div class="file f" style="left:${200 + i * 240}px;top:720px">${n}</div>`).join('')}`,
  draw(S) { const p = S.P(0, S.T('faster'), eo); S.$('#f50').textContent = Math.round(50 * p) + '% faster';
    const ta = S.T('throwing'); S.$('#by').style.opacity = S.P(ta - .2, .2);
    S.$$('.f').forEach((f, i) => { const q = S.P(ta + i * .15, .5, x => x * x); f.style.transform = `translate(${(480 - 200 - i * 240 - 60) * q}px,${300 * q}px) rotate(${q * (i - 1) * 40}deg) scale(${1 - .5 * q})`; f.style.opacity = 1 - clamp((q - .8) * 5); if (S.on(ta + i * .15)) S.sfx(ta + i * .15 + .4, 'thud'); }); }},
 { // 1 page shows, button dead
  html: `${PAGE(380)}<div class="tap" id="tp" style="left:640px;top:670px"></div>
   <div class="abs center" id="dead" style="top:900px;font:800 46px Roboto;color:var(--red);opacity:0">👆 tap… nothing happens</div>`,
  draw(S) { const ts = S.T('showed'); S.$('#pg').style.opacity = S.P(ts - .4, .3); const tb = S.T('button'); tapAt(S, S.$('#tp'), tb - .3); S.$('#dead').style.opacity = S.P(tb, .2); }},
 { // 2 just a picture, then download + run React
  html: `${PAGE(380)}${[[70, 360, 0], [950, 360, 90], [70, 790, 270], [950, 790, 180]].map(c => `<div class="corner" style="left:${c[0]}px;top:${c[1]}px;transform:rotate(${c[2]}deg);border-right:0;border-bottom:0"></div>`).join('')}
   <div class="abs" id="pic" style="left:110px;top:400px;padding:8px 20px;border-radius:10px;background:var(--yel);color:#111;font:800 34px Roboto;opacity:0">📸 just a picture</div>
   <div class="cmp" style="top:960px"><div class="l"><span class="mono" style="font-size:36px">⬇ react.js</span><span id="ph"></span></div><div class="t"><i id="pb" style="background:var(--yel)"></i></div></div>`,
  draw(S) { const tp = S.T('picture'); S.$('#pic').style.opacity = S.P(tp - .2, .2); S.$('#pg').style.filter = S.on(tp - .2) ? 'grayscale(1) brightness(.7)' : ''; if (S.on(tp - .2)) S.sfx(tp - .2, 'click');
    const td = S.T('download'), tr = S.T('run'); const run = S.on(tr - .1); const p = run ? S.P(tr - .1, S.dur - tr, x => x) : S.P(td - .2, tr - td + .1, x => x);
    S.$('#pb').style.width = (100 * p) + '%'; S.$('#pb').style.background = run ? 'var(--red)' : 'var(--yel)'; S.$('#ph').textContent = S.on(td - .2) ? (run ? 'running…' : 'downloading…') : ''; }},
 { // 3 hydration: add water
  html: `${PAGE(380)}<div class="abs" id="drop" style="left:500px;top:240px;font-size:90px">${EMO('droplet')}</div>
   <div class="abs center h" style="top:900px;font-size:120px"><span class="mark" id="mk">Hydration</span></div>
   <div class="abs center" id="sub" style="top:1060px;font:600 42px Roboto;color:var(--mute);opacity:0">add water → it comes alive</div>`,
  draw(S) { const th = S.T('hydration'), tw = S.T('water'); S.$('#mk').style.setProperty('--m', S.P(th - .1, .3)); if (S.on(th)) S.sfx(th, 'ding');
    const d = S.P(tw - .5, .5, x => x * x); S.$('#drop').style.top = (240 + 260 * d) + 'px'; S.$('#drop').style.opacity = d < 1 ? 1 : 0;
    const l = S.P(tw, .5); S.$('#pg').style.filter = `grayscale(${1 - l}) brightness(${.7 + .3 * l})`; S.$('#sub').style.opacity = S.P(tw - .2, .3); if (S.on(tw)) S.sfx(tw, 'pop'); }},
 { // 4 one job: email + button
  html: `${PAGE(340)}<div class="job j0" style="top:880px">✍️ type your email</div><div class="job j1" style="top:980px">👆 press a button</div>
   <div class="abs center kick" style="top:1120px" id="only">that's the whole job</div>`,
  draw(S) { const te = S.T('email'), tb = S.T('button'); S.$('.j0').style.opacity = S.P(te - .4, .2); S.$('.j1').style.opacity = S.P(tb - .4, .2);
    S.$('.em').style.boxShadow = S.on(te - .4) ? 'inset 0 0 0 4px var(--yel)' : ''; S.$('.go').style.boxShadow = S.on(tb - .4) ? '0 0 0 5px var(--yel)' : '';
    S.$('#only').style.opacity = S.P(S.T('job') - .2, .3); if (S.on(te - .4)) S.sfx(te - .4, 'pop'); if (S.on(tb - .4)) S.sfx(tb - .4, 'pop'); }},
 { // 5 why all of React for one button? (size comparison)
  html: `<div class="abs" id="L" style="left:110px;top:380px;width:520px;height:520px;border-radius:30px;background:#61dafb;color:#111;font:900 60px Roboto;display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center">ALL of React<span style="font:600 32px Roboto;margin-top:10px">+ libraries<br>~200 KB</span></div>
   <div class="abs" id="Rb" style="left:700px;top:600px;padding:16px 26px;border-radius:12px;background:#e50914;font:800 32px Roboto">Get started ›</div>
   <div class="abs" style="left:700px;top:680px;font:600 28px Roboto;color:var(--mute)" id="rl">the only thing<br>that needs it</div>
   <div class="abs center h2" id="q" style="top:1000px;opacity:0">…for <span class="mark">one button?</span></div>`,
  draw(S) { const ta = S.T('all'), p = S.P(ta - .3, .4, back); S.$('#L').style.transform = `scale(${.3 + .7 * clamp(p)})`; S.$('#L').style.opacity = clamp(p * 2); if (S.on(ta)) S.sfx(ta, 'thud');
    const to = S.T('one'); S.$('#Rb').style.opacity = S.P(to - .4, .2); S.$('#rl').style.opacity = S.P(to - .2, .2); S.$('#q').style.opacity = S.P(to - .2, .25); }},
 { // 6 plain JS, -200 KB
  html: `<div class="edit" style="top:360px;font-size:36px"><div style="color:#888">// plain JavaScript</div><div>button.onclick = () =&gt; {</div><div>&nbsp;&nbsp;goToStep2(email.value);</div><div>};</div></div>
   <div class="abs center big" id="kb" style="top:800px;font-size:160px;color:var(--red);opacity:0">−200 KB</div>`,
  draw(S) { S.$$('.edit div').forEach((d, i) => d.style.opacity = S.P(i * .2, .2)); const tk = S.T('kilobytes'); const o = S.P(tk - .4, .25, back); S.$('#kb').style.opacity = clamp(o); S.$('#kb').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(tk - .4)) S.sfx(tk - .4, 'thud'); }},
 { // 7 half the time (drop)
  html: `<div class="abs center kick" style="top:420px">time until the button works</div>
   <div class="cmp" style="top:540px"><div class="l"><span>before</span><span>🐢</span></div><div class="t"><i style="background:var(--red);width:100%"></i></div></div>
   <div class="cmp" style="top:740px"><div class="l"><span>after</span><span>⚡</span></div><div class="t"><i id="ab" style="background:var(--grn)"></i></div></div>
   <div class="abs center big" id="hf" style="top:940px;font-size:150px;color:var(--grn);opacity:0">2× faster</div>`,
  draw(S) { if (S.t < .07) flash(.5); const th = S.T('half'), p = S.P(.1, th, eio); S.$('#ab').style.width = (100 - 50 * p) + '%';
    const o = S.P(th - .1, .25, back); S.$('#hf').style.opacity = clamp(o); S.$('#hf').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(th - .1)) S.sfx(th - .1, 'thud'); }},
 { // 8 React loads quietly for the next page
  html: `${PAGE(340)}<div class="abs" style="left:120px;right:120px;top:900px;padding:24px 30px;border-radius:18px;background:#16161a;box-shadow:0 0 0 1px rgba(255,255,255,.08)">
     <div style="font:600 34px Roboto;color:var(--mute);display:flex;justify-content:space-between"><span>🤫 React, for the next page</span><span id="pp">0%</span></div>
     <div style="height:20px;border-radius:10px;background:#2a2a31;margin-top:18px;overflow:hidden"><i id="pf" style="display:block;height:100%;background:var(--grn)"></i></div></div>`,
  draw(S) { const tq = S.T('quietly'), p = S.P(tq - .3, S.dur - tq, x => x); S.$('#pf').style.width = (100 * p) + '%'; S.$('#pp').textContent = Math.round(100 * p) + '%'; }},
 { // 9 lesson
  html: `<div class="abs center h2" style="top:470px">Don't ship a <span class="mark" id="m0">whole engine</span></div><div class="abs center h2" style="top:590px" id="l1">for one button.</div>
   <div class="abs center" style="top:800px;font-size:160px" id="ic">🚂 <span style="font-size:80px">vs</span> 🔘</div>`,
  draw(S) { const tw = S.T('whole'); S.$('#m0').style.setProperty('--m', S.P(tw - .1, .3)); S.$('#l1').style.opacity = S.P(S.T('button') - .3, .2); S.$('#ic').style.opacity = S.P(tw, .3); if (S.on(tw)) S.sfx(tw, 'ding'); }},
 ctaScene(),
];
