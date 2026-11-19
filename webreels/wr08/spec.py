EP = dict(id='WR08', tag='SYSTEMS', short='Netflix deleted React and got faster', tail=1.2, bpm=116, drop_scenes=(6,),
          caption=("Netflix removed React from its landing page… and got 50% faster. 🍿\n\n"
                   "In 2017 Netflix kept React on the server to build the logged-out homepage, but swapped client-side React (and libraries like Lodash) for plain JavaScript. "
                   "~200 KB less JS, time-to-interactive cut by over 50%. Then it prefetched React for the next sign-up steps while you read.\n\n"
                   "SSR, hydration and islands explained in Season 2 on my page.\n"
                   "Full system design series on my page.\n💬 Comment NOTES for the cheat sheet."))
NARRATION = [
    "Netflix deleted React from its homepage. And it got fifty percent faster.",
    "Wait. Netflix is built with React. So what happened?",
    "The sign-up page looked ready. But your browser was still downloading React and running it, just to wake the page up.",
    "That wake-up step has a name. Hydration.",
    "So Netflix kept React on the server, to build the page. And in your browser? Plain JavaScript.",
    "Two hundred kilobytes of JavaScript. Gone.",
    "Time until you could click: cut in half.",
    "And while you read the page, it quietly prefetched React for the next step.",
    "The lesson: ship less JavaScript. Hydrate only what needs it.",
    "Want to understand systems like this? The full system design series is on my page. Follow.",
]
