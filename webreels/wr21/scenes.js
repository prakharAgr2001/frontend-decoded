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
// WR21: Cloudflare outage, 2 July 2019: a WAF regex with catastrophic backtracking -> CPU 100%, 502s for ~27 min
const SITE = i => `<div class="site"><div class="sb"></div><div class="e">502</div><div class="el">Bad Gateway</div></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="tm" style="top:360px;font-size:130px;color:var(--red)">00:00</div><div class="sites">${[...Array(9)].map(SITE).join('')}</div>
   <div class="abs center h" style="top:1330px;font-size:84px"><span class="mark" id="mk">One regex</span></div>`,
  draw(S) { MK(S, '#mk', .05); const p = S.P(0, S.dur, x => x); S.$('#tm').textContent = String(Math.floor(27 * p)).padStart(2, '0') + ':' + String(Math.floor(27 * 60 * p) % 60).padStart(2, '0');
    S.$$('.site').forEach((s, i) => { const at = .3 + R(i) * 1.5; s.classList.toggle('off', S.on(at)); if (S.on(at)) S.sfx(at, 'click'); }); }},
 { // 1 pushed everywhere at once
  html: `<div class="abs center kick" style="top:400px">July 2019 · a new firewall rule</div><div class="globe" id="gl">${[...Array(60)].map((_, i) => `<i style="left:${50 + 44 * Math.cos(i * 2.4) * Math.sqrt(R(i))}%;top:${50 + 44 * Math.sin(i * 2.4) * Math.sqrt(R(i))}%"></i>`).join('')}</div>
   <div class="abs center h2" id="ev" style="top:1360px;opacity:0">everywhere, <span class="mark" id="mk">at once</span></div>`,
  draw(S) { const te = TT(S, 'Everywhere', .7); S.$$('#gl i').forEach((d, i) => d.classList.toggle('on', S.on(te - .3))); if (S.on(te - .3)) S.sfx(te - .3, 'whoosh'); IN(S, '#ev', te - .2); MK(S, '#mk', TT(S, 'once', .9)); }},
 { // 2 the regex
  html: `<div class="abs center kick" style="top:440px">a pattern to spot attacks</div><div class="tile" style="left:90px;right:90px;top:560px;height:260px;display:flex;align-items:center;justify-content:center;font:700 96px Mono;color:var(--yel)">/.*.*=.*/</div>
   <div class="abs center lab" style="top:880px;font-size:36px">(simplified)</div>`,
  draw(S) {}},
 { // 3 backtracking explosion
  html: `<div class="abs center kick" style="top:400px">tries per request</div><div class="abs center big" id="n" style="top:500px;font-size:140px">1</div><svg id="tr" class="abs" width="1080" height="900" style="left:0;top:700px"></svg>`,
  draw(S) { const p = S.P(0, S.dur - .3, x => x), lv = Math.floor(1 + 6 * p); S.$('#n').textContent = fmt(Math.pow(4.6, 6 * p)); let h = '';
    for (let d = 0; d < lv; d++) { const n = Math.pow(2, d); for (let k = 0; k < n; k++) { const x = (k + .5) / n * 1000 + 40, y = 40 + d * 130, px = (Math.floor(k / 2) + .5) / (n / 2) * 1000 + 40;
      if (d) h += `<line x1="${px}" y1="${y - 130}" x2="${x}" y2="${y}" stroke="#555" stroke-width="3"/>`; h += `<circle cx="${x}" cy="${y}" r="${Math.max(4, 16 - d * 2)}" fill="${d === lv - 1 ? '#ff3b3b' : '#ffd23f'}"/>`; } }
    S.$('#tr').innerHTML = h; if (lv !== this.l) S.sfx(S.t, 'pop'); this.l = lv; }},
 { // 4 CPUs at 100%
  html: `<div class="cpus">${[...Array(6)].map((_, i) => `<div class="cpu"><div class="lab">CPU ${i + 1}</div><div class="bar"><i></i></div><b>0%</b></div>`).join('')}</div>
   <div class="stamp" id="e" style="left:330px;top:1220px;font-size:100px">502</div>`,
  draw(S) { const t1 = TT(S, '100', .4); S.$$('.cpu').forEach((c, i) => { const v = Math.min(100, 20 + 80 * S.P(i * .08, t1 - i * .08, x => x)); c.querySelector('i').style.width = v + '%'; c.querySelector('b').textContent = Math.round(v) + '%';
      c.querySelector('i').style.background = v > 95 ? 'var(--red)' : 'var(--yel)'; }); STAMP(S, '#e', TT(S, '502', .75)); }},
 { // 5 switched off, recovered
  html: `<div class="tgl" id="tg"><i></i></div><div class="abs center lab" style="top:700px;font-size:40px">firewall rules</div><div class="sites" style="top:780px">${[...Array(9)].map(SITE).join('')}</div>`,
  draw(S) { const to = TT(S, 'off', .25), tr = TT(S, 'recovered', .8); S.$('#tg').classList.toggle('off', S.on(to)); if (S.on(to)) S.sfx(to, 'click');
    S.$$('.site').forEach((s, i) => { const ok = S.on(tr - .6 + i * .05); s.classList.toggle('off', !ok); s.classList.toggle('ok', ok); }); if (S.on(tr)) S.sfx(tr, 'ding'); }},
 { // 6 lessons
  html: `<div class="abs center h2" style="top:400px">the lesson</div>
   <div class="tile chk" id="c1" style="left:110px;right:110px;top:560px;height:190px"><b>✓</b>Test how slow a pattern can get</div>
   <div class="tile chk" id="c2" style="left:110px;right:110px;top:800px;height:190px"><b>✓</b>Roll out gradually</div>
   <div class="roll" id="rl">${['1%', '10%', '50%', '100%'].map(x => `<span>${x}</span>`).join('')}</div>`,
  draw(S) { const a = TT(S, 'Test', .1), b = TT(S, 'Roll', .6); IN(S, '#c1', a); IN(S, '#c2', b); if (S.on(a)) S.sfx(a, 'ding'); if (S.on(b)) S.sfx(b, 'ding'); S.$$('#rl span').forEach((s, i) => s.classList.toggle('on', S.on(b + .2 + i * .3))); }},
 ctaScene(),
];
