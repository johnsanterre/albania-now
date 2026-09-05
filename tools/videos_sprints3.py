#!/usr/bin/env python3
"""Albania Now — main videos, sprints 6 & 7, at the 5-minute standard
(6 scenes × ~135 words at the measured Kokoro rate).
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_sprints3.py [slug]"""
import sys
from vidlib import s_title, s_bullets, s_code, s_notebook, build_all, GREEN

RD = {}
SRC = {}

RD["alnow-read-1"] = [
 (s_title("Week 1 · Reading Python", "Trace like the machine",
          "Reading code means running it in your head."),
  "Welcome to the reading sprint — built on a professional secret. "
  "Programmers spend most of their time reading code, not writing it. Their "
  "own from last month. Their teammates'. And, more every year, code an AI "
  "wrote in seconds — fluent, confident, and completely unread by any human. "
  "Somebody has to judge those lines before trusting them, and that somebody "
  "is you. This month you learn to read code the way professionals do, "
  "starting with the foundation of all of it: the trace."),
 (s_bullets("The technique", "The finger on the line", [
   "Become the machine — act the story out",
   "One line at a time, no jumping",
   "Keep the whiteboard on paper",
   "Cross out the old value at every store",
   "Commit the prediction BEFORE the end"]),
  "Reading code is not like reading prose. Prose you skim; code you trace — "
  "you become the machine and act the story out, one line at a time, keeping "
  "the whiteboard of variables on paper. Put a finger on line one. Say what "
  "it does to the whiteboard. Move down. It looks childish and it is the "
  "advanced technique — every professional debugging session is this exact "
  "motion done fast. When a variable is reassigned, cross out the old value; "
  "the crossing-out is where most misreadings hide. And before the final "
  "line runs, commit to what it will print. Out loud, or on paper."),
 (s_code("Why commit", "The snapshot trap",
   ['a = 3', 'b = a + 2', 'a = 10', 'print(a + b)'],
   console=[("15", GREEN)],
   note="b took a snapshot at line 2. Reassigning a later never touches b."),
  "Here is why committing matters. Line one stores three under a. Line two "
  "computes a plus two — five — and stores it under b. Line three stores ten "
  "under a. Now the question: does b feel that change? If you trace casually, "
  "you'll say twenty. But b took a snapshot of the value five at the moment "
  "of its store — variables hold values, not connections to other variables. "
  "Ten plus five: fifteen. If you committed to twenty first, this surprise "
  "just taught you the snapshot rule permanently. If you didn't commit, your "
  "brain quietly rewrites history and learns nothing. That is the entire "
  "logic of this week's notebook."),
 (s_notebook("The drill format", "Predict, run, check", [
   (['# PREDICT 1 — replace None', 'pred_1 = 15'], [("", "ok")]),
   (['a = 3', 'b = a + 2', 'a = 10', 'print(a + b)'], [("15", "ok")]),
   (['# CHECK 1', 'assert pred_1 == 15'], [("PASSED — your trace matched the machine", "ok")]),
  ], note="The machine referees your trace. No grading on vibes."),
  "The notebook makes commitment mechanical. For every drill, you store your "
  "prediction in a variable first — pred one equals whatever your paper trace "
  "says. Then the program runs. Then a check cell compares your committed "
  "answer to what actually happened. Passed means your trace matched the "
  "machine. A red assertion means your model of the machine diverged "
  "somewhere — and the divergence is the most valuable thing you'll find all "
  "week, because it is small, specific, and fixable in a minute. Ten drills, "
  "ten committed predictions, one honest score."),
 (s_bullets("Why now", "Reading in the AI era", [
   "AI writes in seconds; you judge in minutes",
   "You are the FIRST reader of that code",
   "Trust follows tracing, not fluency",
   "Fluent and wrong look identical — until traced"]),
  "One more reason this sprint exists now. When an AI assistant hands you "
  "code, you are its first reader — nobody else has ever looked at it. It "
  "arrives fluent, well-formatted, and confident, and fluent-and-wrong looks "
  "exactly like fluent-and-right until somebody traces it. The programmers "
  "who thrive in the next decade are not the fastest typists; they are the "
  "readers who can put a finger on line one of anything and know, three "
  "minutes later, whether to trust it. That skill starts with three-line "
  "programs this week and scales for the rest of your life."),
 (s_bullets("This week", "Your job", [
   "Three programs in the figure — trace first",
   "Ten notebook drills, predictions committed",
   "Build: one full paper trace, photographed",
   "Paper and pen are required equipment"], closing=True),
  "Your job this week. Trace the three programs in the figure with your "
  "finger before touching any answer. Then the notebook: ten drills, every "
  "prediction committed before the program runs, every check honest. The "
  "build is one full paper trace of the week's longest program — every line, "
  "the whiteboard after every store, photographed next to the real output, "
  "with one sentence on where your trace diverged, if it did. Paper and pen "
  "are not optional this month. They are the debugger you always carry. "
  "Finger on the line."),
]

