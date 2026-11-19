"""Static cheat-sheet website -> site/  (no backend; deployed on Netlify, see netlify.toml).
site/index.html       single-page app: type "s2e5", "2 5", "season 2 episode 5" or a name ("event loop") and read
site/sXeYY/index.html one static page per episode (shareable links, SEO, works without JS)
site/notes.json       all notes (for anything else that wants them)
Built from notes/seasonN.md, so it updates whenever a season is released. Usage: python3 -m publish.build_site"""
import glob, html, json, os, re, shutil
import markdown

SEASONS = {}
for line in open('REGISTRY.md'):
    for m in re.finditer(r'S(\d+) · ([^(·—]+?)\s*(?:—[^(]*)?\(', line):
        SEASONS[int(m.group(1))] = m.group(2).strip()
IG = 'https://instagram.com/tech.explained.dev'

CSS = """
:root{--paper:#F5F2EA;--ink:#15171C;--yel:#FFD23F;--red:#E63946;--mute:#6b675f;--line:#e2ddd1;--card:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 Inter,system-ui,-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}.wrap{max-width:780px;margin:0 auto;padding:18px 18px 90px}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:6px 0 18px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;font:700 21px Oswald,Impact,sans-serif;letter-spacing:.4px}
.logo img{width:38px;height:38px;border-radius:9px;border:2px solid var(--ink)}.logo b{color:var(--red)}
.follow{font-weight:700;font-size:14px;text-decoration:none;background:var(--ink);color:#fff;padding:8px 14px;border-radius:99px;white-space:nowrap}
h1{font:700 clamp(36px,9vw,60px)/1.02 Oswald,Impact,sans-serif;text-transform:uppercase;margin:8px 0 10px}
.hl{background:linear-gradient(transparent 14%,var(--yel) 14%,var(--yel) 86%,transparent 86%);padding:0 8px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.lead{color:var(--mute);margin:0 0 18px}
.search{position:sticky;top:0;z-index:5;background:var(--paper);padding:10px 0 12px}
.search input{width:100%;font:600 19px Inter,system-ui,sans-serif;padding:16px 18px 16px 52px;border:3px solid var(--ink);border-radius:16px;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' fill='none' stroke='%2315171C' stroke-width='3' stroke-linecap='round'%3E%3Ccircle cx='9.5' cy='9.5' r='7'/%3E%3Cpath d='M15 15l5 5'/%3E%3C/svg%3E") 18px 50%/22px no-repeat;box-shadow:5px 5px 0 var(--ink);outline:none;-webkit-appearance:none}
.search input:focus{box-shadow:5px 5px 0 var(--yel)}
.hint{font-size:14px;color:var(--mute);margin-top:10px}.hint code{cursor:pointer}
.chips{display:flex;gap:8px;overflow-x:auto;padding:4px 0 14px;scrollbar-width:none}
.chips button{flex:none;font:700 14px Inter,sans-serif;color:var(--ink);border:2px solid var(--ink);background:#fff;border-radius:99px;padding:7px 14px;cursor:pointer}
.chips button.on{background:var(--ink);color:#fff}
.group h2{font:700 22px Oswald,Impact,sans-serif;text-transform:uppercase;margin:22px 0 8px}
.item{display:flex;gap:12px;align-items:center;padding:12px 14px;margin:8px 0;background:#fff;border:2px solid var(--ink);border-radius:14px;text-decoration:none;transition:transform .08s}
.item:hover,.item.sel{background:var(--yel);transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--ink)}
.n{font:700 13px Inter,sans-serif;background:var(--ink);color:#fff;border-radius:99px;padding:3px 10px;white-space:nowrap}
.t{font-weight:600}.snip{display:block;font-size:13px;color:var(--mute);margin-top:2px}
.empty{padding:30px 6px;color:var(--mute)}
.pill{display:inline-block;background:var(--ink);color:#fff;border-radius:99px;padding:4px 14px;font-weight:700;font-size:14px}
.sheet{background:var(--card);border:3px solid var(--ink);border-radius:20px;box-shadow:7px 7px 0 var(--ink);padding:6px 24px 10px;margin-top:16px}
.sheet ul{padding-left:20px}.sheet li{margin:12px 0}.sheet strong{background:linear-gradient(transparent 60%,#ffe58a 60%)}
code{font-family:'JetBrains Mono',ui-monospace,monospace;background:#f0ece2;border-radius:6px;padding:1px 6px;font-size:.9em}
table{border-collapse:collapse;width:100%;font-size:15px;margin:12px 0;display:block;overflow-x:auto}td,th{border-bottom:1px solid var(--line);padding:8px;text-align:left;vertical-align:top}
.bar{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.btn{font:700 15px Inter,sans-serif;color:var(--ink);border:2px solid var(--ink);background:#fff;border-radius:12px;padding:10px 14px;cursor:pointer;text-decoration:none}
.btn:hover{background:var(--yel)}
.nav{display:flex;justify-content:space-between;gap:10px;margin-top:22px}.nav a{flex:1;max-width:48%;text-decoration:none;border:2px solid var(--ink);border-radius:14px;padding:10px 14px;background:#fff;font-weight:600}
.nav a:hover{background:var(--yel)}.nav small{display:block;color:var(--mute);font-weight:700;font-size:12px}.nav .r{text-align:right;margin-left:auto}
.cta{margin-top:26px;padding:18px 20px;border-radius:16px;background:var(--ink);color:#fff}.cta a{color:var(--yel);font-weight:700}
footer{margin-top:44px;color:var(--mute);font-size:14px}
@media (max-width:520px){.sheet{padding:4px 16px 8px}.follow{display:none}}
"""

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#F5F2EA">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{root}fox.png">
<link rel="icon" href="{root}fox.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono&family=Oswald:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css"></head><body><div class="wrap">
<div class="top"><a class="logo" href="{root}"><img src="{root}fox.png" alt="">TECH, <b>EXPLAINED</b></a><a class="follow" href="IGURL">Follow on Instagram</a></div>""".replace('IGURL', IG)
FOOT = """<footer>Short, visual explainers on how the web really works · <a href="IGURL">@tech.explained.dev</a></footer></div>{js}</body></html>""".replace('IGURL', IG)

def episodes():
    out = []
    for f in glob.glob('notes/season*.md'):
        m = re.fullmatch(r'notes/season(\d+)\.md', f)
        if not m: continue
        s = int(m.group(1))
        for sec in re.split(r'\n(?=## E\d\d)', open(f).read())[1:]:
            h = re.match(r'## E(\d\d) · (.*)', sec)
            body = sec.split('\n', 1)[1].strip().replace('Frontend Decoded', 'Tech, Explained')
            body = re.sub(r'(^\|.*\|[ \t]*\n)(?!\|)', r'\1\n', body, flags=re.M)  # end tables before bullets
            body = re.sub(r'\n---\s*$', '', body).strip()
            e = int(h.group(1))
            ht = markdown.markdown(body, extensions=['tables'])
            text = re.sub(r'<[^>]+>', ' ', ht); text = html.unescape(re.sub(r'\s+', ' ', text)).strip()
            out.append(dict(id=f'S{s}E{e:02d}', s=s, e=e, title=h.group(2).strip(), season=SEASONS.get(s, ''), html=ht, text=text))
    return sorted(out, key=lambda x: (x['s'], x['e']))

def ep_page(ep, prev, nxt):
    t = html.escape(ep['title']); slug = lambda x: f"../{x['id'].lower()}/"
    p = HEAD.format(title=f"{ep['title']} · S{ep['s']} E{ep['e']} · Tech, Explained cheat sheet",
                    desc=html.escape(ep['text'][:150]), root='../')
    p += f"""<span class="pill">Season {ep['s']} · Episode {ep['e']} · {html.escape(ep['season'])}</span>
