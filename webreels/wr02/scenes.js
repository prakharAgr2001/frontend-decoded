// WR02: one update crashed 8.5 million PCs (CrowdStrike, 19 July 2024)
const ICON = {
  plane: `<svg viewBox="0 0 24 24" fill="none" stroke="#ffd23f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 16l20-6-2-2-8 2-5-6H5l3 7-4 1-2-2H1l1 6z"/><path d="M2 21h20"/></svg>`,
  hosp: `<svg viewBox="0 0 24 24" fill="none" stroke="#ff3b3b" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M12 7v10M7 12h10"/></svg>`,
  tv: `<svg viewBox="0 0 24 24" fill="none" stroke="#4c9dff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="14" rx="2"/><path d="M8 2l4 4 4-4M5 9l14 8M19 9L5 17"/></svg>`,
};
const FLIGHTS = [['AI 302', 'MUMBAI'], ['6E 119', 'DELHI'], ['UK 851', 'GOA'], ['AI 640', 'PUNE'], ['6E 772', 'CHENNAI'], ['QP 103', 'KOLKATA'], ['SG 415', 'JAIPUR']];
const laps = n => '<div style="width:910px;margin:0 auto;line-height:0">' + '<span class="lap"><span class="sc"></span><span class="bs"></span></span>'.repeat(n) + '</div>';

