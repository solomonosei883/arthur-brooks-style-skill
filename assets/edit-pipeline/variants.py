"""Build the B and C design options of every beat as real scenes on Arthur's audio, for the plan page previews.

Writes compositions/vNNb.html / vNNc.html and previews.html (all 36 options back to back, each over its own
slice of the A-roll), plus previews.json with each option's slot on the previews timeline.
Option A of every beat is the built edit itself (compositions/sNN.html via index.html).
"""
import json, os, math
import build as b
from build import (ph, W, F, onset, esc, BLUE, AZURE, WHITE, INK, GREY, LGREY, NAVY, FIGURE, SEATED, rough_filter,
                   figure, mini_shape, graph_layers, driven_line, spiral_pts, pop, GRADES)

PROJ = os.path.join(os.path.dirname(b.PROJ), "previews")  # separate project: one root composition per project
def loc_fn(start): return lambda i: onset(i) - start
def svg(inner, h=1920, defs=""):
    return (f'<svg viewBox="0 0 1080 {h}" width="1080" height="{h}" style="position:absolute;inset:0" data-layout-ignore>'
            f'<defs>{defs}</defs>{inner}</svg>')
def word_spans(sid, tag, ids, disp=None):
    disp = disp or {}
    return " ".join(f'<span class="w" id="{sid}-{tag}-w{i}">{esc(disp.get(i, W[i]["w"]))}</span>' for i in ids)
def word_pops(sid, tag, ids, start, dur, lag=3):
    return [f'tl.set("#{sid}-{tag}-w{i}", {{ opacity: 1 }}, {pop(onset(i) - start + lag * F, 0, dur):.3f});' for i in ids]
def draw(sel, t, d, ease="power2.out", f0=1000, f1=0):
    return (f'tl.fromTo("{sel}", {{ strokeDasharray: 1000, strokeDashoffset: {f0} }}, '
            f'{{ strokeDashoffset: {f1}, duration: {d:.3f}, ease: "{ease}" }}, {max(0, t):.3f});')

# ------------------------------------------------------------------ new art
def art_map4(sid, start, dur, sg):
    """1B: the four pattern shapes draw in side by side on the graph page."""
    loc = loc_fn(start)
    cells = [(150, 720, "stairs", "No.1", "LINEAR"), (590, 720, "zigzag", "No.2", "TRANSITORY"),
             (150, 1180, "flat", "No.3", "EXPERT"), (590, 1180, "spiral", "No.4", "SPIRAL")]
    grid = "".join(f'<line x1="0" y1="{y}" x2="1080" y2="{y}"/>' for y in range(600, 1561, 120)) + \
           "".join(f'<line x1="{x}" y1="600" x2="{x}" y2="1560"/>' for x in range(120, 1000, 120))
    g = [f'<g stroke="#FFFFFF" stroke-opacity=".09" stroke-width="2">{grid}</g>']
    js = []
    for k, (x, y, kind, no, name) in enumerate(cells):
        g.append(f'<path id="{sid}-m{k}" d="{mini_shape(kind, x, y, 340, 230)}" fill="none" stroke="{AZURE}" stroke-width="9" '
                 f'stroke-linecap="round" stroke-linejoin="round" pathLength="1000" filter="url(#{sid}-glow)"/>'
                 f'<text id="{sid}-ml{k}" x="{x}" y="{y + 300}" font-family="ABSerif" font-style="italic" font-weight="700" font-size="40" fill="#FFFFFF">{no}</text>'
                 f'<text id="{sid}-mn{k}" x="{x + 90}" y="{y + 300}" font-family="ABSans" font-weight="600" font-size="22" letter-spacing="3" fill="#FFFFFF" fill-opacity=".7">{name}</text>')
        t = loc(2) + 2 * F + k * 7 * F
        js.append(draw(f"#{sid}-m{k}", t, 14 * F))
        js.append(f'tl.fromTo(["#{sid}-ml{k}", "#{sid}-mn{k}"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, {t + 6 * F:.3f});')
    return svg("".join(g), defs=rough_filter(sid)), "\n".join(js)

