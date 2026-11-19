EP = dict(id='WR08', tag='SYSTEMS', short='Netflix deleted React and got faster', tail=1.2, bpm=116, drop_scenes=(7,),
          caption=("Netflix removed React from its landing page… and got 50% faster. 🍿\n\n"
                   "In 2017 Netflix kept React on the server to build the logged-out homepage, but swapped client-side React (and libraries like Lodash) for plain JavaScript. "
                   "~200 KB less JS, time-to-interactive cut by over 50%. Then it prefetched React for the next sign-up steps while you read.\n\n"
                   "SSR, hydration and islands explained in Season 2 on my page.\n"
                   "Full system design series on my page.\n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "Netflix made its homepage fifty percent faster. By throwing code away.",
    "Here's the problem. The sign-up page showed up fast. But the button didn't work yet.",
    "Because that page was just a picture. To make it clickable, your browser had to download React, and run it.",
    "That step is called hydration. Like adding water to bring it to life.",
    "But this page had one job. Type your email. Press a button.",
    "So Netflix asked: why load all of React for one button?",
    "They wrote that part in plain JavaScript. Two hundred kilobytes, gone.",
    "The button started working in half the time.",
    "And React? It loaded quietly in the background, ready for the next page.",
    "The lesson: don't ship a whole engine for one button.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
