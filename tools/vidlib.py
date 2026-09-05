#!/usr/bin/env python3
"""Shared machinery for the animated lesson videos (Chicago palette).

Scene primitives here; per-course scene data lives in videos_course*.py.
Each scene is (draw_fn, narration); draw_fn animates across the exact
duration of its Kokoro narration. Run course files with the _/tts venv.
"""
import math, os, random, subprocess, sys
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
W, H, FPS = 1280, 720, 15
os.makedirs(WORK, exist_ok=True)
os.makedirs(f"{SITE}/video", exist_ok=True)

PAPER = (252, 251, 248); INK = (30, 37, 48); INK2 = (91, 101, 114)
NAVY = (126, 27, 20); STAR = (206, 58, 54); SKY = (242, 215, 213)
CARD = (255, 255, 255); HAIR = (227, 224, 216); GREEN = (27, 122, 69)
DARK = (32, 38, 46); CODEINK = (232, 236, 242); CODEGRN = (140, 200, 160)

HN = "/System/Library/Fonts/HelveticaNeue.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"
def F(size, bold=False, med=False):
    return ImageFont.truetype(HN, size, index=1 if bold else (10 if med else 0))
def FM(size, bold=False):
    return ImageFont.truetype(MENLO, size, index=1 if bold else 0)

def ease(t): return t * t * (3 - 2 * t)
def clamp01(x): return max(0.0, min(1.0, x))
def sub(t, a, b): return clamp01((t - a) / (b - a)) if b > a else 1.0
def mix(c1, c2, a): return tuple(int(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))

def chi_star(dr, cx, cy, r, fill):
    pts = []
    for i in range(12):
        ang = math.pi / 6 * i - math.pi / 2
        rad = r if i % 2 == 0 else r * 0.5
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    dr.polygon(pts, fill=fill)

def frame_base(num, total, course):
    im = Image.new("RGB", (W, H), PAPER)
    dr = ImageDraw.Draw(im)
    dr.text((80, 26), "Albania Now", font=F(22, bold=True), fill=NAVY)
    tw = dr.textlength("Albania Now ", font=F(22, bold=True))
    chi_star(dr, 80 + tw + 12, 40, 11, STAR)
    dr.text((W - 80, 28), f"{course} · {num}/{total}", font=F(16), fill=INK2, anchor="ra")
    dr.rectangle([0, H - 10, W, H], fill=SKY)
    return im, dr

def kick(dr, text, y=78):
    dr.text((80, y), text.upper(), font=F(18, bold=True), fill=STAR)

def type_text(dr, xy, text, t, font, fill, cursor=True):
    n = int(round(len(text) * clamp01(t)))
    dr.text(xy, text[:n], font=font, fill=fill)
    if cursor and 0 < t < 1:
        cw = dr.textlength(text[:n], font=font)
        dr.rectangle([xy[0] + cw + 3, xy[1] + 4, xy[0] + cw + 6,
                      xy[1] + font.size - 2], fill=STAR)

# ---------------------------------------------------------------- primitives

def s_title(kicker, big, sub_line):
    def draw(dr, t, rng):
        kick(dr, kicker)
        a = ease(sub(t, 0.03, 0.25))
        dr.text((80, 140), big, font=F(58, bold=True), fill=mix(PAPER, NAVY, a))
        type_text(dr, (80, 270), sub_line, sub(t, 0.32, 0.8), F(33), INK)
    return draw

def s_bullets(kicker, title, lines, closing=False):
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 118), title, font=F(42, bold=True), fill=NAVY)
        yy = 224
        for i, ln in enumerate(lines):
            at = 0.15 + i * (0.68 / max(1, len(lines)))
            if t > at:
                a = ease(sub(t, at, at + 0.12))
                dr.ellipse([84, yy + 13, 98, yy + 27], fill=mix(PAPER, STAR, a))
                dr.text((116, yy), ln, font=F(29, med=closing), fill=mix(PAPER, INK, a))
            yy += 70
    return draw

