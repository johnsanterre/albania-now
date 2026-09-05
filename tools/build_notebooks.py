#!/usr/bin/env python3
"""Albania Now — notebook builder. Writes the 8 sprint notebooks as .ipynb.
Run: python3 build_notebooks.py  (from albania/tools/; writes into albania/notebooks/)"""
import json, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SITE, 'notebooks')
os.makedirs(OUT, exist_ok=True)


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

# ---------------------------------------------------------------- ds1
nb('ds1-first-steps', [
 md("# Week 1 — Code in your browser\n" + HDR),
 md("**How this notebook works:** teaching cells you run, **YOUR TURN** cells "
    "you write, and **CHECK** cells that grade your work on the spot — if a "
    "CHECK cell prints PASSED, you got it; if it shows red, read the report "
    "and fix your cell above. Expect about an hour if you do everything."),
 md("## 1. Press play\nClick the cell below, then the play button (or Shift+Enter)."),
 code('print("Hello from a Google computer")'),
 md("The code ran in a data center, not on your machine. Only the text came "
    "back. Nothing you do in here can break your computer — the worst case is "
    "red text, and red text is a report."),
 md("## 2. Python is a calculator that reads"),
 code("2026 - 2010   # the last line of a cell shows its value"),
 code('print("If you were born in 2010 you are", 2026 - 2010, "years old")'),
 code("print(10 / 4)    # division ALWAYS gives a decimal — even 8 / 4 gives 2.0"),
 md("**YOUR TURN:** in one cell, compute how many days old you roughly are "
    "(years × 365) and print it in a sentence."),
 code("# your turn\n"),
 md("## 3. Variables — the notebook's memory\n`=` means *store*, not equals. "
    "The last store wins. Quotes decide name-lookup vs literal text."),
 code('city = "Tirana"\npeople = 560000\nprint(city, "has about", people, "people")'),
 code('x = 4\nx = x + 3     # take what x holds, add 3, store it back\nprint(x)'),
 code('emri = "Ana"\nprint(emri)      # looks up the name\nprint("emri")    # quotes = the text itself'),
 md("**YOUR TURN:** fill in the three variables, then run the CHECK cell."),
 code('emri = ""      # your name, in the quotes\nmosha = 0      # your age, no quotes\n'
      'qyteti = ""    # your town, in the quotes\n\n'
      'print(emri, "is", mosha, "and lives in", qyteti)'),
 code('# CHECK — run me after filling in the cell above\n'
      'assert emri != "", "emri is still empty — put your name in the quotes"\n'
      'assert not isinstance(mosha, str), "mosha is in quotes — that makes it text, not a number"\n'
      'assert mosha > 0, "mosha is still 0 — set your age (no quotes: it is a number)"\n'
      'assert qyteti != "", "qyteti is still empty"\n'
      'print("PASSED — three variables live in memory, and one is a real number")'),
 md("## 4. Text vs numbers — and the bridges\n`7` is a number, `\"7\"` is text. "
    "`+` adds two numbers or glues two texts, and refuses to mix. `str()` and "
    "`int()` are the bridges."),
 code('print(7 + 7)        # math\nprint("7" + "7")    # gluing text'),
 code('print("Age " + str(16))   # str() turns a number into text — now + can glue'),
 code('mosha_text = "16"\nprint(int(mosha_text) + 1)   # int() goes the other way'),
 code('print("Va" * 3)     # multiplying text repeats it — real, and really useful'),
 md("**YOUR TURN:** make one line that prints `====================` (20 equals "
    "signs) WITHOUT typing 20 of them, then run the CHECK."),
 code('line = ""   # your one expression here, e.g. something * something\nprint(line)'),
 code('# CHECK\nassert line == "=" * 20, "line should be exactly 20 = signs — use text multiplication"\n'
      'print("PASSED — you just wrote your first shortcut")'),
 md("## 5. The error safari — read three reports on purpose\nRun each broken "
    "cell. **Do not fix it until you have read the red text**: what stopped it, "
    "which line, what does it suggest? Then fix it and rerun. *(Runtime → Run "
    "all will stop at the first broken cell — that is expected; run this "
    "section cell by cell.)*"),
 code('print(vitet)          # broken on purpose: what KIND of error is this?'),
 code('print("age: " + 16)   # broken on purpose: a different kind — read, then fix two ways'),
 code('print(5 +              # broken on purpose: a third kind — the line ends mid-thought'),
 md("Three reports, three kinds: **NameError** (a name Python has never seen), "
    "**TypeError** (text glued to a number), **SyntaxError** (the sentence "
    "itself is malformed). You will meet all three for the rest of your life — "
    "on first-name terms is better."),
 md("## 6. Cells run in the order YOU run them\nRun the SECOND cell below "
    "first, watch it fail, then run the first, then the second again. Haunted "
    "notebooks are cured by **Runtime → Restart and run all**."),
 code('kryeqyteti = "Tirana"'),
 code('print(kryeqyteti)   # NameError if the cell above has not run yet'),
 md("## 7. Lab B — the receipt printer\nEverything this week in one artifact: "
    "variables, str(), text repetition, and print. First the teaching example:"),
 code('artikull = "byrek"\ncmim = 120\n\nprint("=" * 24)\nprint("PRANVERA MARKET")\n'
      'print("=" * 24)\nprint(artikull + "  " + str(cmim) + " lek")'),
 md("**YOUR TURN — Lab B:** two items with prices, divider lines, and a total "
    "line. The rule: the total must be *computed* from the price variables, "
    "never typed as a number. Then run the CHECK."),
 code('# Lab B — your receipt\nartikull1 = ""\ncmim1 = 0\nartikull2 = ""\ncmim2 = 0\n'
      'total = 0    # compute it from the two prices\n\n'
      '# build your receipt with print lines here\n'),
 code('# CHECK — Lab B\nassert artikull1 != "" and artikull2 != "", "name both items"\n'
      'assert cmim1 > 0 and cmim2 > 0, "give both prices (numbers, no quotes)"\n'
      'assert total == cmim1 + cmim2, "total must be COMPUTED from the two prices"\n'
      'print("PASSED — receipt math checks out")'),
 md("## 8. Lab C — the fix-me clinic\nThree cells, each hiding one bug. The "
    "protocol, every time: **run it, read the report out loud, then repair "
    "it** — and prove the repair with the CHECK underneath."),
 code('# FIX ME 1 — run it, read the report, repair it\n'
      'pershendetje = "Mirëdita\nprint(pershendetje)'),
 code('# CHECK — fix 1\nassert pershendetje == "Mirëdita"\n'
      'print("PASSED — the quote is closed")'),
 code('# FIX ME 2 — run, read, repair (the total should be the number 150)\n'
      'total_lek = "100" + 50\nprint(total_lek)'),
 code('# CHECK — fix 2\nassert total_lek == 150, "total_lek should be the NUMBER 150"\n'
      'print("PASSED — bridged with int()")'),
 code('# FIX ME 3 — nothing is misspelled; the problem is ORDER. Repair it.\n'
      'print(qytet)\nqytet = "Berat"'),
 code('# CHECK — fix 3\nassert qytet == "Berat"\n'
      'print("PASSED — defined before used")'),
 md("## 9. The build — three parts (this is the turn-in)\n**Part A — scale.** "
    "Print a sentence about your town 500 times, then the numbers 1 to 500. "
    "Not taught yet, on purpose: ask an AI assistant or search, and understand "
    "**every word** before keeping it."),
 code("# Part A\n"),
 md("**Part B — the mad-lib.** Your three variables from section 3, one print "
    "that weaves them into a sentence. Change the values, rerun, watch the "
    "sentence follow."),
 code("# Part B\n"),
 md("**Part C — the error safari, yours.** Cause a NameError, a TypeError, and "
    "a SyntaxError on purpose (three cells). Under each, a text cell with one "
    "sentence reading the report."),
 code("# Part C — error 1\n"),
 code("# Part C — error 2\n"),
 code("# Part C — error 3\n"),
 md("**Turn-in:** screenshots of all three parts to your teacher.\n\n"
    "**Stretch (optional):** print a countdown from 10 to 1, each on its own "
    "line, ending with the word `Fest!` — the hint is that `range` can count "
    "backwards; ask your AI partner how, and make it explain until you could "
    "teach it."),
 code("# stretch\n"),
])

