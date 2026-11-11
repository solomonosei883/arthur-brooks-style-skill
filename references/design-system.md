# Design system

Everything visual: fonts, sizes, layout grid, colors, textures, shapes and framing elements. Values were measured on the 6 reference reels (720×1280, scaled ×1.5 to 1080×1920) and cross-checked with the tutorial doc. Tokens and classes are in `assets/tokens.css`.

## 1. Typography ("cinematic text")

**Fonts**
- **Inter**: helpers in Regular/Medium (400–500); key words in Bold/ExtraBold (700–800). Tracking −1% on helpers, −3% on bold key words.
- **Playfair Display**: Italic 700 for most serif key words; Roman 400–500 for some headings and labels ("The meaning", "idea behind"). Tracking −2% to −3%.
- Within a scene the key word is either serif *or* bold Inter, never both in one lockup. Helpers are always Inter.

**Sizes at 1080×1920**
| Role | Size | Notes |
|---|---|---|
| Key word | 110–140 px font (text box 130–160 px tall) | One per line |
| Helper words | 0.33× key height (IQR 0.27–0.40), about 36–48 px | Inter Medium |
| Subtitle-style line (low emphasis) | 34–44 px | Inter Medium; one word may go bold |
| Tiny line on a card (blue cards, 03/05) | 26–32 px | Used alone, dead center |
| Diagram labels | 26–34 px Inter SemiBold, or 36–44 px Playfair Italic | On white: blue or ink |
| Timeline labels | 20–24 px Inter, caps | grey `#5B6478` |
| End-card CTA | key ≈ 90–110 px serif; sub-line ≈ 28 px | |

The tutorial says the light sans is "75% of the big bold text". On screen, helpers measure about **one-third** of the key word's height, so use the measured ratio for size.

**Line logic (the lockup)**
1. Take a phrase of ≤5 words.
2. Choose the key word: the noun, adjective or verb that carries the meaning (*meaning, mistake, painful, hatred, wrong, anxiety, achievement*). It sits late in the phrase: median position 0.67, and the last word 37% of the time.
3. Set the key word big and centered.
4. Tuck the helpers into the gaps around it: above-left ("all the" over "time in"), above-right, below-right ("people" under "time in"), or above-center. Helpers almost touch the key word's ascenders and descenders.
5. Keep punctuation on the key word ("lives.", "basically.", "you,"). Quotes get big curly marks in serif italic, in the text color.

Lockup slots in `tokens.css`: `.ab-tl .ab-tr .ab-tc .ab-bl .ab-br .ab-bc` around `.ab-key`.

**Common patterns** (see the library for each)
- helpers above-left + above-right with a gap, key word dropping into the gap (V01-A03)
- small line on top, key word under it (V01-A18, V03-A32)
- key word first, a row of tiny helpers building under it (V01-A22, V03-A22)
- three-level stack: tiny helper / serif key words / smaller serif line (V04-A12)
- subtitle only, no key word (V01-A23, V03-A24)
- quote: big curly marks around a serif line (V03-A45, V05-A37)

## 2. Layout

| Context | Key word center (y, fraction of height) | Notes |
|---|---|---|
| B-roll, text card, end card | 0.50 (10th–90th pct 0.44–0.54) | Centered on the focal point |
| Talking head | 0.53 (0.48–0.64) | Chest / mic height, never over the face |
| Illustration, collage or diagram in the lower half | 0.24–0.35 | Text owns the top third |
| B-roll inset | 0.39 | Just above the inset |

- Horizontally centered (x 0.48–0.52), with 80 px side margins.
- Illustrations fill the lower half and bleed up into the middle. Side illustrations take one flank, with text on the other.
- **Inset:** a rounded clip with 16–24 px radius, about 82–85% of frame width, centered on black. The tall variant is about 64% wide.

## 3. Color

