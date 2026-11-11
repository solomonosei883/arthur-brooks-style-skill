import json, subprocess, sys, numpy as np
fps = 24000 / 1001
# usage: python render_locked2.py <project>/cut_list.json
C = json.load(open(sys.argv[1]))
d = json.load(open("crop.json")); S = d["shots"]; xs = np.array(d["xs"]); ys = np.array(d["ys"])
joins = []; cum = 0.0
for a, b in C["segments"]:
    f0 = round(cum * fps); cum += b - a; joins.append(f0)
N = round(cum * fps)
cuts = sorted(set([0] + [v["frames"][0] for v in S.values()] + joins + [N]))
shot_of = lambda f: next(int(k) for k, v in S.items() if v["frames"][0] <= f <= v["frames"][1])
ranges = []
for a, b in zip(cuts, cuts[1:]):
    if b <= a: continue
    s = shot_of(a); z = S[str(s)]["zoom"]
    core = xs[a + (1 if b - a > 3 else 0): b - (1 if b - a > 3 else 0)]
    x = int(np.median(core)); y = int(np.median(ys[a:b])) if z != 1 else 0
    if ranges and ranges[-1]["shot"] == s and abs(ranges[-1]["x"] - x) < 40:
        ranges[-1]["b"] = b; continue          # same framing: stay locked across this jump cut
    ranges.append(dict(a=a, b=b, shot=s, x=x, y=y, z=z))
parts = []
for k, r in enumerate(ranges):
    w = 608 if r["z"] == 1 else 392; h = 1080 if r["z"] == 1 else 696
    x = max(0, min(1920 - w, r["x"])); y = max(0, min(1080 - h, r["y"]))
    out = f"r{k:02d}.mp4"
    vf = f"trim=start_frame={r['a']}:end_frame={r['b']},setpts=PTS-STARTPTS,crop={w}:{h}:{x}:{y},scale=1080:1920:flags=lanczos,setsar=1"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", "land.mp4", "-vf", vf, "-an", "-c:v", "libx264", "-crf", "8", "-preset", "veryfast", "-pix_fmt", "yuv420p", out], check=True)
    parts.append(f"file '{out}'"); print(f"frames {r['a']}-{r['b'] - 1} shot {r['shot']} crop x={x} y={y}")
open("ranges.txt", "w").write("\n".join(parts) + "\n")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", "ranges.txt", "-c", "copy", "locked_v.mp4"], check=True)
json.dump(ranges, open("ranges.json", "w"))
