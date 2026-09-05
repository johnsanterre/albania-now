#!/usr/bin/env python3
"""Albania Now — watch-segment videos for both sprints (vidlib slides+narration).
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_sprints.py [slug]"""
import sys
from vidlib import s_title, s_bullets, s_chart, build_all

DS = {}
SP = {}

DS["alnow-ds-1"] = [
 (s_title("Week 1 · Data Science", "Code in your browser",
          "Real Python. A Google computer. Nothing to install."),
  "Welcome to week one of the data science sprint. This week you write real "
  "Python — in your browser, with nothing to install. The tool is called Colab: "
  "a notebook made of cells, and every code cell has a play button."),
 (s_bullets("The five facts", "What happens when you press play", [
   "Your code runs in a Google data center",
   "Only the result travels back to you",
   "Nothing you do can break your computer",
   "Red text is a report, not a judgment",
   "Cells run in the order YOU run them"]),
  "Five facts carry the whole week. Your code runs far away, in a data center. "
  "Only the result comes back. So nothing you do can break your machine — "
  "experiment freely. Red error text is a report that names what stopped the "
  "code, often with a suggested fix. And cells run in the order you run them, "
  "not the order they sit on the page — restart and run all is the cure."),
 (s_bullets("This week", "Your job", [
   "Read three error reports in the figure",
   "Run the notebook: print, variables, one error",
   "Build: make the computer work 500 times",
   "Turn in the screenshot"], closing=True),
  "Your job this week: read three error reports in the figure, run the notebook "
  "top to bottom, then the build — make the computer print something five "
  "hundred times, understand every word of how, and turn in the screenshot. "
  "Let's go."),
]

DS["alnow-ds-2"] = [
 (s_title("Week 2 · Data Science", "Tables",
          "Rows are things. Columns are facts. Three moves."),
  "Week two. Almost every dataset in the world is a table — one row per thing, "
  "one column per fact about it. Cities, football matches, hospital visits: "
  "rows and columns. And three moves answer nearly every question."),
 (s_bullets("The three moves", "Filter, sort, group", [
   "Filter — keep rows that pass a test",
   "Sort — same rows, new order",
   "Group — fold many rows into few",
   "Count before and after every filter",
   "Always know what one row IS"]),
  "Filter keeps only the rows that pass a test — coastal cities only. Sort "
  "reorders by a column — largest first. Group folds the table: pile up rows "
  "that share a value and summarize each pile — that is where findings come "
  "from. Two habits from day one: count rows before and after every filter, "
  "and always know what one row is. Those two habits prevent the wrong answers "
  "that look right."),
 (s_bullets("This week", "Your job", [
   "Push the three moves in the figure",
   "Run them in pandas on eight Albanian cities",
   "Build: three questions, with receipts",
   "Turn in the screenshot"], closing=True),
  "This week: push the moves around by hand in the figure, then run them for "
  "real in pandas on a table of eight Albanian cities. The build is three "
  "questions of your own — one filter, one sort, one group — with the output "
  "as the receipt."),
]

DS["alnow-ds-3"] = [
 (s_title("Week 3 · Data Science", "Charts that tell the truth",
          "A chart is a claim. Claims can lie with true numbers."),
  "Week three. A chart is not decoration — it is a claim about data, made "
  "visual. Bar charts compare things. Line charts show change over time. "
  "Scatter plots show relationships. And any of them can lie while every "
  "number on it is true."),
 (s_chart("The crime", "Same data, two stories",
          ["Shop A", "Shop B"], [96, 100],
          "Axis at zero: honest", compare_ylim=(90, 101),
          claim2="Axis at 90: a landslide",
          note="96 vs 100 — a 4% difference, twice"),
  "Here is the crime. Shop A sold ninety-six, shop B sold one hundred — a four "
  "percent difference. On the left, the axis starts at zero and the bars say "
  "so. On the right, the same two numbers with the axis starting at ninety — "
  "and suddenly B looks like a landslide. Nothing was faked. The picture is "
  "doing the lying. Bars must start at zero; that is their silent promise."),
 (s_bullets("This week", "Your job", [
   "Drag the chop yourself in the figure",
   "Draw honest and chopped in matplotlib",
   "Build: one truth, one lie, one caption",
   "Spot one chopped axis in the wild"], closing=True),
  "This week: drag the chopped axis yourself until you feel it, draw both "
  "versions in code, and for the build, make one honest chart and one liar "
  "from the same numbers — with a caption naming exactly what the liar does. "
  "Then keep your eyes open: you will start seeing this everywhere."),
]