RD["alnow-read-2"] = [
 (s_title("Week 2 · Reading Python", "Read the shapes",
          "See WHAT code is before reading a word of it."),
  "Week two. Show twenty lines to an experienced programmer and within "
  "seconds they'll say: a loop that builds a total, with a guard for the "
  "empty case. They did not read every word — they read the shape. This week "
  "you get that superpower at beginner scale: the two shapes that cover most "
  "code you'll meet, and the reading order that uses them."),
 (s_code("Structure", "Indentation IS the program",
   ['total = 0', 'for cmim in [120, 150, 180]:', '    total = total + cmim', 'print(total)'],
   console=[("450", GREEN)],
   note="Everything indented under the for happens once per item."),
  "Python draws its structure with indentation. Everything indented under a "
  "for happens once per item in the list. Everything under an if happens "
  "only when the test is true. That means indentation is not style — it is "
  "the program. Move that print one level right, and it runs three times "
  "instead of once: a different program, same words. When you read Python, "
  "your eye should track the left margin the way your finger tracks the "
  "lines: every step in is a door into a block, every step out is the door "
  "closing."),
 (s_bullets("Shape one", "The accumulator", [
   "Starts at zero or empty, before the loop",
   "Grows inside the loop, once per item",
   "Gets used after the loop",
   "Can sum, count, or build text",
   "Spot it = know the purpose instantly"]),
  "Shape one: the accumulator. A variable starts at zero or empty before a "
  "loop, grows inside it, and is used after. Once you can spot that "
  "pattern, you know the loop's purpose before tracing a single pass — it "
  "is building one thing out of many. And it wears costumes: total plus "
  "cmim sums prices; numri plus one counts items; fjalia plus fjale glues "
  "text into a sentence. Same skeleton, three jobs. Most loops you will "
  "read this year are accumulators in one costume or another, and naming "
  "the costume is half the reading."),
 (s_bullets("Shape two", "The fork — read the test first", [
   "if / else splits the road",
   "The TEST decides everything — read it first",
   "Then each branch, knowing what chose it",
   "No else? The false case walks through",
   "Fork inside a loop = filtering"]),
  "Shape two: the fork. An if and its else split the road, and the "
  "professional move is to read the test first — not the branches — because "
  "the test is what decides everything. Then read each branch knowing what "
  "sent you there. Watch for the fork with no else: when the test is false, "
  "the program just walks through, unchanged, and that silence trips "
  "readers constantly. And when a fork lives inside a loop, the two shapes "
  "combine into filtering: only some items feed the accumulator. That "
  "combination — loop, test, grow — is most of real-world data code."),
 (s_bullets("The method", "Shape, purpose, trace", [
   "Name the shape first",
   "Guess the purpose out loud",
   "Trace exactly TWO passes",
   "All passes only if the two disagree"]),
  "The reading order that follows: shape, purpose, trace. Name the shape — "
  "accumulator, fork, or both. Guess the purpose out loud, as a real "
  "commitment. Then trace exactly two passes of the loop — the first pass "
  "and one more catches most misreadings, and tracing every pass of every "
  "loop is how beginners exhaust themselves. Only trace deeper when the "
  "first two passes disagree with your guess. This is how experienced "
  "readers move fast without being careless: careful where the shape says "
  "to be careful, quick everywhere else."),
 (s_bullets("This week", "Your job", [
   "Unroll the loop in the figure, pass by pass",
   "Eight drills — name the shape, THEN predict",
   "Build: your shape catalog + one combined program",
   "Two passes, committed predictions, honest checks"], closing=True),
  "Your job this week. Unroll the figure's loop one pass at a time, "
  "predicting each total before you press. Then eight notebook drills — and "
  "the new move: name the shape out loud before committing each prediction. "
  "The build is your personal shape catalog — one accumulator, one fork, "
  "each with its one-line purpose and its load-bearing line marked — plus "
  "one program of your own that uses both shapes at once. Next week the "
  "programs stop being yours: you read code somebody else wrote, and the "
  "shapes are how you'll survive it."),
]

