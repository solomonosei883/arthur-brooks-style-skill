---
name: arthurcbrooks
description: The "Arthur Brooks" clean, premium, minimal educational short-form editing style, as a complete kit. It includes the design system (Inter + Playfair Display Italic "cinematic text", signature blue/white paper, textures, shapes, layout), frame-level timing rules (cut on onset −1 f, each word pops at onset +3 f), easing and animation durations, 15 scene types, a scene-plan template, HyperFrames/GSAP building blocks, and a library of 280 reference animations (clip, keyframe, frame strip and notes each). Use it whenever the user wants to plan, script, storyboard, design, animate, build or review a vertical 9:16 talking-head or voice-over reel in this style, and every time the user posts a plain video to be edited: it runs the house edit-plan workflow (a shared plan page with 3 playable design options per beat, an own-plan option, reference-image uploads, revised scenes to approve, then the render). Triggers include "Arthur Brooks style", "cinematic text", "blue paper cards", "serif + sans captions", "like the reference reels", "make it look like the breakdown", or a request to turn a script, topic or footage into an edit in this look. Created by @ond.finds.
---

# arthurcbrooks: clean, premium, minimal educational reels

> **Created by @ond.finds** · Instagram: https://www.instagram.com/ond.finds/ · TikTok: https://www.tiktok.com/@ond.finds
> This skill, the edit-plan workflow and the plan page are the creator's work. Keep this credit when you share or adapt them.

This kit was learned from 6 reference reels: 343 scenes, 2,089 spoken words, 17,999 frames OCR'd, and motion measured frame by frame. It was cross-checked against the tutorial *How to Edit Viral Talking Head Videos Using Claude*.

**The references teach the logic. Never reuse their footage, wording or audio in original work.**

## What's in the kit

| Need | Read / use |
|---|---|
| **A plain video to edit: the full house workflow (plan page → picks → revisions → approve → render)** | `references/edit-plan-workflow.md` |
| **The approved house standards (locked camera, painting filter, centered captions, looks, recipes)** | `references/house-standards.md` |
| The plan page (Artifact) to publish for the user | `assets/plan-page/plan-template.html` |
| The working build pipeline (scenes, previews, revisions, locked-camera recrop) | `assets/edit-pipeline/` (start with its `README.md`) |
| Fonts, colors, sizes, layout, textures, shapes | `references/design-system.md` |
| Where cuts land, when each word appears, pacing | `references/timing-and-sync.md` |
| Easing, durations, camera, transitions, signature moves | `references/motion.md` |
| The 15 scene types, with when to use each, recipes and library examples | `references/scene-types.md` |
| Story structure, script → scene workflow, plan-card format, QA | `references/planning.md` |
| Building in HyperFrames / GSAP (tokens, helpers, snippets) | `references/build-hyperframes.md` |
| All 280 reference animations, by category | `references/animation-library.md` |
| One animation's full notes (timing table, motion, design, recipe) | `references/library/<ID>.md`, e.g. `references/library/V01-A16.md` |
| CSS tokens and classes | `assets/tokens.css` |
| Timing helpers (cut, pop, ghost line, photo fly-in, on-twos) | `assets/ab-timing.js` |
| Paper and overlay textures (generated, original) | `assets/textures/` |
| SVG shape kit (arc line, orbit ring, Venn, triangle, steps, timeline, inset, graph…) | `assets/shapes/` |
| Live demo of the look; preview sheet of every shape (open over HTTP) | `assets/templates/style-demo.html`, `assets/templates/shape-kit.html` |

Everything needed to plan and build is inside this skill, so it works in the Claude app as well as in Claude Code. The **media** for the library (clips, keyframes, frame strips) lives only on the user's Mac. When that folder exists (Claude Code on that machine), use it. Otherwise rely on `references/library/*.md`.

If you build your own study folder (not part of this repo; it holds media you collect yourself), keep it at e.g. `~/arthurcbrooks-study/` with this layout:
- `animations/<ID Title>/`: `clip.mp4`, `still.png`, `strip.jpg` and `notes.md` for each of the 280 animations, plus `INDEX.md` and `index.json`
- `scenes/breakdowns/video-0X.md` and `.json`: per-reel word-level transcript, scene timing and reveal timing
- `scenes/STYLE-GUIDE.md`: the human-readable guide
- `scenes/index.html` and `video-0X/scene_XXX.jpg`: the annotated scene cards (design reference)

Use the **scene cards** to learn the design and the **reference clips** to learn the animation logic. To understand a move, open the matching library folder: `strip.jpg` shows every frame, labeled with frame number and ms, and `notes.md` gives the timing numbers.

## Workflow

**A plain video to edit → always run the house workflow in `references/edit-plan-workflow.md`:** prep (word-level transcript, silence cut, 9:16 with a locked camera) → beats with 3 design options each → every option built and rendered as a playable preview on the real audio → the plan page (options, D · My own plan, changes, exact-file reference images, Copy Plan + files) → read the user's picks and images and build → Revised vN clips to Approve / Needs more changes → repeat until approved → final render. Apply `references/house-standards.md` throughout.

