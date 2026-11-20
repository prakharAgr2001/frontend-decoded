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
.meta{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:4px 0 14px;color:var(--mute);font-weight:600;font-size:14px}
.reel{display:inline-flex;align-items:center;gap:8px;background:var(--red);color:#fff;text-decoration:none;font-weight:700;font-size:14px;padding:8px 14px;border-radius:99px}
.tabs{display:flex;gap:0;margin:8px 0 0;border:3px solid var(--ink);border-radius:14px;overflow:hidden;width:max-content;box-shadow:4px 4px 0 var(--ink)}
.tabs button{font:700 15px Inter,sans-serif;border:0;background:#fff;color:var(--ink);padding:10px 18px;cursor:pointer}.tabs button.on{background:var(--ink);color:#fff}
.pane{display:none}.pane.on{display:block}
.deep{margin-top:18px}.deep h2{font:700 26px/1.15 Oswald,Impact,sans-serif;text-transform:uppercase;margin:38px 0 10px;scroll-margin-top:16px}
.deep h2::before{content:'';display:inline-block;width:12px;height:22px;background:var(--yel);margin-right:10px;vertical-align:-2px;border:2px solid var(--ink)}
.deep h3{font-size:19px;margin:24px 0 6px}.deep p,.deep li{font-size:17px}.deep li{margin:6px 0}
.deep h2#unused-one-line+p{font:600 20px/1.45 Inter,sans-serif;background:var(--yel);border:3px solid var(--ink);border-radius:16px;padding:16px 18px;box-shadow:5px 5px 0 var(--ink)}
.deep h2#interview-answer+blockquote{margin:12px 0;background:var(--ink);color:#fff;border-radius:16px;padding:36px 18px 16px 18px;position:relative;font-size:16.5px}
.deep h2#interview-answer+blockquote::before{content:'SAY THIS';position:absolute;left:18px;top:14px;font:800 11px Inter,sans-serif;letter-spacing:1.5px;color:var(--yel)}
.deep h2#interview-answer+blockquote code{background:#2c2f38;color:#ffe58a}
.deep h2#common-traps+ul{list-style:none;padding-left:0}.deep h2#common-traps+ul li{border-left:4px solid var(--red);padding:2px 0 2px 14px;margin:12px 0}
.deep h2#key-points+ul{background:var(--yel);border:3px solid var(--ink);border-radius:16px;padding:14px 18px 14px 36px;box-shadow:5px 5px 0 var(--ink)}
.deep pre{background:#15171C;color:#e8e6df;border-radius:14px;padding:16px 18px;overflow-x:auto;font-size:14px;line-height:1.55}
.deep pre code{background:none;padding:0;color:inherit;font-size:14px}
.deep pre.mermaid{background:#fff;border:2px solid var(--ink);color:var(--ink);text-align:center;padding:18px 8px}
.deep table{display:table;background:#fff;border:2px solid var(--ink);border-radius:12px;overflow:hidden}.deep th{background:var(--ink);color:#fff}
.deep details{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:12px 16px;margin:12px 0}
.deep details summary{font-weight:700;cursor:pointer;list-style:none}.deep details summary::before{content:'Q ';color:var(--red);font-weight:800}
.deep details[open] summary{margin-bottom:8px}.deep details summary::-webkit-details-marker{display:none}
.diagram{margin:16px 0;background:#fff;border:2px solid var(--ink);border-radius:14px;padding:14px 8px;overflow-x:auto;text-align:center}.diagram svg{max-width:100%;height:auto}
.hl-code{background:#15171C!important;border-radius:14px;margin:12px 0;overflow-x:auto}.hl-code pre{margin:0;background:none!important}
pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.hl-code .hll { background-color: #49483e }
.hl-code { background: #272822; color: #F8F8F2 }
.hl-code .c { color: #959077 } /* Comment */
.hl-code .err { color: #ED007E; background-color: #1E0010 } /* Error */
.hl-code .esc { color: #F8F8F2 } /* Escape */
.hl-code .g { color: #F8F8F2 } /* Generic */
.hl-code .k { color: #66D9EF } /* Keyword */
.hl-code .l { color: #AE81FF } /* Literal */
.hl-code .n { color: #F8F8F2 } /* Name */
.hl-code .o { color: #FF4689 } /* Operator */
.hl-code .x { color: #F8F8F2 } /* Other */
.hl-code .p { color: #F8F8F2 } /* Punctuation */
.hl-code .ch { color: #959077 } /* Comment.Hashbang */
.hl-code .cm { color: #959077 } /* Comment.Multiline */
.hl-code .cp { color: #959077 } /* Comment.Preproc */
.hl-code .cpf { color: #959077 } /* Comment.PreprocFile */
.hl-code .c1 { color: #959077 } /* Comment.Single */
.hl-code .cs { color: #959077 } /* Comment.Special */
.hl-code .gd { color: #FF4689 } /* Generic.Deleted */
.hl-code .ge { color: #F8F8F2; font-style: italic } /* Generic.Emph */
.hl-code .ges { color: #F8F8F2; font-weight: bold; font-style: italic } /* Generic.EmphStrong */
.hl-code .gr { color: #FF4689 } /* Generic.Error */
.hl-code .gh { color: #F8F8F2 } /* Generic.Heading */
.hl-code .gi { color: #A6E22E } /* Generic.Inserted */
.hl-code .go { color: #66D9EF } /* Generic.Output */
.hl-code .gp { color: #FF4689; font-weight: bold } /* Generic.Prompt */
.hl-code .gs { color: #F8F8F2; font-weight: bold } /* Generic.Strong */
.hl-code .gu { color: #959077 } /* Generic.Subheading */
.hl-code .gt { color: #66D9EF } /* Generic.Traceback */
.hl-code .kc { color: #66D9EF } /* Keyword.Constant */
.hl-code .kd { color: #66D9EF } /* Keyword.Declaration */
.hl-code .kn { color: #FF4689 } /* Keyword.Namespace */
.hl-code .kp { color: #66D9EF } /* Keyword.Pseudo */
.hl-code .kr { color: #66D9EF } /* Keyword.Reserved */
.hl-code .kt { color: #66D9EF } /* Keyword.Type */
.hl-code .ld { color: #E6DB74 } /* Literal.Date */
.hl-code .m { color: #AE81FF } /* Literal.Number */
.hl-code .s { color: #E6DB74 } /* Literal.String */
.hl-code .na { color: #A6E22E } /* Name.Attribute */
.hl-code .nb { color: #A6E22E } /* Name.Builtin */
.hl-code .nc { color: #A6E22E } /* Name.Class */
.hl-code .no { color: #66D9EF } /* Name.Constant */
.hl-code .nd { color: #A6E22E } /* Name.Decorator */
.hl-code .ni { color: #F8F8F2 } /* Name.Entity */
.hl-code .ne { color: #A6E22E } /* Name.Exception */
.hl-code .nf { color: #A6E22E } /* Name.Function */
.hl-code .nl { color: #F8F8F2 } /* Name.Label */
.hl-code .nn { color: #F8F8F2 } /* Name.Namespace */
.hl-code .nx { color: #A6E22E } /* Name.Other */
.hl-code .py { color: #F8F8F2 } /* Name.Property */
.hl-code .nt { color: #FF4689 } /* Name.Tag */
.hl-code .nv { color: #F8F8F2 } /* Name.Variable */
.hl-code .ow { color: #FF4689 } /* Operator.Word */
.hl-code .pm { color: #F8F8F2 } /* Punctuation.Marker */
.hl-code .w { color: #F8F8F2 } /* Text.Whitespace */
.hl-code .mb { color: #AE81FF } /* Literal.Number.Bin */
.hl-code .mf { color: #AE81FF } /* Literal.Number.Float */
.hl-code .mh { color: #AE81FF } /* Literal.Number.Hex */
.hl-code .mi { color: #AE81FF } /* Literal.Number.Integer */
.hl-code .mo { color: #AE81FF } /* Literal.Number.Oct */
.hl-code .sa { color: #E6DB74 } /* Literal.String.Affix */
.hl-code .sb { color: #E6DB74 } /* Literal.String.Backtick */
.hl-code .sc { color: #E6DB74 } /* Literal.String.Char */
.hl-code .dl { color: #E6DB74 } /* Literal.String.Delimiter */
.hl-code .sd { color: #E6DB74 } /* Literal.String.Doc */
.hl-code .s2 { color: #E6DB74 } /* Literal.String.Double */
.hl-code .se { color: #AE81FF } /* Literal.String.Escape */
.hl-code .sh { color: #E6DB74 } /* Literal.String.Heredoc */
.hl-code .si { color: #E6DB74 } /* Literal.String.Interpol */
.hl-code .sx { color: #E6DB74 } /* Literal.String.Other */
.hl-code .sr { color: #E6DB74 } /* Literal.String.Regex */
.hl-code .s1 { color: #E6DB74 } /* Literal.String.Single */
.hl-code .ss { color: #E6DB74 } /* Literal.String.Symbol */
.hl-code .bp { color: #A6E22E } /* Name.Builtin.Pseudo */
.hl-code .fm { color: #A6E22E } /* Name.Function.Magic */
.hl-code .vc { color: #F8F8F2 } /* Name.Variable.Class */
.hl-code .vg { color: #F8F8F2 } /* Name.Variable.Global */
.hl-code .vi { color: #F8F8F2 } /* Name.Variable.Instance */
.hl-code .vm { color: #F8F8F2 } /* Name.Variable.Magic */
.hl-code .il { color: #AE81FF } /* Literal.Number.Integer.Long */
.dg{margin:18px 0}
.dg-steps{list-style:none;counter-reset:st;padding:0;margin:0}
.dg-steps li{counter-increment:st;position:relative;background:#fff;border:2px solid var(--ink);border-radius:14px;padding:12px 14px 12px 58px;margin:0 0 22px;box-shadow:3px 3px 0 var(--ink)}
.dg-steps li::before{content:counter(st);position:absolute;left:12px;top:50%;transform:translateY(-50%);width:32px;height:32px;border-radius:50%;background:var(--yel);border:2px solid var(--ink);font:800 16px/28px Inter;text-align:center}
.dg-steps li:not(:last-child)::after{content:'↓';position:absolute;left:50%;bottom:-22px;font:800 18px/20px Inter;color:var(--ink)}
.dg-steps li b{display:block;font-size:16px}.dg-steps li span{display:block;font-size:14.5px;color:#4b4840;margin-top:2px;line-height:1.45}
.dg-loopback{margin:-8px 0 0;text-align:center;font:700 14px Inter;color:var(--red)}
.dg-chat{background:#fff;border:2px solid var(--ink);border-radius:16px;padding:12px}
.dg-msg{max-width:88%;margin:8px 0;padding:9px 12px;border-radius:14px 14px 14px 4px;background:#FFF3C4;border:1.5px solid var(--ink)}
.dg-msg.reply{margin-left:auto;border-radius:14px 14px 4px 14px;background:#E8F7EE}
.dg-msg .who{font:800 11.5px Inter;letter-spacing:.3px;text-transform:uppercase;color:#4b4840}.dg-msg .who i{font-style:normal;color:var(--red)}
.dg-msg .say{font-size:15px;line-height:1.4;margin-top:2px;overflow-wrap:anywhere}
.dg-note{text-align:center;font:600 13.5px Inter;color:#4b4840;margin:10px 0;padding:6px;border:1.5px dashed #b9b3a5;border-radius:10px}
.dg-compare{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.dg-col{border:2px solid var(--ink);border-radius:14px;overflow:hidden;background:#fff}.dg-h{font:800 14px Inter;padding:9px 10px;color:#fff}
.dg-col.bad .dg-h{background:var(--ink)}.dg-col.good .dg-h{background:var(--yel);color:var(--ink)}
.dg-c{font-size:14px;line-height:1.4;padding:9px 10px;border-top:1px solid var(--line);overflow-wrap:anywhere}
.hl-code pre{white-space:pre-wrap;word-break:break-word}
.medium{display:block;margin-top:22px;padding:16px 18px;border:3px solid var(--ink);border-radius:16px;background:#fff;text-decoration:none;box-shadow:5px 5px 0 var(--ink)}.medium:hover{background:var(--yel)}.medium b{display:block;font-size:17px}.medium span{display:block;color:var(--mute);font-size:14.5px;margin-top:3px}
.toc{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:10px 16px;margin-top:16px;font-size:15px}
.toc summary{font-weight:700;cursor:pointer}.toc ul{margin:8px 0 4px;padding-left:20px}.toc a{text-decoration:none}.toc a:hover{background:var(--yel)}
.badge{font:800 11px Inter,sans-serif;background:var(--yel);border:1.5px solid var(--ink);border-radius:99px;padding:2px 8px;margin-left:6px;vertical-align:2px}
@media print{.top,.bar,.nav,.cta,footer,.tabs,.meta,.pill,.toc,#deep{display:none!important}#sheet{display:block!important}body{background:#fff}.sheet{box-shadow:none}}
"""

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#F5F2EA">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{root}fox.png">
<link rel="icon" href="{root}fox.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono&family=Oswald:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css"></head><body><div class="wrap">
<div class="top"><a class="logo" href="{root}"><img src="{root}fox.png" alt="">TECH, <b>EXPLAINED</b></a><a class="follow" href="IGURL">Follow on Instagram</a></div>""".replace('IGURL', IG)
FOOT = """<footer>Short, visual explainers on how the web really works · <a href="IGURL">@tech.explained.dev</a></footer></div>{js}</body></html>""".replace('IGURL', IG)

REELS = {}
for _q in ('publish/queue.json', 'publish/shorts_queue.json'):
    if os.path.exists(_q):
        REELS.update({e['id']: e.get('permalink') for e in json.load(open(_q)) if e.get('permalink')})

def _steps(body, loop=False):
    rows = [l.split('|', 1) for l in body.strip().splitlines() if l.strip()]
    h = ''.join(f'<li><b>{html.escape(t.strip())}</b>{"<span>" + html.escape(d.strip()) + "</span>" if len(r) > 1 and (d := r[1]) else ""}</li>'
                for r in rows for t in [r[0]])
    return f'<ol class="dg-steps{" loop" if loop else ""}">{h}</ol>' + ('<div class="dg-loopback">Then back to step 1, forever</div>' if loop else '')

def _chat(body):
    out = []
    for l in body.strip().splitlines():
        l = l.strip()
        if not l: continue
        if l.lower().startswith('note:'):
            out.append(f'<div class="dg-note">{html.escape(l[5:].strip())}</div>'); continue
        m = re.match(r'(.+?)\s*(->|<-)\s*(.+?):\s*(.*)', l)
        a, arrow, b, msg = m.groups(); reply = arrow == '<-'
        out.append(f'<div class="dg-msg{" reply" if reply else ""}"><div class="who">{html.escape(a)} <i>{"←" if reply else "→"}</i> {html.escape(b)}</div><div class="say">{html.escape(msg)}</div></div>')
    return '<div class="dg-chat">' + ''.join(out) + '</div>'

def _compare(body):
    rows = [[c.strip() for c in l.split('||')] for l in body.strip().splitlines() if l.strip()]
    head, rest = rows[0], rows[1:]
    col = lambda i, cls: f'<div class="dg-col {cls}"><div class="dg-h">{html.escape(head[i])}</div>' + ''.join(f'<div class="dg-c">{html.escape(r[i])}</div>' for r in rest) + '</div>'
    return f'<div class="dg-compare">{col(0, "bad")}{col(1, "good")}</div>'

DIAGRAMS = {'steps': _steps, 'loop': lambda b: _steps(b, True), 'chat': _chat, 'compare': _compare}

LINKS = json.load(open('notes/links.json')) if os.path.exists('notes/links.json') else {}

def medium_card(eid=None):
    art = (LINKS.get('episodes') or {}).get(eid) if eid else None
    prof = LINKS.get('medium_profile')
    if art:
        return f'<a class="medium" href="{html.escape(art)}" target="_blank" rel="noopener"><b>Go deeper on Medium</b><span>Interview questions, follow-ups and design breakdowns for this topic →</span></a>'
    if prof:
        return f'<a class="medium" href="{html.escape(prof)}" target="_blank" rel="noopener"><b>Interview prep on Medium</b><span>System design and frontend interview questions, explained step by step →</span></a>'
    return ''

def render_deep(md_text):
    # ```mermaid blocks -> <pre class="mermaid"> (rendered in the browser); <details> may contain markdown
    md_text = re.sub(r'```(steps|loop|chat|compare)\n(.*?)```', lambda m: '\n<figure class="dg">' + DIAGRAMS[m.group(1)](m.group(2)) + '</figure>\n', md_text, flags=re.S)
    md_text = md_text.replace('<details>', '<details markdown="1">')
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'md_in_html', 'toc'], extension_configs={'toc': {'toc_depth': '2'}, 'codehilite': {'guess_lang': False, 'css_class': 'hl-code'}})
    body = md.convert(md_text)
    links = re.findall(r'<a href="(#[^"]+)">([^<]+)</a>', md.toc)
    toc = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
    return body, toc

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
            eid = f'S{s}E{e:02d}'; dp = f'notes/deep/{eid.lower()}.md'; deep = toc = None; mins = 0
            if os.path.exists(dp):
                deep, toc = render_deep(open(dp).read()); mins = max(1, round(len(open(dp).read().split()) / 220))
            out.append(dict(id=eid, s=s, e=e, title=h.group(2).strip(), season=SEASONS.get(s, ''), html=ht, text=text, deep=deep, toc=toc, mins=mins, reel=REELS.get(eid)))
    return sorted(out, key=lambda x: (x['s'], x['e']))

def ep_page(ep, prev, nxt):
    t = html.escape(ep['title']); slug = lambda x: f"../{x['id'].lower()}/"
    p = HEAD.format(title=f"{ep['title']} · S{ep['s']} E{ep['e']} · Tech, Explained cheat sheet",
                    desc=html.escape(ep['text'][:150]), root='../')
    p += f"""<span class="pill">Season {ep['s']} · Episode {ep['e']} · {html.escape(ep['season'])}</span>
<h1><span class="hl">{t}</span></h1>
{deep_block(ep)}
<div class="bar"><a class="btn" href="../">Search all notes</a><button class="btn" onclick="navigator.share?navigator.share({{title:document.title,url:location.href}}):navigator.clipboard.writeText(location.href).then(()=>this.textContent='Link copied')">Share</button></div>
<div class="nav">{f'<a href="{slug(prev)}"><small>← PREVIOUS</small>{html.escape(prev["title"])}</a>' if prev else '<span></span>'}
{f'<a class="r" href="{slug(nxt)}"><small>NEXT →</small>{html.escape(nxt["title"])}</a>' if nxt else ''}</div>
{medium_card(ep['id'])}
<div class="cta">These notes go with a 60-second reel. New reel every day: <a href="{IG}">follow @tech.explained.dev</a></div>"""
    return p + FOOT.format(js=DEEP_JS if ep.get('deep') else '')

def deep_block(ep):
    reel = f'<a class="reel" href="{ep["reel"]}" target="_blank" rel="noopener">Watch the reel</a>' if ep.get('reel') else ''
    if not ep.get('deep'):
        return f'<div class="meta">{reel}</div><div class="sheet">{ep["html"]}</div>'
    return f'''<div class="meta">{reel}<span>{ep["mins"]} min read</span></div>
<div class="tabs"><button class="on" data-p="deep">Notes</button><button data-p="sheet">Cheat sheet</button></div>
<div class="pane on" id="deep"><details class="toc"><summary>On this page</summary><ul>{ep["toc"]}</ul></details><div class="deep">{ep["deep"]}</div></div>
<div class="pane" id="sheet"><div class="sheet">{ep["html"]}</div><div class="bar"><button class="btn" onclick="print()">Print / save as PDF</button></div></div>'''

DEEP_JS = '''<script>
document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.tabs button').forEach(x=>x.classList.toggle('on',x===b));
  document.querySelectorAll('.pane').forEach(p=>p.classList.toggle('on',p.id===b.dataset.p));history.replaceState(null,'',b.dataset.p==='sheet'?'#cheatsheet':location.pathname)});
if(location.hash==='#cheatsheet')document.querySelector('[data-p=sheet]').click();
</script>'''

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
    h+=`<a class="item${i===0&&v?' sel':''}" href="${d.id.toLowerCase()}/"><span class="n">S${d.s} · E${String(d.e).padStart(2,'0')}</span><span><span class="t">${esc(d.title)}${d.deep?'<span class="badge">DEEP NOTES</span>':''}</span>${snip?`<span class="snip">…${esc(snip)}…</span>`:''}</span></a>`;});
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
    data = [dict(id=e['id'], s=e['s'], e=e['e'], title=e['title'], season=e['season'], text=e['text'], deep=bool(e.get('deep'))) for e in eps]
    json.dump([dict(d, html=e['html'], deep_html=e.get('deep')) for d, e in zip(data, eps)], open('site/notes.json', 'w'), ensure_ascii=False)
    idx = HEAD.format(title='Tech, Explained · cheat sheets for every reel',
                      desc='Type a season and episode (like s2e5) or a topic and read the one-minute cheat sheet.', root='')
    idx += f"""<h1>Every reel, <span class="hl">one-minute notes</span></h1>
<p class="lead">{len(eps)} cheat sheets across {len({e['s'] for e in eps})} seasons. Type the number from the reel, or what it was about.</p>
<div class="search"><input id="q" type="search" placeholder="s2e5 · 3 10 · event loop" autocomplete="off" aria-label="Search notes">
<div class="hint">Try <code>s1e5</code> <code>2 3</code> <code>season 4 episode 2</code> <code>debounce</code></div></div>
{medium_card()}<div class="chips" id="chips"></div><div id="list"></div>"""
    js = APP_JS.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')).replace('__SEASONS__', json.dumps(SEASONS))
    open('site/index.html', 'w').write(idx + FOOT.format(js=js))
    open('site/404.html', 'w').write(HEAD.format(title='Not found · Tech, Explained', desc='', root='/') +
                                     '<h1><span class="hl">Not found</span></h1><p><a class="btn" href="/">Search all notes</a></p>' + FOOT.format(js=''))
    print('site/:', len(eps), 'episode pages')

if __name__ == '__main__':
    build()
