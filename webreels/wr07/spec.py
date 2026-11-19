EP = dict(id='WR07', tag='SYSTEMS', short='Pinterest made you wait 23 seconds', tail=1.2, bpm=116, drop_scenes=(5,),
          caption=("23 seconds before you could tap anything. 🥶\n\n"
                   "Pinterest's old mobile site (average Android, slow 3G) took 23 s to become interactive: over 2.5 MB of JavaScript to parse first. "
                   "The 2017 rebuild split the code and shipped only what each page needed: core JS ~620 KB → 150 KB, time to interactive 23 s → 5.6 s. "
                   "Time spent +40%, user-generated ad revenue +44%.\n\n"
                   "Code splitting explained in S3E12–S3E15 on my page.\n"
                   "Full system design series on my page.\n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "Twenty-three seconds. That's how long Pinterest made you wait before you could tap anything.",
    "On a normal phone, on 3G, the page showed up. But it was frozen.",
    "Why? Pinterest sent over two megabytes of JavaScript. The phone had to chew through all of it before it could respond.",
    "So they rebuilt it. They split the code, and sent only what each page needed.",
    "The main bundle went from over six hundred kilobytes, down to one fifty.",
    "Twenty-three seconds became under six.",
    "Time spent went up forty percent. Ad revenue from users? Up forty-four.",
    "It's called code splitting. Ship only what the page needs.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
