# House standards (approved by the user, 2026-11-08)

> **Created by @ond.finds** · Instagram: https://www.instagram.com/ond.finds/ · TikTok: https://www.tiktok.com/@ond.finds
> This skill, the edit-plan workflow and the plan page are the creator's work. Keep this credit when you share or adapt them.

These override any older or looser guidance in this kit. Apply them to every edit.

## 1. Locked camera on the speaker

- The camera on the speaker must be **firm**: no drift, wobble or slow pan while they talk. Never use a face-tracking crop that follows the head.
- Make the 9:16 A-roll from the 16:9 source with **one fixed crop per stretch between cuts**. The framing may change only at a cut that already exists (a camera cut or a jump cut from the silence edit), where a reframe is invisible.
- Pick each stretch's crop from the median face/subject position in that stretch; keep the face fully in frame at the stretch's extremes (check frames where the subject leans most).
- Snap shot boundaries to the real camera cut (the frame-difference spike within ±5 f of the detected change); being 1–4 frames off shows a wrong-framed flash.
- The only camera motion allowed on the speaker is a **deliberate zoom effect** the plan asks for (slow push-in, `scale 1.00 → 1.12`, `sine.inOut`, over the beat, origin on the face). Do it in the scene on a muted, dense-keyframe copy of the A-roll (`-g 24`), with the sound still coming from the root A-roll.
- Pipeline: rebuild the landscape cut from the source with the same segment list and frame counts as the 9:16 cut (`round(cum_start·fps)` … `round(cum_end·fps)` per segment), confirm sync against the old cut (join-frame spikes line up at offset 0), measure the old crop per frame by template matching (OpenCV), take medians per stretch, render `crop → scale 1080×1920 lanczos`, mux the original audio unchanged. Scripts: `assets/edit-pipeline/recrop/`.

## 2. Painting animation (every painting, every time)

Every painting scene gets the full painting treatment unless the user says to keep a specific one as is:

1. **Paint texture filter**: canonical HyperFrames grading on the `<img>`:
   `{"preset":"neutral","intensity":1,"adjust":{"exposure":-0.12,"contrast":0.1,"saturation":-0.18},"details":{"vignette":0.55,"grain":0.35,"grainSize":0.45,"grainRoughness":0.85},"effects":{"kuwahara":0.7,"kuwaharaRadius":0.14,"kuwaharaSharpness":0.45}}`
   (Kuwahara stronger than ~0.75 smears faces; keep faces readable.)
2. **Rough paper texture** on top, two layers: the kit's mottled texture (`cloth-grey.jpg`, cover, `mix-blend-mode: overlay`, opacity 0.6) and paper speckle (`paper-white-rough.jpg`, `multiply`, opacity 0.75).
3. **Quick camera slide-in reveal**: camera from `scale +0.18, x ±140` to the resting scale in 16 f `power3.out`, then a slow push (+0.04 over the rest). Stay inside the overscan (|x| ≤ (scale−1)·540).
4. **Captions in the middle**: centered horizontally, stacked: small Inter line centered above, serif key word centered below (e.g. "and I fell in love with a girl in / **San Diego.**"). Place the block where it is readable and does **not** cover the subject's face; if the subject's head is at the top, lower the painting (resting scale ~1.25 and a y offset) to open space above it.
5. Keep the main subject (faces, figures) in view for the whole scene. Check a frame at the end of the slide-in and at the scene's end.

## 3. Captions

- Captions sit in the **middle**: horizontally centered on paintings, object/photo cards, B-roll and text cards. On the talking head they sit at chest height (y≈0.53–0.58), centered, never over the face.
- Helper line above the key word is centered over it (`tc`), not hung left.
- The scene-final word must stay on screen at least **5 frames** before the cut: pop at `min(onset + 3 f, cut − 5 f)` (never earlier than 2 f into the scene). Fast last words may pop 1–3 f early; that's fine.
- A key word can get a **highlight**: blue box (`#0844EA`) wiping in from the left behind the word (6 f, `power2.out`), white text, box padded `−0.06em … +0.16em` so the last glyph (incl. period) is inside it. Use Inter ExtraBold, larger (≈190 px), uppercase when the user writes the word in caps.

## 4. Footage looks (canonical treatments only)

- **Soft black and white** (A-roll or B-roll): `{"preset":"mono-fade","intensity":1,"details":{"vignette":0.12,"grain":0.06}}`.
- **Dark, moody B-roll with a bold key word** (the "fight against something" look): `{"preset":"muted-editorial","intensity":0.85,"adjust":{"exposure":-0.75,"contrast":0.25,"highlights":-0.3,"saturation":-0.4},"details":{"vignette":0.5,"grain":0.12,"grainSize":0.24}}`; caption centered: small helper above-left, Inter ExtraBold key, small helper below-right.
- Ordinary B-roll: `muted-editorial` 0.7, vignette 0.18, grain 0.1.
- Apply looks with `data-color-grading` (validate with `hyperframes media-treatment --apply --dry-run`). Never fake them with CSS filters or DOM grain/vignette overlays. The paper textures in §2 are design layers, not treatments.
- A graded `<img>` that is much larger than its visible box (e.g. a face zoom inside a small circle) may render ungraded: pre-crop and pre-grade that image as a file instead (e.g. a black-and-white face crop for a circle photo).

## 5. Transitions and recipes the user approved

- **Smooth hand-off from the face to a cut-away**: the next segment fades in with a zoom-through (`opacity 0→1`, `scale 1.12→1`, 14 f `power2.out`, starting 5 f before the cut), the face segment's captions fade out over 8 f. Start the cut-away video 5 f early so it's visible during the fade.
- **Line + Text** (user's own design): rough white paper; thick blue line (≈64 px, `#0844EA`) leads up to each piece of text, is interrupted by it and continues; the camera tracks the line (world container translated per beat, each new word kept in the lower-middle). Black serif key words, Inter helpers.
- **Object callout**: one photo object on rough paper revealed with a rough-edged wipe (SVG mask rect + displacement filter, height tween); serif labels with thin callout lines and dots pointing at the object; credit line at the bottom.
- **Desk / object photo card**: straight (0°) and centered, white border, soft shadow; caption centered above it.

## 6. Delivery

- Frame rate follows the source (e.g. 23.976 = `24000/1001`); render with `-q delivery`.
- End when the speaker ends unless the plan has an end card.
- Credits for licensed photos on screen (small, bottom) and in the brief.

## 7. Creator credit

- The workflow, plan page and this skill were created by **@ond.finds** (Instagram https://www.instagram.com/ond.finds/ · TikTok https://www.tiktok.com/@ond.finds).
- Every plan page shows the credit (title line, corner watermark, footer) and every copied plan / zip carries it (`CREDITS.txt`). Keep it when sharing.
