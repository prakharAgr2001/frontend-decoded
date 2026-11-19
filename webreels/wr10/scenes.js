// WR10: Hinge Most Compatible ~ Gale–Shapley (1962). Hinge: 8x more likely to go on a date (beta tests).
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const L = [['A', '#e05a7a', 520], ['B', '#4c9dff', 760], ['C', '#9b6bff', 1000]], Rr = [['X', '#ff9f43', 520], ['Y', '#2ecc71', 760], ['Z', '#e84393', 1000]];
const NODES = `${L.map(n => `<div class="pn" style="left:150px;top:${n[2] - 65}px;background:${n[1]}">${n[0]}</div>`).join('')}${Rr.map(n => `<div class="pn" style="left:800px;top:${n[2] - 65}px;background:${n[1]}">${n[0]}</div>`).join('')}<svg class="abs" style="left:0;top:0" width="1080" height="1400"><g class="lk" stroke-width="10" stroke-linecap="round" fill="none"></g></svg>`;
const line = (a, b, col, dash = '', op = 1) => `<line x1="285" y1="${L[a][2]}" x2="795" y2="${Rr[b][2]}" stroke="${col}" stroke-dasharray="${dash}" opacity="${op}"/>`;
const SCENES = [
 { // 0 hook: Nobel algorithm picks your match
  html: `<div class="pcard" id="pc" style="left:100px;top:420px"><div class="ph" style="background:linear-gradient(135deg,#e05a7a,#ff9f43)">A</div><div class="nm">Your match</div><div class="tg">✨ MOST COMPATIBLE</div></div>
   <div class="medal" id="md" style="left:640px;top:560px;opacity:0">NOBEL<br>PRIZE</div>
   <div class="abs center h2" id="al" style="top:1080px;opacity:0">picked by an <span class="mark">algorithm</span></div>`,
  draw(S) { const p = S.P(0, .3, back); S.$('#pc').style.transform = `scale(${clamp(p)}) rotate(-4deg)`; S.sfx(0.02, 'pop');
    S.$('#al').style.opacity = S.P(S.T('algorithm') - .2, .2); const tn = S.T('Nobel'), o = S.P(tn - .2, .3, back); S.$('#md').style.opacity = clamp(o); S.$('#md').style.transform = `scale(${.5 + .5 * clamp(o)}) rotate(${12 * Math.sin(S.t * 3)}deg)`; if (S.on(tn - .2)) S.sfx(tn - .2, 'ding'); }},
 { // 1 1962, stable marriage problem
  html: `<div class="paper" id="pp"><div style="font:700 30px Mono;color:#8a6d1a;letter-spacing:3px">1962 · GALE &amp; SHAPLEY</div><div style="font:600 52px/1.15 Serif;margin-top:20px">College Admissions and the Stability of Marriage</div><div style="margin-top:24px;color:#666">A mathematical paper…</div></div>
   <div class="abs center h" style="top:1000px;font-size:78px"><span class="mark" id="mk">the stable marriage problem</span></div>`,
  draw(S) { const p = S.P(0, .35, eo); S.$('#pp').style.transform = `translateY(${(1 - p) * 80}px) rotate(-2deg)`; S.$('#pp').style.opacity = p;
    const ts = S.T('stable'); S.$('#mk').style.setProperty('--m', S.P(ts - .1, .4)); S.$('#mk').parentNode.style.opacity = S.on(ts - .2) ? 1 : 0; if (S.on(ts)) S.sfx(ts, 'swish'); }},
 { // 2 goal: no two would rather run off
  html: `${NODES}<div class="badge" id="un" style="left:420px;top:560px;background:var(--red);color:#fff;opacity:0">would rather run off 🏃</div>
   <div class="abs center" style="top:1180px;font:800 46px Roboto" id="gl">goal: <span style="color:var(--grn)">nobody wants to run off</span></div>`,
  draw(S) { const tr = S.T('run'); S.$('.lk').innerHTML = line(0, 1, '#666') + line(1, 0, '#666') + line(2, 2, '#666') + (S.on(tr - .3) ? line(0, 0, '#ff3b3b', '18 22', .5 + .5 * Math.sin(S.t * 12)) : '');
    S.$('#un').style.opacity = S.P(tr - .3, .2); if (S.on(tr - .3)) S.sfx(tr - .3, 'buzz'); S.$('#gl').style.opacity = S.P(0, .3); }},
 { // 3 rank + propose to top choice
  html: `${NODES}${L.map((n, i) => `<div class="badge rk" style="left:40px;top:${n[2] + 70}px;background:#1d1d23;color:var(--mute);font-size:24px">ranks: ${['Y X Z', 'Y Z X', 'Z X Y'][i]}</div>`).join('')}`,
  draw(S) { const tr = S.T('ranks'), tp = S.T('proposes'); S.$$('.rk').forEach(r => r.style.opacity = S.P(tr - .2, .3)); if (S.on(tr)) S.sfx(tr, 'pop');
    const q = S.P(tp - .2, .5); S.$('.lk').innerHTML = q > 0 ? `<g opacity="${q}">${line(0, 1, '#ffd23f')}${line(2, 2, '#ffd23f')}</g>` : ''; if (S.on(tp)) S.sfx(tp, 'whoosh'); }},
 { // 4 better offer -> switch, dumped proposes next
  html: `${NODES}<div class="badge" id="bo" style="left:430px;top:680px;background:var(--yel);color:#111;opacity:0">B: better offer!</div>
   <div class="badge" id="dp" style="left:110px;top:380px;background:var(--red);color:#fff;opacity:0">💔 dumped</div>`,
  draw(S) { const ts = S.T('switch'), td = S.T('dumped'), tn = S.T('next');
    const sw = S.on(ts - .3); let h = line(2, 2, '#ffd23f') + (sw ? line(1, 1, '#ffd23f') : line(0, 1, '#ffd23f') + line(1, 1, '#4c9dff', '14 18', .7));
    if (S.on(tn - .2)) h += line(0, 0, '#ffd23f', '', S.P(tn - .2, .3)); S.$('.lk').innerHTML = h;
    S.$('#bo').style.opacity = S.P(0, .2); S.$('#dp').style.opacity = S.P(td - .3, .2); if (S.on(ts - .3)) S.sfx(ts - .3, 'swish'); if (S.on(td - .3)) S.sfx(td - .3, 'thud'); }},
 { // 5 stable
  html: `${NODES}<div class="abs center" id="st" style="top:1180px;font:900 70px Roboto;color:var(--grn);opacity:0">STABLE ✓</div>`,
  draw(S) { const tb = S.T('stable'); const on = S.on(tb - .3); S.$('.lk').innerHTML = line(0, 0, on ? '#3ddc84' : '#ffd23f') + line(1, 1, on ? '#3ddc84' : '#ffd23f') + line(2, 2, on ? '#3ddc84' : '#ffd23f');
    const o = S.P(tb - .3, .25, back); S.$('#st').style.opacity = clamp(o); S.$('#st').style.transform = `scale(${1.3 - .3 * clamp(o)})`; if (S.on(tb - .3)) S.sfx(tb - .3, 'ding'); }},
 { // 6 both see each other
  html: `<div class="pcard p0" style="left:70px;top:420px;width:440px"><div class="ph" style="height:300px;background:linear-gradient(135deg,#e05a7a,#ff9f43)">A</div><div class="nm">you see A</div><div class="tg">✨ MOST COMPATIBLE</div></div>
   <div class="pcard p1" style="left:570px;top:420px;width:440px"><div class="ph" style="height:300px;background:linear-gradient(135deg,#4c9dff,#2ecc71)">You</div><div class="nm">A sees you</div><div class="tg">✨ MOST COMPATIBLE</div></div>
   <div class="abs center" id="hr" style="top:1040px;font-size:140px;opacity:0">${EMO('red-heart')}</div>`,
  draw(S) { const tc = S.T('compatible'); S.$('.p0').style.opacity = S.P(tc - .5, .3); const tt = S.T('too'); S.$('.p1').style.opacity = S.P(tt - .5, .3); if (S.on(tt - .5)) S.sfx(tt - .5, 'pop');
    const o = S.P(tt - .1, .3, back); S.$('#hr').style.opacity = clamp(o); S.$('#hr').style.transform = `scale(${.6 + .4 * clamp(o) + .05 * Math.sin(S.t * 10)})`; }},
 { // 7 8x more dates (drop)
  html: `<div class="abs center big" id="x8" style="top:360px;font-size:300px;color:var(--yel)">0×</div><div class="abs center h2" style="top:700px">more likely to go on a <span class="mark" id="mk">date</span></div>
   <div class="abs" style="left:200px;right:200px;top:880px;height:420px;display:flex;align-items:flex-end;gap:120px"><div style="flex:1;text-align:center"><i id="b1" style="display:block;background:#555;border-radius:14px 14px 0 0;height:0"></i><div style="font:600 30px Roboto;color:var(--mute);margin-top:12px">other picks</div></div><div style="flex:1;text-align:center"><i id="b8" style="display:block;background:var(--yel);border-radius:14px 14px 0 0;height:0"></i><div style="font:600 30px Roboto;color:var(--mute);margin-top:12px">Most Compatible</div></div></div>`,
  draw(S) { if (S.t < .07) flash(.5); const te = S.T('eight'), p = S.P(te - .3, .5, eo); S.$('#x8').textContent = Math.round(8 * p) + '×'; S.$('#b1').style.height = (45 * S.P(0, .4)) + 'px'; S.$('#b8').style.height = (360 * p) + 'px'; if (S.on(te)) S.sfx(te, 'thud');
    S.$('#mk').style.setProperty('--m', S.P(S.T('date') - .2, .3)); }},
 ctaScene(),
];