def cup(x, y):
    return (f'<g transform="translate({x},{y})"><path d="M10 30 L110 30 L98 140 Q96 156 80 156 L40 156 Q24 156 22 140 Z" fill="{BLUE}"/>'
            f'<path d="M108 52 Q150 52 150 86 Q150 120 102 120" fill="none" stroke="{BLUE}" stroke-width="14"/>'
            f'<path d="M40 0 Q30 14 42 24 M62 0 Q52 14 64 24 M84 0 Q74 14 86 24" fill="none" stroke="{AZURE}" stroke-width="6" stroke-linecap="round"/></g>')
def van(x, y):
    return (f'<g transform="translate({x},{y})"><rect x="0" y="30" width="120" height="100" rx="8" fill="{BLUE}"/>'
            f'<path d="M120 60 L160 60 L186 96 L186 130 L120 130 Z" fill="{BLUE}"/><path d="M128 68 L156 68 L174 94 L128 94 Z" fill="#FBF9FC"/>'
            f'<circle cx="38" cy="134" r="20" fill="{INK}"/><circle cx="150" cy="134" r="20" fill="{INK}"/></g>')
def heart(x, y):
    return f'<g transform="translate({x},{y})"><path d="M80 150 C20 104 0 76 0 46 C0 18 22 0 46 0 C62 0 74 8 80 22 C86 8 98 0 114 0 C138 0 160 18 160 46 C160 76 140 104 80 150 Z" fill="{BLUE}"/></g>'

def art_icons3(sid, start, dur, sg):
    """5C: blue figure left, a cup, a van and a heart pop on the right as each is said."""
    loc = loc_fn(start)
    rows = [(560, cup, [66], [61, 62, 63, 64, 65]), (940, van, [69, 70], [67, 68]), (1320, heart, [80, 81], [73, 74, 75, 76, 77, 78, 79])]
    mk = [svg(f'<g id="{sid}-fig">{figure(sid, 250, 1560, 900, BLUE)}</g>' +
              "".join(f'<g id="{sid}-ic{k}">{fn(450, y)}</g>' for k, (y, fn, _, _) in enumerate(rows)), defs=rough_filter(sid))]
    js = [f'tl.fromTo("#{sid}-fig", {{ x: -260, opacity: 0 }}, {{ x: 0, opacity: 1, duration: {16 * F:.3f}, ease: "power2.out" }}, 0);']
    for k, (y, fn, key, helper) in enumerate(rows):
        mk.append(f'<div class="lbl-sans" style="left:650px;top:{y + 6}px;width:400px;white-space:normal;font-size:30px;line-height:1.15;color:{INK}">{word_spans(sid, f"r{k}", helper)}</div>'
                  f'<div class="lbl-serif" style="left:646px;top:{y + 52 + (36 if k == 2 else 0)}px;font-size:72px;color:{BLUE}">{word_spans(sid, f"r{k}", key)}</div>')
        t = loc(key[0]) - 3 * F
        js.append(f'tl.fromTo("#{sid}-ic{k}", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {8 * F:.3f}, ease: "back.out(2)" }}, {max(2 * F, t):.3f});')
        js += word_pops(sid, f"r{k}", helper + key, start, dur)
    return "".join(mk), "\n".join(js)

def art_hill(sid, start, dur, sg):
    """8C: a seated figure on a rough white hill under a pale sun."""
    mk = svg(f'<circle id="{sid}-sun" cx="540" cy="1080" r="300" fill="{AZURE}" fill-opacity=".16"/>'
             f'<g filter="url(#{sid}-rough)"><path id="{sid}-hill" d="M -80 1940 L -80 1560 Q 540 1150 1160 1560 L 1160 1940 Z" fill="#FFFFFF"/></g>'
             f'<path d="M -80 1560 Q 540 1150 1160 1560" fill="none" stroke="{LGREY}" stroke-width="3"/>'
             f'<g id="{sid}-fig">{figure(sid, 560, 1368, 430, BLUE, SEATED, 160, 222)}</g>', defs=rough_filter(sid))
    js = f"""tl.fromTo("#{sid}-hill", {{ y: 260 }}, {{ y: 0, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);
tl.fromTo("#{sid}-fig", {{ y: 300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: {18 * F:.3f}, ease: "power2.out" }}, {3 * F:.3f});
tl.fromTo("#{sid}-sun", {{ scale: .7, transformOrigin: "50% 50%" }}, {{ scale: 1.08, duration: {dur:.3f}, ease: "none" }}, 0);"""
    return mk, js

