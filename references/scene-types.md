# Scene types

The 10 principles from the tutorial (1–10), plus 5 measured extras (11–15). The numbers match the `Category:` line in every library `notes.md`. Examples are library notes in `references/library/` (media, if you have it, in your own study folder's `animations/`).

## Decision table

| When the script… | Use |
|---|---|
| Speaker introduces a new idea / category / story beat | 1 talking head |
| Speaker describes something concrete | 2 B-roll + text (or 3 painting if historical/philosophical) |
| Abstract emotion or state of mind | 7 center illustration |
| Two things side by side / comparison | 8 side illustration, or 11 dual rings / Step nodes |
| A list, framework, 'three parts', 'two steps' | 11 diagram |
| A study, a paper, a website, a DM | 13 screen capture / document |
| A personal history / biography / 'in 1988…' | 9 object + text (photos, timeline) |
| Numbers, growth, decline | 10 graph |
| Punchline, reversal, a quote, a question to the viewer | 6 text-centric |
| A big summary sentence with 2–3 key words | 4 line + text |
| Guiding the eye to an object or through phases | 5 line + illustrations |
| Quiet B-roll moment, text needs space | 12 inset |
| The last 5 s | 14 end card |

Mix targets (measured): B-roll ~40%, talking head ~16%, collage/object ~11%, illustration ~10%, text card ~9%, diagram ~8%, inset ~4%, screen/end card ~3%.

## 1. On-screen caption (talking head)

- **When:** Introducing an idea, personal lines, jokes, dialogue, anything where the face carries the emotion.
- **Composition:** Interview A-roll (dark or warm set). Caption at y≈0.53, chest/mic height, never over the face. Helpers Inter Medium ~40 px; key word Inter ExtraBold or Playfair Italic ~120 px. Variants: blue highlight pill behind a quoted line; tinted panel-slide exits.
- **Timing / motion:** Pops at onset +2 f, 1 f opacity step. Captions swap every 1–5 words; median hold 2.4 s per shot.
- **House standard:** the camera on the speaker is locked (no tracking drift; reframe only at cuts). Optional effects the user may ask for: a clean slow zoom-in over the beat (1.00→1.12, `sine.inOut`), soft black and white (`mono-fade`), a blue highlight box behind a bolder key word. See `house-standards.md` §1, §3, §4.
- **Library:** 64 examples
  - `V04-A01 Talking-head caption at chest height`: 3103 ms. Interview A-roll; small white sans caption builds at chest height, a serif key phrase lands once, then a negative-tinted image panel slides in from the right as the transition out.
  - `V04-A04 Caption swaps line, panel-slide out`: 1602 ms. A-roll; a small sans caption with one bold word builds, the line is replaced, then a negative-tinted panel slides in from the right.
  - `V04-A10 Bold word inside a sans caption`: 2002 ms. A-roll; a small sans caption with a single bold word builds at chest height, then the line swaps.
  - `V04-A13 Small caption swaps at chest height`: 1702 ms. A-roll with small white sans captions only, swapping as each phrase ends.
  - `V04-A14 Low-emphasis caption, one word grey`: 1568 ms. A-roll; a small sans caption builds with one word briefly ghosted before it lights up.
  - `V04-A15 Caption then yellow wash transition`: 2336 ms. A-roll caption builds word by word, then the frame floods to a yellow paper wash.
  - `V04-A17 Caption with a ghosted word`: 1735 ms. A-roll; the caption builds, with words appearing grey first then white.
  - `V04-A19 Caption then panel-slide out`: 1134 ms. A-roll caption builds, then a negative-tinted panel slides in from the right as the exit.

## 2. B-roll + text

- **When:** Describing what the speaker is talking about: literal or mood footage for the phrase.
- **Composition:** Desaturated, vignetted, lightly grained B-roll; text centered on the focal point (y≈0.50), white. Serif key word with tiny Inter helpers, or bold Inter key word. Archival = B&W.
- **Timing / motion:** ~1 s per shot; text pops at onset +3–7 f; the text block may carry across 2–4 shots while footage cuts underneath; slow push-in ≈1%/s.
- **House standard:** caption centered. "Dark, moody" variant: heavy darkening grade + bold Inter key word in the middle, small helpers above-left / below-right. Coming from the face, use the smooth zoom-through fade. See `house-standards.md` §4–5.
- **Library:** 81 examples
  - `V01-A03 Helpers first, serif key word drops into gap`: 934 ms. Warm close-up B-roll; small sans helpers pop at their final positions (one left, one right, a gap between), then the big serif key word pops into the reserved center gap.
  - `V01-A04 Text line carries across two B-roll shots`: 1835 ms. Helpers + serif key word build over a red silhouette shot; the footage hard-cuts to a sunset shot while the text block stays in place and the last word pops in below after the cut.
  - `V01-A05 Serif key word, helpers above-left and below-right`: 1001 ms. Dark office B-roll; tiny sans helper above-left, big white serif key word center, two small words pop below-right, all word by word.
  - `V01-A10 Top-down desk shot, serif key word pops`: 901 ms. Overhead B-roll of hands at a desk; small helpers build above, then a big serif key word with comma pops center.
  - `V01-A14 Halo figure into B-roll question run`: 6840 ms. Continues the halo-figure scene, then a fast run of B-roll shots each carrying one serif or bold key word, ending on a sunset shot with a bold sans key word.
  - `V01-A17 Single small label over B-roll`: 334 ms. Minimal subtitle treatment: one small white sans word centered over a muted book close-up, no key word.
  - `V01-A18 Small words build, serif key word lands`: 1101 ms. Dark backlit B-roll; four small sans words build in a row, then a large serif key word lands underneath.
  - `V01-A20 Serif word swap across two shots`: 2503 ms. Serif key word over a window-light shot, hard cut to a dark hand close-up where a new serif key word takes the same center position with a small helper below.

## 3. Paintings animation

- **When:** Philosophical, historical or 'ancient wisdom' beats.
- **Composition:** Classical painting, fresco or statue with paint + rough-paper texture; cinematic text beside the main subject; optional framed fresco cutout on white paper.
- **Timing / motion:** Quick camera slide-in (8–15 f, power2.out); fast montage of 3–4 artworks, each with one serif key phrase.
- **House standard (every painting):** paint texture filter (Kuwahara + grain + vignette + slight desaturation) + two-layer rough paper texture + quick slide-in reveal + captions **centered and stacked** (small line above, serif key word below), never over the subject's face. Exact values in `house-standards.md` §2.
- **Library:** 2 examples
  - `V02-A24 Ancient art montage into framed fresco`: 2333 ms. Fast montage of statues, frescoes and Egyptian paintings each with a serif key phrase, ending on white paper with the phrase above a framed fresco cutout.
  - `V02-A25 Engraving cutouts slide in on deep blue`: 1667 ms. Deep blue gradient; two tilted engraving cutouts slide in from the right and settle while a serif key word with a small helper builds beside them.

## 4. Line + text

- **When:** A big thesis line whose key words should feel connected.
- **Composition:** White or black paper; thick accent-blue stroke (≈80 px) drawn along a curve; a key word interrupts the line, which continues to the next word.
- **Timing / motion:** Line draws 12–20 f power2.out; camera follows the line head; each word pops when the line reaches it.
- **House standard:** the line (≈64 px blue) leads up to each piece of text, is interrupted by it and continues; the camera tracks the line so each new word lands in the lower-middle; black serif key words on rough white paper. See `house-standards.md` §5.
- **Library:** 3 examples
  - `V02-A23 Blue arc line leads into the word`: 3833 ms. White paper; a thick blue arc draws in from the edge and stops at a serif key word, then continues down the frame and leads to a small brain illustration.
  - `V02-A40 Thick blue arc swings into the text`: 2100 ms. White paper; a thick blue arc sweeps in from the left edge, the camera follows it, and it ends pointing at a serif key word that builds with helpers below.
  - `V03-A12 Thick blue line weaves between words`: 3600 ms. White paper; a thick blue line enters from above, stops at a serif word, swings past it, continues to the next word, and the camera follows its path.

## 5. Line + illustrations

- **When:** Leading the eye to an object, or a multi-step progression.
- **Composition:** Thin glowing line with a white anchor dot above an illustration; zigzag line with alternating objects; or a direct lead-in to the subject; construction lines linking images.
- **Timing / motion:** Camera pans along the line; objects pop as the line reaches them (6–11 f).
- **Library:** 1 examples
  - `V03-A19 Thin guide lines link fetus, brain and evolution`: 4500 ms. White paper with thin grey construction lines; a fetus engraving with a serif key phrase, a red-centered brain/nerve illustration with "danger.", then a line of evolution figures under a serif key word: the camera slides along the lines between them.

## 6. Text-centric

- **When:** Punchlines, reversals ('But that's wrong.'), quotes, the ending.
- **Composition:** White, rough-white or blue paper; big curly quotes optional; one lockup dead center; ghost-line variant common; tiny-line-alone variant on blue.
- **Timing / motion:** Ghost or pre-placed words snap on at onset +3–5 f; 0.6–2 s; exits on the cut.
- **Library:** 25 examples
  - `V01-A02 Ghost line karaoke on blue paper`: 1668 ms. The whole line is pre-set at ~15% white on blue paper; each word snaps to 100% as it is spoken, small sans helpers first, the bold sans key word last.
  - `V01-A09 Ghost text on white, blue sans lights up`: 834 ms. White paper card; the short line sits as a faint ghost, then the blue bold sans words light up in sync with the voice.
  - `V01-A19 Hard cut to blue card, ghost sans text`: 2002 ms. B&W portrait B-roll with small sans words, then a hard cut to blue paper where the next words sit as ghosts and light up white.
  - `V01-A21 Ghost sans line lights up on white`: 901 ms. White paper; a short blue bold sans line is pre-set as a faint ghost and each word snaps to full blue on its spoken word, left to right.
  - `V01-A26 Ghost serif line on white, words light blue`: 1401 ms. White paper; the whole two-level layout (tiny sans helpers above, blue serif key words, small word below) sits as a ghost and lights up word by word.
  - `V01-A38 Tiny ghost line on blue lights up`: 1168 ms. Blue paper; a single tiny sans line sits as a ghost and lights up white word by word, bold on the key word only.
  - `V01-A42 Ghost line then hard swap to one word`: 1001 ms. Blue paper; a tiny ghost line lights up, then is replaced by a single bold sans key word with comma, center.
  - `V02-A06 Tiny sans line, then serif key word on blue`: 1667 ms. Lighter blue paper; tiny sans words build one by one, then the big white serif key word lands with the helpers tucked on top of it.

## 7. Center illustration

- **When:** Showing the main idea as an image: a person, a state of mind, a brain.
- **Composition:** Rough painted blue figure (or black silhouette, X-ray head, brain, concentric rings, glowing disc) occupying the lower half on white/blue/black paper; text in the top third.
- **Timing / motion:** Entrance 15–30 f power2.out (scale-up from small, rise from the bottom, light reveal); sometimes a slow pull-out; serif key words swap above as each is spoken.
- **Library:** 25 examples
  - `V01-A01 Puzzle-head illustration, serif title builds`: 2002 ms. White paper with a blue puzzle-piece head illustration filling the lower half; sans helpers "You can't solve a" build word by word top-left, then the line swaps to a blue serif key word with a small sans word tucked under it.
  - `V01-A11 Figure on blue mountain with concentric rings`: 2736 ms. Camera pushes from a tiny figure into a blue painted figure seated on a blue mountain, thin concentric rings around the head; serif key word builds above with small helpers underneath.
  - `V01-A12 Glowing figure rises out of black`: 267 ms. Pure black frame; a glowing white disc with a blue figure rises in from the bottom edge, a light-reveal bridge into the next scene.
  - `V01-A13 Backlit figure with halo ring, question builds`: 2736 ms. Blue figure silhouette against a glowing white disc ringed by a thin circle with tick marks; small sans question builds, then the big serif key phrase lands.
  - `V01-A24 Brain lifts out of head illustration`: 4171 ms. Blue line-art head on white; the brain rises out of the open skull, serif key words swap above, then the camera pulls back to a small engraved brain with a serif key word above it.
  - `V02-A01 Head opens, blue paint fills profile`: 2933 ms. A blue dot opens into a black head illustration with a red brain on blue; serif key word with helper below, then cut to a painted profile with a blue brain where serif words build on top.
  - `V02-A22 Brain scan with block-glitch text`: 3233 ms. X-ray/brain scan illustrations on white with serif key words; black redaction-style bars glitch across the frame between beats.
  - `V02-A31 Meditating figure in rings with blue glow`: 2667 ms. White paper; a dark meditating figure with a soft blue glow and concentric rings with arrows; serif key words swap at the top as each is spoken.

## 8. Side illustration + text

- **When:** Two elements at once, a comparison, or a figure plus a statement.
- **Composition:** Figure or half-circle on one flank, text on the other; optional text rotating around the shape; cloth texture fill.
- **Timing / motion:** Entrance 15–20 f power2.out; balanced composition.
- **Library:** 1 examples
  - `V01-A07 Diagonal blue wipe reveals drawn figure`: 1568 ms. Blue panel wipes away on a diagonal to reveal a hand-drawn line figure on white/blue split; small sans helper plus serif key word set top-left of the figure; ends on a hard cut to a big avatar circle.

## 9. Object + text

- **When:** Personal history, biography, evidence: photos, objects, timelines.
- **Composition:** Photo cutouts with white borders + soft shadow, tilted 5–25°, stacked; thin timeline with year ticks and labels; blue label tags; circle highlight around a face.
- **Timing / motion:** Fly in from off-frame and settle 17–30 f power2.out, staggered ~10 f; timeline slides power2.inOut; camera drifts or pulls back; background may wash white → blue.
- **House standard:** object callout = one photo/object on rough paper revealed with a rough-edged wipe, serif labels with thin callout lines pointing at it, caption centered. A single photo card sits straight and centered with the caption centered above. See `house-standards.md` §5.
- **Library:** 23 examples
  - `V01-A30 Text pulls back, photo cutouts fly in tilted`: 3670 ms. White paper; ghost blue sans line lights up word by word, the camera pulls back and drifts, then three tilted photo cutouts fly in from the corners and settle while blue serif key words light up above.
  - `V01-A31 Background swaps to blue under the same photo stack`: 1902 ms. Same three-photo stack, now on blue paper; serif heading on top, then a long line of small sans helpers builds under it word by word.
  - `V02-A12 Photo stack on timeline, blue wash, paper flies in`: 1733 ms. White paper; three photo cutouts pop around a year tick on a thin blue timeline, the frame washes to blue in steps over ~10 frames while sliding left, and a document flies in rotated.
  - `V02-A20 Evolution engraving, camera slides across`: 2500 ms. Tilted vintage evolution-chart print; serif key words build over it while the camera slides across the figures, ending on a cut to a small inset clip.
  - `V02-A32 Photo cutouts stack up on blue`: 7000 ms. Blue paper; tilted photo cutouts of the speaker drop in one by one into a loose stack while serif key words and small helpers appear above and below.
  - `V02-A34 Line builds then photo collage drops in`: 3000 ms. Blue paper; a small sans line builds center word by word, then a tilted stack of photos drops in with a small caption at the bottom.
  - `V03-A27 Buddha photo on a timeline into B&W insets`: 3233 ms. White paper; a pale disc and a small statue photo sit on a thin timeline with a serif heading, then a hard cut to tall rounded B&W insets on black with serif key words.
  - `V03-A29 Brain scan headline on deep blue, then dims`: 2067 ms. Deep blue glow; a large realistic brain with a serif-over-bold headline and a tiny paragraph, small skull icons at the top; the scene dims to black.

## 10. Graphs + statistics

- **When:** Numbers, trajectories, trends.
- **Composition:** Flat dark textured background, thin glowing white grid, white trace, blue ball at the head.
- **Timing / motion:** Camera follows the ball; the line can step once per repeated word ('up… up… up…').
- **Library:** 0 examples
  - Not present in these 6 reels. The recipe comes from the tutorial doc; build it from `shapes/graph-grid.svg`.

## 11. Diagram / motion graphic

- **When:** Frameworks, lists, science, systems (three parts, two steps, overlaps).
- **Composition:** Soft radial blue glow on white or blue; thin 1–2 px rings with a travelling dot; solid blue triangle / Venn center / Step nodes / dual glowing rings; small Inter labels or Playfair Italic labels with hand-drawn arrows.
- **Timing / motion:** Each part builds on its spoken word: 6–17 f power2.out; labels pop 1–2 f; holds 3–9 s; graphics often on twos.
- **Library:** 21 examples
  - `V01-A08 Avatar orbit with icons circling`: 4104 ms. Big white avatar circle on blue shrinks into a small avatar inside dashed orbit rings; small icons travel the orbits while serif phrases swap above it one at a time.
  - `V01-A15 Blue glow bloom with orbiting dot`: 1502 ms. White paper; a soft radial blue glow blooms center while a small dot travels a thin circle path; small sans helper above a blue serif key word.
  - `V01-A16 Dot falls, becomes triangle, labels pop`: 7407 ms. A blue dot travels diagonally into the center and shrinks, morphs into a solid blue triangle; three sans labels pop at the vertices one by one as each concept is named.
  - `V01-A35 Glowing brain with orbit labels`: 5005 ms. White paper with a soft blue glow around a realistic brain; a serif key word with small helpers sits above, then small labels appear on a thin orbit ring around the brain.
  - `V02-A10 Brain blueprint splits into two halves`: 3000 ms. Line-art brain on blue with a thin frame; sans labels build above, then a white panel wipes in from the left over half the frame, splitting the brain diagram into two systems with tiny labels.
  - `V02-A16 Blue grid chart builds, bars grow`: 7067 ms. White paper; a blue square splits into a 2x2 grid, axis labels pop left and top, then small blue bars step out of the grid edges.
  - `V02-A19 Blue dot grows into a labeled dial`: 4900 ms. White paper; a small blue circle labeled in sans grows a soft halo ring, serif key words above, then a large serif word wraps around the dial while tiny helpers build overhead.
  - `V02-A27 Brain with red half, network lines`: 3267 ms. Sunset silhouettes carry the quote, then a cut to blue paper with a realistic brain beside a white half-disc; the brain turns red and thin network lines with dots spread around it.

## 12. B-roll inset

- **When:** Quieter B-roll moments, or when the text needs space above.
- **Composition:** Rounded clip (16–24 px radius, ~85% width; tall variant ~64%) centered on black; small text above at y≈0.39.
- **Timing / motion:** Inset pops in 6–12 f; the footage may swap under persistent text.
- **Library:** 8 examples
  - `V01-A06 Inset clip swaps under persistent text`: 1001 ms. Rounded-corner B-roll inset centered on black; small sans helpers above, serif key words build; the inset footage changes mid-line while the text keeps building.
  - `V02-A17 Inset clip with tiny caption building`: 933 ms. Rounded B-roll inset on black; a tiny sans caption builds word by word above it and the inset footage changes mid-line.
  - `V02-A21 Serif key word over swapping inset clips`: 1267 ms. Big serif key word fixed at the top third on black while rounded inset clips swap underneath it.
  - `V03-A21 Small caption over sunlit inset`: 1000 ms. Rounded sunset inset on black; a tiny sans caption builds above it in two steps.
  - `V03-A31 Tall inset with bold sans key word`: 1933 ms. Tall rounded B-roll inset on black; small helpers build, the inset footage changes, then a bold sans key word with comma lands center.
  - `V03-A35 Small inset with tiny caption`: 2167 ms. Small rounded inset on black; a tiny sans caption builds above it word by word.
  - `V05-A21 Small inset clips swap, serif key phrase`: 1933 ms. Small rounded insets on black swap footage; small captions above, then a serif italic key phrase lands over the inset top edge.
  - `V05-A41 Tall inset run with serif key words`: 3233 ms. Tall rounded insets on black swap footage every few frames while serif italic key phrases build over them.

## 13. Screen capture / document

- **When:** Citing a study, a website, a profile, a DM.
- **Composition:** Research paper with dog-eared corner on blue; full-frame page capture; social profile; chat bubble.
- **Timing / motion:** Paper flips/flies in rotated and lands flat (2–20 f), then a slow push-in to the title; highlight bars wipe across key lines; bubbles type on.
- **Library:** 11 examples
  - `V02-A13 Research paper lands flat on blue`: 433 ms. A white research document with a dog-eared corner settles flat in the center of blue paper and holds still.
  - `V02-A14 Slow zoom into paper title`: 567 ms. Screen capture of a document page; a slow push-in toward the paper's title and author block.
  - `V02-A15 Big serif acronym over the paper`: 2600 ms. Blue paper; a large white serif title in curly quotes sits above the centered document while a tiny subtitle line builds underneath.
  - `V03-A46 Website capture with blue serif heading`: 2733 ms. A light-grey website capture with three small columns; a blue serif heading builds on top word by word with a tiny helper.
  - `V05-A07 Profile page capture with caption`: 767 ms. A dark social-profile screen capture with slight drift; a small sans caption builds center.
  - `V05-A08 Profile scrolls, serif key word lands`: 1600 ms. The profile capture scrolls up while a serif italic key phrase builds over it.
  - `V05-A11 DM bubble types out on a profile`: 5067 ms. A-roll with a bold key word, then a cut to a dark message screen where a blue chat bubble grows as the question text types out.
  - `V06-A03 Cyan flash, paper flips in on blue`: 876 ms. Library shot with a serif key word, a cyan flash frame, then on blue paper a document flips in rotated in 3D and lands flat.

## 14. End card / CTA

- **When:** The last 3–5 s.
- **Composition:** Blue or white paper; serif 'Comment "KEYWORD"' line with a tiny sub-line, or a website with a rounded photo card.
- **Timing / motion:** Build word by word, URL can type letter by letter; hold ≈5 s.
- **Library:** 6 examples
  - `V01-A44 End card -  blue serif line then photo slides up`: 1502 ms. White end card; blue serif call-to-action words build center, then a rounded photo card slides up over the text and sharpens.
  - `V01-A45 End card -  caption builds over photo`: 1502 ms. White end card with a rounded property photo; small sans caption builds above the photo word by word.
  - `V01-A46 End card -  URL types on letter by letter`: 2302 ms. White end card; a blue bold sans web address types on letter by letter above the rounded photo.
  - `V02-A45 Fast serif line on blue before the CTA`: 2133 ms. Blue paper; a small serif key phrase with tiny helpers builds fast, then a tiny two-word line replaces it.
  - `V02-A46 Comment CTA end card on blue`: 3700 ms. Blue paper end card; a serif "Comment" line with the keyword in quotes and a tiny sans line below, held for several seconds.
  - `V05-A65 Thank-you sign-off on A-roll`: 1200 ms. Wide A-roll; a bold sans key phrase builds at chest height with a tiny line below, held as the sign-off.

## 15. Transition

- **When:** Between beats, never on its own.
- **Composition:** Glitch smear, pixel mosaic, slide-out whip, invert/white/cyan flash, dip to black, panel slide, blank beat.
- **Timing / motion:** 1–6 f; always hand off with a hard cut.
- **Library:** 9 examples
  - `V02-A02 Pixel-smear glitch into B-roll`: 833 ms. Painted profile with serif text; a 5-frame desaturated pixel-smear glitch tears the frame, then a hard cut to a field B-roll where a serif key word appears.
  - `V02-A03 Glitch transition, isolated`: 167 ms. The isolated glitch: frame desaturates to grey, a pixel-smear displacement drags the image sideways for ~5 frames, then cut.
  - `V02-A08 Iris-in fade to black on eye close-up`: 167 ms. B&W eye close-up; a single small word appears in the pupil, then the frame dips fully to black for 2-3 frames.
  - `V02-A09 Eye close-up dips to black between words`: 233 ms. Second B&W eye shot; a small two-word line sits in the iris, then a quick dip to black closes the beat.
  - `V03-A02 Slide-out whip into white scene`: 733 ms. The blue title scene accelerates left (ease-in, ~3 frames) and hard-cuts to white paper with a seated silhouette on a rough hill, a blue serif word appearing top center.
  - `V03-A10 Invert-flash between white and black frames`: 333 ms. 1-frame color invert flashes alternate between a black figure on white and a white glowing figure on black: a strobe transition.
  - `V03-A18 Pixel-mosaic glitch with ghost figure`: 500 ms. Black-and-white blocky pixel-mosaic glitch frames flicker around a dissolving figure before settling on black with a small caption.
  - `V03-A40 White flash then black beat`: 167 ms. A short transition: two frames of pure white then black, a flash-and-blank beat between scenes.