DS["alnow-ds-4"] = [
 (s_title("Week 4 · Data Science", "A real analysis",
          "Question. Table. Moves. Picture. Finding."),
  "Capstone week. Everything you have learned becomes one machine — the loop "
  "that every real analysis runs, in a newsroom, a lab, or a company."),
 (s_bullets("The loop", "Question to finding", [
   "A sharp question you care about",
   "A table where you know what a row is",
   "Filter, group, sort — with counts",
   "One honest chart",
   "The finding: three sentences"]),
  "The loop: a sharp question — which weekday earns the most beats understand "
  "the shop. A table that could answer it. The moves, with row counts checked. "
  "One honest picture. And the finding in exactly three sentences: what I "
  "measured, what I found, and what this does not prove. That third sentence "
  "separates professionals from vibes. The data showed coastal sales were "
  "higher — it never tested whether the sea causes spending."),
 (s_bullets("This week", "Finish the sprint", [
   "Sort six claims: supported or too far",
   "Walk the loop once in the notebook",
   "Build: YOUR analysis, YOUR finding",
   "All four builds in = the lecture list"], closing=True),
  "This week: calibrate yourself on six claims in the figure, walk the loop "
  "once with the shop data, then take the wheel — your question, your chart, "
  "your three sentences. Turn it in, and that completes the sprint: you are on "
  "the list for the live lecture. Bring a question."),
]

SP["alnow-space-1"] = [
 (s_title("Week 1 · Planetary Exploration", "How we know, without going",
          "Light carries fingerprints. We read them."),
  "Welcome to the planetary exploration sprint. Week one starts with the trick "
  "under everything: how we know what a world's air is made of, from a billion "
  "kilometers away, without ever going."),
 (s_bullets("The trick", "Fingerprints in the rainbow", [
   "Spread light into a spectrum",
   "Gases steal specific colors — dark lines",
   "Each molecule steals its OWN pattern",
   "Match the pattern, name the gas",
   "Titan's methane: read from Earth, 1944"]),
  "Spread a world's light into a spectrum and dark lines appear — colors "
  "stolen by whatever gas the light passed through. Each molecule steals its "
  "own exact pattern, as distinctive as a fingerprint. Match the pattern "
  "against lab measurements and you have named the gas. Astronomers read "
  "methane in Titan's light in nineteen forty-four, from Earth, decades before "
  "any spacecraft. The Webb telescope does the same for planets around other "
  "stars today."),
 (s_bullets("This week", "Your job", [
   "Match three fingerprints in the figure",
   "Build a spectrum in the notebook",
   "Find the deepest bite by code",
   "Build: explain the trick to a younger student"], closing=True),
  "Your job: match three mystery worlds to their gases in the figure, build a "
  "spectrum in code and find its deepest bite, and for the build, explain the "
  "whole trick in your own words to a younger student. If you can teach it, "
  "you own it."),
]

SP["alnow-space-2"] = [
 (s_title("Week 2 · Planetary Exploration", "Getting there",
          "Flyby. Orbit. Land. Return. And the senses aboard."),
  "Week two: once telescopes say a world is interesting, there is a ladder of "
  "ways to visit — each rung harder and more revealing than the last."),
 (s_bullets("The ladder and the senses", "Missions and instruments", [
   "Flyby — race past once, no second chance",
   "Orbiter — stay for years, watch seasons",
   "Lander — touch the ground",
   "Camera = eyes · spectrometer = nose",
   "Radar = touch, straight through haze"]),
  "Flyby: race past once, cameras blazing — still our only close look at "
  "Neptune. Orbiter: stay for years — Cassini circled Saturn for thirteen. "
  "Lander: touch down — Huygens on Titan, the most distant landing ever. And "
  "the instruments are the senses: a camera is eyes, a spectrometer is last "
  "week's nose, and radar is touch at a distance — it found Titan's lakes "
  "through haze no camera could pierce."),
 (s_bullets("The catch", "Nobody has a joystick", [
   "Radio moves at light speed — and Saturn",
   "is over a light-HOUR away",
   "The event is over before Earth sees it",
   "Distant spacecraft are trusted, not steered",
   "Build: design your own mission card"], closing=True),
  "And the catch: radio commands move at light speed, and Saturn is over a "
  "light-hour away. By the time you see the problem, it happened an hour ago — "
  "so distant spacecraft are trusted with a plan, not steered with a joystick. "
  "This week you design a mission in the figure, compute the delays yourself "
  "in the notebook, and build your own mission card. Question first, rocket "
  "second."),
]

