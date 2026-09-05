#!/usr/bin/env python3
"""Albania Now — lesson-page builder.

Generates lesson-{key}-{n}.html from TPL + LESSONS below. The HTML files
are the deliverable; this script is the source of truth for regenerating
them. Format: the Chicago First lesson anatomy extended to 8 segments
(watch, listen, read & play, code, go deeper, check, build, done) —
John's ask 2026-09-04: ~50% more material per lesson than Chicago First.

Run: python3 build_lessons.py   (from albania/tools/; writes into albania/)
"""
import os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TPL = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>@@TITLE@@ · Albania Now</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html"><svg class="wingmark" width="26" height="18" viewBox="0 0 26 18" aria-hidden="true"><polygon points="13,2 1,10 6,10 10,14 13,9 16,14 20,10 25,10 13,2" fill="#1A1414"/><polygon points="13,9 11,17 13,14 15,17 13,9" fill="#1A1414"/></svg>Albania Now</a>
  <span class="crumb"><a href="index.html">Sprints</a> / <a href="@@SPRINTPAGE@@">@@SPRINT@@</a> / Week @@N@@</span>
</div></header>

<div class="wrap">
<p class="kicker">@@SPRINT@@ · Week @@N@@ of 4 · about 2–4 hours</p>
<h1>@@TITLE@@</h1>
<p class="lede">@@LEDE@@</p>

<div class="progresswrap">
  <div class="progressbar"><div id="pbar"></div></div>
  <div class="plabel"><span id="pdone">0</span> of @@NSEG@@ segments complete</div>
</div>

<section class="seg" data-seg="watch">
  <div class="stype">Watch</div>
  <h2>@@WATCH_H2@@</h2>
  <video controls preload="metadata" style="width:100%;border-radius:8px;background:#000"
    src="video/alnow-@@KEY@@-@@N@@-watch.mp4"></video>
  <p style="font-size:13px;color:var(--ink2);margin:6px 0 0">@@WATCH_NOTE@@
  <span style="color:var(--ink2)">(Animated explainer with narration; a recorded lecture can replace it later.)</span></p>
@@WATCH2@@
  <button class="mark" data-for="watch">Mark complete</button>
</section>

<section class="seg" data-seg="listen">
  <div class="stype">Listen</div>
  <h2>Before you read</h2>
  <p>@@LISTEN_LINE@@</p>
  <audio controls preload="none" style="width:100%" src="audio/alnow-@@KEY@@-@@N@@-listen.m4a"></audio>
  <button class="mark" data-for="listen">Mark complete</button>
</section>

<section class="seg" data-seg="read">
  <div class="stype">Read &amp; play</div>
  <h2>@@READ_H2@@</h2>

@@READ_HTML@@
  <button class="mark" data-for="read">Mark complete</button>
</section>

@@PRACTICE@@<section class="seg" data-seg="code">
  <div class="stype">Code</div>
  <h2>@@CODE_H2@@</h2>
  <p>@@CODE_INTRO@@</p>
  <p style="display:flex;gap:1em;align-items:center;flex-wrap:wrap">
    <a class="colab-btn" href="https://colab.research.google.com/github/johnsanterre/albania-now/blob/main/notebooks/@@NB@@.ipynb" target="_blank" rel="noopener">&#9654;&nbsp;Open in Colab</a>
    <a href="notebooks/@@NB@@.ipynb" download style="font-size:13.5px">or download the .ipynb</a>
  </p>
  <details style="margin-top:6px"><summary style="cursor:pointer;font-weight:600">First time in Colab?</summary>
    <ol style="font-size:14.5px">
      <li>The button opens the notebook directly in Colab — sign in with a Google account.</li>
      <li><b>File &rarr; Save a copy in Drive</b> right away, so your work is yours.</li>
      <li>Run cells top to bottom with the &#9654; button or <b>Shift+Enter</b>.</li>
    </ol>
    <p style="font-size:13px;color:var(--ink2)">Offline or blocked? Use the download link and
    <b>File &rarr; Upload notebook</b> in Colab instead.</p>
  </details>
  <button class="mark" data-for="code">Mark complete</button>
</section>

<section class="seg" data-seg="deeper">
  <div class="stype">Go deeper <span style="color:var(--ink2);letter-spacing:0;text-transform:none;font-weight:400">— optional, for when the lesson wasn't enough</span></div>
  <h2>@@DEEPER_H2@@</h2>
@@DEEPER_HTML@@
  <p style="font-size:13.5px;color:var(--ink2)">None of this is required for the sprint. Mark this segment complete either way.</p>
  <button class="mark" data-for="deeper">Mark complete</button>
</section>

<section class="seg" data-seg="check">
  <div class="stype">Quick check</div>
  <h2>Check yourself</h2>
@@QUIZ_HTML@@
</section>

<section class="seg" data-seg="build">
  <div class="stype">Build</div>
  <h2>@@BUILD_H2@@</h2>
  <div class="buildtask">

@@BUILD_HTML@@
  </div>
  <button class="mark" data-for="build">Mark complete</button>
</section>

<section class="seg" data-seg="done">
  <div class="stype">Done</div>
  <h2 id="doneHead">Finish week @@N@@</h2>
  <p id="doneMsg">Complete the segments above, then claim the finish here.</p>
  <p style="font-size:14.5px;color:var(--ink2)">One lesson a week finishes this sprint
  in a month. Turn in all four builds and you are on the list for the closing
  lecture — that is the deal.</p>
  <button class="mark" id="finishBtn" data-for="done" disabled>Complete week @@N@@</button>
</section>

<p style="margin:30px 0;display:flex;justify-content:space-between">@@PREV@@ @@NEXT@@</p>
</div>

<footer class="site"><div class="wrap">Albania Now &middot; a Free Focus program,
built with Chicago First &middot; @@SPRINT@@, week @@N@@ of 4 &middot;
watch &rarr; listen &rarr; read &rarr; code &rarr; deeper &rarr; check &rarr; build &rarr; done.</div></footer>

<script>
(function(){
  const KEY='alnow-@@KEY@@-@@N@@';
  const SEGS=@@SEGS_JS@@;
  document.querySelectorAll('.seg .stype').forEach((el,i)=>{
    el.insertBefore(document.createTextNode((i+1)+' \\u00b7 '),el.firstChild)});
  document.querySelectorAll('.ex').forEach((ex,i)=>{
    const b=ex.querySelector('.exbtn'),a=ex.querySelector('.exans');
    if(b&&a){a.hidden=true;b.addEventListener('click',()=>{
      a.hidden=!a.hidden;b.textContent=a.hidden?'Show the answer':'Hide the answer'})}});
  let state={};
  try{state=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){state={}}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
  function segEl(id){return document.querySelector('.seg[data-seg="'+id+'"]')}
  function render(){
    let n=0;
    for(const s of SEGS){
      const done=!!state[s]; if(done)n++;
      const el=segEl(s); el.classList.toggle('done',done);
      const b=el.querySelector('button.mark[data-for="'+s+'"]');
      if(b&&s!=='done'){b.disabled=false;b.textContent=done?'\\u2713 Complete — undo':'Mark complete'}
    }
    document.getElementById('pbar').style.width=(n/SEGS.length*100)+'%';
    document.getElementById('pdone').textContent=n;
    const others=SEGS.slice(0,-1).every(s=>state[s]);
    const fin=document.getElementById('finishBtn');
    if(state.done){fin.disabled=false;fin.textContent='\\u2713 Week @@N@@ complete — undo';
      document.getElementById('doneHead').textContent='Week @@N@@ complete';
      document.getElementById('doneMsg').textContent='Logged. The next lesson is waiting when you are.';}
    else{fin.disabled=!others;fin.textContent='Complete week @@N@@';
      document.getElementById('doneHead').textContent='Finish week @@N@@';
      document.getElementById('doneMsg').textContent=others?
        'Everything above is done — claim it.':'Complete the segments above, then claim the finish here.'}
  }
  document.querySelectorAll('button.mark').forEach(b=>{
    b.addEventListener('click',()=>{
      const sg=b.dataset.for;state[sg]=!state[sg];save();render();})
  });
  const groups=[...document.querySelectorAll('[data-q]')];
  const right={};
  groups.forEach(g=>{
    const q=g.dataset.q;
    g.querySelectorAll('.choice').forEach(c=>{
      c.addEventListener('click',()=>{
        const ok=c.dataset.ok==='1';
        g.querySelectorAll('.choice').forEach(x=>x.classList.remove('right','wrong'));
        c.classList.add(ok?'right':'wrong');
        document.getElementById('fb'+q).textContent=ok?
          'Right.':'Not quite — the Read segment has what you need. Try again.';
        right[q]=ok;
        if(groups.every(x=>right[x.dataset.q])){state.check=true;save();render()}
      })
    })
  });
  render();
})();
</script>
<script>
/* ---- figure ---- */
@@FIG_JS@@
</script>
<script data-goatcounter="https://johnsanterre.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''


def quiz(qs):
    out = []
    for i, (q, choices) in enumerate(qs, 1):
        attr = '' if i == 1 else ' style="margin-top:1.2em"'
        out.append('  <p%s><b>%d. %s</b></p>' % (attr, i, q))
        out.append('  <div data-q="%d">' % i)
        for text, ok in choices:
            out.append('    <button class="choice" data-ok="%d">%s</button>' % (1 if ok else 0, text))
        out.append('  </div>')
        out.append('  <p class="feedback" id="fb%d"></p>' % i)
    return '\n'.join(out)


DS = ('Data Science, from zero', 'sprint-data.html', 'ds')
SP = ('Planetary Exploration', 'sprint-space.html', 'space')

LESSONS = []