<h1><span class="hl">{t}</span></h1>
<div class="sheet">{ep['html']}</div>
<div class="bar"><a class="btn" href="../">🔎 Search all notes</a><button class="btn" onclick="navigator.share?navigator.share({{title:document.title,url:location.href}}):navigator.clipboard.writeText(location.href).then(()=>this.textContent='✅ Link copied')">📤 Share</button></div>
<div class="nav">{f'<a href="{slug(prev)}"><small>← PREVIOUS</small>{html.escape(prev["title"])}</a>' if prev else '<span></span>'}
{f'<a class="r" href="{slug(nxt)}"><small>NEXT →</small>{html.escape(nxt["title"])}</a>' if nxt else ''}</div>
<div class="cta">🦊 This is the cheat sheet for a short reel. Watch it, and get a new one every day: <a href="{IG}">follow @tech.explained.dev</a></div>"""
    return p + FOOT.format(js='')

APP_JS = r"""<script>
const D=__DATA__, S=__SEASONS__;
const q=document.getElementById('q'), list=document.getElementById('list'), chips=document.getElementById('chips');
let season=0, sel=0;
const norm=s=>s.toLowerCase().normalize('NFKD').replace(/[^a-z0-9 ]+/g,' ').replace(/\s+/g,' ').trim();
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
D.forEach(d=>d.k=norm(d.title+' '+d.season+' '+d.text));
function parseNum(v){ // "s2e5", "S2 E05", "2 5", "2.5", "2x5", "season 2 episode 5", "s3", "season 3", "e5"
  let m=v.match(/^\s*(?:s(?:eason)?\s*)?(\d{1,2})\s*(?:[ .x:\-\/]+|\s*e(?:p(?:isode)?)?\s*)(\d{1,2})\s*$/i);
  if(m) return {s:+m[1],e:+m[2]};
  m=v.match(/^\s*s(?:eason)?\s*(\d{1,2})\s*$/i); if(m) return {s:+m[1]};
  m=v.match(/^\s*e(?:p(?:isode)?)?\s*(\d{1,2})\s*$/i); if(m) return {e:+m[1]};
  return null;
}
function score(d,words,raw){let sc=0;const t=norm(d.title);
  for(const w of words){if(!d.k.includes(w))return -1; sc+=t.includes(w)?10:1; if(t.startsWith(w))sc+=5;}
  if(t===raw)sc+=50; return sc;}
