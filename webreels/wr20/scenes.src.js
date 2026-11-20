// WR20: Amazon S3 outage, 28 Feb 2017 (us-east-1): mistyped input removed far more capacity than intended
const GRIDS = (n) => `<div class="srv">${[...Array(n)].map(() => '<i></i>').join('')}</div>`;
const SITE = (i) => `<div class="site"><div class="sb"></div><div class="si">${['shop', 'news', 'chat', 'photos', 'docs', 'music'][i]}</div><div class="sx">✗</div></div>`;
const SCENES = [
 { // 0 hook
  html: `${WIN('terminal', `<span class="g">$</span> <span id="cmd"></span>`)}<div class="abs center h" id="hk" style="top:780px;font-size:96px"><span class="mark" id="mk">One typo</span></div>
   <div class="abs lab" style="right:90px;top:690px;font-size:24px">illustration</div><div class="sites" style="top:960px">${[0, 1, 2, 3, 4, 5].map(SITE).join('')}</div>`,
  init(el) { el.querySelector('.win').style.top = '420px'; },
  draw(S) { TYPE(S, '#cmd', 'remove-servers --count 9OO', 0, 1); MK(S, '#mk', .3); const td = TT(S, 'down', .5); S.$$('.site').forEach((s, i) => { const off = S.on(td + i * .08); s.classList.toggle('off', off); if (S.on(td + i * .08)) S.sfx(td + i * .08, 'click'); }); }},
 { // 1 the plan: remove a few servers
  html: `<div class="abs center kick" style="top:400px">February 2017 · S3 file storage</div>${GRIDS(96)}<div class="abs center lab" style="top:1360px;font-size:40px">plan: take <b class="y">a few</b> offline</div>`,
  draw(S) { S.$$('.srv i').forEach((b, i) => b.classList.toggle('pl', i < 4 && S.on(TT(S, 'few', .6)))); }},
 { // 2 far more go offline
  html: `${GRIDS(96)}<div class="abs center h2" id="t" style="top:1360px">far more went offline</div>`,
  draw(S) { const tf = TT(S, 'Far', .5); S.$$('.srv i').forEach((b, i) => { const at = tf + R(i) * 1.2; b.classList.toggle('dead', S.on(at) && R(i + 50) < .78 || i < 4); });
    if (S.on(tf)) S.sfx(tf, 'buzz'); S.$('#t').style.opacity = S.P(tf, .3); }},
 { // 3 full restart, hours
  html: `<div class="abs center kick" style="top:420px">full restart</div><div class="abs center big" id="h" style="top:540px;font-size:160px">0:00</div>
   <div class="abs" style="left:110px;right:110px;top:800px;height:40px;border-radius:20px;background:#2a2a31;overflow:hidden"><div id="b" style="height:100%;width:0;background:var(--yel)"></div></div>
   <div class="abs center lab" style="top:880px;font-size:40px">restarting something this big is slow</div>`,
  draw(S) { const p = S.P(0, S.dur, x => x), m = Math.floor(240 * p); S.$('#h').textContent = Math.floor(m / 60) + ':' + String(m % 60).padStart(2, '0'); S.$('#b').style.width = 100 * p * .6 + '%'; if (Math.floor(S.t * 6) % 2) S.sfx(S.t, 'tick'); }},
 { // 4 sites broke, status page
  html: `<div class="sites" style="top:420px">${[0, 1, 2, 3, 4, 5].map(SITE).join('')}</div>
   <div class="tile" id="sp" style="left:110px;right:110px;top:1000px;height:300px;padding:36px 44px;opacity:0"><div class="lab">STATUS PAGE</div><div style="font:700 48px Roboto;margin-top:20px"><span class="g">●</span> All systems operational</div><div class="lab" style="margin-top:20px;color:var(--red)">(it depended on… S3)</div></div>`,
  draw(S) { S.$$('.site').forEach((s, i) => { const at = .1 + i * .12; s.classList.toggle('off', S.on(at)); if (S.on(at)) S.sfx(at, 'click'); }); IN(S, '#sp', TT(S, 'status', .6) - .2); }},
 { // 5 the fix: slow removal + floor
  html: `<div class="abs center h2" style="top:400px">the fix</div><div class="meter"><div class="lv" id="lv"></div><div class="floor"><span>SAFE MINIMUM</span></div></div>
   <div class="abs center lab" id="sl" style="top:1350px;font-size:40px">removes servers slowly · refuses to go below the line</div>`,
  draw(S) { const p = S.P(.3, S.dur - .5, x => x), v = Math.max(35, 100 - 90 * p); S.$('#lv').style.height = v + '%'; S.$('#lv').style.background = v <= 35.5 ? 'var(--grn)' : 'var(--blue)'; }},
 ctaScene(),
];
