from engine.lib import *

EP = dict(id='S5E09', tag='S5 · E09', short='IQ: PAGINATION', hook='4 pagination questions')

SCENES = [
    (scene_iq_intro('PAGINATION'),
     "Four interview questions on pagination. Pause the video, and answer each one before the reveal."),
    (scene_iq(1, 'Page two of a feed shows a post you already saw on page one. What is happening?',
              [('offset', 'Offset pagination'), ('shifted', 'New post on top → rows shifted by one'), ('cursor', 'Fix: cursor = "older than the last one"')]),
     "Question one. Page two of a feed shows a post you already saw on page one. What's happening? [[3]] Answer: it's offset pagination. A new post was added at the top, so everything shifted down by one. Switch to a cursor, like posts older than the last one you saw."),
    (scene_iq(2, 'Your cursor is the created_at timestamp, and some posts go missing. Why?',
              [('ties', 'Ties: posts share a timestamp'), ('skips', '"strictly less than" skips them'), ('both', 'Sort by (created_at, id) · cursor holds both')]),
     "Question two. Your cursor is the created at timestamp, and some posts go missing. Why? [[3]] Answer: ties. Several posts share the same timestamp, and the strictly less than condition skips them. Sort by timestamp and id, and put both in the cursor."),
    (scene_iq(3, 'Product wants users to jump straight to page 50 of search results. Cursor or offset?',
              ['Offset · cursors can’t jump', ('stable', 'Fine for fairly stable results'), ('cap', 'Cap the depth: deep offsets get slow')]),
     "Question three. Product wants users to jump straight to page fifty of search results. Cursor, or offset? [[3]] Answer: offset. Cursors can't jump. For fairly stable results, offset is fine. Just cap how deep users can go, because deep offsets get slow."),
    (scene_iq(4, 'How do you build infinite scroll without listening to the scroll event?',
              [('Intersection', 'IntersectionObserver on a sentinel'), ('margin', 'rootMargin → load before the bottom'), ('virtualization', 'Very long lists → virtualization')]),
     "Question four. How do you build infinite scroll without listening to the scroll event? [[3]] Answer: put an Intersection Observer on a sentinel element below the list. Give it a root margin, so the next page starts loading before the user hits the bottom. For very long lists, add virtualization."),
    (scene_next('S5 · E10', 'WATERFALLS', 'why your page loads one request at a time', 'waterfalls', 'time'),
     "Got all four? Tell me your score below. Next: request waterfalls, and why your page loads one request at a time. Comment NOTES for the cheat sheet."),
]