RD["alnow-read-3"] = [
 (s_title("Week 3 · Reading Python", "Read code you didn’t write",
          "Names first. Then the weight. Then the smells."),
  "Week three, and the training wheels come off: code you didn't write, "
  "arriving without your memory of writing it. A foreign city. The "
  "beginner's mistake is walking every street in order. The skill — this "
  "week's skill — is reading the map first."),
 (s_bullets("The skim", "Top-down, names first", [
   "Read the NAMES before any logic",
   "Good names are the author's plot summary",
   "total_lek, clean_name, count_words",
   "Then find the load-bearing line",
   "One line does the work; the rest delivers"]),
  "Open thirty unfamiliar lines and read the names first — the variables, "
  "the functions — before any logic. Total lek. Clean name. Count words. "
  "Good names are the author telling you the plot, and even bad names tell "
  "you where the author stopped caring. Then find the load-bearing line. In "
  "most short programs, one line does the real work and everything else is "
  "setup and delivery. Find the weight, and you know where to trace "
  "carefully — and where a light skim is enough. Careful everywhere is the "
  "same as careful nowhere; budget your attention like a professional."),
 (s_code("Smell one and two", "Magic numbers, lying names",
   ['cmimi = 2500', 'zbritja = cmimi * 0.30', 'average = zbritja + cmimi'],
   console=None, err_line=1,
   note="Why 0.30? And that name — average of WHAT?"),
  "Now the smells — patterns that don't prove a bug but earn a second read. "
  "Smell one: the magic number. A bare zero point three zero in the middle "
  "of a formula. Why thirty percent? Who decided? A number with no name "
  "carries no explanation, and when the discount changes next month, "
  "somebody has to guess what this one meant. Smell two: the lying name. A "
  "variable called average that holds a sum plus a discount — the name "
  "promises one thing, the code does another, and every future reader "
  "inherits the lie. Names are documentation; lying documentation is worse "
  "than none."),
 (s_bullets("Smell three", "The unused value", [
   "Computed, then never touched again",
   "Sometimes a leftover from an old version",
   "Sometimes the author MEANT to use it",
   "That second case is a bug in camouflage"]),
  "Smell three: the unused value. Something computed carefully — then never "
  "touched again. Sometimes it is a harmless leftover from an older version "
  "of the program. But sometimes the author meant to use it and forgot — "
  "they computed the average and then printed the total, and the program "
  "runs perfectly while doing the wrong thing. That is the most dangerous "
  "kind of bug: no red text, no crash, just a quiet wrong answer wearing a "
  "correct-looking outfit. Unused values are where you hunt for it. Your "
  "eye will learn to snag on them within the week."),
 (s_bullets("The AI angle", "You are the first reader", [
   "AI code arrives fluent and unread",
   "Fluent-and-wrong looks like fluent-and-right",
   "Names, weight, smells — same tools",
   "Verify before trust — every time"]),
  "And the reason this week matters double now: AI-written code. It arrives "
  "in seconds, fluent and formatted and confident — and completely unread "
  "by any human being. You are its first reader ever. The tools you just "
  "learned are exactly the tools for the job: skim its names, find its "
  "load-bearing line, hunt its smells — the magic numbers it invented, the "
  "names that drifted from what the code actually does. The verification "
  "habit your other sprints preach has a street address now, and this week "
  "you practice on three programs by another author, one of which hides a "
  "real bug."),
 (s_bullets("This week", "Your job", [
   "Click the load-bearing line, three times",
   "Read three programs COLD in the notebook",
   "Committed answers before running — as always",
   "Build: a professional bug report"], closing=True),
  "Your job this week. In the figure: three programs, click the one line "
  "that does the real work in each. In the notebook: three programs by "
  "another author — a receipt totaler, a temperature converter, a word "
  "counter. Read them cold. Commit your answers to what they print before "
  "running them. One hides a real bug, and the build is a proper bug "
  "report: what the program claims, what it actually does with the input "
  "that proves it, the line where the bug lives, and the one-line fix. "
  "Welcome to the foreign city. Read the map first."),
]

