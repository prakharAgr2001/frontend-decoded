"""CHEATSHEETS.md = every season's cheat sheet in one public page (the link sent by the 'Comment NOTES' auto-DM)."""
import glob, re
files = sorted(glob.glob('notes/season*.md'), key=lambda p: int(re.search(r'season(\d+)', p).group(1)))
files = [f for f in files if re.fullmatch(r'notes/season\d+\.md', f)]
out = ['# Tech, Explained · cheat sheets', '',
       'Key ideas, DevTools tricks and interview traps from every reel. Find your episode below (S = season, E = episode).', '']
out += [f'- [Season {re.search(r"(\d+)", f).group(1)}](#season-{re.search(r"(\d+)", f).group(1)})' for f in files] + ['']
for f in files:
    n = re.search(r'(\d+)', f).group(1)
    body = open(f).read().split('\n', 1)[1].strip()
    body = body.replace('Frontend Decoded', 'Tech, Explained').replace('## E', f'### S{n} · E')
    out += [f'## Season {n}', '', body, '']
open('CHEATSHEETS.md', 'w').write('\n'.join(out))
print('CHEATSHEETS.md:', len(files), 'seasons')

# one page per episode: cheatsheets/SxEyy.md (the per-reel "Comment NOTES" DM links here)
import os
os.makedirs('cheatsheets', exist_ok=True)
for f in files:
    n = re.search(r'(\d+)', f).group(1)
    for sec in re.split(r'\n(?=## E\d\d)', open(f).read())[1:]:
        m = re.match(r'## E(\d\d) · (.*)', sec)
        ep = f'S{n}E{m.group(1)}'
        body = sec.split('\n', 1)[1].strip().replace('Frontend Decoded', 'Tech, Explained')
        open(f'cheatsheets/{ep}.md', 'w').write(
            f'# {m.group(2).strip()} · S{n} · E{m.group(1)}\n\n{body}\n\n---\n'
            f'Every episode\'s cheat sheet: [all cheat sheets](../CHEATSHEETS.md) · New reel daily on Instagram: @tech.explained.dev\n')
print('per-episode pages:', len(os.listdir('cheatsheets')))
