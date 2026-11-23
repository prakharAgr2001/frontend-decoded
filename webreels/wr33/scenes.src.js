// WR33: Heartbleed (2014): OpenSSL heartbeat trusted the client's length field; up to 64 KB of server memory leaked. ~half a million servers (Netcraft ~17%). No logo drawn.
const MEM = 'BIRD|user=priya&pass=sunflower22|session=8f3a…|GET /account|-----PRIVATE KEY-----MIIEv…|cookie=sid91c…|user=arjun&pass=…|';
const SCENES = [
 { // 0 hook
  html: `<div class="abs center h" style="top:400px;font-size:96px">One <span class="mark" id="mk">missing check</span></div>
   <div class="sites">${[...Array(24)].map(() => '<div class="st"><span class="lk">🔒</span></div>').join('')}</div>`,
  draw(S) { MK(S, '#mk', .1); const t = TT(S, 'exposed', .45); S.$$('.st').forEach((s, i) => { const o = S.on(t + R(i) * 1.2); s.classList.toggle('open', o); s.querySelector('.lk').textContent = o ? '🔓' : '🔒'; }); if (S.on(t)) S.sfx(t, 'buzz'); }},
 { // 1 Heartbleed / OpenSSL
  html: `<div class="abs center kick" style="top:440px">2014</div><div class="abs center h" style="top:520px;font-size:140px"><span class="mark" id="mk">Heartbleed</span></div>
   <div class="abs center lab" style="top:800px;font-size:44px">a bug in OpenSSL</div><div class="addr"><span>🔒</span> https://yourbank.example</div><div class="abs center lab" style="top:1180px;font-size:36px">the code behind this lock</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'Heartbleed', .3)); IN(S, '.addr', TT(S, 'lock', .8) - .3, 40); }},
 { // 2 heartbeat request
  html: `<div class="node c">YOU</div><div class="node s">SERVER</div><div class="msg" id="m1">are you there? send back <b>"BIRD"</b> · <span class="y">length: 4</span></div><div class="msg back" id="m2">"BIRD"</div>`,
  draw(S) { const p = S.P(0, 1.2, eio); S.$('#m1').style.transform = `translateY(${-60 + 200 * p}px)`; S.$('#m1').style.opacity = clamp(S.P(0, .3)); if (S.t < .1) S.sfx(0, 'whoosh');
    const t4 = TT(S, '4', .85); IN(S, '#m2', t4, 40); }},
 { // 3 the lie: ask 64 KB
  html: `<div class="node c">YOU</div><div class="node s">SERVER</div><div class="msg" id="m1">send back <b>"BIRD"</b> · <span class="r" id="ln">length: 4</span></div>
   <div class="abs center h2" id="nc" style="top:1250px;opacity:0">the server <span class="mark" id="mk">never checked</span></div>`,
  init(el) { el.querySelector('#m1').style.transform = 'translateY(140px)'; },
  draw(S) { const t = TT(S, 'checked', .3); IN(S, '#nc', t - .3); MK(S, '#mk', t); const t64 = TT(S, '64', .55); S.$('#ln').textContent = S.on(t64) ? 'length: 65,535' : 'length: 4'; if (S.on(t64)) S.sfx(t64, 'thud'); SHAKE(S, '#m1', t64); }},
 { // 4 memory leak stream
  html: `<div class="abs center kick" style="top:400px">what came back</div><div class="leak" id="lk"></div>`,
  draw(S) { const n = Math.floor(S.P(0, S.dur - .3, x => x) * MEM.length * 3); let s = (MEM + MEM + MEM).slice(0, n); s = s.replace(/</g, '&lt;').replace(/(pass=[^&|]*)/g, '<span class="r">$1</span>').replace(/(PRIVATE KEY)/g, '<span class="r">$1</span>').replace(/^BIRD/, '<span class="g">BIRD</span>');
    S.$('#lk').innerHTML = s; if (Math.floor(S.t * 14) % 2) S.sfx(S.t, 'tick'); }},
 { // 5 half a million servers
  html: `<div class="abs center big" id="n" style="top:440px;font-size:170px;color:var(--red)">0</div><div class="abs center lab" style="top:660px;font-size:44px">secure servers open</div>
   <div class="sv">${[...Array(100)].map((_, i) => `<i class="${i < 17 ? 'o' : ''}"></i>`).join('')}</div><div class="abs center lab" style="top:1360px">≈ 1 in 6 secure websites (Netcraft)</div>`,
  draw(S) { COUNT(S, '#n', 0, 500000, 0, 1.2, v => '~' + fmt(v)); S.$$('.sv i.o').forEach((d, i) => d.style.background = S.on(1 + i * .05) ? 'var(--red)' : ''); }},
 { // 6 lesson
  html: `<div class="abs center h" style="top:470px;font-size:90px">Never trust a<br><span class="mark" id="mk">length</span> the user<br>sends you.</div>
   ${WIN('fix', `<span class="k">if</span> (claimed > actual) <span class="k">return</span> <span class="r">drop</span>()`)}`,
  init(el) { el.querySelector('.win').style.top = '920px'; },
  draw(S) { MK(S, '#mk', TT(S, 'length', .4)); }},
 ctaScene(),
];