RD["alnow-read-4"] = [
 (s_title("Week 4 · Reading Python", "The traceback, and the review",
          "Read the full report. Write the professional artifact."),
  "Capstone week, two skills. First: the traceback — the multi-line report "
  "real programs produce when they fail in chains. Second: the written code "
  "review, the professional artifact of reading, which you will produce for "
  "real by Friday. Both are the week-one finger-trace, grown up."),
 (s_code("The chain", "Read it bottom-up",
   ['Traceback (most recent call last):',
    '  File "receipt.py", line 12, in <module>',
    '  File "receipt.py", line 7, in total_line',
    'TypeError: can only concatenate str (not "int") to str'],
   console=None, err_line=3,
   note="Bottom: the kind. Climb: to the line you can change."),
  "A real failure prints a chain: line twelve called a helper, the helper "
  "failed on line seven, and Python shows the whole hallway. It reads "
  "bottom-up. The last line names the kind of problem — type error, text "
  "glued to a number — and the message that describes it. Then you climb: "
  "up through the chain until you reach a line you wrote or can change. "
  "That line is where the fixing starts, even though the crash happened "
  "deeper. Beginners read tracebacks top-down and drown; professionals "
  "read the last line, climb two frames, and start fixing. Sixty seconds, "
  "most days."),
 (s_bullets("The review", "Four parts, fixed shape", [
   "What it does — two sentences",
   "What's solid — name something good",
   "Findings — line numbers + WHY",
   "First change — one edit, not a rewrite"]),
  "The written code review has a fixed, four-part shape. What it does: two "
  "sentences from your top-down skim — prove you read the plot. What's "
  "solid: name something genuinely good, because reviews that only attack "
  "teach nothing and get ignored by everyone who receives them. The "
  "findings: what's wrong or smelly, each with the line it lives on and "
  "why it matters — a lying name, an unused value, a magic number. And "
  "what you'd change first: one concrete edit, not a rewrite, because "
  "reviews that demand everything get nothing. That shape works on a "
  "classmate's build, an AI's output, and someday a colleague's pull "
  "request."),
 (s_notebook("The target", "Three findings are hiding", [
   (['total = 0', 'for nota in notat:', '    total = total + nota',
     'average = total'], [("", "ok")]),
   (['shuma_e_katrorit = mesatarja * mesatarja * 0.25'], [("", "ok")]),
  ], note="A lying name. An unused value. A magic number. Find all three."),
  "Your review target is a twenty-line program that mostly works — which is "
  "exactly what makes it realistic. Somewhere in it: a name that promises "
  "an average and stores something else. A value computed at the end and "
  "never used by anything. A bare number in a formula with no explanation "
  "anywhere. At least three findings, none of which crashes the program — "
  "it runs happily, printing correct-looking output, which is why reading "
  "matters at all. Read it cold, names first, weight second, smells third. "
  "Then write the four parts."),
 (s_bullets("The standard", "What complete looks like", [
   "Traceback drills: kind + fixing line, committed",
   "The review: all four parts, three findings",
   "One change made, before and after shown",
   "This is the sprint's whole skill, on paper"]),
  "The standard for the capstone. The traceback drills first: two failing "
  "chains, and for each you commit the kind of error and the line where "
  "fixing starts — checked by the machine, as always. Then the review: all "
  "four parts, at least three findings with line numbers and reasons, and "
  "the one change you'd make first — actually made, with before and after "
  "shown running. When you finish, look back at week one: you started "
  "tracing three-line programs with a finger. You are ending the month "
  "reviewing someone else's program in professional form. That distance is "
  "the sprint."),
 (s_bullets("Finish", "The lecture list awaits", [
   "Climb the figure's traceback",
   "Two drill chains in the notebook",
   "The review target: read, write, fix",
   "All four builds in = the lecture"], closing=True),
  "Your job this week. Climb the traceback in the figure — click where the "
  "fixing starts. Run the two drill chains in the notebook, bottom-up, "
  "predictions committed. Then the main event: read the target cold, write "
  "the four-part review, find the three findings, make your one change, "
  "and show it running. Turn it in, and the sprint is complete — four "
  "weeks, four builds, and a seat at the closing lecture with a working "
  "engineer whose entire day is exactly this skill. Bring the review. It "
  "is worth discussing."),
]

