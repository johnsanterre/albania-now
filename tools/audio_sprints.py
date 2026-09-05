#!/usr/bin/env python3
"""Albania Now — listen-segment narrations for both sprints.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_sprints.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/alnow-audio"
os.makedirs(WORK, exist_ok=True)
os.makedirs(f"{SITE}/audio", exist_ok=True)

T = {}

T["ds-1"] = ("Before you read, the shape of the week. When you press play in "
 "Colab, your code does not run on your laptop. It travels to a computer in a "
 "Google data center, runs there, and only the result comes back. That is why "
 "nothing you do this month can break anything — the worst case is red text, "
 "and red text is not a punishment. It is a report: what stopped the code, on "
 "which line, often with a guess at the fix. People who read the report go "
 "fast; people who fear it go slow. That is the single biggest difference "
 "between beginners who thrive and beginners who quit, and it is a habit, not "
 "a talent. "
 "Here is the working method, and it costs nothing: predict, run, compare. "
 "Before you press play on any cell, say out loud what you expect. Then run "
 "it. Then compare. When the output matches, you have confirmed a piece of "
 "your mental model. When it surprises you, you have found something better — "
 "a place where your model is wrong, small enough to fix in one minute. "
 "Students who skip the prediction run twice as many cells and learn half as "
 "much. "
 "Three ideas carry the whole lesson. First, variables: the equals sign means "
 "store, not equals. X equals x plus three is not impossible math — it is an "
 "order. Take what x holds, add three, store it back. A variable holds "
 "whatever was stored most recently, in the order the cells actually ran — "
 "not the order they sit on the page. Second, quotes: seven in quotes is "
 "text, seven without quotes is a number you can do math on. Half of all "
 "beginner errors are those two getting mixed up, and when it happens to you "
 "this week — and it will — you are not behind. You are exactly on schedule. "
 "Third, the whiteboard: behind your notebook the machine keeps an invisible "
 "whiteboard of every variable alive right now. Every cell reads it and "
 "writes it. Run a cell twice and it writes twice. When a notebook starts "
 "acting haunted, restart and run all wipes the board and replays everything "
 "top to bottom, so the page and the memory finally agree. "
 "The week ends with a three-part build: make the computer work five hundred "
 "times, weave a sentence from your own variables, and cause three different "
 "errors on purpose, reading each report like a field guide. Do the practice "
 "before the notebook, and commit to every answer before revealing. The "
 "struggle is the mechanism. Press play.")

T["ds-2"] = ("Almost every dataset you will ever "
 "meet is a table: one row per thing, one column per fact. And three moves answer "
 "almost every question anyone asks of a table. Filter keeps the rows that pass a "
 "test. Sort reorders them. Group folds many rows into a few summary rows — and "
 "that folding is where findings come from. Two professional habits, starting "
 "now, while the tables are small. Count your rows before and after every filter, "
 "because code will happily average nothing and tell you no error. And always "
 "know what one row is — a city, a person, a purchase — because grouping a table "
 "you misunderstand gives a correct-looking wrong answer, and those are the "
 "dangerous ones. Eight Albanian cities are waiting in the figure. Push the "
 "moves around by hand before you type them.")

T["ds-3"] = ("A chart is a claim about data, made "
 "visual — and it can lie while every number on it is true. The trick to know is "
 "the chopped axis. Bars keep a silent promise: they start at zero, so twice the "
 "length means twice the value. Start the axis at ninety instead, and ninety-six "
 "versus one hundred stops looking like a four percent difference and starts "
 "looking like a landslide. Nothing was faked; the picture lies anyway. After "
 "today you will see this constantly — news, ads, presentations. Two more honesty "
 "rules. Label everything, because a number without units is not information. "
 "And ask whether the fair comparison is the total or the per-person number — "
 "big places have more of everything, and choosing which to show is the actual "
 "analysis. Drag the slider in the figure until the lie is yours.")

T["ds-4"] = ("Capstone week. Every real analysis "
 "is the same loop. A sharp question. A table that could answer it, where you "
 "know what one row is. The moves — filter, group, sort — with counts checked. "
 "An honest picture. And then the finding, in exactly three sentences: what I "
 "measured, what I found, and what this does not prove. That third sentence is "
 "the professional one. The failure mode this week is not broken code — it is "
 "the overclaim, a true computation dressed up as a bigger truth than it earned. "
 "Your table says coastal shops sold more in July. It does not say the sea makes "
 "people spend. The gap between those sentences is where trust lives, and the "
 "figure will calibrate you on six of them. Finish this week and you are on the "
 "lecture list.")

T["space-1"] = ("Nobody has dipped a cup into "
 "Titan's lakes, and yet we know what its air is made of. The trick is that "
 "light carries fingerprints. Spread starlight into a spectrum and you find dark "
 "lines — colors stolen by whatever gas the light passed through. Each molecule "
 "steals its own exact pattern. Methane's pattern showed up in Titan's light in "
 "nineteen forty-four, read by a telescope on Earth, decades before any "
 "spacecraft went. The same trick, pointed through the James Webb telescope, "
 "reads the air of planets around other stars today. Much of the action is in "
 "the infrared — heat-light your eye cannot see — which is why the instrument "
 "Doctor Nixon worked on, an infrared spectrometer named CIRS, could read "
 "Titan's chemistry through its haze for thirteen years. In the figure, three "
 "worlds are waiting. Read their fingerprints.")

T["space-2"] = ("Once a world looks interesting, "
 "there is a ladder of ways to visit. Fly past once, cameras blazing. Stay and "
 "orbit for years. Land. Or hardest of all, bring a piece home. Each rung costs "
 "more and reveals more, and the right rung depends entirely on the question — "
 "which is why mission design starts with the question, never the rocket. "
 "Whatever you fly carries instruments, and instruments are senses. A camera is "
 "eyes. A spectrometer is the nose from last week. Radar is touch at a distance "
 "— it beamed through Titan's haze and found the lakes no camera could see. And "
 "everything happens on a delay: Saturn is over a light-hour away, so nobody "
 "drives a probe with a joystick. By the time you see the problem, it happened "
 "an hour ago. Distant spacecraft are trusted, not steered. Design a mission in "
 "the figure and feel the trade.")

T["space-3"] = ("Titan is the only moon in the "
 "solar system with real air — mostly nitrogen, like ours, and half again as "
 "thick at the surface. But it is minus one hundred seventy-nine Celsius, and "
 "that cold rearranges everything. Water is not weather there; water is rock, "
 "frozen harder than granite, building the mountains. The job water does here "
 "is done there by methane: methane clouds, methane rain, rivers that carve "
 "valleys, and seas — the largest, Kraken Mare, outsizes the Caspian. A full "
 "weather system with the molecule swapped. The orange sky is sunlight breaking "
 "methane apart and the pieces reassembling into heavier carbon molecules — "
 "organic chemistry running planet-wide, four billion years running. That is "
 "why chemists look at Titan and see the early Earth, kept in a freezer. Hold "
 "the two worlds side by side in the figure. Next week, you find a planet "
 "yourself.")

T["space-4"] = ("Capstone week. Thousands of "
 "planets around other stars were found without a single picture of them. Here "
 "is how. Record a star's brightness, hour after hour, and plot it. If a "
 "planet's orbit carries it across the star's face, it blocks a sliver of light "
 "— a small, clean dip. Wait, and the dip returns on a perfect schedule. The "
 "schedule is the planet's year. The depth is the planet's size: the fraction "
 "of light blocked is the fraction of the star's disk covered, so the radius is "
 "the square root of the depth. A one percent dip is a planet a tenth the "
 "star's radius — roughly Jupiter. And then the discipline you learned in the "
 "data sprint: not every dip is a planet, so say what the data shows and what "
 "it does not prove. A repeating dip is a candidate until a second method "
 "confirms it. Find yours, write the three sentences, and Doctor Nixon's "
 "lecture is waiting.")


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
    print("AUDIO DONE", flush=True)


if __name__ == "__main__":
    main()
