"""Generate the career-patterns edit: compositions/sNN.html (18 beats) + index.html.

Inputs: ../plan/plan-data.json (beat windows) and ../transcript.json (word onsets, cut timeline).
Rules (arthurcbrooks skill): scene cut = first onset - 1 f; word pop = onset + 3 f (A-roll + 2 f), binary
opacity; pre-placed lockups; key ~120 px, helpers ~0.36x; power2.out moves; text exits on the cut.
"""
import json, os, html, math

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
ROOT = os.path.dirname(PROJ)
FPS = 24000 / 1001
F = 1 / FPS
T = json.load(open(os.path.join(ROOT, "transcript.json")))
W = {w["i"]: dict(w) for w in T["words"]}
W[81]["w"] = "Diego."
PLAN = json.load(open(os.path.join(ROOT, "plan", "plan-data.json")))
BEAT = {b["n"]: b for b in PLAN["beats"]}
AUDIO_END = round(T["duration"], 3)
END_HOLD = 1.5
TOTAL = round(AUDIO_END + END_HOLD, 3)

BLUE, NODE, AZURE, WHITE, INK, GREY, LGREY, BLACK, NAVY = (
    "#0844EA", "#2F6BF2", "#1E6AF1", "#FBF9FC", "#1A1A2E", "#5B6478", "#9AA3B8", "#000402", "#0B0C10")

def onset(i): return W[i]["start"]
def esc(s): return html.escape(s)

# ------------------------------------------------------------------ scene specs
# A scene is a list of segments. Each segment: bg + optional art + text phases.
# Phase slots: tl/tr/tc (above key), key, br/bl/bc (below key), sub (wrapping subtitle line).
def ph(**k): return k
SCENES = {
 1: [dict(bg="aroll", phases=[ph(tc=[1], key=[2], style="bold", bc=[3, 4, 5])])],
 2: [dict(bg="graph", art="stairs", phases=[ph(tl=[6], key=[7], style="serif", bc=[8, 9, 10, 11], y=.15),
                                            ph(sub=[24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], y=.15)])],
 3: [dict(bg="graph", art="zigzag", phases=[ph(tl=[35, 36], key=[37], style="serif", bc=[38, 39, 40, 41], y=.15),
                                            ph(tl=[42, 43], key=[44, 45], style="serif", br=[46, 47], y=.15)])],
 4: [dict(bg="bluerough", art="quote", phases=[ph(tc=[48, 49, 50, 51, 52], key=[53, 54, 55, 56], style="serif", br=[57])])],
 5: [dict(bg="broll", clip="barista", crop=(1.12, "50% 40%"), grade="warm", phases=[ph(tl=[61, 62, 63, 64, 65], key=[66], style="serif", y=.40)]),
     dict(bg="broll", clip="van", crop=(1.10, "50% 45%"), grade="cool", phases=[ph(tl=[67, 68], key=[69, 70], style="serif", y=.30)]),
     dict(bg="broll", clip="beach", crop=(1.08, "50% 55%"), grade="warm", phases=[ph(tc=[71, 72, 73, 74, 75, 76, 77, 78, 79], key=[80, 81], style="serif", y=.36)])],
 6: [dict(bg="graph", art="flat", phases=[ph(tl=[82, 83, 84, 85], key=[86], style="serif", y=.15),
                                          ph(tl=[87, 88, 89], key=[90, 91, 92], style="serif", y=.15)])],
 7: [dict(bg="aroll", art="hud42", phases=[ph(tl=[93, 94, 95, 96], key=[97, 98], style="serif", br=[99, 100, 101], y=.56)])],
 8: [dict(bg="whiterough", art="side", phases=[])],
 9: [dict(bg="painting", img="vangogh-postman-roulin", pos="50% 30%", phases=[ph(tl=[121, 122, 123, 124], key=[125, 126, 127], style="serif", y=.84)])],
 10: [dict(bg="aroll", phases=[ph(tl=[128, 129, 130, 131], key=[132], style="bold", br=[133, 134, 135, 136, 137])]),
      dict(bg="graph", art="spiral", phases=[ph(tl=[138], key=[139], style="serif", y=.15),
                                             ph(tl=[140, 141], key=[142, 143, 144], style="serif", br=[145], y=.15)])],
 11: [dict(bg="broll", clip="studs", crop=(1.06, "50% 50%"), grade="warm", phases=[ph(tc=[146, 147, 148, 149, 150, 151, 152, 153], key=[154, 155, 156, 157], style="serif", y=.50)]),
      dict(bg="broll", clip="saw", crop=(1.08, "50% 45%"), grade="warm", phases=[ph(tl=[158], key=[159, 160], style="serif", y=.30)])],
 12: [dict(bg="white", art="turnline", phases=[ph(tl=[161], key=[162, 163], style="serif", bc=[164, 165], y=.60)])],
 13: [dict(bg="whiterough", art="photo", phases=[ph(tl=[166, 167, 168, 169], key=[170, 171], style="serif", y=.15),
                                                 ph(tl=[172, 173, 174], key=[175], style="serif", y=.15),
                                                 ph(tl=[176, 177], key=[178], style="serif", y=.15)])],
 14: [dict(bg="painting", img="titian-sisyphus", pos="50% 50%", phases=[ph(tc=[179, 180, 181, 182, 183], key=[184], style="serif", y=.17)])],
 15: [dict(bg="white", art="turns", phases=[])],
 16: [dict(bg="aroll", phases=[ph(tl=[198, 199, 200, 201], key=[202, 203], style="serif")]),
      dict(bg="painting", img="watteau-pierrot", pos="50% 30%", phases=[ph(tl=[204, 205, 206], key=[207, 208], style="serif", y=.86)]),
      dict(bg="painting", img="maurer-american-fireman", pos="50% 40%", phases=[ph(tl=[209], key=[210], style="serif", y=.84)])],
 17: [dict(bg="black", art="disc", phases=[ph(sub=[211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222], y=.16),
                                           ph(tl=[223], key=[224, 225], style="serif", y=.16),
                                           ph(tl=[226, 227, 228, 229], key=[230], style="serif", y=.16)])],
 18: [dict(bg="aroll", phases=[ph(tl=[231, 232, 233, 234], key=[235], style="serif"),
                               ph(tl=[236, 237], key=[238], style="serif")]),
      dict(bg="bluerough", art="endcard", phases=[ph(tc=[239, 240, 241, 242, 243], key=[244, 245, 246, 247], style="serif")])],
}
DEFAULT_Y = {"aroll": .58, "broll": .50, "painting": .80, "graph": .15, "bluerough": .50, "blue": .50,
             "white": .50, "whiterough": .50, "black": .50}
LIGHT_BG = {"white", "whiterough"}
LAG = {"aroll": 2, "aroll_zoom": 2}
DEFAULT_Y["aroll_zoom"] = .58