def _editor(dr, x, y, w, h, title="editor"):
    dr.rounded_rectangle([x, y, x + w, y + h], 10, fill=DARK)
    for i, c in enumerate([STAR, (230, 190, 80), GREEN]):
        dr.ellipse([x + 16 + i * 24, y + 12, x + 30 + i * 24, y + 26], fill=c)
    dr.text((x + w - 14, y + 10), title, font=F(14), fill=(150, 158, 170), anchor="ra")

def _browserpane(dr, x, y, w, h, url="my-site/hello.html"):
    dr.rounded_rectangle([x, y, x + w, y + h], 10, fill=CARD, outline=HAIR, width=3)
    dr.rounded_rectangle([x + 12, y + 10, x + w - 12, y + 40], 6, fill=PAPER, outline=HAIR, width=2)
    dr.text((x + 24, y + 16), url, font=F(15), fill=INK2)

def _render_item(dr, x, y, kind, text, styled):
    """Draw one 'rendered page' element; returns new y."""
    if kind == "h1":
        dr.text((x, y), text, font=F(30, bold=True), fill=NAVY if styled else INK)
        return y + 48
    if kind == "p":
        dr.text((x, y), text, font=F(18), fill=INK2 if styled else INK)
        return y + (34 if styled else 28)
    if kind == "a":
        col = NAVY
        dr.text((x, y), text, font=F(18), fill=col)
        tw = dr.textlength(text, font=F(18))
        dr.line([x, y + 24, x + tw, y + 24], fill=col, width=2)
        return y + 34
    if kind == "img":
        dr.rectangle([x, y, x + 120, y + 74], fill=mix(CARD, HAIR, 0.7), outline=HAIR, width=2)
        dr.ellipse([x + 16, y + 14, x + 40, y + 38], fill=CARD, outline=INK2, width=2)
        dr.polygon([(x + 14, y + 70), (x + 58, y + 26), (x + 106, y + 70)], fill=INK2)
        return y + 88
    if kind == "li":
        dr.ellipse([x + 6, y + 9, x + 14, y + 17], fill=INK)
        dr.text((x + 26, y), text, font=F(18), fill=INK)
        return y + 30
    if kind == "btn":
        tw = dr.textlength(text, font=F(17, med=True))
        dr.rounded_rectangle([x, y, x + tw + 34, y + 38], 7, fill=NAVY)
        dr.text((x + 17, y + 8), text, font=F(17, med=True), fill=CARD)
        return y + 52
    if kind == "gap":
        return y + 16
    return y