def art_envelope(sid, start, dur, sg):
    """9B: a vintage envelope cut-out drops onto white paper."""
    mk = (f'<div id="{sid}-env" style="position:absolute;left:190px;top:820px;width:700px;height:460px;box-shadow:0 18px 40px rgba(0,0,0,.22)">' +
          svg(f'<rect x="0" y="0" width="700" height="460" fill="#F1E7D4"/><rect x="0" y="0" width="700" height="460" fill="none" stroke="#CDBB98" stroke-width="4"/>'
              f'<path d="M0 0 L350 250 L700 0" fill="none" stroke="#CDBB98" stroke-width="4"/>'
              f'<rect x="560" y="40" width="96" height="120" fill="{BLUE}"/><rect x="572" y="52" width="72" height="96" fill="none" stroke="#FBF9FC" stroke-width="3"/>'
              f'<circle cx="520" cy="112" r="52" fill="none" stroke="#6B6B78" stroke-width="3"/><circle cx="520" cy="112" r="40" fill="none" stroke="#6B6B78" stroke-width="2"/>'
              f'<path d="M420 92 q14 -10 28 0 t28 0 t28 0 M420 112 q14 -10 28 0 t28 0 t28 0 M420 132 q14 -10 28 0 t28 0 t28 0" fill="none" stroke="#6B6B78" stroke-width="3"/>'
              f'<line x1="200" y1="320" x2="520" y2="320" stroke="#8C7D63" stroke-width="5"/><line x1="200" y1="362" x2="470" y2="362" stroke="#8C7D63" stroke-width="5"/>'
              f'<line x1="200" y1="404" x2="420" y2="404" stroke="#8C7D63" stroke-width="5"/>', h=460).replace('viewBox="0 0 1080 460" width="1080"', 'viewBox="0 0 700 460" width="700"') +
          '</div>')
    js = f"""tl.fromTo("#{sid}-env", {{ y: 360, rotation: -16, opacity: 0 }}, {{ y: 0, rotation: -5, opacity: 1, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);
tl.fromTo("#{sid}-env", {{ scale: 1 }}, {{ scale: 1.04, duration: {max(0.3, dur - 18 * F):.3f}, ease: "none", immediateRender: false }}, {18 * F:.3f});"""
    return mk, js

def art_photo2(sid, start, dur, sg):
    """7C: a tilted photo card (desk) on white paper."""
    L, T, Wc, Hc = sg.get("box", (230, 620, 620, 860))
    mk = (f'<div id="{sid}-card" style="position:absolute;left:{L}px;top:{T}px;width:{Wc}px;height:{Hc}px;background:#FFFFFF;padding:16px;box-shadow:0 18px 42px rgba(0,0,0,.26)">'
          f'<img id="{sid}-ph" src="assets/art/{sg["img"]}.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 45%;display:block" alt=""></div>')
    r0, r1 = sg.get("tilt", (10, 3))
    js = f"""tl.fromTo("#{sid}-card", {{ y: 260, rotation: {r0}, opacity: 0 }}, {{ y: 0, rotation: {r1}, opacity: 1, duration: {20 * F:.3f}, ease: "power2.out" }}, 0);
tl.fromTo("#{sid}-card", {{ scale: 1 }}, {{ scale: 1.04, duration: {max(0.3, dur - 20 * F):.3f}, ease: "none", immediateRender: false }}, {20 * F:.3f});"""
    return mk, js

