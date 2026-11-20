// WR18: the Year 2038 problem (signed 32-bit Unix time)
const MAX = 2147483647;
const CLOCK = `<div class="clk"><div class="cd" id="dt">19 Jan 2038</div><div class="ct" id="tm">03:14:05</div><div class="lab">UTC</div></div>`;
const DEV = (ic, name, ok) => `<div class="tile dev"><div style="font-size:90px">${ic}</div><div class="nm">${name}</div><div class="ok ${ok ? 'g' : 'r'}">${ok ? '✓ 64-bit' : '⚠ 32-bit?'}</div></div>`;
const SCENES = [
 { // 0 hook
  html: `${CLOCK}<div class="abs center h" id="hk" style="top:1020px;font-size:84px">some computers will<br>think it's <span class="mark" id="mk">1901</span></div>`,
  draw(S) { const tf = TT(S, '1901', .7); const flip = S.on(tf - .3); S.$('#dt').textContent = flip ? '13 Dec 1901' : '19 Jan 2038'; S.$('#tm').textContent = flip ? '20:45:52' : '03:14:0' + Math.min(7, 5 + Math.floor(S.t));
    S.$('.clk').style.boxShadow = flip ? '0 0 0 5px var(--red),0 0 100px rgba(255,59,59,.5)' : ''; S.$('#dt').style.color = flip ? 'var(--red)' : 'var(--paper)'; if (S.on(tf - .3)) S.sfx(tf - .3, 'thud'); MK(S, '#mk', tf); SHAKE(S, '.clk', tf - .3); }},
 { // 1 seconds since 1970
  html: `<div class="abs center kick" style="top:420px">seconds since 1 Jan 1970</div><div class="tile" style="left:90px;right:90px;top:520px;height:280px;display:flex;align-items:center;justify-content:center"><span class="num" id="c" style="font-size:120px">0</span></div>
   <div class="abs center lab" style="top:880px;font-size:40px">that's how many systems store "now"</div>`,
  draw(S) { COUNT(S, '#c', 0, 1.79e9, 0, S.dur - .3, fmt, eo); if (Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); }},
 { // 2 32 switches
  html: `<div class="abs center h2" style="top:380px">a signed <span class="mark" id="mk">32-bit</span> number</div><div class="abs center" style="top:560px">${SWITCHES(32, 8)}</div>
   <div class="abs center big" id="mx" style="top:1050px;font-size:96px">0</div><div class="abs center lab" style="top:1170px">biggest value it can hold</div>`,
  draw(S) { MK(S, '#mk', .1); const n = Math.round(31 * S.P(.3, S.dur - .8, x => x)); SETSW(S, n); if (n > (this.l || 0)) S.sfx(S.t, 'click'); this.l = n; S.$('#mx').textContent = fmt(Math.pow(2, n) - 1); S.$('#mx').style.color = n >= 31 ? 'var(--yel)' : 'var(--paper)'; }},
 { // 3 runs out at...
  html: `<div class="abs center kick" style="top:420px">it runs out at</div>${CLOCK}<div class="abs center num" id="v" style="top:1040px;font-size:80px;color:var(--yel)">2,147,483,647</div>`,
  init(el) { el.querySelector('.clk').style.top = '520px'; },
  draw(S) { const s = Math.min(7, Math.floor(S.P(0, S.dur - .4, x => x) * 8)); S.$('#tm').textContent = '03:14:0' + s; S.$('#v').textContent = fmt(MAX - 7 + s); if (s !== this.s) S.sfx(S.t, 'tick'); this.s = s; }},
 { // 4 flips negative
  noFlash: true,
  html: `<div class="redbg" id="rb"></div><div class="abs center kick" style="top:420px;color:#ffd6d6">one second later</div>
   <div class="abs center num" id="v" style="top:560px;font-size:90px;color:#fff">2,147,483,647</div><div class="abs center" style="top:700px;font-size:70px">↓</div>
   <div class="abs center h" id="yr" style="top:840px;font-size:150px;color:#fff;opacity:0">1901</div>`,
  draw(S) { const tn = TT(S, 'negative', .3); const neg = S.on(tn - .2); S.$('#v').textContent = neg ? '−2,147,483,648' : '2,147,483,647'; S.$('#rb').style.opacity = neg ? 1 : 0; if (neg) S.sfx(tn - .2, 'thud'); if (S.t > tn - .2 && S.t < tn - .1) flash(.6);
    POP(S, '#yr', TT(S, '1901', .8) - .2, 'buzz'); }},
 { // 5 devices
  html: `<div class="devs">${DEV(EMO('mobile-phone'), 'phones', 1)}${DEV(EMO('high-voltage'), 'modern servers', 1)}${DEV(EMO('alarm-clock'), 'old devices', 0)}${DEV(EMO('robot'), 'embedded chips', 0)}</div>`,
  draw(S) { const tm = TT(S, 'Old', .55); S.$$('.dev').forEach((d, i) => { const at = i < 2 ? .1 + i * .2 : tm + (i - 2) * .25; const p = S.P(at, .3, back); d.style.opacity = clamp(p); d.style.transform = `scale(${.8 + .2 * clamp(p)})`; if (S.on(at)) S.sfx(at, i < 2 ? 'pop' : 'buzz'); }); }},
 { // 6 same number as YouTube
  html: `<div class="abs center h2" style="top:420px">sound familiar?</div><div class="abs center num" style="top:600px;font-size:110px;color:var(--yel)">2,147,483,647</div>
   <div class="tile" id="yt" style="left:160px;right:160px;top:820px;height:300px;padding:40px;opacity:0"><div style="height:140px;border-radius:14px;background:linear-gradient(135deg,#ff4fa0,#7b5cff)"></div><div style="font:500 40px Roboto;margin-top:26px">2,147,483,647 views</div></div>
   <div class="abs center h2" id="br" style="top:1200px;opacity:0">the number that almost broke YouTube</div>`,
  draw(S) { IN(S, '#yt', TT(S, 'number', .5) - .2); POP(S, '#br', TT(S, 'YouTube', .85) - .3, 'ding'); }},
 ctaScene(),
];
