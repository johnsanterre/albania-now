#!/usr/bin/env python3
"""Albania Now — port 8 Chicago First lessons into sprint format (John's
"reuse material, rebrand" directive, 2026-09-04). Copies each source page,
rebrands header/footer/nav, converts 7-segment course framing to 8-segment
week framing (adds the Go deeper segment), renames localStorage keys
chsai-* -> alnow-*, and copies+renames the rendered media.
Run: python3 port_lessons.py  (from albania/tools/)"""
import os, re, shutil, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHI = os.path.join(os.path.dirname(SITE), 'chicago-hs-ai')

HEADER = '''<header class="site"><div class="wrap">
  <a class="brand" href="index.html"><svg class="wingmark" width="26" height="18" viewBox="0 0 26 18" aria-hidden="true"><polygon points="13,2 1,10 6,10 10,14 13,9 16,14 20,10 25,10 13,2" fill="#1A1414"/><polygon points="13,9 11,17 13,14 15,17 13,9" fill="#1A1414"/></svg>Albania Now</a>
  <span class="crumb"><a href="index.html">Sprints</a> / <a href="{page}">{sprint}</a> / Week {n}</span>
</div></header>'''

DEEPER = '''<section class="seg" data-seg="deeper">
  <div class="stype">Go deeper <span style="color:var(--ink2);letter-spacing:0;text-transform:none;font-weight:400">— optional, for when the lesson wasn't enough</span></div>
  <h2>{h2}</h2>
{body}
  <p style="font-size:13.5px;color:var(--ink2)">None of this is required for the sprint. Mark this segment complete either way.</p>
  <button class="mark" data-for="deeper">Mark complete</button>
</section>

'''

PACE = ('<p style="font-size:14.5px;color:var(--ink2)">One lesson a week finishes '
        'this sprint in a month. Turn in all four builds and you are on the list '
        'for the closing lecture — that is the deal.</p>')

FOOTER = ('<footer class="site"><div class="wrap">Albania Now &middot; a Free Focus '
          'program, built with Chicago First &middot; {sprint}, week {n} of 4 '
          '&middot; complete the sprint, join the lecture.</div></footer>')