| Token | Hex | Use |
|---|---|---|
| `--ab-blue` | `#0844EA` | Signature blue paper (median). Per reel: 01 `#2150F1`, 02 `#1A6AF4`, 03 `#072EE6`, 04 `#0C3EDB`, 06 `#107DF3`. **Pick one per video.** |
| `--ab-blue-node` | `#2F6BF2` | Diagram nodes, highlight pill |
| `--ab-azure` | `#1E6AF1` | Glowing lines and dots on black |
| `--ab-white` | `#FBF9FC` | White paper |
| `--ab-white-rough` | `#ECE9E5` | Speckled / creased white paper |
| `--ab-black` | `#000402` | Black paper; inset and line scenes |
| `--ab-navy` | `#0B0C10` | Graph and dark diagram background |
| `--ab-yellow` | `#F9DB59` | Full-frame wash or paper panels (rare, one reel) |
| `--ab-ink` | `#1A1A2E` | Dark helper text and arrows on white |
| `--ab-grey` / `--ab-line-grey` | `#5B6478` / `#9AA3B8` | Timeline labels, construction lines, Venn rings |
| `--ab-red` | `#C8102E` | Rare emphasis (heart, "danger" brain) |
| `--ab-cyan` | `#3FF3FF` | 1-frame flash, negative tint |

**Text color**
- White on footage, blue and black.
- Blue on white paper, with ink or blue helpers.
- Near-black serif for a reversal on white ("But that's wrong.").

## 4. Textures (`assets/textures/`, generated, not from the reels)

| File | Look | Use |
|---|---|---|
| `paper-blue.jpg` | Fine grain, about ±2.4 levels, slight mottle | Default blue card |
| `paper-blue-rough.jpg` | Strong mottle, fibers, light speckle | Quote cards, illustration backgrounds |
| `paper-blue-v01.jpg` | Lighter blue `#2150F1` | Reel-01 look |
| `paper-white.jpg` | Nearly flat, faint fibers | Default white card / diagram |
| `paper-white-rough.jpg` | Grey-white with dark speckles | Rough text-centric cards, center illustrations |
| `paper-black.jpg` | Slight grain | Line, inset and glow scenes |
| `paper-yellow-rough.jpg` | Rough yellow | Accent wash |
| `grain-tile-512.png` | Tileable grain (overlay blend, 35%) | Over everything, footage included |
| `vignette.png` | Radial edge darkening (edges ≈0.8 brightness) | B-roll, paintings |
| `glow-blue.png` | Soft radial blue glow | Behind diagrams and orbit graphics |
| `cloth-grey.jpg` | Rough cloth | Fill for silhouettes and half-circles (via mask / blend) |

**Footage treatment**
- **B-roll:** saturation −30% (median 0.28 vs 0.33 on A-roll), vignette, slight edge blur (`.ab-broll-edgeblur`) and grain. Archival stays B&W.
- **Paintings:** paint plus rough-paper texture.
- **Illustrations:** flat blue (`#0844EA`–`#1E6AF1`) painted silhouettes with rough, noisy edges (SVG `feTurbulence` + `feDisplacementMap`, or a painted PNG) on white paper. Black rough-edged silhouettes also work on white or blue.

## 5. Shapes (`assets/shapes/`)

| File | What |
|---|---|
| `arc-line.svg` | Thick blue sweeping arc (≈80 px). Line + text |
| `line-weave.svg` | Line that breaks at a word and continues to the next |
| `line-dot-horizon.svg` | Glowing curve with a white anchor dot (line + illustration, on black) |
| `zigzag-path.svg` | Multi-phase zigzag with node dots |
| `orbit-ring.svg` | Thin 2 px ring with ticks and a travelling dot |
| `concentric-rings.svg` | Spiral / ripple rings around a head or dot |
| `triangle-diagram.svg` | Solid blue triangle, three-part framework |
| `venn-3.svg` | Three thin circles with a solid blue center |
| `step-nodes.svg` | Step-1 / Step-2 blue nodes with italic labels |
| `dual-rings-glow.svg` | Two glowing rings (comparison / overlap) |
| `timeline.svg` | Thin timeline with ticks, year labels and an active marker |
| `inset-frame.svg` | Rounded inset mask on black |
| `highlight-pill.svg` | Blue box behind a quoted caption |
| `curved-arrow.svg` | Hand-drawn pointer from a label |
| `half-circle.svg` | Side-illustration anchor shape |
| `graph-grid.svg` | Dark grid, glowing trace, blue ball |
| `quote-marks.svg` | Big curly quotes |

## 6. Framing elements (CSS classes)

- `.ab-photo`: photo cutout with a 10 px white border and a soft shadow (0 18 px 42 px, 28%). Tilt 5–25°.
- `.ab-doc`: research-paper card with a dog-eared bottom-right corner.
- `.ab-inset` / `.ab-inset.is-tall`: rounded B-roll clip.
- `.ab-highlight`: blue pill behind a caption line (talking head, reel 06).
- `.ab-tag`: small blue label tag (on photos and timelines).
