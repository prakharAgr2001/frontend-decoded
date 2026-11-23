// WR29: Zune 30GB leap-year freeze, 31 Dec 2008 (clock-driver loop never ends on day 366). Generic player drawn, no product design copied.
const PLAYER = `<div class="pl"><div class="scr" id="sc"><div class="ld"><i></i><i></i><i></i></div><span>loading…</span></div><div class="wheel"></div></div>`;
const CODE = `<span class="k">while</span> (days > 365) {
  <span class="k">if</span> (<span class="f">isLeap</span>(year)) {
    <span class="k">if</span> (days > 366) {
      days -= 366; year++
    }
    <span class="c" id="c1">// days == 366 ? nothing.</span>
  } <span class="k">else</span> {
    days -= 365; year++
  }
}`;
const SCENES = [
 { // 0 hook: many players frozen
  html: `<div class="abs center kick" style="top:380px">31 December 2008</div><div class="grid">${[...Array(12)].map(() => `<div class="mini"><div class="ms2"></div></div>`).join('')}</div>`,
  draw(S) { const tf = TT(S, 'froze', .4); S.$$('.mini').forEach((m, i) => { const f = S.on(tf + i * .04); m.classList.toggle('fz', f); }); if (S.on(tf)) S.sfx(tf, 'thud'); if (S.t > tf && S.t < tf + .08) flash(.4); }},
 { // 1 stuck on loading
  html: `${PLAYER}<div class="abs center lab" style="top:1380px;font-size:40px">30 GB model · stuck</div>`,
  draw(S) { S.$$('.ld i').forEach((d, i) => d.style.opacity = .3 + .7 * (Math.floor(S.t * 3) % 3 === i)); }},
 { // 2 loop code
  html: `${WIN('clock_driver.c (simplified)', CODE)}`,
  init(el) { el.querySelector('.win').style.top = '420px'; el.querySelector('.wb').style.fontSize = '34px'; },
  draw(S) {}},
 { // 3 day 366
  html: `<div class="abs center kick" style="top:400px">2008 was a leap year</div><div class="abs center big" id="d" style="top:500px;font-size:220px">day 360</div>
   <div class="rules"><div class="rule" id="r1">days > 366 ? <b>no</b></div><div class="rule" id="r2">days > 365 ? <b>yes, keep looping</b></div></div>`,
  draw(S) { const t = TT(S, '366', .5), n = Math.min(366, 360 + Math.floor(6 * S.P(0, t, x => x))); S.$('#d').textContent = 'day ' + n; S.$('#d').style.color = n === 366 ? 'var(--red)' : 'var(--paper)'; IN(S, '#r1', t + .2); IN(S, '#r2', t + .6); }},
 { // 4 infinite loop
  html: `<svg class="abs" style="left:290px;top:480px" width="500" height="500" viewBox="0 0 100 100"><circle cx="50" cy="50" r="38" fill="none" stroke="#2a2a31" stroke-width="8"/><circle id="sp" cx="50" cy="50" r="38" fill="none" stroke="#ff3b3b" stroke-width="8" stroke-dasharray="60 180" stroke-linecap="round"/></svg>
   <div class="abs center big" style="top:640px;font-size:150px">∞</div><div class="abs center big" id="it" style="top:1080px;font-size:80px;color:var(--mute)">loop #0</div>`,
  draw(S) { S.$('#sp').setAttribute('transform', `rotate(${S.t * 720} 50 50)`); S.$('#it').textContent = 'loop #' + fmt(Math.pow(10, 1 + 5 * S.t / S.dur)); if (Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); }},
 { // 5 wait until tomorrow
  html: `<div class="cal"><div class="ch">DEC 2008</div><div class="cday" id="cd">31</div></div><div class="abs center h2" id="w" style="top:1150px;opacity:0">official fix: <span class="mark" id="mk">wait</span></div>`,
  draw(S) { const tt = TT(S, 'tomorrow', .7); IN(S, '#w', TT(S, 'fix', .3)); MK(S, '#mk', TT(S, 'Wait', .5)); const n = S.on(tt); S.$('#cd').textContent = n ? '1' : '31'; S.$('.ch').textContent = n ? 'JAN 2009' : 'DEC 2008'; if (S.on(tt)) S.sfx(tt, 'ding'); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:470px;font-size:96px">One missing<br><span class="mark" id="mk">edge case</span></div><div class="abs center h2" id="l2" style="top:820px;opacity:0">every device · same day</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'edge', .3)); IN(S, '#l2', TT(S, 'Every', .6) - .2); }},
 ctaScene(),
];
