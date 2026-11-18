"""Static cheat-sheet website -> site/ (deployed to GitHub Pages by .github/workflows/site.yml).
site/index.html = every season + search; site/sXeYY/index.html = one page per episode.
Built from notes/seasonN.md (the same source as the DMs), so it updates whenever a season is released."""
import glob, html, json, os, re, shutil
import markdown

SEASONS = {}
for line in open('REGISTRY.md'):
    for m in re.finditer(r'S(\d+) · ([^(·—]+?)\s*(?:—[^(]*)?\(', line):
        SEASONS[int(m.group(1))] = m.group(2).strip()
posted = set()
if os.path.exists('publish/queue.json'):
    posted = {e['id'] for e in json.load(open('publish/queue.json')) if e.get('posted')}

CSS = """
:root{--paper:#F4F1EA;--ink:#16181D;--yel:#FFD23F;--red:#E63946;--mute:#6b675f;--card:#fff}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 Inter,system-ui,sans-serif}
a{color:inherit}.wrap{max-width:760px;margin:0 auto;padding:28px 20px 80px}
header{display:flex;align-items:center;gap:12px;margin-bottom:28px}header img{width:44px;height:44px;border-radius:10px}
.brand{font:700 22px Oswald,Impact,sans-serif;letter-spacing:.5px;text-decoration:none}.brand b{color:var(--red);font-weight:700}
h1{font:700 clamp(34px,8vw,56px)/1.05 Oswald,Impact,sans-serif;text-transform:uppercase;margin:6px 0 10px}
h1 span{background:linear-gradient(transparent 12%,var(--yel) 12%,var(--yel) 88%,transparent 88%);padding:0 8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.pill{display:inline-block;background:var(--ink);color:#fff;border-radius:99px;padding:3px 14px;font-weight:700;font-size:14px}
.sub{color:var(--mute);margin:0 0 22px}
.sheet{background:var(--card);border:3px solid var(--ink);border-radius:18px;box-shadow:6px 6px 0 var(--ink);padding:8px 24px}
.sheet ul{padding-left:20px}.sheet li{margin:10px 0}code{background:#f0ece2;border-radius:6px;padding:1px 6px;font-size:.92em}
table{border-collapse:collapse;width:100%;font-size:15px;margin:12px 0}td,th{border-bottom:1px solid #e3ded3;padding:8px;text-align:left;vertical-align:top}
.nav{display:flex;justify-content:space-between;gap:12px;margin-top:26px;font-weight:600}.nav a{text-decoration:none;border-bottom:3px solid var(--yel)}
.cta{margin-top:30px;padding:18px 20px;border-radius:14px;background:var(--ink);color:#fff}.cta a{color:var(--yel)}
input{width:100%;padding:14px 16px;font-size:17px;border:3px solid var(--ink);border-radius:14px;margin:4px 0 26px;background:#fff}
h2{font:700 26px Oswald,Impact,sans-serif;text-transform:uppercase;margin:34px 0 10px}
.list a{display:flex;gap:12px;align-items:center;padding:11px 14px;margin:8px 0;background:#fff;border:2px solid var(--ink);border-radius:12px;text-decoration:none}
.list a:hover{background:var(--yel)}.list .n{font-weight:700;font-size:13px;background:var(--ink);color:#fff;border-radius:99px;padding:2px 10px;white-space:nowrap}
.soon{opacity:.45}footer{margin-top:50px;color:var(--mute);font-size:14px}
"""
HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:image" content="{root}fox.png"><link rel="icon" href="{root}fox.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Oswald:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css"></head><body><div class="wrap">
<header><img src="{root}fox.png" alt=""><a class="brand" href="{root}">TECH, <b>EXPLAINED</b></a></header>"""
FOOT = """<footer>Short, visual explainers on how the web really works. New reel every day on Instagram:
<a href="https://instagram.com/tech.explained.dev">@tech.explained.dev</a></footer></div>{js}</body></html>"""

def episodes():
    out = []
    for f in sorted(glob.glob('notes/season*.md')):
        m = re.fullmatch(r'notes/season(\d+)\.md', f)
        if not m: continue
        s = int(m.group(1))
        for sec in re.split(r'\n(?=## E\d\d)', open(f).read())[1:]:
            h = re.match(r'## E(\d\d) · (.*)', sec)
            body = sec.split('\n', 1)[1].strip().replace('Frontend Decoded', 'Tech, Explained')
            body = re.sub(r'(^\|.*\|[ \t]*\n)(?!\|)', r'\1\n', body, flags=re.M)  # end tables before bullets
            out.append(dict(s=s, e=int(h.group(1)), id=f'S{s}E{h.group(1)}', title=h.group(2).strip(), md=body))
    return sorted(out, key=lambda x: (x['s'], x['e']))

def build():
    eps = episodes()
    shutil.rmtree('site', ignore_errors=True); os.makedirs('site')
    open('site/style.css', 'w').write(CSS)
    shutil.copy('brand/pixel_fox_browser_profile.png', 'site/fox.png')
    open('site/.nojekyll', 'w').close()
    for i, ep in enumerate(eps):
        d = f"site/{ep['id'].lower()}"; os.makedirs(d)
        prev = eps[i - 1] if i and eps[i - 1]['s'] == ep['s'] else None
        nxt = eps[i + 1] if i + 1 < len(eps) and eps[i + 1]['s'] == ep['s'] else None
        t = html.escape(ep['title'])
        page = HEAD.format(title=f"{ep['title']} · cheat sheet · Tech, Explained", desc=f"Cheat sheet: {t}. Key ideas, DevTools tricks and interview traps.", root='../')
        page += f"""<span class="pill">S{ep['s']} · E{ep['e']:02d} · {html.escape(SEASONS.get(ep['s'], ''))}</span>