# ================================================================ DS 1
LESSONS.append(dict(sprint=DS, n=1, nb='ds1-first-steps',
 title='Code in your browser',
 lede='Scroll straight down. Watch, listen, read, run real Python on a Google '
      'computer, go deeper if you want, answer the check, build one thing. '
      'When the bar hits 100%, week 1 is done.',
 watch_h2='What Colab is, in three minutes',
 watch_note='A notebook, a play button, and a computer far away.',
 listen_line='What actually happens when you press play — and why nothing you do '
      'this month can break anything.',
 read_h2='Cells, the play button, and reports',
 read_html='''
  <p>You are about to write real code, and you will not install anything. The tool
  is <b>Google Colab</b> — a notebook that runs in your browser. A notebook is a page
  made of <b>cells</b>. A cell holds either text or code. Code cells have a play
  button on the left edge. Press it, and the code runs on a Google computer far
  away; the result appears under the cell about a second later.</p>
  <p>That distance matters. The code does not run on your laptop, your school
  Chromebook, or your phone. It runs in a data center, and only the result travels
  back. Which means:</p>
  <p><b>Nothing you do can break your computer.</b> Experiment freely. The worst
  case is an error message, and error messages are the next thing to learn.</p>
  <p><b>Errors are reports, not judgments.</b> Red text is the computer telling you
  exactly what stopped it, usually with the line number and often with a guess at
  the fix. People who read the report go fast; people who panic at red text go
  slow. That is the single biggest difference between beginners who thrive and
  beginners who quit.</p>
  <p><b>Cells run in the order you run them</b>, not the order they sit on the page.
  If a notebook starts acting haunted — cells disagreeing with each other —
  <i>Runtime &rarr; Restart and run all</i> reruns everything top to bottom. Fixes
  it almost every time.</p>
  <p>Two more ideas and you are ready for the notebook. First, a <b>variable</b> is
  a name for a value: <span style="font-family:ui-monospace,Menlo,monospace">city =
  "Tirana"</span> stores the word, and from then on <span
  style="font-family:ui-monospace,Menlo,monospace">city</span> means that word.
  Second, Python treats text and numbers differently: <span
  style="font-family:ui-monospace,Menlo,monospace">"7"</span> in quotes is text,
  <span style="font-family:ui-monospace,Menlo,monospace">7</span> without quotes is
  a number you can do math on. Half of all beginner errors are those two getting
  mixed up — so when you see one this week, you will know you are on schedule.</p>
  <p>Now prove you can read reports:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Read the report</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Three cells, three results. For each: what is the computer telling you?</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>

  <h3 style="margin-top:26px">Variables — the notebook's memory</h3>
  <p>A variable is a name with a value stored under it. Three rules govern all
  of them, and all three fit in one small program:</p>
  <pre class="code">x = 4
x = x + 3
emri = "Ana"
print(emri, x)</pre>
  <p><b>Rule 1: <span style="font-family:ui-monospace,Menlo,monospace">=</span>
  means store, not equals.</b> <span style="font-family:ui-monospace,Menlo,monospace">x
  = x + 3</span> is not an equation (it would be a false one) — it is an order:
  take what x holds, add 3, store the result back under the name x.</p>
  <p><b>Rule 2: the last store wins.</b> A variable holds exactly one value —
  whatever was stored most recently, in the order the cells actually ran.</p>
  <p><b>Rule 3: quotes decide whether a word is a name or text.</b>
  <span style="font-family:ui-monospace,Menlo,monospace">print(emri)</span> looks
  up the name and shows <i>Ana</i>;
  <span style="font-family:ui-monospace,Menlo,monospace">print("emri")</span>
  shows the word <i>emri</i>, because quotes mean "this is the text itself."</p>
  <p>Trace it yourself:</p>

  <div class="fig" id="fig2">
    <div class="figlabel">Interactive · Figure 2</div>
    <h3>Trace the program</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">The four-line program above,
    three questions. Predict before you click.</p>
    <div id="q2"></div>
    <p class="fignote" id="q2sum"></p>
  </div>

  <h3 style="margin-top:26px">Number, text, and the third thing</h3>
  <p>Every expression you write lands in one of three bins: it makes a
  <b>number</b>, it makes <b>text</b>, or it makes an <b>error report</b>. The
  glue operator <span style="font-family:ui-monospace,Menlo,monospace">+</span>
  joins two texts or adds two numbers, but refuses to mix them —
  <span style="font-family:ui-monospace,Menlo,monospace">str(16)</span> converts
  a number into text when you need the mix, and
  <span style="font-family:ui-monospace,Menlo,monospace">int("16")</span> goes
  the other way. Two surprises worth meeting now: division always gives a
  decimal (<span style="font-family:ui-monospace,Menlo,monospace">10 / 4</span>
  is 2.5, not 2), and multiplying text repeats it —
  <span style="font-family:ui-monospace,Menlo,monospace">"Va" * 3</span> is
  <i>VaVaVa</i>. Sort all eight:</p>

  <div class="fig" id="fig3">
    <div class="figlabel">Interactive · Figure 3</div>
    <h3>Number, text, or error?</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Eight expressions. Call each
    one before the computer does.</p>
    <div id="q3"></div>
    <p class="fignote" id="q3sum"></p>
  </div>
''',
 watch2=('Worked example: a first session, errors included', 'alnow-ds-1b-watch.mp4'),
 practice=dict(
  h2='Ten predictions before the notebook',
  intro='Paper-and-brain work: for each exercise, commit to an answer — say it '
        'out loud or write it down — then reveal. These are exactly the moves '
        'the notebook will ask your fingers to make.',
  items=[
   ('What does <pre>print(3 * 7)</pre> show?',
    '<b>21.</b> Both sides are numbers, so * is arithmetic.'),
   ('What does <pre>print("3" + "7")</pre> show?',
    '<b>37</b> — as text. Quotes make them text, and + glues text end to end.'),
   ('This cell fails: <pre>pritn("tungjatjeta")</pre> What will the report say, roughly — and what is the fix?',
    '<b>NameError: name ’pritn’ is not defined — did you mean print?</b> '
    'The fix is the spelling. The report even guesses it for you.'),
   ('What does this show? <pre>x = 5\nx = x + 2\nprint(x)</pre>',
    '<b>7.</b> Line 2 is an order, not an equation: take 5, add 2, store back under x.'),
   ('This cell fails: <pre>print("years: " + 12)</pre> Why — and name TWO different fixes.',
    '<b>TypeError</b> — text and a number cannot be glued. Fix 1: '
    '<span style="font-family:ui-monospace,Menlo,monospace">str(12)</span>. '
    'Fix 2: a comma — <span style="font-family:ui-monospace,Menlo,monospace">print("years:", 12)</span>.'),
   ('Cell A says <pre>print(qyteti)</pre> and cell B says <pre>qyteti = "Vlorë"</pre> '
    'You run A first, then B. What happens, and what is the one-move cure?',
    '<b>A fails with NameError</b> — qyteti did not exist yet when A ran. Cells run in the '
    'order YOU run them. Cure: <b>Runtime → Restart and run all</b>.'),
   ('Write one line that prints your name 3 times in a row. (Hint: the * surprise from the reading.)',
    '<pre>print("Drita " * 3)</pre> Multiplying text repeats it. A loop works too — that is the build.'),
   ('What does this show? <pre>emri = "Drita"\nprint("emri")</pre>',
    '<b>emri</b> — the word itself. The quotes in line 2 mean "this text, literally," '
    'so the variable is never looked up.'),
   ('What does <pre>print(10 / 4)</pre> show?',
    '<b>2.5.</b> Division always produces a decimal in Python — even 8 / 4 shows 2.0.'),
   ('This fails: <pre>mosha = "16"\nprint(mosha + 1)</pre> Why — and the fix?',
    '<b>TypeError</b> — "16" in quotes is text, and text + number refuses. Fix: '
    '<span style="font-family:ui-monospace,Menlo,monospace">int(mosha) + 1</span> '
    'converts the text into a number first.'),
  ]),
 code_h2='Open your first notebook',
 code_intro='The notebook walks everything above with your-turn cells: print, '
      'variables, text vs numbers, one deliberate error to read, and the build at '
      'the end.',
 deeper_h2='More road, if you want it',
 deeper_html='''
  <div class="gd"><b>Colab's own welcome tour.</b> Open
  <a href="https://colab.research.google.com/notebooks/intro.ipynb" target="_blank" rel="noopener">colab.research.google.com/notebooks/intro.ipynb</a>
  — Google's official introduction notebook. Fifteen minutes, and you will have seen
  every button that matters.</div>
  <div class="gd"><b>Python's official starting point.</b>
  <a href="https://www.python.org/about/gettingstarted/" target="_blank" rel="noopener">python.org/about/gettingstarted</a>
  — where the language itself points beginners.</div>
  <div class="gd"><b>Stretch build.</b> Sit someone in your family in front of your
  notebook for five minutes. Show them a cell, the play button, and one error.
  Teaching it is the fastest way to find out what you actually understood.</div>
''',
 quiz=[
  ('Where does your code actually run when you press play in Colab?',
   [('On your own laptop or phone', 0),
    ('On a computer in a Google data center — only the result comes back', 1),
    ('Inside the web page itself', 0)]),
  ('A cell prints red error text. What is the right move?',
   [('Restart your computer', 0),
    ('Read it — it names what stopped the code, often with a suggested fix', 1),
    ('Delete the notebook and start again', 0)]),
  ('What is the difference between 7 and "7" in Python?',
   [('Nothing — Python figures it out', 0),
    ('7 is a number you can do math on; "7" is text', 1),
    ('"7" is more precise', 0)]),
  ('A variable is best described as…',
   [('a name with a value stored under it', 1),
    ('a special kind of number', 0),
    ('a cell that runs automatically', 0)]),
  ('x = 4 runs, then x = 9 runs, then print(x). What shows?',
   [('4 — the first value is protected', 0),
    ('9 — the last store wins', 1),
    ('49', 0)]),
  ('Which line prints the literal word emri instead of looking up a variable?',
   [('print(emri)', 0), ('print("emri")', 1), ('print(str(emri))', 0)]),
  ('You run cell 3, then cell 1, then cell 2. Python’s memory now reflects…',
   [('the order they sit on the page', 0),
    ('the order you actually ran them: 3, 1, 2', 1),
    ('only the last cell', 0)]),
  ('print("Age " + str(16)) works, while print("Age " + 16) fails, because…',
   [('str converts the number into text, so + can glue two texts', 1),
    ('16 is too large to print', 0),
    ('spaces are not allowed before numbers', 0)]),
  ('What does print(10 / 4) show?',
   [('2', 0), ('2.5 — division gives decimals', 1), ('2 remainder 2', 0)]),
 ],
 build_h2='The three-part build',
 build_html='''
  <p><b>Part A — scale.</b> Make a cell that prints a sentence about your town
  500 times. You have not been taught how — that is on purpose. Ask an AI
  assistant or search, run what you get, and make sure you understand every word
  before keeping it. Then change it to print the numbers 1 to 500.</p>
  <p><b>Part B — the mad-lib.</b> Three variables — emri, mosha, qyteti (name,
  age, town) — and one print that weaves them into a sentence. Change the
  values, rerun, watch the sentence follow the variables.</p>
  <p><b>Part C — the error safari.</b> Cause three DIFFERENT errors on purpose:
  a NameError, a TypeError, and a SyntaxError. For each, write one sentence
  reading the report — what stopped the code and where.</p>
  <p><b>Turn-in:</b> screenshots of all three parts (part C includes your three
  one-sentence readings), to your teacher.</p>
''',
 fig_js='''
(function(){
  const QS=[
 {q:'emri = "Arber"\\nprint(emri)\\n\\n>>> Arber',mono:true,a:0,
  opts:["It stored the name in a variable, then printed what the variable holds",
        "It printed the word emri","It sent the name to Google"],
  why:"A variable is a name for a value. print(emri) looks up what emri holds and shows it."},
 {q:'print(vitet)\\n\\n>>> NameError: name \\'vitet\\' is not defined',mono:true,a:1,
  opts:["Python does not allow Albanian words",
        "The computer was asked for a variable that was never created — the report even names it",
        "The notebook crashed"],
  why:"NameError means: you used a name I have never seen. Create the variable first, or check the spelling."},
 {q:'print("age: " + 16)\\n\\n>>> TypeError: can only concatenate str (not "int") to str',mono:true,a:2,
  opts:["16 is too big a number","print can only show one thing at a time",
        "Text and a number cannot be glued with + — the report says a str met an int"],
  why:'Half of beginner errors are text-vs-number mixups. str(16) turns the number into text, and the glue works.'}];
  const wrap=document.getElementById('q1');let done=0,score=0;
  QS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq"'+(q.mono?' style="font-family:ui-monospace,Menlo,monospace;font-size:14px;white-space:pre-wrap"':'')+'></div>';
    card.querySelector('.qq').textContent=q.q;
    q.opts.forEach((opt,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=opt;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=j===q.a;if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach((x,k)=>{
          x.disabled=true;if(k===q.a)x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Called it.</b> ':'<b>Reveal:</b> ')+q.why;
        card.appendChild(fb);
        if(done===QS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+QS.length+'.</b> Errors read, not feared — that is the whole skill.';
      });
      card.appendChild(b);});
    wrap.appendChild(card);});
})();

/* ---- Figure 2: trace the program ---- */
(function(){
  const QS=[
 {q:'After line 2 runs, what does x hold?',a:1,opts:['4','7','x + 3'],
  why:'Line 2 is an order: take what x holds (4), add 3, store 7 back under x. The last store wins.'},
 {q:'What does line 4 print?',a:0,opts:['Ana 7','emri x','"Ana" "7"'],
  why:'Both names are looked up: emri holds Ana, x holds 7. No quotes around them, so they are lookups, not text.'},
 {q:'Swap lines 1 and 2 (so x = x + 3 runs FIRST). What happens?',a:2,
  opts:['x becomes 3','x becomes 7 anyway','NameError — x is used before it exists'],
  why:'x = x + 3 must look up x before storing — and nothing is stored under x yet. Order of execution is everything.'}];
  const wrap=document.getElementById('q2');let done=0,score=0;
  QS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq"></div>';
    card.querySelector('.qq').textContent=q.q;
    q.opts.forEach((opt,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=opt;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=j===q.a;if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach((x,k)=>{
          x.disabled=true;if(k===q.a)x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Traced it.</b> ':'<b>Reveal:</b> ')+q.why;
        card.appendChild(fb);
        if(done===QS.length)document.getElementById('q2sum').innerHTML=
          '<b>'+score+' of '+QS.length+'.</b> Tracing by hand is how programmers debug in their heads.';
      });
      card.appendChild(b);});
    wrap.appendChild(card);});
})();

/* ---- Figure 3: number, text, or error ---- */
(function(){
  const ES=[
 ['5 + 5',0,'10 — two numbers, arithmetic.'],
 ['"5" + "5"',1,'"55" — two texts, glued end to end.'],
 ['"5" + 5',2,'TypeError — text refuses to glue to a number. str() or int() bridges them.'],
 ['2026 - 16',0,'2010 — plain arithmetic.'],
 ['"Va" * 3',1,'"VaVaVa" — multiplying text repeats it. Genuinely useful, genuinely surprising.'],
 ['vitet',2,'NameError — no quotes, so Python looks up a variable named vitet, and none exists.'],
 ['str(7) + "!"',1,'"7!" — str turned the number into text, and text + text glues.'],
 ['10 / 4',0,'2.5 — division always gives a decimal.']];
  const LAB=['Number','Text','Error'];
  const wrap=document.getElementById('q3');let done=0,score=0;
  ES.forEach(e=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-family:ui-monospace,Menlo,monospace;font-size:15px"></div>';
    card.querySelector('.qq').textContent=e[0];
    LAB.forEach((lbl,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=lbl;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=j===e[1];if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach((x,k)=>{
          x.disabled=true;if(k===e[1])x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Called it.</b> ':'<b>Reveal:</b> ')+e[2];
        card.appendChild(fb);
        if(done===ES.length)document.getElementById('q3sum').innerHTML=
          '<b>'+score+' of '+ES.length+'.</b> Three bins cover everything you will ever type.';
      });
      card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ DS 2
LESSONS.append(dict(sprint=DS, n=2, nb='ds2-tables',
 title='Tables — most data is a table',
 lede='Rows are things, columns are facts about them. This week you load a real '
      'table and make it answer questions: filter, sort, group.',
 watch_h2='Rows, columns, and the three moves',
 watch_note='Filter, sort, group — nearly every data question is one of these.',
 listen_line='Why a table of eight cities is enough to learn the three moves that '
      'run all of data science.',
 read_h2='Filter, sort, group',
 read_html='''
  <p>Almost every dataset you will ever meet is a <b>table</b>: one row per thing,
  one column per fact. A table of cities: each row is a city, the columns are its
  region, its population, whether it touches the sea. A table of football matches:
  each row a match, the columns the teams and the score. Once data is a table,
  three moves answer nearly every question.</p>
  <p><b>Filter</b> keeps only the rows that pass a test. <i>Coastal cities only.
  Population over 100,000 only.</i> The table gets shorter; the columns stay.</p>
  <p><b>Sort</b> reorders rows by a column. <i>Largest population first.</i>
  Nothing is lost — the order changes.</p>
  <p><b>Group</b> folds the table: collect rows that share a value, then summarize
  each pile. <i>Group by region, count the cities in each; group by region, average
  the population.</i> Grouping turns many rows into a few — that is where findings
  come from.</p>
  <p>Two habits to install now, while the tables are small. First: <b>count before
  and after you filter.</b> If you started with 8 rows and ended with 0, your test
  was wrong, and code will happily compute averages of nothing. Second: <b>know
  what one row is.</b> The most common serious mistake in data work is grouping a
  table without knowing whether a row is a city, a person, or a measurement — the
  same code gives a correct-looking, wrong answer.</p>
  <p>In Python, the tool for tables is a library called <b>pandas</b>. You will
  meet five of its verbs in the notebook — read, look, filter, sort, group — and
  they map one-to-one onto the moves you just read. But first, run the moves by
  hand:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Eight cities, three moves</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A real table of Albanian cities
    (populations rounded, for practice). Push the buttons; watch what each move
    does to the rows.</p>
    <div id="ctl" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px"></div>
    <div id="tbl" style="overflow-x:auto"></div>
    <p class="fignote" id="tsum"></p>
  </div>
''',
 code_h2='The same moves, in pandas',
 code_intro='The notebook loads the cities table and walks the five verbs: '
      'read_csv, head, filtering with a test, sort_values, groupby. Then hands '
      'you three questions the table can answer.',
 deeper_h2='More tables, if you want them',
 deeper_html='''
  <div class="gd"><b>pandas in 10 minutes.</b>
  <a href="https://pandas.pydata.org/docs/user_guide/10min.html" target="_blank" rel="noopener">pandas.pydata.org — "10 minutes to pandas"</a>
  — the official quick tour. Skim it; recognize the verbs you just learned.</div>
  <div class="gd"><b>Albania's own numbers.</b>
  <a href="https://www.instat.gov.al/en/" target="_blank" rel="noopener">INSTAT</a>,
  the Institute of Statistics of Albania, publishes real tables about the country —
  population, education, tourism. Every one of them is rows and columns.</div>
  <div class="gd"><b>Our World in Data.</b>
  <a href="https://ourworldindata.org" target="_blank" rel="noopener">ourworldindata.org</a>
  — thousands of clean tables about the whole world, all downloadable.</div>
  <div class="gd"><b>Stretch build.</b> Find any CSV file online (INSTAT and Our
  World in Data both offer downloads), load it in your notebook with read_csv, and
  run one filter and one groupby on it.</div>
''',
 quiz=[
  ('You filter a table of 8 cities and 0 rows survive. Most likely:',
   [('There are no such cities', 0),
    ('Your test is wrong — check it before trusting anything downstream', 1),
    ('pandas removed the rows to save memory', 0)]),
  ('Which move turns many rows into a few summary rows?',
   [('Filter', 0), ('Sort', 0), ('Group', 1)]),
  ('From week 1: your code cell shows red text. That means…',
   [('the notebook is broken', 0),
    ('a report — read it, it names what stopped the code', 1),
    ('you should rerun the cell until it passes', 0)]),
 ],
 build_h2='Three questions, with receipts',
 build_html='''
  <p>Using the notebook's cities table, answer three questions in code — one
  filter, one sort, one group. For example: which coastal city is largest? How
  many cities per region? You choose the questions.</p>
  <p><b>Turn-in:</b> a screenshot showing each question as a text cell, the code,
  and the output under it. The output is the receipt.</p>
''',
 fig_js='''
(function(){
  const ROWS=[
   ["Tirana","Central",560000,"no"],["Durr\\u00ebs","Coast",200000,"yes"],
   ["Vlor\\u00eb","Coast",130000,"yes"],["Elbasan","Central",140000,"no"],
   ["Shkod\\u00ebr","North",135000,"no"],["Fier","South",120000,"no"],
   ["Kor\\u00e7\\u00eb","Southeast",75000,"no"],["Sarand\\u00eb","Coast",40000,"yes"]];
  const HEAD=["city","region","population","coastal"];
  const tbl=document.getElementById('tbl'),sum=document.getElementById('tsum');
  function render(rows,note){
    let h='<table style="border-collapse:collapse;font-size:14px;min-width:340px">'+
      '<tr>'+HEAD.map(x=>'<th style="text-align:left;padding:4px 12px;border-bottom:2px solid var(--star)">'+x+'</th>').join('')+'</tr>';
    rows.forEach(r=>{h+='<tr>'+r.map(c=>'<td style="padding:4px 12px;border-bottom:1px solid var(--hair)">'+
      (typeof c==='number'?c.toLocaleString('en'):c)+'</td>').join('')+'</tr>'});
    tbl.innerHTML=h+'</table>';sum.innerHTML=note;
  }
  function grouped(){
    const g={};ROWS.forEach(r=>{(g[r[1]]=g[r[1]]||[]).push(r[2])});
    let h='<table style="border-collapse:collapse;font-size:14px;min-width:340px">'+
      '<tr><th style="text-align:left;padding:4px 12px;border-bottom:2px solid var(--star)">region</th>'+
      '<th style="text-align:left;padding:4px 12px;border-bottom:2px solid var(--star)">cities</th>'+
      '<th style="text-align:left;padding:4px 12px;border-bottom:2px solid var(--star)">mean population</th></tr>';
    Object.keys(g).forEach(k=>{
      const m=Math.round(g[k].reduce((a,b)=>a+b,0)/g[k].length);
      h+='<tr><td style="padding:4px 12px;border-bottom:1px solid var(--hair)">'+k+'</td>'+
         '<td style="padding:4px 12px;border-bottom:1px solid var(--hair)">'+g[k].length+'</td>'+
         '<td style="padding:4px 12px;border-bottom:1px solid var(--hair)">'+m.toLocaleString('en')+'</td></tr>'});
    tbl.innerHTML=h+'</table>';
    sum.innerHTML='<b>Group by region:</b> 8 rows folded into '+Object.keys(g).length+' summary rows. This is where findings come from.';
  }
  const BTNS=[
   ['All 8 rows',()=>render(ROWS,'The full table: one row per city, one column per fact.')],
   ['Filter: coastal',()=>{const r=ROWS.filter(x=>x[3]==='yes');
     render(r,'<b>Filter:</b> 8 rows in, '+r.length+' out. Columns untouched.')}],
   ['Filter: over 100k',()=>{const r=ROWS.filter(x=>x[2]>100000);
     render(r,'<b>Filter:</b> 8 rows in, '+r.length+' out. Count before and after — always.')}],
   ['Sort by population',()=>{const r=[...ROWS].sort((a,b)=>b[2]-a[2]);
     render(r,'<b>Sort:</b> same 8 rows, new order. Nothing lost.')}],
   ['Group by region',grouped]];
  const ctl=document.getElementById('ctl');
  BTNS.forEach(([lbl,fn])=>{const b=document.createElement('button');
    b.className='choice';b.textContent=lbl;b.addEventListener('click',fn);ctl.appendChild(b)});
  BTNS[0][1]();
})();
'''))

# ================================================================ DS 3
LESSONS.append(dict(sprint=DS, n=3, nb='ds3-charts',
 title='Charts that tell the truth',
 lede='A chart is a claim. This week: the three chart types that cover most of '
      'life, and the axis trick that makes honest numbers lie.',
 watch_h2='Three charts, one crime',
 watch_note='Bar compares, line shows change, scatter shows relationship — and the '
      'chopped axis lies with true numbers.',
 listen_line='Why the same two numbers can look equal or wildly different, '
      'depending on one quiet choice about the axis.',
 read_h2='The claim, the chart, and the chop',
 read_html='''
  <p>A chart is not decoration. It is a <b>claim about data, made visual</b> — and
  like any claim it can be honest or dishonest with the exact same numbers. Three
  chart types cover most of what you will ever need:</p>
  <p><b>Bar charts compare.</b> Categories side by side — cities, teams, months as
  separate things. The eye reads the bar's <i>length</i>, which is why the axis
  trick below works so well on bars.</p>
  <p><b>Line charts show change.</b> One thing over time. The eye reads the slope —
  is it rising, falling, bending?</p>
  <p><b>Scatter plots show relationship.</b> Two facts about the same things, one
  per axis: each dot a city, across is population, up is number of schools. A
  cloud that leans is a relationship; a shapeless cloud is none.</p>
  <p>Now the crime. A bar chart's power comes from a silent promise: <b>the bars
  start at zero</b>, so twice the length means twice the value. Start the axis at
  90 instead of 0, and a 96 next to a 100 stops looking like a 4% difference and
  starts looking like a landslide. Nothing was faked — the numbers are true, the
  labels are true — and the picture lies. News graphics do this constantly, and
  after today you will spot it constantly. There are honest reasons to zoom an
  axis on a <i>line</i> chart (small changes matter in a heartbeat monitor), but a
  zoomed <i>bar</i> chart is almost always a thumb on the scale.</p>
  <p>Two more honesty rules. <b>Label everything</b> — a number without units is
  not information (96 what? lek, people, percent?). And <b>totals versus
  per-person</b>: Tirana has more of almost everything than Sarand&euml; because
  it has more people; dividing by population is often the honest comparison.
  Choosing which one to show <i>is</i> the analysis.</p>
  <p>Feel the chop with your own hands:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The chopped axis</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Two shops. Shop A sold 96, Shop B
    sold 100 — a 4% difference. Drag where the axis starts.</p>
    <div style="display:flex;align-items:flex-end;gap:40px;height:180px;margin:14px 0 4px;padding-left:8px" id="bars">
      <div style="text-align:center"><div id="barA" style="width:64px;background:var(--star);border-radius:4px 4px 0 0;transition:height .15s"></div><b>Shop A</b><br><span style="font-size:13px;color:var(--ink2)">96</span></div>
      <div style="text-align:center"><div id="barB" style="width:64px;background:var(--navy);border-radius:4px 4px 0 0;transition:height .15s"></div><b>Shop B</b><br><span style="font-size:13px;color:var(--ink2)">100</span></div>
    </div>
    <label style="font-size:14px">Axis starts at: <b id="axv">0</b>
      <input type="range" id="ax" min="0" max="95" value="0" style="width:min(300px,60vw);vertical-align:middle"></label>
    <p class="fignote" id="axsum"></p>
  </div>
''',
 code_h2='Draw both versions yourself',
 code_intro='The notebook uses matplotlib to draw the honest chart and the chopped '
      'one from the same numbers, then a line chart and a scatter — four cells, '
      'four pictures.',
 deeper_h2='Sharper eyes, if you want them',
 deeper_html='''
  <div class="gd"><b>The matplotlib gallery.</b>
  <a href="https://matplotlib.org/stable/gallery/" target="_blank" rel="noopener">matplotlib.org/stable/gallery</a>
  — every chart the library can draw, each with the code that drew it. Steal
  freely; that is what it is for.</div>
  <div class="gd"><b>A whole book on this.</b> <i>How Charts Lie</i> by Alberto
  Cairo — a data-visualization professor cataloguing exactly these tricks in real
  published graphics. If this lesson was fun, the book is more of it.</div>
  <div class="gd"><b>Stretch build.</b> This week, find one real chart in the wild
  — news, social media, an ad — that uses a chopped axis or missing labels.
  Screenshot it and write two sentences: what it shows, and what it wants you to
  believe.</div>
''',
 quiz=[
  ('A bar chart of two values, 96 and 100, starts its axis at 90. The picture now says:',
   [('B is slightly ahead — same as the data', 0),
    ('B dwarfs A — a visual claim the numbers do not make', 1),
    ('Nothing changed', 0)]),
  ('You want to show how one city\u2019s population changed over 50 years. Best tool:',
   [('Bar chart', 0), ('Line chart', 1), ('Scatter plot', 0)]),
  ('From week 2: which pandas move would you reach for to compare average income per region?',
   [('sort_values', 0), ('groupby', 1), ('head', 0)]),
 ],
 build_h2='One honest chart, one liar, one caption',
 build_html='''
  <p>In the notebook, pick any numbers you like — real or invented — and draw the
  same comparison twice: once honestly (axis at zero, labels, units) and once as a
  liar (chopped axis). Under them, write a two-sentence caption naming exactly
  what the second chart does to the viewer.</p>
  <p><b>Turn-in:</b> a screenshot of both charts and your caption.</p>
''',
 fig_js='''
(function(){
  const A=96,B=100,H=150;
  const ax=document.getElementById('ax'),axv=document.getElementById('axv'),
        bA=document.getElementById('barA'),bB=document.getElementById('barB'),
        sum=document.getElementById('axsum');
  function upd(){
    const z=+ax.value;axv.textContent=z;
    const hA=Math.max(2,(A-z)/(100-z)*H),hB=(B-z)/(100-z)*H;
    bA.style.height=hA+'px';bB.style.height=hB+'px';
    const ratio=(B-z)/Math.max(1e-9,(A-z));
    sum.innerHTML= z===0
      ? 'Axis at 0: B\\u2019s bar is 1.04\\u00d7 A\\u2019s \\u2014 exactly what the data says.'
      : 'Axis at '+z+': B\\u2019s bar is now <b>'+(ratio>50?'\\u221e':ratio.toFixed(1))+
        '\\u00d7</b> A\\u2019s on screen. Same two numbers. The picture is doing the lying.';
  }
  ax.addEventListener('input',upd);upd();
})();
'''))

# ================================================================ DS 4
LESSONS.append(dict(sprint=DS, n=4, nb='ds4-capstone',
 title='A real analysis, start to finding',
 lede='The capstone week. Question, table, moves, chart, and a finding you can '
      'defend — the full loop, on data of your own.',
 watch_h2='The loop: question to finding',
 watch_note='Every analysis is the same loop — and the finding must not outrun the data.',
 listen_line='What separates a finding from a vibe: the receipts, and the sentence '
      'that says what the data does not prove.',
 read_h2='The loop, and the overclaim',
 read_html='''
  <p>Everything you learned this month is one machine now. Every real analysis —
  in a newsroom, a lab, a company — runs the same loop:</p>
  <p><b>1. A question you actually care about.</b> Sharp beats grand: "which weekday
  does the shop sell the most?" beats "understand the shop".</p>
  <p><b>2. A table that could answer it.</b> Know what one row is before you touch
  anything else.</p>
  <p><b>3. The moves.</b> Filter to the rows that matter, group to fold them,
  sort to rank them. Count before and after every filter.</p>
  <p><b>4. A picture.</b> The chart type follows the question — compare, change,
  or relationship. Axis at zero unless you can defend otherwise. Labels and
  units, always.</p>
  <p><b>5. The finding — three sentences.</b> What I measured. What I found. What
  this does <i>not</i> prove. That third sentence is the professional one. Data
  from one month does not prove a law of nature; eight cities do not speak for
  every city; sales going up when it rains does not mean rain causes sales.</p>
  <p>The failure mode of week 4 is not broken code — it is the <b>overclaim</b>:
  a true computation dressed as a bigger truth than it earned. "Coastal cities
  average fewer people" is what your table said. "People prefer living inland"
  is a theory your table never tested. The gap between those two sentences is
  where data science either earns trust or loses it. Calibrate yourself:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Supported, or too far?</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Six claims, each with what the
    data actually showed. Sort them.</p>
    <div id="claims"></div>
    <p class="fignote" id="csum"></p>
  </div>
''',
 code_h2='The capstone notebook',
 code_intro='One month of sales from a small (fictional) Tirana shop — 120 rows.'
      ' The notebook walks the loop once with you, then hands you the wheel: your '
      'question, your moves, your chart, your three-sentence finding.',
 deeper_h2='Data of your own, if you want it',
 deeper_html='''
  <div class="gd"><b>Kaggle.</b>
  <a href="https://www.kaggle.com/datasets" target="_blank" rel="noopener">kaggle.com/datasets</a>
  — tens of thousands of real datasets: football, films, weather, prices.
  Downloadable as CSV, ready for read_csv.</div>
  <div class="gd"><b>Google Dataset Search.</b>
  <a href="https://datasetsearch.research.google.com" target="_blank" rel="noopener">datasetsearch.research.google.com</a>
  — a search engine that only finds datasets.</div>
  <div class="gd"><b>Stretch build.</b> Rerun the whole loop on a dataset you chose
  yourself. Same rules: sharp question, counted filters, honest chart, three
  sentences. This is exactly the shape of a portfolio piece.</div>
''',
 quiz=[
  ('The table shows ice-cream sales are higher on hot days. Which claim is supported?',
   [('Heat causes people to buy ice cream', 0),
    ('In this data, hotter days had higher sales', 1),
    ('Ice cream sales will be high next summer', 0)]),
  ('The third sentence of a finding says:',
   [('What the analyst personally believes', 0),
    ('What the data does not prove', 1),
    ('Which chart was used', 0)]),
  ('From week 3: your capstone bar chart should start its axis at…',
   [('the smallest value in the data', 0),
    ('zero, unless you can defend otherwise', 1),
    ('90', 0)]),
 ],
 build_h2='The capstone: your analysis',
 build_html='''
  <p>Run the full loop in the notebook: your question about the shop data (or a
  dataset you chose), your filters and groups with counts shown, one honest
  chart, and the three-sentence finding — measured, found, not-proven.</p>
  <p><b>Turn-in:</b> the notebook itself (File &rarr; Download .ipynb) plus a
  screenshot of the chart and finding. <b>This turn-in completes the sprint</b> —
  your teacher confirms all four weeks, and you are on the list for the live
  lecture with John Santerre.</p>
''',
 fig_js='''
(function(){
  const CS=[
 ["Data: in 120 rows, Saturday has the highest mean sales.","Claim: \\u201cSaturday is this shop\\u2019s best day this month.\\u201d",1,
  "Supported \\u2014 the claim stays inside the month and the shop the table describes."],
 ["Data: in 120 rows, Saturday has the highest mean sales.","Claim: \\u201cAlbanians shop most on Saturdays.\\u201d",0,
  "Too far \\u2014 one shop, one month, one country-sized conclusion. The table never tested Albania."],
 ["Data: coastal rows average 40% higher sales in July.","Claim: \\u201cIn this data, July sales were higher at coastal locations.\\u201d",1,
  "Supported \\u2014 measured, hedged to the data, no cause claimed."],
 ["Data: coastal rows average 40% higher sales in July.","Claim: \\u201cThe sea makes people spend more.\\u201d",0,
  "Too far \\u2014 tourists, holidays, and prices all differ by the coast. The data showed a difference, not a cause."],
 ["Data: 3 of 120 rows are missing the price column.","Claim: \\u201cAverages using price rest on 117 rows, not 120.\\u201d",1,
  "Supported \\u2014 and saying so is exactly the receipts habit."],
 ["Data: sales rose every week for four weeks.","Claim: \\u201cSales will keep rising next month.\\u201d",0,
  "Too far \\u2014 four points make a trend inside the data, not a promise about the future."]];
  const wrap=document.getElementById('claims');let done=0,score=0;
  CS.forEach(c=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14px"><span style="color:var(--ink2)">'+c[0]+'</span><br>'+c[1]+'</div>';
    ['Supported','Too far'].forEach((lbl,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=lbl;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=(j===0)===(c[2]===1);if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach(x=>x.disabled=true);
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Called it.</b> ':'<b>Reveal:</b> ')+c[3];
        card.appendChild(fb);
        if(done===CS.length)document.getElementById('csum').innerHTML=
          '<b>'+score+' of '+CS.length+'.</b> The gap between computed and claimed is where trust lives.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ SPACE 1
LESSONS.append(dict(sprint=SP, n=1, nb='space1-spectra',
 title='How we know, without going',
 lede='Nobody has been to Titan, yet we know what its air is made of. This week: '
      'how light carries fingerprints, and how to read them.',
 watch_h2='Light is the messenger',
 watch_note='Spread light into a rainbow and the dark lines name the gases it passed through.',
 listen_line='How a telescope on Earth can smell the air of a world a billion '
      'kilometers away.',
 read_h2='Fingerprints in the rainbow',
 read_html='''
  <p>Every fact in this sprint rests on one trick, so we start there. Pass light
  through a prism and it spreads into a rainbow — a <b>spectrum</b>, from violet
  to red and beyond into infrared light your eye cannot see. Now the trick: when
  light passes through a gas, the gas steals specific colors. <b>Each kind of
  molecule steals its own exact set</b> — methane takes one pattern of slices,
  water vapor another, carbon dioxide a third. The stolen colors show up as dark
  lines in the spectrum, and the pattern of lines is as distinctive as a
  fingerprint.</p>
  <p>So the recipe for reading a distant world's air is: catch its light, spread
  it into a spectrum, and match the dark-line fingerprints against gases we
  measure in laboratories here on Earth. No travel required. This is
  <b>spectroscopy</b>, and it is how astronomers knew Titan's atmosphere held
  methane in 1944 — from a telescope on Earth, decades before any spacecraft went
  to look. It is how the James Webb Space Telescope reads the air of planets
  around <i>other stars</i> today.</p>
  <p>Much of the action is in the <b>infrared</b> — heat-light. Molecules like
  methane absorb strongly there, which is why planetary spacecraft carry infrared
  spectrometers. The instrument Dr. Nixon works on, Cassini's CIRS, was exactly
  this: an infrared spectrometer that read temperatures and chemistry through
  Titan's haze for thirteen years.</p>
  <p>One more idea: light takes time. From the Sun to Earth, about 8 minutes;
  from Saturn to Earth, over an hour. Every telescope is a time machine looking
  at a slightly earlier universe — and every command sent to a spacecraft at
  Saturn takes that same hour-plus to arrive, which will matter next week.</p>
  <p>Now read three fingerprints yourself:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Match the fingerprint</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Three mystery worlds, their
    spectra below — dark lines where a gas stole light. The reference cards show
    each gas's pattern. Name the gas in each world's air.</p>
    <div id="refs" style="display:flex;gap:14px;flex-wrap:wrap;margin-bottom:12px"></div>
    <div id="worlds"></div>
    <p class="fignote" id="ssum"></p>
  </div>
''',
 code_h2='Plot a spectrum, find the thief',
 code_intro='The notebook builds a simple spectrum with code — brightness across '
      'wavelength — drops a gas\u2019s absorption dips into it, and has you locate '
      'them by eye and then by code (where is the minimum?).',
 deeper_h2='Farther down the light, if you want it',
 deeper_html='''
  <div class="gd"><b>NASA's solar system portal.</b>
  <a href="https://science.nasa.gov/solar-system/" target="_blank" rel="noopener">science.nasa.gov/solar-system</a>
  — every planet and major moon, with the current state of knowledge.</div>
  <div class="gd"><b>The Webb telescope.</b>
  <a href="https://webbtelescope.org" target="_blank" rel="noopener">webbtelescope.org</a>
  — the observatory doing this lesson's trick on worlds around other stars. In
  2022 it read carbon dioxide in the air of exoplanet WASP-39 b, hundreds of
  light-years away — same fingerprint method you just used.</div>
  <div class="gd"><b>Stretch.</b> Look up which gases Webb has reported in an
  exoplanet atmosphere so far. For each: is it a gas you met in this lesson?</div>
''',
 quiz=[
  ('How did astronomers know Titan\u2019s air held methane before any spacecraft went?',
   [('A probe returned an air sample', 0),
    ('Methane\u2019s fingerprint appeared in Titan\u2019s spectrum from Earth-based telescopes', 1),
    ('They guessed from its orange color', 0)]),
  ('Why do planetary spacecraft carry infrared spectrometers?',
   [('Infrared travels faster than visible light', 0),
    ('Molecules like methane absorb strongly in the infrared — the fingerprints are there', 1),
    ('Cameras don\u2019t work in space', 0)]),
  ('Light from Saturn takes over an hour to reach Earth. So a telescope pointed at Saturn sees…',
   [('Saturn as it was over an hour ago', 1),
    ('Saturn exactly as it is now', 0),
    ('nothing — it\u2019s too far', 0)]),
 ],
 build_h2='Explain the trick to a younger student',
 build_html='''
  <p>Write five to eight sentences, in your own words, explaining to a younger
  student how we can know what a faraway world's air is made of without going
  there. It must include: what a spectrum is, what the dark lines are, and one
  real example from this lesson. No copying — the test is whether it sounds like
  you.</p>
  <p><b>Turn-in:</b> the paragraph, to your teacher.</p>
''',
 fig_js='''
(function(){
  const GAS={methane:[2,5,9],water:[1,4,10],co2:[3,7,11]};
  const NAME={methane:'Methane',water:'Water vapor',co2:'Carbon dioxide'};
  function strip(lines,w){
    const seg=[];for(let i=0;i<13;i++){
      const dark=lines.includes(i);
      seg.push('<span style="display:inline-block;width:'+(w||16)+'px;height:26px;background:'+
        (dark?'#1A1414':'linear-gradient(90deg,hsl('+(260-i*20)+',75%,55%),hsl('+(260-(i+1)*20)+',75%,55%))')+'"></span>')}
    return '<span style="font-size:0;border:1px solid var(--hair);border-radius:4px;overflow:hidden;display:inline-block">'+seg.join('')+'</span>';
  }
  const refs=document.getElementById('refs');
  Object.keys(GAS).forEach(g=>{
    const d=document.createElement('div');
    d.innerHTML='<div style="font-size:13px;font-weight:700">'+NAME[g]+'</div>'+strip(GAS[g],12);
    refs.appendChild(d);});
  const WORLDS=[['World A',GAS.methane,'methane','Methane \\u2014 the same three slices are missing. This is Titan\\u2019s story.'],
                ['World B',GAS.co2,'co2','Carbon dioxide \\u2014 the pattern matches slice for slice. Venus and Mars are CO2 worlds.'],
                ['World C',GAS.water,'water','Water vapor \\u2014 the fingerprint every astronomer hopes to find.']];
  const wrap=document.getElementById('worlds');let done=0,score=0;
  WORLDS.forEach(w=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14px"><b>'+w[0]+'</b><br>'+strip(w[1])+'</div>';
    Object.keys(GAS).forEach(g=>{
      const b=document.createElement('button');b.className='choice';b.textContent=NAME[g];
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=g===w[2];if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach(x=>{x.disabled=true;
          if(x.textContent===NAME[w[2]])x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Matched.</b> ':'<b>Reveal:</b> ')+w[3];
        card.appendChild(fb);
        if(done===WORLDS.length)document.getElementById('ssum').innerHTML=
          '<b>'+score+' of '+WORLDS.length+'.</b> You just did spectroscopy \\u2014 the founding trick of planetary science.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ SPACE 2
LESSONS.append(dict(sprint=SP, n=2, nb='space2-missions',
 title='Getting there — missions and instruments',
 lede='Four ways to visit a world, and the senses a spacecraft brings. This week '
      'you design a mission on paper — target, question, craft, instruments.',
 watch_h2='Flyby, orbit, land',
 watch_note='Each mission type buys more knowledge and costs more difficulty.',
 listen_line='Why every mission is a trade — speed against depth, distance against '
      'time — and why the answer starts with the question.',
 read_h2='The ladder, the senses, and the delay',
 read_html='''
  <p>Once telescopes have told you a world is interesting, there are four ways to
  go look closer — a ladder, each rung harder and more revealing than the last.</p>
  <p><b>Flyby:</b> race past once, cameras blazing. Days of data, no second
  chances. Voyager 2's flybys are still our only close look at Uranus and
  Neptune.</p>
  <p><b>Orbiter:</b> stay, and circle for years. Cassini orbited Saturn from 2004
  to 2017 and flew past Titan more than a hundred times, building maps and
  watching seasons change.</p>
  <p><b>Lander or rover:</b> touch the ground. The Huygens probe rode with Cassini
  and parachuted onto Titan in 2005 — still the most distant landing ever made.</p>
  <p><b>Sample return:</b> bring pieces home to Earth's labs — the hardest and
  rarest rung.</p>
  <p>Whatever the rung, the spacecraft carries <b>instruments — its senses</b>.
  A camera is eyes. A spectrometer is the nose from last week, reading
  fingerprints in light — CIRS on Cassini was an infrared one. Radar is touch at
  a distance: it beams radio waves through clouds and reads the echo, which is
  how Cassini mapped lakes on Titan through haze no camera could pierce. The
  choice of instruments <i>is</i> the choice of what the mission can learn.</p>
  <p>And everything happens on a delay. Radio commands travel at light speed, and
  Saturn is over a light-hour away — so nobody "drives" a Titan probe with a
  joystick. By the time you saw a problem, it happened more than an hour ago.
  Distant spacecraft must be told their plans in advance and trusted to execute
  alone. Remember that when a landing succeeds: the whole thing was over before
  Earth heard it began.</p>
  <p>Now run the trade yourself:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Design the mission</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Pick a question, then choose the
    craft and the instrument that could answer it. The figure judges the fit.</p>
    <div id="mq" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px"></div>
    <div id="mc" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px"></div>
    <div id="mi" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px"></div>
    <p class="fignote" id="msum">Choose a question to begin.</p>
  </div>
''',
 code_h2='Compute the delay yourself',
 code_intro='The notebook computes light-travel time to every planet from real '
      'average distances, plots the delays, and asks: at which worlds could you '
      'joystick a rover from Earth, honestly?',
 deeper_h2='More missions, if you want them',
 deeper_html='''
  <div class="gd"><b>NASA Eyes.</b>
  <a href="https://eyes.nasa.gov" target="_blank" rel="noopener">eyes.nasa.gov</a>
  — a live 3D map of the solar system and every active spacecraft in it. Find out
  what is flying right now.</div>
  <div class="gd"><b>Cassini's legacy.</b>
  <a href="https://science.nasa.gov/mission/cassini/" target="_blank" rel="noopener">science.nasa.gov/mission/cassini</a>
  — thirteen years at Saturn, and the mission Dr. Nixon worked on. The Grand
  Finale section is worth ten minutes of anyone's life.</div>
  <div class="gd"><b>Huygens' descent.</b>
  <a href="https://www.esa.int/Science_Exploration/Space_Science/Cassini-Huygens" target="_blank" rel="noopener">esa.int — Cassini-Huygens</a>
  — the European probe that landed on Titan in 2005, with the descent imagery.</div>
  <div class="gd"><b>Stretch.</b> Using the notebook's delay numbers: Mars rovers
  drive themselves between commands. Write three sentences on why, citing the
  delay you computed.</div>
''',
 quiz=[
  ('Cassini mapped Titan\u2019s lakes through its haze. Which sense did that?',
   [('A sharper camera', 0),
    ('Radar — radio waves pass through the haze and echo back', 1),
    ('The infrared spectrometer', 0)]),
  ('Why can\u2019t anyone joystick a probe at Saturn?',
   [('The signal is too weak', 0),
    ('Commands take over an hour each way — the event is over before you see it', 1),
    ('Spacecraft don\u2019t accept commands after launch', 0)]),
  ('From week 1: a spectrometer aboard a spacecraft is for…',
   [('measuring the craft\u2019s speed', 0),
    ('reading gas fingerprints in light', 1),
    ('navigation', 0)]),
 ],
 build_h2='Your mission card',
 build_html='''
  <p>Choose any world in the solar system except Earth. Write a mission card:
  the world, one sharp question about it, the rung of the ladder you would use
  (flyby, orbiter, lander, sample return), the two instruments you would carry
  and what each answers, and the one risk that worries you most. One page,
  any format.</p>
  <p><b>Turn-in:</b> the mission card, to your teacher.</p>
''',
 fig_js='''
(function(){
  const QS=[
   ['What is under Europa\\u2019s ice?','europa'],
   ['Does Titan\\u2019s rain carve its rivers?','titan'],
   ['What is Neptune\\u2019s deep atmosphere made of?','neptune']];
  const CRAFT=['Flyby','Orbiter','Lander'];
  const INST=['Camera','Spectrometer','Radar'];
  const VERDICT={
   europa:{best:['Orbiter','Radar'],
    why:'An orbiter with ice-penetrating radar \\u2014 radar is touch through the crust; a flyby gets one glance and a camera sees only the surface.'},
   titan:{best:['Orbiter','Radar'],
    why:'Orbiter + radar maps the rivers through the haze across seasons; a camera alone cannot pierce it. (A lander sees one riverbank \\u2014 real missions pair them.)'},
   neptune:{best:['Orbiter','Spectrometer'],
    why:'A spectrometer reads the gas fingerprints; staying in orbit watches the atmosphere move. Only a flyby has ever visited \\u2014 which is why we know so little.'}};
  let q=null,c=null,inst=null;
  const mq=document.getElementById('mq'),mc=document.getElementById('mc'),
        mi=document.getElementById('mi'),sum=document.getElementById('msum');
  function btnrow(el,items,cb){el.innerHTML='';items.forEach(t=>{
    const b=document.createElement('button');b.className='choice';b.textContent=Array.isArray(t)?t[0]:t;
    b.addEventListener('click',()=>{[...el.children].forEach(x=>x.classList.remove('right'));
      b.classList.add('right');cb(Array.isArray(t)?t[1]:t);judge()});el.appendChild(b);});}
  function judge(){
    if(!q){sum.textContent='Choose a question to begin.';return}
    if(!c||!inst){sum.textContent='Now pick a craft and an instrument.';return}
    const v=VERDICT[q];const hit=(c===v.best[0])+(inst===v.best[1]);
    sum.innerHTML=(hit===2?'<b>Strong design.</b> ':hit===1?'<b>Half right.</b> ':'<b>Mismatch.</b> ')+v.why;}
  btnrow(mq,QS,v=>{q=v});btnrow(mc,CRAFT,v=>{c=v});btnrow(mi,INST,v=>{inst=v});
})();
'''))

# ================================================================ SPACE 3
LESSONS.append(dict(sprint=SP, n=3, nb='space3-titan',
 title='Titan — the world with weather',
 lede='Saturn\u2019s largest moon has thick air, orange haze, methane rain, and '
      'seas you could sail. This is Dr. Nixon\u2019s world — meet it properly.',
 watch_h2='The moon that behaves like a planet',
 watch_note='Thick atmosphere, rain, rivers, lakes — with methane playing the role of water.',
 listen_line='A world where it rains at minus 179 degrees, and why chemists look '
      'at Titan and see the early Earth.',
 read_h2='Weather, with the water swapped out',
 read_html='''
  <p>Titan is the only moon in the solar system with a substantial atmosphere —
  mostly nitrogen, like Earth's, and thick: surface pressure is about one and a
  half times ours. Stand on Titan and the air presses on you a little harder than
  at sea level here. Everything else is stranger.</p>
  <p>It is cold in a way that rearranges chemistry: about <b>&minus;179&nbsp;&deg;C
  (94 kelvin)</b>. At that temperature water is not a liquid, a cloud, or a rain —
  it is rock. Titan's mountains and sands are built on water ice frozen harder
  than granite. And with water locked up, another substance takes over its job:
  <b>methane</b>. On Titan, methane forms clouds, falls as rain, carves rivers,
  and pools into lakes and seas — the largest, Kraken Mare, is bigger than the
  Caspian Sea. Titan runs a full weather cycle, with seasons, exactly like
  Earth's water cycle with the molecule swapped.</p>
  <p>The orange color is haze: sunlight breaks methane apart high in the
  atmosphere and the fragments reassemble into heavier carbon molecules — organic
  chemistry running planet-wide, all the time. That is why chemists care so much:
  Titan is a natural laboratory for the kind of carbon chemistry that preceded
  life on the early Earth, kept in a freezer for four billion years.</p>
  <p>Reading a world through opaque haze took the instruments from last week:
  radar mapped the seas, and the infrared spectrometer <b>CIRS</b> — Dr. Nixon
  was its deputy principal investigator — read temperatures and chemistry
  through the murk for the length of the Cassini mission. Huygens landed in 2005
  and photographed rounded pebbles of water ice by a dry riverbed. Next:
  <b>Dragonfly</b>, a NASA rotorcraft now in development, will fly from site to
  site in that thick air — a drone on a moon of Saturn, with its cameras aimed
  at exactly this chemistry.</p>
  <p>Hold the two worlds side by side:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Earth vs Titan</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Pick a property; compare the pair.</p>
    <div id="props" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px"></div>
    <div id="pair" style="display:grid;grid-template-columns:1fr 1fr;gap:12px"></div>
    <p class="fignote" id="psum"></p>
  </div>
''',
 code_h2='Titan, by the numbers',
 code_intro='The notebook does honest arithmetic on Titan: your weight in its '
      'gravity, how much harder the air presses, how long Cassini\u2019s radio '
      'took to report a Titan flyby, and a temperature plot that shows why '
      'methane can rain there and water cannot.',
 deeper_h2='Deeper into the haze, if you want it',
 deeper_html='''
  <div class="gd"><b>NASA's Titan page.</b>
  <a href="https://science.nasa.gov/saturn/moons/titan/" target="_blank" rel="noopener">science.nasa.gov/saturn/moons/titan</a>
  — the current state of knowledge, with imagery from Cassini and Huygens.</div>
  <div class="gd"><b>Dragonfly.</b>
  <a href="https://dragonfly.jhuapl.edu" target="_blank" rel="noopener">dragonfly.jhuapl.edu</a>
  — the rotorcraft mission in development. Look at where it will land and what it
  will carry.</div>
  <div class="gd"><b>Huygens' pictures.</b> Search the ESA Cassini-Huygens pages
  from last week for the surface images — rounded ice pebbles by a dry channel,
  photographed 1.2 billion kilometers from home.</div>
  <div class="gd"><b>Stretch.</b> Make a two-column table: the water cycle on
  Earth vs the methane cycle on Titan — evaporation, clouds, rain, rivers, seas.
  Which row is missing on Titan? (Hint: think about what life does to Earth's
  cycle.)</div>
''',
 quiz=[
  ('What plays the role of water in Titan\u2019s weather?',
   [('Liquid nitrogen', 0), ('Methane', 1), ('Ammonia', 0)]),
  ('At Titan\u2019s &minus;179 &deg;C, water is…',
   [('vapor in the clouds', 0),
    ('rock-hard ice — the mountains are built of it', 1),
    ('a salty ocean on the surface', 0)]),
  ('From week 2: how did Cassini see Titan\u2019s seas through the haze?',
   [('A more powerful camera', 0), ('Radar echoes', 1), ('It waited for clear weather', 0)]),
 ],
 build_h2='A postcard from Titan',
 build_html='''
  <p>Write a postcard home from a research station on Titan — six to ten
  sentences describing a day there. The rule that makes it science and not
  fiction: <b>every claim must trace to a number or fact from this lesson</b>
  (the pressure, the temperature, the gravity from the notebook, what the rain
  is, what the ground is). Voice is yours; facts are Titan's.</p>
  <p><b>Turn-in:</b> the postcard, to your teacher.</p>
''',
 fig_js='''
(function(){
  const P={
   'Air':['Nitrogen-oxygen, 1 atmosphere of pressure','Mostly nitrogen, ~1.5&times; Earth\\u2019s surface pressure \\u2014 thicker air than home'],
   'Temperature':['Global average about +15 &deg;C','About &minus;179 &deg;C (94 K) \\u2014 cold enough that water is a rock'],
   'Rain':['Water, from water clouds','Methane, from methane clouds \\u2014 a full weather cycle with the molecule swapped'],
   'Lakes &amp; seas':['Water; largest is the Pacific','Liquid methane/ethane; Kraken Mare outsizes the Caspian Sea'],
   'The ground':['Rock and soil','Water ice frozen granite-hard, with dark organic sands'],
   'Sky color':['Blue \\u2014 scattered sunlight','Orange \\u2014 a global haze of carbon molecules made from broken methane']};
  const props=document.getElementById('props'),pair=document.getElementById('pair'),
        sum=document.getElementById('psum');
  function show(k){
    pair.innerHTML='<div class="gd"><b>Earth</b><br>'+P[k][0]+'</div>'+
                   '<div class="gd" style="border-left:3px solid var(--star)"><b>Titan</b><br>'+P[k][1]+'</div>';
    sum.innerHTML='Same physics, different ingredients \\u2014 that is why Titan teaches us about worlds in general.';}
  Object.keys(P).forEach((k,i)=>{const b=document.createElement('button');
    b.className='choice';b.innerHTML=k;
    b.addEventListener('click',()=>{[...props.children].forEach(x=>x.classList.remove('right'));
      b.classList.add('right');show(k)});
    props.appendChild(b);if(i===0){b.classList.add('right');show(k)}});
})();
'''))

# ================================================================ SPACE 4
LESSONS.append(dict(sprint=SP, n=4, nb='space4-transit',
 title='Find a planet in the data',
 lede='The capstone week. Thousands of planets have been found as tiny dips in '
      'starlight — this week you find one yourself, in data, with the skills '
      'from both sprints.',
 watch_h2='The transit trick',
 watch_note='A planet crossing its star steals a sliver of light — the dip repeats every orbit.',
 listen_line='How a 1% flicker, repeating on schedule, becomes a planet — and how '
      'big the planet is, straight from the depth of the dip.',
 read_h2='Dips, depth, and discipline',
 read_html='''
  <p>Point a telescope at a star and record its brightness, hour after hour. You
  get a table — time in one column, brightness in the next. Plot it and you have
  a <b>light curve</b>: a wobbly, noisy line. Most stars flicker a little.
  But if a planet's orbit happens to carry it <i>across</i> the star's face from
  our point of view, it blocks a sliver of light — and the curve shows a small,
  clean <b>dip</b>. Wait, and the dip returns, on a perfect schedule. That
  schedule is the planet's year.</p>
  <p>The dip's <b>depth tells you the planet's size</b>, with arithmetic you
  already own: the fraction of light blocked equals the fraction of the star's
  disk the planet covers. A dip of 1% means the planet's disk is 1% of the
  star's — and since disk area scales with radius squared, the planet's radius
  is the <b>square root</b> of the depth times the star's radius.
  &radic;0.01 = 0.1: a 1% dip is a planet one-tenth the star's radius. Roughly
  Jupiter, if the star is like the Sun. This is how the Kepler space telescope
  found thousands of planets: not pictures — tables, dips, and square roots.</p>
  <p>Now the discipline, because week 4 of the data sprint applies here too. Not
  every dip is a planet. Starspots — dark patches on the star itself — cause
  dips that <i>drift</i> instead of repeating on schedule. A second star grazing
  the first causes deep, V-shaped dips. The professionals' rule is the one you
  already learned: <b>say what the data shows, and what it does not prove.</b> A
  repeating, flat-bottomed dip at a constant period is a planet <i>candidate</i>
  until a second method confirms it. Thousands of candidates died on follow-up;
  the ones that survived are the catalog.</p>
  <p>Find yours:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The transit finder</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Thirty days of brightness for one
    star. Drag the threshold down until you catch the dips — but not the noise.</p>
    <canvas id="lc" width="820" height="240" style="width:100%;max-width:820px;border:1px solid var(--hair);border-radius:6px;background:#fff"></canvas><br>
    <label style="font-size:14px">Threshold:
      <input type="range" id="th" min="900" max="1000" value="1000" style="width:min(300px,60vw);vertical-align:middle"></label>
    <p class="fignote" id="lcsum">Everything above the line is treated as normal flicker; every excursion below is a detection.</p>
  </div>
''',
 code_h2='The capstone notebook',
 code_intro='A month of (synthetic, realistic) light-curve data, embedded in the '
      'notebook. You plot it, find the dips, measure the period and the depth, '
      'and compute the planet\u2019s size with the square-root rule. Then the '
      'finding: three sentences, exactly like the data sprint\u2019s.',
 deeper_h2='Real starlight, if you want it',
 deeper_html='''
  <div class="gd"><b>The NASA Exoplanet Archive.</b>
  <a href="https://exoplanetarchive.ipac.caltech.edu" target="_blank" rel="noopener">exoplanetarchive.ipac.caltech.edu</a>
  — the official catalog of every confirmed exoplanet, with the actual measured
  depths and periods. Your notebook's numbers live in these columns for real
  worlds.</div>
  <div class="gd"><b>Exoplanet Watch.</b>
  <a href="https://science.nasa.gov/exoplanets/exoplanet-watch/" target="_blank" rel="noopener">NASA Exoplanet Watch</a>
  — a NASA citizen-science project where non-professionals help track transit
  timings for real targets.</div>
  <div class="gd"><b>Planet Hunters TESS.</b>
  <a href="https://www.zooniverse.org/projects/nora-dot-eisner/planet-hunters-tess" target="_blank" rel="noopener">zooniverse.org — Planet Hunters TESS</a>
  — classify real light curves from NASA's TESS telescope by eye. People doing
  exactly what you did in Figure 1 have found planets the algorithms missed.</div>
  <div class="gd"><b>Stretch.</b> Spend twenty minutes on Planet Hunters TESS
  classifying real curves. Bring your strangest one to the lecture.</div>
''',
 quiz=[
  ('A light curve shows a 1% dip repeating every 12 days. The 12 days is…',
   [('the planet\u2019s size', 0), ('the planet\u2019s year — its orbital period', 1),
    ('the star\u2019s age', 0)]),
  ('Depth 1%, star like the Sun. The planet\u2019s radius is about…',
   [('1% of the star\u2019s', 0),
    ('10% of the star\u2019s — the square root of the depth', 1),
    ('half the star\u2019s', 0)]),
  ('From the data sprint: your transit finding should include a third sentence saying…',
   [('how exciting the discovery is', 0),
    ('what the data does not prove — candidate, not confirmed', 1),
    ('which telescope you would name after yourself', 0)]),
 ],
 build_h2='The capstone: your detection',
 build_html='''
  <p>In the notebook: plot the light curve, find the dips, measure the period and
  depth, compute the size ratio with the square-root rule, and write the
  three-sentence finding — what you measured, what you found, what it does not
  prove.</p>
  <p><b>Turn-in:</b> the notebook (File &rarr; Download .ipynb) plus a screenshot
  of your plot and finding. <b>This turn-in completes the sprint</b> — your
  teacher confirms all four weeks, and you are on the list for the live lecture
  with Dr. Nixon.</p>
''',
 fig_js='''
(function(){
  const N=600,BASE=1000,DEPTH=12,PERIOD=200,WIDTH=14;
  function noise(i){const x=Math.sin(i*12.9898)*43758.5453;return (x-Math.floor(x)-0.5)*6}
  const data=[];
  for(let i=0;i<N;i++){
    let v=BASE+noise(i);
    for(const c of [80,280,480]) if(Math.abs(i-c)<WIDTH/2) v-=DEPTH;
    data.push(v);}
  const cv=document.getElementById('lc'),cx=cv.getContext('2d'),
        th=document.getElementById('th'),sum=document.getElementById('lcsum');
  function draw(){
    const T=+th.value;
    cx.clearRect(0,0,820,240);
    cx.strokeStyle='#E3E0D8';
    for(let g=960;g<=1000;g+=10){const y=240-(g-940)*3.4;
      cx.beginPath();cx.moveTo(0,y);cx.lineTo(820,y);cx.stroke();}
    let hits=[],inDip=false;
    cx.beginPath();
    data.forEach((v,i)=>{
      const x=i/N*820,y=240-(v-940)*3.4;
      i?cx.lineTo(x,y):cx.moveTo(x,y);});
    cx.strokeStyle='#7E1B14';cx.lineWidth=1.4;cx.stroke();cx.lineWidth=1;
    data.forEach((v,i)=>{
      if(v<T&&!inDip){hits.push(i);inDip=true}
      if(v>=T)inDip=false;});
    const ty=240-(T-940)*3.4;
    cx.strokeStyle='#D8291F';cx.setLineDash([6,4]);
    cx.beginPath();cx.moveTo(0,ty);cx.lineTo(820,ty);cx.stroke();cx.setLineDash([]);
    data.forEach((v,i)=>{if(v<T){const x=i/N*820,y=240-(v-940)*3.4;
      cx.fillStyle='#D8291F';cx.fillRect(x-1.2,y-1.2,2.4,2.4);}});
    if(hits.length===0)sum.innerHTML='Threshold at '+T+': nothing detected. Bring it down \\u2014 carefully.';
    else if(hits.length===3){
      const depthPct=(DEPTH/BASE*100).toFixed(1),ratio=Math.sqrt(DEPTH/BASE);
      sum.innerHTML='<b>Three dips, evenly spaced \\u2014 a candidate.</b> Depth \\u2248 '+depthPct+
        '%, so radius \\u2248 \\u221a0.0'+Math.round(DEPTH/BASE*1000)+' \\u2248 '+(ratio*100).toFixed(0)+
        '% of the star\\u2019s. Period: the spacing of the dips. Say it like week 4: found, measured, not yet confirmed.';}
    else if(hits.length<3)sum.innerHTML='Threshold at '+T+': '+hits.length+' of the dips caught. A bit lower.';
    else sum.innerHTML='Threshold at '+T+': '+hits.length+' detections \\u2014 you are now catching noise as planets. Back up.';
  }
  th.addEventListener('input',draw);draw();
})();
'''))


PRACTICE_TPL = '''<section class="seg" data-seg="practice">
  <div class="stype">Practice</div>
  <h2>%s</h2>
  <p>%s</p>
%s
  <p style="font-size:13.5px;color:var(--ink2)">Attempt each one before revealing —
  the struggle is the mechanism, not a malfunction. When you have worked through
  them all, mark the segment complete.</p>
  <button class="mark" data-for="practice">Mark complete</button>
</section>

'''


def practice_html(p):
    cards = []
    for i, (q, a) in enumerate(p['items'], 1):
        cards.append('  <div class="ex"><div class="exnum">EXERCISE %d</div>\n'
                     '  <div class="exq">%s</div>\n'
                     '  <button class="exbtn">Show the answer</button>\n'
                     '  <div class="exans">%s</div></div>' % (i, q, a))
    return PRACTICE_TPL % (p['h2'], p['intro'], '\n'.join(cards))


def fill(l):
    s, page, key = l['sprint']
    n = l['n']
    prev = ('<a href="%s">&larr; Sprint page</a>' % page) if n == 1 else \
           ('<a href="lesson-%s-%d.html">&larr; Week %d</a>' % (key, n - 1, n - 1))
    nxt = ('<a href="lesson-%s-%d.html">Week %d &rarr;</a>' % (key, n + 1, n + 1)) if n < 4 else \
          ('<a href="%s">Back to the sprint &rarr;</a>' % page)
    segs = ['watch', 'listen', 'read'] + (['practice'] if 'practice' in l else []) + \
           ['code', 'deeper', 'check', 'build', 'done']
    watch2 = ''
    if 'watch2' in l:
        w2h, w2src = l['watch2']
        watch2 = ('  <p style="margin:16px 0 4px;font-weight:600">%s</p>\n'
                  '  <video controls preload="metadata" style="width:100%%;border-radius:8px;background:#000"\n'
                  '    src="video/%s"></video>\n' % (w2h, w2src))
    h = TPL
    h = h.replace('@@NSEG@@', str(len(segs)))
    h = h.replace('@@SEGS_JS@@', repr(segs).replace(' ', ''))
    h = h.replace('@@PRACTICE@@', practice_html(l['practice']) if 'practice' in l else '')
    h = h.replace('@@WATCH2@@', watch2)
    for tok, val in [
        ('@@TITLE@@', l['title']), ('@@SPRINT@@', s), ('@@SPRINTPAGE@@', page),
        ('@@N@@', str(n)), ('@@KEY@@', key), ('@@LEDE@@', l['lede']),
        ('@@WATCH_H2@@', l['watch_h2']), ('@@WATCH_NOTE@@', l['watch_note']),
        ('@@LISTEN_LINE@@', l['listen_line']), ('@@READ_H2@@', l['read_h2']),
        ('@@READ_HTML@@', l['read_html']), ('@@CODE_H2@@', l['code_h2']),
        ('@@CODE_INTRO@@', l['code_intro']), ('@@NB@@', l['nb']),
        ('@@DEEPER_H2@@', l['deeper_h2']), ('@@DEEPER_HTML@@', l['deeper_html']),
        ('@@QUIZ_HTML@@', quiz(l['quiz'])), ('@@BUILD_H2@@', l['build_h2']),
        ('@@BUILD_HTML@@', l['build_html']), ('@@FIG_JS@@', l['fig_js']),
        ('@@PREV@@', prev), ('@@NEXT@@', nxt)]:
        h = h.replace(tok, val)
    return h


def main():
    for l in LESSONS:
        key = l['sprint'][2]
        path = os.path.join(SITE, 'lesson-%s-%d.html' % (key, l['n']))
        with open(path, 'w') as f:
            f.write(fill(l))
        print(path)


if __name__ == '__main__':
    main()
