// Web-reel runtime. Each reel defines SCENES = [ {html:`...`, draw(S){...}} ] in scenes.js (one per narration line).
// DATA (timing) is injected by engine/webreel.py: {total, spans:[[t0,t1]], words:[[w,t0,t1,si]], chunks:[[st,en,[[w,t0,t1]]]]}
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lin = (t, a, b) => clamp((t - a) / (b - a));
const eo = x => 1 - Math.pow(1 - x, 3);
const eio = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const back = x => { const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const mixc = (a, b, p) => a.map((v, i) => Math.round(v + (b[i] - v) * p));
const rgb = a => `rgb(${a.join(',')})`;
const fmt = n => Math.round(n).toLocaleString('en-US');
const fmtIN = n => Math.round(n).toLocaleString('en-IN');
const R = i => ((Math.sin(i * 99.13) * 43758.5) % 1 + 1) % 1;   // deterministic random
window.SFX = [];
let built = false;

function build() {
  const root = $('#scenes');
  SCENES.forEach((s, i) => { const d = document.createElement('div'); d.className = 'scene'; d.id = 's' + i; d.innerHTML = s.html || ''; root.appendChild(d); s.el = d; if (s.init) s.init(d); });
  built = true;
}

function helper(si, t) {
  const [t0, t1] = DATA.spans[si];
  const words = DATA.words.filter(w => w[3] === si).map(w => [w[0], w[1] - t0, w[2] - t0]);
  const norm = w => w.toLowerCase().replace(/[^a-z0-9%'-]/g, '');
  const S = {
    t: t - t0, dur: t1 - t0, abs: t, el: SCENES[si].el,
    T(word, n = 1) { let k = 0; for (const w of words) if (norm(w[0]) === norm(word) && ++k === n) return w[1];
      throw new Error(`scene ${si}: word "${word}" #${n} not found in: ${words.map(w => w[0]).join(' ')}`); },
    P(at, d = .4, e = eo) { return e(lin(S.t, at, at + d)); },
    on(at) { return S.t >= at; },
    sfx(at, kind = 'pop') { if (at >= 0 && at <= S.dur) SFX.push([+(t0 + at).toFixed(3), kind]); },
    $(s) { return $(s, S.el); }, $$(s) { return $$(s, S.el); },
  };
  return S;
}

window.render = function (t) {
  if (!built) build();
  let si = DATA.spans.findIndex(([a, b]) => t >= a && t < b); if (si < 0) si = DATA.spans.length - 1;
  SCENES.forEach((s, i) => s.el.style.display = i === si ? 'block' : 'none');
  const S = helper(si, t);
  SCENES[si].draw(S);
  // camera: tiny punch-in on every cut + slow drift
  const lt = S.t, p = 1 - eo(lin(lt, 0, .32));
  const cam = SCENES[si].noCam ? '' : `scale(${1 + .045 * p + .012 * lt / Math.max(1, S.dur)})`;
  SCENES[si].el.style.transform = cam;
  $('#flash').style.opacity = (si > 0 && lt < 1.5 / 30 && !SCENES[si].noFlash) ? .18 : (window.FLASH || 0);
  window.FLASH = 0;
  // captions
  const ch = DATA.chunks.find(c => t >= c[0] && t < c[1]);
  const cap = $('#cap');
  if (SCENES[si].noCap || !ch) cap.innerHTML = '';
  else { let act = -1; ch[2].forEach((w, j) => { if (w[1] - .05 <= t) act = j; });
    cap.innerHTML = ch[2].map((w, j) => `<span class="${j === act ? 'on' : ''}">${w[0].replace(/[<>&]/g, '')}</span>`).join(''); }
  $('#prog').style.width = (100 * t / DATA.total) + '%';
};
window.flash = v => { window.FLASH = v; };

// Shared last scene: profile-style grid of real series covers + follow button.
window.SERIES_COVERS = ['S1E01', 'S1E14', 'S2E05', 'S1E16', 'S3E23', 'S1E06'];
window.ctaScene = (extra = '') => ({
  html: `<div class="abs center h2" style="top:290px;font-size:70px">Understand systems<br><i style="color:var(--yel)">like this</i></div>
    <div class="cta-grid">${SERIES_COVERS.map(c => `<img src="../../covers/${c}.jpg">`).join('')}</div>
    <div class="abs center" style="top:1330px"><span class="cta-btn" id="fb">Follow @tech.explained.dev</span></div>
    <div class="abs center" style="top:1460px;font:500 32px Roboto;color:var(--mute)">full system design series on my page</div>${extra}`,
  draw(S) {
    S.$$('.cta-grid img').forEach((im, i) => { const p = S.P(.05 + i * .05, .3, back); im.style.opacity = clamp(p); im.style.transform = `scale(${.85 + .15 * clamp(p)})`; });
    let tf; try { tf = S.T('Follow'); } catch (e) { tf = S.dur - .8; }
    const b = S.$('#fb'); const pul = S.on(tf) ? 1 + .06 * Math.sin((S.t - tf) * 12) * Math.exp(-(S.t - tf) * 2) : 1;
    b.style.transform = `scale(${pul})`; if (S.on(tf)) S.sfx(tf, 'pop');
    try { const ts = S.T('series'); S.$('.cta-grid').style.boxShadow = S.on(ts) ? '0 0 0 4px var(--yel),0 50px 110px rgba(0,0,0,.6)' : ''; } catch (e) {}
  }});
