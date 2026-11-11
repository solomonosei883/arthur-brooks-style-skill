# Building it

HyperFrames is the default target. Load the `hyperframes` skill first: it's the mandatory entry point and it owns the project structure, composition contract, timing attributes and rendering. This file covers only what's specific to the style.

## 1. Setup

1. Create or resume the HyperFrames project through the `hyperframes` skill. Use `general-video` for narrated multi-scene pieces, or `talking-head-recut` when cutting real A-roll.
2. Copy this skill's `assets/` folder into the project, for example to `assets/ab/`. `tokens.css` uses paths relative to itself, so keep `textures/` beside it.
3. Link `assets/ab/tokens.css` (it imports Inter and Playfair Display from Google Fonts) and load `assets/ab/ab-timing.js` after GSAP.
4. Canvas: 1080×1920, 30 fps. Make every scene its own sub-composition (per `hyperframes-studio`), with captions on one track.

## 2. Timing source

- Get word-level timings for the voice-over: `hyperframes transcribe`, or Whisper with `word_timestamps=True`. Ideally refine each start to the acoustic onset.
- Store them as `[{w, start, end}]`. All scene starts and word pops derive from `start`:

```js
const cut = AB.cutTime(words[firstIdx].start);          // scene in-point
AB.popWords(tl, els, words.slice(firstIdx, lastIdx+1).map(w => w.start), { kind: 'broll', sceneStart: cut });
AB.exitOnCut(tl, els, nextCut);                          // unless the sentence carries over
```

## 3. Snippets per scene type

**Cinematic lockup** (types 1, 2, 6, 7, 12)

```html
<div class="ab-cine">                       <!-- add is-aroll / is-upper / on-white / ab-ghost -->
  <span class="ab-lockup">
    <span class="ab-helper ab-tl ab-word">all the</span>
    <span class="ab-key ab-key--serif ab-word">time in</span>   <!-- or ab-key--bold -->
    <span class="ab-helper ab-br ab-word">people</span>
  </span>
</div>
```

Order the `.ab-word` elements to match the spoken order before calling `AB.popWords`.

**B-roll shot**

```html
<video class="ab-broll" src="footage/clip.mp4" muted playsinline></video>
<div class="ab-broll-edgeblur"></div><div class="ab-vignette"></div><div class="ab-grain"></div>
```

Add `AB.kenBurns(tl, video, cut, dur, 0.01)`.

**Ghost-line text card**

`<div class="ab-bg ab-paper-blue"></div>` plus `.ab-cine.ab-ghost`, then:

```js
AB.ghostLine(tl, els, onsets, { kind: 'card', at: cut, sceneStart: cut })
```

**Line + text**

Inline `shapes/arc-line.svg` or `line-weave.svg` with `pathLength="1000"`:

```js
AB.drawLine(tl, path, cut, 15)
```

The words pop when the line reaches them. For a camera follow, tween the wrapper's `y` with `power2.inOut`.

**Center illustration**

- A painted figure PNG/SVG (rough edges: `feTurbulence` + `feDisplacementMap`) in the lower half on `ab-paper-white` or `-rough`.
- `AB.enter(tl, fig, { y: 220, scale: .9, opacity: 0 }, cut, 20)`, with the text `.is-upper`.

**Photo cutouts / timeline**

- `.ab-photo` elements tilted 5–25°.
- `AB.photoFlyIn(tl, el, cut + i * AB.f(10), { dx, dy, rot, frames: 24 })`.
- For a timeline, slide `shapes/timeline.svg` horizontally with `power2.inOut` so the active tick sits at x = 540.

**Diagram**

- `ab-paper-white` + `.ab-glow`, a ring from `shapes/orbit-ring.svg` drawn with `AB.drawLine(…, 20)`.
- Labels as `.ab-label.ab-word`, popped on their spoken words.
- Nodes/triangle/Venn: scale from 0.6 → 1 over 11 f `power2.out`.
- Optionally run graphics on twos with `ease: AB.onTwos('power2.out', dur, 12)`.

**Document fly-in**

`.ab-doc` on `ab-paper-blue`:

```js
tl.from(doc, { rotation: -35, rotationX: 40, x: -300, y: -200, duration: AB.f(3), ease: 'power2.out' }, cut)
```

Then a slow scale 1 → 1.15 over 2 s, and highlight bars (`scaleX` 0→1, transform-origin left, 6 f).

**Inset**

`.ab-inset` holding a `<video>`; text `.ab-cine` with `top: var(--ab-y-inset-text)`; pop the inset in with `AB.enter(tl, inset, { scale: .94, opacity: 0 }, cut, 8)`.

**Transitions**

- `AB.slideOut(tl, sceneEl, nextCut)`.
- Flash: `tl.set(flashEl, { opacity: 1 }, nextCut - AB.f(1)).set(flashEl, { opacity: 0 }, nextCut)`.
- Glitch: 4–6 frames of a displacement filter, then cut.

**End card**

`ab-paper-blue`; `<span class="ab-key ab-key--serif">Comment "GUIDE"</span>` with a tiny `.ab-subtitle` sub-line; hold 5 s.

## 4. Rendering

- 1080×1920, 30 fps, H.264 high profile, CRF ≈18, AAC 192 kbps.
- Audio: voice-over first; music under it at about −20 dB and ducked under speech (`hyperframes-audio`).
- Check against the QA list in `planning.md`. Render a contact sheet of scene midpoints and compare it with the reference cards.

## 5. Other editors (Premiere, Final Cut, CapCut, After Effects)

Export a cue sheet from the plan: `scene, cut_in, cut_out, type, text, key, asset, motion`, plus per-word pop times (`onset + 3 f`). Then apply the same tokens: fonts, sizes, colors and easing (After Effects: Easy Ease Out, influence ≈70%).