For a script or topic without footage, the steps below still apply:

1. **Get the brief.** You need the topic, script (or offer to write one), footage/assets and their folder, the CTA, and brand overrides (default: match the reference). Ask only for what's missing.
2. **Transcribe** the voice-over to word level, with each word's onset (Whisper word timestamps, ideally refined to the acoustic onset). Every timing rule keys off word onsets.
3. **Phrase the script** into 1–5-word units. Mark one key word per unit (the meaning-carrying word, usually late in the phrase).
4. **Pick a scene type per unit** using the decision table in `references/scene-types.md`:
   - announce an idea → face
   - describe it → B-roll / painting / illustration
   - frameworks → diagram
   - numbers → graph
   - punchline or reversal → text card
5. **Write the scene-by-scene plan.** For footage, this is the plan page (3 options per beat + own plan). Otherwise use the plan-card format (`references/planning.md`). Each scene runs ~1–2 s, with on-screen text (key word marked), shot type, visual, elements, motion and timing. **Wait for the user's picks / OK before building.**
6. **Build.** Load the `hyperframes` skill first if HyperFrames is the target. Copy `assets/` into the project, link `tokens.css`, and drive the timing with `ab-timing.js` using the transcript onsets. Follow `references/build-hyperframes.md`.
7. **QA** against the checklist in `references/planning.md`: cut timing, pop lag, one key word per line, exits on cuts, easing, safe margins, colors, texture, CTA hold.

## The 15 rules that make the look

1. **A new visual every 1.0–1.8 s.** Median scene: 1.0 s on B-roll, 2.4 s on the talking head. Diagrams get 3–9 s.
2. **Cut 1 frame before the first word of the next phrase.** Measured median −0.5 f; 57% of cuts land within ±3 f.
3. **Cut phrase-to-phrase, not sentence-to-sentence.** Only 25% of cuts follow punctuation. Most land on *the / you / I / that / a / and*.
4. **One word at a time.** 85% of reveals are a single word.
5. **Each word pops 3–5 f after its onset.** Median +4.8 f; talking head +2 f, B-roll +7 f. Never before the voice.
6. **Hard pop:** opacity 0→1 in 1–2 f, with no scale, rise or blur. Measured travel: 0 px.
7. **Pre-placed layout.** Helpers sit in their final spots with a gap reserved for the key word, and nothing reflows.
8. **Key word ≈120 px; helpers 0.33× its height.** IQR 0.27–0.40. Key word is Playfair Display Italic *or* Inter ExtraBold; helpers are Inter Medium.
9. **Key words sit center** (y 0.50); on the talking head, at chest height (0.53); over a lower-half illustration, in the upper third (0.25–0.35).
10. **Text exits on the cut** (92%) and never fades out.
11. **When a sentence spans two shots, the text stays and only the footage changes underneath.**
12. **Ghost-line variant:** the whole line sits at 15% (white on blue) or 10% (blue on white), and each word snaps to 100% as it's spoken.
13. **Everything eases out** (`power2.out`). Entrances take 8–17 f; photos and illustrations settle over 15–30 f. The only ease-in is the slide-out exit.
14. **Graphics on twos.** Designed scenes can update at ~12 fps while footage stays at 30 (`AB.onTwos`).
15. **Palette:** blue paper `#0844EA` (one per-reel variant per video), white `#FBF9FC`, black `#000402`, yellow `#F9DB59` (rare). B-roll is desaturated about 30%, with vignette and grain.

### House standards (the user's approved upgrades, always on)

16. **Locked camera on the speaker.** No face-tracking drift; one fixed crop per stretch between cuts; reframe only at existing cuts. The only allowed motion is a deliberate zoom effect.
17. **Every painting gets the painting animation:** paint texture filter + rough paper texture + quick slide-in, subject kept in view.
18. **Captions in the middle:** centered and stacked (small line above, key word below) on paintings, photo/object cards and cut-aways; chest height and centered on the face.
19. **Last word stays ≥5 frames** before the cut.
20. **Looks via canonical treatments only** (`data-color-grading`), never CSS filters.

Exact values and recipes: `references/house-standards.md`.

## Defaults when the user says "match the reference"

- 1080×1920 at 30 fps (or the source's frame rate when editing footage), 90–110 s, 200 wpm voice
- Story: hook → relatable problem → science → older wisdom → practical change → payoff + CTA card held about 5 s
- Shot mix target: B-roll ~40%, talking head ~15% (if there is A-roll), text cards ~10%, illustration ~10%, collage/object ~10%, diagram ~8%, inset/screen/end card remainder
- Fonts: Inter + Playfair Display (Google Fonts, linked in `tokens.css`)
