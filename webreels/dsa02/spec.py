# Sources (checked 2026-11-23):
# Amazon reports: Glassdoor Amazon interview question (16 Feb 2025) https://www.glassdoor.sg/Interview/Problem-Longest-Substring-Without-Repeating-Characters-QTN_7989487.htm
#                 Glassdoor Amazon interview question (6 Sep 2025) https://clear.glassdoor.nl/Interview/I-was-asked-was-to-implement-an-algorithm-to-find-the-longest-substring-without-repeating-characters-QTN_8492928.htm
#                 Naukri Code360 Amazon SDE experience (Jan 2022) https://www.naukri.com/code360/interview-experiences/amazon/interview-experience-jan-2022-exp-0-2-years-2-3014
# Also reported: Google SDE India (Aug 2025, Taro), Flipkart SDE-1 (Aug 2025, Taro)
# Salary: Amazon SDE-1 India ~Rs 27-30 LPA total comp (AmbitionBox via upGrad, Apr 2026; Levels.fyi median ~Rs 27-32 LPA)
EP = dict(id='DSA02', tag='DSA', short='Amazon sliding window', tail=1.0, bpm=108, drop_scenes=(4,),
          caption='sample v2, not for posting')
NARRATION = ['Want a 28 lakh job at Amazon? This exact question keeps showing up in their interviews.', 'Here it is: find the longest part of a string with no repeated letter.', 'Take "chaichai". The answer is four. C, H, A, I.', "Most people try every possible part. On a long string, that's millions of checks. Rejected.", 'The trick? A sliding window. Two pointers: left, and right.', 'Right moves forward, adding one letter at a time. C, H, A, I. A window of four.', 'Next letter is C again. Repeat! So left jumps just past the old C.', 'Keep a map of where each letter was last seen, so that jump is instant.', "Every letter is touched only once. That's O of n.", "Comment NOTES, and I'll send you five more questions with this exact pattern."]
