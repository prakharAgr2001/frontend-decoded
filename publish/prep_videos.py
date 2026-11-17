"""Make upload-ready reels: smaller file (cover is sent separately as cover_url).
Usage: python3 -m publish.prep_videos [S1E01 ...]"""
import glob, os, subprocess, sys

def prep(src):
    ep = os.path.basename(src)[:5]
    dst, tmp = f'videos/{ep}.mp4', f'videos/{ep}.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src,
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-maxrate', '3M', '-bufsize', '6M',
                    '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', tmp], check=True)
    os.replace(tmp, dst); print(dst, os.path.getsize(dst) // 1024, 'KB', flush=True)

if __name__ == '__main__':
    os.makedirs('videos', exist_ok=True)
    eps = sys.argv[1:] or [os.path.basename(p)[:5] for p in sorted(glob.glob('out/S1E*.mp4'))]
    for e in eps: prep(glob.glob(f'out/{e}_*.mp4')[0])