# ---------------------------------------------------------------- ds2
CITIES = ("city,region,population,coastal\nTirana,Central,560000,no\n"
          "Durres,Coast,200000,yes\nVlore,Coast,130000,yes\nElbasan,Central,140000,no\n"
          "Shkoder,North,135000,no\nFier,South,120000,no\nKorce,Southeast,75000,no\n"
          "Sarande,Coast,40000,yes\n")
nb('ds2-tables', [
 md("# Week 2 — Tables\n" + HDR),
 md("## 1. Load the table\npandas is Python's table tool. The table is 8 Albanian "
    "cities (populations rounded, for practice)."),
 code('import pandas as pd\nimport io\n\ncsv = """' + CITIES + '"""\n'
      'df = pd.read_csv(io.StringIO(csv))\ndf'),
 md("One row per city, one column per fact. `len(df)` counts rows — count before "
    "and after every filter."),
 code("len(df)"),
 md("## 2. Filter — keep rows that pass a test"),
 code('coastal = df[df["coastal"] == "yes"]\ncoastal'),
 code('big = df[df["population"] > 100000]\nprint(len(df), "rows in,", len(big), "rows out")\nbig'),
 md("## 3. Sort — same rows, new order"),
 code('df.sort_values("population", ascending=False)'),
 md("## 4. Group — fold the table and summarize each pile"),
 code('df.groupby("region")["population"].mean().round(0)'),
 code('df.groupby("region").size()'),
 md("## 5. The build — three questions, with receipts\nAnswer three questions "
    "using this table: one filter, one sort, one group. Write each question as a "
    "text cell, the code under it, the output as the receipt.\n\n"
    "**Turn-in:** screenshot of questions, code, and outputs."),
 md("**Question 1:** (write it here)"),
 code("# question 1\n"),
 md("**Question 2:**"),
 code("# question 2\n"),
 md("**Question 3:**"),
 code("# question 3\n"),
])

