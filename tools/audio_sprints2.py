#!/usr/bin/env python3
"""Albania Now — listen narrations, sprint 4 (AI Image Analysis on Other Planets).
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_sprints2.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/alnow-audio"
os.makedirs(WORK, exist_ok=True)

T = {}

T["img-1"] = ("When an orbiter photographs a moon, "
 "no picture crosses the solar system. What travels home is a grid of numbers — "
 "one per pixel, zero for black, two fifty-five for white. Your screen rebuilds "
 "the picture; the machine never needs to. And that is the opportunity: if an "
 "image is numbers, questions about the image become arithmetic. Where is it "
 "dark? Which numbers are small. Where is the crater rim? Where small numbers "
 "jump to large ones. Craters are the perfect first target because the Sun "
 "labels them for you — a shadowed bowl beside a sunlit rim. Scientists counted "
 "craters by hand for decades, because crater counts date a surface: more "
 "craters, older ground. This month you build the machines that do the "
 "counting. It starts with reading one grid, by hand, today.")

T["img-2"] = ("One comparison — is this pixel "
 "darker than the cutoff — turns an image into a map of yes and no. That is a "
 "threshold, and it is step one of the classical detector. Step two is the "
 "paint bucket: shadow pixels that touch each other belong to the same crater, "
 "so flood outward and call everything you reach one blob. Step three throws "
 "out the specks — a one-pixel blob is camera noise, not a crater, and the "
 "minimum size you choose quietly sets the smallest crater you can find. Say "
 "that limitation out loud; it is part of the count. Threshold, group, filter. "
 "Where does the cutoff come from? The histogram's valley — never from hope. "
 "Drag the slider in the figure and watch six true craters and a field of junk "
 "fight over your count.")

T["img-3"] = ("This week the machine stops being "
 "hand-tuned and starts learning — from examples you label. The recipe is all "
 "of machine learning in miniature. Label patches: crater, not crater. Measure "
 "features — numbers computable from any patch, like how round its dark region "
 "is. Learn a rule — ours just averages each class and asks which average a new "
 "patch lands closer to. And then the honesty rule of the entire field: grade "
 "the machine on patches it never saw. A machine graded on its own training "
 "data can score perfectly by memorizing, and the score is a lie. Held-out "
 "data, or it doesn't count. One more thing: your labels are the machine's "
 "only truth. Label carelessly and it learns your carelessness — in real "
 "planetary science, expert labeling time is the scarce ingredient.")

T["img-4"] = ("Capstone week. Run your detector "
 "on new terrain and two errors appear, and they trade against each other. "
 "Loosen the threshold: every crater caught, plus boulders and noise counted "
 "as craters — false alarms. Tighten it: the junk vanishes, and the faint "
 "small craters vanish with it — misses. No setting kills both. Spam filters, "
 "medical scans, earthquake alarms — everything that detects lives on this "
 "seesaw. So a professional never reports just a count. The report carries "
 "the settings, the measured miss rate, the measured false-alarm rate, and "
 "the smallest crater even attempted. Every clause is a boundary around the "
 "claim — your three-sentence finding, grown up. Tune it, measure it, sign "
 "it. And then bring your strangest question to Doctor Nixon.")


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
    print("AUDIO2 DONE", flush=True)


if __name__ == "__main__":
    main()
