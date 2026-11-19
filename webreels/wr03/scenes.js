// WR03 v2 (photo edition): JioHotstar, T20 World Cup final 2026, ~7.2 crore peak concurrent (ICC). Photos: Unsplash (stock, illustrative).
const IM = n => `url(../../webreels/wr03/img/c${n}.jpg)`;
const crore = n => (n / 1e7).toFixed(1) + ' crore';
const PLAYER = (top, img, extra = '') => `<div class="player" style="top:${top}px"><div class="vid" style="background-image:${IM(img)}"><div class="live">● LIVE</div><div class="watch">👁 <span class="w">7.2 crore</span></div><div class="bar2"><i></i></div></div>${extra}</div>`;
const kb = (S, el, z = .08) => { el.style.transform = `scale(${1.04 + z * S.P(0, S.dur, x => x)})`; };
const SCENES = [
 { // 0 hook: night stadium, live counter, the ball
  noCam: true,
  html: `<div class="bg" id="bg" style="background-image:${IM(4)}"></div><div class="shade"></div>
   <div class="h abs center" style="top:240px;font-size:104px"><span class="mark" id="mk">7 crore people.</span></div>
   <div class="abs center" style="top:430px"><span style="display:inline-block;padding:14px 30px;border-radius:14px;background:#e11;font:900 44px Inter">● LIVE &nbsp;👁 <span id="w">0</span></span></div>
   <div class="abs" id="ball" style="left:390px;top:640px;width:300px;height:300px;border-radius:50%;background-image:${IM(5)};background-size:760px;background-position:88% 72%;box-shadow:0 0 0 8px #fff,0 30px 80px rgba(0,0,0,.7);opacity:0"></div>
   <div class="h abs center" id="sm" style="top:1050px;font-size:100px;opacity:0">same <i style="color:var(--yel)">second.</i></div>`,
  draw(S) { kb(S, S.$('#bg')); S.$('#mk').style.setProperty('--m', eo(lin(S.t, -.2, .3))); S.$('#w').textContent = crore(7.2e7 * S.P(0, S.T('people'), eo));
    const tb = S.T('ball'), o = S.P(tb - .3, .3, back); S.$('#ball').style.opacity = clamp(o * 2); S.$('#ball').style.transform = `scale(${clamp(o)}) rotate(${S.t * 200}deg)`; if (S.on(tb - .3)) S.sfx(tb - .3, 'whoosh');
    const ts = S.T('second'); S.$('#sm').style.opacity = S.P(ts - .3, .2); if (S.on(ts - .3)) S.sfx(ts - .3, 'thud'); S.sfx(.02, 'tick'); }},
 { // 1 should crash: glitch
  noCam: true,
  html: `<div class="bg" id="b1" style="background-image:${IM(4)}"></div><div class="bg" id="b2" style="background-image:${IM(4)};mix-blend-mode:screen;opacity:.6;filter:hue-rotate(-60deg) saturate(3)"></div><div class="shade" style="background:rgba(120,0,0,.35)"></div>
   <div class="h abs center" style="top:620px;font-size:130px;color:#fff;text-shadow:6px 0 #f00,-6px 0 #0ff" id="cr">Should crash.</div>
   <div class="abs center" style="top:860px"><span style="display:inline-block;padding:18px 34px;border-radius:16px;background:#fff;color:#111;font:800 36px Inter">⚠️ Something went wrong · 503</span></div>`,
  draw(S) { const j = Math.floor(S.t * 20); S.$('#b1').style.transform = `translate(${(R(j) - .5) * 30}px,${(R(j + 1) - .5) * 20}px) scale(1.08)`; S.$('#b2').style.transform = `translate(${(R(j + 2) - .5) * 60}px,0) scale(1.08)`;
    S.$('#cr').style.transform = `translateX(${(R(j + 5) - .5) * 24}px)`; S.sfx(.02, 'buzz'); if (S.t < .07) flash(.4); }},
 { // 2 millions of phones at once: photo tiles + notification + spike
  html: `${[[11, 60, 360, 460, 330], [12, 560, 360, 460, 330], [10, 60, 720, 460, 330], [7, 560, 720, 460, 330]].map((t, i) => `<div class="tilep tp" style="left:${t[1]}px;top:${t[2]}px;width:${t[3]}px;height:${t[4]}px;background-image:${IM(t[0])}"><div class="ntf">🏏 WICKET! Watch live now</div></div>`).join('')}
   <svg class="abs" style="left:60px;top:1080px" width="960" height="300"><path id="ln" fill="none" stroke="#ffd23f" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/></svg>`,
  draw(S) { const tm = S.T('millions'); S.$$('.tp').forEach((t, i) => { const p = S.P(i * .15, .25, back); t.style.opacity = clamp(p); t.style.transform = `scale(${.8 + .2 * clamp(p)})`; const n = t.querySelector('.ntf'), q = S.P(tm - .2 + i * .1, .25, back); n.style.transform = `translateY(${(1 - clamp(q)) * -90}px)`; n.style.opacity = clamp(q); if (S.on(tm - .2 + i * .1)) S.sfx(tm - .2 + i * .1, 'ding'); });
    const p = S.P(0, S.dur * .9, x => x), pts = []; for (let i = 0; i <= 100 * p; i++) { const sp = i > 70 ? Math.min(1, (i - 70) / 5) : 0; pts.push([i * 9.6, 260 - 20 * Math.sin(i / 5) - 230 * sp]); }
    S.$('#ln').setAttribute('d', pts.map((q, i) => (i ? 'L' : 'M') + q[0] + ' ' + q[1]).join(' ')); }},
 { // 3 servers boot in minutes, spike in seconds (data center bg)
  html: `<div class="bg" id="dc" style="background-image:${IM(15)};filter:brightness(.35)"></div>
   <div class="cmp" style="top:500px"><div class="l"><span>🐢 new server boots</span><span>~minutes</span></div><div class="t"><i id="b0" style="background:#888"></i></div></div>
   <div class="cmp" style="top:760px"><div class="l"><span>⚡ the spike arrives</span><span>~seconds</span></div><div class="t"><i id="b1" style="background:var(--red)"></i></div></div>
   <div class="h abs center" id="lose" style="top:1020px;font-size:120px;color:var(--red);opacity:0">Too slow.</div>`,
  draw(S) { kb(S, S.$('#dc'), .05); const ts = S.T('spike'); S.$('#b0').style.width = (12 * S.P(0, S.dur, x => x)) + '%'; S.$('#b1').style.width = (100 * S.P(ts - .2, .5, eo)) + '%';
    const o = S.P(ts + .4, .2); S.$('#lose').style.opacity = o; if (S.on(ts + .4)) S.sfx(ts + .4, 'thud'); }},
 { // 4 cheat: servers on before the match
  html: `<div class="bg" id="sv" style="background-image:${IM(16)};filter:brightness(.45)"></div><div class="shade"></div>
   <div class="abs center h2" style="top:360px">So Hotstar <span class="mark" id="mk4">cheats</span> 😏</div>
   <div class="abs" style="left:110px;right:110px;top:560px;padding:30px;border-radius:24px;background:rgba(12,12,14,.75);line-height:0;text-align:center" id="leds">${'<i class="led"></i>'.repeat(120)}</div>
   <div class="abs" style="left:110px;right:110px;top:900px;display:flex;justify-content:space-between;font:800 40px Inter"><span id="t1" style="color:var(--grn)">6:30 PM · servers ready ✓</span><span style="color:var(--mute)">7:30 🏏</span></div>
   <div class="abs center" id="pr" style="top:1010px;font:700 36px Inter;color:var(--mute);opacity:0">sized for the crowd it predicts 📈</div>`,
  draw(S) { kb(S, S.$('#sv'), .06); S.$('#mk4').style.setProperty('--m', S.P(S.T('cheats') - .1, .3)); const tt = S.T('turns'), p = S.P(tt - .2, 1, x => x);
    S.$$('.led').forEach((l, i) => { const on = R(i + 4) < p * 1.05; l.style.background = on ? '#3ddc84' : '#333'; l.style.boxShadow = on ? '0 0 10px #3ddc84' : ''; });
    S.$('#t1').style.opacity = S.P(S.T('before') - .3, .3); if (S.on(S.T('before'))) S.sfx(S.T('before'), 'ding'); S.$('#pr').style.opacity = S.P(S.T('predicts') - .6, .3); }},
 { // 5 video chopped into pieces -> edge servers near you
  html: `<div class="abs" id="fr" style="left:270px;top:360px;width:540px;height:300px;border-radius:14px;background-image:${IM(6)};background-size:cover;box-shadow:0 30px 70px rgba(0,0,0,.6)"></div><div id="pcs"></div>
   ${[['Mumbai', 120, 1000], ['Delhi', 455, 840], ['Bengaluru', 790, 1000], ['Chennai', 290, 1210], ['Kolkata', 620, 1210]].map(x => `<div class="edge e" style="left:${x[1]}px;top:${x[2]}px">${x[0]}</div>`).join('')}
   <div class="abs center h2" style="top:250px;font-size:56px" id="tl">chopped into <span class="mark" id="mk5">tiny pieces</span></div>`,
  init(el) { el.querySelector('#pcs').innerHTML = Array.from({ length: 30 }, (_, i) => `<div class="piece" style="background-image:${IM(6)};background-position:${-(i % 6) * 90}px ${-Math.floor(i / 6) * 60}px"></div>`).join(''); },
  draw(S) { const tc = S.T('chopped'), tp = S.T('copied'); S.$('#mk5').style.setProperty('--m', S.P(S.T('tiny') - .1, .3)); const E = [[205, 1085], [540, 925], [875, 1085], [375, 1295], [705, 1295]];
    const cut = S.on(tc - .1); S.$('#fr').style.opacity = cut ? 0 : 1; if (S.on(tc - .1)) S.sfx(tc - .1, 'swish');
    S.$$('.piece').forEach((p, i) => { const sx = 270 + (i % 6) * 90, sy = 360 + Math.floor(i / 6) * 60; const sep = S.P(tc - .1, .4, eo); const go = S.P(tp - .3 + (i % 10) * .06, .7, eio); const e = E[i % 5];
      p.style.opacity = cut ? 1 : 0; p.style.left = (sx + (sx - 540) * .25 * sep + (e[0] - 45 - sx) * go) + 'px'; p.style.top = (sy + (sy - 510) * .3 * sep + (e[1] - 30 - sy) * go) + 'px'; p.style.transform = `scale(${1 - .4 * go})`; });
    S.$$('.e').forEach((e, i) => e.style.boxShadow = S.on(tp + .4 + i * .08) ? '0 0 0 4px var(--grn),0 0 30px rgba(61,220,132,.5)' : '0 0 0 3px #3a3a42'); }},
 { // 6 panic mode: realistic app, extras switch off
  html: `${PLAYER(330, 3, [['Live comments', '“what a shot!!” · 6️⃣6️⃣6️⃣', 7], ['Recommended for you', 'highlights · replays', 6], ['Extras', 'polls · predict & win', 12]].map((p, i) => `<div class="panel p${i}"><i style="background-image:${IM(p[2])}"></i><div>${p[0]}<small>${p[1]}</small></div></div>`).join(''))}
   <div class="abs center" id="pm" style="top:240px;opacity:0"><span style="display:inline-block;padding:14px 34px;border-radius:14px;background:var(--red);font:900 44px Inter">🚨 PANIC MODE</span></div>`,
  draw(S) { const tp = S.T('Panic'); S.$('#pm').style.opacity = S.on(tp) ? .6 + .4 * Math.abs(Math.sin(S.t * 6)) : 0; if (S.on(tp)) S.sfx(tp, 'buzz');
    [['Comments', 0], ['recommendations', 1], ['extras', 2]].forEach(([w, i]) => { const off = S.on(S.T(w)); const p = S.$('.p' + i); p.style.opacity = off ? .15 : 1; p.style.filter = off ? 'grayscale(1)' : ''; if (off) S.sfx(S.T(w), 'click'); });
    const ts = S.T('stays'); S.$('.vid').style.boxShadow = S.on(ts - .2) ? 'inset 0 0 0 8px var(--grn)' : ''; }},
 { // 7 it held: crowd celebration
  noCam: true,
  html: `<div class="bg" id="cw" style="background-image:${IM(7)}"></div><div class="shade"></div>
   <div class="abs center big" style="top:420px;font-size:170px;color:var(--yel);text-shadow:0 10px 40px rgba(0,0,0,.6)">7.2 crore</div>
   <div class="h abs center" id="held" style="top:700px;font-size:150px;opacity:0;text-shadow:0 10px 40px rgba(0,0,0,.6)">And it <span style="color:var(--grn)">held.</span></div>`,
  draw(S) { kb(S, S.$('#cw'), .1); if (S.t < .07) flash(.5); const th = S.T('held'), o = S.P(th - .1, .2, back); S.$('#held').style.opacity = clamp(o); S.$('#held').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(th - .1)) S.sfx(th - .1, 'thud'); }},
 ctaScene(),
];
