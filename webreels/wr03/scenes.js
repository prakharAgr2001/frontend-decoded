// WR03: seven crore viewers, one ball (JioHotstar, T20 World Cup final 2026; ICC figure 72.5M peak)
const PHONE = (left, top) => `<div class="phone" style="left:${left}px;top:${top}px"><div class="field"><div class="pitch"></div><div class="ball"></div></div>
  <div class="live">LIVE</div><div class="watch"><span class="w">0</span> watching</div>
  <div class="panel p0" style="top:360px">💬 Live comments<small>“what a shot!!” · “6️⃣6️⃣6️⃣”</small></div>
  <div class="panel p1" style="top:500px">✨ Recommended for you<small>highlights · replays · shorts</small></div>
  <div class="panel p2" style="top:640px">📊 Live poll<small>who wins? 72% India</small></div>
  <div class="panel p3" style="top:780px">🎁 Offers<small>predict & win</small></div></div>`;
function ball(S) { const b = S.$('.ball'); if (b) { const u = (S.abs * 1.4) % 1; b.style.left = (250 + 30 * Math.sin(S.abs * 3)) + 'px'; b.style.top = (40 + 230 * u) + 'px'; } }
const crore = n => (n / 1e7).toFixed(1) + ' crore';
const SCENES = [
 { // 0 HOOK: phone with live stream + counter; racks behind turning red
  html: `<div class="h abs center" style="top:250px;font-size:96px"><span class="mark" id="mk">7 crore people.</span><br>One ball.</div>
   ${[0, 1, 2, 3, 4].map(i => `<div class="rack r${i}" style="left:40px;top:${560 + i * 140}px"><i></i><i></i><i></i><i></i></div>`).join('')}
   ${PHONE(480, 520)}`,
  draw(S) {
    S.$('#mk').style.setProperty('--m', eo(lin(S.t, -.2, .3))); ball(S);
    const p = S.P(0, S.dur, x => x); S.$('.w').textContent = crore(1.5e7 + 5.75e7 * eo(p));
    S.$$('.rack').forEach((r, i) => { const hot = p * (1 + i * .1); r.style.background = rgb(mixc([38, 38, 44], [170, 30, 30], clamp(hot))); r.style.transform = `translateX(${hot > .6 ? 4 * Math.sin(S.abs * 60 + i) : 0}px)`;
      r.querySelectorAll('i').forEach((d, j) => d.style.background = Math.floor(S.abs * 10 + j) % 2 && hot > .5 ? '#ff3b3b' : '#3ddc84'); });
  }},
 { // 1 that should crash any app
  html: `${[0, 1, 2, 3, 4].map(i => `<div class="rack r${i}" style="left:40px;top:${560 + i * 140}px;background:#a01e1e"><i></i><i></i><i></i><i></i></div>`).join('')}${PHONE(480, 520)}
   <div class="h abs center" id="cr" style="top:300px;font-size:110px;color:var(--red)">Should crash.</div>`,
  draw(S) { ball(S); S.$('.w').textContent = '7.2 crore'; S.$('.phone').style.transform = `translateX(${6 * Math.sin(S.t * 70)}px) rotate(${.6 * Math.sin(S.t * 40)}deg)`; S.sfx(0.05, 'buzz');
    S.$$('.rack i').forEach((d, j) => d.style.background = Math.floor(S.t * 12 + j) % 2 ? '#ff3b3b' : '#550'); }},
 { // 2 the spike graph
  html: `<div class="abs center kick" style="top:420px">every big moment</div>
   <svg class="abs" style="left:80px;top:520px" width="920" height="700"><path id="ln" fill="none" stroke="#ffd23f" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/><path id="ar" fill="rgba(255,210,63,.12)"/></svg>
   <div class="abs" id="wk" style="left:700px;top:500px;padding:8px 18px;border-radius:10px;background:var(--red);font:800 30px Inter;opacity:0">WICKET!</div>
   <div class="abs center" style="top:1250px;font:700 44px Roboto">millions open the app <span style="color:var(--yel)">at once</span></div>`,
  draw(S) {
    const p = S.P(0, S.dur * .85, x => x), pts = [];
    for (let i = 0; i <= 100 * p; i++) { const x = i * 9.2, spike = i > 70 ? Math.min(1, (i - 70) / 6) : 0; pts.push([x, 620 - 60 - 20 * Math.sin(i / 5) - 520 * spike]); }
    const d = pts.map((q, i) => (i ? 'L' : 'M') + q[0] + ' ' + q[1]).join(' '); S.$('#ln').setAttribute('d', d);
    S.$('#ar').setAttribute('d', d + (pts.length ? ` L${pts[pts.length - 1][0]} 700 L0 700 Z` : ''));
    const on = p > .7; S.$('#wk').style.opacity = on ? 1 : 0; if (on) S.sfx(S.dur * .85 * .7, 'thud');
  }},
 { // 3 race: servers boot (minutes) vs spike (seconds)
  html: `<div class="race" style="top:520px"><div class="lab">🐢 New server boots</div><div class="tr"><i id="b0" style="background:#888"></i></div><div style="font:500 28px Roboto;color:var(--mute);margin-top:10px">~ minutes</div></div>
   <div class="race" style="top:820px"><div class="lab">⚡ The spike arrives</div><div class="tr"><i id="b1" style="background:var(--red)"></i></div><div style="font:500 28px Roboto;color:var(--mute);margin-top:10px">~ seconds</div></div>
   <div class="h abs center" id="lose" style="top:1120px;font-size:110px;color:var(--red);opacity:0">Too slow.</div>`,
  draw(S) {
    const ts = S.T('spike'); S.$('#b0').style.width = (100 * .12 * S.P(0, S.dur, x => x)) + '%'; S.$('#b1').style.width = (100 * S.P(ts - .2, .5, eo)) + '%';
    const o = S.P(ts + .4, .2); S.$('#lose').style.opacity = o; if (S.on(ts + .4)) S.sfx(ts + .4, 'thud');
  }},
 { // 4 cheat: servers on before the match
  html: `<div class="abs center h2" style="top:380px">So Hotstar <span class="mark" id="mk4">cheats</span></div>
   <div class="abs" style="left:60px;right:60px;top:560px;text-align:center;line-height:0">${'<span class="srv"></span>'.repeat(24)}</div>
   <div class="abs" style="left:100px;right:100px;top:1170px;height:6px;background:#2a2a31"></div>
   <div class="abs" id="tm" style="top:1150px;left:100px;width:44px;height:44px;border-radius:50%;background:var(--yel)"></div>
   <div class="abs" style="right:100px;top:1210px;font:700 30px Roboto;color:var(--mute)">🏏 MATCH STARTS</div>
   <div class="abs" style="left:100px;top:1210px;font:700 30px Roboto;color:var(--grn)" id="pw">servers ready ✓</div>`,
  draw(S) {
    S.$('#mk4').style.setProperty('--m', S.P(S.T('cheats') - .1, .3));
    const tb = S.T('before'), p = S.P(S.T('turns') - .2, 1.2, x => x); S.$$('.srv').forEach((s, i) => s.style.setProperty('--c', i / 24 < p ? '#3ddc84' : '#444'));
    S.$('#tm').style.left = (100 + 820 * S.P(tb, S.dur - tb, x => x) * .9) + 'px'; S.$('#pw').style.opacity = S.P(tb - .3, .3); if (S.on(tb)) S.sfx(tb, 'ding');
  }},
 { // 5 chunks to edge servers near you
  html: `<div class="abs center h2" style="top:380px">chopped into <span class="mark" id="mk5">tiny pieces</span></div>
   <div class="edge" style="left:465px;top:560px;width:150px;height:150px;background:var(--yel);color:#0c0c0e">LIVE<br>FEED</div>
   ${['Mumbai|90|900', 'Delhi|465|1000', 'Bengaluru|840|900', 'Chennai|200|1200', 'Kolkata|730|1200'].map(x => { const [n, l, t] = x.split('|'); return `<div class="edge e" style="left:${l}px;top:${t}px">${n}</div>`; }).join('')}
   <div id="ch"></div>`,
  init(el) { el.querySelector('#ch').innerHTML = Array.from({ length: 30 }, () => '<div class="chunk"></div>').join(''); },
  draw(S) {
    S.$('#mk5').style.setProperty('--m', S.P(S.T('tiny') - .1, .3));
    const E = [[165, 975], [540, 1075], [915, 975], [275, 1275], [805, 1275]], tc = S.T('copied');
    S.$$('.chunk').forEach((c, i) => { const e = E[i % 5], t = ((S.t - tc + 1) * .9 + i * .13) % 1, on = S.on(tc - .8);
      c.style.opacity = on ? 1 : 0; c.style.left = (518 + (e[0] - 540) * t) + 'px'; c.style.top = (620 + (e[1] - 635) * t) + 'px'; });
    S.$$('.e').forEach((e, i) => e.style.boxShadow = S.on(tc + i * .1) ? '0 0 0 4px var(--grn),0 0 30px rgba(61,220,132,.5)' : '0 0 0 3px #3a3a42');
  }},
 { // 6 panic mode: extras switch off, match stays
  html: `${PHONE(280, 470)}<div class="abs center" id="pm" style="top:350px"><span class="pill" style="background:var(--red);color:#fff;font:800 40px Inter;padding:14px 34px">PANIC MODE</span></div>`,
  draw(S) {
    ball(S); S.$('.w').textContent = '7.2 crore'; const tp = S.T('Panic'); S.$('#pm').style.opacity = S.on(tp) ? 1 : 0; if (S.on(tp)) S.sfx(tp, 'buzz');
    [['Comments', 0], ['recommendations', 1], ['extras', 2]].forEach(([w, i]) => { const off = S.on(S.T(w)); const p = S.$('.p' + i); p.style.opacity = off ? .12 : 1; p.style.filter = off ? 'grayscale(1)' : ''; if (off) S.sfx(S.T(w), 'click'); });
    const to = S.T('off'); S.$('.p3').style.opacity = S.on(to) ? .12 : 1;
    const ts = S.T('stays'); S.$('.field').style.boxShadow = S.on(ts) ? 'inset 0 0 0 6px var(--grn)' : '';
  }},
 { // 7 it held (drop)
  html: `<div class="abs center big" style="top:560px;font-size:170px;color:var(--yel)">7.2 crore</div>
   <div class="abs center" style="top:760px;font:600 40px Roboto;color:var(--mute)">watching at the same time</div>
   <div class="h abs center" id="held" style="top:930px;font-size:150px;opacity:0">And it <span style="color:var(--grn)">held.</span></div>`,
  draw(S) { const th = S.T('held'); const o = S.P(th - .1, .2); S.$('#held').style.opacity = o; S.$('#held').style.transform = `scale(${1.2 - .2 * o})`; if (S.on(th - .1)) S.sfx(th - .1, 'thud'); }},
 ctaScene(),
];