def art_linebreak(sid, start, dur, sg):
    """11C: a thick azure line runs down the frame, breaks at "studs", starts again."""
    loc = loc_fn(start)
    mk = svg(f'<line id="{sid}-l1" x1="170" y1="-20" x2="170" y2="900" stroke="{AZURE}" stroke-width="64" pathLength="1000"/>'
             f'<line id="{sid}-c1" x1="120" y1="930" x2="220" y2="880" stroke="{AZURE}" stroke-width="10" stroke-linecap="round"/>'
             f'<line id="{sid}-c2" x1="120" y1="1030" x2="220" y2="980" stroke="{AZURE}" stroke-width="10" stroke-linecap="round"/>'
             f'<line id="{sid}-l2" x1="170" y1="1040" x2="170" y2="1940" stroke="{AZURE}" stroke-width="64" pathLength="1000"/>')
    tb, ts = loc(157), loc(159)
    js = [draw(f"#{sid}-l1", 0, max(0.3, tb), "power1.inOut"),
          f'tl.fromTo(["#{sid}-c1", "#{sid}-c2"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.001 }}, {tb + 2 * F:.3f});',
          f'tl.fromTo("#{sid}-c1", {{ x: 0, y: 0 }}, {{ x: -18, y: -14, duration: {10 * F:.3f}, ease: "power2.out" }}, {tb + 2 * F:.3f});',
          f'tl.fromTo("#{sid}-c2", {{ x: 0, y: 0 }}, {{ x: 18, y: 14, duration: {10 * F:.3f}, ease: "power2.out" }}, {tb + 2 * F:.3f});',
          draw(f"#{sid}-l2", ts - 1 * F, 14 * F)]
    return mk, "\n".join(js)

def art_turn2(sid, start, dur, sg):
    """13C: an azure line runs from "French horn", bends hard and runs on into "scientist,"."""
    loc = loc_fn(start)
    mk = (svg(f'<path id="{sid}-ln" d="M 120 760 L 660 760 Q 760 760 760 860 L 760 1250" fill="none" stroke="{AZURE}" stroke-width="40" '
              f'stroke-linecap="round" stroke-linejoin="round" pathLength="1000"/>'
              f'<circle id="{sid}-n0" cx="120" cy="760" r="30" fill="{BLUE}"/><circle id="{sid}-n1" cx="760" cy="1250" r="30" fill="{BLUE}"/>') +
          f'<div class="lbl-sans" style="left:110px;top:540px;font-size:44px;color:{INK}">{word_spans(sid, "t", [166, 167, 168, 169])}</div>'
          f'<div class="lbl-serif" style="left:104px;top:588px;font-size:116px;color:{BLUE}">{word_spans(sid, "t", [170, 171])}</div>'
          f'<div class="lbl-sans" style="left:420px;top:1300px;width:680px;font-size:44px;color:{INK}">{word_spans(sid, "t", [172, 173, 174])}</div>'
          f'<div class="lbl-serif" style="left:414px;top:1348px;font-size:116px;color:{BLUE}">{word_spans(sid, "t", [175])}</div>')
    js = [f'tl.fromTo("#{sid}-n0", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {2 * F:.3f});',
          draw(f"#{sid}-ln", loc(170), 14 * F, "power2.out", 1000, 480),
          f'tl.to("#{sid}-ln", {{ strokeDashoffset: 0, duration: {16 * F:.3f}, ease: "power2.inOut" }}, {max(loc(172), loc(170) + 15 * F):.3f});',
          f'tl.fromTo("#{sid}-n1", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {loc(172) + 14 * F:.3f});']
    js += word_pops(sid, "t", list(range(166, 176)), start, dur)
    return mk, "\n".join(js)

def art_stack(sid, start, dur, sg):
    """14B: three small "really"s stack, then a big bold "hard."."""
    rows = [(179, 180, 560, 52), (181, None, 640, 64), (182, None, 724, 64), (183, None, 808, 64)]
    mk = []
    for k, (i, j, y, fs) in enumerate(rows):
        ids = [i] + ([j] if j else [])
        mk.append(f'<div class="lbl-sans" style="left:150px;top:{y}px;font-size:{fs}px;color:#FFFFFF;opacity:{1 if k == 0 else .9}">{word_spans(sid, "k", ids)}</div>')
    mk.append(f'<div class="lbl-sans" style="left:128px;top:880px;font-size:330px;font-weight:800;letter-spacing:-0.04em;line-height:1;color:#FFFFFF">{word_spans(sid, "k", [184])}</div>')
    return "".join(mk), "\n".join(word_pops(sid, "k", list(range(179, 185)), start, dur))

