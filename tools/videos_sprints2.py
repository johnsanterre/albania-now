#!/usr/bin/env python3
"""Albania Now — watch videos, sprint 4 (AI Image Analysis on Other Planets).
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_sprints2.py [slug]"""
import sys
from vidlib import s_title, s_bullets, s_chart, build_all

IMG = {}

IMG["alnow-img-1"] = [
 (s_title("Week 1 · AI Image Analysis", "An image is numbers",
          "What a spacecraft actually radios home."),
  "Welcome to the image analysis sprint. When an orbiter photographs another "
  "world, no picture travels home — a grid of numbers does, one number per "
  "pixel. Your screen rebuilds the picture. The machine never needs to."),
 (s_bullets("The grid", "Why numbers unlock everything", [
   "One number per pixel: 0 dark, 255 bright",
   "Questions become arithmetic",
   "Shadow = small numbers, rim = big ones",
   "The Sun labels craters for free",
   "More craters = older ground"]),
  "If an image is numbers, questions about the image become arithmetic. Where "
  "is it dark? Which numbers are small. Where is the rim catching sunlight? "
  "Where the numbers jump. Craters come pre-labeled by the Sun — a shadowed "
  "bowl beside a bright rim — and counting them dates the surface: more "
  "craters, older ground. That is real planetary science, and it is all in "
  "the grid."),
 (s_bullets("This week", "Your job", [
   "Read a 16-by-16 grid in the figure",
   "Build a crater from pure numpy",
   "Meet the histogram and its valley",
   "Build: decode a mystery block by hand"], closing=True),
  "Your job this week: read a sixteen-by-sixteen grid pixel by pixel in the "
  "figure, build a synthetic crater out of pure arithmetic in the notebook, "
  "and meet the histogram — the tally of brightness that shows you where the "
  "shadows hang. The build: decode a mystery block of raw numbers by hand, "
  "then check yourself."),
]

IMG["alnow-img-2"] = [
 (s_title("Week 2 · AI Image Analysis", "Find the craters",
          "Threshold. Group. Filter. Count."),
  "Week two: the classical crater detector, built from three steps you can "
  "hold in one hand."),
 (s_bullets("The recipe", "Three steps to a count", [
   "Threshold: darker than the cutoff?",
   "  — the cutoff comes from the histogram",
   "Group: touching shadows = one blob",
   "  — the paint-bucket trick",
   "Filter: throw out speck-sized junk"]),
  "Step one, threshold: every pixel answers one question — darker than the "
  "cutoff? The cutoff comes from the histogram's valley, never from hope. "
  "Step two, group: shadow pixels that touch belong to the same crater; flood "
  "outward like a paint bucket and collect the blob. Step three, filter: a "
  "one-pixel blob is noise, not a crater — and the minimum size you choose "
  "sets the smallest crater you can find. Say that out loud when you report."),
 (s_bullets("This week", "Your job", [
   "Drag the threshold on a six-crater field",
   "Build the detector in the notebook",
   "Count a field with a hidden answer",
   "Build: defend your two settings"], closing=True),
  "Your job: drag the threshold in the figure and watch the count fight the "
  "junk, build the full detector in the notebook, then face a field whose "
  "crater count you are not told. Report the count and defend your threshold "
  "and size filter in two sentences. The defense is the skill."),
]

IMG["alnow-img-3"] = [
 (s_title("Week 3 · AI Image Analysis", "Teach a machine to sort",
          "Labels in, rule out, graded on fresh data."),
  "Week three: the machine stops being hand-tuned and learns — from examples "
  "you label. This is machine learning in miniature, small enough to inspect "
  "every part."),
 (s_bullets("The recipe", "All of machine learning, small", [
   "Label patches: crater / not crater",
   "Measure features: roundness, darkness",
   "Learn: average each class, pick nearer",
   "Grade on patches it NEVER saw",
   "Your labels are its only truth"]),
  "Label small patches: crater or not. Measure features — numbers computable "
  "from any patch, like how round its dark region is. Learn the rule: average "
  "each class, classify new patches by the nearer average. And the honesty "
  "rule of the whole field: grade on held-out patches the machine never "
  "trained on, because a machine graded on its own homework can memorize a "
  "perfect score, and that score is a lie. Remember: it learns from your "
  "labels — including your mistakes."),
 (s_bullets("This week", "Your job", [
   "Label eight patches; watch it learn",
   "Build the classifier in the notebook",
   "Run both sabotage experiments",
   "Build: report the honest and dishonest scores"], closing=True),
  "Your job: label eight patches in the figure and watch the machine learn "
  "your labels — including any sloppy ones. Build the classifier in the "
  "notebook, then sabotage it twice: grade it on its own training data, and "
  "flip two labels and retrain. The build is a report on what the three "
  "scores teach about machine learning claims in the wild."),
]

IMG["alnow-img-4"] = [
 (s_title("Week 4 · AI Image Analysis", "New worlds, honest claims",
          "Misses versus false alarms — the seesaw."),
  "Capstone week. Your detector meets terrain it has never seen, and the two "
  "errors of every detector come out to trade against each other."),
 (s_chart("The seesaw", "Same detector, two thresholds",
          ["missed", "junk"], [3, 5],
          "Strict: 3 missed, 0 junk", compare_ylim=(0, 6),
          claim2="Loose: 0 missed, 5 junk",
          note="No setting removes both. The report carries both numbers."),
  "Here is the seesaw on this week's actual terrain. A strict threshold: "
  "three faint craters missed, zero junk. A loose one: every crater caught, "
  "and five boulder shadows counted as craters. No setting removes both "
  "errors. So the professional report never says just the count — it says "
  "the count, the settings, the measured miss rate, the measured false-alarm "
  "rate, and the smallest crater even attempted."),
 (s_bullets("This week", "Finish the sprint", [
   "Ride the seesaw in the figure",
   "Tune, measure, and report in the notebook",
   "Three sentences: measured, found, not proven",
   "All four builds in = Dr. Nixon's lecture"], closing=True),
  "Your job: ride the seesaw in the figure until you can feel the trade, then "
  "tune your detector on the new terrain, measure both error rates against "
  "the labeled strip, and sign your detection report — measured, found, not "
  "proven. Turn it in and the sprint is complete: Doctor Nixon's lecture is "
  "waiting, and machine learning on planetary images is his actual research. "
  "Bring a hard question."),
]


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(IMG, "AI Image Analysis", only=only)
