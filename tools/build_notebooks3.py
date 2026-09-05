#!/usr/bin/env python3
"""Albania Now — sprint 6 notebooks (Learning to Read Python).
The pattern: student STORES a prediction in a variable, the program runs,
a CHECK compares prediction to reality. Committed predictions, honest scores.
Run: python3 build_notebooks3.py"""
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
       "Run cells top to bottom. First: **File → Save a copy in Drive**.*\n\n"
       "**The rule of this notebook:** store your prediction BEFORE running the "
       "program cell. The CHECK compares your committed prediction to reality — "
       "that comparison is the entire lesson.")


def drill(num, program, answer_expr, pred_name, hint=''):
    """One prediction drill: predict cell -> program cell -> CHECK cell."""
    return [
        md("### Drill %d\nTrace on paper, then commit:%s" % (num, ('\n\n*' + hint + '*') if hint else '')),
        code("# PREDICT %d — replace None with what the program will print\n%s = None" % (num, pred_name)),
        code(program),
        code("# CHECK %d\nassert %s is not None, 'commit a prediction first'\n"
             "assert %s == %s, f'you predicted {%s!r} — the machine says otherwise: trace again'\n"
             "print('PASSED — your trace matched the machine')"
             % (num, pred_name, pred_name, answer_expr, pred_name)),
    ]


# ---------------------------------------------------------------- read1
cells = [md("# Week 1 — Trace like the machine\n" + HDR)]
cells += drill(1, 'a = 3\nb = a + 2\na = 10\nrezultati = a + b\nprint(rezultati)',
               '15', 'pred_1', 'b takes a snapshot')
cells += drill(2, 'x = 1\nx = x + x\nx = x + x\nx = x + x\nprint(x)', '8', 'pred_2')
cells += drill(3, 'emri = "Blerta"\ngjatesia = len(emri)\nrezultati = emri + " " + str(gjatesia)\nprint(rezultati)',
               '"Blerta 6"', 'pred_3', 'len counts letters; predict the full printed text, in quotes')
cells += drill(4, 'a = "5"\nb = a * 3\nprint(b)', '"555"', 'pred_4', 'quotes make it text')
cells += drill(5, 'x = 10\ny = x\nx = x - 4\nrezultati = x + y\nprint(rezultati)', '16', 'pred_5')
cells += drill(6, 'fjala = "Va"\nkenga = fjala * 2 + "!"\nprint(kenga)', '"VaVa!"', 'pred_6')
cells += drill(7, 'a = 7\nb = 2\nrezultati = a // b\nprint(rezultati)', '3', 'pred_7',
               'double slash drops the fraction')
cells += drill(8, 'x = 4\nx = x * x\nx = x - 6\nprint(x)', '10', 'pred_8')
cells += drill(9, 'mosha = "16"\nmosha_ri = int(mosha) + 1\nprint(mosha_ri)', '17', 'pred_9')
cells += drill(10, 'a = 2\nb = 3\na = b\nb = a\nrezultati = str(a) + str(b)\nprint(rezultati)',
               '"33"', 'pred_10', 'the classic non-swap — trace it slowly')
cells += [
 md("## The build — the traced program\nThe longest program of the week. Trace "
    "it ON PAPER first — every line, the whiteboard after each store, the final "
    "output. Photograph the paper. THEN run it."),
 code('cmimet = [120, 150, 180, 90]\ntotal = 0\nme_i_shtrenjte = 0\n'
      'for cmim in cmimet:\n    total = total + cmim\n'
      '    if cmim > me_i_shtrenjte:\n        me_i_shtrenjte = cmim\n'
      'mesatarja = total / len(cmimet)\n'
      'print("total:", total)\nprint("max:", me_i_shtrenjte)\nprint("mesatarja:", mesatarja)'),
 md("**Turn-in:** your paper trace next to the real output, plus one sentence on "
    "where (if anywhere) your trace diverged and why."),
]
nb('read1-trace-drills', cells)

# ---------------------------------------------------------------- read2
cells = [md("# Week 2 — Read the shapes\n" + HDR +
            "\n\nNew move this week: BEFORE the prediction, name the shape out "
            "loud — accumulator, or fork?")]