def art_spiral2(sid, start, dur, sg):
    """15B: the No.4 spiral continues; the dot travels turns 2, 3 and 4, each faster."""
    loc = loc_fn(start)
    svgm, js = graph_layers(sid, 3, start, dur, None)
    pts = spiral_pts(turns=4.0, r1=400)
    sched = [(0, 0, .25, 0.001, "none"), (loc(185) + F, .25, .5, 20 * F, "sine.inOut"),
             (loc(188) + F, .5, .75, 12 * F, "sine.inOut"), (loc(191) + F, .75, 1.0, 8 * F, "power2.out")]
    shape, ljs = driven_line(sid, pts, sched)
    nums = "".join(f'<text id="{sid}-no{k}" x="{1000}" y="{700 + k * 60}" text-anchor="end" font-family="ABSerif" font-style="italic" font-weight="700" font-size="44" fill="#FFFFFF" opacity="0">{k + 1}</text>' for k in range(4))
    js2 = [f'tl.set("#{sid}-no{k}", {{ opacity: 1 }}, {t:.3f});' for k, t in enumerate([2 * F, loc(185) + 4 * F, loc(188) + 4 * F, loc(191) + 4 * F])]
    return svgm.replace("{SHAPE}", shape), js + "\n" + ljs

def art_halo(sid, start, dur, sg):
    """16C: a blue figure under a glowing halo ring; the two jobs as small labels."""
    mk = (svg(f'<ellipse id="{sid}-glow2" cx="540" cy="860" rx="300" ry="300" fill="{AZURE}" fill-opacity=".14"/>'
              f'<g id="{sid}-fig">{figure(sid, 540, 1700, 920, BLUE)}</g>'
              f'<ellipse id="{sid}-ring" cx="540" cy="700" rx="150" ry="40" fill="none" stroke="{AZURE}" stroke-width="12" filter="url(#{sid}-glow)" pathLength="1000"/>',
              defs=rough_filter(sid)) +
          f'<div class="cap" style="left:70px;top:1060px;color:{BLUE};font-size:30px">{word_spans(sid, "h", [207, 208])}</div>'
          f'<div class="cap" style="left:760px;top:1240px;color:{BLUE};font-size:30px">{word_spans(sid, "h", [210])}</div>')
    js = [f'tl.fromTo("#{sid}-fig", {{ y: 220, opacity: 0 }}, {{ y: 0, opacity: 1, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);',
          draw(f"#{sid}-ring", 10 * F, 18 * F),
          f'tl.fromTo("#{sid}-ring", {{ y: 0 }}, {{ y: -16, duration: {max(0.4, dur - 10 * F):.3f}, ease: "sine.inOut", immediateRender: false }}, {10 * F:.3f});']
    js += word_pops(sid, "h", [207, 208, 210], start, dur)
    return mk, "\n".join(js)

def art_mountain(sid, start, dur, sg):
    """18B: a figure on a blue mountain with thin rings."""
    rings = "".join(f'<circle id="{sid}-r{k}" cx="540" cy="1080" r="{240 + k * 120}" fill="none" stroke="{GREY}" stroke-opacity=".5" stroke-width="3" pathLength="1000"/>' for k in range(3))
    mk = svg(rings + f'<g filter="url(#{sid}-rough)"><path id="{sid}-mt" d="M -80 1960 L 540 1090 L 1160 1960 Z" fill="{BLUE}"/></g>'
             f'<g id="{sid}-fig">{figure(sid, 540, 1100, 300, AZURE)}</g>', defs=rough_filter(sid))
    js = [f'tl.fromTo("#{sid}-mt", {{ y: 420 }}, {{ y: 0, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);',
          f'tl.fromTo("#{sid}-fig", {{ y: 420 }}, {{ y: 0, duration: {18 * F:.3f}, ease: "power2.out" }}, 0);']
    js += [draw(f"#{sid}-r{k}", 8 * F + k * 5 * F, 22 * F) for k in range(3)]
    js.append(f'tl.fromTo(["#{sid}-r0", "#{sid}-r1", "#{sid}-r2"], {{ scale: 1, transformOrigin: "50% 50%" }}, {{ scale: 1.06, duration: {dur:.3f}, ease: "none", immediateRender: false }}, 0);')
    return mk, "\n".join(js)