# ---------------------------------------------------------------- ds3
nb('ds3-charts', [
 md("# Week 3 — Charts that tell the truth\n" + HDR),
 md("## 1. The honest bar chart\nTwo shops: A sold 96, B sold 100."),
 code("import matplotlib.pyplot as plt\n\nshops = [\"Shop A\", \"Shop B\"]\nsales = [96, 100]\n\n"
      "plt.bar(shops, sales, color=[\"#D8291F\", \"#7E1B14\"])\n"
      "plt.ylabel(\"items sold (July)\")\nplt.title(\"Honest: axis starts at 0\")\nplt.show()"),
 md("## 2. The same numbers, lying\nOne line changes: where the axis starts."),
 code("plt.bar(shops, sales, color=[\"#D8291F\", \"#7E1B14\"])\n"
      "plt.ylabel(\"items sold (July)\")\nplt.ylim(90, 101)   # the chop\n"
      "plt.title(\"Chopped: same data, different story\")\nplt.show()"),
 md("## 3. A line chart — change over time"),
 code("weeks = [1, 2, 3, 4]\nvisits = [120, 135, 128, 160]\n\n"
      "plt.plot(weeks, visits, marker=\"o\", color=\"#7E1B14\")\n"
      "plt.xlabel(\"week\")\nplt.ylabel(\"library visits\")\nplt.xticks(weeks)\nplt.show()"),
 md("## 4. A scatter — relationship\nEach dot is one of last week's cities: "
    "population across, a (invented, for practice) count of high schools up."),
 code("pop = [560, 200, 130, 140, 135, 120, 75, 40]        # thousands\n"
      "schools = [48, 19, 12, 14, 13, 11, 8, 4]\n\n"
      "plt.scatter(pop, schools, color=\"#D8291F\")\n"
      "plt.xlabel(\"population (thousands)\")\nplt.ylabel(\"high schools\")\nplt.show()"),
 md("The cloud leans — bigger cities, more schools. A relationship, not a cause."),
 md("## 5. The build — one honest chart, one liar, one caption\nPick any numbers "
    "(real or invented). Draw the comparison honestly, then chopped. Under them, "
    "a two-sentence caption naming what the chopped one does to the viewer.\n\n"
    "**Turn-in:** screenshot of both charts and the caption."),
 code("# the build\n"),
])

