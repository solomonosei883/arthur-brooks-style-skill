# Edit pipeline (reference implementation)

> **Created by @ond.finds** · Instagram: https://www.instagram.com/ond.finds/ · TikTok: https://www.tiktok.com/@ond.finds
> This skill, the edit-plan workflow and the plan page are the creator's work. Keep this credit when you share or adapt them.

These are the scripts that built and shipped a real 18-beat edit (2026-11-08); `beats_example.py` is a short neutral sample of the beat format. They are the working pattern for every footage edit; copy them into a new project's `edit/tools/` and adapt the project-specific parts (beats, word indices, scene specs, assets). The workflow they serve is `references/edit-plan-workflow.md`; the rules they implement are `references/house-standards.md`.

## Project layout they expect

```
projects/<name>/
  transcript.json        # {duration, words: [{i, w, start, end}]} on the cut timeline (ms onsets)
  cut_list.json          # {segments: [[a, b], ...]} in source-segment time (silence cut, 30 ms padding)
  plan/plan-data.json    # beats + 3 options each (+ rev once built), see make_plan_page.py
  plan/index.html        # the plan page (make_plan_page.py), opts/, rev/, posters/, media/
  edit/                  # HyperFrames project: index.html, compositions/sNN.html, assets/, tools/
  previews/              # second HyperFrames project for the B/C option previews (same assets)
  assets-src/            # downloaded originals + credits.json (Commons, Pexels)
  renders/               # final render
```

## Scripts

| Script | What it does |
|---|---|
| `beats_example.py` | How the beats + 3 options are written (first/last word index, note, options with category, kind, description, Ref ID). Produces `plan-data.json`. |
| `build.py` | The shared builder: design tokens, lockups (helpers + key word, slots tl/tr/tc/br/bl/bc/sub, centered placement, wrap widths, ghost words, highlight box), word-pop clamp, backgrounds (A-roll, A-roll copy with zoom/grade, B-roll, painting with slide-in + paint grade + rough paper, paper colors, graph page), segment cuts and smooth zoom-through hand-offs, `GRADES` (canonical `data-color-grading` payloads), art functions (career map graphs, HUD, side illustration, turns path, light disc, photo card…). `build_scene(n, segs, sid, over, end)` makes one scene composition. |
| `variants.py` | The B/C options for every beat as real scenes + `previews/index.html` (all options end to end over their own A-roll slices). More art: map, icons, hill, envelope, photo card, line break, line turn, stacked text, spiral, halo figure, mountain. |
| `final.py` | The edit from the user's picks: one dict per beat (`FINAL`), the user-plan arts (Line + Text with a tracking camera, object callout with rough reveal), `NOTES` per beat for the Revised notes, writes `compositions/sNN.html` + `index.html`. |
| `cut_previews.py` | Cuts one 540×960 clip + end-frame poster per option from the edit render (A) and the previews render (B/C) into `plan/opts/`. |
| `publish_rev.py <render> <v>` | Cuts Revised vN clips per beat into `plan/rev/`, writes `rev: {v, dur, what}` into `plan-data.json` and the page's data block. Then republish the page with `rev/*` + `plan-data.json`. |
| `ascii_safe.py <page.html>` | Puts `<meta charset="utf-8">` first and escapes every non-ASCII character, so no viewer shows garbled text (Â, â€œ). Run after editing a page. |
| `make_plan_page.py <plan-data.json> <out.html>` | Fills `../plan-page/plan-template.html`. Publish with capabilities `{db: {}, assets: {}, downloads: true}`. |
| `recrop/` | Locked-camera A-roll (each script takes its files as arguments, see the `usage:` line at its top): `extract.py` (rebuild the landscape cut, same segments + frame counts) → `analyze.py` (sync check + per-frame crop measured from the old 9:16 by template matching) → `snap_boundaries.py` (shot boundaries onto real camera cuts) → `render_locked2.py` (one fixed crop per stretch between cuts, reframe only at cuts). Mux the original audio: `ffmpeg -i locked_v.mp4 -i old_aroll.mp4 -map 0:v -map 1:a -c:v libx264 -crf 15 -g 24 -c:a copy`. Needs a venv with `numpy opencv-python-headless`. |

## Order of work

1. Transcribe + silence cut + 9:16 (locked camera from the start: run `recrop/` on the cut).
2. Beats + options → `plan-data.json`.
3. Build the A scenes (`build.py`/`final.py` pattern) and B/C (`variants.py`), lint/check both projects, snapshot, render both at draft, `cut_previews.py`.
4. `make_plan_page.py`, publish, give the user the link.
5. When the picks are in: read `beats` with ArtifactData, read every reference image (Artifact read, `path: <asset id>`), update `FINAL`, build, check, draft render, `publish_rev.py`, republish.
6. Repeat 5 per round of changes; final render with `-q delivery` when approved.

## Checks that caught real problems

- `hyperframes lint` warns on overlapping tweens (camera keyframes that touch), negative z-index, nested media start basis (add `data-hf-media-start-basis="local"`), multiple root compositions (keep previews in their own project), duplicate audio on one track (alternate track indexes).
- Snapshots don't always run the grading shader: verify looks in Studio or in a draft render.
- `freezedetect` on A-roll clips; audio envelope cross-correlation between option clips (0 ms).
- A big graded `<img>` mostly outside its box rendered ungraded: pre-grade such crops as files.