def pop(t, t0, t1):
    """Word pop time: onset + lag, but never later than 5 frames before the cut, never before the scene's 2nd frame."""
    return max(t0 + 2 * F, min(t, t1 - 5 * F))

def phase_words(p):
    return [i for s in ("tl", "tr", "tc", "key", "br", "bl", "bc", "sub") for i in p.get(s, [])]

# ------------------------------------------------------------------ text
def est_width(text, size, style):
    return len(text) * size * {"serif": 0.47, "bold": 0.60, "helper": 0.52}[style]

def lockup(sid, p, pid, color, hcolor, top):
    style = p.get("style", "serif")
    disp = p.get("disp", {})
    def wt(i): return disp.get(i, W[i]["w"])
    key_ids = p.get("key", [])
    key_text = " ".join(wt(i) for i in key_ids)
    size = p.get("size", 120)
    if "size" not in p and "kw" not in p:
        while key_ids and est_width(key_text, size, style) > 900 and size > 64: size -= 4
    hsize = p.get("hs") or ((round(size * 0.36) if size >= 100 else 40) if "size" not in p else min(64, round(size * 0.36)))
    def words(ids, ghost=False):
        c = "w ghost" if ghost else "w"
        return " ".join(f'<span class="{c}" id="{sid}-{pid}-w{i}">{esc(wt(i))}</span>' for i in ids)
    hc = f";color:{hcolor}" if hcolor else ""
    if p.get("sub"):
        body = f'<span class="sub" style="max-width:900px{hc}">{words(p["sub"])}</span>'
    else:
        kw = est_width(key_text, size, style)
        parts = []
        for slot in ("tl", "tr", "tc", "br", "bl", "bc"):
            ids = p.get(slot)
            if not ids: continue
            text = " ".join(wt(i) for i in ids); s = slot
            if not p.get("hw") and slot in ("tl", "tr") and est_width(text, hsize, "helper") > 0.92 * kw: s = "tc"
            if not p.get("hw") and slot in ("br", "bl") and est_width(text, hsize, "helper") > 0.92 * kw: s = "bc"
            hwst = f";white-space:normal;width:{p['hw']}px;line-height:1.12" if p.get("hw") else ""
            parts.append(f'<span class="helper slot-{s}" style="font-size:{hsize}px{hc}{hwst}">{words(ids, p.get("ghost"))}</span>')
        kc = "key-serif" if style == "serif" else "key-bold"
        box = f'<span class="kbox" id="{sid}-{pid}-box"></span>' if p.get("box") else ""
        kst = f"font-size:{size}px" + (";position:relative;isolation:isolate;padding:0 .08em" if box else "") + (";font-variant-numeric:lining-nums" if p.get("lining") else "") \
            + (f";white-space:normal;max-width:{p['kw']}px;line-height:.86" if p.get("kw") else "") + (f";color:{p['kc']}" if p.get("kc") else "")
        body = f'<span class="lockup">{"".join(parts)}<span class="key {kc}" style="{kst}">{box}{words(key_ids)}</span></span>'
    lx, rx, al = p.get("lx", 80), p.get("rx", 80), p.get("align", "center")
    place = (f';left:{lx}px' if lx != 80 else "") + (f';right:{rx}px' if rx != 80 else "") + \
        ({"left": ";justify-content:flex-start;text-align:left", "right": ";justify-content:flex-end;text-align:right"}.get(al, ""))
    return f'<div class="lockup-wrap" id="{sid}-lk{pid}" style="top:{top - 300}px;height:600px;color:{color}{place}">{body}</div>'

# ------------------------------------------------------------------ CSS
FONTS = """
@font-face { font-family: "ABSans"; font-weight: 500; src: url("assets/fonts/inter-latin-500-normal.woff2") format("woff2"); }
@font-face { font-family: "ABSans"; font-weight: 600; src: url("assets/fonts/inter-latin-600-normal.woff2") format("woff2"); }
@font-face { font-family: "ABSans"; font-weight: 800; src: url("assets/fonts/inter-latin-800-normal.woff2") format("woff2"); }
@font-face { font-family: "ABSerif"; font-weight: 700; font-style: italic; src: url("assets/fonts/playfair-display-latin-700-italic.woff2") format("woff2"); }
@font-face { font-family: "ABSerif"; font-weight: 400; font-style: italic; src: url("assets/fonts/playfair-display-latin-400-italic.woff2") format("woff2"); }
"""
CSS = """
#root { position: absolute; inset: 0; overflow: hidden; color: #FFFFFF; font-family: "ABSans", sans-serif; }
#root .seg { position: absolute; inset: 0; overflow: hidden; }
#root .bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
#root .bg-white { background-color: #FBF9FC; background-image: url("assets/textures/paper-white.jpg"); }
#root .bg-whiterough { background-color: #ECE9E5; background-image: url("assets/textures/paper-white-rough.jpg"); }
#root .bg-blue { background-color: #0844EA; background-image: url("assets/textures/paper-blue.jpg"); }
#root .bg-bluerough { background-color: #0844EA; background-image: url("assets/textures/paper-blue-rough.jpg"); }
#root .bg-black { background-color: #000402; background-image: url("assets/textures/paper-black.jpg"); }
#root .bg-graph { background-color: #0B0C10; background-image: url("assets/textures/paper-black.jpg"); }
#root .grain { position: absolute; inset: 0; background-image: url("assets/textures/grain-tile-512.png"); mix-blend-mode: overlay; opacity: .30; pointer-events: none; }
#root .vignette { position: absolute; inset: 0; background-image: url("assets/textures/vignette.png"); background-size: cover; pointer-events: none; }
#root .scrim { position: absolute; left: 0; right: 0; height: 640px; pointer-events: none;
  background: radial-gradient(ellipse 64% 50% at 50% 50%, rgba(0,4,2,.62) 0%, rgba(0,4,2,.34) 45%, rgba(0,4,2,0) 100%); }
#root .lockup-wrap { position: absolute; left: 80px; right: 80px; display: flex; justify-content: center; align-items: center; text-align: center; }
#root .lockup { position: relative; display: inline-block; line-height: .9; }
#root .key { display: inline-block; white-space: nowrap; }
#root .key-serif { font-family: "ABSerif", serif; font-style: italic; font-weight: 700; letter-spacing: -0.02em; }
#root .key-bold { font-family: "ABSans", sans-serif; font-weight: 800; letter-spacing: -0.03em; }
#root .helper { font-family: "ABSans", sans-serif; font-weight: 500; letter-spacing: -0.01em; line-height: 1; white-space: nowrap; position: absolute; }
#root .slot-tl { left: 3%; bottom: 100%; margin-bottom: -0.12em; }
#root .slot-tr { right: 2%; bottom: 100%; margin-bottom: -0.12em; }
#root .slot-tc { left: 50%; bottom: 100%; margin-bottom: -0.12em; transform: translateX(-50%); }
#root .slot-br { right: 2%; top: 100%; margin-top: 0.05em; }
#root .slot-bl { left: 3%; top: 100%; margin-top: 0.05em; }
#root .slot-bc { left: 50%; top: 100%; margin-top: 0.15em; transform: translateX(-50%); }
#root .sub { font-family: "ABSans", sans-serif; font-weight: 500; font-size: 46px; line-height: 1.25; }
#root .w { opacity: 0; }
#root .w.ghost { opacity: .15; }
#root .kbox { position: absolute; left: -.06em; right: -.16em; top: .1em; bottom: .02em; background: #0844EA; z-index: 0; transform-origin: 0 50%; transform: scaleX(0); }
#root .kbox ~ .w { position: relative; z-index: 1; }
#root .media { position: absolute; inset: 0; overflow: hidden; }
#root .media .cam { position: absolute; inset: 0; will-change: transform; }
#root .media video, #root .media img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
#root .quote-mark { position: absolute; font-family: "ABSerif", serif; font-style: italic; font-weight: 700; font-size: 220px; line-height: 1; }
#root .cap { position: absolute; font-family: "ABSans", sans-serif; font-weight: 600; font-size: 26px; letter-spacing: .12em; text-transform: uppercase; white-space: nowrap; }
#root .lbl-serif { position: absolute; font-family: "ABSerif", serif; font-style: italic; font-weight: 700; white-space: nowrap; }
#root .lbl-sans { position: absolute; font-family: "ABSans", sans-serif; font-weight: 500; white-space: nowrap; }
"""

