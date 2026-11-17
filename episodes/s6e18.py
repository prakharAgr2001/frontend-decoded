from engine.lib import *

EP = dict(id='S6E18', tag='S6 · E18', short='IQ: COLLABORATION')

SCENES = [
    (scene_iq_intro('PRESENCE & COLLABORATION'),
     "Four interview questions on presence and collaboration. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Design "typing…" for a group of 200. What do you send, and how often?',
              [('throttle', 'Throttle: about one event every 3 s'), ('viewing', 'Fan out only to members viewing the chat'),
               ('expires', 'Auto-expires after a few silent seconds'), ('database', 'Never written to the database')]),
     "Question one. Design a typing indicator for a group of two hundred people. What do you send, and how often? [[3]] Answer: throttle typing events to about one every three seconds. The server fans them out only to members viewing that chat. The indicator expires on its own after a few silent seconds. And none of it is written to the database."),
    (scene_iq(2, 'Two admins edit the same profile form at once. How do you stop lost updates without locks?',
              [('started', 'Send the version you started from (ETag)'), ('header', 'PUT with an If-Match header'),
               ('rejects', 'Mismatch: server rejects with 412'), ('merge', 'Show the conflict, or merge fields')]),
     "Question two. Two admins edit the same profile form at once. How do you stop lost updates, without locks? [[3]] Answer: send the version you started from, as an E tag, in an If-Match header. If someone saved first, the server rejects it with a four twelve. Then show the conflict, or merge field by field."),
    (scene_iq(3, 'Text is "cat". A inserts "h" at 1, while B deletes position 2. What is the right result, and how does OT get it?',
              [('cha', 'Result: "cha"'), ('shifts', "A's insert shifts everything right"), ('three', "B's delete @2 becomes delete @3")]),
     "Question three. The text is cat. A inserts h at position one, while B deletes position two. What's the right result, and how does OT get there? [[3]] Answer: cha. A's insert came first, and it shifts everything after it to the right. So the server transforms B's delete, from position two, to position three."),
    (scene_iq(4, 'OT or CRDT for an offline-first notes app with no central server?',
              [('any', 'CRDT: merges in any order, no server'), ('library', 'Use a library: Yjs or Automerge'), ('tombstones', 'Cost: metadata + tombstones')]),
     "Question four. OT or CRDT, for an offline first notes app, with no central server? [[3]] Answer: a CRDT. Edits merge in any order, on any device, with no server in the middle. Use a library like Yjs or Automerge. The cost is extra metadata, and tombstones for deleted text."),
    (scene_next('S6 · E19', 'THE FINALE', 'one chat app, end to end', 'finale', 'chat'),
     "Got all four? Tell me your score below. Next: the finale. One chat app, built end to end. Comment NOTES for the cheat sheet."),
]
