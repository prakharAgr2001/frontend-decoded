# Series bible

## Look
- 1080×1920, 30 fps. Paper background `#F4F1EA` with grain + vignette. Ink `#16181D`, highlight yellow `#FFD23F`, alert red `#E63946`, dark cards `#111418`.
- Fonts: Oswald Bold (titles, stamps), Inter / Inter Display (body, captions), JetBrains Mono (code). All OFL, in `fonts/`.
- Signature moves: highlighter swipe behind titles, hard ink drop-shadow cards, rotated rubber stamps, self-drawing arrows, packets moving along links, slow 3% camera push per scene.
- Chrome: top-left episode pill (`S1 · E05`) + short title, top-right `FRONTEND DECODED`, yellow progress bar at bottom.
- Captions: white pill at y≈1490, 2–4 words, active word on yellow. Keep content between y 260 and 1380 (Instagram UI covers the rest).
- Oswald has no arrow glyphs: never put `→ ∝ ✓` inside `stamp()`/`title()`; Inter has `→`.

## Voice
Speko · google-tts · `Charon` (deep, neutral English documentary narrator). ~150 wpm. Spell out acronyms and camelCase in the TTS instructions.

## Teaching rules (every concept episode)
1. Hook on a real website moment, never a definition.
2. One concept per episode.
3. Plain-English definition on first use of any term.
4. Order: Hook → Problem → Analogy → How it works → Real-site proof (DevTools) → Interview trap/question → Try it (optional) → Next + "Comment NOTES".
5. 🔍 claims must be visible in DevTools/UI; 💡 illustrations never claim a company's internals.
6. The interview beat is a *real* gotcha (the one people actually get wrong), not a strawman.
7. Code on screen ≤ 10 lines, real working JS.

## Episode types
- Concept: 6–9 scenes, 70–100 s.
- IQ (`scene_iq_intro` + 4× `scene_iq` + `scene_next`): question → `[[3]]` pause with countdown ring → answer card.
- Finale: one journey through a real site, `chapter()` pills referencing each episode, season map, next-season card.
