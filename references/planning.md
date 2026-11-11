# Planning: story, scene plan, QA

## 1. Story structure (repeats across the reels)

| Beat | Time | What | Typical scenes |
|---|---|---|---|
| Hook | 0–5 s | A bold claim or "the biggest mistake…"; text on screen by frame 5 | Center illustration or text card first; never open on a plain talking head without text |
| Relatable problem | 5–25 s | Everyday struggle, "maybe that's you" | Fast B-roll run (~1 s per shot), one key word each |
| Science | 25–50 s | "Researchers confirmed…", a study or a mechanism | Photo cutouts on a timeline, paper fly-in, brain/diagram graphic held 3–9 s |
| Older wisdom | 50–65 s | "The ancients understood…", scripture, philosophy | Painting / statue montage, engraving cutouts, quote card |
| Practical change | 65–85 s | Step-1 / Step-2, a reframing question | Diagram nodes, quote card, talking head with highlight pill |
| Payoff + CTA | last 5–10 s | Restate the promise; "Comment ___ and I'll send you…" | Blue quote card → end card held ≈5 s |

For talking-head reels (04–06 style), the face carries 30–50% of the time. Cut away on every concrete noun or image.

## 2. From script to plan

1. **Get word timings.** Transcribe at word level. If there's no voice-over yet, estimate at 205 wpm (0.29 s per word) and re-time after recording.
2. **Phrase.** Split into 1–5-word units at natural sense breaks (often before *the / you / I / that / and*).
3. **Key word.** Mark one per unit. A function-word-only unit gets the subtitle style, with no key word.
4. **Scene type.** Use the decision table in `scene-types.md`. Group units that share one visual: a sentence across 2 B-roll shots, or a diagram across 3–6 units.
5. **Timing.**
   - Scene start = onset of its first word − 1 f.
   - Word pops = onset + 3 f (talking head + 2 f).
   - Diagrams hold until their last label has been on screen ≥1 s.
6. **Variety pass.**
   - No more than 4 B-roll shots in a row without a designed card.
   - Alternate blue, white and black backgrounds.
   - Bring back one motif (a figure, ring or line) 2–3 times.
7. **CTA.** The end card is the last 5 s; the comment keyword goes in quotes.

## 3. Plan-card format

Write each scene the way the breakdown cards read: header, shot-type tag, on-screen text with the key word in **bold**, and callouts for each element. Keep each scene about 1–2 s.

```
SCENE 07 / 58 · 0:09.4–0:10.6 (36 f) · B-ROLL
On-screen text: "to finally / **rest.**"      key = rest. (Playfair Italic 120 px), helpers Inter 40 px above-left
Voice: "…to finally rest."                    cut at onset("to") − 1 f; pops: to +3 f, finally +3 f, rest. +3 f
Visual: woman exhaling on a balcony at dusk (own footage: broll/balcony_03.mp4, 00:04–00:06)
Elements:  → cinematic text  → B-roll (desaturated −30%, vignette, grain)
Motion: push-in 1%/s; hard cut in, text exits on cut
Ref: V01-A05, V01-A22 (library)
```

For a whole video, a table also works:

| # | Time | Frames | Type | On-screen text (**key**) | Visual / asset | Motion | Ref |
|---|---|---|---|---|---|---|---|
| 1 | 0:00.0–0:01.9 | 57 | ILLUSTRATION | "the habit / **nobody** / talks about" | Blue painted figure on white paper, lower half | Figure rises 20 f power2.out; words pop +3 f | V01-A01, V03-A01 |

Always end the plan with:
- shot-mix percentages
- total length
- any assets the user still has to supply

Then **wait for the user's OK before building.**

## 4. QA checklist (run before delivery)

- [ ] 1080×1920, 30 fps (or the source fps), H.264 + AAC, loudness about −14 LUFS for social
- [ ] Every cut lands 0–2 f before a phrase's first word, never mid-word
- [ ] Every word pops 2–5 f after its onset; none appears before it's spoken
- [ ] One key word per line, ≈120 px; helpers ≈40 px, tucked tight, no reflow
- [ ] Text exits on cuts. The only text surviving a cut is a sentence that carries over.
- [ ] Key word y: 0.50 on B-roll / cards, 0.53 on the talking head (not over the face), upper third over illustrations
- [ ] Side margins ≥80 px, and nothing in the bottom 12% or top 8% (platform UI)
- [ ] All moves ease out (`power2.out`); no bounces or overshoots
- [ ] One blue value for the whole video; textures on every paper card; B-roll graded (desaturated, vignette, grain)
- [ ] Scene lengths median 1–1.8 s; diagrams held long enough to read
- [ ] Hook text visible by frame 5; CTA end card held ≈5 s
- [ ] No reference footage, wording, audio or likeness reused
- [ ] Camera on the speaker locked (no drift between cuts); zoom only where the plan asks
- [ ] Every painting: paint texture filter + rough paper texture + slide-in; faces not covered
- [ ] Captions centered (middle) and stacked; last word on screen ≥5 f
- [ ] Every beat approved on the plan page (or the user said it's final) before the delivery render

For footage edits, the plan lives on the plan page, not in plan cards: see `edit-plan-workflow.md`.
