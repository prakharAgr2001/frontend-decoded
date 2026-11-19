// WR04: the day Facebook vanished (4 Oct 2021, DNS + BGP)
const APPS = [['Facebook', '#1877f2'], ['Instagram', '#e1306c'], ['WhatsApp', '#25d366']];
const appCards = (top) => APPS.map((a, i) => `<div class="app a${i}" style="top:${top + i * 190}px"><i style="background:${a[1]}"></i>${a[0]}<small class="st"></small></div>`).join('');
const BOOK = (top, fb) => `<div class="book" style="top:${top}px"><div class="hd">📖 DNS · THE INTERNET'S PHONE BOOK</div>
  <div class="row"><span>google.com</span><span>142.250.x.x</span></div>
  <div class="row" id="fbrow"><span>facebook.com</span><span id="fbip">${fb}</span></div>
  <div class="row"><span>youtube.com</span><span>142.251.x.x</span></div>
  <div class="row"><span>amazon.in</span><span>52.95.x.x</span></div></div>`;
const SCENES = [
 { // 0 three apps, gone
  html: `${appCards(420)}<div class="h abs center" id="gone" style="top:1060px;font-size:170px;color:var(--red);opacity:0">GONE.</div>`,
  draw(S) {
    ['Facebook', 'Instagram', 'WhatsApp'].forEach((w, i) => { const at = Math.max(0, S.T(w) - .15), p = S.P(at, .25, back); const a = S.$('.a' + i);
      a.style.opacity = clamp(p); a.style.transform = `scale(${.85 + .15 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'pop'); });
    const tg = S.T('Gone'); if (S.on(tg)) { S.$$('.app').forEach((a, i) => { a.style.filter = 'grayscale(1)'; a.style.opacity = .35; a.style.transform = `translateX(${Math.sin(S.abs * 50 + i) * 8}px)`; a.querySelector('.st').textContent = 'OFFLINE'; a.querySelector('.st').style.color = 'var(--red)'; }); S.sfx(tg, 'thud'); }
    const o = S.P(tg, .2); S.$('#gone').style.opacity = o; S.$('#gone').style.transform = `scale(${1.3 - .3 * o})`;
  }},
 { // 1 refresh, nothing loads
  html: `<div class="abs center kick" style="top:330px">October 2021</div>
   <div class="phone"><div class="spin"></div>${[0, 1, 2, 3].map(i => `<div class="sk" style="top:${220 + i * 170}px;height:140px"></div>`).join('')}<div class="toast" id="ts" style="opacity:0">Couldn't refresh feed</div></div>`,
  draw(S) { S.$('.spin').style.transform = `rotate(${S.t * 720}deg)`; S.$$('.sk').forEach((k, i) => k.style.opacity = .5 + .4 * Math.sin(S.t * 6 + i));
    const tn = S.T('Nothing'); S.$('#ts').style.opacity = S.P(tn, .2); if (S.on(tn)) S.sfx(tn, 'buzz'); const tr = S.T('refresh'); if (S.on(tr)) S.sfx(tr, 'swish'); }},
 { // 2 not slow, not down, vanished
  html: `<div class="abs center h" style="top:420px;font-size:120px"><span class="strike" id="k0">Not slow.</span></div>
   <div class="abs center h" style="top:600px;font-size:120px"><span class="strike" id="k1">Not down.</span></div>
   <div class="abs center h" id="van" style="top:820px;font-size:140px;color:var(--yel)">Vanished.</div>
   <canvas id="dust" width="1080" height="500" style="position:absolute;left:0;top:780px"></canvas>`,
  draw(S) {
    [['slow', 0], ['down', 1]].forEach(([w, i]) => { const at = S.T(w) + .1; S.$('#k' + i).style.setProperty('--s', S.P(at, .2)); if (S.on(at)) S.sfx(at, 'swish'); });
    const tv = S.T('vanished'), p = S.P(tv, .9, x => x); S.$('#van').style.opacity = S.on(tv - .3) ? 1 - p : 0; if (S.on(tv)) S.sfx(tv, 'whoosh');
    const g = S.$('#dust').getContext('2d'); g.clearRect(0, 0, 1080, 500);
    if (p > 0) for (let i = 0; i < 260; i++) { const x = 220 + R(i) * 640, y = 60 + R(i + 7) * 160; g.fillStyle = `rgba(255,210,63,${(1 - p) * .9})`; g.fillRect(x + p * 300 * (R(i + 3) - .2), y - p * 260 * R(i + 5), 6, 6); }
  }},
 { // 3 DNS phone book
  html: `<div class="ask" id="q" style="top:330px">where is facebook.com? 🤔</div>${BOOK(560, '157.240.x.x')}`,
  draw(S) { const tq = S.T('where') - .2, p = S.P(tq, .3, back); S.$('#q').style.opacity = clamp(p); S.$('#q').style.transform = `scale(${.8 + .2 * clamp(p)})`; if (S.on(tq)) S.sfx(tq, 'pop');
    const tb = S.T('book'); S.$('.book').style.opacity = S.P(tb - .3, .3); S.$('.book').style.transform = `translateY(${(1 - S.P(tb - .3, .3)) * 60}px)`;
    if (S.on(tq + .2)) { S.$('#fbrow').style.background = 'var(--yel)'; } }},
 { // 4 maintenance command cuts data centers off
  html: `<div class="abs mono" style="left:100px;right:100px;top:330px;padding:26px 30px;border-radius:18px;background:#0a0a0b;font-size:34px;color:#9f9;box-shadow:0 0 0 1px rgba(255,255,255,.08)"><span id="cmd"></span><span id="cur">▌</span></div>
   <svg class="abs" style="left:0;top:520px" width="1080" height="800"><g id="ln" stroke-width="10" stroke-linecap="round"></g></svg>
   <div class="dc" style="left:435px;top:820px;width:210px;background:var(--yel);color:#111">BACKBONE</div>
   ${[[90, 560], [780, 560], [90, 1140], [780, 1140]].map((p, i) => `<div class="dc" style="left:${p[0]}px;top:${p[1]}px">Data center ${i + 1}</div>`).join('')}`,
  draw(S) {
    const txt = '$ routine maintenance job…'; S.$('#cmd').textContent = txt.slice(0, Math.floor(txt.length * S.P(0, S.T('command'), x => x))); S.$('#cur').style.opacity = Math.floor(S.t * 4) % 2;
    const tc = S.T('cut'), cut = S.on(tc); const C = [540, 360], E = [[195, 100], [885, 100], [195, 680], [885, 680]];
    S.$('#ln').innerHTML = E.map(e => `<line x1="${C[0]}" y1="${C[1]}" x2="${e[0]}" y2="${e[1]}" stroke="${cut ? '#ff3b3b' : '#3ddc84'}" stroke-dasharray="${cut ? '20 40' : 'none'}" opacity="${cut ? .5 + .5 * Math.sin(S.t * 20) : 1}"/>`).join('');
    if (cut) { S.sfx(tc, 'thud'); if (S.t - tc < .07) flash(.4); }
  }},
 { // 5 DNS servers take themselves offline (drop)
  html: `<div class="abs center kick" style="top:330px">Facebook's DNS servers</div>
   ${[0, 1, 2, 3, 4].map(i => `<div class="rack r" style="top:${420 + i * 150}px"><i></i><i></i><i></i><span style="margin-left:auto" class="lb">ONLINE</span></div>`).join('')}
   <div class="abs center" id="rule" style="top:1200px;font:600 36px Roboto;color:var(--mute)">rule: can't reach the data centers? <b style="color:var(--yel)">go quiet.</b></div>`,
  draw(S) {
    const tb = S.T('built'); S.$('#rule').style.opacity = S.P(tb - .3, .3);
    const to = S.T('offline') - .6; S.$$('.r').forEach((r, i) => { const off = S.on(to + i * .13); r.querySelectorAll('i').forEach((d, j) => d.style.background = off ? '#333' : (Math.floor(S.abs * 8 + j + i) % 3 ? '#3ddc84' : '#1f6b40'));
      r.querySelector('.lb').textContent = off ? 'OFFLINE' : 'ONLINE'; r.querySelector('.lb').style.color = off ? 'var(--red)' : 'var(--grn)'; r.style.opacity = off ? .45 : 1; if (off) S.sfx(to + i * .13, 'click'); });
  }},
 { // 6 phone book has no answer
  html: `${BOOK(360, '157.240.x.x')}<div class="browser" style="top:960px"><div class="bar"><span>facebook.com</span></div><div style="padding:40px 40px 50px;font:600 46px Roboto">😶 This site can't be reached<div style="font:400 30px Roboto;color:#777;margin-top:12px">the address could not be found</div></div></div>`,
  draw(S) { const tn = S.T('no'); const on = S.on(tn); S.$('#fbip').textContent = on ? '??? no answer' : '157.240.x.x'; S.$('#fbrow').style.background = on ? '#ffdede' : 'transparent'; S.$('#fbrow').style.color = on ? '#c00' : '';
    const tf = S.T('facebook', 1); S.$('.browser').style.opacity = S.P(tf - .2, .25); if (S.on(tn)) S.sfx(tn, 'buzz'); }},
 { // 7 tools down, go physically
  html: `${[['💬', 'Team chat'], ['📊', 'Dashboards'], ['🖥️', 'Remote login']].map((t, i) => `<div class="tool t${i}" style="top:${360 + i * 150}px">${t[0]} ${t[1]}<b>✕</b></div>`).join('')}
   <div class="abs" style="left:140px;right:140px;top:880px;height:300px;border-radius:24px;background:#16161a;box-shadow:0 0 0 1px rgba(255,255,255,.08)">
     <div class="abs" style="left:40px;top:120px;font:700 34px Roboto">🏢 HQ</div><div class="abs" style="right:40px;top:120px;font:700 34px Roboto">🗄️ Data center</div>
     <div class="abs" style="left:180px;right:280px;top:142px;border-top:6px dashed #555"></div><div class="abs" id="car" style="left:180px;top:100px;font-size:60px;transform:scaleX(-1)">🚗</div></div>
   <div class="abs center" id="phy" style="top:1230px;font:800 50px Roboto;color:var(--yel);opacity:0">in person.</div>`,
  draw(S) {
    const tt = S.T('tools'); S.$$('.tool').forEach((t, i) => { const p = S.P(tt - .2 + i * .15, .25); t.style.opacity = p; t.querySelector('b').style.opacity = S.on(S.T('same')) ? 1 : 0; });
    if (S.on(S.T('same'))) S.sfx(S.T('same'), 'buzz');
    const tp = S.T('physically'); S.$('#car').style.left = (180 + 220 * S.P(tp - .3, 1.4, eio)) + 'px'; S.$('#phy').style.opacity = S.P(tp, .25); if (S.on(tp)) S.sfx(tp, 'whoosh');
  }},
 { // 8 six hours later, back
  html: `<div class="abs center big" id="hrs" style="top:330px;font-size:190px;color:var(--yel)"></div><div class="abs center kick" style="top:530px">hours offline</div>${appCards(660)}`,
  draw(S) { const p = S.P(0, S.T('later'), eio); S.$('#hrs').textContent = (6 * p).toFixed(1).replace('.0', '') + 'h';
    const tb = S.T('back'); S.$$('.app').forEach((a, i) => { const on = S.on(tb - .1 + i * .1); a.style.filter = on ? '' : 'grayscale(1)'; a.style.opacity = on ? 1 : .35;
      a.querySelector('.st').textContent = on ? 'BACK ✓' : 'OFFLINE'; a.querySelector('.st').style.color = on ? 'var(--grn)' : 'var(--red)'; }); if (S.on(tb)) S.sfx(tb, 'ding'); }},
 ctaScene(),
];
