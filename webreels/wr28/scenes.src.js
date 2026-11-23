// WR28: Flipkart Big Billion Day, 6 Oct 2014: ~$100M (~₹600 crore) GMV in 10 hours; site trouble, out-of-stock; founders' apology email next day. No logos.
const PROD = (n, p) => `<div class="pr"><div class="pi"></div><b>${n}</b><span>${p}</span><i class="so">SOLD OUT</i></div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="abs center big" id="m" style="top:380px;font-size:170px;color:var(--grn)">₹0</div><div class="abs center lab" style="top:580px;font-size:44px" id="hr">in 0 hours</div>
   <div class="mail" id="ml"><div class="mh">From: The founders</div><div class="ms">We're truly sorry</div></div>`,
  draw(S) { const p = S.P(0, TT(S, 'Then', .55) - .2, x => x); S.$('#m').textContent = '₹' + Math.round(600 * eo(p)) + ' crore'; S.$('#hr').textContent = 'in ' + Math.round(10 * p) + ' hours'; if (p < 1 && Math.floor(S.t * 12) % 2) S.sfx(S.t, 'tick');
    IN(S, '#ml', TT(S, 'apologised', .8) - .2, 80); if (S.on(TT(S, 'apologised', .8) - .2)) S.sfx(TT(S, 'apologised', .8) - .2, 'whoosh'); }},
 { // 1 sale day
  html: `<div class="abs center kick" style="top:420px">6 October 2014 · 8 AM</div><div class="abs center h" style="top:520px;font-size:120px"><span class="mark" id="mk">BIG SALE</span></div><div class="abs center h2" style="top:760px">billed as India's biggest sale</div>`,
  draw(S) { MK(S, '#mk', .2); if (S.t < .1) S.sfx(0, 'pop'); }},
 { // 2 traffic above plan
  html: `<svg class="abs" width="1080" height="1300" style="left:0;top:0"><line x1="110" y1="800" x2="970" y2="800" stroke="var(--grn)" stroke-width="6" stroke-dasharray="20 14"/><path id="tr" d="" stroke="var(--red)" stroke-width="10" fill="none"/></svg>
   <div class="abs lab" style="left:110px;top:820px;color:var(--grn)">planned capacity</div><div class="abs center kick" style="top:420px">traffic</div>`,
  draw(S) { const p = S.P(0, S.dur - .3, x => x); let d = 'M110 1150'; for (let i = 1; i <= 40 * p; i++) { const x = 110 + i * 21.5, y = 1150 - 700 * Math.pow(i / 40, 1.6) - 30 * Math.sin(i); d += ` L${x} ${y}`; } S.$('#tr').setAttribute('d', d); if (Math.floor(S.t * 8) % 2) S.sfx(S.t, 'tick'); }},
 { // 3 failures
  html: `<div class="prods">${[['Phone', '₹9,999'], ['Laptop', '₹24,999'], ['TV', '₹14,999'], ['Watch', '₹999']].map(x => PROD(...x)).join('')}</div>
   <div class="err" id="e1">Something went wrong. Please try again.</div>`,
  draw(S) { const tf = TT(S, 'failed', .1), ts = TT(S, 'seconds', .45); POP(S, '#e1', tf, 'buzz'); S.$$('.pr').forEach((p, i) => { const s = S.on(ts - .3 + i * .15); p.classList.toggle('out', s); if (S.on(ts - .3 + i * .15)) S.sfx(ts - .3 + i * .15, 'click'); }); }},
 { // 4 apology email
  html: `<div class="mail big2" id="ml"><div class="mh">To: every customer</div><div class="ms">Yesterday was a big day for us…</div><div class="mb"><i></i><i></i><i style="width:60%"></i></div><div class="ms y" id="sr" style="opacity:0">we are truly sorry.</div></div>`,
  draw(S) { IN(S, '#ml', .1, 80); POP(S, '#sr', TT(S, 'sorry', .8) - .2, 'ding'); }},
 { // 5 lesson
  html: `<div class="abs center h" style="top:500px;font-size:90px">A sale is a<br><span class="mark" id="mk">load test</span></div><div class="abs center h2" id="l2" style="top:780px;opacity:0">you run on real customers.</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'load', .3)); IN(S, '#l2', TT(S, 'real', .7) - .2); }},
 ctaScene(),
];
