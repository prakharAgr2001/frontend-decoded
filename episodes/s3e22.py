from engine.lib import *

EP = dict(id='S3E22', tag='S3 · E22', short='IQ: ASSETS')

SCENES = [
    (scene_iq_intro('IMAGES · FONTS · 3RD PARTY'),
     "Four interview questions on images, fonts and third party scripts. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'srcset lists the files. Why do you also need sizes?',
              [('widths', 'srcset = files + their widths'), ('shown', 'sizes = how wide it will be shown'), ('density', 'browser picks smallest sharp file (× density)'),
               ('assumes', 'no sizes → assumes 100vw')]),
     "Question one. Srcset lists the image files. Why do you also need sizes? [[3]] Answer: srcset gives the files and their widths. Sizes tells the browser how wide the image will be shown. With both, it picks the smallest sharp file for the screen density. Without sizes, it assumes the full viewport width."),
    (scene_iq(2, 'The LCP element is a hero image, and it is slow. What do you check?',
              [('HTML', 'Plain <img> in the HTML'), ('fetchpriority', 'fetchpriority="high" (or preload)'), ('lazy', 'No loading="lazy"'),
               ('size', 'Right size + AVIF / WebP + CDN')]),
     "Question two. The LCP element is a hero image, and it's slow. What do you check? [[3]] Answer: it's a plain image tag in the HTML, so it's found early. It has fetchpriority high, or a preload. It's not lazy loaded. And it's the right size, in a modern format, from a CDN."),
    (scene_iq(3, 'How do you avoid both invisible text and font layout shifts?',
              [('FOIT', 'FOIT hides text · FOUT swaps later'), ('optional', 'font-display: optional, or swap'), ('adjust', '+ size-adjust matched fallback'),
               ('preload', 'self-host, preload, woff2, subset')]),
     "Question three. How do you avoid both invisible text, and layout shifts from fonts? [[3]] Answer: FOIT hides text, and FOUT swaps it later. Use font display optional, or swap with a fallback matched using size adjust. And get the font in early: self host, preload, woff2, and subset."),
    (scene_iq(4, 'Marketing wants a chat widget. How do you add it safely?',
              [('Measure', 'Measure its cost (block + compare)'), ('facade', 'Facade first, real widget on click'), ('after', 'Or load it after first interaction'),
               ('Reserve', 'Reserve its space → no CLS')]),
     "Question four. Marketing wants a chat widget. How do you add it without hurting your vitals? [[3]] Answer: Measure its cost first, by blocking it and comparing. Ship a facade, and load the real widget on click. Or load it after the first interaction. And reserve its space, so it never shifts the layout."),
    (scene_next('S3 · E23', 'DEBOUNCE', 'stop firing on every keystroke', 'debounce', 'keystroke'),
     "Got all four? Tell me your score below. Next: debounce, and why your search box shouldn't fire on every keystroke. Comment NOTES for the cheat sheet."),
]