# ---------------------------------------------------------------- ds4
nb('ds4-capstone', [
 md("# Week 4 — A real analysis, start to finding\n" + HDR),
 md("## 1. The data\nOne month of a small (fictional) Tirana shop: 120 rows — "
    "30 days × 4 products. Generated, so every class gets the same table."),
 code("import pandas as pd\n\ndays = list(range(1, 31))\n"
      "weekday = [\"Mon\",\"Tue\",\"Wed\",\"Thu\",\"Fri\",\"Sat\",\"Sun\"]\n"
      "products = [(\"byrek\", 120), (\"coffee\", 150), (\"juice\", 180), (\"ice cream\", 200)]\n"
      "rows = []\nfor d in days:\n    wd = weekday[(d - 1) % 7]\n"
      "    for i, (prod, price) in enumerate(products):\n"
      "        base = 20 + 8 * ((d * 7 + i * 13) % 5)\n"
      "        if wd in (\"Sat\", \"Sun\"): base += 15\n"
      "        if prod == \"ice cream\": base += d // 3   # warming month\n"
      "        rows.append([d, wd, prod, base, price])\n"
      "df = pd.DataFrame(rows, columns=[\"day\", \"weekday\", \"product\", \"units\", \"price_lek\"])\n"
      "df[\"revenue_lek\"] = df[\"units\"] * df[\"price_lek\"]\n"
      "print(len(df), \"rows\")\ndf.head()"),
 md("## 2. The loop, walked once\n**Question:** which weekday earns the most?"),
 code('by_day = df.groupby("weekday")["revenue_lek"].mean().sort_values(ascending=False)\nby_day'),
 code("import matplotlib.pyplot as plt\n\nby_day.plot(kind=\"bar\", color=\"#7E1B14\")\n"
      "plt.ylabel(\"mean revenue (lek)\")\nplt.title(\"Mean daily revenue by weekday — one month, one shop\")\nplt.show()"),
 md("**The finding, three sentences:**\n1. *Measured:* mean daily revenue by "
    "weekday, one month, one shop, 120 rows.\n2. *Found:* weekend days average "
    "the highest revenue.\n3. *Not proven:* that this holds in other months, other "
    "shops, or that the weekend causes it — school holidays, weather, and tourism "
    "all moved together this month."),
 md("## 3. The build — your analysis\nYour question about this table (or a dataset "
    "you found yourself — Kaggle and INSTAT both work). Filters with counts shown, "
    "a group, one honest chart, and the three-sentence finding.\n\n"
    "**Turn-in:** this notebook (File → Download .ipynb) + a screenshot of chart "
    "and finding. **This completes the sprint — the lecture list awaits.**"),
 md("**My question:**"),
 code("# your analysis — filters (show counts!), group, chart\n"),
 md("**My finding:**\n1. Measured: …\n2. Found: …\n3. Not proven: …"),
])

# ---------------------------------------------------------------- space1
nb('space1-spectra', [
 md("# Week 1 — How we know, without going\n" + HDR),
 md("## 1. Build a spectrum\nBrightness across wavelength — smooth starlight, "
    "before any gas touches it."),
 code("import numpy as np\nimport matplotlib.pyplot as plt\n\n"
      "wl = np.linspace(1.0, 5.0, 400)       # wavelength, micrometers (infrared)\n"
      "star = 1.0 - 0.05 * (wl - 3.0) ** 2    # smooth starlight\n\n"
      "plt.plot(wl, star, color=\"#7E1B14\")\nplt.xlabel(\"wavelength (micrometers)\")\n"
      "plt.ylabel(\"brightness\")\nplt.title(\"Starlight, untouched\")\nplt.show()"),
 md("## 2. Pass it through methane\nMethane steals light near 2.3 and 3.3 "
    "micrometers — its infrared fingerprint. We carve those dips in:"),
 code("def dip(wl, center, width, depth):\n"
      "    return depth * np.exp(-((wl - center) / width) ** 2)\n\n"
      "seen = star - dip(wl, 2.3, 0.08, 0.25) - dip(wl, 3.3, 0.12, 0.45)\n\n"
      "plt.plot(wl, star, color=\"#B9B2A6\", label=\"before the gas\")\n"
      "plt.plot(wl, seen, color=\"#D8291F\", label=\"after methane\")\n"
      "plt.xlabel(\"wavelength (micrometers)\")\nplt.ylabel(\"brightness\")\n"
      "plt.legend()\nplt.title(\"The fingerprint\")\nplt.show()"),
 md("## 3. Find the thief by code\nWhere is the deepest bite?"),
 code("deepest = wl[np.argmin(seen)]\nprint(\"Deepest absorption at\", round(deepest, 2), \"micrometers\")"),
 md("That number — 3.3 — is how a spectrum names its gas: look up which molecule "
    "bites there, and methane is the answer. This is what Cassini's CIRS did at "
    "Titan, in the infrared, for thirteen years."),
 md("## 4. Your turn — a second gas\nCarbon dioxide bites near 4.3 micrometers. "
    "Add a CO2 dip (center 4.3, width 0.1, depth 0.35) to the spectrum, plot it, "
    "and confirm by code where the TWO deepest bites now sit."),
 code("# your turn\n"),
 md("## 5. The build\nThe build for this week is written, not coded: five to eight "
    "sentences explaining the trick to a younger student (spectrum, dark lines, one "
    "real example). See the lesson page.\n\n**Turn-in:** the paragraph."),
])

