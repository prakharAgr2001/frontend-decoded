// WR11 v2: Bumble Private Detector (2019): blurs likely-explicit chat images; ~98% accuracy reported in testing; open-sourced 2022 (Apache-2.0).
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const CHAT = (top, inner) => `<div class="chat" style="top:${top}px"><div class="hd"><i></i>Match</div>${inner}</div>`;
const BLURIMG = (top, warn = true) => `<div class="imgb" style="top:${top}px"><div class="blur"></div>${warn ? `<div class="warn"><span style="font-size:80px">${EMO('warning')}</span>may be explicit<br><span style="font:600 26px Roboto">tap to view</span></div>` : ''}</div>`;
const OK = [['linear-gradient(135deg,#ffb35c,#ff7a8a)', '🌅'], ['linear-gradient(135deg,#6fb3ff,#5fe08f)', '🐶'], ['linear-gradient(135deg,#b48cff,#6fb3ff)', '🍕'], ['linear-gradient(135deg,#5fe08f,#ffd23f)', '🏔️']];
const SCENES = [
 { // 0 hook: notification -> AI saw it first
  html: `<div class="lock" style="top:330px"><div class="tm">02:46</div><div class="notif" id="nf"><i>B</i><div>New photo 📷<div style="font:400 26px Roboto;color:#555">from your match</div></div></div>
     <div class="abs" id="eye" style="left:0;right:0;top:600px;text-align:center;font-size:220px;opacity:0">${EMO('eye')}</div><div class="scan" id="sc" style="opacity:0"></div></div>
   <div class="stamp" id="ai" style="left:240px;top:1150px;opacity:0">AI SAW IT FIRST</div>`,
  draw(S) { const p = S.P(0, .3, back); S.$('#nf').style.transform = `translateY(${-200 * (1 - clamp(p))}px)`; S.sfx(0.02, 'ding');
    const ta = S.T('AI'); S.$('#eye').style.opacity = S.P(ta - .3, .2); S.$('#eye').style.transform = `scale(${1 + .1 * Math.sin(S.t * 10)})`; S.$('#sc').style.opacity = S.on(ta - .3) ? 1 : 0; S.$('#sc').style.top = (100 + 800 * ((S.t * 1.3) % 1)) + 'px';
    const tf = S.T('first'), o = S.P(tf - .2, .2, back); S.$('#ai').style.opacity = clamp(o); S.$('#ai').style.transform = `rotate(-6deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tf - .2)) S.sfx(tf - .2, 'thud'); }},
 { // 1 flood of unwanted photos
  html: CHAT(330, `<div id="fl"></div>`) + `<div class="stamp" id="na" style="left:260px;top:1100px;opacity:0">NOBODY ASKED</div><div class="abs" id="ey" style="left:780px;top:1210px;font-size:130px;opacity:0">${EMO('face-with-rolling-eyes')}</div>`,
  init(el) { el.querySelector('#fl').innerHTML = Array.from({ length: 6 }, (_, i) => `<div class="imgb fi" style="top:${140 + i * 70}px;left:${30 + (i % 2) * 60}px;width:300px;height:300px;box-shadow:0 10px 30px rgba(0,0,0,.4)"><div class="blur"></div></div>`).join(''); },
  draw(S) { S.$$('.fi').forEach((f, i) => { const at = i * .22, p = S.P(at, .2, back); f.style.opacity = clamp(p); f.style.transform = `scale(${.6 + .4 * clamp(p)}) rotate(${(R(i) - .5) * 14}deg)`; if (S.on(at)) S.sfx(at, 'pop'); });
    const tn = S.T('nobody'), o = S.P(tn - .2, .2, back); S.$('#na').style.opacity = clamp(o); S.$('#na').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tn - .2)) S.sfx(tn - .2, 'thud'); S.$('#ey').style.opacity = S.P(tn, .3);
    if (S.t > 1) S.$('.chat').style.transform = `translateX(${3 * Math.sin(S.t * 40)}px)`; }},
 { // 2 the bouncer gate
  html: `<div class="abs center h" style="top:330px;font-size:110px">the AI <span class="mark" id="mk">bouncer</span> 🕶️</div><div class="gate" id="gt">CHECK</div><div id="tl"></div>
   <div class="abs" style="left:60px;top:1300px;font:700 32px Roboto;color:var(--mute)">incoming</div><div class="abs" style="right:60px;top:1300px;font:700 32px Roboto;color:var(--mute)">your chat</div>`,
  init(el) { el.querySelector('#tl').innerHTML = [0, 1, 2, 3, 4].map(i => `<div class="tile t${i}" style="background:${i === 2 ? '#866' : OK[i % 4][0]}">${i === 2 ? '<div class="blur" style="position:absolute;inset:0;background:radial-gradient(circle,#c99,#866);filter:blur(16px)"></div>' : OK[i % 4][1]}</div>`).join(''); },
  draw(S) { const tb = S.T('bouncer'); S.$('#mk').style.setProperty('--m', S.P(tb - .1, .3)); if (S.on(tb)) S.sfx(tb, 'ding'); const t0 = S.T('checked') - 1.2;
    S.$$('.tile').forEach((t, i) => { const u = clamp((S.t - t0 - i * .45) / 1.2); const bad = i === 2; const x = 60 + 880 * u, y = 830 + (bad && u > .45 ? 0 : 0);
      t.style.left = x + 'px'; t.style.top = y + 'px'; t.style.opacity = u > 0 && u < 1 ? 1 : (u >= 1 ? 1 : 0); if (bad && u > .45) { t.style.boxShadow = '0 0 0 6px var(--red),0 0 40px rgba(255,59,59,.7)'; t.innerHTML = '<div style="position:absolute;inset:0;background:radial-gradient(circle,#c99,#866);filter:blur(16px)"></div><span style="position:relative;font-size:70px">⚠️</span>'; }
      else if (u > .45) t.style.boxShadow = '0 0 0 6px var(--grn)'; if (Math.abs(u - .45) < .03) S.sfx(S.t, bad ? 'buzz' : 'click'); });
    const anyBad = S.$('.t2').style.boxShadow.includes('255'); S.$('#gt').style.boxShadow = anyBad && S.t < t0 + .9 * 1.2 + 1.2 ? '0 0 0 5px var(--red),0 0 60px rgba(255,59,59,.6)' : '0 0 0 5px var(--grn),0 0 50px rgba(61,220,132,.4)'; }},
 { // 3 arrives blurred with warning
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div>${BLURIMG(260)}`),
  draw(S) { const tb = S.T('blurred'), p = S.P(tb - .5, .3, back); S.$('.imgb').style.opacity = clamp(p); S.$('.imgb').style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(tb - .5)) S.sfx(tb - .5, 'pop');
    const tw = S.T('warning'); S.$('.warn span').style.transform = `scale(${S.on(tw - .2) ? 1 + .15 * Math.abs(Math.sin(S.t * 8)) : 1})`; }},
 { // 4 you decide
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div>${BLURIMG(260)}`) + `<div class="abs center" style="top:1100px"><span class="act a0" style="background:#2a2a31">👁️ Open</span><span class="act a1" style="background:#2a2a31">⛔ Block</span><span class="act a2" style="background:var(--red)">🚩 Report</span></div>`,
  draw(S) { [['Open', 0], ['Block', 1], ['report', 2]].forEach(([w, i]) => { const at = S.T(w) - .2, p = S.P(at, .25, back); const a = S.$('.a' + i); a.style.opacity = clamp(p); a.style.transform = `scale(${.6 + .4 * clamp(p) + (S.on(at) && S.t < at + .25 ? .15 : 0)})`; if (S.on(at)) S.sfx(at, 'click'); }); }},
 { // 5 98% (drop)
  html: `<svg class="ring" viewBox="0 0 500 500"><circle cx="250" cy="250" r="210" stroke="#2a2a31" stroke-width="34" fill="none"/><circle id="arc" cx="250" cy="250" r="210" stroke="#3ddc84" stroke-width="34" fill="none" stroke-linecap="round" transform="rotate(-90 250 250)" stroke-dasharray="1320" stroke-dashoffset="1320"/></svg>
   <div class="abs center big" id="pc" style="top:590px;font-size:150px;color:var(--grn)">0%</div><div class="abs center h2" style="top:980px">accurate in testing</div>`,
  draw(S) { if (S.t < .07) flash(.5); const tn = S.T('ninety-eight'), p = S.P(.05, tn, eo); S.$('#pc').textContent = Math.round(98 * p) + '%'; S.$('#arc').setAttribute('stroke-dashoffset', 1320 * (1 - .98 * p));
    S.$('.ring').style.transform = `scale(${1 + .06 * Math.max(0, 1 - Math.abs(S.t - tn) * 4)})`; if (S.on(tn)) S.sfx(tn, 'thud'); }},
 { // 6 gave it away: gift -> burst to many apps
  html: `<div class="abs center" id="gf" style="top:520px;font-size:200px">🎁</div><div id="ap"></div>
   <div class="abs center" style="top:1250px" id="tags"><span class="act" style="background:var(--grn);color:#111">FREE</span><span class="act" style="background:#4c9dff">OPEN SOURCE</span></div>`,
  init(el) { el.querySelector('#ap').innerHTML = Array.from({ length: 10 }, (_, i) => `<div class="tile ap" style="width:120px;height:120px;font-size:56px;background:${OK[i % 4][0]}">📱</div>`).join(''); },
  draw(S) { const tg = S.T('away'), p = S.P(tg - .2, .7, eo); S.$('#gf').style.transform = `scale(${1 + .3 * Math.sin(Math.min(1, S.t / Math.max(.1, tg)) * Math.PI)}) rotate(${S.on(tg - .2) ? 0 : 8 * Math.sin(S.t * 20)}deg)`; if (S.on(tg - .2)) S.sfx(tg - .2, 'whoosh');
    S.$$('.ap').forEach((a, i) => { const ang = i / 10 * 6.283; a.style.left = (480 + 400 * Math.cos(ang) * p) + 'px'; a.style.top = (600 + 380 * Math.sin(ang) * p) + 'px'; a.style.opacity = p; });
    const tf = S.T('free'); S.$('#tags').style.opacity = S.P(tf - .2, .2); }},
 ctaScene(),
];
