import cv2, numpy as np, json, sys
# usage: python analyze.py <project>/cut_list.json <project>/edit/assets/aroll.mp4
C = json.load(open(sys.argv[1]))
fps = 24000 / 1001
AR = sys.argv[2]
SHOTS = [0.0, 61.75, 80.5, 89.5, 92.0, 105.0]; ZOOM = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.55, 4: 1.0}
# frame -> seg time -> shot
segt = []; joins = []; cum = 0.0
for a, b in C["segments"]:
    f0 = round(cum * fps); cum += b - a; f1 = round(cum * fps)
    joins.append(f0)
    for f in range(f0, f1): segt.append(a + (f / fps - (cum - (b - a))))
shot = [max(i for i in range(5) if SHOTS[i] <= t) for t in segt]
L = cv2.VideoCapture("land.mp4"); A = cv2.VideoCapture(AR)
dl, da, xs, ys, sc = [], [], [], [], []
pl = pa = None; i = 0
while True:
    ok1, fl = L.read(); ok2, fa = A.read()
    if not ok1 or not ok2: break
    gl = cv2.cvtColor(cv2.resize(fl, (480, 270), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY).astype(np.float32)
    ga = cv2.cvtColor(cv2.resize(fa, (270, 480), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY).astype(np.float32)
    dl.append(0 if pl is None else float(np.mean(np.abs(gl - pl)))); da.append(0 if pa is None else float(np.mean(np.abs(ga - pa))))
    pl, pa = gl, ga
    z = ZOOM[shot[i]]; tw, th = round(1080 * 9 / 16 / z / 4), round(1080 / z / 4)
    tmpl = cv2.resize(ga, (tw, th), interpolation=cv2.INTER_AREA)
    r = cv2.matchTemplate(gl, tmpl, cv2.TM_CCOEFF_NORMED); _, mx, _, loc = cv2.minMaxLoc(r)
    xs.append(loc[0] * 4); ys.append(loc[1] * 4); sc.append(mx); i += 1
print("frames", i, "min match", round(min(sc), 3), "mean match", round(float(np.mean(sc)), 3))
da = np.array(da); dl = np.array(dl)
for off in (-1, 0, 1):
    hits = 0
    for j in joins[1:]:
        jj = j + off
        if 3 <= jj < len(da) - 3:
            nb = np.median(np.r_[da[jj-3:jj], da[jj+1:jj+4]]); hits += da[jj] > 2.0 * nb + 0.5
    print("offset", off, "join spikes in aroll", hits, "of", len(joins) - 1)
res = {}
for s in range(5):
    idx = [k for k in range(i) if shot[k] == s]
    if not idx: continue
    xa = np.array([xs[k] for k in idx]); ya = np.array([ys[k] for k in idx])
    res[s] = dict(frames=[idx[0], idx[-1]], x_med=int(np.median(xa)), x_min=int(xa.min()), x_max=int(xa.max()), y_med=int(np.median(ya)), zoom=ZOOM[s])
    print("shot", s, res[s])
json.dump(dict(shots=res, xs=xs, ys=ys, shot=shot), open("crop.json", "w"))
