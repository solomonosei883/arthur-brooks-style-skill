"""Cut one small preview clip (+ poster) per design option for the plan page.

A options come from a render of the edit (index.html); B and C from a render of ../previews (previews.json slots).
Usage: python3 cut_previews.py <edit-render.mp4> [<options-render.mp4>]
Writes ../plan/opts/bNNx.mp4 and bNNx.jpg (540x960).
"""
import json, os, subprocess, sys
import build as b

PLAN = os.path.join(b.ROOT, "plan")
OUT = os.path.join(PLAN, "opts")
os.makedirs(OUT, exist_ok=True)

def cut(src, t0, dur, name, poster_at):
    mp4 = os.path.join(OUT, name + ".mp4"); jpg = os.path.join(OUT, name + ".jpg")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{dur:.3f}",
                    "-vf", "scale=540:960:flags=lanczos", "-c:v", "libx264", "-preset", "slow", "-crf", "27", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", mp4], check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t0 + poster_at:.3f}", "-i", src, "-frames:v", "1",
                    "-vf", "scale=270:480:flags=lanczos", "-q:v", "4", jpg], check=True)

def main():
    edit = sys.argv[1]
    for n in range(1, 19):
        st = b.BEAT[n]["start"]; en = b.BEAT[n]["end"] if n < 18 else b.TOTAL
        cut(edit, st, en - st, f"b{n:02d}a", en - st - 0.15)
    if len(sys.argv) > 2:
        opts = sys.argv[2]
        d = json.load(open(os.path.join(os.path.dirname(b.ROOT), os.path.basename(b.ROOT), "previews", "previews.json")))
        for s in d["slots"]:
            n = s["beat"]; letter = s["opt"][-1].lower()
            cut(opts, s["start"], s["dur"], f"b{n:02d}{letter}", s["dur"] - 0.15)
    print("cut", len(os.listdir(OUT)) // 2, "options")

if __name__ == "__main__":
    main()
