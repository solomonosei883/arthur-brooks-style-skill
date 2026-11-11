"""Example beat plan: how beats + 3 design options are written for the plan page.
Neutral sample voice-over: "Most people try to remember everything. Write one sentence a day instead."
Replace with your own project's beats (word indices refer to your transcript.json)."""
CAT = {1: "On-Screen Caption", 2: "B-Roll + Text", 3: "Painting", 4: "Line + Text", 5: "Line + Illustration",
       6: "Text-Centric", 7: "Center Illustration", 8: "Side Illustration + Text", 9: "Object + Text", 10: "Graphs + Statistics"}
AROLL, OVER, CUT = "A-roll + captions", "Overlay on A-roll", "Cut-away scene"
# (first word, last word, seen-in-the-reels note, [options]); option = (title, cat, kind, description, ref, thumb)
BEATS = [
 (0, 5, "The problem stated in one line. The reels open on the face and land the key word late in the phrase.", [
   ("Opening caption", 1, AROLL, "Stay on A-roll. Small \"Most people try to\", then \"remember everything.\" as the key phrase at chest height.", "V04-A01", "lib:V04-A01"),
   ("Overflowing notes B-roll", 2, CUT, "A desk buried in sticky notes, edges darkened; \"remember\" lands as the serif key word.", "V03-A54", "lib:V03-A54"),
   ("Text-centric card", 6, CUT, "Blue paper. \"remember everything\" builds word by word, \"everything\" in Playfair Italic.", "V01-A02", "lib:V01-A02")]),
 (6, 11, "The fix, small and concrete. A single object makes it feel doable.", [
   ("Object: one notebook line", 9, CUT, "A tilted photo card of an open notebook with one handwritten line; blue serif \"one sentence\" above it.", "V05-A14", "lib:V05-A14"),
   ("Line + text", 4, CUT, "A thin blue line draws left to right and stops at \"a day\", like a daily tick.", "V02-A40", "lib:V02-A40"),
   ("Stay on A-roll", 1, AROLL, "\"Write / one sentence\" then \"a day / instead.\" at chest height.", "V05-A26", "lib:V05-A26")]),
]
