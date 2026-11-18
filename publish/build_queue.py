"""Build publish/queue.json for every season: one entry per videos/SxEyy.mp4, ordered S1E01, S1E02, ... S2E01 ...
Captions come from notes/seasonN_captions.md (**E01 · title** blocks); missing ones get a generic caption.
Keeps 'posted' status of existing entries."""
import glob, importlib, json, os, re
TAGS = '#techexplained #frontend #webdevelopment #javascript #softwareengineer #systemdesign #codinginterview #webdev #programming #techreels'
FOLLOW = 'Follow @tech.explained.dev for the full series.'

def captions(season):
    p = f'notes/season{season}_captions.md'
    if not os.path.exists(p): return {}
    md = open(p).read()
    return {f'S{season}E{m.group(1)}': m.group(2).strip()
            for m in re.finditer(r'\*\*E(\d\d) · [^*]+\*\*\n(.*?)(?=\n\n\*\*E|\n\n---|\Z)', md, re.S)}

def generic(ep):
    s, n = ep[1:ep.index('E')], int(ep[ep.index('E') + 1:])
    short = importlib.import_module(f'episodes.s{s}e{n:02d}').EP['short'].title()
    return f'{short}, explained in under 2 minutes 🦊\nSeason {s}, Episode {n} of Tech, Explained.\n💬 Comment NOTES for the cheat sheet.'

def key(ep): return int(ep[1:ep.index('E')]), int(ep[ep.index('E') + 1:])

if __name__ == '__main__':
    old = {e['id']: e for e in json.load(open('publish/queue.json'))} if os.path.exists('publish/queue.json') else {}
    eps = sorted((os.path.basename(p)[:-4] for p in glob.glob('videos/S*E*.mp4')), key=key)
    caps = {}
    for s in sorted({key(e)[0] for e in eps}): caps.update(captions(s))
    out = []
    for ep in eps:
        cap = caps.get(ep) or generic(ep)
        cap = cap.replace('Frontend Decoded', 'Tech, Explained')
        e = old.get(ep, {'id': ep, 'posted': False})
        e.update(video=f'videos/{ep}.mp4', cover=f'covers/{ep}.jpg', caption=f'{cap}\n\n{FOLLOW}\n\n{TAGS}')
        out.append(e)
    json.dump(out, open('publish/queue.json', 'w'), indent=1, ensure_ascii=False)
    print(len(out), 'entries,', sum(not e['posted'] for e in out), 'waiting')