b.ART_FNS.update({"map4": art_map4, "icons3": art_icons3, "hill": art_hill, "envelope": art_envelope, "photo2": art_photo2,
                  "linebreak": art_linebreak, "turn2": art_turn2, "stack": art_stack, "spiral2": art_spiral2,
                  "halo": art_halo, "mountain": art_mountain})

# ------------------------------------------------------------------ the 36 options
R = lambda a, z: list(range(a, z + 1))
BR = lambda clip, crop=(1.08, "50% 50%"), grade="warm", **k: dict(bg="broll", clip=clip, crop=crop, grade=grade, **k)
V = {
 "1B": dict(segs=[dict(bg="graph", art="map4", phases=[ph(tl=[1], key=[2], style="serif", bc=[3, 4, 5], y=.18)])]),
 "1C": dict(segs=[dict(bg="bluerough", phases=[ph(tl=[1], key=[2], disp={2: "4"}, size=560, hs=50, ghost=True, lining=True, bc=[3, 4, 5], y=.42)])]),
 "2B": dict(segs=[BR("stairs", (1.06, "50% 60%"), phases=[ph(tl=[6], key=[7], style="serif", bc=[8, 9, 10, 11], y=.10),
                                                          ph(sub=R(12, 23), y=.10), ph(sub=R(24, 30), y=.10),
                                                          ph(tl=[31, 32, 33], key=[34], style="serif", y=.10)])]),
 "2C": dict(segs=[dict(bg="painting", img="blake-jacobs-ladder", pos="50% 50%", move="up",
                       phases=[ph(tl=[6], key=[7], style="serif", bc=[8, 9, 10, 11], y=.16), ph(sub=R(12, 23), y=.16),
                               ph(sub=R(24, 30), y=.16), ph(tl=[31, 32, 33], key=[34], style="serif", y=.16)])]),
 "3B": dict(segs=[BR("apron", (1.06, "50% 40%"), phases=[]), BR("hardhat", (1.06, "50% 40%"), at=38, phases=[]),
                  BR("laptop", (1.06, "50% 50%"), at=42, phases=[]), BR("suitcase", (1.06, "50% 50%"), at=44, phases=[])],
            over=dict(bg="broll", phases=[ph(tl=[35, 36], key=[37], style="serif", y=.42),
                                          ph(tl=[42, 43], key=[44, 45], style="serif", br=[46, 47], y=.42)])),
 "3C": dict(segs=[dict(bg="aroll", phases=[ph(tl=[35, 36], key=[37], style="serif"), ph(tl=[42, 43], key=[44, 45], style="serif", br=[46, 47])])]),
 "4B": dict(segs=[dict(bg="painting", img="bruegel-harvesters", pos="50% 40%", phases=[ph(tc=R(48, 52), key=R(53, 56), style="serif", br=[57], y=.16)])]),
 "4C": dict(segs=[dict(bg="aroll", phases=[ph(tl=[48, 49], key=[50, 51, 52], style="bold"), ph(tl=[53], key=[54, 55, 56], style="bold", br=[57])])]),
 "5B": dict(segs=[dict(bg="painting", img="vangogh-cafe-terrace", pos="50% 50%", phases=[ph(tl=R(61, 65), key=[66], style="serif", y=.15),
                                                                                       ph(tl=[67, 68], key=[69, 70], style="serif", y=.15)]),
                  dict(bg="painting", img="renoir-dance-bougival", pos="50% 30%", phases=[ph(tc=R(71, 79), key=[80, 81], style="serif", y=.84)])]),
 "5C": dict(segs=[dict(bg="whiterough", art="icons3", phases=[])]),
 "6B": dict(segs=[dict(bg="painting", img="vermeer-lacemaker", pos="50% 50%", move="push",
                       phases=[ph(tl=R(82, 85), key=[86], style="serif", y=.15), ph(tl=[87, 88, 89], key=[90, 91, 92], style="serif", y=.15)])]),
 "6C": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(82, 85), key=[86], style="serif"), ph(tl=[87, 88, 89], key=[90], style="serif", br=[91, 92])])]),
 "7B": dict(segs=[dict(bg="painting", img="holbein-merchant-gisze", pos="50% 40%", phases=[ph(tl=R(93, 96), key=[97, 98], style="serif", br=[99, 100, 101], y=.84)])]),
 "7C": dict(segs=[dict(bg="white", art="photo2", img="desk-pexels", phases=[ph(tl=R(93, 96), key=[97, 98], style="serif", y=.17),
                                                                            ph(tl=[99], key=[100, 101], style="serif", y=.17)])]),
 "8B": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(102, 108), key=[109], style="serif"), ph(tl=[110, 111, 112], key=[113, 114], style="serif"),
                                           ph(tl=R(115, 119), key=[120], style="serif")])]),
 "8C": dict(segs=[dict(bg="whiterough", art="hill", phases=[ph(tl=R(102, 108), key=[109], style="serif", y=.17),
                                                            ph(tl=[110, 111, 112], key=[113, 114], style="serif", y=.17),
                                                            ph(tl=R(115, 119), key=[120], style="serif", y=.17)])]),
 "9B": dict(segs=[dict(bg="white", art="envelope", phases=[ph(key=[121, 122], style="serif", bc=R(123, 127), y=.25)])]),
 "9C": dict(segs=[BR("mail", (1.06, "50% 40%"), phases=[ph(tl=R(121, 124), key=R(125, 127), style="serif", y=.78)])]),
 "10B": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(128, 131), key=[132], style="bold", br=R(133, 137)),
                                            ph(tl=[138], key=[139], style="serif", box=True),
                                            ph(tl=[140, 141], key=[142, 143, 144], style="serif", br=[145])])]),
 "10C": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(128, 131), key=[132], style="bold", br=R(133, 137))]),
                   BR("spiral", (1.04, "50% 50%"), grade="cool", phases=[ph(tl=[138], key=[139], style="serif", y=.5),
                                                                        ph(tl=[140, 141], key=[142, 143, 144], style="serif", br=[145], y=.5)])]),
 "11B": dict(segs=[dict(bg="painting", img="caillebotte-floor-scrapers", pos="50% 50%", phases=[ph(tc=R(146, 153), key=R(154, 157), style="serif", y=.74),
                                                                                              ph(tl=[158], key=[159, 160], style="serif", y=.74)])]),
 "11C": dict(segs=[dict(bg="white", art="linebreak", phases=[ph(tc=R(146, 153), key=R(154, 157), style="serif", y=.30, lx=270),
                                                             ph(tl=[158], key=[159, 160], style="serif", y=.66, lx=270)])]),
 "12B": dict(segs=[dict(bg="white", phases=[ph(tl=R(161, 164), key=[165], style="serif", size=200, y=.5)])]),
 "12C": dict(segs=[dict(bg="aroll", phases=[ph(tl=[161], key=[162, 163], style="serif", br=[164, 165])])]),
 "13B": dict(segs=[dict(bg="painting", img="wright-air-pump", pos="50% 50%", move="push",
                        phases=[ph(tl=R(166, 169), key=[170, 171], style="serif", y=.14), ph(tl=[172, 173, 174], key=[175], style="serif", y=.14),
                                ph(tl=[176, 177], key=[178], style="serif", y=.14)])]),
 "13C": dict(segs=[dict(bg="white", art="turn2", phases=[ph(tl=[176, 177], key=[178], style="serif", y=.86)])]),
 "14B": dict(segs=[dict(bg="black", art="stack", phases=[])]),
 "14C": dict(segs=[dict(bg="aroll_zoom", crop=(1.12, "52% 22%"), phases=[ph(tc=R(179, 183), key=[184], style="bold", y=.62)])]),
 "15B": dict(segs=[dict(bg="graph", art="spiral2", phases=[ph(tl=[185, 186], key=[187], style="serif", y=.15), ph(tl=[188, 189], key=[190], style="serif", y=.15),
                                                           ph(tl=[191, 192, 193], key=[194, 195], style="serif", br=[196, 197], y=.15)])]),
 "15C": dict(segs=[dict(bg="aroll", phases=[ph(tl=[185, 186], key=[187], style="serif"), ph(tl=[188, 189], key=[190], style="serif"),
                                            ph(tl=[191, 192, 193], key=[194, 195], style="serif", br=[196, 197])])]),
 "16B": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(198, 201), key=[202, 203], style="serif"), ph(tl=[204, 205, 206], key=[207, 208], style="serif"),
                                            ph(tl=[209], key=[210], style="serif")])]),
 "16C": dict(segs=[dict(bg="whiterough", art="halo", phases=[ph(key=[198, 199], style="serif", y=.14), ph(tl=[200, 201], key=[202, 203], style="serif", y=.14)])]),
 "17B": dict(segs=[dict(bg="painting", img="friedrich-wanderer", pos="50% 40%", move="push",
                        phases=[ph(sub=R(211, 222), y=.86), ph(tl=[223], key=[224, 225], style="serif", y=.86), ph(tl=R(226, 229), key=[230], style="serif", y=.86)])]),
 "17C": dict(segs=[BR("ridge", (1.06, "50% 50%"), phases=[ph(sub=R(211, 222), y=.14, ink=True), ph(tl=[223], key=[224, 225], style="serif", y=.14, ink=True),
                                                          ph(tl=R(226, 229), key=[230], style="serif", y=.14, ink=True)])]),
 "18B": dict(segs=[dict(bg="whiterough", art="mountain", phases=[ph(tl=R(231, 234), key=[235], style="serif", y=.15), ph(tl=[236, 237], key=[238], style="serif", y=.15),
                                                                 ph(tc=R(239, 243), key=R(244, 247), style="serif", y=.15)])]),
 "18C": dict(segs=[dict(bg="aroll", phases=[ph(tl=R(231, 234), key=[235], style="serif"), ph(tl=[236, 237], key=[238], style="serif"),
                                            ph(tc=R(239, 243), key=R(244, 247), style="serif")])]),
}

