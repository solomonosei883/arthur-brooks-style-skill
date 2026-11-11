/* arthurcbrooks: timing helpers for GSAP / HyperFrames compositions.
   Measured rules (see references/timing-and-sync.md):
     cut        = phrase's first word onset − 1 frame
     word pop   = word onset + 3 frames (talking head: + 2), opacity 0→1 over 1 frame
     first text after a fresh cut ≈ cut + 5 frames (falls out of the rule above)
     text exit  = hard, on the cut (no fade-out)
     moves      = power2.out, 8–17 f (UI/text), 11 f (diagram parts), 15–30 f (illustration / photo settle)
   All times in seconds unless stated. Words come from a word-level transcript: [{w, start, end}] (start = onset). */

const AB = (() => {
  const FPS = 30;
  const f = (frames, fps = FPS) => frames / fps;

  /** Time of the cut for a phrase whose first word starts at `onset`. */
  const cutTime = (onset, fps = FPS) => Math.max(0, onset - f(1, fps));

  /** When a word should pop. kind: 'broll' | 'card' | 'aroll' | 'diagram' */
  const popTime = (onset, kind = 'broll', fps = FPS) => onset + f(kind === 'aroll' ? 2 : 3, fps);

  /**
   * Pop each word element on its spoken onset.
   * els:    array of elements (pre-placed, opacity 0 or ghost)
   * onsets: array of seconds, same order
   * opts:   { kind, fps, popFrames (1–2), sceneStart (clamp: never before the scene's cut + 2 f) }
   */
  function popWords(tl, els, onsets, opts = {}) {
    const { kind = 'broll', fps = FPS, popFrames = 1, sceneStart = 0 } = opts;
    els.forEach((el, i) => {
      const t = Math.max(popTime(onsets[i], kind, fps), sceneStart + f(2, fps));
      tl.to(el, { opacity: 1, duration: f(popFrames, fps), ease: 'none' }, t);
    });
    return tl;
  }

  /** Ghost line: show every word at `ghost` opacity from `at`, then pop each on its onset. */
  function ghostLine(tl, els, onsets, opts = {}) {
    const { ghost = 0.15, at = 0 } = opts;
    tl.set(els, { opacity: ghost }, at);
    return popWords(tl, els, onsets, opts);
  }

  /** Hard exit on the cut (text never fades out). */
  const exitOnCut = (tl, els, cut) => tl.set(els, { opacity: 0 }, cut);

  /** Standard entrance (element, illustration, photo). */
  function enter(tl, el, from, at, frames = 11, fps = FPS) {
    return tl.from(el, { ...from, duration: f(frames, fps), ease: 'power2.out' }, at);
  }

  /** Photo cutout fly-in: off-frame, rotated, settles with ease-out. Stagger ≈10 f between photos. */
  function photoFlyIn(tl, el, at, { dx = 700, dy = -300, rot = -18, frames = 24, fps = FPS } = {}) {
    return tl.from(el, { x: dx, y: dy, rotation: rot, duration: f(frames, fps), ease: 'power2.out' }, at);
  }

  /** Slide-out transition: frame accelerates left ≈240 px in 3 f (ease-in), then hard cut. */
  function slideOut(tl, el, cut, fps = FPS) {
    return tl.to(el, { x: -240, duration: f(3, fps), ease: 'power2.in' }, cut - f(3, fps));
  }

  /** Slow camera on stills/B-roll: scale 1 → 1+rate*dur (rate ≈ 0.01 per second = 1 %/s). */
  function kenBurns(tl, el, at, dur, rate = 0.01) {
    return tl.fromTo(el, { scale: 1 }, { scale: 1 + rate * dur, duration: dur, ease: 'none' }, at);
  }

  /** "On twos": quantise any ease to N updates per second (reels 01–03 graphics run ≈12 fps). */
  function onTwos(ease = 'power2.out', duration = 0.4, updatesPerSec = 12) {
    const base = gsap.parseEase(ease);
    const steps = Math.max(1, Math.round(duration * updatesPerSec));
    return (p) => base(Math.floor(p * steps) / steps);
  }

  /** Draw an SVG path (needs pathLength="1000" on the path). */
  function drawLine(tl, path, at, frames = 15, fps = FPS) {
    tl.set(path, { strokeDasharray: 1000, strokeDashoffset: 1000 }, 0);
    return tl.to(path, { strokeDashoffset: 0, duration: f(frames, fps), ease: 'power2.out' }, at);
  }

  return { FPS, f, cutTime, popTime, popWords, ghostLine, exitOnCut, enter, photoFlyIn, slideOut, kenBurns, onTwos, drawLine };
})();
if (typeof window !== 'undefined') window.AB = AB;
if (typeof module !== 'undefined') module.exports = AB;
