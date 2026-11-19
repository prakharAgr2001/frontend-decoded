// WR11: Bumble Private Detector (2019): blurs likely-explicit images in chat; ~98% accuracy reported in testing; 0.1% of users send; open-sourced 2022.
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const CHAT = (top, inner) => `<div class="chat" style="top:${top}px"><div class="hd"><i></i>Match</div>${inner}</div>`;
const BLURIMG = (top, warn = true) => `<div class="imgb" style="top:${top}px"><div class="blur"></div>${warn ? `<div class="warn"><span style="font-size:80px">${EMO('warning')}</span>may be explicit<br><span style="font:600 26px Roboto">tap to view</span></div>` : ''}</div>`;
const SCENES = [
 { // 0 hook: AI looks before you
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div><div class="imgb" style="top:260px"><div class="blur"></div><div class="scan" id="sc"></div></div>
     <div class="abs" id="ai" style="left:470px;top:360px;font:800 34px Roboto;color:#111;opacity:0">${EMO('eye')} AI<br>checking…</div>`),
  draw(S) { S.$('#sc').style.top = (420 * ((S.t * 1.2) % 1)) + 'px'; const ta = S.T('AI'); S.$('#ai').style.opacity = S.P(ta - .2, .2); if (S.on(ta - .2)) S.sfx(ta - .2, 'pop'); S.sfx(.05, 'swish'); }},
 { // 1 why: unwanted explicit photos
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div>${BLURIMG(260, false)}`) + `<div class="stamp" id="na" style="left:300px;top:1000px;opacity:0">NOBODY ASKED</div><div class="abs" id="ey" style="left:760px;top:1150px;font-size:130px;opacity:0">${EMO('face-with-rolling-eyes')}</div>`,
  draw(S) { const tn = S.T('nobody'), o = S.P(tn - .2, .2, back); S.$('#na').style.opacity = clamp(o); S.$('#na').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tn - .2)) S.sfx(tn - .2, 'thud'); S.$('#ey').style.opacity = S.P(tn, .3); }},
 { // 2 2019 Private Detector: pipeline
  html: `<div class="abs center kick" style="top:380px">2019 · Bumble builds</div><div class="abs center h" style="top:450px;font-size:110px"><span class="mark" id="mk">Private Detector</span></div>
   <div class="box" style="left:60px;top:800px;width:240px;height:200px;font-size:44px">Sender</div><div class="box" id="ai" style="left:400px;top:780px;width:280px;height:240px;background:#1f2a22;box-shadow:0 0 0 4px var(--grn);font-size:46px;color:var(--grn)">AI check</div><div class="box" style="left:780px;top:800px;width:240px;height:200px;font-size:44px">You</div>
   <div class="abs" id="pk" style="width:60px;height:60px;border-radius:12px;background:var(--yel);top:1080px"></div><div class="abs" style="left:150px;right:120px;top:1106px;height:8px;background:#333"></div>`,
  draw(S) { const tp = S.T('Private'); S.$('#mk').style.setProperty('--m', S.P(tp - .1, .35)); if (S.on(tp)) S.sfx(tp, 'ding');
    const ta = S.T('arrive'), u = ((S.t - (ta - 1.2)) * .8) % 1; S.$('#pk').style.opacity = S.on(ta - 1.2) ? 1 : 0; S.$('#pk').style.left = (150 + 760 * u) + 'px';
    S.$('#ai').style.boxShadow = `0 0 0 4px var(--grn),0 0 ${u > .35 && u < .6 ? 60 : 10}px rgba(61,220,132,.7)`; }},
 { // 3 arrives blurred
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div>${BLURIMG(260)}`),
  draw(S) { const tb = S.T('blurred'), p = S.P(tb - .5, .4); S.$('.imgb').style.opacity = p; S.$('.imgb').style.transform = `scale(${.9 + .1 * p})`; if (S.on(tb - .5)) S.sfx(tb - .5, 'pop'); }},
 { // 4 you decide: view / block / report
  html: CHAT(330, `<div class="msg in" style="top:150px">hey 👋</div>${BLURIMG(260)}`) + `<div class="abs center" style="top:1130px"><span class="act a0" style="background:#2a2a31">👁️ View</span><span class="act a1" style="background:#2a2a31">⛔ Block</span><span class="act a2" style="background:var(--red)">🚩 Report</span></div>`,
  draw(S) { [['View', 0], ['Block', 1], ['report', 2]].forEach(([w, i]) => { const at = S.T(w) - .2, p = S.P(at, .25, back); const a = S.$('.a' + i); a.style.opacity = clamp(p); a.style.transform = `scale(${.6 + .4 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'click'); }); }},
 { // 5 98% (drop)
  html: `<div class="abs center big" id="pc" style="top:470px;font-size:280px;color:var(--grn)">0%</div><div class="abs center h2" style="top:800px">accurate in testing</div>`,
  draw(S) { if (S.t < .07) flash(.5); const tn = S.T('ninety-eight'), p = S.P(.1, tn, eo); S.$('#pc').textContent = Math.round(98 * p) + '%'; if (S.on(tn)) S.sfx(tn, 'thud'); }},
 { // 6 0.1% of users but huge dataset
  html: `<div class="abs" style="left:140px;top:380px;width:800px;line-height:0" id="grid">${'<i style="display:inline-block;width:16px;height:16px;margin:2px;border-radius:3px;background:#3a3a42"></i>'.repeat(1000)}</div>
   <div class="abs center big" id="pt" style="top:1050px;font-size:120px;color:var(--yel);opacity:0">0.1%</div>
   <div class="abs center" id="pile" style="top:1210px;font:700 44px Roboto;opacity:0">…of millions = ${EMO('books')} huge training set</div>`,
  draw(S) { const tp = S.T('point'); const g = S.$$('#grid i'); g[537].style.background = S.on(tp) ? 'var(--yel)' : '#3a3a42'; g[537].style.boxShadow = S.on(tp) ? '0 0 20px var(--yel)' : '';
    S.$('#pt').style.opacity = S.P(tp, .2); if (S.on(tp)) S.sfx(tp, 'pop'); const th = S.T('huge'); S.$('#pile').style.opacity = S.P(th - .4, .3);
    if (S.on(th - .4)) g.forEach((d, i) => { if (R(i) < .25 * S.P(th - .4, 1.2)) d.style.background = '#ffd23f88'; }); }},
 { // 7 open-sourced
  html: `<div class="abs" style="left:110px;right:110px;top:400px;padding:34px 40px;border-radius:24px;background:#0f0f12;box-shadow:0 0 0 2px #333">
     <div style="font:700 40px Mono;color:#4c9dff">bumble-tech / private-detector</div><div style="font:500 30px Roboto;color:var(--mute);margin-top:14px">open source · Apache-2.0 · free to use</div></div>
   ${[0, 1, 2, 3].map(i => `<div class="box ap" style="left:${110 + i * 220}px;top:820px;width:190px;height:190px;font-size:28px">📱<br>app ${i + 1}</div>`).join('')}
   <div class="abs center kick" style="top:1060px" id="fr">any app. for free.</div>`,
  draw(S) { const to = S.T('open-sourced'); S.$('.abs').style.opacity = S.P(to - .4, .3); const tf = S.T('free'); S.$$('.ap').forEach((a, i) => { const at = tf - .9 + i * .15, p = S.P(at, .25, back); a.style.opacity = clamp(p); a.style.transform = `scale(${.6 + .4 * clamp(p)})`; a.style.boxShadow = S.on(at) ? '0 0 0 4px var(--grn)' : ''; if (S.on(at)) S.sfx(at, 'pop'); });
    S.$('#fr').style.opacity = S.P(tf - .2, .2); }},
 ctaScene(),
];
