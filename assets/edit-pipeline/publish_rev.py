"""Cut one revised clip per beat from a render of the edit and attach it to the plan page as "Revised vN".

Usage: python3 publish_rev.py <edit-render.mp4> <version>
Writes ../plan/rev/bNN-vN.mp4 + .jpg and sets beats[n].rev = {v, dur, what} in ../plan/plan-data.json and in the
data block embedded in ../plan/index.html. Notes come from tools/revision-notes.json (written by final.py).
"""
import json, os, re, subprocess, sys
import build as b

PLAN = os.path.join(b.ROOT, "plan")
OUT = os.path.join(PLAN, "rev")

def cut(src, t0, dur, name, poster_at):
    mp4 = os.path.join(OUT, name + ".mp4"); jpg = os.path.join(OUT, name + ".jpg")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{dur:.3f}",
                    "-vf", "scale=540:960:flags=lanczos", "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", mp4], check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t0 + poster_at:.3f}", "-i", src, "-frames:v", "1",
                    "-vf", "scale=300:533:flags=lanczos", "-q:v", "4", jpg], check=True)

def main():
    src, v = sys.argv[1], int(sys.argv[2])
    os.makedirs(OUT, exist_ok=True)
    notes = json.load(open(os.path.join(b.PROJ, "tools", "revision-notes.json")))
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                                 capture_output=True, text=True).stdout)
    revs = {}
    for n in range(1, 19):
        st = b.BEAT[n]["start"]; en = min(b.BEAT[n]["end"], total) if n < 18 else total
        cut(src, st, en - st, f"b{n:02d}-v{v}", max(0, en - st - 0.15))
        revs[n] = {"v": v, "dur": round(en - st, 2), "what": notes[str(n)]}
    data_path = os.path.join(PLAN, "plan-data.json")
    D = json.load(open(data_path))
    for bt in D["beats"]: bt["rev"] = revs[bt["n"]]
    json.dump(D, open(data_path, "w"), ensure_ascii=False)
    page = os.path.join(PLAN, "index.html"); h = open(page).read()
    m = re.search(r'(<script id="plan-data" type="application/json">)(.*?)(</script>)', h, re.S)
    E = json.loads(m.group(2))
    for bt in E["beats"]: bt["rev"] = revs[bt["n"]]
    blob = json.dumps(E, ensure_ascii=True).replace("</", "<\\/")
    h = h[:m.start(2)] + blob + h[m.end(2):]
    open(page, "w").write(h)
    print(f"revised v{v}: {len(revs)} clips in {OUT}")

if __name__ == "__main__":
    main()