<h1><span>{t}</span></h1><p class="sub">Cheat sheet: key ideas, DevTools tricks and interview traps.</p>
<div class="sheet">{markdown.markdown(ep['md'], extensions=['tables'])}</div>
<div class="nav"><span>{f'<a href="../{prev["id"].lower()}/">← {html.escape(prev["title"])}</a>' if prev else ''}</span>
<span>{f'<a href="../{nxt["id"].lower()}/">{html.escape(nxt["title"])} →</a>' if nxt else ''}</span></div>
<div class="cta">🦊 Watch this one as a 90-second reel, and get a new one every day: <a href="https://instagram.com/tech.explained.dev">follow @tech.explained.dev</a> · <a href="../">all cheat sheets</a></div>"""
        open(f'{d}/index.html', 'w').write(page + FOOT.format(js=''))
    idx = HEAD.format(title='Cheat sheets · Tech, Explained', desc='Every Tech, Explained reel as a one-minute cheat sheet.', root='')
    idx += """<h1><span>Cheat sheets</span></h1><p class="sub">Every reel as a one-minute read. Find yours by name or episode number (like <b>S1 E05</b>).</p>
<input id="q" placeholder="Search: DNS, event loop, S1 E05…" autocomplete="off">"""
    for s in sorted({e['s'] for e in eps}):
        idx += f'<section><h2>Season {s} · {html.escape(SEASONS.get(s, ""))}</h2><div class="list">'
        for ep in (e for e in eps if e['s'] == s):
            soon = '' if ep['id'] in posted or s == 1 else ' soon'
            idx += (f'<a class="item{soon}" href="{ep["id"].lower()}/" data-k="{ep["id"].lower()} s{s} e{ep["e"]:02d} s{s} e{ep["e"]} {html.escape(ep["title"].lower())}">'
                    f'<span class="n">S{s} · E{ep["e"]:02d}</span>{html.escape(ep["title"])}</a>')
        idx += '</div></section>'
    js = """<script>const q=document.getElementById('q');q.oninput=()=>{const v=q.value.toLowerCase().trim();
document.querySelectorAll('section').forEach(s=>{let any=0;s.querySelectorAll('.item').forEach(a=>{const ok=!v||v.split(/\\s+/).every(w=>a.dataset.k.includes(w));a.style.display=ok?'':'none';any|=ok});s.style.display=any?'':'none'})}</script>"""
    open('site/index.html', 'w').write(idx + FOOT.format(js=js))
    print('site/:', len(eps), 'episode pages')

if __name__ == '__main__':
    build()