SRC["alnow-sources-1"] = [
 (s_title("Week 1 · Learning to Learn", "The map of where answers live",
          "A thousand sources, no syllabus — until now."),
  "Welcome to the sprint about everything else you will ever learn. School "
  "hands you one source at a time: the textbook, the teacher. The real "
  "world is the opposite — a thousand sources and no syllabus — and 'just "
  "search it' is useless advice until you know what kind of answer you "
  "need. This week: the map."),
 (s_bullets("The kinds", "Five kinds of source", [
   "Docs — the reference; look up, don't learn",
   "Tutorials — the ordered path; best at zero",
   "Videos — hands doing the thing",
   "Q&A — your exact wall, already hit",
   "Communities — taste, currency, the unanswerable"]),
  "Everything you'll ever teach yourself lives in five kinds of source. "
  "Official documentation: complete, correct, dry — built for looking "
  "things up, and reading it cover-to-cover is reading a dictionary to "
  "learn a language. Tutorials: someone ordered the ideas for you — "
  "unbeatable at the start, too slow once you're moving. Videos: hands "
  "doing the thing — perfect for the physical and visual. Q and A sites: "
  "exact answers to exact questions, because someone already hit your "
  "wall. And communities — where taste lives: what people actually use, "
  "what's current, what's hype."),
 (s_bullets("The match", "The need picks the kind", [
   "“What does this argument do?” → docs",
   "“Teach me from zero” → tutorial",
   "“How do I hold it?” → video",
   "“This exact error” → Q&A",
   "“What do people actually use?” → community"]),
  "The skill is matching the need to the kind. A lookup question — what "
  "does the second argument do — goes to the docs and takes ten seconds. "
  "Learning from zero goes to a tutorial, because you need the ordering "
  "more than the facts. Anything physical goes to video — you need to see "
  "hands. An exact error goes to Q and A, quoted. And the questions about "
  "taste — which laptop, which tool, is this still current — go to the "
  "community, because currency and taste live in conversation, not "
  "documents. Wrong kind, wasted hour. Right kind, ten minutes."),
 (s_bullets("The protocol", "The first fifteen minutes", [
   "1–5: official source, skim, learn the vocabulary",
   "5–10: one tutorial, read ONLY its contents page",
   "10–15: find where the community lives",
   "Outcome: not the topic — the topic's MAP"]),
  "The week's tool: the first-fifteen-minutes protocol, for any new topic "
  "in any field. Minutes one to five: find the official source and skim "
  "its front page — you are not learning yet, you are collecting the "
  "vocabulary the field uses for itself, which unlocks every later search. "
  "Minutes five to ten: find one well-regarded tutorial and read only its "
  "table of contents — now you know the shape of the path, what comes "
  "before what. Minutes ten to fifteen: find where the community lives. "
  "Fifteen minutes, and the topic has a map with your three landmarks on "
  "it."),
 (s_bullets("Why it transfers", "Any field, same map", [
   "Guitar, chemistry, cameras, code — same five kinds",
   "The map is the meta-skill",
   "Schools rarely teach it",
   "You'll use it for fifty years"]),
  "Here is why this sprint has no code in it: the map is the same for "
  "every field. Guitar has docs — they're called method books — and "
  "tutorials and videos and forums full of taste. Chemistry has them. "
  "Photography has them. Your future profession, whatever it turns out to "
  "be, has them. Learning to find, judge, and use sources is the "
  "meta-skill above every skill, the one that makes every later learning "
  "faster — and almost no school teaches it on purpose. Four weeks from "
  "now you will have a system. This week you get the map."),
 (s_bullets("This week", "Your job", [
   "Match six needs to kinds in the figure",
   "Run the 15-minute protocol on YOUR topic",
   "Log: source, contents, community, surprise",
   "Build: the log + which kind will carry you"], closing=True),
  "Your job this week. Match the six needs to their kinds in the figure. "
  "Then pick something you genuinely want to learn — an instrument, a "
  "sport, a language, a program — and run the protocol with a real timer: "
  "official source, tutorial contents, community, fifteen minutes. The "
  "build is your five-line log plus one paragraph: which kind of source "
  "will carry most of your learning for this topic, and why — because a "
  "guitar and a Python library have different answers, and seeing that "
  "difference is the lesson. Set the timer."),
]

