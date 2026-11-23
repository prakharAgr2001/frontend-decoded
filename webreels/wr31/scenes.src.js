// WR31: Gmail announced 1 April 2004 with 1 GB free (Hotmail: 2 MB), search instead of folders, invite-only until Feb 2007. No logos.
const SCENES = [
 { // 0 hook
  html: `<div class="cal"><div class="ch">APRIL 2004</div><div class="cday">1</div></div><div class="abs center h2" style="top:1100px">a new email service launches</div>
   <div class="stamp" id="j" style="left:250px;top:1250px;font-size:84px">A JOKE?</div>`,
  draw(S) { POP(S, '.cal', 0, 'pop'); STAMP(S, '#j', TT(S, 'joke', .75)); }},
 { // 1 a few MB
  html: `<div class="abs center kick" style="top:420px">2004 · free inbox storage</div><div class="bx" style="top:540px"><span>Hotmail (free)</span><div class="tr"><i id="h" style="background:var(--red)"></i></div><b id="hv">2 MB</b></div>
   <div class="abs center lab" style="top:780px;font-size:40px">≈ a few hundred emails, then "inbox full"</div>`,
  draw(S) { S.$('#h').style.width = .2 * S.P(TT(S, 'Hotmail', .6) - .3, .4) + '%'; }},
 { // 2 1 GB, 500x
  html: `<div class="bx" style="top:480px"><span>Hotmail (free)</span><div class="tr"><i style="width:.2%;background:var(--red)"></i></div><b>2 MB</b></div>
   <div class="bx" style="top:700px"><span>Gmail (free)</span><div class="tr"><i id="g" style="background:var(--grn)"></i></div><b>1 GB</b></div>
   <div class="abs center big" id="x" style="top:1000px;font-size:180px;color:var(--yel);opacity:0">500x</div><div class="abs center lab" style="top:1220px;font-size:44px">free</div>`,
  draw(S) { S.$('#g').style.width = 100 * S.P(TT(S, 'gigabyte', .3) - .3, 1, eo) + '%'; POP(S, '#x', TT(S, '500', .75) - .2, 'thud'); }},
 { // 3 search instead of folders
  html: `<div class="fold" id="fd">${['Work', 'Family', 'Bills', 'Old', 'Misc'].map(f => `<div>📁 ${f}</div>`).join('')}</div>
   <div class="srch" id="sr"><span id="q"></span><b>Search</b></div><div class="abs center h2" id="t" style="top:1200px;opacity:0">search, <span class="mark" id="mk">not folders</span></div>`,
  draw(S) { const ts = TT(S, 'search', .3); S.$('#fd').style.opacity = 1 - .8 * S.P(ts, .4); S.$('#fd').style.filter = S.on(ts) ? 'grayscale(1)' : ''; IN(S, '#sr', ts - .1, 40); TYPE(S, '#q', 'flight ticket march', ts + .1, .9); IN(S, '#t', TT(S, 'folders', .8) - .3); MK(S, '#mk', TT(S, 'folders', .8)); }},
 { // 4 invite only
  html: `<div class="inv" id="iv"><div class="lab">YOU'RE INVITED</div><div style="font:800 64px Roboto;margin:24px 0">Join the new email</div><div class="lab">invite-only · 2004 → 2007</div></div><div class="stamp g" id="rl" style="left:330px;top:1150px">IT WAS REAL</div>`,
  draw(S) { IN(S, '#iv', .1, 80); STAMP(S, '#rl', TT(S, 'real', .2), -6); }},
 { // 5 lesson
  html: `<div class="abs center h" style="top:470px;font-size:84px"><span class="mark" id="m1">Cheap storage</span><br>+ <span class="mark" id="m2">great search</span></div><div class="abs center h2" id="l2" style="top:780px;opacity:0">changed how we keep<br>everything.</div>`,
  draw(S) { MK(S, '#m1', TT(S, 'storage', .2)); MK(S, '#m2', TT(S, 'search', .45)); IN(S, '#l2', TT(S, 'changed', .7) - .2); }},
 ctaScene(),
];
