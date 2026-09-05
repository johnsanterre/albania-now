#!/usr/bin/env python3
"""Albania Now — the top-down pacing map (John's directive 2026-09-04:
"more top down view, to make sure it's balanced").

MEASURES every lesson page, notebook, and media file — no vibes — and
computes student-minutes from stated per-activity rates. Writes PACING.md.
Run after any content change: python3 pacing.py
"""
import json, os, re, subprocess

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Per-activity rates (stated so they can be argued with and calibrated
# against a real pilot student; these deliberately lean FAST per John's
# "you think things take longer than they do").
RATES = dict(
    read_wpm=200,          # teen reading technical prose with figures nearby
    figure_min=3.0,        # one interactive figure, played properly
    practice_min=2.0,      # one attempt-then-reveal exercise
    quiz_min=0.6,          # one 3-choice question
    nb_teach_min=1.2,      # run + read one teaching cell
    nb_scaffold_min=5.0,   # one YOUR-TURN / build-part cell actually attempted
    nb_check_min=0.5,
    build_flat_min=15.0,   # written/screenshot overhead beyond notebook scaffolds
)

TARGET = (240, 360)   # minutes/lesson; center 300 = 5h. John's spec
                      # 2026-09-04: 20 HOURS of material per sprint-month.
SPRINT_TARGET = 1200  # minutes per 4-week sprint

SPRINTS = [
    ('Data Science, from zero', 'ds'),
    ('Planetary Exploration', 'space'),
    ('Intro to Large Language Models', 'llm'),
    ('AI Image Analysis on Other Planets', 'img'),
    ('Leveraging AI in Your Own Education', 'learn'),
    ('Learning to Read Python', 'read'),
    ('Learning to Learn from External Resources', 'sources'),
]


def media_minutes(path):
    if not os.path.exists(path):
        return 0.0
    try:
        out = subprocess.run(
            ['ffprobe', '-v', 'quiet', '-show_entries', 'format=duration',
             '-of', 'csv=p=0', path], capture_output=True, text=True)
        return float(out.stdout.strip()) / 60
    except Exception:
        return 0.0


def strip_tags(html):
    html = re.sub(r'<script>.*?</script>', ' ', html, flags=re.S)
    html = re.sub(r'<[^>]+>', ' ', html)
    return html


def lesson_stats(key, n):
    path = os.path.join(SITE, 'lesson-%s-%d.html' % (key, n))
    if not os.path.exists(path):
        return None
    h = open(path).read()

    def section(seg):
        m = re.search(r'<section class="seg" data-seg="%s">(.*?)</section>' % seg, h, re.S)
        return m.group(1) if m else ''

    read = section('read')
    read_words = len(strip_tags(read).split())
    figures = len(re.findall(r'Interactive · Figure|Interactive · Figure', h)) or \
        len(re.findall(r'class="fig"', h))
    practice = len(re.findall(r'class="ex"', h))
    quiz = len(re.findall(r'data-q="', h))
    deeper = len(re.findall(r'class="gd"', h))
    build_parts = len(re.findall(r'<b>Part [A-Z]', section('build'))) or 1
    videos = re.findall(r'src="video/([^"]+)"', h)
    audios = re.findall(r'src="audio/([^"]+)"', h)
    vid_min = sum(media_minutes(os.path.join(SITE, 'video', v)) for v in videos)
    aud_min = sum(media_minutes(os.path.join(SITE, 'audio', a)) for a in audios)

    nb_m = re.search(r'notebooks/([a-z0-9-]+)\.ipynb', h)
    nb_teach = nb_scaffold = nb_check = 0
    if nb_m:
        nb_path = os.path.join(SITE, 'notebooks', nb_m.group(1) + '.ipynb')
        if os.path.exists(nb_path):
            doc = json.load(open(nb_path))
            for c in doc['cells']:
                if c['cell_type'] != 'code':
                    continue
                src = ''.join(c['source'])
                first = src.strip().splitlines()[0].lower() if src.strip() else ''
                if first.startswith('# check'):
                    nb_check += 1
                elif first.startswith(('# your turn', '# part', '# the build',
                                       '# question', '# stretch', '# your',
                                       '# quest')):
                    nb_scaffold += 1
                else:
                    nb_teach += 1

    mins = dict(
        watch=vid_min,
        listen=aud_min,
        read=read_words / RATES['read_wpm'] + figures * RATES['figure_min'],
        practice=practice * RATES['practice_min'],
        code=(nb_teach * RATES['nb_teach_min'] + nb_scaffold * RATES['nb_scaffold_min']
              + nb_check * RATES['nb_check_min']),
        check=quiz * RATES['quiz_min'],
        build=RATES['build_flat_min'] * build_parts,
    )
    return dict(mins=mins, words=read_words, figures=figures, practice=practice,
                quiz=quiz, deeper=deeper, videos=len(videos), vid_min=vid_min,
                nb=(nb_teach, nb_scaffold, nb_check), build_parts=build_parts,
                total=sum(mins.values()))


def flag(total):
    lo, hi = TARGET
    if total < lo * 0.75:
        return 'UNDER'
    if total < lo:
        return 'thin'
    if total > hi:
        return 'OVER'
    return 'ok'


def main():
    out = ['# Albania Now — pacing map (measured)', '',
           'Generated by `tools/pacing.py` — rerun after any content change.',
           'Spec: **20 hours per sprint-month** = ~%d min (5h) per weekly '
           'lesson; band %d–%d. Rates are stated in the script and lean fast; '
           'calibrate against a real pilot student.' % (SPRINT_TARGET // 4, *TARGET), '']
    grand = []
    sprint_rows = []
    for sprint, key in SPRINTS:
        out.append('## %s (`%s`)' % (sprint, key))
        out.append('')
        out.append('| wk | total | flag | watch | listen | read+figs | practice | notebook | check | build | words | figs | ex | quiz | nb t/s/c | vids |')
        out.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
        stot = 0
        for n in range(1, 5):
            s = lesson_stats(key, n)
            if not s:
                out.append('| %d | — | missing | | | | | | | | | | | | | |' % n)
                continue
            m = s['mins']
            grand.append(s['total'])
            stot += s['total']
            out.append('| %d | **%dm** | %s | %.0f | %.0f | %.0f | %.0f | %.0f | %.0f | %.0f | %d | %d | %d | %d | %d/%d/%d | %d |' % (
                n, round(s['total']), flag(s['total']),
                m['watch'], m['listen'], m['read'], m['practice'], m['code'],
                m['check'], m['build'],
                s['words'], s['figures'], s['practice'], s['quiz'],
                s['nb'][0], s['nb'][1], s['nb'][2], s['videos']))
        out.append('')
        pct = round(stot / SPRINT_TARGET * 100)
        sprint_rows.append((sprint, stot, pct))
        out.append('**Sprint total: %dm of %dm target (%d%%)**' % (round(stot), SPRINT_TARGET, pct))
        out.append('')
    if grand:
        out.append('**Catalog: %d lessons measured · median %dm · min %dm · max %dm**' % (
            len(grand), round(sorted(grand)[len(grand) // 2]),
            round(min(grand)), round(max(grand))))
    out.append('')
    out.append('Legend: flag UNDER < %dm · thin < %dm · ok · OVER > %dm. '
               'nb t/s/c = notebook teaching / scaffold (your-turn) / check cells.' % (
                   int(TARGET[0] * .75), TARGET[0], TARGET[1]))
    path = os.path.join(SITE, 'PACING.md')
    open(path, 'w').write('\n'.join(out) + '\n')
    print(path)
    for line in out:
        if line.startswith(('| ', '**Catalog')):
            print(line)


if __name__ == '__main__':
    main()
