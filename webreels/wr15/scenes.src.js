// WR15: left-pad, 22 Mar 2016. (code shown is our own illustration of padding, not the original package)
const CODE = `<span class="k">function</span> <span class="f">pad</span>(<span class="v">str</span>, <span class="v">len</span>, <span class="v">ch</span>) {
  <span class="v">str</span> = <span class="f">String</span>(<span class="v">str</span>)
  <span class="k">while</span> (<span class="v">str</span>.length < <span class="v">len</span>) {
    <span class="v">str</span> = <span class="v">ch</span> + <span class="v">str</span>
  }
  <span class="k">return</span> <span class="v">str</span>
}`;
const TREE = [['left-pad', 540, 470], ['line-numbers', 540, 690], ['Babel', 540, 910]];
const SCENES = [
 { // 0 hook
  html: `<div class="abs center h" style="top:320px;font-size:96px"><span class="mark" id="mk">11 lines</span> of code</div>
   ${WIN('the idea, simplified', CODE)}<div class="abs center big" id="br" style="top:1240px;font-size:76px;color:var(--red);opacity:0">broke thousands of apps</div>`,
  init(el) { const w = el.querySelector('.win'); w.style.top = '520px'; },
  draw(S) { MK(S, '#mk', .05); const tb = TT(S, 'broke', .4); POP(S, '#br', tb, 'thud'); SHAKE(S, '.win', tb, 16, .8); S.$('.win').style.boxShadow = S.on(tb) ? '0 0 0 4px var(--red),0 60px 120px rgba(0,0,0,.6)' : ''; }},
 { // 1 developer deletes all packages
  html: `${WIN('terminal', `<span class="g">$</span> <span id="cmd"></span>\n<div id="pk"></div>`)}`,
  init(el) { el.querySelector('.win').style.top = '420px'; el.querySelector('.wb').style.minHeight = '880px'; },
  draw(S) { TYPE(S, '#cmd', 'npm unpublish --all', .1, .9); const n = Math.floor(273 * S.P(1.2, S.dur - 1.6, x => x)); S.$('#pk').innerHTML = (n > 0 ? '<div class="m">− removed kik</div>' : '') + (n > 1 ? '<div class="y">− removed left-pad</div>' : '') + (n > 2 ? `<div class="m">− removed ${n - 2} more…</div>` : '') + (n >= 273 ? '<div class="r">273 packages gone</div>' : ''); if (n > 2 && Math.floor(S.t * 10) % 2) S.sfx(S.t, 'click'); this.l = n; }},
 { // 2 what it does
  html: `<div class="abs center kick" style="top:420px">what left-pad does</div>
   <div class="abs center" style="top:560px;font:500 60px Mono">pad(<span class="s">"5"</span>, 3, <span class="s">"0"</span>)</div>
   <div class="abs center" style="top:700px;font-size:80px;color:var(--mute)">↓</div>
   <div class="abs center" id="res" style="top:820px;font:700 200px Mono;color:var(--yel)"><span id="z" style="color:var(--mute)">00</span>5</div>
   <div class="abs center h" id="ti" style="top:1150px;font-size:100px;opacity:0">That's it.</div>`,
  draw(S) { S.$('#z').style.opacity = S.P(TT(S, 'spaces', .3), .4); POP(S, '#ti', TT(S, "That's", .8), 'pop'); }},
 { // 3 dependency tree
  html: `<svg class="abs" style="left:0;top:0" width="1080" height="1500" id="lk"></svg>
   ${TREE.map((n, i) => `<div class="node" id="n${i}" style="left:${n[1] - 200}px;top:${n[2]}px">${n[0]}</div>`).join('')}
   <div class="dots" id="dots">${[...Array(120)].map(() => '<i></i>').join('')}</div><div class="abs center lab" style="top:1440px">React projects built with Babel</div>`,
  draw(S) { const tb = TT(S, 'Babel', .2), tt = TT(S, 'thousands', .55); [0, 1, 2].forEach(i => POP(S, '#n' + i, i === 2 ? tb - .2 : i * .25, 'pop'));
    S.$('#lk').innerHTML = [[0, 1], [1, 2]].map(([a, b]) => `<line x1="540" y1="${TREE[a][2] + 100}" x2="540" y2="${TREE[b][2]}" stroke="#555" stroke-width="6" opacity="${S.on(b === 2 ? tb - .2 : .25) ? 1 : 0}"/>`).join('');
    S.$$('#dots i').forEach((d, i) => { d.style.opacity = S.on(tt + i * .008) ? 1 : 0; }); if (S.on(tt)) S.sfx(tt, 'whoosh'); }},
 { // 4 installs fail
  html: `${WIN('terminal', `<span class="g">$</span> npm install\n<div id="er"></div>`)}<div class="redwash" id="rw"></div>`,
  init(el) { el.querySelector('.win').style.top = '420px'; el.querySelector('.wb').style.minHeight = '880px'; },
  draw(S) { const n = Math.floor(S.t * 7); S.$('#er').innerHTML = [...Array(Math.min(n, 11))].map((_, i) => `<div class="r">npm ERR! 404 Not Found: left-pad</div>`).join(''); if (n !== this.l) S.sfx(S.t, 'buzz'); this.l = n;
    S.$('#rw').style.opacity = .25 * S.P(0, 1); }},
 { // 5 npm brings it back
  html: `<div class="abs" id="bx" style="left:290px;top:500px;width:500px;height:400px;border-radius:30px;background:#16161a;box-shadow:0 0 0 4px var(--grn),0 0 90px rgba(61,220,132,.35);display:flex;align-items:center;justify-content:center;font:700 64px Mono;color:var(--grn)">left-pad</div>
   <div class="stamp g" id="rs" style="left:270px;top:990px;font-size:80px">RESTORED</div><div class="abs center lab" style="top:1200px">a first for npm</div>`,
  draw(S) { const tb = TT(S, 'back', .7), p = S.P(tb - .6, .6, back); S.$('#bx').style.transform = `translateY(${-400 * (1 - clamp(p))}px)`; S.$('#bx').style.opacity = clamp(p); STAMP(S, '#rs', tb, -5); }},
 { // 6 rules changed
  html: `<svg class="abs" style="left:440px;top:400px" width="200" height="240" viewBox="0 0 100 120"><path d="M25 50 V35 A25 25 0 0 1 75 35 V50" stroke="#ffd23f" stroke-width="10" fill="none"/><rect x="12" y="50" width="76" height="62" rx="10" fill="#ffd23f"/></svg>
   <div class="tile" id="ru" style="left:110px;right:110px;top:720px;padding:50px 60px;font:600 46px/1.5 Roboto">New rule:<br><span class="y">popular packages can't just be unpublished</span></div>`,
  draw(S) { IN(S, '#ru', TT(S, 'rules', .2)); if (S.on(TT(S, 'rules', .2))) S.sfx(TT(S, 'rules', .2), 'ding'); }},
 ctaScene(),
];
