#!/usr/bin/env python3
"""Albania Now — listen briefs, sprints 6 & 7 (~400+ words each, the
corrected rate: ~200 wpm spoken → ~2 min).
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_sprints3.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/alnow-audio"
os.makedirs(WORK, exist_ok=True)

T = {}

T["read-1"] = ("Before you read, a professional secret: programmers spend most "
 "of their working life reading code, not writing it — their own from last "
 "month, their teammates', and, more every year, code an AI wrote in seconds. "
 "The AI did not shrink that job. It multiplied it, because somebody has to "
 "judge those thirty confident lines, and that somebody is you. Reading code "
 "is not like reading prose. Prose you skim. Code you trace — you become the "
 "machine and act the story out, line by line, keeping a little whiteboard of "
 "variables in your head, or better, on paper. The technique looks childish: "
 "put a finger on line one, say what it does, move down. It is not childish. "
 "It is what every professional debugging session actually is, done fast. "
 "Three rules carry the week. One line at a time — your eye wants to jump to "
 "the interesting line, and the bug is usually in a boring one. Track every "
 "store — when a variable is reassigned, the old value is gone, and your "
 "paper should show the crossing-out. And commit your prediction before the "
 "last line runs. A prediction you did not commit to teaches you nothing, "
 "because after the fact it quietly becomes what you meant all along. The "
 "notebook this week takes that seriously: you will store each prediction in "
 "a variable before the program runs, and a check cell will compare your "
 "committed answer against the machine's. No grading on vibes — the trace "
 "either matched or it didn't, and both outcomes teach. Paper and pen ready. "
 "Finger on the line.")

T["read-2"] = ("Before you read: show twenty lines to an experienced "
 "programmer and within seconds they will say something like, a loop that "
 "builds a total, with a guard for the empty case. They did not read every "
 "word. They read the shape. Python draws its shapes with indentation — "
 "everything indented under a for happens once per item; everything under an "
 "if happens only when the test is true. The indentation is not decoration. "
 "It is the structure itself, which is why a wrongly indented line is not "
 "ugly — it is a different program. Two shapes cover most beginner code. The "
 "accumulator: a variable starts at zero or empty before a loop, grows inside "
 "it, and gets used after. Spot that pattern and you know the loop's purpose "
 "before tracing a single pass. And the fork: an if and its else split the "
 "road — and the professional move is to read the test first, because the "
 "test is what decides everything. The reading order for the week: shape, "
 "then purpose, then trace. Name the shape. Say the purpose out loud, as a "
 "guess. Then trace exactly two passes of the loop — the first pass and one "
 "more catches most misreadings, and tracing all of them is usually wasted "
 "motion. Only go deeper when the first two passes disagree with your guess. "
 "The figure unrolls a loop pass by pass so you can watch an accumulator "
 "actually accumulate. Then eight drills, predictions committed first, "
 "machine as referee. Shapes first, words second.")

T["read-3"] = ("Before you read: code you didn't write is a foreign city, and "
 "the beginner's mistake is walking every street in order. The skill is "
 "reading the map first. Skim top-down: read the names before any logic — "
 "total lek, clean name, count words. Good names are the author telling you "
 "the plot. Then find the load-bearing line. In most short programs, one "
 "line does the real work and everything else is setup and delivery. Find "
 "it, and you know where to trace carefully — and where to trace lightly, "
 "which matters just as much. Then come the smells: patterns that don't "
 "prove a bug but earn a second read. The magic number — a bare zero point "
 "one eight sitting in a formula, explaining nothing. The lying name — a "
 "variable called average that actually holds a sum, a lie every future "
 "reader inherits. The unused value — computed, then never touched again; "
 "sometimes a leftover, sometimes the author meant to use it and forgot, "
 "which is a bug wearing camouflage. All of this applies double to code an "
 "AI hands you. It arrives fluent, confident, and completely unread — you "
 "are its first reader ever. The verification habit from your other sprints "
 "has a street address now: names first, then the weight, then the smells. "
 "This week's notebook hands you three programs by another author, one "
 "hiding a real bug, and asks you to read before you run. The build is a "
 "proper bug report. Welcome to the foreign city.")

T["read-4"] = ("Capstone week. So far your errors have been one report deep. "
 "Real programs fail in chains: a line calls a helper, the helper fails, and "
 "Python prints the whole chain — a traceback. It looks like a wall of text, "
 "and it reads like a hallway once you know the direction: bottom-up. The "
 "last line names the kind of problem and the message. The lines above walk "
 "the chain of calls — and your move is to climb until you reach a line you "
 "wrote or can change, because that is where the fixing starts, even when "
 "the failure happened deeper. Then the second half of the capstone: the "
 "written code review, the professional artifact of reading. It has a fixed "
 "shape, four parts. What the program does — two sentences, from your "
 "top-down skim. What's solid — name something genuinely good, because "
 "reviews that only attack teach nothing and get ignored. What's wrong or "
 "smelly — each finding with the line it lives on and why it matters. And "
 "what you would change first — one concrete edit, not a rewrite. That "
 "shape works on a classmate's build, an AI's thirty lines, and someday a "
 "colleague's pull request. This week you write one for real: a twenty-line "
 "program with at least three findings hiding in it — a lying name, an "
 "unused value, a magic number. Find them, write them up, make one change, "
 "show it running. Finish, and the sprint is complete — the lecture list "
 "has your name.")

T["sources-1"] = ("Before you read: school hands you one source at a time — "
 "the textbook, the teacher. The real world is the opposite: a thousand "
 "sources and no syllabus, which is why just search it is useless advice "
 "until you know what kind of answer you need. Everything you will ever "
 "teach yourself lives in the same five kinds of source. Official "
 "documentation is the reference — complete, correct, dry, built for looking "
 "things up, not for learning from zero; reading docs cover to cover is "
 "reading a dictionary to learn a language. Tutorials and courses are the "
 "guided path — someone ordered the ideas for you, unbeatable at the start, "
 "too slow once you're moving. Videos show hands doing the thing — perfect "
 "for anything physical or visual, painful for anything you need to search "
 "or copy. Q and A sites hold answers to exact narrow questions — someone "
 "already hit your exact wall, almost always. And communities — forums, "
 "Discords, clubs — are where the unanswerable questions go, and where "
 "taste lives: which tools people actually use, what is current, what is "
 "hype. The week's tool is the first-fifteen-minutes protocol for any new "
 "topic. Five minutes: find the official source, skim its front page, learn "
 "the vocabulary the field uses for itself. Five more: find one respected "
 "tutorial and read just its table of contents — now you know the shape of "
 "the path. Last five: find where the community lives. You won't know the "
 "topic yet. You'll know where the topic keeps its answers — and that is "
 "the meta-skill this whole month is about.")

T["sources-2"] = ("Before you read: bad learning material does not announce "
 "itself. It is fluently written, beautifully formatted, and quietly wrong — "
 "stale, copied, or confident beyond its knowledge. And since you cannot "
 "judge the content of a field you're new to, you judge the signals around "
 "it. Five checks, under a minute. The date — fields move, and a programming "
 "tutorial from twenty-twelve teaches a version that will fight you line by "
 "line; the faster the field, the harder the date matters, and an undated "
 "tutorial in a fast field is a red flag all by itself. The author — not "
 "fame, accountability: a named person with a history in the topic beats an "
 "anonymous content farm rewriting other people's posts for clicks. The why "
 "— great material explains why each step exists; bad material lists steps, "
 "and steps without reasons cannot survive contact with your situation, "
 "which is always slightly different. The working example — in anything "
 "technical, run the tutorial's own first example before investing your "
 "afternoon; a broken first example predicts everything after it. And the "
 "cross-check — any claim you are about to build on gets confirmed by a "
 "second, independent source. Independent is the hard part: much of the "
 "internet is one origin, paraphrased twenty ways. This week you run the "
 "autopsy on real material: two tutorials, one topic, five checks each, one "
 "winner. One minute of checking saves one weekend of wrong.")

T["sources-3"] = ("Before you read: at some point every learner hits a wall "
 "no source answers, and what happens next separates people who learn fast "
 "from people who stay stuck. First, the move that solves most walls "
 "without bothering anyone: search the exact error text, in quotes — the "
 "machine's own words, not your description of them. Error messages are "
 "identical across the whole world, which makes them the best search terms "
 "ever written. Strip out your personal file names, quote the rest. When "
 "search fails, you ask — and a good question has an anatomy of exactly "
 "three parts. The goal: what you are actually trying to achieve, one "
 "sentence, because half of all stuck people are stuck on the wrong "
 "approach, and only the destination reveals that. What you tried: the "
 "smallest complete version of your attempt — not the whole project, the "
 "smallest piece that still shows the problem. Cutting it down is "
 "respectful work, ten of your minutes for ten of ten readers' — and half "
 "the time the cutting reveals the answer by itself; the effect is so "
 "reliable it has a name, rubber-duck debugging. And what happened: the "
 "exact error or the exact wrong output, pasted, never paraphrased — "
 "described errors are invisible, pasted errors are searchable and "
 "diagnosable. Where to ask, in order: the sprint's Discord, the topic's "
 "own community, then the public Q and A sites, where your well-shaped "
 "question becomes the next stuck person's answer. Asked well, a question "
 "is a gift. This week you write and post a real one.")

T["sources-4"] = ("Capstone week. You can find sources, judge them, and ask "
 "when they fail you. Now the system that turns all of it into actual "
 "learning. Start with notes, and one rule: your own words. Copying a "
 "source's sentence feels efficient and stores nothing — the words pass "
 "through your hands without visiting your head. Rewriting the idea as if "
 "explaining it to a classmate forces the visit. The test for every note: "
 "could you have written this sentence before you read the source? If yes, "
 "skip it. If no — that is the note. Then returns. You met this as "
 "retrieval practice in other sprints, and it governs self-study too: a "
 "note you come back to after two days, then a week, then a month, becomes "
 "yours; a notebook filled once and never reopened is a diary of things you "
 "almost learned. Put the return dates in the plan — they are study "
 "sessions, not admin. And then the plan itself, the honest kind: built "
 "against your real week, school and family and the days you're wrecked — "
 "not the imaginary week where you study every evening. Each session gets "
 "one sitting-sized goal with a visible finish, one source, and a two-line "
 "note slot. One catch-up day per week, because life. A plan that survives "
 "two real weeks beats a beautiful plan that dies on day three — and "
 "knowing that difference is the sprint. Write the plan, run day one before "
 "the week ends, and bring the log. The lecture list has your name.")


def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for key, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/{key}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/alnow-{key}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO3 DONE", flush=True)


if __name__ == "__main__":
    main()