function render(){
  const v=q.value.trim(), num=parseNum(v); let r=D.filter(d=>!season||d.s===season);
  if(num){r=r.filter(d=>(!num.s||d.s===num.s)&&(!num.e||d.e===num.e));}
  else if(v){const raw=norm(v), w=raw.split(' ').filter(Boolean);
    r=r.map(d=>[score(d,w,raw),d]).filter(x=>x[0]>=0).sort((a,b)=>b[0]-a[0]).map(x=>x[1]);}
  sel=0;
  if(!r.length){list.innerHTML='<div class="empty">No episode found. Try <b>s1e5</b>, <b>2 3</b> or a word like <b>cache</b>. (Interview-question episodes have no notes.)</div>';return}
  const grouped=!v; let h='', cur=-1;
  r.forEach((d,i)=>{ if(grouped&&d.s!==cur){if(cur>0)h+='</div>';cur=d.s;h+=`<div class="group"><h2>Season ${d.s} · ${S[d.s]||''}</h2>`}
    let snip=''; if(v&&!num){const w=norm(v).split(' ')[0], j=d.text.toLowerCase().indexOf(w); if(j>=0)snip=d.text.slice(Math.max(0,j-40),j+80);}
    h+=`<a class="item${i===0&&v?' sel':''}" href="${d.id.toLowerCase()}/"><span class="n">S${d.s} · E${String(d.e).padStart(2,'0')}</span><span><span class="t">${esc(d.title)}</span>${snip?`<span class="snip">…${esc(snip)}…</span>`:''}</span></a>`;});
  if(grouped)h+='</div>'; list.innerHTML=h;
}
chips.innerHTML='<button class="on" data-s="0">All</button>'+Object.keys(S).filter(s=>D.some(d=>d.s==s)).map(s=>`<button data-s="${s}">S${s} · ${S[s]}</button>`).join('');
chips.onclick=e=>{const b=e.target.closest('button');if(!b)return;season=+b.dataset.s;chips.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));render()};
q.oninput=()=>{history.replaceState(null,'',q.value?'#q='+encodeURIComponent(q.value):location.pathname);render()};
q.onkeydown=e=>{const items=[...list.querySelectorAll('.item')];
  if(e.key==='Enter'&&items[sel]){location.href=items[sel].href}
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();sel=Math.max(0,Math.min(items.length-1,sel+(e.key==='ArrowDown'?1:-1)));
    items.forEach((x,i)=>x.classList.toggle('sel',i===sel));items[sel]&&items[sel].scrollIntoView({block:'nearest'})}};
document.querySelectorAll('.hint code').forEach(c=>c.onclick=()=>{q.value=c.textContent;q.oninput();q.focus()});
const h=new URLSearchParams(location.hash.slice(1)).get('q'); if(h)q.value=h;
document.addEventListener('keydown',e=>{if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus()}});
render();
</script>"""

def build():
    eps = episodes()
    shutil.rmtree('site', ignore_errors=True); os.makedirs('site')
    open('site/style.css', 'w').write(CSS)
    shutil.copy('brand/pixel_fox_browser_profile.png', 'site/fox.png')
    for i, ep in enumerate(eps):
        prev = eps[i - 1] if i and eps[i - 1]['s'] == ep['s'] else None
        nxt = eps[i + 1] if i + 1 < len(eps) and eps[i + 1]['s'] == ep['s'] else None
        os.makedirs(f"site/{ep['id'].lower()}")
        open(f"site/{ep['id'].lower()}/index.html", 'w').write(ep_page(ep, prev, nxt))
    data = [dict(id=e['id'], s=e['s'], e=e['e'], title=e['title'], season=e['season'], text=e['text']) for e in eps]
    json.dump([dict(d, html=e['html']) for d, e in zip(data, eps)], open('site/notes.json', 'w'), ensure_ascii=False)
    idx = HEAD.format(title='Tech, Explained · cheat sheets for every reel',
                      desc='Type a season and episode (like s2e5) or a topic and read the one-minute cheat sheet.', root='')
    idx += f"""<h1>Every reel, <span class="hl">one-minute notes</span></h1>
<p class="lead">{len(eps)} cheat sheets across {len({e['s'] for e in eps})} seasons. Type the number from the reel, or what it was about.</p>
<div class="search"><input id="q" type="search" placeholder="s2e5 · 3 10 · event loop" autocomplete="off" aria-label="Search notes">
<div class="hint">Try <code>s1e5</code> <code>2 3</code> <code>season 4 episode 2</code> <code>debounce</code></div></div>
<div class="chips" id="chips"></div><div id="list"></div>"""
    js = APP_JS.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')).replace('__SEASONS__', json.dumps(SEASONS))
    open('site/index.html', 'w').write(idx + FOOT.format(js=js))
    open('site/404.html', 'w').write(HEAD.format(title='Not found · Tech, Explained', desc='', root='/') +
                                     '<h1><span class="hl">Not found</span></h1><p><a class="btn" href="/">🔎 Search all notes</a></p>' + FOOT.format(js=''))
    print('site/:', len(eps), 'episode pages')

if __name__ == '__main__':
    build()
