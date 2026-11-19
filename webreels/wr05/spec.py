EP = dict(id='WR05', tag='SYSTEMS', short='One setting broke the internet', tail=1.2, bpm=114, drop_scenes=(6,),
          caption=("One customer changed one setting. Huge parts of the internet went down. 🌐💥\n\n"
                   "On 8 June 2021, Amazon, Reddit, the New York Times and gov.uk all showed errors. They shared one CDN: Fastly. "
                   "A bug shipped in May lay dormant until a customer pushed a perfectly valid config change, and 85% of Fastly's network returned errors. "
                   "Spotted in 1 minute, 95% back in 49.\n\n"
                   "CDNs explained in S1E06 on my page.\n"
                   "Full system design series on my page.\n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "One person changed one setting. And huge parts of the internet went down.",
    "June 2021. Amazon. Reddit. The New York Times. The UK government. All showing the same error.",
    "They all used the same company. Fastly. A CDN.",
    "A CDN keeps copies of websites on servers near you, so pages load fast.",
    "But in May, Fastly shipped a hidden bug. It just sat there. Waiting.",
    "On June eighth, one customer pushed a perfectly normal settings change.",
    "Boom. Eighty-five percent of Fastly's network started returning errors.",
    "They caught it in one minute. Most of it was back in forty-nine.",
    "The lesson? When everyone shares one CDN, one bug is everyone's bug.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