SRC["alnow-sources-2"] = [
 (s_title("Week 2 · Learning to Learn", "Judge before you trust",
          "The best and worst tutorials look identical — for one minute."),
  "Week two. Bad learning material does not announce itself. It is "
  "fluently written, beautifully formatted, and quietly wrong — stale, "
  "copied, or confident beyond its knowledge. You cannot yet judge the "
  "content of a field you're new to. So you judge the signals around it: "
  "five checks, under a minute."),
 (s_bullets("Checks 1 & 2", "The date, the author", [
   "Fields move — stale material fights you",
   "Fast field + no date = red flag alone",
   "Author: accountability, not fame",
   "A named history beats a content farm",
   "One search on the name settles it"]),
  "Check one: the date. Fields move at different speeds — a programming "
  "tutorial from twenty-twelve teaches a version that will fight you line "
  "by line, while a camera guide from five years back is mostly fine. The "
  "faster the field, the harder the date matters, and an undated tutorial "
  "in a fast field is a red flag all by itself: dates get omitted on "
  "purpose. Check two: the author — not fame, accountability. A named "
  "person with a visible history in the topic beats an anonymous content "
  "farm rewriting other people's work for ad clicks. One search on the "
  "author's name settles it."),
 (s_bullets("Checks 3 & 4", "The why, the working example", [
   "Great material explains WHY each step exists",
   "Steps without reasons can't adapt",
   "Your situation is ALWAYS slightly different",
   "Technical? Run the FIRST example early",
   "A broken example predicts everything after"]),
  "Check three: the why. Great material explains why each step exists; bad "
  "material lists steps. The difference matters because steps without "
  "reasons cannot survive contact with your situation — and your situation "
  "is always slightly different from the author's. Reasons are what let "
  "you adapt; recipes without reasons break the moment your kitchen "
  "differs. Check four, for anything technical: the working example. "
  "Before investing an afternoon, run the tutorial's own first example. If "
  "it doesn't work as written, stop — a broken first example predicts "
  "everything that follows it."),
 (s_bullets("Check 5", "The cross-check", [
   "Load-bearing claims get a second source",
   "INDEPENDENT is the hard part",
   "Much of the internet is one origin, paraphrased",
   "Different kind of source = more independent",
   "The research habit, made daily"]),
  "Check five, the professional one: the cross-check. Any claim you are "
  "about to build on — an installation step, a safety instruction, a "
  "grammar rule — gets confirmed by a second, independent source. "
  "Independent is the hard part. Much of the internet is a single origin "
  "paraphrased twenty ways, so twenty agreeing pages can be one wrong "
  "page, twenty times. The strongest cross-check crosses kinds: a "
  "tutorial's claim confirmed by the official docs, or by the community. "
  "This is the research world's habit, shrunk to daily size, and it "
  "compounds for life."),
 (s_bullets("The economics", "One minute versus one weekend", [
   "The checks cost under a minute",
   "A stale tutorial costs a weekend",
   "A confident wrong one costs more: trust",
   "Judging is not cynicism — it's speed"]),
  "The arithmetic that makes this week matter: the five checks cost under "
  "a minute. A stale tutorial costs a weekend of fighting version errors. "
  "A confidently wrong one costs more — it installs a wrong idea early, "
  "and wrong ideas learned first are the hardest to evict. Judging your "
  "sources is not cynicism; it is speed. The learners who move fastest "
  "are not the ones who trust everything or the ones who trust nothing — "
  "they are the ones who can tell, in a minute, which is which. That "
  "minute is this week."),
 (s_bullets("This week", "Your job", [
   "Autopsy four tutorials in the figure",
   "Find two real ones on YOUR topic",
   "Five checks each, side by side",
   "Build: the scorecard + the verdict"], closing=True),
  "Your job this week. Run the figure's autopsies — four tutorial "
  "descriptions, trust or run, and name the check that decided. Then the "
  "real thing: two tutorials on the topic you mapped last week, all five "
  "checks on each, scored side by side. The build is the scorecard plus a "
  "three-sentence verdict: which you'd follow, which check decided it, "
  "and what the loser would have cost you. Next week: what to do when "
  "even good sources fail you — asking strangers, well. One minute of "
  "checks. One weekend saved."),
]

