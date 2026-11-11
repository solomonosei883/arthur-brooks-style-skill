# The edit-plan workflow (house standard)

> **Created by @ond.finds** · Instagram: https://www.instagram.com/ond.finds/ · TikTok: https://www.tiktok.com/@ond.finds
> This skill, the edit-plan workflow and the plan page are the creator's work. Keep this credit when you share or adapt them.

Follow this **every time** the user posts a plain video (podcast clip, talking head, voice-over) to be edited in this style. It replaces the old "write a plan, wait for OK, build" loop with a shared plan page the user picks from, a build on the real audio, a review round, then the render.

First used and approved on "Four career patterns" (2026-11-07/08). The working implementation is in `assets/edit-pipeline/` (scripts) and `assets/plan-page/plan-template.html` (the page).

## The flow at a glance

| Step | Who | What happens |
|---|---|---|
| 1. Prep | Claude | Word-level transcript (ms onsets) → silence cut (30 ms padding) → 9:16 A-roll with a **locked camera** (see `house-standards.md`). |
| 2. Beats | Claude | Split the script into beats (one idea each, ~1–6 s). For every beat write **3 design options** (A = my pick), each from a different scene type where it fits, covering all 10 core scene types across the video. |
| 3. Previews | Claude | Build **every option as a real scene on the beat's own audio** and render it. A = "Built", B/C = "Preview". Cut one small clip + poster per option. |
| 4. Plan page | Claude | Publish the plan page (Artifact) with the beat timeline, the 3 playable options, **D · My own plan**, a changes box and reference-image uploads per beat. |
| 5. Pick | User | Plays the options, presses **Use this** (or writes D), writes changes, uploads reference images. Everything saves automatically. Then says "my picks are in" or pastes **Copy Plan + files**. |
| 6. Build | Claude | Reads the page's database and images directly, builds every beat from its pick + changes + reference images, renders a draft, cuts **Revised vN** clips per beat, republishes the page. |
| 7. Review | User | Plays each Revised clip, presses **Approve** or writes more changes + **Needs more changes**. Repeat 6–7 (v2, v3…) until everything is approved or the user says it's perfect. |
| 8. Render | Claude | Final render at the source frame rate, `-q delivery`. Check it (frames, duration, loudness) and report. |

Never skip the page. Never build the final edit before the user has picked.

## Step 2: writing the options

- One beat = one phrase group that one visual can carry (often a sentence). Keep the A-roll on the beat that **announces** a new idea; cut away on the beats that **describe** it.
- Each option card: letter, title, category (one of the 10 types below), kind (A-roll + captions / Overlay on A-roll / Cut-away scene), a one-paragraph description that says exactly what's on screen, the key word(s), and a Ref ID from the animation library.
- Across the video, use all 10 core types at least once where the script allows: 1 On-Screen Caption · 2 B-Roll + Text · 3 Painting · 4 Line + Text · 5 Line + Illustration · 6 Text-Centric · 7 Center Illustration · 8 Side Illustration + Text · 9 Object + Text · 10 Graphs + Statistics.
- Assets: paintings from Wikimedia Commons (public domain only), stock footage from Pexels (fetch the CDN file via the in-app browser, then download), photos of a real person only under a free license, with the credit shown on screen and kept in `credits.json`.

## Step 3: previews on the real audio

- Build B/C options in a **separate HyperFrames project** (`previews/`) that shares the edit's assets, so the edit project keeps one root composition. Lay all options end to end, each over its own A-roll slice (`data-media-start` = beat start), alternate track indexes so audio never overlaps.
- Render both projects at draft quality, cut each option (540×960, CRF ~27, AAC 96k, `+faststart`) and grab the poster from the scene's **final** frame (end − 0.15 s), so the card shows the finished design.
- Check: no frozen frames in A-roll options (`freezedetect`), audio of B/C matches A (envelope cross-correlation, 0 ms offset).

## Step 4: the plan page

Publish `assets/plan-page/plan-template.html` with the project's data in the `plan-data` JSON block. Capabilities: `{db: {}, assets: {}, downloads: true}`.

