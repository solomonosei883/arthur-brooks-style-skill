"""Build the edit from the approved plan picks (plan page, 2026-11-08): compositions/sNN.html + index.html.

Each beat uses the design picked on the plan page plus the written changes:
  1 A · 2 own (Line + Text) · 3 C + slow zoom · 4 C · 5 B paintings (paint texture, slide-in, text by the subject)
  6 C black & white · 7 C · 8 B + slow zoom · 9 C dark B-roll, bold key · 10 C smooth hand-off · 11 B painting style
  12 C · 13 A as an object callout · 14 C bold highlighted HARD · 15 A · 16 B · 17 B from A-roll into the painting · 18 C + slow zoom
"""
import json, os
import build as b
import variants as v
from build import ph, W, F, onset, esc, BLUE, AZURE, INK, GREY, LGREY, pop

PROJ = b.PROJ
R = lambda a, z: list(range(a, z + 1))
LINE = BLUE
ZOOM = lambda: (1.0, 1.12, "sine.inOut")

# ------------------------------------------------------------------ beat 2: Line + Text (the user's own plan)
def art_linetext(sid, start, dur, sg):
    """A thick blue line leads up to each piece of text, is interrupted by it, and carries on; the camera
    climbs with the line through every "up"."""
    loc = lambda i: onset(i) - start
    H = 4300
    L1 = (540, 3340)
    UPS = [(13, 330, 2880), (15, 750, 2580), (17, 330, 2280), (19, 750, 1980), (21, 330, 1680), (23, 750, 1380)]
    L3 = (540, 760)
    def wsp(tag, ids, disp=None): return v.word_spans(sid, tag, ids, disp)
    def curve(x0, y0, x1, y1):
        my = (y0 + y1) / 2
        return f"M {x0} {y0} C {x0} {my} {x1} {my} {x1} {y1}"
    segs = [("M -60 3930 C 260 3930 540 3800 540 3480", None)]
    pts = [(L1[0], L1[1] - 140)] + [(x, y) for _, x, y in UPS]
    for k in range(len(UPS)):
        x0, y0 = pts[k]; x1, y1 = UPS[k][1], UPS[k][2] + 72
        if k > 0: y0 -= 72
        segs.append((curve(x0, y0, x1, y1), None))
    segs.append((curve(UPS[-1][1], UPS[-1][2] - 72, L3[0], L3[1] + 150), None))
    segs.append((f"M {L3[0]} {L3[1] - 210} C {L3[0]} 380 820 300 1160 300", None))
    paths = "".join(f'<path id="{sid}-ln{k}" d="{d}" fill="none" stroke="{LINE}" stroke-width="64" pathLength="1000"/>' for k, (d, _) in enumerate(segs))
    ups = "".join(f'<div class="lbl-serif" style="left:{x - 200}px;top:{y - 80}px;width:400px;text-align:center;font-size:120px;color:{INK}">'
                  + (f'<span class="lbl-sans" style="position:relative;font-size:40px;vertical-align:42px;margin-right:10px">{wsp("u", [12])}</span>' if i == 13 else "")
                  + f'{wsp("u", [i])}</div>' for i, x, y in UPS)
    mk = (f'<div id="{sid}-world" style="position:absolute;left:0;top:0;width:1080px;height:{H}px;will-change:transform">'
          f'<svg viewBox="0 0 1080 {H}" width="1080" height="{H}" style="position:absolute;left:0;top:0;overflow:visible" data-layout-ignore>{paths}</svg>'
          f'<div class="lbl-sans" style="left:0;width:1080px;top:{L1[1] - 150}px;text-align:center;font-size:46px;color:{INK}">{wsp("a", [6])}</div>'
          f'<div class="lbl-serif" style="left:0;width:1080px;top:{L1[1] - 96}px;text-align:center;font-size:170px;color:{INK}">{wsp("a", [7])}</div>'
          f'<div class="lbl-sans" style="left:0;width:1080px;top:{L1[1] + 84}px;text-align:center;font-size:46px;color:{INK}">{wsp("a", [8, 9, 10, 11])}</div>'
          + ups +
          f'<div class="lbl-sans" style="left:0;width:1080px;top:{L3[1] - 190}px;text-align:center;font-size:46px;color:{INK}">{wsp("c", [24, 25, 26])}</div>'
          f'<div class="lbl-sans" style="left:0;width:1080px;top:{L3[1] - 132}px;text-align:center;font-size:46px;color:{INK}">{wsp("c", R(27, 33))}</div>'
          f'<div class="lbl-serif" style="left:0;width:1080px;top:{L3[1] - 76}px;text-align:center;font-size:170px;color:{INK}">{wsp("c", [34])}</div>'
          f'</div>')
    js = []
    # the line leads into each word: segment k finishes as its text lands
    t_up = [pop(loc(i) + 3 * F, 0, dur) for i, _, _ in UPS]
    js.append(v.draw(f"#{sid}-ln0", 0, max(8 * F, loc(7)), "power2.out"))
    starts = [max(loc(12) - 6 * F, loc(11))] + t_up[:-1]
    for k in range(len(UPS)):
        a0 = starts[k]; a1 = t_up[k]
        js.append(v.draw(f"#{sid}-ln{k + 1}", a0, max(3 * F, a1 - a0), "power1.inOut"))
    t_c = pop(loc(34) + 3 * F, 0, dur)
    js.append(v.draw(f"#{sid}-ln7", t_up[-1], max(6 * F, loc(27) - t_up[-1]), "power1.inOut"))
    js.append(v.draw(f"#{sid}-ln8", t_c, max(6 * F, min(14 * F, dur - t_c - F)), "power2.out"))
    # camera: starts on "linears", climbs with the "up"s, settles on "better."
    cy0 = L1[1] - 960
    js.append(f'tl.set("#{sid}-world", {{ y: {-cy0} }}, 0);')
    prev = max(loc(12) - 6 * F, F)
    for k, (i, x, y) in enumerate(UPS):
        prev = round(prev, 3); d = round(max(3 * F, t_up[k] - prev), 3)
        js.append(f'tl.to("#{sid}-world", {{ y: {-(y - 1080)}, duration: {d:.3f}, ease: "power1.inOut" }}, {prev:.3f});')
        prev = round(prev + d + 0.002, 3)
    js.append(f'tl.to("#{sid}-world", {{ y: {-(L3[1] - 960)}, duration: {max(10 * F, loc(27) - prev):.3f}, ease: "power2.inOut" }}, {prev + 0.01:.3f});')
    js += v.word_pops(sid, "a", R(6, 11), start, dur) + v.word_pops(sid, "u", [12] + [i for i, _, _ in UPS], start, dur) + v.word_pops(sid, "c", R(24, 34), start, dur)
    return mk, "\n".join(js)