cells += drill(1, 'total = 0\nfor n in [4, 7, 2]:\n    total = total + n\nprint(total)',
               '13', 'pred_1', 'name the shape first')
cells += drill(2, 'numri = 0\nfor fjale in ["mire", "dita", "sot"]:\n    numri = numri + 1\nprint(numri)',
               '3', 'pred_2', 'an accumulator can count, not just sum')
cells += drill(3, 'mosha = 15\nif mosha >= 16:\n    print("mund te votosh ne disa vende")\nelse:\n    print("jo ende")',
               '"jo ende"', 'pred_3', 'read the test first; predict the printed text in quotes')
cells += drill(4, 'x = 9\nif x > 5:\n    x = x * 2\nprint(x)', '18', 'pred_4',
               'a fork with no else — what happens when the test is false?')
cells += drill(5, 'fjalia = ""\nfor fjale in ["sa", "mire"]:\n    fjalia = fjalia + fjale + " "\nprint(fjalia)',
               '"sa mire "', 'pred_5', 'accumulators build text too — watch the trailing space')
cells += drill(6, 'total = 0\nfor n in [3, 10, 4, 20]:\n    if n > 5:\n        total = total + n\nprint(total)',
               '30', 'pred_6', 'both shapes at once: a loop that counts only some')
cells += drill(7, 'i_madh = 0\nfor n in [12, 5, 19, 3]:\n    if n > i_madh:\n        i_madh = n\nprint(i_madh)',
               '19', 'pred_7', 'the find-the-biggest pattern — trace two passes, then decide')
cells += drill(8, 'x = 0\nfor n in [1, 2, 3]:\n    x = x + n\n    x = x + n\nprint(x)',
               '12', 'pred_8', 'TWO adds inside the loop — indentation is structure')
cells += [
 md("## The build — the shape catalog\nCopy one accumulator and one fork from "
    "above into the cells below, each with a one-line purpose comment. Then "
    "write ONE program of your own that uses both shapes at once, purpose "
    "comment on top."),
 code("# my accumulator example + purpose\n"),
 code("# my fork example + purpose\n"),
 code("# my combined program\n"),
]
nb('read2-shape-drills', cells)

# ---------------------------------------------------------------- read3
cells = [
 md("# Week 3 — Read code you didn't write\n" + HDR +
    "\n\nThree programs by another author. For each: read COLD first — names, "
    "load-bearing line, smells — and answer before running."),
 md("## Program 1 — the receipt totaler\nRead it. Do NOT run yet."),
 code('# by another author\ncmimet = [250, 120, 480, 95]\ntotal = 0\n'
      'for cmim in cmimet:\n    total = total + cmim\n'
      'zbritja = total * 0.10\nprint("Pagesa:", total - zbritja)'),
 code("# PREDICT — what number does it print?\npred_1 = None"),
 code('# CHECK 1\nassert pred_1 is not None, "commit first"\n'
      'assert pred_1 == 850.5, f"you predicted {pred_1!r} — trace the discount line again"\n'
      'print("PASSED")'),
 md("*Smell check: the 0.10 is a magic number — nothing says why 10%.*"),
 md("## Program 2 — the temperature converter\nRead cold. One of these two "
    "programs (2 or 3) hides a real bug."),
 code('# by another author\ncelsius = 25\nfahrenheit = celsius * 9 / 5 + 32\n'
      'print(celsius, "C =", fahrenheit, "F")'),
 code("# PREDICT — the fahrenheit value it prints\npred_2 = None"),
 code('# CHECK 2\nassert pred_2 is not None, "commit first"\n'
      'assert pred_2 == 77.0, f"you predicted {pred_2!r} — 25 * 9 / 5 + 32, left to right"\n'
      'print("PASSED")'),
 md("## Program 3 — the word counter\nRead cold. The author CLAIMS it counts "
    "how many words are longer than 3 letters."),
 code('# by another author — claimed: counts words longer than 3 letters\n'
      'fjalia = "sot eshte nje dite shume e mire"\nnumri = 0\n'
      'for fjale in fjalia.split():\n    if len(fjale) > 3:\n        numri = numri + 1\n'
      'print("fjale te gjata:", numri)'),
 code('# PREDICT — the number it prints (count by hand: sot/eshte/nje/dite/shume/e/mire)\npred_3 = None'),
 code('# CHECK 3\nassert pred_3 is not None, "commit first"\n'
      'assert pred_3 == 3, f"you predicted {pred_3!r} — which words have MORE than 3 letters (not 3 exactly)?"\n'
      'print("PASSED — eshte, dite, shume. The > is doing exactly what it says, not what you assume")'),
 md("## The build — the bug report\nOne of the three programs behaves "
    "differently from its author's claim for some inputs. (Hint: what should "
    "the word counter do with the word `dite`? What does `> 3` versus `>= 3` "
    "mean for a claim that says 'longer than 3'? Is the claim or the code "
    "right? Decide — and check program 1's discount against a receipt of ONE "
    "item costing 100.) Write the report: claim, actual behavior with proving "
    "input, load-bearing line, one-line fix."),
 code("# your investigation space\n"),
]
nb('read3-three-programs', cells)

