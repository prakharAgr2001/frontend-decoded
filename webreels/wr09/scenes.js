// WR09: Yahoo! JAPAN News CLS fix (web.dev case study): CLS ~0.2 -> ~0, +15.1% page views/session, +13.3% session length
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const TOPBAR = `<div style="position:absolute;left:0;right:0;top:0;height:80px;background:#fff;display:flex;align-items:center;padding-left:30px;font:800 32px Roboto;color:#222;box-shadow:0 2px 0 #ddd">📰 News</div>`;
const SCENES = [
 { // 0 tap link, page jumps, hit ad
  html: `<div class="phone" style="left:280px;top:330px">${TOPBAR}<div class="art"><div class="ad" id="ad" style="height:0">AD · BUY NOW</div><div class="ln"></div><div class="ln" style="width:80%"></div><div class="lk">Read the full story →</div><div class="ln"></div><div class="ln" style="width:70%"></div><div class="ln"></div></div></div>
   <div class="abs" id="fg" style="left:600px;top:700px;font-size:110px">${EMO('backhand-index-pointing-down')}</div><div class="tap" id="tp" style="left:560px;top:620px;opacity:0"></div>
   <div class="abs center" id="mad" style="top:1360px;font-size:120px;opacity:0">${EMO('pouting-face')}</div>`,
  draw(S) { const tj = S.T('jumps'), j = S.P(tj - .1, .18, back); S.$('#ad').style.height = (230 * clamp(j)) + 'px'; S.$('#ad').style.marginBottom = (16 * clamp(j)) + 'px'; if (S.on(tj)) S.sfx(tj, 'thud');
    S.$('#fg').style.top = (700 - 120 * S.P(0, S.T('tap') + .3, eo)) + 'px'; const ta = S.T('ad'), u = S.P(ta - .3, .4, x => x); S.$('#tp').style.opacity = S.on(ta - .3) ? 1 - u : 0; S.$('#tp').style.transform = `scale(${.5 + u})`; if (S.on(ta - .3)) S.sfx(ta - .3, 'click');
    S.$('#mad').style.opacity = S.P(ta, .2); }},
 { // 1 layout shift, Google measures it
  html: `<div class="abs center kick" style="top:420px">that jump has a name</div><div class="h abs center" style="top:510px;font-size:130px"><span class="mark" id="mk">Layout shift</span></div>
   <div class="abs center" id="g" style="top:760px;font:700 46px Roboto;opacity:0">📏 and Google measures it</div>`,
  draw(S) { const tl = S.T('layout'); S.$('#mk').style.setProperty('--m', S.P(tl - .1, .3)); S.$('.h').style.transform = `translateY(${Math.round(Math.sin(S.t * 18) * 10 * Math.max(0, 1 - Math.abs(S.t - tl - .5)))}px)`; if (S.on(tl)) S.sfx(tl, 'swish');
    S.$('#g').style.opacity = S.P(S.T('measures') - .3, .25); }},
 { // 2 Yahoo Japan, 22B views, jumping
  html: `<div class="abs center kick" style="top:380px">Yahoo! JAPAN News</div><div class="abs center big" id="pv" style="top:460px;font-size:120px;color:var(--yel)"></div>
   <div class="abs center" style="top:610px;font:600 36px Roboto;color:var(--mute)">page views every month</div>
   <div class="phone" style="left:280px;top:720px;height:640px">${TOPBAR}<div class="art"><div class="ln"></div><div class="ln" style="width:80%"></div><div class="ln"></div><div class="ln" style="width:60%"></div><div class="ln"></div></div></div>`,
  draw(S) { const tb = S.T('billion'); S.$('#pv').textContent = fmt(22e9 * S.P(0, tb, eo)); const tj = S.T('jumping'); const on = S.on(tj - .2);
    S.$('.art').style.transform = on ? `translateY(${Math.round(Math.abs(Math.sin(S.t * 9)) * 60)}px)` : ''; if (on) S.sfx(tj - .2, 'buzz'); }},
 { // 3 culprit: late images push text
  html: `<div class="phone" style="left:280px;top:340px">${TOPBAR}<div class="art"><div class="img" id="im" style="height:0"></div><div class="ln"></div><div class="ln" style="width:80%"></div><div class="ln"></div><div class="ln" style="width:70%"></div><div class="ln"></div><div class="ln" style="width:60%"></div></div></div>
   <div class="abs" id="ar" style="left:830px;top:700px;font:900 120px Roboto;color:var(--red);opacity:0">↓</div>`,
  draw(S) { const tl = S.T('late'), p = S.P(tl - .2, .3, back); S.$('#im').style.height = (320 * clamp(p)) + 'px'; S.$('#im').style.marginBottom = (16 * clamp(p)) + 'px'; if (S.on(tl - .2)) S.sfx(tl - .2, 'thud');
    const ts = S.T('shoved'); S.$('#ar').style.opacity = S.on(ts - .3) ? 1 : 0; S.$('#ar').style.transform = `translateY(${30 * Math.abs(Math.sin(S.t * 6))}px)`; }},
 { // 4 reserve the space
  html: `<div class="phone" style="left:280px;top:340px">${TOPBAR}<div class="art"><div class="img" id="im" style="height:320px;margin-bottom:16px;background:transparent;box-shadow:inset 0 0 0 4px #999;border:0"></div><div class="ln"></div><div class="ln" style="width:80%"></div><div class="ln"></div><div class="ln" style="width:70%"></div><div class="ln"></div></div></div>
   <div class="abs" id="lb" style="left:330px;top:530px;font:800 36px Mono;color:#333;width:420px;text-align:center">[ space reserved ]</div>
   <div class="abs center" id="ok" style="top:1380px;font:800 46px Roboto;color:var(--grn);opacity:0">✓ nothing moves</div>`,
  draw(S) { const ts = S.T('save'); S.$('#im').style.opacity = S.P(ts - .3, .3); const tl = S.T('loads'), p = S.P(tl - .2, .4); S.$('#im').style.background = p > 0 ? `linear-gradient(135deg,rgba(155,196,232,${p}),rgba(214,184,232,${p}))` : 'transparent'; S.$('#lb').style.opacity = 1 - p;
    S.$('#ok').style.opacity = S.P(tl, .3); if (S.on(ts)) S.sfx(ts, 'pop'); if (S.on(tl)) S.sfx(tl, 'ding'); }},
 { // 5 CLS ~0.2 -> 0
  html: `<div class="abs center kick" style="top:440px">layout shift score</div><div class="abs center big" id="cls" style="top:540px;font-size:240px"></div>
   <div class="abs" style="left:110px;right:110px;top:880px;height:40px;border-radius:20px;background:linear-gradient(90deg,var(--grn) 0 40%,#ffb020 40% 100%)"></div>
   <div class="abs" id="pt" style="top:850px;width:24px;height:100px;border-radius:12px;background:#fff;box-shadow:0 0 20px #fff"></div>`,
  draw(S) { const tz = S.T('zero'), p = S.P(S.T('dropped') - .2, tz - S.T('dropped') + .4, eio), v = .2 * (1 - p); S.$('#cls').textContent = v.toFixed(2); S.$('#cls').style.color = v < .1 ? 'var(--grn)' : '#ffb020';
    S.$('#pt').style.left = (110 + 860 * v / .25 - 12) + 'px'; if (S.on(tz)) S.sfx(tz, 'ding'); }},
 { // 6 +15% / +13% (drop)
  html: `<div class="stat s0" style="top:420px"><div class="v" id="v0">+0%</div><div class="l">pages read per visit</div></div><div class="stat s1" style="top:720px"><div class="v" id="v1">+0%</div><div class="l">longer sessions</div></div>`,
  draw(S) { if (S.t < .07) flash(.5); [['fifteen', 0, 15], ['thirteen', 1, 13]].forEach(([w, i, n]) => { const at = S.T(w) - .3, p = S.P(at, .5); S.$('.s' + i).style.opacity = S.P(at, .2); S.$('#v' + i).textContent = '+' + Math.round(n * p) + '%'; if (S.on(at)) S.sfx(at, 'pop'); }); }},
 { // 7 name it, one of the three
  html: `<div class="abs center h" style="top:420px;font-size:96px"><span class="mark" id="mk">Cumulative Layout Shift</span></div>
   <div class="abs center" style="top:680px"><span class="chip c0">LCP</span><span class="chip c1">INP</span><span class="chip c2">CLS</span></div>
   <div class="abs center kick" id="cv" style="top:820px;opacity:0">the three Core Web Vitals</div>`,
  draw(S) { const tc = S.T('cumulative'); S.$('#mk').style.setProperty('--m', S.P(tc - .1, .4)); if (S.on(tc)) S.sfx(tc, 'ding'); const tt = S.T('three');
    [0, 1, 2].forEach(i => { const c = S.$('.c' + i), p = S.P(tt - .3 + i * .1, .25, back); c.style.opacity = clamp(p); c.style.transform = `scale(${.7 + .3 * clamp(p)})`; if (i === 2 && S.on(tt + .4)) { c.style.background = 'var(--yel)'; c.style.color = '#111'; } });
    S.$('#cv').style.opacity = S.P(S.T('vitals') - .4, .3); }},
 ctaScene(),
];