SP["alnow-space-3"] = [
 (s_title("Week 3 · Planetary Exploration", "Titan",
          "Thick air. Orange haze. Methane rain. Real seas."),
  "Week three is one world: Titan, Saturn's largest moon, and Doctor Nixon's "
  "specialty. The only moon in the solar system with real air — and weather."),
 (s_bullets("The world", "Weather, with the water swapped", [
   "Nitrogen air, 1.5x Earth's pressure",
   "Minus 179 Celsius — water is ROCK there",
   "Methane plays water: clouds, rain, rivers",
   "Kraken Mare — a sea bigger than the Caspian",
   "Orange haze = planet-wide carbon chemistry"]),
  "Titan's air is mostly nitrogen, like ours, and half again as thick. But at "
  "minus one hundred seventy-nine Celsius, water is rock — the mountains are "
  "ice frozen harder than granite. Methane takes water's job: methane clouds, "
  "methane rain, rivers, and seas — Kraken Mare outsizes the Caspian. The "
  "orange haze is sunlight breaking methane into fragments that reassemble "
  "into heavier carbon molecules: organic chemistry running planet-wide, four "
  "billion years and counting. Chemists see the early Earth, kept in a "
  "freezer."),
 (s_bullets("This week", "Your job", [
   "Compare Earth and Titan in the figure",
   "Notebook: your weight, the cold, the delay",
   "Build: a postcard from Titan",
   "Every claim traces to a number"], closing=True),
  "Your job: hold the two worlds side by side in the figure, do Titan's "
  "arithmetic in the notebook — your weight there, how cold the cold is, how "
  "long Titan's news takes to reach Earth — and build a postcard from Titan "
  "where every claim traces to a real number. Voice yours, facts Titan's."),
]

SP["alnow-space-4"] = [
 (s_title("Week 4 · Planetary Exploration", "Find a planet in the data",
          "A 1% flicker, on schedule, is a world."),
  "Capstone week — and the two sprints meet. Thousands of planets around other "
  "stars were found without a single photograph. They were found in tables."),
 (s_bullets("The transit trick", "Dips, depth, and schedule", [
   "Record a star's brightness for weeks",
   "A crossing planet blocks a sliver — a dip",
   "The dip repeats: that schedule is its YEAR",
   "Depth = fraction of the star covered",
   "Radius = the square root of the depth"]),
  "Record a star's brightness, hour after hour. If a planet's orbit crosses "
  "the star's face, it blocks a sliver of light — a small, clean dip that "
  "returns on a perfect schedule. The schedule is the planet's year. The depth "
  "is its size: a one percent dip means the planet covers one percent of the "
  "star's disk, and the radius is the square root of that — one tenth the "
  "star. Roughly Jupiter. Tables, dips, and square roots — that is how Kepler "
  "found thousands."),
 (s_bullets("This week", "Finish the sprint", [
   "Catch three dips with the threshold figure",
   "Measure period, depth, size in the notebook",
   "Write the finding — candidate, not confirmed",
   "All four builds in = Dr. Nixon's lecture"], closing=True),
  "Your job: catch the dips with the threshold in the figure — without "
  "catching noise — then measure the period, the depth, and the size in the "
  "notebook, and write the three-sentence finding. Say candidate, not "
  "confirmed; that discipline is the data sprint talking. Turn it in, and the "
  "sprint is complete: Doctor Nixon's lecture is waiting. Bring your strangest "
  "question."),
]


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(DS, "Data Science", only=only)
    build_all(SP, "Planetary Exploration", only=only)