# ---------------------------------------------------------------- space2
nb('space2-missions', [
 md("# Week 2 — Missions and instruments\n" + HDR),
 md("## 1. How far is far\nAverage distances from Earth, in millions of km "
    "(they change as planets orbit — these are rough means for the math)."),
 code("import matplotlib.pyplot as plt\n\n"
      "worlds = [\"Moon\", \"Venus\", \"Mars\", \"Jupiter\", \"Saturn\", \"Neptune\"]\n"
      "dist_mkm = [0.384, 41, 78, 628, 1280, 4350]   # millions of km, rough averages\n"
      "SPEED = 300000   # km per second — light, and radio\n\n"
      "delay_min = [d * 1e6 / SPEED / 60 for d in dist_mkm]\n"
      "for w, m in zip(worlds, delay_min):\n"
      "    print(f\"{w:8s}  one-way radio delay ≈ {m:8.1f} minutes\")"),
 code("plt.bar(worlds, delay_min, color=\"#7E1B14\")\n"
      "plt.ylabel(\"one-way delay (minutes)\")\n"
      "plt.title(\"Why nobody joysticks a Saturn probe\")\nplt.show()"),
 md("## 2. The conversation test\nA rover sees a cliff and asks Earth what to do. "
    "How long until the answer arrives? (Round trip = twice the delay.)"),
 code("saturn = delay_min[4]\nprint(\"Saturn round trip:\", round(2 * saturn), \"minutes —\",\n"
      "      round(2 * saturn / 60, 1), \"hours between question and answer\")"),
 md("## 3. Your turn\nCompute the round-trip delay for Mars in minutes. Then: the "
    "Huygens probe descended through Titan's atmosphere for about 2.5 hours. Could "
    "Earth have steered it? Show the arithmetic that answers it."),
 code("# your turn\n"),
 md("## 4. The build — your mission card\nWritten, not coded: a world, a sharp "
    "question, the ladder rung (flyby / orbiter / lander / sample return), two "
    "instruments and what each answers, one risk. One page. See the lesson page.\n\n"
    "**Turn-in:** the mission card."),
])

