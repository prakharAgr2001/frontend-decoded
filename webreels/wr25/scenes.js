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
// WR25: GitLab.com database incident, 31 Jan 2017 (their public postmortem): ~300 GB deleted on the primary, 5 backup methods failed, 6 h of data lost
const BK = ['daily DB dumps', 'disk snapshots', 'uploads to S3', 'replication', 'daily LVM snapshots'];
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" style="top:360px;font-size:220px">5</div><div class="abs center h2" style="top:600px">backup systems</div>
   <div class="bks">${BK.map((b, i) => `<div class="bk" id="k${i}"><span>${b}</span><b>✓</b></div>`).join('')}</div>`,
  draw(S) { const tn = TT(S, 'none', .75); S.$$('.bk').forEach((k, i) => { IN(S, '#k' + i, .1 + i * .15, 30); const x = S.on(tn + i * .12); k.classList.toggle('bad', x); k.querySelector('b').textContent = x ? '✗' : '✓'; if (S.on(tn + i * .12)) S.sfx(tn + i * .12, 'buzz'); }); }},
 { // 1 late at night
  html: `<div class="abs center big" id="ck" style="top:440px;font-size:200px;color:var(--yel)">23:00</div><div class="abs center lab" style="top:700px;font-size:40px">January 2017 · fixing a database</div>
   <div class="abs center" style="top:850px;font-size:200px">${EMO('alarm-clock')}</div>`,
  draw(S) { const m = Math.floor(S.P(0, S.dur, x => x) * 27); S.$('#ck').textContent = '23:' + String(m).padStart(2, '0'); }},
 { // 2 wrong server
  html: `<div class="tile sv" id="s1" style="left:90px;top:440px"><div class="lab">db1</div><b>PRIMARY</b><span>live data</span></div><div class="tile sv" id="s2" style="left:590px;top:440px"><div class="lab">db2</div><b>SECONDARY</b><span>copy</span></div>
   ${WIN('terminal', `<span class="g">$</span> <span id="cmd"></span>`)}`,
  init(el) { el.querySelector('.win').style.top = '920px'; },
  draw(S) { TYPE(S, '#cmd', 'delete data/   # on db1', .1, 1); const tw = TT(S, 'wrong', .7); S.$('#s1').style.boxShadow = S.on(tw) ? '0 0 0 5px var(--red),0 0 80px rgba(255,59,59,.5)' : ''; S.$('#s2').style.opacity = S.on(tw) ? .4 : 1; if (S.on(tw)) S.sfx(tw, 'thud'); SHAKE(S, '#s1', tw); }},
 { // 3 300 GB gone
  html: `<div class="abs center big" id="gb" style="top:460px;font-size:200px">300 GB</div><div class="abs" style="left:110px;right:110px;top:760px;height:60px;border-radius:30px;background:#2a2a31;overflow:hidden"><div id="b" style="height:100%;width:100%;background:var(--blue)"></div></div>
   <div class="stamp" id="g" style="left:330px;top:950px;font-size:110px">GONE</div>`,
  draw(S) { const p = S.P(.3, 1.4, x => x); S.$('#b').style.width = 100 * (1 - p) + '%'; S.$('#gb').textContent = Math.round(300 * (1 - p)) + ' GB'; S.$('#gb').style.color = p >= 1 ? 'var(--red)' : 'var(--paper)'; if (p < 1 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick'); STAMP(S, '#g', TT(S, 'Gone', .75)); }},
 { // 4 backups fail one by one
  html: `<div class="abs center h2" style="top:380px">checking backups…</div><div class="bks" style="top:500px">${BK.map((b, i) => `<div class="bk" id="k${i}"><span>${b}</span><b>?</b></div>`).join('')}</div>`,
  draw(S) { const at = [TT(S, 'one', .1), TT(S, 'Two', .3), TT(S, 'Three', .5), TT(S, 'four', .65), TT(S, 'five', .8)]; S.$$('.bk').forEach((k, i) => { const x = S.on(at[i]); k.classList.toggle('bad', x); k.querySelector('b').textContent = x ? '✗' : '?'; if (S.on(at[i])) S.sfx(at[i], 'buzz'); }); }},
 { // 5 lucky copy
  html: `<div class="tile" id="lc" style="left:150px;right:150px;top:450px;height:320px;padding:50px;box-shadow:0 0 0 5px var(--grn),0 0 80px rgba(61,220,132,.35);opacity:0"><div class="lab">manual copy</div><div style="font:800 80px Roboto;margin-top:20px">6 hours old</div></div>
   <div class="tl6"><i id="t1"></i><i id="t2"></i><span style="left:0">copy</span><span style="right:0">delete</span></div><div class="abs center h2" id="ls" style="top:1250px;opacity:0;color:var(--red)">6 hours of data, lost</div>`,
  draw(S) { POP(S, '#lc', .1, 'ding'); S.$('#t2').style.width = 100 * S.P(TT(S, 'Six', .6) - .2, .8) + '%'; IN(S, '#ls', TT(S, 'lost', .85) - .3); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:470px;font-size:84px">A backup you<br>never <span class="mark" id="mk">restore</span></div><div class="abs center h" id="l2" style="top:760px;font-size:84px;opacity:0">is not a backup.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'restore', .4)); POP(S, '#l2', TT(S, 'not', .7) - .1, 'thud'); }},
 ctaScene(),
];