def main():
    slots, t = [], 0.0
    for name, spec in V.items():
        n = int(name[:-1]); sid = f"v{n:02d}{name[-1].lower()}"
        end = b.AUDIO_END if n == 18 else None
        sid, start, dur, doc = b.build_scene(n, spec["segs"], sid=sid, over=spec.get("over"), end=end)
        open(os.path.join(PROJ, "compositions", f"{sid}.html"), "w").write(doc)
        slots.append(dict(opt=name, sid=sid, beat=n, start=round(t, 3), dur=dur, media_start=start))
        t = round(t + dur, 3)
    total = t
    rows = []
    for j, s in enumerate(slots):
        rows.append(f'    <video id="a-{s["sid"]}" class="clip" src="assets/aroll.mp4" playsinline data-has-audio="true" data-start="{s["start"]:.3f}" '
                    f'data-duration="{s["dur"]:.3f}" data-media-start="{s["media_start"]:.3f}" data-track-index="{2 * (j % 2)}" data-volume="1"></video>')
        rows.append(f'    <div id="el-{s["sid"]}" data-composition-id="{s["sid"]}" data-composition-src="compositions/{s["sid"]}.html" '
                    f'data-start="{s["start"]:.3f}" data-duration="{s["dur"]:.3f}" data-track-index="{1 + 2 * (j % 2)}" data-width="1080" data-height="1920"></div>')
    doc = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Design Option Previews</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      body {{ margin: 0; background: #000402; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #000402; }}
      #root > video {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
      [data-composition-id="previews"] > div[data-composition-src] {{ position: absolute; inset: 0; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="previews" data-start="0" data-width="1080" data-height="1920" data-fps="24000/1001" data-duration="{total}">
{chr(10).join(rows)}
    </div>
    <script>
      window.__timelines["previews"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(os.path.join(PROJ, "index.html"), "w").write(doc)
    json.dump(dict(total=total, slots=slots), open(os.path.join(PROJ, "previews.json"), "w"), indent=1)
    print(f"built {len(slots)} option scenes; previews.html {total} s")

if __name__ == "__main__":
    main()
