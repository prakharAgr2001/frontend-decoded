EP = dict(id='WR09', tag='SYSTEMS', short='The page that jumps under your thumb', tail=1.2, bpm=116, drop_scenes=(6,),
          caption=("You tap a link. The page jumps. You hit an ad. 😤\n\n"
                   "Yahoo! JAPAN News (22B+ page views a month) found its article pages jumping as late images pushed text down. "
                   "The fix: reserve each image's space before it loads. Layout shift went from ~0.2 to ~0, and pages per session rose 15%, sessions got 13% longer (web.dev case study).\n\n"
                   "Layout shift (CLS) explained in S3E04 on my page.\n"
                   "Full system design series on my page.\n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "You go to tap a link. The page jumps. And you tap an ad instead.",
    "That jump has a name. Layout shift. And Google measures it.",
    "Yahoo Japan News gets over twenty-two billion page views a month. And its pages were jumping.",
    "The culprit? Images that loaded late, and shoved the text down.",
    "The fix was almost boring. Save the image's space before it loads.",
    "The jumping dropped to almost zero.",
    "And people read fifteen percent more pages per visit. Sessions got thirteen percent longer.",
    "Google calls it Cumulative Layout Shift. One of the three Core Web Vitals.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
