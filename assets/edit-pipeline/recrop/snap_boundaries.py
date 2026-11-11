"""Snap each shot boundary in crop.json to the real camera cut (largest frame difference within ±5 f).
Run after analyze.py, before render_locked2.py. Needs numpy + opencv-python-headless."""
import json, numpy as np, cv2
d = json.load(open("crop.json")); S = d["shots"]
cap = cv2.VideoCapture("land.mp4"); prev = None; dl = []
while True:
    ok, f = cap.read()
    if not ok: break
    g = cv2.cvtColor(cv2.resize(f, (480, 270)), cv2.COLOR_BGR2GRAY).astype(np.float32)
    dl.append(0.0 if prev is None else float(np.mean(np.abs(g - prev)))); prev = g
keys = sorted(S, key=int); starts = [S[k]["frames"][0] for k in keys]
new = [0] + [max(range(b - 5, b + 6), key=lambda i: dl[i]) for b in starts[1:]]
for k, (s0, s1) in zip(keys, zip(new, new[1:] + [len(dl)])): S[k]["frames"] = [s0, s1 - 1]
d["shots"] = S; json.dump(d, open("crop.json", "w")); print("shots:", {k: S[k]["frames"] for k in keys})