def s_browser(kicker, title, code, render, url="my-site/hello.html",
              style_at=None, note=None):
    """Split view: code types on the left, the page assembles on the right.
    code: list[str]; render: list[(line_idx, kind, text)] — item appears once
    its line is typed. style_at: line_idx after which the render is 'styled'."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 112), title, font=F(36, bold=True), fill=NAVY)
        ex, ey, ew, eh = 80, 180, 560, 440
        _editor(dr, ex, ey, ew, eh)
        span = (0.08, 0.78)
        prog = sub(t, *span) * len(code)
        for i, ln in enumerate(code):
            ly = ey + 44 + i * 30
            if ly > ey + eh - 34: break
            share = clamp01(prog - i)
            if share <= 0: continue
            n = int(round(len(ln) * share))
            col = CODEGRN if ln.strip().startswith("<") or ln.strip().startswith("}") \
                  or ":" in ln and "{" not in ln else CODEINK
            dr.text((ex + 22, ly), ln[:n], font=FM(17), fill=col)
        bx, by, bw, bh = 680, 180, 520, 440
        _browserpane(dr, bx, by, bw, bh, url)
        styled = style_at is not None and prog >= style_at
        if styled:
            dr.rounded_rectangle([bx + 12, by + 52, bx + bw - 12, by + bh - 12], 6,
                                 fill=PAPER)
        yy = by + 66
        for line_idx, kind, text in render:
            if prog >= line_idx + 1:
                yy = _render_item(dr, bx + 34, yy, kind, text, styled)
        if note and t > 0.82:
            dr.text((80, 648), note, font=F(23, med=True), fill=STAR)
    return draw

def s_code(kicker, title, code, console=None, note=None, err_line=None):
    """Editor pane + optional console pane. console: list[(text, color)]."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 112), title, font=F(36, bold=True), fill=NAVY)
        ex, ey, ew = 80, 180, 1120
        eh = 300 if console else 440
        _editor(dr, ex, ey, ew, eh)
        prog = sub(t, 0.08, 0.6 if console else 0.8) * len(code)
        for i, ln in enumerate(code):
            ly = ey + 44 + i * 30
            if ly > ey + eh - 30: break
            share = clamp01(prog - i)
            if share <= 0: continue
            n = int(round(len(ln) * share))
            hot = err_line is not None and i == err_line and t > 0.55
            dr.text((ex + 22, ly), ln[:n], font=FM(17),
                    fill=STAR if hot else CODEINK)
            if hot:
                tw = dr.textlength(ln, font=FM(17))
                dr.line([ex + 22, ly + 24, ex + 22 + tw, ly + 24], fill=STAR, width=3)
        if console:
            cy = ey + eh + 16
            dr.rounded_rectangle([ex, cy, ex + ew, cy + 150], 10, fill=(18, 22, 27))
            dr.text((ex + 18, cy + 8), "console", font=F(13), fill=(130, 140, 150))
            for i, (txt, col) in enumerate(console):
                at = 0.62 + i * 0.1
                if t > at:
                    dr.text((ex + 22, cy + 36 + i * 30), txt, font=FM(16), fill=col)
        if note and t > 0.85:
            dr.text((80, 655), note, font=F(23, med=True), fill=STAR)
    return draw

def s_loop(kicker, title, steps, note=None, cycles=2.0):
    """Boxes in a row with arrows and a return arc; highlight cycles through."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 118), title, font=F(42, bold=True), fill=NAVY)
        n = len(steps)
        bw = min(230, (1120 - (n - 1) * 60) // n)
        total_w = n * bw + (n - 1) * 60
        x0 = (W - total_w) // 2
        y = 330
        active = int(sub(t, 0.1, 0.95) * cycles * n) % n if t > 0.1 else -1
        for i, s in enumerate(steps):
            x = x0 + i * (bw + 60)
            on = i == active
            dr.rounded_rectangle([x, y, x + bw, y + 86], 10,
                                 fill=NAVY if on else CARD,
                                 outline=NAVY if on else HAIR, width=3)
            dr.text((x + bw / 2, y + 24), s, font=F(24, med=True),
                    fill=CARD if on else INK, anchor="ma")
            if i < n - 1:
                ax = x + bw + 8
                dr.line([ax, y + 43, ax + 44, y + 43], fill=INK2, width=4)
                dr.polygon([(ax + 44, y + 35), (ax + 58, y + 43), (ax + 44, y + 51)], fill=INK2)
        arc_y = y + 130
        dr.arc([x0 + bw / 2, y + 60, x0 + total_w - bw / 2, arc_y + 90],
               20, 160, fill=INK2, width=4)
        dr.polygon([(x0 + bw / 2 - 4, arc_y + 28), (x0 + bw / 2 + 16, arc_y + 40),
                    (x0 + bw / 2 + 12, arc_y + 16)], fill=INK2)
        dr.text((W / 2, arc_y + 64), "…and around again", font=F(20), fill=INK2, anchor="ma")
        if note and t > 0.8:
            dr.text((W / 2, 600), note, font=F(26, bold=True), fill=NAVY, anchor="ma")
    return draw

def s_chat(kicker, title, exchanges, note=None):
    """exchanges: list[(who, text)] who in {'you','ai'}; bubbles stagger in."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 112), title, font=F(36, bold=True), fill=NAVY)
        yy = 190
        for i, (who, text) in enumerate(exchanges):
            at = 0.1 + i * (0.72 / len(exchanges))
            if t > at:
                a = ease(sub(t, at, at + 0.1))
                fnt = F(20)
                words, lines, cur = text.split(" "), [], ""
                for wd in words:
                    trial = (cur + " " + wd).strip()
                    if dr.textlength(trial, font=fnt) > 660 and cur:
                        lines.append(cur); cur = wd
                    else:
                        cur = trial
                lines.append(cur)
                bh = 24 + len(lines) * 28
                maxw = max(dr.textlength(l, font=fnt) for l in lines)
                if who == "you":
                    x1 = W - 120 - maxw - 40
                    dr.rounded_rectangle([x1, yy, W - 120, yy + bh], 12,
                                         fill=mix(PAPER, SKY, a))
                    for j, l in enumerate(lines):
                        dr.text((x1 + 20, yy + 12 + j * 28), l, font=fnt,
                                fill=mix(PAPER, NAVY, a))
                else:
                    dr.rounded_rectangle([120, yy, 120 + maxw + 40, yy + bh], 12,
                                         fill=mix(PAPER, CARD, a),
                                         outline=mix(PAPER, HAIR, a), width=2)
                    for j, l in enumerate(lines):
                        dr.text((140, yy + 12 + j * 28), l, font=fnt,
                                fill=mix(PAPER, INK, a))
                yy += bh + 18
        if note and t > 0.85:
            dr.text((80, 648), note, font=F(23, med=True), fill=STAR)
    return draw

