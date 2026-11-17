"""Pixel Fox mascot: static SVG/PNG + animated blink/ear-twitch loop (GIF + MP4)."""
import math, os, subprocess, cairosvg
OUT = os.path.dirname(os.path.abspath(__file__))
INK, OR, OR2, CREAM, YEL, BG = '#16181D', '#F28C28', '#D9701A', '#FFF4E6', '#FFD23F', '#111418'

def fox(blink=0.0, ear=0.0, bob=0.0, wink_px=False):
    e = max(0.08, 1 - blink)  # eye openness
    eyes = ''
    for cx in (442, 638):
        eyes += f'<ellipse cx="{cx}" cy="{612 + bob}" rx="30" ry="{40 * e:.1f}" fill="{INK}"/>'
        if e > 0.5: eyes += f'<circle cx="{cx + 10}" cy="{598 + bob}" r="10" fill="white"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080">
<rect width="1080" height="1080" fill="{BG}"/>
<circle cx="540" cy="560" r="400" fill="{YEL}"/>
<g transform="translate(0,{bob})">
  <!-- ears -->
  <g transform="rotate({-ear * 0.4} 395 380)">
    <path d="M285 470 L345 160 L480 370 Z" fill="{OR}" stroke="{INK}" stroke-width="16" stroke-linejoin="round"/>
    <path d="M325 420 L355 245 L435 370 Z" fill="{INK}"/>
  </g>
  <g transform="rotate({ear} 685 380)">
    <path d="M795 470 L735 160 L600 370 Z" fill="{OR}" stroke="{INK}" stroke-width="16" stroke-linejoin="round"/>
    <path d="M755 420 L725 245 L645 370 Z" fill="{INK}"/>
  </g>
  <!-- head -->
  <path d="M250 480 Q540 300 830 480 Q880 650 705 770 Q610 845 540 868 Q470 845 375 770 Q200 650 250 480 Z" fill="{OR}" stroke="{INK}" stroke-width="16" stroke-linejoin="round"/>
  <!-- cheeks / muzzle -->
  <path d="M285 610 Q420 640 505 760 Q535 820 540 866 Q470 845 385 772 Q275 690 285 610 Z" fill="{CREAM}"/>
  <path d="M795 610 Q660 640 575 760 Q545 820 540 866 Q610 845 695 772 Q805 690 795 610 Z" fill="{CREAM}"/>
  <path d="M250 480 Q540 300 830 480 Q880 650 705 770 Q610 845 540 868 Q470 845 375 770 Q200 650 250 480 Z" fill="none" stroke="{INK}" stroke-width="16" stroke-linejoin="round"/>
  <!-- forehead stripe -->
  <path d="M500 400 Q540 380 580 400 L560 500 Q540 512 520 500 Z" fill="{OR2}"/>
  {eyes}
  <!-- dev glasses -->
  <rect x="372" y="548" width="140" height="124" rx="34" fill="none" stroke="{INK}" stroke-width="14"/>
  <rect x="568" y="548" width="140" height="124" rx="34" fill="none" stroke="{INK}" stroke-width="14"/>
  <path d="M512 600 Q540 584 568 600" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
  <!-- nose + smile -->
  <ellipse cx="540" cy="790" rx="40" ry="28" fill="{INK}"/>
  <ellipse cx="528" cy="781" rx="12" ry="7" fill="white" opacity="0.7"/>
  <path d="M500 830 Q540 860 580 830" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <!-- code tag badge -->
  <rect x="470" y="420" width="140" height="62" rx="31" fill="{INK}"/>
  <text x="540" y="463" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="bold" font-size="40" fill="{YEL}">&lt;/&gt;</text>
</g>
</svg>'''

if __name__ == '__main__':
    open(f'{OUT}/pixel_fox.svg', 'w').write(fox())
    cairosvg.svg2png(bytestring=fox().encode(), write_to=f'{OUT}/pixel_fox_profile.png', output_width=1080, output_height=1080)
    os.makedirs('/tmp/foxf', exist_ok=True)
    N = 72  # 3 s at 24 fps
    for i in range(N):
        t = i / 24
        blink = max(0, 1 - abs(t - 1.2) / 0.08) if abs(t - 1.2) < 0.08 else (max(0, 1 - abs(t - 1.4) / 0.08) if abs(t - 1.4) < 0.08 else 0)
        ear = 10 * math.sin(max(0, t - 2.0) * 18) * math.exp(-max(0, t - 2.0) * 4) if t > 2.0 else 0
        bob = 8 * math.sin(t * 2 * math.pi / 3)
        cairosvg.svg2png(bytestring=fox(blink, ear, bob).encode(), write_to=f'/tmp/foxf/f{i:03d}.png', output_width=540, output_height=540)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '24', '-i', '/tmp/foxf/f%03d.png', '-vf', 'split[a][b];[a]palettegen[p];[b][p]paletteuse', '-loop', '0', f'{OUT}/pixel_fox_animated.gif'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-stream_loop', '2', '-framerate', '24', '-i', '/tmp/foxf/f%03d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', f'{OUT}/pixel_fox_animated.mp4'], check=True)
    print('ok')