GD = {
 ('llm', 1): ('More of the machine, if you want it', '''
  <div class="gd"><b>Watch the idea again, bigger.</b> Search YouTube for
  3Blue1Brown's <i>"Large language models explained briefly"</i> — the same
  next-word machine, beautifully animated, in seven minutes.</div>
  <div class="gd"><b>A long read that goes all the way down.</b> Stephen Wolfram's
  essay <i>"What Is ChatGPT Doing … and Why Does It Work?"</i> (free online) walks
  from next-word betting to the full architecture. Ambitious, readable.</div>
  <div class="gd"><b>Stretch.</b> Your phone keyboard's suggestion bar is a tiny
  language model. Start a sentence, accept the middle suggestion ten times, and
  compare the result with Figure 3's toy. Same trick, different scale.</div>'''),
 ('llm', 2): ('More on tokens and training, if you want it', '''
  <div class="gd"><b>Chop your own text.</b> OpenAI's tokenizer playground
  (platform.openai.com/tokenizer) shows exactly how any sentence you type gets
  split into pieces. Paste English, then paste Albanian — watch the difference.</div>
  <div class="gd"><b>Stretch.</b> Find three Albanian words the tokenizer splits
  into many small pieces. What does that predict about how well models handle
  smaller languages — and what would fix it?</div>'''),
 ('llm', 3): ('Sharper defenses, if you want them', '''
  <div class="gd"><b>The phenomenon has a name.</b> The Wikipedia article
  <i>"Hallucination (artificial intelligence)"</i> catalogs real incidents —
  invented court cases, fake citations — and why the mechanism produces them.</div>
  <div class="gd"><b>Stretch.</b> Apply the verify rule to one real AI answer this
  week: anything with a number, a name, a date, or a quote gets checked against a
  source you can open. Log what survived.</div>'''),
 ('llm', 4): ('Bigger tiny models, if you want them', '''
  <div class="gd"><b>The professional version of what you just built.</b> Andrej
  Karpathy's free <i>"Let's build GPT"</i> lecture on YouTube builds a real
  transformer from scratch in code. Hard, honest, and the true next rung.</div>
  <div class="gd"><b>Stretch.</b> Retrain this week's bigram machine on a
  different corpus — song lyrics, your own essays, a public-domain book in
  Albanian — and watch the voice change. The corpus IS the voice.</div>'''),
 ('learn', 1): ('More on the three buckets, if you want it', '''
  <div class="gd"><b>Your chatbot probably has a study mode.</b> The major AI
  chatbots now ship learning modes that quiz instead of answer. Find yours —
  look for "study" or "learning" in the settings — and compare it with the
  buckets from this lesson.</div>
  <div class="gd"><b>Stretch.</b> Sort your actual current week — every task you
  owe school — into delegate, collaborate, never. Keep the list; week 4's
  capstone starts from it.</div>'''),
 ('learn', 2): ('More on retrieval, if you want it', '''
  <div class="gd"><b>The science behind the struggle.</b> retrievalpractice.org
  — a researcher-run site on why being quizzed beats rereading, with guides for
  students. The five tutor settings in this lesson come straight from these
  findings.</div>
  <div class="gd"><b>Stretch.</b> Before your next real test, run one full tutor
  session with the five settings — and note which question you missed that
  rereading would never have caught.</div>'''),
 ('learn', 3): ('More on the honesty line, if you want it', '''
  <div class="gd"><b>Find your school's actual policy.</b> Ask a teacher what the
  school's AI rule is, in writing. If there isn't one, that is a conversation
  worth starting — bring this lesson's disclosure sentence as a proposal.</div>
  <div class="gd"><b>Stretch.</b> Take one paragraph you already wrote and run it
  down both paths — ghostwriter ("rewrite this") and coach ("critique this, do
  not rewrite"). Put the results side by side. Decide which version you could
  defend out loud, sentence by sentence.</div>'''),
 ('learn', 4): ('Running the week with company, if you want it', '''
  <div class="gd"><b>Recruit one classmate.</b> The capstone week is better run
  in pairs: same rules, separate logs, then swap playbooks on Friday and defend
  the differences.</div>
  <div class="gd"><b>Stretch.</b> After the week, write the one rule you would
  give a younger student starting with AI — and bring it to Dr. Teneva's
  lecture. She has spent a career on this question.</div>'''),
}

PORT = [
 ('lesson-ai-1',    'llm',   1, 'Intro to Large Language Models', 'sprint-llm.html', 'ai-1'),
 ('lesson-ai-2',    'llm',   2, 'Intro to Large Language Models', 'sprint-llm.html', 'ai-2'),
 ('lesson-ai-6',    'llm',   3, 'Intro to Large Language Models', 'sprint-llm.html', 'ai-6'),
 ('lesson-tiny-2',  'llm',   4, 'Intro to Large Language Models', 'sprint-llm.html', 'tiny-2'),
 ('lesson-think-1', 'learn', 1, 'Leveraging AI in Your Own Education', 'sprint-learning.html', 'think-1'),
 ('lesson-think-3', 'learn', 2, 'Leveraging AI in Your Own Education', 'sprint-learning.html', 'think-3'),
 ('lesson-think-4', 'learn', 3, 'Leveraging AI in Your Own Education', 'sprint-learning.html', 'think-4'),
 ('lesson-think-8', 'learn', 4, 'Leveraging AI in Your Own Education', 'sprint-learning.html', 'think-8'),
]