SRC["alnow-sources-3"] = [
 (s_title("Week 3 · Learning to Learn", "Ask well",
          "The most underrated skill on the internet."),
  "Week three. At some point every learner hits a wall no source answers. "
  "What happens next separates people who learn fast from people who stay "
  "stuck — and it is a craft, not a personality trait. This week: how to "
  "ask strangers for help so well that they enjoy answering."),
 (s_bullets("Search first", "The exact-error trick", [
   "Search the machine's OWN words, in quotes",
   "Strip your personal file and variable names",
   "Error text is identical worldwide",
   "The best search terms ever written",
   "Solves most walls in five minutes"]),
  "First, the move that answers most questions without bothering anyone: "
  "search the exact error text, in quotes. Not your description of the "
  "problem — the machine's own words. Error messages are identical across "
  "the entire world, which makes them the best search terms ever written: "
  "millions of people have hit your exact wall, and the ones who asked "
  "well left the answer where the search can find it. Strip out the parts "
  "unique to you — your file names, your variable names — and quote the "
  "rest. This one habit resolves most walls in five minutes, and it works "
  "far beyond code."),
 (s_bullets("The anatomy", "Three parts, always", [
   "1. The GOAL — one sentence, the destination",
   "2. What you TRIED — the smallest failing piece",
   "3. What HAPPENED — pasted exactly, never described",
   "Half of stuck people are on the wrong road",
   "Only the goal reveals it"]),
  "When search fails, you ask — and a good question has an anatomy of "
  "exactly three parts. Part one, the goal: what you're actually trying to "
  "achieve, in one sentence. Half of all stuck people are stuck on the "
  "wrong approach entirely, and the answerer can only see that if they "
  "know the destination. Part two, what you tried: the smallest complete "
  "piece that still shows the problem — never the whole project. Part "
  "three, what happened: the exact error or the exact wrong output, "
  "pasted, never paraphrased. 'It gives an error' is invisible. The error "
  "itself is searchable, diagnosable, answerable."),
 (s_bullets("The magic", "Rubber-duck debugging", [
   "Cutting it down is respectful work",
   "Ten of your minutes for ten readers' ten",
   "Half the time, the cutting SOLVES it",
   "So reliable, it has a name",
   "The question improves you before it's asked"]),
  "About that smallest-piece rule: cutting your problem down is work, and "
  "it is respectful work — you spend ten minutes so ten readers don't "
  "each spend ten. But something better happens along the way. Half the "
  "time, the act of cutting the problem down to its smallest failing "
  "piece reveals the answer by itself — the bug has nowhere left to hide. "
  "The effect is so reliable it has a name, rubber-duck debugging: "
  "explaining your problem carefully, even to a rubber duck, solves it. "
  "A well-prepared question improves the asker before anyone answers it. "
  "That is not a trick. That is how understanding works."),
 (s_bullets("Where and why", "The gift economy", [
   "First: the sprint's Discord — fast, friendly",
   "Then: the topic's own community",
   "Then: public Q&A — your question becomes",
   "  the next searcher's answer",
   "A good question, asked publicly, is a gift"]),
  "Where to ask, in order. First, the sprint's Discord — fastest and "
  "friendliest, and the mentors are there for exactly this. Then the "
  "topic's own community, the one you mapped in week one. Then the big "
  "public Q and A sites — where something bigger happens: your well-shaped "
  "question, answered, becomes the next stuck person's search result. The "
  "answer you needed today was left by someone who asked well two years "
  "ago. Asking publicly and well is how the internet's knowledge actually "
  "gets built — a gift economy, and this week you learn to give properly."),
 (s_bullets("This week", "Your job", [
   "Rebuild the broken plea in the figure",
   "Take a REAL wall you've hit",
   "Write the three parts, run the checklist",
   "Build: post it, then reflect on the answer"], closing=True),
  "Your job this week. Fix the figure's broken plea — my code doesn't "
  "work, please help — one choice at a time, into a question that gets "
  "answered. Then the real thing: take a wall you have actually hit, in "
  "any sprint or any subject, and write the three-part question — goal, "
  "smallest attempt, exact result. Run the checklist: searched first? "
  "goal in one sentence? smallest piece? pasted, not paraphrased? Then "
  "post it — Discord, class board, or a Q and A site. The build is the "
  "post plus your reflection on what the answer taught you about the "
  "question. Ask like it's a craft. It is."),
]

