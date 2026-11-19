// WR01: the number that almost broke YouTube. One scene per narration line.
const MAX = 2147483647;
const WRAP = (() => { const a = new Int32Array([MAX]); a[0]++; return a[0]; })();   // real 32-bit overflow: -2147483648
const CURSOR = `<svg class="cursor" viewBox="0 0 28 40"><path d="M2 2 L2 32 L10 25 L15 37 L20 35 L15 23 L25 23 Z" fill="#fff" stroke="#000" stroke-width="2" stroke-linejoin="round"/></svg>`;
const VCARD = (top) => `<div class="vcard" style="top:${top}px"><div class="vid">
  <div class="beam b1" style="left:140px"></div><div class="beam b2" style="left:420px"></div><div class="beam b3" style="left:700px"></div>
  <div class="crowd"></div><div class="vbar"><i></i></div></div>
  <div class="meta"><div class="vt">K-pop music video (2012) · Official M/V</div>
  <div class="row"><div class="av"></div><span style="color:#f1f1f1;font-weight:500">Music label</span><span>· official channel</span></div>
  <div class="views"><span class="cnt"></span><span class="lab">views</span></div></div></div>`;
function lights(S) { S.$$('.beam').forEach((b, i) => b.style.transform = `rotate(${[-18, 6, 22][i] + 14 * Math.sin(S.abs * 2.2 + i * 2)}deg)`); }
const EDITOR = (top) => `<div class="ed" style="top:${top}px"><div class="edt"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span style="margin-left:20px">counter.js</span></div><div class="code"></div><div class="out"><small>output</small><span class="res"></span></div></div>`;
function typeCode(S, parts, p) {
  const full = parts.map(x => x[1]).join(''), k = Math.floor(full.length * p); let out = '', n = 0;
  for (const [cls, s] of parts) { if (n >= k) break; const part = s.slice(0, k - n); n += s.length; out += cls ? `<span class="${cls}">${part}</span>` : part; }
  S.$('.code').innerHTML = out + '<span class="caret"></span>';
}
const switches = (n, cols) => `<div style="width:${cols * 102}px;margin:0 auto;line-height:0">${'<span class="sw"></span>'.repeat(n)}</div>`;
function setSwitches(S, onCount, bits) { S.$$('.sw').forEach((s, i) => { const on = bits ? bits[i] === '1' : i < onCount; s.classList.toggle('on', on); s.style.setProperty('--x', on ? '38px' : '0px'); }); }

