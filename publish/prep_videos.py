"""Make upload-ready reels: cover as the first 0.1 s (so thumb_offset=0 shows it) + smaller file.
Usage: python3 -m publish.prep_videos [S1E01 ...]"""
import glob, os, subprocess, sys

def prep(src):
    ep = os.path.basename(src)[:5]
    dst, tmp = f'videos/{ep}.mp4', f'videos/{ep}.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-framerate', '30', '-t', '0.1', '-i', f'covers/{ep}.jpg',
                    '-f', 'lavfi', '-t', '0.1', '-i', 'anullsrc=r=48000:cl=stereo', '-i', src,
                    '-filter_complex', '[0:v]format=yuv420p,setsar=1[c];[2:v]setsar=1[m];[2:a]aresample=48000[a2];[c][1:a][m][a2]concat=n=2:v=1:a=1[v][a]',
                    '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-maxrate', '3M', '-bufsize', '6M',
                    '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', tmp], check=True)
    os.replace(tmp, dst); print(dst, os.path.getsize(dst) // 1024, 'KB', flush=True)

if __name__ == '__main__':
    os.makedirs('videos', exist_ok=True)
    eps = sys.argv[1:] or [os.path.basename(p)[:5] for p in sorted(glob.glob('out/S1E*.mp4'))]
    for e in eps: prep(glob.glob(f'out/{e}_*.mp4')[0])
