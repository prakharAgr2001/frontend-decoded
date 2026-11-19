"""Shorts (SHnn) and web reels (WRnn) -> posting queue. For every out/SHnn_*.mp4 not yet in videos/: compress to videos/SHnn.mp4,
cover = the hook frame (0.4 s), caption from EP['caption'] + tags. Queue: publish/shorts_queue.json.
Usage: python3 -m publish.release_shorts"""
import glob, importlib, json, os, subprocess
TAGS = '#techexplained #technews #tech #india #ai #github #startup #business #techreels #explained'
FOLLOW = 'Follow @tech.explained.dev for tech, explained in 30 seconds.'
Q = 'publish/shorts_queue.json'
q = {e['id']: e for e in json.load(open(Q))} if os.path.exists(Q) else {}
for src in sorted(glob.glob('out/SH*_*.mp4') + glob.glob('out/WR*_*.mp4')):
    ep = os.path.basename(src).split('_')[0]
    if not os.path.exists(f'videos/{ep}.mp4'):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '26',
                        '-maxrate', '3M', '-bufsize', '6M', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k',
                        '-movflags', '+faststart', f'videos/{ep}.mp4'], check=True)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '0.4', '-i', src, '-frames:v', '1', '-q:v', '3', f'covers/{ep}.jpg'], check=True)
    EP = (importlib.import_module(f'shorts.{ep.lower()}') if ep.startswith('SH') else importlib.import_module(f'webreels.{ep.lower()}.spec')).EP
    e = q.get(ep, {'id': ep, 'posted': False})
    e.update(video=f'videos/{ep}.mp4', cover=f'covers/{ep}.jpg', caption=f"{EP['caption']}\n\n{FOLLOW}\n\n{TAGS}")
    q[ep] = e
json.dump(sorted(q.values(), key=lambda e: e['id']), open(Q, 'w'), indent=1, ensure_ascii=False)
print(len(q), 'shorts,', sum(not e['posted'] for e in q.values()), 'waiting')