const SCENES = [
 { // 0 HOOK: the number itself, glowing
  html: `<div class="h abs center" style="top:330px;font-size:104px">This number almost<br><span class="mark" id="mk">broke</span> YouTube.</div>
   <div class="abs center big" id="n0" style="top:800px;font-size:136px;color:var(--paper);text-shadow:0 0 60px rgba(255,59,59,.55)">2,147,483,647</div>
   <div class="abs center" style="top:980px;font:500 40px Roboto;color:var(--mute)">views</div>`,
  draw(S) {
    S.$('#mk').style.setProperty('--m', eo(lin(S.t, -.15, .3)));
    const j = S.t < S.dur * .7 ? 1 : 0;   // jitter the digits like they're under pressure
    S.$('#n0').style.transform = `translate(${j * 3 * Math.sin(S.t * 60)}px,${j * 2 * Math.cos(S.t * 47)}px) scale(${1 + .04 * S.t})`;
  }},
 { // 1 2014, racing toward 2 billion
  html: `<div class="abs center kick" style="top:330px">2014</div>${VCARD(420)}
   <div class="abs" style="left:110px;right:110px;top:1330px;height:16px;border-radius:8px;background:#2a2a31"><div id="pb" style="height:100%;border-radius:8px;background:var(--yel)"></div></div>
   <div class="abs" style="right:110px;top:1360px;font:600 28px Roboto;color:var(--mute)">2,000,000,000</div>`,
  draw(S) {
    lights(S); const p = S.P(0, S.dur, x => x);
    S.$('.cnt').textContent = fmt(1.2e9 + .79e9 * eo(p)); S.$('#pb').style.width = (60 + 39 * eo(p)) + '%';
  }},
 { // 2 hard ceiling: column rises and slams into a red line
  html: `<div class="abs center h2" style="top:330px">a <span class="mark" id="mk2">hard ceiling</span></div>
   <div class="ceil" style="top:640px"><span>LIMIT</span></div>
   <div class="abs" style="left:0;right:0;top:648px;height:900px">
     <div class="col" id="c1" style="left:150px;height:30%"></div><div class="col" id="c2" style="left:465px;height:55%"></div><div class="col" id="c3" style="left:780px"></div></div>`,
  draw(S) {
    S.$('#mk2').style.setProperty('--m', S.P(S.T('hard') - .1, .3));
    const p = S.P(0, S.dur * .7, eio); S.$('#c3').style.height = (100 * p) + '%';
    if (p > .99) { S.sfx(S.dur * .7, 'thud'); S.$('#c3').style.boxShadow = '0 -10px 60px rgba(255,59,59,.8)'; }
  }},
 { // 3 the exact number, slammed
  html: `<div class="abs center kick" style="top:520px">the ceiling</div>
   <div class="abs center big" id="num" style="top:620px;font-size:140px"></div>
   <div class="abs center h" id="no" style="top:900px;font-size:110px;opacity:0">Not <span style="color:var(--red)">one</span> view more.</div>`,
  draw(S) {
    const s = fmt(MAX), k = Math.ceil(s.length * S.P(0, S.T('Not') - .1, x => x));
    S.$('#num').textContent = s.slice(0, k); if (k < s.length) S.sfx(S.t, 'tick');
    const tn = S.T('Not'), o = S.P(tn, .2); S.$('#no').style.opacity = o; S.$('#no').style.transform = `scale(${1.15 - .15 * o})`;
    if (S.on(tn)) S.sfx(tn, 'thud'); S.$('#num').style.color = S.on(tn) ? 'var(--yel)' : 'var(--paper)';
  }},
 { // 4 +1 flies into the counter, it shakes, starts to spin
  html: `${VCARD(560)}<div class="abs" id="plus" style="font:800 90px Roboto;color:var(--grn)">+1</div>`,
  draw(S) {
    lights(S); const c = S.$('.cnt'); if (!this.r) this.r = c.getBoundingClientRect();
    const to = S.T('One'), tf = S.T('flip'), p = S.P(to, .6, eio), pl = S.$('#plus');
    pl.style.left = (800 + (this.r.left + 200 - 800) * p) + 'px'; pl.style.top = (420 + (this.r.top - 40 - 420) * p) + 'px'; pl.style.opacity = p < 1 ? 1 : 0;
    if (S.t < tf) { c.textContent = fmt(MAX); c.style.color = '#f1f1f1'; }
    else { c.textContent = fmt(MAX).replace(/\d/g, (d, i) => String(Math.floor(R(i * 7 + Math.floor(S.t * 30)) * 10))); c.style.color = 'var(--yel)'; S.sfx(S.t, 'tick'); }
    const sh = S.on(to + .6) ? 1 : 0; S.$('.vcard').style.transform = `translate(${sh * 6 * Math.sin(S.t * 70)}px,0)`;
  }},
 { // 5 MINUS TWO BILLION: red room, glitch
  noFlash: true,
  html: `<div class="redbg"></div><div class="abs center big glitch" id="neg" style="top:780px;font-size:150px;color:#fff"></div>
   <div class="abs center" style="top:980px;font:700 44px Roboto;letter-spacing:6px;color:#ffd6d6">VIEWS</div>`,
  draw(S) {
    S.sfx(0, 'thud'); if (S.t < .08) flash(.6);
    const g = clamp(1 - S.t / .5); S.$('#neg').textContent = fmt(WRAP).replace('-', '−');
    S.$('#neg').style.textShadow = `${14 * g + 3}px 0 rgba(0,255,255,.75),${-14 * g - 3}px 0 rgba(255,0,80,.85)`;
    S.$('#neg').style.transform = `translate(${10 * g * Math.sin(S.t * 90)}px,0) scale(${1.15 - .15 * eo(lin(S.t, 0, .3))})`;
  }},
 { // 6 why: 32 switches fill up -> exactly that number
  html: `<div class="abs center h2" style="top:330px">stored in <span class="mark" id="mk6">32 bits</span></div>
   <div class="abs center" style="top:560px">${switches(32, 8)}</div>
   <div class="abs center big" id="bn" style="top:1100px;font-size:96px"></div>
   <div class="abs center" style="top:1220px;font:500 30px Roboto;color:var(--mute)">the max of a signed 32-bit integer</div>`,
  draw(S) {
    S.$('#mk6').style.setProperty('--m', S.P(S.T('32') - .1, .3));
    const n = Math.round(31 * S.P(S.T('32') + .2, S.T('biggest') - S.T('32'), x => x));
    setSwitches(S, n); if (n > (this.l || 0)) S.sfx(S.t, 'click'); this.l = n;
    S.$('#bn').textContent = fmt(Math.pow(2, n) - 1); S.$('#bn').style.color = n >= 31 ? 'var(--yel)' : 'var(--paper)';
  }},
 { // 7 64 bits: ceiling shoots up, counter spins to 9 quintillion
  html: `<div class="abs center h2" style="top:330px">rebuilt in <span class="mark" id="mk7">64 bits</span></div>
   <div class="ceil" id="cl" style="top:900px;background:var(--grn);box-shadow:0 0 30px var(--grn)"><span style="color:var(--grn)">NEW LIMIT</span></div>
   <div class="abs center big" id="q" style="top:1150px;font-size:70px;color:var(--grn)"></div>`,
  draw(S) {
    S.$('#mk7').style.setProperty('--m', S.P(S.T('64') - .1, .3));
    const tn = S.T('New'), up = S.P(tn - .3, .5, eio); S.$('#cl').style.top = (900 - 300 * up) + 'px'; if (S.on(tn - .3)) S.sfx(tn - .3, 'whoosh');
    const tq = S.T('quintillion'), big = '9,223,372,036,854,775,807', p = S.P(tq - .7, .7, x => x);
    S.$('#q').textContent = p >= 1 ? big : big.replace(/\d/g, (d, i) => i < big.length * p ? d : String(Math.floor(R(i + Math.floor(S.t * 25)) * 10)));
    if (S.on(tq)) S.sfx(tq, 'ding');
  }},
 { // 8 the troll: hover easter egg
  html: `<div class="abs center" style="top:380px"><span class="pill" style="background:var(--yel);color:#0c0c0e">EASTER EGG</span></div>${VCARD(500)}${CURSOR}
   <img id="sm" src="../../brand/emoji/smirking-face.svg" style="position:absolute;width:150px;left:820px;top:1360px;opacity:0">`,
  draw(S) {
    lights(S); const c = S.$('.cnt'); if (!this.r) this.r = c.getBoundingClientRect();
    const th = S.T('Hover'), ts = S.T('spun'), p = S.P(th - .3, .6, eio);
    const cur = S.$('.cursor'); cur.style.left = (900 + (this.r.left + 120 - 900) * p) + 'px'; cur.style.top = (1500 + (this.r.top + 20 - 1500) * p) + 'px';
    if (S.t < ts) { c.textContent = '9,000,000,000+'; c.style.color = '#f1f1f1'; }
    else if (S.t < ts + .6) { c.textContent = '−' + fmt(MAX).replace(/\d/g, (d, i) => String(Math.floor(R(i * 7 + Math.floor(S.t * 30)) * 10))); S.sfx(S.t, 'tick'); }
    else { c.textContent = fmt(WRAP).replace('-', '−'); c.style.color = 'var(--red)'; S.sfx(ts + .6, 'ding'); }
    const tt = S.T('trolled'), o = S.P(tt, .3, back); S.$('#sm').style.opacity = clamp(o); S.$('#sm').style.transform = `scale(${o}) rotate(${-10 + 10 * o}deg)`;
  }},
 ctaScene(),
];
