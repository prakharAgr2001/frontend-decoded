EP = dict(id='WR01', tag='SYSTEMS', short='The number that almost broke YouTube', tail=1.2, bpm=112, drop_scenes=(5,),
          caption=("This number almost broke YouTube. 🤯\n\n"
                   "In 2014 one K-pop video hit 2,147,483,647 views, the biggest number its 32-bit view counter could hold. "
                   "One more view and it would have flipped to −2,147,483,648. Engineers saw it coming and moved to 64 bits (limit: ~9.2 quintillion). "
                   "Then they hid an easter egg that spun the counter negative anyway.\n\n"
                   "Full system design series on my page. \n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "This number almost broke YouTube.",
    "2014. One K-pop video is racing toward two billion views.",
    "But YouTube's counter has a hard ceiling.",
    "Two billion, one hundred forty-seven million. Not one view more.",
    "One more view, and it wouldn't go up. It would flip.",
    "To minus two billion.",
    "Why? Views were stored in 32 bits. And that's the biggest number 32 bits can hold.",
    "So engineers rebuilt it in 64 bits. New ceiling? Nine quintillion.",
    "And then they trolled us. Hover over the counter, and it spun negative anyway.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