Per beat:
- Header with time range and a status pill ("Chosen: B", "Own plan", "Revised: review it", "Approved v2").
- **Changes for this beat** box + **Reference images** (for changes to A/B/C).
- The 3 option cards, each with a 9:16 preview tile that plays with sound (one video at a time), category, description, Ref ID, "My pick" badge on A, **Use this**.
- **D · My own plan**: its own text box (typing selects D), **Use my own plan**, and its own **Reference images for your plan**.
- **Revised scene · vN** block (once built): player, "what I changed", **Approve** / **Needs more changes**.
- Side column: the script, the beat's raw A-roll player, the "seen in the reels" note, camera line.

Creator credit (always, on every plan page): "Made by @ond.finds · Instagram · TikTok" under the title, a "Made by @ond.finds" corner watermark linking to https://www.instagram.com/ond.finds/, the footer line, a credit line in the copied plan text and `CREDITS.txt` in the zip. The template already has all five; never remove them.

Header: beat timeline (colored by kind, ✓ on approved beats, outline for own plans), the 3-step status line, the save pill, **Copy Plan + files**.

- Text must read cleanly in every viewer (claude.ai, the desktop app, a local file): the page starts with `<meta charset="utf-8">` and every non-ASCII character is written as an escape (HTML entity in markup, `\uXXXX` in scripts and the JSON data block). Run `assets/edit-pipeline/ascii_safe.py` on the page after any edit; data writers use `ensure_ascii=True`.

Data (`db` collection `beats`, doc `bNN`): `{beat, pick: "A"|"B"|"C"|"own"|null, note, own, refs: [ref], ownRefs: [ref], approved: vN|null, updatedAt}` where `ref = {id, name, type, bytes, w, h}`.

Reference images — non-negotiable:
- Upload the **exact original file**, byte for byte. Never resize, re-encode or convert. Accept PNG / JPG / GIF / WebP; refuse anything else (HEIC, AVIF…) with a message to re-save it as PNG or JPG. Refuse >20 MB.
- Thumbnails show the **whole** image (`object-fit: contain`, no crop, nothing drawn over it); name + Remove (Yes/No) under it. Click → full-size viewer with name, pixel size, file size and **Open original**.
- After upload, compare stored size with the file size and warn if different.

**Copy Plan + files** copies the plan text (per beat: design, description or own plan, changes, reference image file names, revision status, video file name) **and** saves a zip (`downloads.save`) containing `plan.txt`, `plan.json`, `images/` (every uploaded reference image, original bytes) and `videos/` (per beat the clip it uses: approved or latest Revised vN, otherwise the chosen option's preview). Built with JSZip (`cdnjs … jszip/3.10.1`), `compression: "STORE"`.

## Step 6: reading the picks and building

- Read the picks with `ArtifactData list beats` (use `out_dir` for many docs) and download every reference image with `Artifact read` + `path: <asset id>`; **look at each image** before building that beat.
- Interpret carefully:
  - A changes box that still contains another option's description means the user switched options; build the **selected** option and say what you did.
  - An own plan saved on a beat whose selected option is A/B/C is **not** used; say so.
  - Text that names other beats (e.g. "use this line for calling, agility, courage") belongs to those beats; ask or note it.
- Build every beat from its pick (`final.py` pattern: one dict per beat), apply the changes, re-run lint/check, snapshot the changed beats, fix, then render a draft and run `publish_rev.py <render> <v>` to cut Revised clips and embed `rev: {v, dur, what}` per beat in the page, and republish (page + `rev/*` + `plan-data.json`).
- Each Revised note says plainly what changed in that version.

## Step 8: final render

- `hyperframes render . -f <source fps> -q delivery -o ../renders/<name>_final_9x16.mp4`.
- Verify: 1080×1920, frame count = audio length × fps, frames tiled at 10 points, loudness measured (social target ≈ −14 LUFS; report the measured value and offer a normalized copy if far off).
- Report the file path, length, size and anything still open.