# ------------------------------------------------------------------ beat 13: object callout with a rough reveal
def art_callout(sid, start, dur, sg):
    loc = lambda i: onset(i) - start
    X, Y, Wd, Ht = 300, 640, 480, 640
    def wsp(tag, ids): return v.word_spans(sid, tag, ids)
    mk = (v.svg(f'<image href="assets/art/brooks-2017-gage-skidmore.jpg" x="{X}" y="{Y}" width="{Wd}" height="{Ht}" preserveAspectRatio="xMidYMid slice" mask="url(#{sid}-m)"/>'
                f'<path id="{sid}-c1" d="M 330 540 L 330 600 L 372 652" fill="none" stroke="{INK}" stroke-width="3" pathLength="1000"/><circle id="{sid}-d1" cx="372" cy="652" r="8" fill="{BLUE}"/>'
                f'<path id="{sid}-c2" d="M 742 1250 L 790 1310 L 790 1350" fill="none" stroke="{INK}" stroke-width="3" pathLength="1000"/><circle id="{sid}-d2" cx="742" cy="1250" r="8" fill="{BLUE}"/>',
                defs=b.rough_filter(sid) + f'<mask id="{sid}-m" maskUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1920">'
                f'<rect id="{sid}-mr" x="{X - 30}" y="{Y - 30}" width="{Wd + 60}" height="0" fill="#fff" filter="url(#{sid}-rough)"/></mask>')
          .replace('style="position:absolute;inset:0"', f'id="{sid}-obj" style="position:absolute;inset:0;transform-origin:540px 960px"') +
          f'<div class="lbl-sans" style="left:96px;top:384px;font-size:44px;color:{INK}">{wsp("t", R(166, 169))}</div>'
          f'<div class="lbl-serif" style="left:90px;top:428px;font-size:108px;color:{BLUE}">{wsp("t", [170, 171])}</div>'
          f'<div class="lbl-sans" style="left:420px;right:80px;top:1366px;text-align:right;font-size:44px;color:{INK}">{wsp("t", R(172, 174))}</div>'
          f'<div class="lbl-serif" style="left:380px;right:76px;top:1410px;text-align:right;font-size:108px;color:{BLUE}">{wsp("t", [175])}</div>'
          f'<div class="lbl-sans" style="left:0;right:0;top:1866px;text-align:center;font-size:20px;color:{GREY}">Photo: Gage Skidmore, CC BY-SA 3.0</div>')
    js = [f'tl.fromTo("#{sid}-mr", {{ attr: {{ height: 0 }} }}, {{ attr: {{ height: {Ht + 60} }}, duration: {16 * F:.3f}, ease: "power2.inOut" }}, {2 * F:.3f});',
          f'tl.fromTo("#{sid}-obj", {{ scale: 1 }}, {{ scale: 1.04, duration: {dur:.3f}, ease: "none" }}, 0);',
          v.draw(f"#{sid}-c1", loc(170), 10 * F), v.draw(f"#{sid}-c2", loc(175) - 2 * F, 10 * F),
          f'tl.fromTo("#{sid}-d1", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {loc(170):.3f});',
          f'tl.fromTo("#{sid}-d2", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: {6 * F:.3f}, ease: "power2.out" }}, {loc(175) - 2 * F:.3f});']
    js += v.word_pops(sid, "t", R(166, 175), start, dur)
    return mk, "\n".join(js)