FIGURE = ("M38 44 Q50 52 62 44 L74 52 Q83 58 83 74 L88 142 Q88 150 81 150 L79 152 L77 252 L59 252 L54 162 "
          "L46 162 L41 252 L23 252 L21 152 L19 150 Q12 150 12 142 L17 74 Q17 58 26 52 Z")
SEATED = ("M50 2 C62 2 70 11 70 23 C70 35 62 44 50 44 C38 44 30 35 30 23 C30 11 38 2 50 2 Z "
          "M28 52 Q50 46 72 52 Q84 58 86 76 L92 136 L140 140 Q156 142 156 158 L156 222 L136 222 L132 168 L74 168 Q56 168 50 152 L22 150 Q12 148 12 136 L16 76 Q18 58 28 52 Z")
def rough_filter(sid):
    return (f'<filter id="{sid}-rough" filterUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1920">'
            f'<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="7" result="n"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G" result="d"/>'
            f'<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="s"/>'
            f'<feColorMatrix in="s" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -3.2 2.55" result="sa"/>'
            f'<feComposite in="d" in2="sa" operator="in"/></filter>'
            f'<filter id="{sid}-glow" filterUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1920"><feGaussianBlur stdDeviation="7" result="b"/>'
            f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
def figure(sid, x, ybase, h, color, path=FIGURE, w0=100, h0=260):
    s = h / h0
    # filter on an unscaled parent so displacement/noise stay at frame scale whatever the figure size
    return (f'<g filter="url(#{sid}-rough)"><g transform="translate({x - w0 / 2 * s:.1f},{ybase - h:.1f}) scale({s:.4f})">'
            + (f'<circle cx="50" cy="22" r="19" fill="{color}"/>' if path is FIGURE else "") + f'<path d="{path}" fill="{color}"/></g></g>')

# ------------------------------------------------------------------ career map (graph scenes)
def stairs_pts():
    x0, y0, x1, y1, n = 150, 1500, 940, 640, 6
    pts = [(x0, y0)]; dx = (x1 - x0) / n; dy = (y0 - y1) / n
    for k in range(n):
        x, y = pts[-1]; pts += [(x, y - dy), (x + dx, y - dy)]
    return pts
ZIG = [(120, 1320), (260, 800), (400, 1260), (540, 740), (680, 1220), (820, 780), (960, 1180)]
def flat_pts(): return [(110, 1080), (970, 1080)]
def spiral_pts(cx=540, cy=1080, turns=3.2, r1=390, n=260):
    out = []
    for k in range(n + 1):
        t = k / n; a = t * turns * 2 * math.pi; r = 12 + (r1 - 12) * t
        out.append((cx + r * math.cos(a - math.pi / 2), cy + r * math.sin(a - math.pi / 2)))
    return out
def path_d(pts): return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
MINI = [("No.1", "linear", "stairs"), ("No.2", "transitory", "zigzag"), ("No.3", "expert", "flat"), ("No.4", "spiral", "spiral")]
def mini_shape(kind, x, y, w, h):
    def fit(pts):
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        sx = w / max(1, max(xs) - min(xs)); sy = h / max(1, max(ys) - min(ys)); s = min(sx, sy)
        ox = x + (w - (max(xs) - min(xs)) * s) / 2; oy = y + (h - (max(ys) - min(ys)) * s) / 2
        return [(ox + (px - min(xs)) * s, oy + (py - min(ys)) * s) for px, py in pts]
    pts = {"stairs": stairs_pts(), "zigzag": ZIG, "flat": [(0, 0), (10, 0)], "spiral": spiral_pts(0, 0, 3.2, 100, 120)}[kind]
    if kind == "flat": return path_d([(x, y + h / 2), (x + w, y + h / 2)])
    return path_d(fit(pts))
def graph_layers(sid, cur, start, dur, kind_js):
    # grid + mini legend; returns (svg_markup, js)
    grid = "".join(f'<line x1="0" y1="{y}" x2="1080" y2="{y}"/>' for y in range(480, 1501, 120)) + \
           "".join(f'<line x1="{x}" y1="480" x2="{x}" y2="1500"/>' for x in range(120, 1000, 120))
    cells = []
    for k, (no, name, kind) in enumerate(MINI):
        x = 60 + k * 245; y = 1600
        if k < cur: op, col, dash = .45, "#FFFFFF", ""
        elif k == cur: op, col, dash = 1, AZURE, ""
        else: op, col, dash = .35, "#FFFFFF", 'stroke-dasharray="6 8"'
        inner = f'<path d="{mini_shape(kind, x + 24, y + 22, 166, 70)}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if k <= cur else ""
        cells.append(f'<g opacity="{op}" id="{sid}-mini{k}"><rect x="{x}" y="{y}" width="214" height="114" rx="12" fill="none" stroke="{col}" stroke-width="2" {dash}/>{inner}'
                     f'<text x="{x + 4}" y="{y + 152}" font-family="ABSerif" font-style="italic" font-weight="700" font-size="34" fill="{col}">{no}</text>'
                     f'<text x="{x + 4}" y="{y + 186}" font-family="ABSans" font-weight="600" font-size="20" letter-spacing="2" fill="{col}">{name.upper()}</text></g>')
    svg = (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
           f'<defs>{rough_filter(sid)}<radialGradient id="{sid}-ballg"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#9CC2FF"/>'
           f'<stop offset=".6" stop-color="{AZURE}" stop-opacity=".9"/><stop offset="1" stop-color="{AZURE}" stop-opacity="0"/></radialGradient></defs>'
           f'<g stroke="#FFFFFF" stroke-opacity=".09" stroke-width="2">{grid}</g>{"".join(cells)}'
           f'<g id="{sid}-pan"><g id="{sid}-world">' + "{SHAPE}" + '</g></g></svg>')
    js = f'tl.fromTo("#{sid}-mini{cur}", {{ opacity: 0.2 }}, {{ opacity: 1, duration: {10 * F:.3f}, ease: "power2.out" }}, 0);'
    return svg, js
def driven_line(sid, pts, schedule, ghost=None):
    """schedule: list of (t, frac_from, frac_to, dur, ease) ; line drawn progressively, ball at the tip."""
    d = path_d(pts)
    shape = (f'<path id="{sid}-line" d="{d}" fill="none" stroke="{AZURE}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round" filter="url(#{sid}-glow)"/>'
             f'<circle id="{sid}-ball" cx="0" cy="0" r="34" fill="url(#{sid}-ballg)"/>')
    js = [f"""const {sid}_p = document.getElementById("{sid}-line"), {sid}_b = document.getElementById("{sid}-ball"), {sid}_L = {sid}_p.getTotalLength();
{sid}_p.style.strokeDasharray = {sid}_L; {sid}_p.style.strokeDashoffset = {sid}_L;
const {sid}_s = {{ f: 0 }};
const {sid}_set = () => {{ const L = {sid}_L * {sid}_s.f; {sid}_p.style.strokeDashoffset = {sid}_L - L; const q = {sid}_p.getPointAtLength(Math.max(0.01, L)); {sid}_b.setAttribute("cx", q.x); {sid}_b.setAttribute("cy", q.y); }};
{sid}_set();"""]
    for t, f0, f1, dur, ease in schedule:
        js.append(f'tl.fromTo({sid}_s, {{ f: {f0:.4f} }}, {{ f: {f1:.4f}, duration: {dur:.3f}, ease: "{ease}", onUpdate: {sid}_set, immediateRender: false }}, {max(0, t):.3f});')
    return shape, "\n".join(js)

def art_graph(sid, kind, start, dur):
    cur = {"stairs": 0, "zigzag": 1, "flat": 2, "spiral": 3}[kind]
    svg, js = graph_layers(sid, cur, start, dur, None)
    loc = lambda i: onset(i) - start
    if kind == "stairs":
        pts = stairs_pts(); n = 6; ups = [13, 15, 17, 19, 21, 23]
        ts = [loc(u) + 1 * F for u in ups] + [loc(24)]
        sched = [(ts[k], (2 * k) / (2 * n), (2 * k + 2) / (2 * n), min(10 * F, ts[k + 1] - ts[k] - 0.002), "power2.out") for k in range(n)]
    elif kind == "zigzag":
        pts = ZIG; hops = [42, 43, 44, 45, 46, 47]; n = len(pts) - 1
        L = [math.dist(pts[k], pts[k + 1]) for k in range(n)]; tot = sum(L); cum = [sum(L[:k]) / tot for k in range(n + 1)]
        ts = [loc(h) + 1 * F for h in hops] + [dur]
        sched = [(ts[k], cum[k], cum[k + 1], min(7 * F, ts[k + 1] - ts[k] - 0.002), "power2.out") for k in range(n)]
    elif kind == "flat":
        pts = flat_pts(); sched = [(6 * F, 0, 1, dur - 12 * F, "none")]
    else:
        pts = spiral_pts(); sched = [(4 * F, 0, 1, min(2.9, dur - 8 * F), "sine.inOut")]
    shape, ljs = driven_line(sid, pts, sched)
    dots = ""
    if kind == "zigzag":
        dots = "".join(f'<circle class="{sid}-dot" id="{sid}-dot{k}" cx="{x}" cy="{y}" r="14" fill="#FFFFFF" opacity="{1 if k == 0 else 0}"/>' for k, (x, y) in enumerate(ZIG))
        for k, i in enumerate([42, 43, 44, 45, 46, 47]):
            ljs += f'\ntl.set("#{sid}-dot{k + 1}", {{ opacity: 1 }}, {loc(i) + 8 * F:.3f});'
    if kind == "flat":
        ticks = "".join(f'<line x1="{x}" y1="1110" x2="{x}" y2="1130" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="3"/>' for x in range(110, 980, 86))
        dots = ticks
    if kind == "stairs":  # camera tilts up with the climb
        ljs += f'\ntl.fromTo("#{sid}-pan", {{ y: -40 }}, {{ y: 40, duration: {loc(23) + 0.5:.3f}, ease: "power1.inOut" }}, 0);'
    return svg.replace("{SHAPE}", dots + shape), js + "\n" + ljs

# ------------------------------------------------------------------ other art
def art_hud42(sid, start, dur):
    t42 = onset(100) - start
    ticks = "".join(f'<line x1="{140 + k * 160}" y1="1648" x2="{140 + k * 160}" y2="1672" stroke="#FFFFFF" stroke-width="3"/>'
                    f'<text x="{140 + k * 160}" y="1712" text-anchor="middle" font-family="ABSans" font-weight="600" font-size="24" fill="#FFFFFF" opacity=".8">{k * 10}</text>' for k in range(6))
    mk = (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
          f'<line id="{sid}-hl" x1="140" y1="1660" x2="940" y2="1660" stroke="#FFFFFF" stroke-width="3" pathLength="1000"/>{ticks}'
          f'<line id="{sid}-fill" x1="140" y1="1660" x2="812" y2="1660" stroke="{AZURE}" stroke-width="9" stroke-linecap="round" pathLength="1000"/>'
          f'<circle id="{sid}-dot" cx="140" cy="1660" r="15" fill="#FFFFFF"/></svg>'
          f'<div class="cap" id="{sid}-yrs" style="left:0;top:1580px;color:#FFFFFF">0 YEARS</div>')
    js = f"""tl.fromTo("#{sid}-hl", {{ strokeDasharray: 1000, strokeDashoffset: 1000 }}, {{ strokeDashoffset: 0, duration: {10 * F:.3f}, ease: "power2.out" }}, 0);
const {sid}_c = {{ v: 0 }}; const {sid}_f = document.getElementById("{sid}-fill"), {sid}_d = document.getElementById("{sid}-dot"), {sid}_y = document.getElementById("{sid}-yrs");
const {sid}_set = () => {{ const v = {sid}_c.v, x = 140 + v * 16; {sid}_f.setAttribute("x2", x.toFixed(1)); {sid}_d.setAttribute("cx", x.toFixed(1)); {sid}_y.style.left = (x - 70).toFixed(1) + "px"; {sid}_y.textContent = Math.round(v) + " YEARS"; }};
{sid}_set();
tl.fromTo({sid}_c, {{ v: 0 }}, {{ v: 42, duration: {max(0.4, t42 - 0.15):.3f}, ease: "power2.out", onUpdate: {sid}_set, immediateRender: false }}, {6 * F:.3f});"""
    return mk, js

def art_side(sid, start, dur):
    loc = lambda i: onset(i) - start
    def w(i, cls=""): return f'<span class="w" id="{sid}-s-w{i}">{esc(W[i]["w"])}</span>'
    mk = (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
          f'<defs>{rough_filter(sid)}<radialGradient id="{sid}-g" cx="0" cy=".5" r=".9"><stop offset="0" stop-color="{AZURE}" stop-opacity=".85"/><stop offset="1" stop-color="{AZURE}" stop-opacity="0"/></radialGradient></defs>'
          f'<g id="{sid}-half"><path d="M0 560 A 440 440 0 0 1 0 1440 Z" fill="url(#{sid}-g)"/><path d="M0 500 A 500 500 0 0 1 0 1500" fill="none" stroke="{GREY}" stroke-width="3"/></g>'
          f'<g id="{sid}-fig">{figure(sid, 200, 1330, 600, BLUE)}</g></svg>'
          f'<div class="lbl-sans" style="left:500px;top:560px;width:500px;white-space:normal;font-size:40px;line-height:1.2;color:{INK}">{" ".join(w(i) for i in range(102, 109))}</div>'
          f'<div class="lbl-serif" style="left:496px;top:700px;font-size:132px;color:{BLUE}">{w(109)}</div>'
          f'<div class="lbl-sans" style="left:500px;top:900px;font-size:40px;color:{INK}">{" ".join(w(i) for i in (110, 111, 112))}</div>'
          f'<div class="lbl-serif" style="left:496px;top:950px;font-size:98px;color:{BLUE}">{w(113)} {w(114)}</div>'
          f'<div class="lbl-sans" style="left:500px;top:1110px;width:500px;white-space:normal;font-size:40px;line-height:1.2;color:{INK}">{" ".join(w(i) for i in range(115, 121))}</div>')
    js = [f'tl.fromTo("#{sid}-half", {{ x: -300, opacity: 0 }}, {{ x: 0, opacity: 1, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);',
          f'tl.fromTo("#{sid}-fig", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: {16 * F:.3f}, ease: "power2.out" }}, {3 * F:.3f});']
    for i in range(102, 121):
        js.append(f'tl.set("#{sid}-s-w{i}", {{ opacity: 1 }}, {pop(loc(i) + 3 * F, 0, dur):.3f});')
    return mk, "\n".join(js)

def art_turnline(sid, start, dur):
    mk = (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
          f'<path id="{sid}-ln" d="M 230 1990 L 230 1080 Q 230 880 430 880 L 1150 880" fill="none" stroke="{AZURE}" stroke-width="80" stroke-linejoin="round" pathLength="1000"/></svg>')
    js = f'tl.fromTo("#{sid}-ln", {{ strokeDasharray: 1000, strokeDashoffset: 1000 }}, {{ strokeDashoffset: 0, duration: {16 * F:.3f}, ease: "power2.out" }}, 0);'
    return mk, js

def art_photo(sid, start, dur):
    tb = onset(173) - start
    mk = (f'<div id="{sid}-card" style="position:absolute;left:250px;top:560px;width:580px;height:740px;background:#FFFFFF;padding:16px;box-shadow:0 18px 42px rgba(0,0,0,.28)">'
          f'<img src="assets/art/brooks-2017-gage-skidmore.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 20%;display:block" alt=""></div>'
          f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
          f'<line x1="140" y1="1470" x2="940" y2="1470" stroke="{LGREY}" stroke-width="3"/>'
          f'<line x1="260" y1="1452" x2="260" y2="1488" stroke="{LGREY}" stroke-width="3"/><line x1="820" y1="1452" x2="820" y2="1488" stroke="{LGREY}" stroke-width="3"/>'
          f'<rect id="{sid}-mk" x="200" y="1462" width="120" height="16" fill="{BLUE}"/></svg>'
          f'<div class="cap" id="{sid}-l1" style="left:110px;top:1510px;width:300px;text-align:center;color:{BLUE}">French horn</div>'
          f'<div class="cap" id="{sid}-l2" style="left:670px;top:1510px;width:300px;text-align:center;color:{GREY}">Scientist</div>'
          f'<div class="lbl-sans" style="left:0;right:0;top:1820px;text-align:center;font-size:22px;color:{GREY}">Photo: Gage Skidmore, CC BY-SA 3.0</div>')
    js = f"""tl.fromTo("#{sid}-card", {{ y: 240, rotation: -12, opacity: 0 }}, {{ y: 0, rotation: -3, opacity: 1, duration: {22 * F:.3f}, ease: "power2.out" }}, 0);
tl.fromTo("#{sid}-card", {{ scale: 1 }}, {{ scale: 1.04, duration: {dur:.3f}, ease: "none", immediateRender: false }}, {22 * F:.3f});
tl.fromTo("#{sid}-mk", {{ x: 0 }}, {{ x: 560, duration: {20 * F:.3f}, ease: "power2.inOut" }}, {max(0.3, tb):.3f});
tl.fromTo("#{sid}-l1", {{ color: "{BLUE}" }}, {{ color: "{GREY}", duration: {4 * F:.3f}, ease: "none" }}, {max(0.3, tb) + 10 * F:.3f});
tl.fromTo("#{sid}-l2", {{ color: "{GREY}" }}, {{ color: "{BLUE}", duration: {4 * F:.3f}, ease: "none" }}, {max(0.3, tb) + 14 * F:.3f});"""
    return mk, js

def art_turns(sid, start, dur):
    loc = lambda i: onset(i) - start
    pts = [(-60, 340), (300, 640), (800, 1260), (330, 1990), (330, 2160)]
    d = f"M -60 340 C 120 420 260 520 300 640 C 360 860 760 1000 800 1260 C 840 1520 380 1700 330 1990"
    def w(i): return f'<span class="w" id="{sid}-t-w{i}">{esc(W[i]["w"])}</span>'
    nodes = [(300, 640), (800, 1260), (330, 1990)]
    mk = (f'<div id="{sid}-world" style="position:absolute;left:0;top:0;width:1080px;height:2900px">'
          f'<svg viewBox="0 0 1080 2900" width="1080" height="2900" style="position:absolute;inset:0" data-layout-ignore>'
          f'<path id="{sid}-ln" d="{d}" fill="none" stroke="{AZURE}" stroke-width="22" stroke-linecap="round" pathLength="1000"/>'
          + "".join(f'<circle id="{sid}-n{k}" cx="{x}" cy="{y}" r="22" fill="{BLUE}"/>' for k, (x, y) in enumerate(nodes)) +
          f'<circle id="{sid}-ring" cx="330" cy="2200" r="186" fill="none" stroke="{BLUE}" stroke-width="6" pathLength="1000"/></svg>'
          f'<div class="lbl-sans" style="left:360px;top:540px;font-size:44px;color:{INK}">{w(185)} {w(186)}</div>'
          f'<div class="lbl-serif" style="left:356px;top:598px;font-size:118px;color:{BLUE}">{w(187)}</div>'
          f'<div class="lbl-sans" style="left:330px;top:1160px;width:420px;text-align:right;font-size:44px;color:{INK}">{w(188)} {w(189)}</div>'
          f'<div class="lbl-serif" style="left:260px;top:1218px;width:500px;text-align:right;font-size:118px;color:{BLUE}">{w(190)}</div>'
          f'<div id="{sid}-ph" style="position:absolute;left:160px;top:2030px;width:340px;height:340px;border-radius:50%;overflow:hidden">'
          f'<img id="{sid}-face" src="assets/art/brooks-2022-face-bw.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" alt=""></div>'
          f'<div class="lbl-sans" style="left:548px;top:2070px;font-size:42px;color:{INK}">{w(191)} {w(192)} {w(193)}</div>'
          f'<div class="lbl-serif" style="left:544px;top:2120px;font-size:88px;color:{BLUE}">{w(194)} {w(195)}</div>'
          f'<div class="lbl-sans" style="left:548px;top:2236px;font-size:42px;color:{INK}">{w(196)} {w(197)}</div>'
          f'<div class="lbl-sans" style="left:160px;top:2400px;font-size:20px;color:{GREY}">Photo: Dshipleyray, CC BY-SA 4.0</div>'
          f'</div>')
    t1, t2, t3 = loc(185), loc(188), loc(191)
    js = [f'tl.fromTo("#{sid}-ln", {{ strokeDasharray: 1000, strokeDashoffset: 1000 }}, {{ strokeDashoffset: 760, duration: {12 * F:.3f}, ease: "power2.out" }}, 0);',
          f'tl.to("#{sid}-ln", {{ strokeDashoffset: 380, duration: {16 * F:.3f}, ease: "power2.inOut" }}, {max(0.2, t2 - 10 * F):.3f});',
          f'tl.to("#{sid}-ln", {{ strokeDashoffset: 0, duration: {16 * F:.3f}, ease: "power2.inOut" }}, {max(0.4, t3 - 12 * F):.3f});',
          f'tl.fromTo("#{sid}-world", {{ y: 0 }}, {{ y: -420, duration: {18 * F:.3f}, ease: "power2.inOut" }}, {max(0.2, t2 - 12 * F):.3f});',
          f'tl.to("#{sid}-world", {{ y: -1000, duration: {18 * F:.3f}, ease: "power2.inOut" }}, {max(0.4, t3 - 14 * F):.3f});',
          f'tl.fromTo("#{sid}-ph", {{ scale: .6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: {14 * F:.3f}, ease: "power2.out" }}, {max(0.4, t3 - 4 * F):.3f});',
          f'tl.fromTo("#{sid}-ring", {{ strokeDasharray: 1000, strokeDashoffset: 1000, rotation: -90, transformOrigin: "50% 50%" }}, {{ strokeDashoffset: 0, duration: {18 * F:.3f}, ease: "power2.out" }}, {max(0.4, t3):.3f});']
    for k, t in enumerate([t1, t2, t3]):
        js.append(f'tl.fromTo("#{sid}-n{k}", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {max(0, t - 2 * F):.3f});')
    for i in range(185, 198):
        js.append(f'tl.set("#{sid}-t-w{i}", {{ opacity: 1 }}, {pop(loc(i) + 3 * F, 0, dur):.3f});')
    return mk, "\n".join(js)

def art_disc(sid, start, dur):
    mk = (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0" data-layout-ignore>'
          f'<defs>{rough_filter(sid)}<radialGradient id="{sid}-dg"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#FFFFFF" stop-opacity=".95"/>'
          f'<stop offset=".72" stop-color="#FFFFFF" stop-opacity=".25"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient></defs>'
          f'<g id="{sid}-disc"><circle cx="540" cy="1230" r="430" fill="url(#{sid}-dg)"/></g>'
          f'<circle id="{sid}-ring" cx="540" cy="1230" r="470" fill="none" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="3" pathLength="1000"/>'
          f'<g id="{sid}-fig">{figure(sid, 540, 1920, 980, AZURE)}</g></svg>')
    js = f"""tl.fromTo("#{sid}-disc", {{ y: 260, opacity: 0 }}, {{ y: 0, opacity: 1, duration: {24 * F:.3f}, ease: "power2.out" }}, 0);
tl.fromTo("#{sid}-fig", {{ y: 240 }}, {{ y: 0, duration: {22 * F:.3f}, ease: "power2.out" }}, {3 * F:.3f});
tl.fromTo("#{sid}-ring", {{ strokeDasharray: 1000, strokeDashoffset: 1000, rotation: -90, transformOrigin: "50% 50%" }}, {{ strokeDashoffset: 0, duration: {30 * F:.3f}, ease: "power2.out" }}, {12 * F:.3f});
tl.fromTo("#{sid}-fig", {{ scale: 1, transformOrigin: "50% 100%" }}, {{ scale: 0.9, duration: {max(0.5, dur - 22 * F):.3f}, ease: "none", immediateRender: false }}, {22 * F:.3f});
tl.fromTo("#{sid}-disc", {{ scale: 1, transformOrigin: "50% 64%" }}, {{ scale: 1.08, duration: {max(0.5, dur - 24 * F):.3f}, ease: "none", immediateRender: false }}, {24 * F:.3f});"""
    return mk, js

GRADES = {k: html.escape(json.dumps(v, separators=(",", ":"))) for k, v in {
    "warm": {"preset": "muted-editorial", "intensity": 0.7, "details": {"vignette": 0.18, "grain": 0.1, "grainSize": 0.22}},
    "cool": {"preset": "muted-editorial", "intensity": 0.75, "details": {"vignette": 0.18, "grain": 0.1, "grainSize": 0.22}},
    "painting": {"preset": "neutral", "intensity": 1, "details": {"vignette": 0.14, "grain": 0.08, "grainSize": 0.2}},
    "mono": {"preset": "mono-clean", "intensity": 1},
    "monofade": {"preset": "mono-fade", "intensity": 1, "details": {"vignette": 0.12, "grain": 0.06}},
    "paint": {"preset": "neutral", "intensity": 1, "details": {"vignette": 0.38, "grain": 0.2, "grainSize": 0.32, "grainRoughness": 0.7},
              "effects": {"kuwahara": 0.55, "kuwaharaRadius": 0.12}},
    "paint2": {"preset": "neutral", "intensity": 1, "adjust": {"exposure": -0.12, "contrast": 0.1, "saturation": -0.18},
               "details": {"vignette": 0.55, "grain": 0.35, "grainSize": 0.45, "grainRoughness": 0.85},
               "effects": {"kuwahara": 0.7, "kuwaharaRadius": 0.14, "kuwaharaSharpness": 0.45}},
    "dark": {"preset": "muted-editorial", "intensity": 0.85, "adjust": {"exposure": -0.75, "contrast": 0.25, "highlights": -0.3, "saturation": -0.4},
             "details": {"vignette": 0.5, "grain": 0.12, "grainSize": 0.24}},
}.items()}

# ------------------------------------------------------------------ scene builder
ART_FNS = {
    "hud42": lambda sid, s, d, sg: art_hud42(sid, s, d), "side": lambda sid, s, d, sg: art_side(sid, s, d),
    "turnline": lambda sid, s, d, sg: art_turnline(sid, s, d), "photo": lambda sid, s, d, sg: art_photo(sid, s, d),
    "turns": lambda sid, s, d, sg: art_turns(sid, s, d), "disc": lambda sid, s, d, sg: art_disc(sid, s, d),
}
SCRIM_BG = ("aroll", "aroll_zoom", "broll", "painting")
PAINT_MOVES = {"drift": ("scale: 1.10, x: 24", "scale: 1.16, x: -24"), "up": ("scale: 1.22, y: 170", "scale: 1.26, y: -170"),
               "push": ("scale: 1.04", "scale: 1.16")}

def emit_phases(sid, k, phases, t0, t1, bg, start, inner, js):
    for p, phs in enumerate(phases):
        pid = f"{k}x{p}"
        y = phs.get("y", DEFAULT_Y.get(bg, .5)); top = round(y * 1920)
        pt0 = t0 if p == 0 else round(onset(min(phase_words(phs))) - F - start, 3)
        pt1 = t1 if p == len(phases) - 1 else round(onset(min(phase_words(phases[p + 1]))) - F - start, 3)
        light = bg in LIGHT_BG or phs.get("ink")
        color = BLUE if light else "#FFFFFF"; hcolor = INK if light else None
        layers_scrim = f'<div class="scrim" id="{sid}-sc{pid}" style="top:{top - 320}px"></div>' if bg in SCRIM_BG and not phs.get("ink") else ""
        inner.append(layers_scrim + lockup(sid, phs, pid, color, hcolor, top))
        sel = f'"#{sid}-lk{pid}"' + (f', "#{sid}-sc{pid}"' if layers_scrim else "")
        if p > 0:
            js.append(f'tl.fromTo([{sel}], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, {pt0:.3f});')
        if p < len(phases) - 1:
            js.append(f'tl.to([{sel}], {{ opacity: 0, duration: 0.001 }}, {pt1:.3f});')
        lag = LAG.get(bg, 3)
        for i in phase_words(phs):
            js.append(f'tl.set("#{sid}-{pid}-w{i}", {{ opacity: 1 }}, {pop(onset(i) - start + lag * F, pt0, pt1):.3f});')
        if phs.get("box"):
            tb = pop(onset(phs["key"][0]) - start + lag * F, pt0, pt1) - 1 * F
            js.append(f'tl.fromTo("#{sid}-{pid}-box", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {max(pt0, tb):.3f});')

def build_scene(n, segs=None, sid=None, over=None, end=None):
    sid = sid or f"s{n:02d}"
    b = BEAT[n]; start = b["start"]
    if end is None: end = b["end"] if n < 18 else TOTAL
    dur = round(end - start, 3)
    segs = segs or SCENES[n]
    seg_t = []
    for k, sg in enumerate(segs):
        if k == 0: t0 = 0.0
        else:
            first = sg.get("at") or min(phase_words(sg["phases"][0]))
            t0 = round(onset(first) - F - start, 3)
        seg_t.append(t0)
    seg_t.append(dur)
    layers, js = [], []
    for k, sg in enumerate(segs):
        t0, t1 = seg_t[k], seg_t[k + 1]; sdur = round(t1 - t0, 3)
        bg = sg["bg"]; inner = []
        if bg == "broll":
            s, o = sg["crop"]; vt0 = max(0.0, t0 - 5 * F) if (k > 0 and sg.get("enter") == "zoomfade") else t0
            inner.append(f'<div class="media"><div class="cam" id="{sid}-cam{k}" style="transform-origin:{o}">'
                         f'<video id="{sid}-v{k}" class="clip" src="assets/broll/{sg["clip"]}.mp4" muted playsinline data-start="{vt0:.3f}" data-duration="{t1 - vt0:.3f}" '
                         f'data-media-start="{sg.get("ms", 0.4)}" data-hf-media-start-basis="local" data-track-index="0" data-color-grading="{GRADES[sg["grade"]]}"></video></div></div>')
            js.append(f'tl.fromTo("#{sid}-cam{k}", {{ scale: {s} }}, {{ scale: {s + 0.012 * sdur:.4f}, duration: {sdur:.3f}, ease: "none" }}, {t0:.3f});')
        elif bg == "aroll_zoom":
            s, o = sg.get("crop", (1.3, "50% 30%"))
            z0, z1, ze = sg.get("zoom", (s, s + 0.02 * sdur, "none"))
            gr = f' data-color-grading="{GRADES[sg["grade"]]}"' if sg.get("grade") else ""
            inner.append(f'<div class="media"><div class="cam" id="{sid}-cam{k}" style="transform-origin:{o}">'
                         f'<video id="{sid}-v{k}" class="clip" src="assets/{sg.get("src", "aroll")}.mp4" muted playsinline data-start="{t0:.3f}" data-duration="{sdur:.3f}" '
                         f'data-media-start="{start + t0:.3f}" data-hf-media-start-basis="local" data-track-index="0"{gr}></video></div></div>')
            if z1 != z0: js.append(f'tl.fromTo("#{sid}-cam{k}", {{ scale: {z0} }}, {{ scale: {z1:.4f}, duration: {sdur:.3f}, ease: "{ze}" }}, {t0:.3f});')
            else: inner[-1] = inner[-1].replace(f'transform-origin:{o}"', f'transform-origin:{o};transform:scale({z0})"')
        elif bg == "painting":
            mv = sg.get("move", "drift")
            inner.append(f'<div class="media"><div class="cam" id="{sid}-cam{k}" style="transform-origin:{sg.get("origin", "50% 50%")}">'
                         f'<img id="{sid}-img{k}" src="assets/art/{sg["img"]}.jpg" style="object-position:{sg["pos"]}" data-color-grading="{GRADES[sg.get("grade", "painting")]}" alt=""></div></div>')
            if sg.get("texture") == "strong":  # rough paper: mottled grain (overlay) plus paper speckle (multiply)
                inner.append('<div class="bg" style="background-image:url(assets/textures/cloth-grey.jpg);background-size:cover;mix-blend-mode:overlay;opacity:.6"></div>'
                             '<div class="bg" style="background-image:url(assets/textures/paper-white-rough.jpg);mix-blend-mode:multiply;opacity:.75"></div>')
            elif sg.get("texture"):  # the style kit's rough paper, multiplied over the painting
                inner.append('<div class="bg" style="background-image:url(assets/textures/paper-white-rough.jpg);mix-blend-mode:multiply;opacity:.5"></div>')
            if mv == "slidein":   # quick camera slide-in reveal, then a slow push
                rs, ry = sg.get("rest", (1.12, 0))   # resting scale and vertical offset after the reveal
                dx = max(-150, min(150, sg.get("from_x", 140))); rv = 16 * F   # stays inside the overscan
                js.append(f'tl.fromTo("#{sid}-cam{k}", {{ scale: {rs + 0.18:.2f}, x: {dx}, y: {ry} }}, {{ scale: {rs}, x: 0, y: {ry}, duration: {rv:.3f}, ease: "power3.out" }}, {t0:.3f});')
                js.append(f'tl.to("#{sid}-cam{k}", {{ scale: {rs + 0.04:.2f}, duration: {max(0.2, sdur - rv):.3f}, ease: "none" }}, {t0 + rv:.3f});')
            else:
                fr, to = PAINT_MOVES[mv]
                js.append(f'tl.fromTo("#{sid}-cam{k}", {{ {fr} }}, {{ {to}, duration: {sdur:.3f}, ease: "none" }}, {t0:.3f});')
        elif bg == "graph":
            inner.append('<div class="bg bg-graph"></div>')
        elif bg != "aroll":
            inner.append(f'<div class="bg bg-{bg}"></div>')
        art = sg.get("art")
        if bg == "graph" and art in ("stairs", "zigzag", "flat", "spiral"):
            mk, ajs = art_graph(sid, art, start + t0, sdur)
            inner.append(f'<div class="cam" id="{sid}-cam" style="position:absolute;inset:0">{mk}</div><div class="vignette"></div>')
            js.append(shift(ajs, t0))
        elif art in ART_FNS:
            mk, ajs = ART_FNS[art](sid, start + t0, sdur, sg)
            inner.append(mk); js.append(shift(ajs, t0))
            if bg == "graph": inner.append('<div class="vignette"></div>')
        elif art in ("quote", "endcard"):
            inner.append(f'<div class="quote-mark" id="{sid}-q1" style="left:70px;top:560px">“</div><div class="quote-mark" id="{sid}-q2" style="right:70px;top:1160px">”</div>'
                         if art == "quote" else "")
            if art == "endcard":
                js.append(f'tl.fromTo("#{sid}-lk{k}x0", {{ scale: 1 }}, {{ scale: 1.035, duration: {sdur:.3f}, ease: "none" }}, {t0:.3f});')
        emit_phases(sid, k, sg["phases"], t0, t1, bg, start, inner, js)
        # segment visibility (hard cuts inside a scene)
        layers.append(f'<div class="seg" id="{sid}-seg{k}">{"".join(inner)}</div>')
        smooth_in = k > 0 and sg.get("enter") == "zoomfade"
        smooth_out = k < len(segs) - 1 and segs[k + 1].get("enter") == "zoomfade"
        if smooth_in:
            js.append(f'tl.fromTo("#{sid}-seg{k}", {{ opacity: 0, scale: 1.12 }}, {{ opacity: 1, scale: 1, duration: {14 * F:.3f}, ease: "power2.out" }}, {t0 - 5 * F:.3f});')
        elif k > 0: js.append(f'tl.fromTo("#{sid}-seg{k}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, {t0:.3f});')
        if smooth_out: js.append(f'tl.to("#{sid}-seg{k}", {{ opacity: 0, duration: {8 * F:.3f}, ease: "power1.in" }}, {t1 - 5 * F:.3f});')
        elif k < len(segs) - 1: js.append(f'tl.to("#{sid}-seg{k}", {{ opacity: 0, duration: 0.001 }}, {t1:.3f});')
    if over:  # one caption layer held across every segment (montage)
        inner = []
        emit_phases(sid, "o", over["phases"], 0.0, dur, over["bg"], start, inner, js)
        layers.append(f'<div class="seg" id="{sid}-over">{"".join(inner)}</div>')
    doc = f"""<!doctype html>
<html>
<head><meta charset="UTF-8" /></head>
<body>
<template id="{sid}-template">
<style>
{FONTS}
{CSS}
</style>
<div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920" data-duration="{dur:.3f}">
{chr(10).join(layers)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines["{sid}"] = tl;
</script>
</template>
</body>
</html>
"""
    return sid, start, dur, doc

def shift(js, t0):
    """Art timelines are written in segment-local time; offset their position parameters by t0."""
    if t0 == 0: return js
    import re
    return re.sub(r"\}, (-?[0-9.]+)\);", lambda m: "}, " + f"{float(m.group(1)) + t0:.3f}" + ");", js)

def main():
    slots = []
    for n in range(1, 19):
        sid, start, dur, doc = build_scene(n)
        open(os.path.join(PROJ, "compositions", f"{sid}.html"), "w").write(doc)
        slots.append(f'    <div id="el-{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" '
                     f'data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="{1 if n % 2 else 2}" data-width="1080" data-height="1920"></div>')
    index = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Four Career Patterns Edit</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      body {{ margin: 0; background: #000402; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #000402; }}
      #aroll {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
      [data-composition-id="main"] > div[data-composition-src] {{ position: absolute; inset: 0; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1080" data-height="1920" data-fps="24000/1001" data-duration="{TOTAL}">
    <video id="aroll" class="clip" src="assets/aroll.mp4" playsinline data-has-audio="true" data-start="0" data-duration="{AUDIO_END}" data-track-index="0" data-volume="1"></video>
{chr(10).join(slots)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(os.path.join(PROJ, "index.html"), "w").write(index)
    print("built 18 scenes; total", TOTAL, "s")

if __name__ == "__main__":
    main()
