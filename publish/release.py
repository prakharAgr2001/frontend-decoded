"""Publish rendered episodes: covers + upload-ready videos for every out/SxEyy_*.mp4 not yet in videos/,
then rebuild the posting queue and the cheat-sheet page. The daily GitHub Action posts one reel per day.
Usage: python3 -m publish.release            (all seasons)
       python3 -m publish.release S3         (one season)"""
import glob, os, subprocess, sys
want = [a.upper() for a in sys.argv[1:]]
eps = sorted({os.path.basename(p)[:p.split('/')[-1].index('_')] for p in glob.glob('out/S*E*_*.mp4')})
eps = [e for e in eps if not os.path.exists(f'videos/{e}.mp4') and (not want or any(e.startswith(w + 'E') for w in want))]
print('new episodes:', eps or 'none')
if eps:
    subprocess.run([sys.executable, '-m', 'publish.make_covers', *eps], check=True)
    subprocess.run([sys.executable, '-m', 'publish.prep_videos', *eps], check=True)
subprocess.run([sys.executable, '-m', 'publish.build_queue'], check=True)
subprocess.run([sys.executable, '-m', 'publish.build_cheatsheets'], check=True)
subprocess.run([sys.executable, '-m', 'publish.build_site'], check=True)
print('Now: git add videos covers publish/queue.json CHEATSHEETS.md && commit && pull --rebase && push')
