# Motion

## 1. Easing

- **Ease-out everywhere, never bouncy.** Across 150 measured motion bursts, speed peaks in the first quarter of the move, and 65–70% of the distance is covered by the halfway point. That matches sine-out or quad-out.
- Use GSAP `power2.out` (CSS `cubic-bezier(0.25, 0.46, 0.45, 0.94)`).
- Some short label pops measure closer to cubic-out (80–86% done at the halfway point). Use `power3.out` for 4–6 f pops.
- **The only ease-in:** a slide-out exit that hands off to a cut (`power2.in`, 3 f).
- Timeline slides and camera pans between points use `power2.inOut`, which reads as slow-fast-slow.

## 2. Durations (frames at 30 fps)

| Animation | Typical | Range |
|---|---|---|
| Word pop | 1 f | 1–8 |
| Ghost → lit | 1 f | 1–2 |
| Text-card internal move | 8 f | 6–18 |
| Diagram part (node, ring segment, label, line) | 11 f | 6–17 |
| Illustration reveal / slide-in / scale-up | 15 f | 8–31 |
| Photo cutout fly-in and settle | 17–24 f | 8–37 |
| B-roll inset pop-in | 8 f | 6–12 |
| Line draw (arc / weave) | 12–20 f | |
| End-card build | 16 f | 14–18 |
| Slide-out transition | 3 f | |
| Glitch smear transition | 5 f | 4–6 |
| Invert / cyan flash | 1 f | 1–2 |

About half of illustration and collage moves start within 2 f of the cut, so the scene arrives already moving.

## 3. Frame cadence ("on twos")

- In reels 01–03, 45–70% of frames in designed scenes repeat the previous frame. Graphics update at about 9–15 unique fps while footage stays at 24–30.
- That stop-motion stepping is part of the crafted feel.
- To recreate it: `ease: AB.onTwos('power2.out', duration, 12)` for graphic layers only. Reels 04–06 run smooth, so it's optional.

## 4. Camera

| Content | Move |
|---|---|
| B-roll | Slow push-in, +0.3 to +1.6% scale per second (default 1%/s); some shots static |
| Illustration | Slow pull-out (−1 to −2%/s) or a lateral drift; sometimes a fast scale-up from small on entry (V01-A11, V03-A39) |
| Paper text card | Static |
| Collage | Camera drifts and pulls back while photos fly in (V01-A30); timelines slide horizontally (`power2.inOut`) so the active tick sits at center (V05-A18, V05-A34) |
| Painting | Quick slide-in reveal, 8–15 f |
| Line scene | Camera follows the line's head (pan down/across, slow-fast-slow) |

`AB.kenBurns(tl, el, at, dur, 0.01)` gives 1%/s.

## 5. Signature moves (library IDs in brackets)

- **Helpers then key word:** helpers pop at their final spots, and the key word drops into the reserved gap [V01-A03, V01-A41].
- **Ghost karaoke line** [V01-A02, V01-A26].
- **Text carries across cuts** [V01-A04, V01-A28, V03-A54, V05-A64].
- **Diagonal / panel wipes:**
  - A blue panel wipes away on a diagonal [V01-A07].
  - A negative-tinted panel slides in from the right as the exit [V04-A01, V04-A04, V04-A19].
  - Yellow or orange paper panels slide over the image [V04-A05, V04-A20].
- **Photo cutouts:** enter from off-frame, rotated 10–25°, settle flat; staggered about every 10 f; white border plus soft shadow [V01-A30, V02-A32, V05-A05, V05-A25].
- **Background wash:** white → blue in 3–4 steps over about 10 f under persistent elements [V02-A12]. Or a match cut that swaps only the background color [V01-A31].
- **Document fly-in:** a paper flips in rotated (2–3 f), lands flat, then a slow push to its title, with highlight bars wiping across a line [V02-A12/A13/A14, V06-A03/A04/A05].
- **Line + text:** a thick blue line draws in from the edge, stops at a word, passes it and continues to the next word while the camera follows [V02-A23, V02-A40, V03-A12].
- **Orbit / ring diagrams:** a soft blue glow blooms, a dot travels a thin ring to draw it, and labels pop at points [V01-A15, V03-A36, V03-A37, V02-A43].
- **Framework builds:** a dot becomes a triangle and labels pop at the vertices [V01-A16]; a Venn draws and its center fills [V03-A49]; Step-1/Step-2 nodes [V06-A19]; dual glowing rings slide to overlap [V06-A08/A09/A10].
- **Light reveal:** a glowing disc behind a blue figure rises from black [V01-A12, V03-A14/A15/A16].
- **Brain/scan treatments:** a scan tints red or green with grid guides [V06-A15/A16]; a brain lid lifts [V04-A08]; CT slices fade in left to right [V05-A58].
- **Circle highlight:** a thin blue or glowing ring draws around a face in a photo [V05-A13, V05-A47].
- **Highlight pill:** a blue box wipes in behind a quoted caption [V06-A23, V06-A11].
- **DM / chat bubble:** grows as the text types on [V05-A11]. **URL type-on:** letter by letter [V01-A46].

## 6. Transitions

More than 90% are hard cuts. The specials:

| Transition | Length | How |
|---|---|---|
| Pixel-smear glitch | 5 f | Desaturate, displacement smear sideways, cut [V02-A02, V02-A03] |
| Pixel-mosaic glitch | 3–6 f | Blocky B&W mosaic around a dissolving figure [V03-A17, V03-A18] |
| Slide-out whip | 3 f | Frame accelerates left 0 → −240 px (`power2.in`), cut [V03-A02] |
| Invert / strobe flash | 1–2 f | Color-inverted frame(s) [V03-A10, V04-A02] |
| White / cyan flash | 1–2 f | [V03-A39, V03-A40, V06-A02, V06-A03] |
| Dip to black | 2–3 f | [V02-A08, V02-A09] |
| Panel slide | 4–6 f | Tinted rectangle slides across [V04-A01, V04-A05] |
| Blank beat | 1–4 f | The next background color before its text arrives |