# ---------------------------------------------------------------- read4
cells = [
 md("# Week 4 — Read the traceback, write the review\n" + HDR),
 md("## Traceback drill 1\nRun it. Read the report BOTTOM-UP, then commit."),
 code('# broken on purpose — run and read the full chain\n'
      'def total_line(cmimet):\n    return "Total: " + sum(cmimet)\n\n'
      'cmimet = [100, 200]\nprint(total_line(cmimet))'),
 code('# PREDICT — which line number does the FIXING start on? (the line inside total_line)\npred_1 = None'),
 code('# CHECK 1\nassert pred_1 is not None, "commit first"\n'
      'assert pred_1 == 2, f"you said line {pred_1!r} — climb to the line INSIDE the helper, where text met a number"\n'
      'print("PASSED — fix: \\"Total: \\" + str(sum(cmimet))")'),
 md("## Traceback drill 2"),
 code('# broken on purpose — a chain through two helpers\n'
      'def mesatarja(numrat):\n    return sum(numrat) / len(numrat)\n\n'
      'def raport(numrat):\n    return "Mesatarja: " + str(mesatarja(numrat))\n\n'
      'print(raport([]))'),
 code('# PREDICT — the KIND of error, as text: "NameError", "TypeError", "ZeroDivisionError", or "ValueError"\npred_2 = None'),
 code('# CHECK 2\nassert pred_2 is not None, "commit first"\n'
      'assert pred_2 == "ZeroDivisionError", f"you said {pred_2!r} — the empty list has len 0, and the division meets it"\n'
      'print("PASSED — and note the fix belongs in mesatarja: guard the empty case")'),
 md("## The review target\nA 20-line program that mostly works. Read it COLD — "
    "names, load-bearing lines, smells — before running. Your review has four "
    "parts: what it does, what's solid, what's wrong or smelly (line numbers + "
    "reasons; at least three findings exist), what you'd change first."),
 code('# by another author — the review target\n'
      'notat = [8, 9, 6, 10, 7, 9]\n\n'
      'total = 0\nfor nota in notat:\n    total = total + nota\n'
      'average = total\n'
      'mesatarja = total / len(notat)\n\n'
      'kalon = 0\nfor nota in notat:\n    if nota > 5:\n        kalon = kalon + 1\n\n'
      'print("Mesatarja:", mesatarja)\n'
      'print("Kalojne:", kalon, "nga", len(notat))\n'
      'print("Nota me e larta:", max(notat))\n'
      'shuma_e_katrorit = mesatarja * mesatarja * 0.25'),
 md("**Findings to hunt** (do not read until you have three of your own): a "
    "lying name that stores the wrong thing, a computed value never used, a "
    "magic number with no explanation."),
 md("## The build — the review + the fix\nWrite the four-part review in the "
    "cell below (as a text cell), make your ONE first change to the program, "
    "and show it running. This completes the sprint."),
 md("**My review:**\n1. What it does: …\n2. Solid: …\n3. Findings: …\n4. First change: …"),
 code("# the program, with your one change applied\n"),
]
nb('read4-traceback-review', cells)

print("NOTEBOOKS3 DONE")
