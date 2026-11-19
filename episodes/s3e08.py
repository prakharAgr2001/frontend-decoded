from engine.lib import *

EP = dict(id='S3E08', tag='S3 · E08', short='IQ: METRICS', hook='4 questions on web vitals')

SCENES = [
    (scene_iq_intro('MEASURING PERFORMANCE'),
     "Four interview questions on measuring performance. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Name the three Core Web Vitals and their "good" thresholds.',
              [('loading', 'LCP ≤ 2.5 s · loading'), ('responsiveness', 'INP ≤ 200 ms · responsiveness'), ('stability', 'CLS ≤ 0.1 · visual stability'),
               ('seventy', 'judged at p75 of real visits')]),
     "Question one. Name the three Core Web Vitals, and their good thresholds. [[3]] Answer: LCP within two point five seconds, for loading. INP within two hundred milliseconds, for responsiveness. CLS at or below zero point one, for visual stability. All judged at the seventy fifth percentile of real visits."),
    (scene_iq(2, 'Lighthouse gives you 98, but field data shows a poor INP. Why?',
              [('interactions', 'Lab run has no real interactions'), ('proxy', 'TBT is only a proxy for INP'), ('phones', 'Real users: slow phones, busy pages'),
               ('window', 'Field data = 28-day window')]),
     "Question two. Lighthouse gives you ninety eight, but field data shows a poor INP. Why? [[3]] Answer: a lab run has no real interactions, and TBT is only a proxy. Real users click on slow phones, deep into busy pages. And field data is a twenty eight day window."),
    (scene_iq(3, 'LCP is 4 s, but the hero image downloads in 300 ms. Where is the time going?',
              [('TTFB', 'TTFB: slow server response'), ('late', 'Load delay: image found late'), ('preload', 'Fix → in the HTML + preload / fetchpriority'),
               ('render', 'Render delay: blocking CSS + JS')]),
     "Question three. LCP is four seconds, but the hero image downloads in three hundred milliseconds. Where is the time going? [[3]] Answer: check TTFB first. Then load delay: the image was found late, through CSS or JavaScript. Put it in the HTML, and preload it or raise its fetch priority. And check render delay from blocking CSS and scripts."),
    (scene_iq(4, 'A banner slides in from the top after load, and CLS spikes. How do you fix it?',
              [('reserve', 'Reserve its space up front (min-height)'), ('overlay', 'Or overlay it: position fixed'), ('transform', 'Animate with transform, not top / height'),
               ('half', 'Shifts < 500 ms after a tap are excluded')]),
     "Question four. A banner slides in from the top after load, and CLS spikes. How do you fix it? [[3]] Answer: reserve its space up front, or overlay it with position fixed so nothing moves. Animate it with transform, not top or height. And if it opens on a tap, shifts within half a second are excluded anyway."),
    (scene_next('S3 · E09', 'CRITICAL RENDERING PATH', 'what blocks the first paint', 'critical', 'blocks'),
     "Got all four? Tell me your score below. Next: the critical rendering path, and what really blocks your first paint. Comment NOTES for the cheat sheet."),
]
