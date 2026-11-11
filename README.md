# Arthur Brooks Style Skill for Claude (unofficial)

A Claude skill that edits **clean, premium, minimal educational reels**: the calm 9:16 talking-head look with blue/white paper cards, serif + sans "cinematic text", and words that pop exactly on the voice.

Made by **[@ond.finds](https://t.me/OutlastNeverDie)**: daily AI tools, tips and tech finds on Telegram. **[Join the channel →](https://t.me/OutlastNeverDie)**

> Unofficial and independent. Not made, endorsed or sponsored by Arthur C. Brooks. His name only describes the style it was inspired by. No footage, audio or wording from his videos is included.

---

## What it gives Claude

- **A design system:** Inter + Playfair Display Italic, blue/white paper, textures, shapes, layout and safe zones (`references/design-system.md`, `assets/tokens.css`)
- **Frame-level timing rules:** cut on the word onset −1 frame, each word pops at onset +3 frames, plus easing and animation durations (`references/timing-and-sync.md`, `references/motion.md`)
- **15 scene types** with a decision table: face, B-roll, painting, diagram, graph and more (`references/scene-types.md`)
- **280 reference animation notes:** timing tables, motion and recipe for each move (`references/library/`)
- **An edit-plan workflow:** a shared plan page with 3 playable design options per beat, your own-plan option, reference images, revisions to approve, then the render (`references/edit-plan-workflow.md`)
- **Building blocks:** HTML/GSAP templates for HyperFrames (HTML → video), an SVG shape kit, original paper textures and a Python edit pipeline (`assets/`)

## Install

**Claude Code**
```bash
git clone https://github.com/solomonosei883/arthur-brooks-style-skill ~/.claude/skills/arthurcbrooks
```
Start a new Claude Code session; the skill loads by itself when you ask for this style.

**Claude app (claude.ai / desktop)**
1. Click **Code → Download ZIP** on this page.
2. In Claude: **Settings → Capabilities → Skills → Upload skill**, and choose the ZIP.

## Use it

Ask Claude things like:
- "Edit this video in the Arthur Brooks style" (attach your talking-head clip)
- "Turn this script into a cinematic-text reel with blue paper cards"
- "Plan a 45-second reel about [topic] in this style, with a scene list"

For full edits from your own footage, Claude also uses: `ffmpeg`, Python 3, a word-level transcriber (e.g. Whisper) and HyperFrames for rendering. Planning and storyboards work without them.

## What's not included

The reference reels, clips and frame strips that the notes were measured from are **not** in this repo. The notes keep all the timing data, so the skill works without them. If you collect your own reference media, the layout is described in `SKILL.md`.

## Credits & license

Created by **@ond.finds**: [Telegram](https://t.me/OutlastNeverDie) · [Instagram](https://www.instagram.com/ond.finds/) · [TikTok](https://www.tiktok.com/@ond.finds). See `CREDITS.md`.

MIT License: free to use and adapt; keep the copyright and credit notice. If this helped you, **star the repo** and **[join the Telegram channel](https://t.me/OutlastNeverDie)**.
