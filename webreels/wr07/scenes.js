// WR07: Pinterest's 23-second wait (old mobile web vs 2017 PWA; Addy Osmani case study)
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const PCOL = ['#e8c4b8', '#b8d4e8', '#d8e8b8', '#e8d8b8', '#c8b8e8', '#b8e8d8', '#e8b8c8', '#d0d0d0'];
const PINS = () => `<div class="pins">${[260, 180, 320, 220, 280, 200, 240, 300].map((h, i) => `<i style="height:${h}px;background:${PCOL[i]}"></i>`).join('')}</div><div style="position:absolute;left:0;right:0;top:0;height:80px;background:#fff;display:flex;align-items:center;padding-left:30px;font:800 34px Roboto;color:#e60023">Pinterest<span style="margin-left:auto;margin-right:30px;font:700 26px Roboto;color:#888" class="net">3G</span></div>`;
const SCENES = [
 { // 0 23 seconds, taps do nothing
  html: `<div class="phone" style="left:280px;top:480px">${PINS()}</div><div class="abs center big" id="tm" style="top:300px;font-size:150px;color:var(--yel)">0s</div>
   <div class="tap" id="tp" style="opacity:0"></div>`,
  draw(S) { const p = S.P(0, S.T('seconds'), x => x); S.$('#tm').textContent = Math.round(23 * eo(p)) + 's'; S.$('#tm').style.color = p > .9 ? 'var(--red)' : 'var(--yel)';
    S.$('.phone').style.filter = 'grayscale(.6)'; const ta = S.T('tap'); const k = Math.floor((S.t - ta) / .45), u = ((S.t - ta) / .45) % 1;
    const tp = S.$('#tp'); if (S.on(ta)) { const P = [[440, 800], [620, 1050], [460, 1250], [600, 700]][k % 4]; tp.style.left = P[0] + 'px'; tp.style.top = P[1] + 'px'; tp.style.opacity = 1 - u; tp.style.transform = `scale(${.5 + u})`; S.sfx(ta + k * .45, 'click'); } }},
 { // 1 3G, frozen
  html: `<div class="phone" style="left:280px;top:420px">${PINS()}<div id="ice" style="position:absolute;inset:0;background:linear-gradient(160deg,rgba(150,210,255,.55),rgba(220,240,255,.25));opacity:0"></div></div>
   <div class="stamp" id="fz" style="left:330px;top:820px;opacity:0;color:#6cc7ff;border-color:#6cc7ff">FROZEN</div>`,
  draw(S) { const t3 = S.T('3g'); S.$('.net').style.color = S.on(t3 - .2) ? 'var(--red)' : '#888'; const tf = S.T('frozen'); S.$('#ice').style.opacity = S.P(tf - .3, .3);
    const o = S.P(tf - .2, .2, back); S.$('#fz').style.opacity = clamp(o); S.$('#fz').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tf - .2)) S.sfx(tf - .2, 'thud'); }},
 { // 2 2.5 MB of JS, CPU maxed
  html: `<div class="js" id="blk" style="left:140px;right:140px;top:360px;height:520px;background:var(--yel);flex-direction:column;font-size:44px">bundle.js<span style="font:900 120px Roboto;margin-top:10px" id="mb">0 MB</span></div>
   <div class="cmp" style="top:960px"><div class="l"><span>📱 phone CPU</span><span id="cpu">0%</span></div><div class="t"><i id="cb" style="background:var(--red)"></i></div></div>
   <div class="abs center mono" id="chew" style="top:1170px;font-size:38px;color:var(--mute)"></div>`,
  draw(S) { const tm = S.T('megabytes'), p = S.P(tm - 1, 1, eo); S.$('#mb').textContent = (2.5 * p).toFixed(1) + ' MB'; S.$('#blk').style.transform = `scale(${.6 + .4 * p})`;
    const tc = S.T('chew'), c = S.P(tc - .3, .5); S.$('#cb').style.width = (100 * c) + '%'; S.$('#cpu').textContent = Math.round(100 * c) + '%';
    S.$('#chew').textContent = S.on(tc) ? 'parsing' + '.'.repeat(1 + Math.floor(S.t * 4) % 3) + ' compiling' + '.'.repeat(1 + Math.floor(S.t * 3) % 3) : ''; if (S.on(tc)) S.sfx(tc, 'buzz'); }},
 { // 3 split the code
  html: `${['home', 'pin', 'search', 'profile', 'boards', 'settings'].map((n, i) => `<div class="js c" style="left:${140 + (i % 2) * 410}px;top:${380 + Math.floor(i / 2) * 190}px;width:390px;height:170px;background:var(--yel)">${n}.js</div>`).join('')}
   <div class="abs center" id="only" style="top:1020px;font:700 44px Roboto;opacity:0">this page needs: <span style="color:var(--grn)">pin.js only</span></div>`,
  draw(S) { const ts = S.T('split'); const sp = S.P(ts - .1, .4, back); S.$$('.c').forEach((c, i) => { const col = i % 2, row = Math.floor(i / 2);
      c.style.transform = `translate(${(col ? 1 : -1) * 20 * clamp(sp) - (col ? 205 : -205) * (1 - clamp(sp))}px,${(row - 1) * 20 * clamp(sp) - (row - 1) * 190 * (1 - clamp(sp))}px)`;
      const on = S.on(S.T('only')); c.style.opacity = on && i !== 1 ? .2 : 1; c.style.boxShadow = on && i === 1 ? '0 0 0 6px var(--grn),0 0 40px rgba(61,220,132,.6)' : ''; });
    if (S.on(ts)) S.sfx(ts, 'swish'); S.$('#only').style.opacity = S.P(S.T('only') - .1, .25); }},
 { // 4 620 KB -> 150 KB
  html: `<div class="abs center kick" style="top:420px">main JavaScript bundle</div><div class="abs center big" id="kb" style="top:500px;font-size:190px"></div>
   <div class="abs" style="left:110px;right:110px;top:800px;height:90px;border-radius:45px;background:#2a2a31;overflow:hidden"><i id="kbb" style="display:block;height:100%;background:var(--yel);border-radius:45px"></i></div>`,
  draw(S) { const td = S.T('down'), p = S.P(td - .2, .8, eio); const v = 620 - 470 * p; S.$('#kb').textContent = Math.round(v) + ' KB'; S.$('#kb').style.color = p > .95 ? 'var(--grn)' : 'var(--paper)'; S.$('#kbb').style.width = (100 * v / 620) + '%'; if (S.on(td)) S.sfx(td, 'whoosh'); }},
 { // 5 23s -> under 6 (drop)
  html: `<div class="abs center big" id="old" style="top:380px;font-size:170px;color:var(--red)"><span class="strike">23s</span></div><div class="abs center big" id="new" style="top:700px;font-size:260px;color:var(--grn);opacity:0">5.6s</div>
   <div class="abs center" style="top:1030px;font:600 36px Roboto;color:var(--mute)">time until you can tap · avg Android, 3G</div>`,
  draw(S) { if (S.t < .07) flash(.5); const tu = S.T('under'); const o = S.P(tu - .2, .25, back); S.$('#new').style.opacity = clamp(o); S.$('#new').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(tu - .2)) S.sfx(tu - .2, 'thud');
    S.$('#old').style.textDecoration = S.on(tu - .2) ? 'line-through' : ''; S.$('#old').style.opacity = S.on(tu - .2) ? .5 : 1; }},
 { // 6 +40% / +44%
  html: `<div class="stat s0" style="top:420px"><div class="v" id="v0">+0%</div><div class="l">time spent on the site</div></div><div class="stat s1" style="top:720px"><div class="v" id="v1">+0%</div><div class="l">ad revenue from users</div></div>`,
  draw(S) { [['forty', 0, 40], ['forty-four', 1, 44]].forEach(([w, i, n]) => { const at = S.T(w) - .4, p = S.P(at, .5); S.$('.s' + i).style.opacity = S.P(at, .2); S.$('#v' + i).textContent = '+' + Math.round(n * p) + '%'; if (S.on(at)) S.sfx(at, 'pop'); }); }},
 { // 7 name
  html: `<div class="abs center kick" style="top:520px">It's called</div><div class="h abs center" style="top:610px;font-size:130px"><span class="mark" id="mk">code splitting</span></div>
   <div class="abs center" id="sub" style="top:820px;font:600 44px Roboto;color:var(--mute);opacity:0">ship only what the page needs ✂️</div>`,
  draw(S) { const tc = S.T('code'); S.$('#mk').style.setProperty('--m', S.P(tc - .1, .35)); if (S.on(tc)) S.sfx(tc, 'ding'); S.$('#sub').style.opacity = S.P(S.T('ship') - .2, .3); }},
 ctaScene(),
];