b.ART_FNS.update({"linetext": art_linetext, "callout": art_callout})

# ------------------------------------------------------------------ the picked designs
def ph_of(name): return v.V[name]["segs"]
FINAL = {
 1: b.SCENES[1],
 2: [dict(bg="whiterough", art="linetext", phases=[])],
 3: [dict(bg="aroll_zoom", src="aroll-k", crop=(1.0, "50% 32%"), zoom=ZOOM(), phases=v.V["3C"]["segs"][0]["phases"])],
 4: ph_of("4C"),
 5: [dict(bg="painting", img="vangogh-cafe-terrace", pos="50% 50%", move="slidein", from_x=140, grade="paint2", texture="strong",
          phases=[ph(tc=R(61, 65), key=[66], style="serif", size=150, y=.15),
                  ph(tc=[67, 68], key=[69, 70], style="serif", size=140, y=.15)]),
     dict(bg="painting", img="renoir-dance-bougival", pos="50% 30%", rest=(1.25, 210), move="slidein", from_x=-140, grade="paint2", texture="strong",
          phases=[ph(tc=R(71, 79), key=[80, 81], style="serif", size=140, y=.12)])],
 6: [dict(bg="aroll_zoom", src="aroll-k", crop=(1.0, "50% 32%"), zoom=(1.0, 1.0, "none"), grade="monofade", phases=v.V["6C"]["segs"][0]["phases"])],
 7: [dict(bg="white", art="photo2", img="desk-pexels", tilt=(6, 0), box=(200, 640, 680, 900),
          phases=[ph(tc=R(93, 96), key=[97, 98], style="serif", y=.18), ph(tc=[99], key=[100, 101], style="serif", y=.18)])],
 8: [dict(bg="aroll_zoom", src="aroll-k", crop=(1.0, "50% 32%"), zoom=ZOOM(), phases=v.V["8B"]["segs"][0]["phases"])],
 9: [dict(bg="broll", clip="mail", crop=(1.06, "50% 40%"), grade="dark",
          phases=[ph(tl=R(121, 124), key=[125], style="bold", br=[126, 127], y=.5)])],
 10: [dict(bg="aroll", phases=[ph(tl=R(128, 131), key=[132], style="bold", br=R(133, 137))]),
      dict(bg="broll", clip="spiral", crop=(1.04, "50% 50%"), grade="cool", enter="zoomfade",
           phases=[ph(tl=[138], key=[139], style="serif", y=.5), ph(tl=[140, 141], key=[142, 143, 144], style="serif", br=[145], y=.5)])],
 11: [dict(bg="painting", img="caillebotte-floor-scrapers", pos="64% 50%", origin="45% 40%", move="slidein", from_x=140, grade="paint2", texture="strong",
           phases=[ph(tc=R(146, 153), key=R(154, 157), style="serif", y=.80), ph(tl=[158], key=[159, 160], style="serif", y=.80)])],
 12: ph_of("12C"),
 13: [dict(bg="whiterough", art="callout", phases=[ph(tl=[176, 177], key=[178], style="serif", y=.88)])],
 14: [dict(bg="aroll_zoom", src="aroll-k", crop=(1.12, "52% 26%"), zoom=(1.12, 1.16, "none"),
           phases=[ph(tc=R(179, 183), key=[184], disp={184: "HARD."}, style="bold", size=190, hs=48, box=True, y=.62)])],
 15: b.SCENES[15],
 16: ph_of("16B"),
 17: [dict(bg="aroll", phases=[ph(tl=R(211, 216), key=R(217, 220), style="serif")]),
      dict(bg="painting", img="friedrich-wanderer", pos="50% 40%", move="slidein", from_x=260, grade="paint", texture=True,
           phases=[ph(tl=[221, 222, 223], key=[224, 225], style="serif", size=104, y=.24, ink=True),
                   ph(tl=R(226, 229), key=[230], style="serif", y=.24, ink=True)])],
 18: [dict(bg="aroll_zoom", src="aroll-k", crop=(1.0, "50% 32%"), zoom=ZOOM(), phases=v.V["18C"]["segs"][0]["phases"])],
}
NOTES = {
 1: "Unchanged: your pick A. The camera on him is now locked between cuts, no drift.",
 2: "Your own plan: Line + Text. A thick blue line leads into “linears”, breaks for each “up” as the camera climbs with it, and runs into “better.”",
 3: "Option C on the A-roll, with a slow zoom-in while he speaks. The camera on him is now locked between cuts, no drift.",
 4: "Option C, unchanged. The camera on him is now locked between cuts, no drift.",
 5: "v2: stronger paint texture and rough-paper texture on both paintings, quick camera slide-in, captions centered and stacked (small line above, key word below).",
 6: "Option C on the A-roll, in soft black and white like your reference. The camera on him is now locked between cuts, no drift.",
 7: "v2: caption centered over the photo; the desk photo now sits straight and centered.",
 8: "Option B on the A-roll, with a slow zoom-in. The camera on him is now locked between cuts, no drift.",
 9: "Option C, styled like your B-roll reference: darker, moodier footage with a bold white key word in the middle.",
 10: "Option C, with a smooth zoom-through fade from his face into the spiral staircase. The camera on him is now locked between cuts, no drift.",
 11: "v2: the same stronger paint and rough-paper texture, quick slide-in, centered caption on the floor below the men.",
 12: "Option C, unchanged. The camera on him is now locked between cuts, no drift.",
 13: "Option A as an object callout: his photo revealed with a rough edge, “French horn” and “scientist,” pointing to it.",
 14: "Option C, with “HARD.” bigger and bolder on a blue highlight. The camera on him is now locked between cuts, no drift.",
 15: "Your pick A. v2: the circle photo of Arthur is now properly black and white.",
 16: "Option B, unchanged. The camera on him is now locked between cuts, no drift.",
 17: "Starts on his face with the caption, then slides into the Wanderer painting in the painting style. The camera on him is now locked between cuts, no drift.",
 18: "Option C on the A-roll, with a clean slow zoom-in. The video now ends when he finishes. The camera on him is now locked between cuts, no drift.",
}

def main():
    end_all = b.AUDIO_END
    slots = []
    for n in range(1, 19):
        sid = f"s{n:02d}"
        sid, start, dur, doc = b.build_scene(n, FINAL[n], sid=sid, end=(end_all if n == 18 else None))
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
    <div id="root" data-composition-id="main" data-start="0" data-width="1080" data-height="1920" data-fps="24000/1001" data-duration="{end_all}">
    <video id="aroll" class="clip" src="assets/aroll.mp4" playsinline data-has-audio="true" data-start="0" data-duration="{end_all}" data-track-index="0" data-volume="1"></video>
{chr(10).join(slots)}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(os.path.join(PROJ, "index.html"), "w").write(index)
    json.dump(NOTES, open(os.path.join(PROJ, "tools", "revision-notes.json"), "w"), indent=1)
    print("built 18 scenes from the plan picks; total", end_all, "s")

if __name__ == "__main__":
    main()
