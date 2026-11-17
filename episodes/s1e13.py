from engine.lib import *

EP = dict(id='S1E13', tag='S1 · E13', short='IQ: RENDERING')

SCENES = [
    (scene_iq_intro('THE RENDERING PIPELINE'),
     "Four interview questions on how the browser turns code into pixels. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'What is the difference between the DOM and the HTML the server sent?',
              [('raw', 'HTML = raw text that arrived'), ('live', 'DOM = live tree built from it'), ('fixes', 'Browser fixes broken markup'),
               ('JavaScript', 'JavaScript keeps changing the DOM')]),
     "Question one. What's the difference between the DOM and the HTML the server sent? [[3]] Answer: the HTML is just the raw text that arrived. The DOM is the live tree the browser builds from it. The browser fixes broken markup, and JavaScript keeps changing the DOM, so the two can differ a lot."),
    (scene_iq(2, 'Walk me through the steps from the DOM and CSSOM to pixels.',
              [('render', '1 · Render tree (visible nodes only)'), ('layout', '2 · Layout: size + position of boxes'),
               ('Paint', '3 · Paint: fill in the pixels'), ('composite', '4 · Composite: GPU stacks the layers')]),
     "Question two. Walk me through the steps from the DOM and CSSOM to pixels. [[3]] Answer: build the render tree from visible nodes. Run layout to compute every box's size and position. Paint the pixels. Then composite the layers into the final frame."),
    (scene_iq(3, 'Why is animating transform smoother than animating left?',
              [('geometry', 'left changes geometry'), ('main', 'layout + paint every frame, main thread'),
               ('compositor', 'transform runs on the compositor'), ('GPU', 'GPU moves an existing layer')]),
     "Question three. Why is animating transform smoother than animating left? [[3]] Answer: left changes geometry, so every frame needs layout and paint on the main thread. Transform can run on the compositor, which just moves an existing layer on the GPU."),
    (scene_iq(4, 'What is layout thrashing, and how do you fix it?',
              [('Interleaving', 'Interleaving DOM reads and writes'), ('forces', 'every read forces a new layout'),
               ('Batch', 'Fix → batch reads, then writes'), ('requestAnimationFrame', 'Schedule writes with rAF')]),
     "Question four. What is layout thrashing, and how do you fix it? [[3]] Answer: interleaving DOM reads and writes, so every read forces a new layout. Batch all the reads, then all the writes, and schedule writes with requestAnimationFrame."),
    (scene_next('S1 · E14', 'EVENT LOOP', "JavaScript's one-chef kitchen", 'event', 'kitchen'),
     "Got all four? Tell me your score below. Next: the event loop, starting with JavaScript's one-chef kitchen. Comment NOTES for the cheat sheet."),
]