SRC["alnow-sources-4"] = [
 (s_title("Week 4 · Learning to Learn", "Build your learning system",
          "Sources + judgment + questions → a system that runs."),
  "Capstone week. You can find sources, judge them in a minute, and ask "
  "well when they fail you. Now the system that turns those parts into "
  "actual learning — notes that survive, returns that stick, and a "
  "two-week plan honest enough to run. Then you run day one, for real."),
 (s_bullets("Notes", "Your own words, or nothing", [
   "Copying stores nothing — words pass through",
   "Rewrite AS IF explaining to a classmate",
   "The test: could I have written this before?",
   "Yes → skip it. No → THAT's the note",
   "Fewer, truer notes beat full notebooks"]),
  "Notes first, one rule: your own words. Copying a source's sentence "
  "feels efficient and stores nothing — the words pass through your hands "
  "without visiting your head. Rewriting the idea as if explaining it to a "
  "classmate forces the visit; that effort you feel is the storing "
  "happening. The test for every note you consider taking: could you have "
  "written this sentence before you read the source? If yes, skip it — "
  "you're transcribing, not learning. If no, that is the note. A page of "
  "hard-won sentences beats a notebook of beautiful transcription every "
  "single time."),
 (s_bullets("Returns", "Coming back is the study", [
   "Two days → a week → a month",
   "Returned-to notes become yours",
   "Filled-once notebooks are diaries of",
   "  things you almost learned",
   "Return dates go IN the plan"]),
  "Second: returns beat volume. You met this in other sprints as retrieval "
  "practice, and it governs self-study just the same. A note you return "
  "to after two days, then a week, then a month — closing the notebook and "
  "re-answering from memory — becomes yours permanently. A notebook filled "
  "once and never reopened is a diary of things you almost learned. So the "
  "return dates go in the plan itself, as real sessions with real dates. "
  "They are not admin. They are the study — the part most self-taught "
  "learners skip, and the reason most self-study evaporates by spring."),
 (s_bullets("The plan", "Honest beats beautiful", [
   "Against your REAL week — school, family, tired days",
   "Each session: one sitting-sized goal",
   "…with a VISIBLE finish",
   "One source per session, one note slot",
   "One catch-up day per week — because life"]),
  "Third: the plan, the honest kind. Built against your real week — "
  "school, family, training, the days you're wrecked — not the imaginary "
  "week where you study every evening. Each session gets one sitting-sized "
  "goal with a visible finish: play the chorus at half speed; chapter "
  "three's exercises run clean. Not 'study chapter three' — you can't see "
  "the end of that from the start, and goals without visible finishes "
  "don't finish. One vetted source per session, a two-line note slot, and "
  "one catch-up day per week, because life happens and a plan that "
  "pretends otherwise dies on day three. The data sprint taught you not "
  "to overclaim from data. Don't overclaim from your calendar either."),
 (s_bullets("Day one", "Plans meet reality", [
   "Run the FIRST session before the week ends",
   "Log: goal, hit or missed, the note, one fix",
   "The fix is the point — plans are drafts",
   "A run plan beats a perfect plan"]),
  "And then the step that separates this capstone from a homework "
  "exercise: you run day one, this week, before the sprint ends. One real "
  "session from your plan, logged honestly: what the goal was, whether "
  "you hit the visible finish, the two-line note in your own words — and "
  "one adjustment the real session taught you to make to the plan. That "
  "adjustment is the point. Plans are drafts until reality edits them, "
  "and a plan you have actually run, even once, is worth ten beautiful "
  "documents. You will know within one session whether your sessions are "
  "really sitting-sized. Most people find out they aren't — and fix it."),
 (s_bullets("Finish", "The system is yours now", [
   "Fix the planted flaws in the figure",
   "Write the real two-week plan",
   "Run day one, log it honestly",
   "All four builds in = the lecture",
   "This system outlives the sprint"], closing=True),
  "Your job this week. Find the four planted flaws in the figure's plan — "
  "you have the eyes for them now. Write your real two-week plan: skill, "
  "vetted sources from week two, sitting-sized sessions with visible "
  "finishes, return dates, catch-up days. Run day one and log it. Turn in "
  "the plan and the log, and the sprint is complete — four builds, and "
  "the closing lecture with a researcher whose whole career is learning "
  "things nobody taught them. The map, the judgment, the questions, the "
  "system: they're yours now, for every topic, for the next fifty years. "
  "Go learn something."),
]


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(RD, "Reading Python", only=only)
    build_all(SRC, "Learning to Learn", only=only)
