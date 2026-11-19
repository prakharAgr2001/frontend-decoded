// WR05: one setting broke huge parts of the internet (Fastly, 8 June 2021)
const SITES = [['amazon.com', 'Amazon'], ['reddit.com', 'Reddit'], ['nytimes.com', 'New York Times'], ['gov.uk', 'UK government']];
const site = (s, l, t, err) => `<div class="site" style="left:${l}px;top:${t}px"><div class="bar"><span>${s[0]}</span></div><div class="bd">${err ? '<span style="color:#c00">Error 503</span><small>Service Unavailable</small>' : s[1] + '<small>loading…</small>'}</div></div>`;
const POS = [[80, 560], [580, 560], [80, 880], [580, 880]];
const SCENES = [
 { // 0 one setting -> sites down
  html: `<div class="set"><div class="r"><span>Some setting</span><span class="tg"><i></i></span></div><div class="r" style="border:0;color:#888"><span>Saved by: 1 customer</span><span>👆</span></div></div>
   <div id="sw">${SITES.map((s, i) => site(s, POS[i][0], POS[i][1] + 160, false)).join('')}</div>`,
  draw(S) {
    const tc = S.T('changed'), on = S.on(tc); S.$('.tg').style.background = on ? 'var(--grn)' : '#bbb'; S.$('.tg i').style.left = (6 + 50 * S.P(tc, .15)) + 'px'; if (on) S.sfx(tc, 'click');
    const td = S.T('down'); S.$$('.site').forEach((x, i) => { const at = td - .5 + i * .1, d = S.on(at); x.style.opacity = S.P(S.T('huge') - .2, .3);
      x.querySelector('.bd').innerHTML = d ? '<span style="color:#c00">Error 503</span><small>Service Unavailable</small>' : SITES[i][1] + '<small>loading…</small>';
      x.style.transform = d ? `translateX(${Math.sin(S.abs * 40 + i) * 5}px)` : ''; if (d) S.sfx(at, 'buzz'); });
  }},
 { // 1 the famous sites, same error
  html: `<div class="abs center kick" style="top:380px">June 2021</div>${SITES.map((s, i) => site(s, POS[i][0], POS[i][1] - 40, true)).join('')}
   <div class="abs center h2" id="same" style="top:1230px;opacity:0">the <span class="mark">same</span> error</div>`,
  draw(S) { const W = ['Amazon', 'Reddit', 'York', 'UK']; S.$$('.site').forEach((x, i) => { const at = S.T(W[i]) - .15, p = S.P(at, .25, back); x.style.opacity = clamp(p); x.style.transform = `scale(${.8 + .2 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'pop'); });
    S.$('#same').style.opacity = S.P(S.T('same') - .2, .25); }},
 { // 2 they all use Fastly
  html: `<svg class="abs" style="left:0;top:0" width="1080" height="1500"><g id="ln" stroke="#ffd23f" stroke-width="6"></g></svg>
   ${SITES.map((s, i) => `<div class="node s" style="left:${[60, 720, 60, 720][i]}px;top:${[400, 400, 1150, 1150][i]}px;width:300px;height:110px;font-size:30px">${s[0]}</div>`).join('')}
   <div class="node" id="fs" style="left:340px;top:690px;width:400px;height:200px;background:var(--red);color:#fff;font-size:64px;box-shadow:0 0 60px rgba(255,59,59,.5)">Fastly<br><span id="cdn" style="font-size:30px;letter-spacing:4px;opacity:0">A CDN</span></div>`,
  draw(S) { const tf = S.T('Fastly'), p = S.P(tf - .1, .3, back); S.$('#fs').style.opacity = clamp(p); S.$('#fs').style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(tf)) S.sfx(tf, 'thud');
    const q = S.P(tf, .4); const A = [[210, 455], [870, 455], [210, 1205], [870, 1205]]; S.$('#ln').innerHTML = A.map(a => `<line x1="${a[0]}" y1="${a[1]}" x2="${a[0] + (540 - a[0]) * q}" y2="${a[1] + (790 - a[1]) * q}"/>`).join('');
    S.$('#cdn').style.opacity = S.P(S.T('CDN') - .1, .2); }},
 { // 3 what a CDN does
  html: `<div class="node" style="left:390px;top:380px;width:300px;height:120px;background:#26262c">🏠 Original site<br><small style="font:400 24px Roboto;color:var(--mute)">far away</small></div>
   ${[[90, 820], [420, 900], [750, 820]].map((p, i) => `<div class="node cp" style="left:${p[0]}px;top:${p[1]}px;width:240px;height:110px;font-size:28px">📦 copy</div>`).join('')}
   <div class="abs" id="you" style="left:470px;top:1220px;font:700 40px Roboto">📱 you</div>
   <div class="abs" id="pk" style="width:30px;height:30px;border-radius:50%;background:var(--yel);box-shadow:0 0 20px var(--yel)"></div>
   <div class="abs center" id="ms" style="top:1320px;font:800 50px Roboto;color:var(--grn);opacity:0">⚡ fast</div>`,
  draw(S) { const tc = S.T('copies'); S.$$('.cp').forEach((c, i) => { const p = S.P(tc - .1 + i * .12, .25, back); c.style.opacity = clamp(p); c.style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(tc + i * .12)) S.sfx(tc + i * .12, 'pop'); });
    const tn = S.T('near'), u = ((S.t - tn) * 1.6) % 1; S.$('#pk').style.opacity = S.on(tn) ? 1 : 0; S.$('#pk').style.left = (525 - 0 * u) + 'px'; S.$('#pk').style.top = (1015 + 190 * u) + 'px';
    S.$('#ms').style.opacity = S.P(S.T('fast') - .2, .2); }},
 { // 4 hidden bug, waiting
  html: `<div class="edit" style="top:380px">${['function handle(config) {', '  validate(config);', '  apply(config);', '  // …', '  route(request);', '}'].map((l, i) => `<div class="ln" id="l${i}"><b>${i + 1}</b><span>${l}</span></div>`).join('')}</div>
   <div class="abs" id="bug" style="left:820px;top:560px;font-size:70px;opacity:0">🐛</div>
   <div class="abs center" style="top:900px"><div id="cal" style="display:inline-block;width:320px;border-radius:24px;overflow:hidden;background:#f3efe4;color:#111;box-shadow:0 40px 90px rgba(0,0,0,.6)"><div style="background:var(--red);color:#fff;font:800 34px Roboto;padding:12px" id="mon">MAY</div><div id="day" style="font:800 140px Roboto;padding:10px 0 20px">12</div></div></div>`,
  draw(S) { const tb = S.T('bug'); S.$('#bug').style.opacity = S.on(tb - .2) ? .4 + .6 * Math.abs(Math.sin(S.t * 4)) : 0; S.$('#l2').style.background = S.on(tb - .2) ? 'rgba(255,59,59,.15)' : ''; if (S.on(tb - .2)) S.sfx(tb - .2, 'pop');
    const tw = S.T('sat'), p = S.P(tw, S.dur - tw - .1, x => x), d = Math.round(12 + 27 * p); S.$('#mon').textContent = d > 31 ? 'JUNE' : 'MAY'; S.$('#day').textContent = d > 31 ? d - 31 : d; S.sfx(tw + Math.floor((S.t - tw) * 6) / 6, 'tick'); }},
 { // 5 one customer pushes a normal change
  html: `<div class="abs center kick" style="top:380px">June 8 · one customer</div>
   <div class="edit" style="top:460px"><div class="ln"><b>~</b><span style="color:#ff7b7b">- cache_rule: old</span></div><div class="ln"><b>~</b><span style="color:#7bff9b">+ cache_rule: new</span></div></div>
   <div class="abs center" id="ok" style="top:740px;font:800 44px Roboto;color:var(--grn);opacity:0">✓ perfectly valid</div>
   <div class="abs center" style="top:900px"><span id="btn" style="display:inline-block;padding:30px 80px;border-radius:24px;background:#4c9dff;font:800 52px Roboto">Push ▶</span></div>`,
  draw(S) { S.$('#ok').style.opacity = S.P(S.T('normal') - .3, .25); const tp = S.T('pushed'); S.$('#btn').style.transform = S.on(tp) && S.t < tp + .2 ? 'scale(.9)' : ''; if (S.on(tp)) { S.$('#btn').style.background = '#2b6cc4'; S.sfx(tp, 'click'); } }},
 { // 6 BOOM 85% errors (drop)
  html: `<div class="abs center h" id="boom" style="top:300px;font-size:120px;color:var(--red)">BOOM.</div><div class="grid100">${'<i></i>'.repeat(100)}</div>
   <div class="abs center big" id="pc" style="top:1290px;font-size:130px;color:var(--red)"></div>`,
  draw(S) { const tb = S.T('Boom'), te = S.T('errors'); S.$('#boom').style.opacity = S.on(tb) ? 1 : 0; if (S.on(tb)) { S.sfx(tb, 'thud'); if (S.t - tb < .07) flash(.5); }
    const p = S.P(tb + .1, te - tb - .1, x => x); S.$$('.grid100 i').forEach((d, i) => { const red = R(i + 3) < .85 && R(i + 11) < p * 1.02 / .98; d.style.background = red ? '#ff3b3b' : '#3ddc84'; });
    S.$('#pc').textContent = Math.round(85 * p) + '% errors'; }},
 { // 7 caught in 1 min, back in 49
  html: `<div class="grid100" style="top:380px">${'<i></i>'.repeat(100)}</div>
   <div class="abs" style="left:110px;top:1170px;font:800 64px Roboto;color:var(--yel)" id="t1">1 min<div style="font:600 28px Roboto;color:var(--mute)">spotted</div></div>
   <div class="abs" style="right:110px;top:1170px;text-align:right;font:800 64px Roboto;color:var(--grn)" id="t2"><span id="m">0</span> min<div style="font:600 28px Roboto;color:var(--mute)">mostly back</div></div>`,
  draw(S) { const tm = S.T('minute'), tf = S.T('forty-nine'); S.$('#t1').style.opacity = S.P(tm - .2, .2); if (S.on(tm)) S.sfx(tm, 'ding');
    const p = S.P(tm, tf - tm + .3, eio); S.$('#m').textContent = Math.round(1 + 48 * p); S.$('#t2').style.opacity = S.P(tm, .2);
    S.$$('.grid100 i').forEach((d, i) => { const red = R(i + 3) < .85 && R(i + 17) > p * .95; d.style.background = red ? '#ff3b3b' : '#3ddc84'; }); }},
 { // 8 lesson: one shared CDN
  html: `<svg class="abs" style="left:0;top:0" width="1080" height="1500"><g id="sp" stroke-width="5"></g></svg>
   ${Array.from({ length: 12 }, (_, i) => { const a = i / 12 * 6.283; return `<div class="node w" style="left:${540 + 400 * Math.cos(a) - 70}px;top:${880 + 400 * Math.sin(a) - 40}px;width:140px;height:80px;font-size:24px">site ${i + 1}</div>`; }).join('')}
   <div class="node" style="left:420px;top:810px;width:240px;height:140px;background:#26262c;font-size:34px">one CDN<br><span id="bg" style="opacity:0">🐛</span></div>
   <div class="abs center h2" style="top:300px">one bug = <span class="mark" id="mk">everyone's bug</span></div>`,
  draw(S) { const tb = S.T('bug'); const p = S.P(tb, .8, x => x); S.$('#bg').style.opacity = S.on(tb - .2) ? 1 : 0;
    S.$('#sp').innerHTML = Array.from({ length: 12 }, (_, i) => { const a = i / 12 * 6.283; return `<line x1="540" y1="880" x2="${540 + 400 * Math.cos(a)}" y2="${880 + 400 * Math.sin(a)}" stroke="${p > .1 ? '#ff3b3b' : '#555'}"/>`; }).join('');
    S.$$('.w').forEach((w, i) => { const r = p > i / 12; w.style.boxShadow = r ? '0 0 0 3px var(--red),0 0 24px rgba(255,59,59,.5)' : '0 0 0 3px #3a3a42'; });
    S.$('#mk').style.setProperty('--m', S.P(S.T('bug', 2) - .3, .3)); if (S.on(tb)) S.sfx(tb, 'buzz'); }},
 ctaScene(),
];
