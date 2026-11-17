"""notes/season1_captions.md -> publish/queue.json (one entry per reel). Keeps 'posted' status of existing entries."""
import json, os, re
TAGS = '#techexplained #frontend #webdevelopment #javascript #softwareengineer #systemdesign #codinginterview #webdev #programming #techreels'
md = open('notes/season1_captions.md').read()
q = {}
if os.path.exists('publish/queue.json'):
    q = {e['id']: e for e in json.load(open('publish/queue.json'))}
out = []
for m in re.finditer(r'\*\*E(\d\d) · [^*]+\*\*\n(.*?)(?=\n\n\*\*E|\Z)', md, re.S):
    ep = f'S1E{m.group(1)}'
    cap = m.group(2).strip().replace('Frontend Decoded', 'Tech, Explained')
    e = q.get(ep, {'id': ep, 'posted': False})
    e.update(video=f'videos/{ep}.mp4', cover=f'covers/{ep}.jpg', caption=f'{cap}\n\nFollow @tech.explained.dev for the full series.\n\n{TAGS}')
    out.append(e)
json.dump(out, open('publish/queue.json', 'w'), indent=1, ensure_ascii=False)
print(len(out), 'entries')
