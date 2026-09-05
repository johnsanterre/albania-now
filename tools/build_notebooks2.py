#!/usr/bin/env python3
"""Albania Now — sprint 4 notebooks (AI Image Analysis on Other Planets).
Run: python3 build_notebooks2.py"""
import json, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SITE, 'notebooks')


def md(s):
    return {"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True)}


def code(s):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": s.splitlines(keepends=True)}


def nb(name, cells):
    doc = {"nbformat": 4, "nbformat_minor": 5,
           "metadata": {"colab": {"name": name}, "kernelspec":
                        {"name": "python3", "display_name": "Python 3"}},
           "cells": cells}
    path = os.path.join(OUT, name + '.ipynb')
    with open(path, 'w') as f:
        json.dump(doc, f, indent=1)
    json.load(open(path))
    print(path)


HDR = ("*Albania Now — a Free Focus program, built with Chicago First. "
       "Run cells top to bottom. First: **File → Save a copy in Drive**.*")

MAKE_TERRAIN = '''import numpy as np

def make_terrain(craters, size=90, seed=1, noise=15, specks=0.006):
    """A synthetic orbital image: bright plain, shadowed crater bowls,
    sunlit rims, camera noise. craters = list of (cx, cy, r)."""
    rng = np.random.default_rng(seed)
    img = 180 + rng.integers(-noise, noise, (size, size)).astype(float)
    yy, xx = np.mgrid[0:size, 0:size]
    for cx, cy, r in craters:
        d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        bowl = d < r
        img[bowl & (xx < cx)] = 55 + rng.integers(0, 20, int((bowl & (xx < cx)).sum()))
        img[bowl & (xx >= cx)] = 225
        img[(d >= r) & (d < r + 1.5) & (xx > cx)] = 240
    sp = rng.random((size, size)) < specks
    img[sp] = 45
    return np.clip(img, 0, 255)

CRATERS = [(20, 18, 8), (55, 25, 11), (75, 70, 7), (30, 60, 9), (62, 48, 5)]
img = make_terrain(CRATERS)
print(img.shape, "pixels, values", int(img.min()), "to", int(img.max()))'''

FLOOD = '''def find_blobs(mask):
    """Group touching True pixels into blobs (the paint-bucket trick)."""
    seen = np.zeros_like(mask, dtype=bool)
    blobs = []
    H, W = mask.shape
    for y0 in range(H):
        for x0 in range(W):
            if mask[y0, x0] and not seen[y0, x0]:
                stack, px = [(y0, x0)], []
                seen[y0, x0] = True
                while stack:
                    y, x = stack.pop()
                    px.append((y, x))
                    for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            stack.append((ny, nx))
                blobs.append(px)
    return blobs'''

# ---------------------------------------------------------------- img1
nb('img1-pixels', [
 md("# Week 1 — An image is numbers\n" + HDR),
 md("## 1. Build a crater out of arithmetic\nNo camera — we make the grid "
    "directly, the same way we'll later make test data for the detector."),
 code(MAKE_TERRAIN),
 md("## 2. The grid IS the image\nLook at it both ways."),
 code("import matplotlib.pyplot as plt\n\n"
      "plt.figure(figsize=(5, 5))\n"
      "plt.imshow(img, cmap=\"gray\", vmin=0, vmax=255)\n"
      "plt.title(\"The picture your screen makes of the grid\")\nplt.show()"),
 code("# the raw numbers of an 8x8 block cut from the biggest crater\n"
      "block = img[20:28, 48:56].astype(int)\nprint(block)"),
 md("## 3. The histogram — where the shadows hang"),
 code("plt.hist(img.ravel(), bins=40, color=\"#7E1B14\")\n"
      "plt.xlabel(\"brightness (0–255)\")\nplt.ylabel(\"pixel count\")\n"
      "plt.title(\"Big hump = ordinary ground. Left tail = shadow. Note the valley.\")\n"
      "plt.show()"),
 md("## 4. Your turn\nCut your own 8×8 block from somewhere else in the image "
    "(pick the coordinates), print the numbers, and say in a text cell whether "
    "you grabbed plain, shadow, or rim — before rendering it to check."),
 code("# your turn\n"),
 md("## 5. The build\nThe cell below prints a mystery 8×8 block. On paper or in "
    "a text cell: where is the shadow, where is the rim, and how did you know? "
    "Then render it and check yourself.\n\n**Turn-in:** your marked-up reading "
    "and the reveal."),
 code("mystery = img[54:62, 24:32].astype(int)\nprint(mystery)\n"
      "# When you have committed your reading, render it:\n"
      "# plt.imshow(mystery, cmap=\"gray\", vmin=0, vmax=255); plt.show()"),
])

# ---------------------------------------------------------------- img2
nb('img2-craters', [
 md("# Week 2 — Find the craters\n" + HDR),
 md("## 1. The terrain (same generator as last week)"),
 code(MAKE_TERRAIN),
 md("## 2. Threshold — one comparison, every pixel\nThe histogram's valley sat "
    "near 100. Everything below it becomes True."),
 code("import matplotlib.pyplot as plt\n\nTHRESHOLD = 100\n"
      "mask = img < THRESHOLD\n"
      "print(mask.sum(), \"shadow pixels of\", mask.size)\n\n"
      "plt.figure(figsize=(5, 5))\nplt.imshow(mask, cmap=\"gray\")\n"
      "plt.title(\"True = candidate shadow\")\nplt.show()"),
 md("## 3. Group touching pixels into blobs"),
 code(FLOOD),
 code("blobs = find_blobs(mask)\nprint(len(blobs), \"blobs before any filtering\")\n"
      "print(\"blob sizes:\", sorted(len(b) for b in blobs)[::-1][:12], \"...\")"),
 md("## 4. The size filter — specks are not craters"),
 code("MIN_SIZE = 12\n"
      "craters = [b for b in blobs if len(b) >= MIN_SIZE]\n"
      "print(len(blobs), \"blobs →\", len(craters), \"detections after the size filter\")\n"
      "print(\"True crater count in this terrain: 5\")"),
 md("## 5. See the detections"),
 code("overlay = np.stack([img, img, img], axis=-1) / 255\n"
      "for b in craters:\n"
      "    for y, x in b:\n"
      "        overlay[y, x] = [0.85, 0.16, 0.12]\n"
      "plt.figure(figsize=(5, 5))\nplt.imshow(overlay)\n"
      "plt.title(f\"{len(craters)} detections\")\nplt.show()"),
 md("## 6. The build — a field you haven't seen\nA fresh terrain, crater count "
    "hidden. Tune THRESHOLD and MIN_SIZE, report the count, and defend both "
    "settings in two sentences (histogram valley; what the size filter costs).\n\n"
    "**Turn-in:** detection image + settings + defense."),
 code("secret = make_terrain([(15, 15, 7), (70, 20, 9), (45, 45, 12),\n"
      "                       (20, 75, 6), (78, 78, 8), (60, 68, 4)],\n"
      "                      seed=42, noise=18, specks=0.01)\n"
      "# your detector here — histogram first, then threshold, blobs, filter, count\n"),
])

# ---------------------------------------------------------------- img3
nb('img3-classifier', [
 md("# Week 3 — Teach a machine to sort\n" + HDR),
 md("## 1. Labeled patches\nSmall crater and not-crater patches — plus labels, "
    "the machine's only source of truth."),
 code("import numpy as np\n\n"
      "def make_patch(kind, seed, size=15):\n"
      "    rng = np.random.default_rng(seed)\n"
      "    p = 175 + rng.integers(-20, 20, (size, size)).astype(float)\n"
      "    yy, xx = np.mgrid[0:size, 0:size]\n"
      "    c = size // 2\n"
      "    if kind == \"crater\":\n"
      "        d = np.sqrt((xx - c) ** 2 + (yy - c) ** 2)\n"
      "        p[(d < 4.5) & (xx < c)] = 60\n"
      "        p[(d < 4.5) & (xx >= c)] = 220\n"
      "        p[(d >= 4.5) & (d < 5.5) & (xx > c)] = 238\n"
      "    else:                       # a ridge shadow — dark but not round\n"
      "        p[:, c - 1:c + 2] = 95 + rng.integers(-10, 10, (size, 3))\n"
      "    return np.clip(p, 0, 255)\n\n"
      "train = [(make_patch(k, s), k) for s, k in enumerate(\n"
      "    [\"crater\", \"ridge\", \"crater\", \"ridge\", \"crater\", \"ridge\",\n"
      "     \"crater\", \"ridge\", \"crater\", \"ridge\"])]\n"
      "test  = [(make_patch(k, 100 + s), k) for s, k in enumerate(\n"
      "    [\"crater\", \"ridge\", \"ridge\", \"crater\", \"crater\", \"ridge\"])]\n"
      "print(len(train), \"training patches,\", len(test), \"held-out patches\")"),
 md("## 2. Features — turn each patch into two numbers"),
 code("def features(p):\n"
      "    dark = p < 110\n"
      "    if not dark.any():\n"
      "        return np.array([0.0, 0.0])\n"
      "    ys, xs = np.nonzero(dark)\n"
      "    spread_y = ys.std() + 1e-9\n"
      "    spread_x = xs.std() + 1e-9\n"
      "    roundness = min(spread_x, spread_y) / max(spread_x, spread_y)\n"
      "    dark_frac = dark.mean()\n"
      "    return np.array([roundness, dark_frac])\n\n"
      "for p, k in train[:4]:\n"
      "    print(k, features(p).round(2))"),
 md("A crater's shadow is compact-round (roundness near 1); a ridge's is a "
    "stripe (roundness low). The feature already separates them — the machine "
    "just has to notice."),
 md("## 3. Train nearest-mean — the smallest real learner"),
 code("crater_mean = np.mean([features(p) for p, k in train if k == \"crater\"], axis=0)\n"
      "ridge_mean  = np.mean([features(p) for p, k in train if k == \"ridge\"], axis=0)\n"
      "print(\"crater mean:\", crater_mean.round(2))\n"
      "print(\"ridge  mean:\", ridge_mean.round(2))\n\n"
      "def classify(p):\n"
      "    f = features(p)\n"
      "    d_c = np.linalg.norm(f - crater_mean)\n"
      "    d_r = np.linalg.norm(f - ridge_mean)\n"
      "    return \"crater\" if d_c < d_r else \"ridge\""),
 md("## 4. Grade it — held-out only"),
 code("correct = sum(classify(p) == k for p, k in test)\n"
      "print(f\"Held-out score: {correct} of {len(test)}\")"),
 md("## 5. The two sabotages\n**A.** Grade on training data and compare. "
    "**B.** Flip two training labels, retrain, re-grade on the held-out set."),
 code("train_score = sum(classify(p) == k for p, k in train)\n"
      "print(f\"Score on its own training data: {train_score} of {len(train)}\")\n"
      "# B: flip two labels in `train`, rerun the training cell, and re-grade\n"),
 md("## 6. The build\nReport (5–8 sentences): the honest score, the two "
    "sabotage scores, and what each dishonesty teaches about machine learning "
    "claims you meet in the wild.\n\n**Turn-in:** report + screenshots of the "
    "three scores."),
])

# ---------------------------------------------------------------- img4
nb('img4-capstone', [
 md("# Week 4 — New worlds, honest claims\n" + HDR),
 md("## 1. New terrain — rougher, fainter, junkier\nEverything you built this "
    "month, against ground it wasn't tuned on."),
 code(MAKE_TERRAIN.replace(
     "CRATERS = [(20, 18, 8), (55, 25, 11), (75, 70, 7), (30, 60, 9), (62, 48, 5)]\n"
     "img = make_terrain(CRATERS)",
     "# the new world: more noise, more specks, and three FAINT craters whose\n"
     "# shadows sit near ordinary-ground brightness — the ones a strict\n"
     "# threshold loses first\n"
     "TRUE_CRATERS = [(12, 20, 5), (35, 12, 7), (68, 18, 4), (25, 48, 8),\n"
     "                (52, 40, 5), (80, 52, 6), (15, 78, 4), (60, 74, 9), (84, 82, 4)]\n"
     "img = make_terrain(TRUE_CRATERS, seed=7, noise=22, specks=0.03)\n"
     "yy, xx = np.mgrid[0:90, 0:90]\n"
     "for cx, cy, r in [(68, 18, 4), (15, 78, 4), (84, 82, 4)]:   # the faint three\n"
     "    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)\n"
     "    img[(d < r) & (img < 110)] += 45\n"
     "# boulder shadows: dark-ish patches that are NOT craters — junk with size\n"
     "for bx, by in [(44, 70), (8, 44), (75, 35), (30, 28), (55, 12)]:\n"
     "    img[by:by + 3, bx:bx + 5] = 108")),
 code("import matplotlib.pyplot as plt\n\n"
      "plt.figure(figsize=(5, 5))\nplt.imshow(img, cmap=\"gray\", vmin=0, vmax=255)\n"
      "plt.title(\"The new world — 9 true craters, if you can defend them\")\nplt.show()\n"
      "plt.hist(img.ravel(), bins=40, color=\"#7E1B14\"); plt.title(\"Start here, as always\")\nplt.show()"),
 md("## 2. Your detector (bring week 2 forward)"),
 code(FLOOD),
 code("THRESHOLD = 100     # retune for THIS terrain — the old value is a guess here\n"
      "MIN_SIZE = 8\n"
      "mask = img < THRESHOLD\n"
      "blobs = find_blobs(mask)\n"
      "dets = [b for b in blobs if len(b) >= MIN_SIZE]\n"
      "print(len(dets), \"detections\")"),
 md("## 3. Measure your errors against the labeled strip\nThe true crater "
    "list is above (it is the labeled data). A detection counts as a hit if "
    "its pixels reach within 2 of a true center."),
 code("import numpy as np\n\n"
      "def score(dets, truths, tol=2):\n"
      "    hits = 0\n"
      "    used = set()\n"
      "    for i, (cx, cy, r) in enumerate(truths):\n"
      "        for b in dets:\n"
      "            ys = np.array([p[0] for p in b]); xs = np.array([p[1] for p in b])\n"
      "            if np.min(np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)) <= r + tol:\n"
      "                hits += 1\n"
      "                used.add(id(b))\n"
      "                break\n"
      "    false_alarms = sum(1 for b in dets if id(b) not in used)\n"
      "    return hits, len(truths) - hits, false_alarms\n\n"
      "hits, misses, fa = score(dets, TRUE_CRATERS)\n"
      "print(f\"hits {hits} · misses {misses} · false alarms {fa}\")"),
 md("## 4. Walk the seesaw\nTry 3–4 thresholds; record (threshold, misses, "
    "false alarms) for each; pick the one you can defend."),
 code("for T in (85, 95, 105, 115):\n"
      "    m = img < T\n"
      "    d = [b for b in find_blobs(m) if len(b) >= MIN_SIZE]\n"
      "    h, mi, f = score(d, TRUE_CRATERS)\n"
      "    print(f\"threshold {T}: {len(d)} detections — misses {mi}, false alarms {f}\")"),
 md("## 5. The build — the detection report\nWrite it like a professional: "
    "count, settings, miss rate, false-alarm rate, size floor, and the "
    "three-sentence finding (measured / found / not proven — remember this "
    "terrain is synthetic and the labels were free; on Titan nobody hands you "
    "TRUE_CRATERS).\n\n**Turn-in:** notebook + screenshot of detections and "
    "report. **This completes the sprint — Dr. Nixon's lecture list awaits.**"),
 md("**My report:**\n- Count: …\n- Settings: …\n- Misses: … / False alarms: …\n"
    "- Size floor: …\n- Finding: 1. Measured … 2. Found … 3. Not proven …"),
])

print("NOTEBOOKS2 DONE")