def _barpanel(dr, x, y, w, h, labels, vals, vmin, vmax, title, title_col, t):
    dr.rounded_rectangle([x, y, x + w, y + h], 8, fill=CARD, outline=HAIR, width=2)
    dr.text((x + w / 2, y + 12), title, font=F(21, bold=True), fill=title_col, anchor="ma")
    bx, by, bw_, bh = x + 50, y + 56, w - 80, h - 110
    dr.line([bx, by + bh, bx + bw_, by + bh], fill=INK2, width=3)
    dr.line([bx, by, bx, by + bh], fill=INK2, width=3)
    dr.text((x + 16, by + bh - 8), str(vmin), font=F(14), fill=INK2)
    dr.text((x + 16, by - 6), str(vmax), font=F(14), fill=INK2)
    n = len(vals)
    slot = bw_ / n
    a = ease(sub(t, 0.15, 0.6))
    for i, (lb, v) in enumerate(zip(labels, vals)):
        frac = clamp01((v - vmin) / (vmax - vmin)) * a
        x1 = bx + i * slot + slot * 0.18
        x2 = bx + (i + 1) * slot - slot * 0.18
        dr.rectangle([x1, by + bh - frac * bh, x2, by + bh], fill=SKY,
                     outline=NAVY, width=2)
        dr.text(((x1 + x2) / 2, by + bh + 8), lb, font=F(15), fill=INK2, anchor="ma")

