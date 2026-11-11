import json, subprocess, sys, os
# usage: python extract.py <source_landscape.mp4> <project>/cut_list.json
SRC = sys.argv[1]
C = json.load(open(sys.argv[2]))
fps = 24000 / 1001; base = 5575.0
cum = 0.0; lst = []; total = 0
for k, (a, b) in enumerate(C["segments"]):
    f0 = round(cum * fps); cum += b - a; f1 = round(cum * fps); n = f1 - f0
    if n <= 0: continue
    out = f"segs/s{k:02d}.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{base + a:.4f}", "-i", SRC, "-frames:v", str(n), "-an",
                    "-vf", "fps=24000/1001", "-c:v", "libx264", "-crf", "8", "-preset", "veryfast", "-pix_fmt", "yuv420p", out], check=True)
    lst.append(f"file '{out}'"); total += n
open("list.txt", "w").write("\n".join(lst) + "\n")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "land.mp4"], check=True)
print("frames planned", total)
