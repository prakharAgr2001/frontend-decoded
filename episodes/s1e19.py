from engine.lib import *

EP = dict(id='S1E19', tag='S1 · E19', short='IQ: PREDICT THE OUTPUT')

SCENES = [
    (scene_iq_intro('PREDICT THE OUTPUT', '4 puzzles · pause and predict before the reveal'),
     "Four event loop puzzles from real interviews. Read the code, pause, and predict the output before the reveal."),
    (scene_iq(1, 'What does this print?',
              ['A → C → B', ('Synchronous', 'sync code runs first'), ('waits', 'the timer callback waits in the task queue')],
              code_lines=["console.log('A');", "setTimeout(() => console.log('B'), 0);", "console.log('C');"]),
     "Question one. What does this print? [[4]] Answer: A, C, B. Synchronous code runs first. The timer callback waits in the task queue."),
    (scene_iq(2, 'What does this print?',
              ['1 → 4 → 3 → 2', ('microtask', 'promise callback = microtask'), ('before', 'microtasks run before the next task')],
              code_lines=["console.log(1);", "setTimeout(() => console.log(2));", "Promise.resolve().then(() => console.log(3));", "console.log(4);"]),
     "Question two. What does this print? [[4]] Answer: one, four, three, two. The promise callback is a microtask, so it runs before the timer's task."),
    (scene_iq(3, 'What does this print?',
              ["p1 → p2 → t", ('added', 'microtasks added during the drain…'), ('still', '…still run before the next task')],
              code_lines=["setTimeout(() => console.log('t'));", "Promise.resolve().then(() => {", "  console.log('p1');",
                          "  Promise.resolve().then(() => console.log('p2'));", "});"]),
     "Question three. What does this print? [[4]] Answer: p one, p two, then t. Microtasks added while the queue is draining still run before the next task."),
    (scene_iq(4, 'What does this print?',
              ["in → out → after", ('before', 'code before the first await runs synchronously'), ('resumes', 'the rest resumes as a microtask')],
              code_lines=["async function f() {", "  console.log('in');", "  await null;", "  console.log('after');", "}", "f(); console.log('out');"]),
     "Question four. What does this print? [[4]] Answer: in, out, after. Code before the first await runs synchronously. Everything after it resumes as a microtask."),
    (scene_next('S1 · E20', 'BUBBLING', 'how events travel through the DOM', 'bubbling', 'travel'),
     "How many did you get? Tell me below. Next: event bubbling and capturing, how events travel through the DOM. Comment NOTES for the cheat sheet."),
]
