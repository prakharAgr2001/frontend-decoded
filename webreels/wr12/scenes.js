// ---- story kit (shared by WR12+; copied into each scenes.js by webreels/_kit/build.sh) ----
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const TT = (S, w, f = .3, n = 1) => { try { return S.T(w, n); } catch (e) { return S.dur * f; } };
const MK = (S, sel, at) => S.$(sel).style.setProperty('--m', S.P(at - .1, .35));
function POP(S, sel, at, snd = 'pop', from = .7) { const e = S.$(sel), p = S.P(at, .3, back); e.style.opacity = clamp(p); e.style.transform = `scale(${from + (1 - from) * clamp(p)})`; if (snd && S.on(at)) S.sfx(at, snd); return p; }
function STAMP(S, sel, at, rot = -8) { const e = S.$(sel), p = S.P(at, .22, back); e.style.opacity = clamp(p * 2); e.style.transform = `rotate(${rot}deg) scale(${1.6 - .6 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'thud'); }
function TYPE(S, sel, txt, at, d) { const k = Math.floor(txt.length * S.P(at, d, x => x)); S.$(sel).innerHTML = txt.slice(0, k).replace(/</g, '&lt;') + (k < txt.length && S.on(at) ? '<span class="caret"></span>' : ''); if (S.on(at) && k < txt.length && Math.floor(S.t * 20) % 2) S.sfx(S.t, 'click'); }
function COUNT(S, sel, a, b, at, d, f = fmt, e = eio) { S.$(sel).textContent = f(a + (b - a) * S.P(at, d, e)); }
function SHAKE(S, sel, at, amp = 12, len = .6) { const k = S.on(at) ? Math.max(0, 1 - (S.t - at) / len) : 0; S.$(sel).style.translate = `${amp * k * Math.sin(S.t * 80)}px ${amp * .5 * k * Math.cos(S.t * 63)}px`; }
function IN(S, sel, at, dy = 60) { const e = S.$(sel), p = S.P(at, .35); e.style.opacity = p; e.style.transform = `translateY(${dy * (1 - p)}px)`; return p; }
const SWITCHES = (n, cols, w = 84) => `<div class="sws" style="width:${cols * (w + 18)}px">${'<span class="sw"></span>'.repeat(n)}</div>`;
function SETSW(S, on) { S.$$('.sw').forEach((s, i) => s.classList.toggle('on', i < on)); }
const WIN = (title, body, cls = '') => `<div class="win ${cls}"><div class="wt"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span>${title}</span></div><div class="wb">${body}</div></div>`;
// ---- end kit ----
// WR12: Boeing 787 had to be power-cycled before 248 days (FAA AD 2015-09-07)
const PLANE = `<svg viewBox="0 0 600 220" class="plane"><path d="M40 120 Q60 95 120 95 L470 95 Q560 100 580 120 Q560 140 470 145 L120 145 Q60 145 40 120Z" fill="#e9e9ee"/>
 <path d="M250 100 L170 10 L215 10 L340 100Z M250 140 L170 230 L215 230 L340 140Z" fill="#c9c9d2"/><path d="M60 110 L20 40 L55 40 L110 100Z" fill="#c9c9d2"/>
 ${[...Array(14)].map((_, i) => `<rect class="wnd" x="${150 + i * 22}" y="108" width="10" height="12" rx="3"/>`).join('')}</svg>`;
const SCENES = [
 { // 0 hook
  html: `<div class="h abs center" style="top:330px;font-size:92px">Switch it off every<br><span class="mark" id="mk">248 days</span></div>
   <div class="abs" id="pl" style="left:240px;top:760px;width:600px">${PLANE}</div>
   <div class="abs center" id="pw" style="top:1080px;font:800 64px Roboto;color:var(--red);opacity:0">${EMO('low-battery')} ALL POWER LOST</div>`,
  draw(S) { MK(S, '#mk', .05); const tp = TT(S, 'power', .7); const off = S.on(tp);
    S.$('#pl').style.transform = `translateY(${8 * Math.sin(S.t * 3) + (off ? 40 * S.P(tp, .8) : 0)}px) rotate(${off ? 4 * S.P(tp, .8) : 0}deg)`;
    S.$$('.wnd').forEach((w, i) => w.setAttribute('fill', off && S.t > tp + i * .03 ? '#333' : '#ffd23f'));
    S.$('#pw').style.opacity = S.P(tp, .2); SHAKE(S, '#pw', tp); if (S.on(tp)) S.sfx(tp, 'thud'); }},
 { // 1 regulator rule
  html: `<div class="tile" id="doc" style="left:150px;right:150px;top:420px;height:900px;background:#f4f1ea;color:#222;padding:60px">
    <div style="font:700 30px Roboto;letter-spacing:4px;color:#666">US AVIATION REGULATOR · 2015</div>
    <div style="font:800 64px/1.1 Roboto;margin:30px 0">Airworthiness<br>Directive</div>
    <div style="font:400 34px/1.5 Roboto;color:#333">Model 787 airplanes powered continuously for <b>248 days</b> can lose all AC electrical power.</div>
    ${[0, 1, 2].map(i => `<div style="height:22px;border-radius:8px;background:#ddd;margin-top:28px;width:${90 - i * 18}%"></div>`).join('')}</div>
   <div class="stamp" id="st" style="left:500px;top:1110px">OFFICIAL</div>`,
  draw(S) { IN(S, '#doc', 0, 120); STAMP(S, '#st', TT(S, 'official', .7)); }},
 { // 2 counter going up
  html: `<div class="abs center kick" style="top:420px">generator control unit · internal counter</div>
   <div class="tile" style="left:110px;right:110px;top:520px;height:300px;display:flex;align-items:center;justify-content:center"><span class="num" id="c" style="font-size:120px">0</span></div>
   <div class="abs center" id="up" style="top:900px;font-size:200px;color:var(--grn)">⬆</div>`,
  draw(S) { const v = Math.pow(S.t / S.dur, 2.2) * 2.1e9; S.$('#c').textContent = fmt(v); if (Math.floor(S.t * 8) % 2) S.sfx(S.t, 'tick');
    S.$('#up').style.transform = `translateY(${-30 * ((S.t * 2) % 1)}px)`; S.$('#up').style.opacity = .4 + .6 * ((S.t * 2) % 1); }},
 { // 3 248 days -> overflow
  html: `<div class="abs center h2" style="top:380px">days of non-stop power</div>
   <div class="abs center big" id="d" style="top:540px;font-size:200px">0</div>
   <div class="abs" style="left:110px;right:110px;top:820px;height:40px;border-radius:20px;background:#2a2a31;overflow:hidden"><div id="b" style="height:100%;background:var(--yel)"></div></div>
   <div class="stamp" id="ov" style="left:270px;top:1000px;font-size:96px">OVERFLOW</div>`,
  draw(S) { const to = TT(S, 'Overflow', .6), p = S.P(0, to - .1, x => x); S.$('#d').textContent = Math.round(248 * p); S.$('#b').style.width = 100 * p + '%';
    S.$('#b').style.background = p > .97 ? 'var(--red)' : 'var(--yel)'; if (p < 1 && Math.floor(S.t * 10) % 2) S.sfx(S.t, 'tick'); STAMP(S, '#ov', to); if (S.t > to && S.t < to + .1) flash(.4); }},
 { // 4 all generators fail at once
  html: `<div class="abs center kick" style="top:400px">4 main generator controllers</div>
   ${[0, 1, 2, 3].map(i => `<div class="tile gen" style="left:${110 + (i % 2) * 450}px;top:${500 + Math.floor(i / 2) * 400}px;width:410px;height:340px;text-align:center;padding-top:60px">
     <div style="font-size:110px" class="gi">${EMO('high-voltage')}</div><div class="lab gs" style="font-size:40px;color:var(--grn)">ONLINE</div></div>`).join('')}`,
  draw(S) { const tf = TT(S, 'fail', .4); S.$$('.gen').forEach(g => { const off = S.on(tf); g.style.boxShadow = off ? '0 0 0 4px var(--red),0 0 80px rgba(255,59,59,.5)' : '';
      g.querySelector('.gs').textContent = off ? 'FAILSAFE' : 'ONLINE'; g.querySelector('.gs').style.color = off ? 'var(--red)' : 'var(--grn)'; g.querySelector('.gi').style.opacity = off ? .15 : 1; });
    if (S.on(tf)) S.sfx(tf, 'buzz'); if (S.t > tf && S.t < tf + .08) flash(.5); }},
 { // 5 the maths
  html: `<div class="abs center h2" style="top:360px">the maths</div>
   <div class="abs center" style="top:500px">${SWITCHES(32, 8, 70)}</div>
   <div class="abs center" id="e1" style="top:930px;font:700 64px Mono;opacity:0">2,147,483,647</div>
   <div class="abs center" id="e2" style="top:1030px;font:500 40px Mono;color:var(--mute);opacity:0">÷ 100 per second ÷ 86,400 s/day</div>
   <div class="abs center" id="e3" style="top:1130px;font:800 110px Roboto;color:var(--yel);opacity:0">≈ 248 days</div>`,
  draw(S) { const t32 = TT(S, '32-bit', .1), th = TT(S, 'hundredth', .45), t2 = TT(S, '248', .8);
    const n = Math.round(32 * S.P(t32, th - t32, x => x)); SETSW(S, n); if (n > (this.l || 0)) S.sfx(S.t, 'click'); this.l = n;
    POP(S, '#e1', t32 + .3, null); POP(S, '#e2', th); POP(S, '#e3', t2 - .2, 'ding'); }},
 { // 6 turn it off and on again
  html: `<div class="abs center kick" style="top:400px">the official fix</div>
   <div class="abs" id="btn" style="left:340px;top:560px;width:400px;height:400px;border-radius:50%;background:#16161a;box-shadow:0 0 0 10px #2a2a31;display:flex;align-items:center;justify-content:center">
   <svg width="200" height="200" viewBox="0 0 100 100"><path d="M30 28 A30 30 0 1 0 70 28" stroke="currentColor" stroke-width="10" fill="none" stroke-linecap="round"/><line x1="50" y1="12" x2="50" y2="50" stroke="currentColor" stroke-width="10" stroke-linecap="round"/></svg></div>
   <div class="abs center h" id="ol" style="top:1060px;font-size:110px">off… <span id="on2" style="opacity:.2">and on again.</span></div>`,
  draw(S) { const tf = TT(S, 'off', .5), to = TT(S, 'on', .75); const st = S.on(to) ? 'var(--grn)' : S.on(tf) ? 'var(--red)' : '#888'; S.$('#btn').style.color = st;
    S.$('#btn').style.boxShadow = `0 0 0 10px ${st === '#888' ? '#2a2a31' : st},0 0 90px ${S.on(tf) ? st : 'transparent'}`; S.$('#on2').style.opacity = S.on(to) ? 1 : .2;
    if (S.on(tf)) S.sfx(tf, 'click'); if (S.on(to)) S.sfx(to, 'ding'); }},
 ctaScene(),
];