const SCENES = [
 { // 0 HOOK: one update, screens die, counter
  html: `<div class="h abs center" style="top:280px;font-size:118px" id="hd"><span class="mark" id="mk">One update.</span></div>
   <div class="abs" id="lp" style="left:0;right:0;top:500px">${laps(30)}</div>
   <div class="abs center big" id="cnt" style="top:1130px;color:var(--red)"></div>
   <div class="abs center" style="top:1290px;font:700 40px Roboto;letter-spacing:4px">COMPUTERS</div>
   <div class="abs center h" id="dead" style="top:1360px;font-size:150px;color:var(--red);opacity:0">Dead.</div>`,
  draw(S) {
    S.$('#mk').style.setProperty('--m', eo(lin(S.t, -.2, .3)));
    S.$$('.lap').forEach((l, i) => { const on = S.t > -0.2 + i * .045; l.classList.toggle('down', on); l.querySelector('.sc').textContent = on ? ':(' : ''; });
    S.$('#cnt').textContent = fmt(8500000 * S.P(0, S.T('computers'), eo));
    const td = S.T('Dead'), o = S.P(td, .18); S.$('#dead').style.opacity = o; S.$('#dead').style.transform = `scale(${1.3 - .3 * o})`; if (S.on(td)) S.sfx(td, 'thud');
  }},
 { // 1 airport board
  html: `<div class="abs center kick" style="top:470px">July 2024 · you're at the airport</div>
   <div class="board" style="top:560px"><div class="hd"><span>DEPARTURES</span><span>09:41</span></div>
     ${FLIGHTS.map(f => `<div class="fl"><span class="cell">${f[0]}</span><span class="cell">${f[1]}</span><span class="cell st">CANCELLED</span></div>`).join('')}</div>`,
  draw(S) {
    const tc = S.T('cancelled'); S.$$('.fl').forEach((r, i) => { const on = S.t > tc - .9 + i * .1; r.querySelector('.st').textContent = on ? 'CANCELLED' : 'ON TIME'; r.querySelector('.st').style.color = on ? 'var(--red)' : 'var(--grn)'; if (on) S.sfx(tc - .9 + i * .1, 'click'); });
    if (S.t > tc) S.$$('.st').forEach(c => c.style.opacity = Math.floor(S.t * 5) % 2 ? 1 : .4);
  }},
 { // 2 hospitals + TV
  html: ['hosp|Hospitals postpone|appointments', 'tv|TV channels off air|live broadcasts dropped'].map((x, i) => {
     const [ic, a, b] = x.split('|'); return `<div class="news n${i}" style="top:${620 + i * 260}px">${ICON[ic]}<div><div class="tx">${a}</div><div class="sub">${b}</div></div></div>`; }).join(''),
  draw(S) { ['Hospitals', 'TV'].forEach((w, i) => { const at = S.T(w) - .15, p = S.P(at, .3); const n = S.$('.n' + i); n.style.opacity = p; n.style.transform = `translateX(${(1 - p) * 140}px)`; if (S.on(at)) S.sfx(at, 'swish'); }); }},
 { // 3 the cause: deepest layer
  html: `<div class="abs center kick" style="top:440px">The cause</div>
   <div class="layer" id="l0" style="top:540px;background:#1d1d23">Your apps<small>Chrome, Excel…</small></div>
   <div class="layer" id="l1" style="top:710px;background:#22222a">Windows<small>the operating system</small></div>
   <div class="layer" id="l2" style="top:880px;background:var(--red);color:#fff">CrowdStrike<small>deepest layer</small></div>
   <div class="abs center mono" id="file" style="top:1110px;font-size:40px;color:var(--yel);opacity:0">📄 C-00000291*.sys</div>`,
  draw(S) {
    ['#l0', '#l1', '#l2'].forEach((s, i) => { const p = S.P(i * .15, .3); S.$(s).style.opacity = p; S.$(s).style.transform = `translateY(${(1 - p) * 40}px)`; });
    const td = S.T('deepest'); S.$('#l2').style.boxShadow = S.on(td) ? `0 0 ${40 + 20 * Math.sin(S.t * 8)}px rgba(255,59,59,.7)` : '';
    const tf = S.T('file'); S.$('#file').style.opacity = S.P(tf, .25); if (S.on(td)) S.sfx(td, 'thud');
  }},
 { // 4 to everyone at once: ripple
  html: `<div class="abs center h2" style="top:400px">To everyone. <i style="color:var(--yel)">At once.</i></div>
   <canvas class="dotmap" width="900" height="700" style="top:560px"></canvas>`,
  draw(S) {
    const g = S.$('canvas').getContext('2d'); g.clearRect(0, 0, 900, 700); const r = 1100 * S.P(0, S.dur, x => x);
    for (let y = 0; y < 22; y++) for (let x = 0; x < 28; x++) {
      const px = 20 + x * 31.5 + (y % 2) * 15, py = 20 + y * 31; if (Math.hypot((px - 450) / 450, (py - 350) / 330) > 1.02) continue;
      g.fillStyle = Math.hypot(px - 450, py - 350) < r ? '#ff3b3b' : '#3a3a42'; g.beginPath(); g.arc(px, py, 6, 0, 7); g.fill(); }
    g.strokeStyle = 'rgba(255,210,63,.7)'; g.lineWidth = 5; g.beginPath(); g.arc(450, 350, r, 0, 7); g.stroke();
    g.fillStyle = '#ffd23f'; g.beginPath(); g.arc(450, 350, 16, 0, 7); g.fill(); S.sfx(0.05, 'whoosh');
  }},
 { // 5 crash loop (drop)
  noFlash: true,
  html: `<div class="bsod"><div class="f">:(</div><div class="m">Something went wrong.<br>Restarting…</div><div class="r" id="lc"></div></div>`,
  draw(S) {
    const cyc = Math.floor(S.t / .55), ph = (S.t % .55) / .55; S.$('.bsod').style.opacity = ph < .12 ? .15 : 1;
    S.$('#lc').textContent = 'crash #' + (cyc + 1); S.sfx(cyc * .55, 'buzz'); if (S.t < .07) flash(.5);
  }},
 { // 6 78 minutes + fixed by hand
  html: `<div class="abs" style="left:100px;top:470px"><div class="clock">04:09</div><div style="font:500 30px Roboto;color:var(--mute);margin-top:8px">update ships</div></div>
   <div class="abs" style="right:100px;top:470px;text-align:right"><div class="clock" style="color:var(--grn)">05:27</div><div style="font:500 30px Roboto;color:var(--mute);margin-top:8px">pulled</div></div>
   <div class="abs" style="left:100px;right:100px;top:690px;height:18px;border-radius:9px;background:#2a2a31"><div id="bar" style="height:100%;border-radius:9px;background:var(--red);width:0"></div></div>
   <div class="abs center" id="mins" style="top:740px;font:700 52px Roboto"></div>
   <div class="abs center h2" id="hand" style="top:900px;opacity:0">…but fixed <span class="mark">by hand</span></div>
   <div class="abs center big" id="x" style="top:1080px;font-size:120px;color:var(--yel);opacity:0">× 8,500,000</div>`,
  draw(S) {
    const p = S.P(0, S.T('minutes'), eio); S.$('#bar').style.width = (100 * p) + '%'; S.$('#mins').textContent = Math.round(78 * p) + ' minutes';
    const th = S.T('hand'); S.$('#hand').style.opacity = S.P(th - .5, .25); const o = S.P(th - .1, .3, back); S.$('#x').style.opacity = clamp(o); S.$('#x').style.transform = `scale(${.8 + .2 * o})`; if (S.on(th - .1)) S.sfx(th - .1, 'thud');
  }},
 { // 7 rings: 1% first
  html: `<div class="ring" id="r2" style="left:90px;top:440px;width:900px;height:900px"><span>everyone</span></div>
   <div class="ring" id="r1" style="left:290px;top:640px;width:500px;height:500px"><span>10%</span></div>
   <div class="ring" id="r0" style="left:440px;top:790px;width:200px;height:200px"><span>1%</span></div>
   <div class="abs" id="bug" style="left:520px;top:870px;width:40px;height:40px;border-radius:50%;background:var(--red);box-shadow:0 0 30px var(--red);opacity:0"></div>
   <div class="abs center" id="ok" style="top:1390px;font:700 44px Roboto;opacity:0">only <span style="color:var(--yel)">1%</span> breaks</div>`,
  draw(S) {
    const t1 = S.T('one'), tb = S.T('breaks');
    const set = (id, on, col) => { const r = S.$(id); r.style.borderColor = on ? col : '#33333a'; r.style.background = on ? 'rgba(255,210,63,.08)' : 'transparent'; r.querySelector('span').style.color = on ? col : 'var(--mute)'; };
    set('#r0', S.on(t1), '#ffd23f'); set('#r1', false); set('#r2', false); if (S.on(t1)) S.sfx(t1, 'pop');
    S.$('#bug').style.opacity = S.on(tb) ? .5 + .5 * Math.sin(S.t * 12) : 0; S.$('#ok').style.opacity = S.P(S.T('breaks', 2) - .2, .25);
    if (S.on(tb)) S.$('#r0').style.borderColor = 'var(--red)';
  }},
 { // 8 name it
  html: `<div class="abs center kick" style="top:560px">It's called</div><div class="h abs center" style="top:650px;font-size:130px">a <span class="mark" id="mk8">staged rollout</span></div>`,
  draw(S) { S.$('#mk8').style.setProperty('--m', S.P(S.T('staged') - .1, .3)); if (S.on(S.T('staged'))) S.sfx(S.T('staged'), 'ding'); }},
 ctaScene(),
];
