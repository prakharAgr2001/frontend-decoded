// WR11 v3 (photo edition): Bumble Private Detector (2019); ~98% accuracy reported in testing; open-sourced 2022 (Apache-2.0). Photos: Unsplash (stock, illustrative).
const I = n => `url(../../webreels/wr11/img/${n}.jpg)`;
const SB = `<div class="sb"><span>2:46</span><span>●●● ▮</span></div>`;
const HEAD = `${SB}<div class="ch"><i style="background:#ddd;display:flex;align-items:center;justify-content:center;font:900 40px Inter;color:#888;font-style:normal">?</i><div><b>New match</b><small>matched today · online</small></div></div>`;
const BLUR = (top, img = 'sunset', warn = true) => `<div class="im" style="top:${top}px"><div class="bl" style="background-image:${I(img)}"></div>${warn ? `<div class="wr"><span style="font-size:70px">⚠️</span>This photo may be explicit<small>Private Detector blurred it</small></div>` : ''}</div>`;
const SCENES = [
 { // 0 hook: lock screen notification -> AI saw it first
  html: `<div class="ph" style="left:220px;top:300px"><div class="lock" style="background-image:${I('wall')}"><div class="dt">Friday, 20 November</div><div class="tm">2:46</div>
     <div class="nt" id="nt"><div class="ic">B</div><div>New match sent you a photo 📷<div style="font:400 24px Inter;color:#555">now · tap to open</div></div></div>
     <div class="scan" id="sc" style="opacity:0"></div></div></div>
   <div class="abs center" id="eye" style="top:860px;font-size:200px;opacity:0;z-index:5">👁️</div>
   <div class="stamp" id="ai" style="left:200px;top:1150px;opacity:0;z-index:6;background:rgba(17,17,17,.7)">AI SAW IT FIRST</div>`,
  draw(S) { const p = S.P(0, .35, back); S.$('#nt').style.transform = `translateY(${-260 * (1 - clamp(p))}px)`; S.sfx(0.02, 'ding');
    const ta = S.T('AI'); S.$('#eye').style.opacity = S.P(ta - .3, .2); S.$('#eye').style.transform = `scale(${1 + .08 * Math.sin(S.t * 10)})`; S.$('#sc').style.opacity = S.on(ta - .3) ? 1 : 0; S.$('#sc').style.top = (100 + 950 * ((S.t * 1.3) % 1)) + 'px'; if (S.on(ta - .3)) S.sfx(ta - .3, 'swish');
    const tf = S.T('first'), o = S.P(tf - .2, .2, back); S.$('#ai').style.opacity = clamp(o); S.$('#ai').style.transform = `rotate(-6deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tf - .2)) S.sfx(tf - .2, 'thud'); }},
 { // 1 unwanted photos flood a real-looking chat
  html: `<div class="ph" id="c1" style="left:220px;top:300px">${HEAD}<div class="bb out" style="top:220px">hey! how's your week? 😊</div><div id="fl"></div></div>
   <div class="stamp" id="na" style="left:230px;top:1100px;opacity:0;z-index:6;background:rgba(17,17,17,.7)">NOBODY ASKED</div><div class="abs" id="ey" style="left:800px;top:1230px;font-size:120px;opacity:0;z-index:6">🙄</div>`,
  init(el) { el.querySelector('#fl').innerHTML = [0, 1, 2, 3].map(i => `<div class="im fi" style="top:${330 + i * 90}px;left:${30 + (i % 2) * 70}px;width:330px;height:400px;box-shadow:0 10px 30px rgba(0,0,0,.3)"><div class="bl" style="background-image:${I(['sunset', 'hills', 'coffee', 'pizza'][i])}"></div></div>`).join(''); },
  draw(S) { S.$$('.fi').forEach((f, i) => { const at = .1 + i * .25, p = S.P(at, .2, back); f.style.opacity = clamp(p); f.style.transform = `scale(${.6 + .4 * clamp(p)}) rotate(${(R(i) - .5) * 12}deg)`; if (S.on(at)) S.sfx(at, 'pop'); });
    const tn = S.T('nobody'), o = S.P(tn - .2, .2, back); S.$('#na').style.opacity = clamp(o); S.$('#na').style.transform = `rotate(-8deg) scale(${1.4 - .4 * clamp(o)})`; if (S.on(tn - .2)) S.sfx(tn - .2, 'thud'); S.$('#ey').style.opacity = S.P(tn, .3);
    if (S.t > 1) S.$('#c1').style.transform = `translateX(${3 * Math.sin(S.t * 40)}px)`; }},
 { // 2 AI bouncer: real photos pass, one gets flagged
  html: `<div class="abs center h" style="top:300px;font-size:104px">the AI <span class="mark" id="mk">bouncer</span> 🕶️</div><div class="gate" id="gt">AI CHECK</div><div id="tl"></div>
   <div class="abs" style="left:60px;top:1290px;font:700 32px Inter;color:var(--mute)">incoming</div><div class="abs" style="right:60px;top:1290px;font:700 32px Inter;color:var(--mute)">your chat</div>`,
  init(el) { el.querySelector('#tl').innerHTML = ['sunset', 'dog', 'X', 'pizza', 'hills'].map((n, i) => `<div class="tile t${i}" style="background-image:${n === 'X' ? 'none' : I(n)};${n === 'X' ? 'background:#866' : ''}">${n === 'X' ? `<div class="bl" style="position:absolute;inset:-30px;background-image:${I('coffee')};background-size:cover;filter:blur(30px) hue-rotate(-30deg)"></div>` : ''}<div class="mk2" style="position:absolute;right:10px;top:10px;font:900 44px Inter"></div></div>`).join(''); },
  draw(S) { const tb = S.T('bouncer'); S.$('#mk').style.setProperty('--m', S.P(tb - .1, .3)); if (S.on(tb)) S.sfx(tb, 'ding'); const t0 = S.T('checked') - 1.0; let red = false;
    S.$$('.tile').forEach((t, i) => { const u = clamp((S.t - t0 - i * .4) / 1.3); const bad = i === 2; t.style.left = (40 + 870 * u) + 'px'; t.style.top = '800px'; t.style.opacity = u > 0 ? 1 : 0; t.style.zIndex = u > .4 && u < .6 ? 2 : 4;
      const m = t.querySelector('.mk2'); if (u > .5) { m.textContent = bad ? '⚠️' : '✓'; m.style.color = bad ? '#fff' : '#3ddc84'; t.style.boxShadow = bad ? '0 0 0 6px var(--red),0 0 40px rgba(255,59,59,.7)' : '0 0 0 6px var(--grn)'; if (bad && u < .9) red = true; } if (Math.abs(u - .5) < .025) S.sfx(S.t, bad ? 'buzz' : 'click'); });
    S.$('#gt').style.boxShadow = red ? '0 0 0 5px var(--red),0 0 60px rgba(255,59,59,.6)' : '0 0 0 5px var(--grn),0 0 50px rgba(61,220,132,.4)'; S.$('#gt').style.color = red ? 'var(--red)' : 'var(--grn)'; }},
 { // 3 arrives blurred with warning in the real chat
  html: `<div class="ph" style="left:220px;top:300px">${HEAD}<div class="bb out" style="top:220px">hey! how's your week? 😊</div>${BLUR(340, 'coffee')}</div>`,
  draw(S) { const tb = S.T('blurred'), p = S.P(tb - .5, .3, back); S.$('.im').style.opacity = clamp(p); S.$('.im').style.transform = `scale(${.7 + .3 * clamp(p)})`; if (S.on(tb - .5)) S.sfx(tb - .5, 'pop');
    const tw = S.T('warning'); S.$('.wr span').style.transform = `scale(${S.on(tw - .2) ? 1 + .15 * Math.abs(Math.sin(S.t * 8)) : 1})`; }},
 { // 4 you decide
  html: `<div class="ph" style="left:220px;top:300px">${HEAD}<div class="bb out" style="top:220px">hey! how's your week? 😊</div>${BLUR(340, 'coffee')}
     <div class="abs" style="left:0;right:0;top:900px;text-align:center"><span class="act a0" style="background:#f0f0f0;color:#111">Open</span><span class="act a1" style="background:#111;color:#fff">Block</span></div>
     <div class="abs" style="left:0;right:0;top:1020px;text-align:center"><span class="act a2" style="background:#e5484d;color:#fff">🚩 Report</span></div></div>`,
  draw(S) { [['Open', 0], ['Block', 1], ['report', 2]].forEach(([w, i]) => { const at = S.T(w) - .2, p = S.P(at, .25, back); const a = S.$('.a' + i); a.style.opacity = clamp(p); a.style.transform = `scale(${.6 + .4 * clamp(p) + (S.on(at) && S.t < at + .25 ? .12 : 0)})`; if (S.on(at)) S.sfx(at, 'click'); }); }},
 { // 5 98% (drop)
  html: `<svg class="ring" viewBox="0 0 500 500"><circle cx="250" cy="250" r="210" stroke="#2a2a31" stroke-width="34" fill="none"/><circle id="arc" cx="250" cy="250" r="210" stroke="#ffc629" stroke-width="34" fill="none" stroke-linecap="round" transform="rotate(-90 250 250)" stroke-dasharray="1320" stroke-dashoffset="1320"/></svg>
   <div class="abs center big" id="pc" style="top:590px;font-size:150px;color:#ffc629">0%</div><div class="abs center h2" style="top:980px">accurate in testing</div>`,
  draw(S) { if (S.t < .07) flash(.5); const tn = S.T('ninety-eight'), p = S.P(.05, tn, eo); S.$('#pc').textContent = Math.round(98 * p) + '%'; S.$('#arc').setAttribute('stroke-dashoffset', 1320 * (1 - .98 * p));
    S.$('.ring').style.transform = `scale(${1 + .06 * Math.max(0, 1 - Math.abs(S.t - tn) * 4)})`; if (S.on(tn)) S.sfx(tn, 'thud'); }},
 { // 6 gave it away: real-looking repo + apps light up
  html: `<div class="repo" id="rp"><div class="t">bumble-tech / private-detector</div><div style="margin-top:12px;color:#8b949e">Pretrained model for detecting lewd images</div><div class="tags"><span>Apache-2.0</span><span>open source</span><span>free</span></div></div>
   ${['#ff5a5f', '#4c9dff', '#8a3ffc', '#00b67a', '#ff9f1c', '#e1306c'].map((c, i) => `<div class="app ap" style="left:${100 + (i % 3) * 320}px;top:${760 + Math.floor(i / 3) * 230}px;background:${c}">${'ABCDEF'[i]}</div>`).join('')}
   <div class="abs center kick" style="top:1260px" id="fr">any app can use it · for free</div>`,
  draw(S) { const tg = S.T('away'); const r = S.P(tg - .4, .3, back); S.$('#rp').style.opacity = clamp(r); S.$('#rp').style.transform = `translateY(${(1 - clamp(r)) * 80}px)`; if (S.on(tg - .4)) S.sfx(tg - .4, 'whoosh');
    const tf = S.T('free'); S.$$('.ap').forEach((a, i) => { const at = tf - .3 + i * .12, p = S.P(at, .25, back); a.style.opacity = clamp(p); a.style.transform = `scale(${.5 + .5 * clamp(p)})`; a.style.boxShadow = S.on(at) ? '0 0 0 5px var(--grn),0 20px 40px rgba(0,0,0,.5)' : ''; if (S.on(at)) S.sfx(at, 'pop'); });
    S.$('#fr').style.opacity = S.P(tf, .3); }},
 ctaScene(),
];