def s_chart(kicker, title, labels, vals, claim, note=None, compare_ylim=None,
            claim2=None):
    """Bar chart with a claim title. compare_ylim=(lo,hi) adds a second,
    axis-chopped panel of the SAME data next to the honest zero-based one."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 112), title, font=F(36, bold=True), fill=NAVY)
        if compare_ylim:
            _barpanel(dr, 80, 180, 540, 430, labels, vals, 0, max(vals) + 1,
                      claim, GREEN, t)
            if t > 0.45:
                _barpanel(dr, 660, 180, 540, 430, labels, vals,
                          compare_ylim[0], compare_ylim[1],
                          claim2 or claim, STAR, sub(t, 0.45, 1.0))
        else:
            _barpanel(dr, 80, 180, 740, 440, labels, vals, 0, max(vals) + 1,
                      claim, NAVY, t)
        if note and t > 0.85:
            dr.text((80, 648), note, font=F(23, med=True), fill=STAR)
    return draw

def s_notebook(kicker, title, cells, note=None):
    """Colab-style cells. cells: list[(code_lines, out_lines)] where out_lines
    is list[(text, 'ok'|'err')]. Cells type in sequence; output follows code."""
    def draw(dr, t, rng):
        kick(dr, kicker)
        dr.text((80, 112), title, font=F(36, bold=True), fill=NAVY)
        total_units = sum(len(c) + 0.6 for c, _ in cells)
        prog = sub(t, 0.08, 0.8) * total_units
        yy = 180
        used = 0.0
        for code, outs in cells:
            cw, cx = 1120, 80
            ch = 20 + len(code) * 30 + 14
            # play button + cell
            dr.rounded_rectangle([cx, yy, cx + cw, yy + ch], 8,
                                 fill=(244, 244, 246), outline=HAIR, width=2)
            done_cell = prog >= used + len(code)
            dr.ellipse([cx + 12, yy + 12, cx + 40, yy + 40],
                       fill=NAVY if done_cell else CARD,
                       outline=NAVY, width=2)
            dr.polygon([(cx + 22, yy + 18), (cx + 34, yy + 26), (cx + 22, yy + 34)],
                       fill=CARD if done_cell else NAVY)
            for i, ln in enumerate(code):
                share = clamp01(prog - used - i)
                if share <= 0: continue
                n = int(round(len(ln) * share))
                dr.text((cx + 58, yy + 14 + i * 30), ln[:n], font=FM(17), fill=INK)
            yy += ch + 6
            if done_cell and outs:
                oh = 10 + len(outs) * 28
                for i, (txt, kind) in enumerate(outs):
                    if prog >= used + len(code) + 0.5:
                        dr.text((cx + 58, yy + 4 + i * 28), txt, font=FM(16),
                                fill=STAR if kind == "err" else INK2)
                yy += oh + 12
            used += len(code) + 0.6
        if note and t > 0.85:
            dr.text((80, 652), note, font=F(23, med=True), fill=STAR)
    return draw

# ---------------------------------------------------------------- build

def narrate(pipe, text, out_wav, pad=0.45):
    chunks = [a for _, _, a in pipe(text, voice="af_heart")]
    audio = np.concatenate(chunks)
    audio = np.concatenate([audio, np.zeros(int(24000 * pad), dtype=audio.dtype)])
    sf.write(out_wav, audio, 24000)
    return len(audio) / 24000

def build(slug, scenes, course_label, pipe):
    total = len(scenes)
    wavs, durs = [], []
    for i, (_, say) in enumerate(scenes, 1):
        wav = f"{WORK}/{slug}-{i}.wav"
        durs.append(narrate(pipe, say, wav)); wavs.append(wav)
    fdir = f"{WORK}/{slug}-frames"
    os.makedirs(fdir, exist_ok=True)
    for old in os.listdir(fdir): os.remove(f"{fdir}/{old}")
    n = 0
    for i, ((fn, _), d) in enumerate(zip(scenes, durs), 1):
        nf = int(round(d * FPS))
        rng = random.Random(i * 7919)
        for k in range(nf):
            t = (k + 0.5) / nf
            im, dr = frame_base(i, total, course_label)
            fn(dr, t, rng)
            im.save(f"{fdir}/f{n:05d}.png")
            n += 1
    allaudio = np.concatenate([sf.read(w)[0] for w in wavs])
    concat = f"{WORK}/{slug}-all.wav"
    sf.write(concat, allaudio, 24000)
    out = f"{SITE}/video/{slug}-watch.mp4"
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", f"{fdir}/f%05d.png",
                    "-i", concat, "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-r", "30", "-c:a", "aac", "-b:a", "96k", "-shortest", out],
                   capture_output=True, check=True)
    print(f"{out}  ({sum(durs)/60:.1f} min, {n} frames)", flush=True)

def build_all(lessons, course_label, only=None):
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for slug, scenes in lessons.items():
        if only and slug != only:
            continue
        build(slug, scenes, course_label, pipe)
    print("COURSE DONE", flush=True)
