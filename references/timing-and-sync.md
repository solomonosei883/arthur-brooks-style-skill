# Timing and sync

All numbers are in frames at 30 fps (1 f = 33 ms), measured against each word's **acoustic onset**: Whisper word timestamps refined to the spectral-flux peak. Measurement noise is about ±2 f.

## 1. Pacing

| | Measured |
|---|---|
| Length | 58–150 s (four of six: 91–111 s) |
| Speech rate | 173–225 wpm (median ~205) |
| Scene length per reel | median 1.0–1.8 s; mean 1.7–2.7 s |
| Words per scene | median 5 (IQR 3–9), about 0.3 s per word |
| Transition slivers | 35 scenes of 1–4 frames |

**Median length by shot type**

| Shot type | Median length |
|---|---|
| B-roll | 1.00 s |
| B-roll inset | 1.00 s |
| Text card | 1.27 s |
| Photo collage | 1.40 s |
| Screen capture | 1.39 s |
| Illustration | 1.60 s |
| Talking head | 2.37 s |
| Motion graphic | 3.27 s |
| End card | 5.31 s |

**Rules**
- B-roll runs at about 1 shot per second, 3–5 words each.
- A concept graphic holds 3–9 s and keeps building, one label per named item.
- The talking head breathes for 2–4 s, then cuts away on the next phrase that can be pictured.
- A one-word punch card ("But then,", "next,") can be 0.6–0.9 s.

## 2. Cuts

- **Position:** cut time minus the nearest word onset is median −0.5 f, IQR −2.8 to +2.1 f; 55% of cuts come slightly before the word. **Rule: cut = onset of the phrase's first word − 1 f.** Never cut mid-word.
- **Trigger:** a new 1–5-word sense unit, usually opening on a function word (*the, you, I, that, a, and, it's, well*). Only 25% of cuts follow punctuation and 19% follow a pause of 150 ms or more, so cuts run inside sentences.
- **Carry-over:** when a sentence spans two shots, the text block stays put and keeps building while the footage changes underneath. It clears on the next cut after the sentence ends. Library: V01-A04, V01-A28, V03-A54, V05-A64.
- **Face vs. show:** introduce on the face, describe on B-roll or an illustration. When a sentence both introduces and describes, stay on the face for the first half and cut on the describing phrase.

## 3. Text reveal

| Measure | Value |
|---|---|
| Reveal unit | 1 word in 85% of cases; 2 words 11%; 3+ words 4% |
| Pop time vs. onset, all shots | median **+4.8 f**, IQR −0.2 to +10.5 (n = 974) |
| by shot type | A-roll +2.0 · photo collage +2.2 · motion graphic +4.4 · text card +5.4 · B-roll +7.4 |
| Key word vs. helpers | same timing (+3.4 vs +3.9 f): the key word gets no special lead |
| First text after a fresh cut | median 5 f after the cut (IQR 3–7) |
| Gap between successive pops | median 6 f (IQR 5–10), following the speech |
| Pop duration (10→90% contrast) | ≤2 f in 63% of cases; the rest are 3–8 f fades |
| Movement during the pop | none (median 0 px; no scale or blur) |
| Exit | on the cut in 92% of cases; no fade-out |

**Rules**
1. Pre-place every word of the line at its final position, at opacity 0 (or at ghost opacity).
2. Word *n* → opacity 1 at `onset(n) + 3 f` (talking head `+2 f`), over 1 f (or 2 f linear).
3. Never show a word before it's spoken. If a word starts within 2 f of the cut, it pops at cut + 2 f.
4. Clear all text on the next cut unless the sentence carries over.

**Ghost line**
- The whole line is visible at ≈15% (white on blue) or ≈8–12% (blue on white) from the first frame, and each word snaps to 100% on its onset.
- Use it on text cards, quote cards and diagram labels.
- Library: V01-A02, V01-A09, V01-A21, V01-A26, V01-A30, V03-A23, V03-A34.

`assets/ab-timing.js` implements this: `AB.cutTime`, `AB.popWords`, `AB.ghostLine` and `AB.exitOnCut`.

## 4. Choosing the key word

- It's the semantic payload: a concept noun, an emotion, a strong verb or adjective, a number, or a name.
- It usually comes late in the phrase: median position 0.67, and the last word 37% of the time.
- One per line. When two words form one idea, they share the key size ("time in", "good lives.", "next chapter,").
- Function words stay small, even when the cut lands on them.