# ---------------------------------------------------------------- space3
nb('space3-titan', [
 md("# Week 3 — Titan, by the numbers\n" + HDR),
 md("## 1. Your weight on Titan\nTitan's surface gravity is about 1.35 m/s² — "
    "Earth's is 9.81."),
 code("my_mass_kg = 60          # change to yours\n\n"
      "earth_weight = my_mass_kg * 9.81\n"
      "titan_weight = my_mass_kg * 1.35\n"
      "print(f\"Earth:  {earth_weight:6.0f} newtons\")\n"
      "print(f\"Titan:  {titan_weight:6.0f} newtons — about \"\n"
      "      f\"{titan_weight / earth_weight:.0%} of home\")"),
 md("You would weigh about a seventh of your Earth weight — and the air is one and "
    "a half times as thick. Humans on Titan could strap on wings and fly with their "
    "arms. That is not fiction; it is these two numbers."),
 md("## 2. How cold is −179 °C, really"),
 code("titan_c = -179\n"
      "titan_k = titan_c + 273.15\n"
      "water_freezes_k = 273.15\n"
      "methane_liquid_k = (90.7, 111.7)   # liquid range at 1 atm, kelvin\n\n"
      "print(\"Titan surface:\", titan_k, \"K\")\n"
      "print(\"Water freezes:\", water_freezes_k, \"K — Titan is\", \n"
      "      round(water_freezes_k - titan_k), \"K below: water is ROCK there\")\n"
      "print(\"Methane is liquid between\", *methane_liquid_k, \n"
      "      \"K — Titan sits right in the rain zone\")"),
 md("## 3. The report takes an hour\nCassini flies past Titan and radios home. "
    "Saturn averages ~1,280 million km from Earth."),
 code("delay_min = 1280e6 / 300000 / 60\n"
      "print(f\"Titan's news reaches Earth ≈ {delay_min:.0f} minutes later\")"),
 md("## 4. Your turn\nKraken Mare's surface is liquid methane at ~92 K. Using the "
    "numbers above: is that within methane's liquid range? And your weight on the "
    "Moon (gravity 1.62 m/s²) — closer to Titan or to Earth?"),
 code("# your turn\n"),
 md("## 5. The build — a postcard from Titan\nSix to ten sentences from a research "
    "station on Titan. Every claim traces to a number or fact from this lesson or "
    "notebook. See the lesson page.\n\n**Turn-in:** the postcard."),
])

# ---------------------------------------------------------------- space4
nb('space4-transit', [
 md("# Week 4 — Find a planet in the data\n" + HDR),
 md("## 1. Thirty days of starlight\nBrightness measured every 72 minutes for a "
    "month (synthetic but realistic — same shape as Kepler data)."),
 code("import numpy as np\nimport matplotlib.pyplot as plt\n\n"
      "N = 600\n"
      "t_days = np.arange(N) * 30 / N\n"
      "rng = np.sin(np.arange(N) * 12.9898) * 43758.5453\n"
      "noise = (rng - np.floor(rng) - 0.5) * 6          # the star's flicker\n"
      "flux = 1000 + noise\n"
      "for center in (80, 280, 480):                     # something passes in front…\n"
      "    mask = np.abs(np.arange(N) - center) < 7\n"
      "    flux[mask] -= 12\n\n"
      "plt.figure(figsize=(10, 3.2))\n"
      "plt.plot(t_days, flux, lw=0.8, color=\"#7E1B14\")\n"
      "plt.xlabel(\"time (days)\")\nplt.ylabel(\"brightness\")\nplt.title(\"One star, one month\")\nplt.show()"),
 md("## 2. Detect the dips\nA threshold, exactly like the figure on the lesson page:"),
 code("THRESHOLD = 991\n\n"
      "below = flux < THRESHOLD\n"
      "starts = np.where(below & ~np.roll(below, 1))[0]\n"
      "print(\"Dip starts at samples:\", starts)\n"
      "print(\"Dip starts at days:   \", np.round(t_days[starts], 1))"),
 md("## 3. Period and depth"),
 code("period_days = np.diff(t_days[starts]).mean()\n"
      "depth = 1000 - flux[below].mean()\n"
      "depth_frac = depth / 1000\n"
      "print(f\"Period ≈ {period_days:.1f} days — the planet's year\")\n"
      "print(f\"Depth ≈ {depth:.1f} units = {depth_frac:.3%} of the light\")"),
 md("## 4. The size, from the square-root rule"),
 code("radius_ratio = np.sqrt(depth_frac)\n"
      "print(f\"Planet radius ≈ {radius_ratio:.2%} of the star's radius\")\n"
      "print(\"For a Sun-like star that is roughly Jupiter-sized\")"),
 md("## 5. The build — your detection\nRerun the detection with a threshold YOU "
    "chose (justify it in a text cell), then write the finding:\n"
    "1. *Measured:* …\n2. *Found:* … (period, depth, size)\n3. *Not proven:* … "
    "(candidate vs confirmed — say why)\n\n"
    "**Turn-in:** this notebook + a screenshot of plot and finding. **This "
    "completes the sprint — Dr. Nixon's lecture list awaits.**"),
 md("**My finding:**\n1. Measured: …\n2. Found: …\n3. Not proven: …"),
])

print("NOTEBOOKS DONE")
