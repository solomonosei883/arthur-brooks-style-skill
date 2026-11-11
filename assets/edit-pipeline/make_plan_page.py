"""Fill the plan page template with a project's plan data.

Usage: python3 make_plan_page.py <plan-data.json> <out/index.html>
The template is ../plan-page/plan-template.html. Publish the result as an Artifact with
capabilities {db: {}, assets: {}, downloads: true} and these files next to it:
  opts/bNNx.mp4 + opts/bNNx.jpg  (one playable preview + poster per option, from cut_previews.py)
  posters/bNN.jpg + media/clip.mp4 (the beat's raw A-roll player)
  rev/bNN-vN.mp4 + .jpg           (revised scenes, from publish_rev.py, once built)
plan-data.json: {title, clip, length, source, style, cats, beats: [{n, start, end, first, last, script, note, camera,
  options: [{letter, title, cat, catn, kind, desc, ref, refTitle, thumb}], rev?: {v, dur, what}}]}
"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(here, "..", "plan-page", "plan-template.html")).read()
data = json.load(open(sys.argv[1]))
blob = json.dumps(data, ensure_ascii=True).replace("</", "<\\/")
os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
open(sys.argv[2], "w").write(tpl.replace("__PLAN_DATA__", blob))
print("wrote", sys.argv[2])