def port(src, key, n, sprint, page, media):
    h = open(os.path.join(CHI, src + '.html')).read()
    old_key = re.search(r"KEY='(chsai-[a-z]+-\d)'", h).group(1)
    new_key = 'alnow-%s-%d' % (key, n)

    h = h.replace(' · Chicago First</title>', ' · Albania Now</title>')
    h = re.sub(r'<header class="site">.*?</header>',
               HEADER.format(page=page, sprint=sprint, n=n), h, count=1, flags=re.S)
    h = re.sub(r'<p class="kicker">[^<]*</p>',
               '<p class="kicker">%s · Week %d of 4 · about 2–4 hours</p>' % (sprint, n),
               h, count=1)
    h = h.replace('of 7 segments', 'of 8 segments')
    h = h.replace('<h2>Listen: two minutes before you go on</h2>',
                  '<h2>Before you read</h2>')
    h = h.replace("'try','check'", "'try','deeper','check'")
    h = h.replace("'code','check'", "'code','deeper','check'")
    h2, body = GD[(key, n)]
    h = h.replace('<section class="seg" data-seg="check">',
                  DEEPER.format(h2=h2, body=body) + '<section class="seg" data-seg="check">', 1)
    h = h.replace("KEY='%s'" % old_key, "KEY='%s'" % new_key)
    h = re.sub(r'<p style="font-size:14\.5px;color:var\(--ink2\)">Pace:.*?</p>',
               PACE, h, count=1, flags=re.S)
    for a, b in [('Complete lesson %d' % n, 'Complete week %d' % n),
                 ('Lesson %d complete' % n, 'Week %d complete' % n),
                 ('Finish the lesson', 'Finish week %d' % n)]:
        h = h.replace(a, b)
    prev = ('<a href="%s">&larr; Sprint page</a>' % page) if n == 1 else \
           ('<a href="lesson-%s-%d.html">&larr; Week %d</a>' % (key, n - 1, n - 1))
    nxt = ('<a href="lesson-%s-%d.html">Week %d &rarr;</a>' % (key, n + 1, n + 1)) if n < 4 else \
          ('<a href="%s">Back to the sprint &rarr;</a>' % page)
    h = re.sub(r'<p style="margin:30px 0;display:flex;justify-content:space-between">.*?</p>',
               '<p style="margin:30px 0;display:flex;justify-content:space-between">%s %s</p>' % (prev, nxt),
               h, count=1, flags=re.S)
    h = re.sub(r'<footer class="site">.*?</footer>',
               FOOTER.format(sprint=sprint, n=n), h, count=1, flags=re.S)

    # media: copy + rename
    for kind, sub, ext in [('watch', 'video', 'mp4'), ('listen', 'audio', 'm4a')]:
        old = 'chsai-%s-%s.%s' % (media, kind, ext)
        new = '%s-%s.%s' % (new_key, kind, ext)
        src_f = os.path.join(CHI, sub, old)
        if os.path.exists(src_f):
            shutil.copy2(src_f, os.path.join(SITE, sub, new))
            h = h.replace('%s/%s' % (sub, old), '%s/%s' % (sub, new))
        else:
            print('  MISSING MEDIA:', src_f)

    # notebook links (tiny-2): point at the albania-now repo + copy the file
    if 'tiny2-bigram-machine' in h:
        h = h.replace('github/johnsanterre/chicago-hs-ai', 'github/johnsanterre/albania-now')
        shutil.copy2(os.path.join(CHI, 'notebooks', 'tiny2-bigram-machine.ipynb'),
                     os.path.join(SITE, 'notebooks', 'tiny2-bigram-machine.ipynb'))

    out = os.path.join(SITE, 'lesson-%s-%d.html' % (key, n))
    open(out, 'w').write(h)

    leftovers = [x for x in re.findall(r'chsai-[a-z0-9-]+', h)]
    chic = h.count('Chicago First') + h.count('Chicago HS AI')
    print('%s -> %s  (chsai refs: %d, chicago refs: %d)' % (src, out, len(leftovers), chic))
    if leftovers[:3]:
        print('   ', leftovers[:3])


for row in PORT:
    port(*row)
print('PORT DONE')
