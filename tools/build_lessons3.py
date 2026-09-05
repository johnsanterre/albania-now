#!/usr/bin/env python3
"""Albania Now — sprints 6 & 7 (John's directive 2026-09-04):
Learning to Read Python (key 'read') and Learning to Learn from External
Resources (key 'sources', no-code try-variant). Launch standard; both join
the 20h deepening queue. Run: python3 build_lessons3.py"""
import os
from build_lessons import quiz, fill, SITE  # noqa: F401

RD = ('Learning to Read Python', 'sprint-reading.html', 'read')
SRC = ('Learning to Learn from External Resources', 'sprint-sources.html', 'sources')

LESSONS = []

# ================================================================ READ 1
LESSONS.append(dict(sprint=RD, n=1, nb='read1-trace-drills',
 title='Trace like the machine',
 lede='Programmers read far more code than they write — and reading code means '
      'running it in your head. This week you build the tracing habit on small '
      'programs, and prove your predictions against the machine.',
 watch_h2='Reading is executing, slowly',
 watch_note='A program is a story the machine acts out — tracing is reading it the way the machine will.',
 listen_line='Why the best code readers move their finger down the lines like a '
      'first-grader — and why that is the advanced technique.',
 read_h2='The finger on the line',
 read_html='''
  <p>Here is a professional secret: programmers spend most of their time
  <b>reading</b> code — their own from last month, their teammates', and, more
  every year, code an AI wrote in seconds. The AI era did not shrink that; it
  multiplied it. When an assistant hands you thirty lines, your job is no
  longer typing — it is <b>judging</b>, and you cannot judge what you cannot
  read.</p>
  <p>Reading code is not like reading prose. Prose you skim; code you
  <b>trace</b> — you become the machine and act the story out, line by line,
  keeping the whiteboard of variables in your head (or better, on paper). The
  technique looks childish and is not: put a finger on line one, say what it
  does to the whiteboard, move down. Every professional debugging session is
  this exact motion, done fast.</p>
  <p>Three tracing rules from day one. <b>One line at a time</b> — the eye
  wants to jump to the interesting line; the bug is usually in a boring one.
  <b>Track every store</b> — when a variable is reassigned, the old value is
  gone; your paper whiteboard should show the crossing-out. <b>Predict before
  the last line</b> — commit to what the program prints before you reach the
  print. A prediction you didn't commit to teaches nothing, because it
  quietly becomes "what I meant."</p>
  <p>Trace these with your finger, then check yourself:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Finger on the line</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Three programs. Trace each on
    paper, commit, then answer.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='The prediction notebook',
 code_intro='Ten small programs. For each: a cell where you STORE your '
      'prediction in a variable, then the program runs, then a CHECK compares '
      'your prediction to reality. The score is honest because you committed '
      'first.',
 deeper_h2='More tracing, if you want it',
 deeper_html='''
  <div class="gd"><b>Python Tutor.</b>
  <a href="https://pythontutor.com" target="_blank" rel="noopener">pythontutor.com</a>
  — paste any small program and it draws the whiteboard for you, step by step.
  Use it to CHECK your hand traces, never to replace them.</div>
  <div class="gd"><b>Stretch.</b> Take a program from this week's notebook,
  trace it on paper including the whiteboard at every line, photograph the
  paper, and compare against Python Tutor's diagram. Where did your whiteboard
  diverge?</div>''',
 quiz=[
  ('Why do professionals trace with a finger (or cursor) on the line?',
   [('Habit from childhood', 0),
    ('The eye jumps to interesting lines; the bug is usually in a boring one', 1),
    ('It makes reading look busy', 0)]),
  ('A prediction only teaches you something if…',
   [('it turns out correct', 0),
    ('you committed to it BEFORE running — otherwise it becomes "what I meant"', 1),
    ('you share it with the class', 0)]),
  ('In the AI era, reading code matters MORE because…',
   [('AIs write code you must judge before trusting', 1),
    ('typing speed no longer matters at all', 0),
    ('code has gotten shorter', 0)]),
 ],
 build_h2='The traced program',
 build_html='''
  <p>Pick the longest program in this week's notebook. Trace it on paper: every
  line, the whiteboard after each store, the final output — BEFORE running it.
  Then run it. Your turn-in is the photograph of your paper trace next to a
  screenshot of the actual output, plus one sentence: where (if anywhere) your
  trace went wrong, and why.</p>
  <p><b>Turn-in:</b> photo + screenshot + the sentence.</p>
''',
 fig_js='''
(function(){
  const QS=[
 {q:'a = 3\\nb = a + 2\\na = 10\\nprint(a + b)',a:1,opts:['8','15','20'],
  why:'b took a snapshot: 5. Reassigning a later does not touch b. 10 + 5 = 15.'},
 {q:'x = 1\\nx = x + x\\nx = x + x\\nprint(x)',a:2,opts:['2','3','4'],
  why:'1 doubles to 2, doubles to 4. Trace every store — the second line changes what the third line reads.'},
 {q:'emri = "Blerta"\\ngjatesia = len(emri)\\nprint(emri + " " + str(gjatesia))',a:0,
  opts:['Blerta 6','Blerta gjatesia','an error'],
  why:'len counts the letters of the text: 6. str bridges the number, and the glue works. Blerta 6.'}];
  const wrap=document.getElementById('q1');let done=0,score=0;
  QS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-family:ui-monospace,Menlo,monospace;font-size:14px;white-space:pre-wrap"></div>';
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
        if(done===QS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+QS.length+'.</b> The finger is the debugger you always carry.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ READ 2
LESSONS.append(dict(sprint=RD, n=2, nb='read2-shape-drills',
 title='Read the shapes',
 lede='Loops and forks have visual signatures. This week you learn to see WHAT '
      'a block of code is before reading a single word of it — then verify the '
      'details by tracing.',
 watch_h2='Code has anatomy',
 watch_note='Indentation is structure: a loop is a repeated block, an if is a fork in the road.',
 listen_line='How experienced readers see "a loop that accumulates" in half a '
      'second — and what they check next.',
 read_h2='Shapes first, words second',
 read_html='''
  <p>Show an experienced programmer twenty lines and within seconds they will
  say something like "a loop that builds a total, with a guard for the empty
  case." They did not read every word — they read the <b>shape</b>. Python
  makes shapes visible with indentation: everything indented under a
  <span style="font-family:ui-monospace,Menlo,monospace">for</span> happens
  once per item; everything under an
  <span style="font-family:ui-monospace,Menlo,monospace">if</span> happens only
  when the test is true. The indentation IS the structure — which is why a
  wrongly indented line is not ugly, it is a different program.</p>
  <p>Two shapes cover most beginner code. <b>The accumulator:</b> a variable
  starts empty or zero before a loop, gets added to inside it, and is used
  after. Spot that pattern and you know the loop's purpose before tracing a
  single pass. <b>The fork:</b> an if/else splits the road; the question to ask
  is not "what does each branch do" first, but <b>"what decides the
  branch?"</b> — read the test, then the branches.</p>
  <p>The reading order that follows: <b>shape &rarr; purpose &rarr; trace.</b>
  Name the shape, guess the purpose out loud, then trace two passes of the loop
  (never zero — the first pass and one more catches most misreadings). Only
  trace all passes when the first two disagree with your guess.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The loop unroller</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">One loop, unrolled pass by
    pass. Predict the total before each press.</p>
    <pre class="code">total = 0
for cmim in [120, 150, 180]:
    total = total + cmim
print(total)</pre>
    <button class="exbtn" id="unroll">Run one pass</button>
    <div id="passes" style="margin-top:8px;font-family:ui-monospace,Menlo,monospace;font-size:14px"></div>
    <p class="fignote" id="usum">The accumulator starts at 0. Press.</p>
  </div>
''',
 code_h2='Shape-reading drills',
 code_intro='Eight loops and forks. For each: name the shape, predict the '
      'output into a pred variable, run, CHECK. The last two mix both shapes.',
 deeper_h2='More shapes, if you want them',
 deeper_html='''
  <div class="gd"><b>Python Tutor, again.</b> Loops are where
  <a href="https://pythontutor.com" target="_blank" rel="noopener">pythontutor.com</a>
  shines — watch the accumulator grow pass by pass, exactly like the figure.</div>
  <div class="gd"><b>Stretch.</b> Find a loop in any code you can see — a
  tutorial, an AI answer, next week's notebook — and write its one-line purpose
  ("builds X from Y") without tracing. Then trace two passes to verify.</div>''',
 quiz=[
  ('A variable is set to 0 before a loop, added to inside it, printed after. The shape is…',
   [('a fork', 0), ('an accumulator — the loop builds a total', 1), ('an error', 0)]),
  ('When you meet an if/else, read FIRST…',
   [('the else branch', 0), ('the test — what decides the road', 1), ('the line after the fork', 0)]),
  ('From week 1: why trace exactly TWO passes of a loop first?',
   [('Two is faster than all and catches most misreadings', 1),
    ('Loops always run twice', 0),
    ('The first pass never matters', 0)]),
 ],
 build_h2='The shape catalog',
 build_html='''
  <p>From this week's notebook drills, build your personal shape catalog: for
  each of the two shapes (accumulator, fork), copy one example, write its
  one-line purpose, and mark the load-bearing line. Then write ONE program of
  your own that uses both shapes at once (a loop that counts only some items),
  with its own one-line purpose at the top as a comment.</p>
  <p><b>Turn-in:</b> the catalog + your combined program, running.</p>
''',
 fig_js='''
(function(){
  const PRICES=[120,150,180];let i=0,total=0;
  const btn=document.getElementById('unroll'),out=document.getElementById('passes'),
        sum=document.getElementById('usum');
  btn.addEventListener('click',()=>{
    if(i<PRICES.length){
      total+=PRICES[i];
      out.innerHTML+='pass '+(i+1)+': cmim = '+PRICES[i]+'  &rarr;  total = '+total+'<br>';
      i++;
      sum.textContent=(i<PRICES.length)?'Predict the next total before pressing.':'One press left — the print.';
    }else if(i===PRICES.length){
      out.innerHTML+='<b>print(total)  &rarr;  '+total+'</b><br>';i++;
      sum.innerHTML='<b>450.</b> Start value, one add per pass, used after — the accumulator, unrolled.';
    }});
})();
'''))

# ================================================================ READ 3
LESSONS.append(dict(sprint=RD, n=3, nb='read3-three-programs',
 title='Read code you didn’t write',
 lede='Other people’s code — including an AI’s — comes without your '
      'memory of writing it. This week: the top-down skim, the load-bearing '
      'line, and the smells that say "read me twice."',
 watch_h2='The top-down skim',
 watch_note='Names first, structure second, details last — and one line usually carries the weight.',
 listen_line='How to open thirty unfamiliar lines without drowning: read the '
      'names, find the load-bearing line, suspect the smells.',
 read_h2='Names, weight, and smells',
 read_html='''
  <p>Code you didn't write is a foreign city. The mistake is walking every
  street in order; the skill is reading the map first. <b>Skim top-down:</b>
  read the variable and function names before any logic —
  <span style="font-family:ui-monospace,Menlo,monospace">total_lek</span>,
  <span style="font-family:ui-monospace,Menlo,monospace">clean_name</span>,
  <span style="font-family:ui-monospace,Menlo,monospace">count_words</span> —
  good names are the author telling you the plot. Then find the <b>load-bearing
  line</b>: in most short programs, one line does the real work and the rest is
  setup and delivery. Find it, and you know what to trace carefully; everything
  else you trace lightly.</p>
  <p>Then the <b>smells</b> — patterns that don't prove a bug but earn a second
  read. <b>The magic number:</b> a bare 0.18 in the middle of a formula — why
  18 percent? A number with no name has no explanation. <b>The lying name:</b>
  a variable called <span style="font-family:ui-monospace,Menlo,monospace">average</span>
  that actually holds a sum — the name says one thing, the code does another,
  and every future reader inherits the lie. <b>The unused variable:</b>
  something computed and never used again — often a leftover, sometimes a bug
  (the author MEANT to use it).</p>
  <p>All of this applies double to AI-written code. It arrives fluent,
  confident, and unread by anyone — you are its first reader, and the smells
  are where to aim your suspicion. The verification habit you built in other
  sprints has a home address now: names, weight, smells.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Find the load-bearing line</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Three short programs. Click
    the ONE line that does the real work.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='Three programs you didn’t write',
 code_intro='A receipt totaler, a temperature converter, and a word counter — '
      'written by someone else, one hiding a real bug. Read FIRST (the notebook '
      'asks your answers via pred variables), run second.',
 deeper_h2='More reading, if you want it',
 deeper_html='''
  <div class="gd"><b>Real code, gently.</b> Any Colab notebook shared publicly
  is practice material — search "colab notebook beginner python" and read one
  cold: names, load-bearing lines, smells. You do not need to run it to read
  it.</div>
  <div class="gd"><b>Stretch.</b> Ask an AI assistant for a 15-line program
  that does something you choose. Before running: skim names, mark the
  load-bearing line, list any smells. Then run and check your read. This is
  the workflow, complete.</div>''',
 quiz=[
  ('Opening 30 unfamiliar lines, you read FIRST…',
   [('every line, in order', 0),
    ('the names — the author telling you the plot', 1),
    ('the last line only', 0)]),
  ('A bare 0.18 sitting in a formula is a smell because…',
   [('decimals are slower', 0),
    ('a number with no name carries no explanation for the next reader', 1),
    ('Python prefers whole numbers', 0)]),
  ('From week 2: before tracing an unfamiliar loop, you name its…',
   [('author', 0), ('shape and purpose', 1), ('line count', 0)]),
 ],
 build_h2='The bug report',
 build_html='''
  <p>One of the notebook's three programs contains a real bug. Your build is a
  proper bug report, the kind a professional files: what the program CLAIMS to
  do, what it ACTUALLY does (with the input that proves it), the load-bearing
  line where the bug lives, and the one-line fix. Write it before fixing;
  verify the fix after.</p>
  <p><b>Turn-in:</b> the report + a screenshot of the fixed program running
  correctly.</p>
''',
 fig_js='''
(function(){
  const PS=[
 {code:['emrat = ["Ana", "Blerim", "Drita"]','pershendetjet = []','for emri in emrat:',
        '    pershendetjet.append("Tungjatjeta, " + emri)','print(pershendetjet)'],a:3,
  why:'Line 4 builds each greeting — the append inside the loop IS the program. The rest is setup and delivery.'},
 {code:['cmimi = 2500','zbritja = cmimi * 0.30','cmimi_ri = cmimi - zbritja','print(cmimi_ri)'],a:1,
  why:'Line 2 computes the discount — and carries a magic number (why 30%?). Load-bearing AND smelly.'},
 {code:['fjalia = "sa mire dita sot"','fjalet = fjalia.split()','numri = len(fjalet)','print(numri)'],a:1,
  why:'split() turns the sentence into a list of words — everything after just counts and shows. The split is the work.'}];
  const wrap=document.getElementById('q1');let done=0,score=0;
  PS.forEach(p=>{
    const card=document.createElement('div');card.className='qcard';
    p.code.forEach((ln,j)=>{
      const b=document.createElement('button');b.className='choice';
      b.style.cssText='display:block;width:100%;text-align:left;font-family:ui-monospace,Menlo,monospace;font-size:13.5px;margin:2px 0';
      b.textContent=ln;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=j===p.a;if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach((x,k)=>{
          x.disabled=true;if(k===p.a)x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>That\\u2019s the one.</b> ':'<b>Reveal:</b> ')+p.why;
        card.appendChild(fb);
        if(done===PS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+PS.length+'.</b> Find the weight, then trace carefully there and lightly everywhere else.';
      });
      card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ READ 4
LESSONS.append(dict(sprint=RD, n=4, nb='read4-traceback-review',
 title='Read the traceback, write the review',
 lede='The capstone. Full tracebacks — the multi-line reports real programs '
      'produce — and your first complete code review, in writing, of a program '
      'you’ve never seen.',
 watch_h2='The traceback, bottom-up',
 watch_note='Last line first: the kind of problem. Then up the stack to YOUR line.',
 listen_line='Why professionals read tracebacks bottom-up, and what a written '
      'code review actually contains.',
 read_h2='The full report, and the review',
 read_html='''
  <p>So far your errors were one report deep. Real programs fail in chains: a
  line calls a helper, the helper fails, and Python prints the whole chain — a
  <b>traceback</b>. It looks like a wall of text and reads like a hallway if
  you know the direction: <b>bottom-up</b>. The last line names the kind of
  problem and the message. The lines above walk the chain — and your move is
  to climb until you reach a line YOU wrote or can change. That line is where
  the fixing starts, even when the failure happened deeper.</p>
  <p>And the capstone skill: the <b>written code review</b>. When a
  professional reviews code, the artifact is prose, and it has a fixed shape.
  <b>What it does</b> — two sentences, from the top-down skim.
  <b>What's solid</b> — name something genuinely good; reviews that only
  attack teach nothing and get ignored.
  <b>What's wrong or smelly</b> — each item with the line it lives on and WHY
  it matters, magic numbers and lying names included.
  <b>What I'd change first</b> — one concrete edit, not a rewrite.
  That shape works on a classmate's program, an AI's thirty lines, and — in a
  few years — a colleague's pull request. It is the reading sprint's whole
  skill, made visible on paper.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Climb the traceback</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A real-shaped traceback.
    Click the line where the FIXING should start.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='The review target',
 code_intro='Traceback drills first — three failing chains, pred variables for '
      'the kind and the fixing line. Then the review target: a 25-line program '
      'that mostly works. Read it cold; the notebook collects your review '
      'section by section.',
 deeper_h2='Where reviews live in the wild, if you want it',
 deeper_html='''
  <div class="gd"><b>Public code review, live.</b> Every open-source project on
  GitHub reviews changes in public — open any popular Python project, click
  "Pull requests", and read one review thread. Notice the shape: what it does,
  what's good, what to change.</div>
  <div class="gd"><b>Stretch.</b> Trade builds with a classmate from any
  sprint and review each other's capstone code with the four-part shape. The
  review you RECEIVE is the stretch.</div>''',
 quiz=[
  ('You read a traceback starting from…',
   [('the top — first things first', 0),
    ('the bottom — the kind of problem, then climb to your line', 1),
    ('the middle', 0)]),
  ('A written review names something genuinely good because…',
   [('politeness rules require it', 0),
    ('reviews that only attack teach nothing and get ignored', 1),
    ('bugs are rare', 0)]),
  ('From week 3: "average = a + b + c" is a lying name because…',
   [('averages need at least four numbers', 0),
    ('the name promises an average; the code stores a sum — every future reader inherits it', 1),
    ('variable names cannot be English words', 0)]),
 ],
 build_h2='The capstone: your first code review',
 build_html='''
  <p>Write the full four-part review of the notebook’s target program:
  what it does, what’s solid, what’s wrong or smelly (with line
  numbers and reasons — there are at least three findings to make), and the one
  change you’d make first. Then make that change and show it running.</p>
  <p><b>Turn-in:</b> the review + before/after screenshots. <b>This completes
  the sprint</b> — your teacher confirms all four weeks, and you are on the
  lecture list.</p>
''',
 fig_js='''
(function(){
  const LINES=[
 ['Traceback (most recent call last):',0],
 ['  File "receipt.py", line 12, in <module>',0],
 ['    print(total_line(cmimet))',0],
 ['  File "receipt.py", line 7, in total_line',1],
 ['    return "Total: " + sum(cmimet)',0],
 ['TypeError: can only concatenate str (not "int") to str',0]];
  const wrap=document.getElementById('q1'),sum=document.getElementById('q1sum');
  const card=document.createElement('div');card.className='qcard';
  LINES.forEach(([ln,ok],j)=>{
    const b=document.createElement('button');b.className='choice';
    b.style.cssText='display:block;width:100%;text-align:left;font-family:ui-monospace,Menlo,monospace;font-size:13px;margin:2px 0;white-space:pre-wrap';
    b.textContent=ln;
    b.addEventListener('click',()=>{
      if(card.dataset.done)return;card.dataset.done=1;
      const right=ok===1;
      card.classList.add(right?'good':'bad');
      [...card.querySelectorAll('.choice')].forEach((x,k)=>{
        x.disabled=true;if(LINES[k][1]===1)x.classList.add('right');
        else if(x===b&&!right)x.classList.add('wrong');});
      sum.innerHTML=(right?'<b>Climbed it.</b> ':'<b>Reveal:</b> ')+
        'Bottom line names the kind: TypeError, text glued to a number. Climb: the failure is on line 7, inside total_line, where sum() (a number) meets "Total: " (text). str(sum(cmimet)) fixes it. Line 12 just made the call.';
    });
    card.appendChild(b);});
  wrap.appendChild(card);
})();
'''))

# ================================================================ SOURCES 1
LESSONS.append(dict(sprint=SRC, n=1,
 title='The map of where answers live',
 lede='School hands you one source at a time. The real world is the opposite: '
      'a thousand sources, no syllabus. This week you learn the map — what '
      'kind of source answers what kind of need.',
 watch_h2='Five kinds of source',
 watch_note='Docs, tutorials, videos, Q&A, communities — each built for a different question.',
 listen_line='Why "just search it" fails beginners: searching works only when '
      'you know which KIND of answer you need.',
 read_h2='Kinds, not brands',
 read_html='''
  <p>Everything you will ever teach yourself — coding, cameras, chemistry,
  chess — lives in the same five kinds of source, and each kind answers a
  different need. Learn the kinds and every new topic gets a map.</p>
  <p><b>Official documentation</b> is the reference: complete, correct, dry.
  Built for looking things UP, not for learning from zero — reading docs
  cover-to-cover is like reading a dictionary to learn a language.
  <b>Tutorials and courses</b> are the guided path: someone ordered the ideas
  for you. Best at the start of a topic; too slow once you're moving.
  <b>Videos</b> show hands doing the thing — unbeatable for anything physical
  or visual, painful for anything you need to search or copy from.
  <b>Q&amp;A sites</b> (Stack Overflow and cousins) hold answers to exact,
  narrow questions — usually someone already hit your exact wall.
  <b>Communities</b> — forums, Discords, clubs — are where you ask the
  questions nothing else answered, and where taste gets transmitted: which
  tools people actually use, what matters, what's hype.</p>
  <p>The <b>first-15-minutes protocol</b> for any new topic: minutes 1–5, find
  the official source and skim its front page — just learn the vocabulary the
  field uses for itself. Minutes 5–10, find ONE well-regarded tutorial and
  read its table of contents — now you know the shape of the path. Minutes
  10–15, find where the community lives. You have not learned the topic — you
  have learned where the topic keeps its answers, and that is the meta-skill
  this month is about.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Match the need to the kind</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Six real needs. Pick the kind
    of source built for each.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='Run the protocol',
 code_intro='Pick something you genuinely want to learn — an instrument, a '
      'sport move, a language, a program. Run the first-15-minutes protocol on '
      'it, with a timer, and log what you found at each step: the official '
      'source, the tutorial and its table of contents, the community.',
 try_html='''
  <div class="gd"><b>The log format:</b> topic · the official source you found
  · the tutorial + three lines of its table of contents · where the community
  lives · one surprise. Five lines, honest, timed.</div>
''',
 deeper_h2='More of the map, if you want it',
 deeper_html='''
  <div class="gd"><b>See a great Q&amp;A answer.</b> Visit
  <a href="https://stackoverflow.com" target="_blank" rel="noopener">stackoverflow.com</a>
  and read one highly-voted answer on any topic — notice it explains WHY, not
  just what, and often corrects the question itself.</div>
  <div class="gd"><b>Stretch.</b> Run the protocol on a SECOND topic from a
  completely different field. The map transfers — feel it transfer.</div>''',
 quiz=[
  ('Official documentation is the wrong place to START a topic because…',
   [('it is usually wrong', 0),
    ('it is a reference — built for looking up, not for learning from zero', 1),
    ('it costs money', 0)]),
  ('Someone already hit your exact error message. The kind of source that holds their fix:',
   [('a video course', 0), ('a Q&A site', 1), ('the official front page', 0)]),
  ('The first-15-minutes protocol ends with you knowing…',
   [('the topic', 0),
    ('where the topic keeps its answers — vocabulary, path, community', 1),
    ('whether the topic is worth learning', 0)]),
 ],
 build_h2='The mapped topic',
 build_html='''
  <p>Turn your protocol run into the build: the five-line log, plus one
  paragraph — which KIND of source will carry most of your learning for this
  topic, and why. (A guitar and a Python library have different answers; that
  difference is the lesson.)</p>
  <p><b>Turn-in:</b> the log + paragraph.</p>
''',
 fig_js='''
(function(){
  const KINDS=['Docs','Tutorial','Video','Q&A','Community'];
  const QS=[
 ['What does the second argument of round() do?',0,'A lookup, not a lesson — the reference answers in ten seconds.'],
 ['I want to learn guitar from zero.',1,'You need someone to ORDER the ideas — a guided path.'],
 ['How do I hold the pick, exactly?',2,'Physical and visual — you need to see hands.'],
 ['My code fails with this exact error message.',3,'Someone hit your wall already — search the exact message.'],
 ['Which laptop do people actually buy for coding?',4,'Taste and current practice live where people talk.'],
 ['Is this tutorial from 2019 still right?',4,'Ask the people who would know what changed — the community holds the "what\\u2019s current" knowledge.']];
  const wrap=document.getElementById('q1');let done=0,score=0;
  QS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14.5px"></div>';
    card.querySelector('.qq').textContent=q[0];
    KINDS.forEach((k,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=k;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=j===q[1];if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach((x,m)=>{
          x.disabled=true;if(m===q[1])x.classList.add('right');
          else if(x===b&&!ok)x.classList.add('wrong');});
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Mapped.</b> ':'<b>Reveal:</b> ')+q[2];
        card.appendChild(fb);
        if(done===QS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+QS.length+'.</b> The need picks the kind; the kind picks the source.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ SOURCES 2
LESSONS.append(dict(sprint=SRC, n=2,
 title='Judge before you trust',
 lede='The internet’s best and worst tutorials look identical at first '
      'glance. This week: the five checks that separate them, run in under a '
      'minute.',
 watch_h2='The one-minute autopsy',
 watch_note='Date, author, the why, the working example, the cross-check.',
 listen_line='Why a beautiful tutorial can be worse than none — stale versions, '
      'confident errors — and the checks that catch it before it costs you a '
      'weekend.',
 read_h2='Five checks, one minute',
 read_html='''
  <p>Bad learning material does not announce itself. It is fluently written,
  nicely formatted, and quietly wrong — stale, copied, or confident beyond its
  knowledge. Since you cannot yet judge the CONTENT of a field you're new to,
  you judge the <b>signals around it</b>. Five checks, under a minute:</p>
  <p><b>1. The date.</b> Fields move. A Python tutorial from 2012 teaches a
  version that no longer runs; a camera guide from last year is fine. Rule of
  thumb: the faster the field changes, the harder the date matters — and an
  UNDATED tutorial in a fast field is a red flag by itself.</p>
  <p><b>2. The author.</b> Not fame — accountability. A named person with a
  history in the topic beats an anonymous content farm rewriting other
  people's posts for ad clicks. One search on the author's name settles it.</p>
  <p><b>3. The why.</b> Great material explains WHY each step exists; bad
  material lists steps. Steps without reasons cannot survive first contact
  with your slightly-different situation — and your situation is always
  slightly different.</p>
  <p><b>4. The working example.</b> In anything technical: does the tutorial's
  own example actually run? Test it EARLY, before investing an afternoon. A
  broken first example predicts everything after it.</p>
  <p><b>5. The cross-check.</b> The professional habit from the research
  world: any load-bearing claim gets confirmed by a second, independent
  source before you build on it. Independent means not copied from the same
  origin — and much of the internet is the same origin, paraphrased.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The tutorial autopsy</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Four tutorial descriptions.
    Trust it, or run — and name the check that decided.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='Autopsy two real ones',
 code_intro='Find two tutorials on ONE topic you care about (the topic from '
      'week 1 works). Run all five checks on each, score them side by side, '
      'and pick a winner — with the check that decided it.',
 try_html='''
  <div class="gd"><b>The scorecard:</b> for each tutorial — date? author?
  explains why? example runs? survives a cross-check? Five rows, two columns,
  one verdict.</div>
''',
 deeper_h2='Sharper judgment, if you want it',
 deeper_html='''
  <div class="gd"><b>Watch version drift bite.</b> Search "python print
  statement error" and see thousands of people caught by material written for
  Python 2 — the classic stale-tutorial injury, still claiming victims.</div>
  <div class="gd"><b>Stretch.</b> Find one piece of material that FAILS three
  or more checks and one that passes all five, in the same field. Save both
  links — they are your calibration pair.</div>''',
 quiz=[
  ('An undated tutorial in a fast-moving field is…',
   [('fine — good content is timeless', 0),
    ('a red flag by itself', 1),
    ('better, because it stays general', 0)]),
  ('Steps without reasons fail because…',
   [('they are harder to memorize', 0),
    ('your situation is always slightly different, and reasons are what adapt', 1),
    ('lists are bad formatting', 0)]),
  ('From week 1: the source kind where you’d ask whether a 2019 tutorial is still current:',
   [('the tutorial itself', 0), ('the community', 1), ('a video', 0)]),
 ],
 build_h2='The graded pair',
 build_html='''
  <p>The build is your two-tutorial scorecard from the Try segment, plus a
  three-sentence verdict: which one you’d follow, which check decided it,
  and what the losing tutorial would have cost you (time, wrong version, a
  broken weekend).</p>
  <p><b>Turn-in:</b> scorecard + verdict.</p>
''',
 fig_js='''
(function(){
  const QS=[
 ['Dated last month, named author who maintains the library, every step has a paragraph of why, first example runs.',1,
  'Passes everything visible. Trust — and still cross-check the load-bearing claims.'],
 ['Beautiful design, no date anywhere, author is "TechGuruBlog", steps with no reasons.',0,
  'Undated + anonymous + no whys — three checks down. The design is exactly what content farms are good at.'],
 ['From 2013, named university author, deep explanations — for a fast-moving programming library.',0,
  'The author and whys pass, but a 2013 version of a fast-moving library will fight you line by line. Date check kills it — find its modern equivalent.'],
 ['Recent video, hands visible doing the physical skill, comments full of "this worked for me".',1,
  'For a physical skill the video IS the right kind, recency passes, and the comments are a live cross-check.']];
  const wrap=document.getElementById('q1');let done=0,score=0;
  QS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14.5px"></div>';
    card.querySelector('.qq').textContent=q[0];
    ['Trust it','Run'].forEach((lbl,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=lbl;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=(j===0)===(q[1]===1);if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach(x=>x.disabled=true);
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Judged.</b> ':'<b>Reveal:</b> ')+q[2];
        card.appendChild(fb);
        if(done===QS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+QS.length+'.</b> One minute of checks saves one weekend of wrong.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ SOURCES 3
LESSONS.append(dict(sprint=SRC, n=3,
 title='Ask well',
 lede='At some point every learner hits a wall no source answers. This week: '
      'how to ask strangers for help so well that they enjoy answering — the '
      'most underrated skill on the internet.',
 watch_h2='The anatomy of a good question',
 watch_note='What you’re trying to do, what you tried, what happened — exactly.',
 listen_line='Why "it doesn’t work, please help" gets silence, and the '
      'three-part shape that gets answers in minutes.',
 read_h2='Search first, then ask like a scientist',
 read_html='''
  <p>First, the move that answers most questions before anyone is bothered:
  <b>search the exact error text, in quotes.</b> Not a description of the
  problem — the machine's own words. Error messages are identical across the
  world, which makes them the best search terms ever written. Strip out the
  parts unique to you (your file names, your variable names) and quote the
  rest. This one habit resolves most walls in five minutes.</p>
  <p>When search fails, you ask — and asking has an anatomy. <b>Part one: the
  goal.</b> What you are actually trying to achieve, one sentence, because
  half of all stuck-people are stuck on the wrong approach and the answerer
  can only see that if they know the destination. <b>Part two: what you
  tried.</b> The smallest complete version of your attempt — not your whole
  project, the smallest piece that still shows the problem. Cutting it down
  is work, and it is respectful work: you spend ten minutes so ten readers
  don't each spend ten. (Half the time, cutting it down reveals the answer
  by itself — the effect is so reliable it has a name: rubber-duck
  debugging.) <b>Part three: what happened.</b> The exact error text or the
  exact wrong output, pasted, never paraphrased. "It gives an error" is
  invisible; the error itself is searchable, diagnosable, answerable.</p>
  <p>Where to ask, in order: the sprint's Discord (fastest, friendliest), the
  topic's own community from week 1, then the big Q&amp;A sites (where your
  well-shaped question becomes the next searcher's answer). A good question,
  asked publicly, is a gift to everyone who hits the wall after you.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Fix the question</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A stuck student’s plea,
    rebuilt one choice at a time.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='Ask one for real',
 code_intro='Take a real wall you’ve hit — in any sprint, any topic — and '
      'write the three-part question: goal, smallest attempt, exact result. '
      'Post it in the sprint Discord (or bring it to class if the channel '
      'isn’t live yet).',
 try_html='''
  <div class="gd"><b>Before posting, the checklist:</b> Did I search the exact
  error first? Is the goal one sentence? Is the attempt the SMALLEST that
  shows the problem? Is the result pasted, not paraphrased?</div>
''',
 deeper_h2='The craft, deeper, if you want it',
 deeper_html='''
  <div class="gd"><b>The canonical guide.</b> Stack Overflow’s own
  <a href="https://stackoverflow.com/help/how-to-ask" target="_blank" rel="noopener">"How do I ask a good question?"</a>
  — the internet’s most battle-tested advice on this exact skill.</div>
  <div class="gd"><b>Stretch.</b> Find one unanswered question online in a
  topic you know a little — and answer it, using the same three-part care.
  Teaching at the exact edge of your knowledge is the fastest learning there
  is.</div>''',
 quiz=[
  ('Your code fails with an error. The FIRST move:',
   [('ask in three places at once', 0),
    ('search the exact error text, in quotes, with your unique names stripped', 1),
    ('rewrite the program from scratch', 0)]),
  ('You cut your broken code down to the smallest piece that still fails, and the answer appears before you post. This is…',
   [('luck', 0),
    ('rubber-duck debugging — so reliable it has a name', 1),
    ('a sign the code was fine', 0)]),
  ('From week 2: pasting the EXACT error instead of describing it also lets answerers…',
   [('grade your spelling', 0),
    ('search and cross-check it — machine words are identical worldwide', 1),
    ('skip reading your question', 0)]),
 ],
 build_h2='The asked question',
 build_html='''
  <p>The build is your real three-part question, actually posted (Discord,
  class board, or a Q&amp;A site) — plus a screenshot of the post and, if an
  answer arrived, two sentences on what the answer taught you about the
  QUESTION (what would you sharpen next time?).</p>
  <p><b>Turn-in:</b> the post + the reflection.</p>
''',
 fig_js='''
(function(){
  const STEPS=[
 {q:'The plea: "my code doesn\\u2019t work pls help :(" \\u2014 what does it need FIRST?',a:1,
  opts:['More politeness','The goal — what are you trying to achieve?','A screenshot of the whole screen'],
  why:'Nobody can help without the destination. One sentence of goal beats three paragraphs of panic.'},
 {q:'Goal added. Now: "here are all 340 lines of my project" — better move?',a:2,
  opts:['Post all 340 — more is more','Post none — describe it instead','Cut to the smallest piece that still shows the problem'],
  why:'The smallest failing piece respects ten readers\\u2019 time — and cutting it down solves it outright half the time.'},
 {q:'Last piece: "it gives an error" — replace with…',a:0,
  opts:['The exact error text, pasted','The error\\u2019s general vibe','How long you\\u2019ve been stuck'],
  why:'Paraphrased errors are invisible; pasted errors are searchable, diagnosable, answerable.'}];
  const wrap=document.getElementById('q1');let done=0,score=0;
  STEPS.forEach(q=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14.5px"></div>';
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
        fb.innerHTML=(ok?'<b>Sharper.</b> ':'<b>Reveal:</b> ')+q.why;
        card.appendChild(fb);
        if(done===STEPS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+STEPS.length+'.</b> Goal, smallest attempt, exact result — the shape that gets answers.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))

# ================================================================ SOURCES 4
LESSONS.append(dict(sprint=SRC, n=4,
 title='Build your learning system',
 lede='The capstone. Sources found, judged, and askable — now assemble them '
      'into a system that survives contact with a real two-week self-study '
      'plan. Then run day one.',
 watch_h2='Notes that survive',
 watch_note='In your own words, returned to on a schedule, organized for the next search.',
 listen_line='Why copied notes evaporate and rewritten notes stay — and what a '
      'self-study plan looks like when it’s honest about your real week.',
 read_h2='The system: notes, returns, and the plan',
 read_html='''
  <p><b>Notes that survive have one rule: your own words.</b> Copying a
  source's sentence feels efficient and stores nothing — the words pass
  through your hands without visiting your head. Rewriting the idea AS IF
  EXPLAINING IT to a classmate forces the visit. The test for every note you
  take: could you have written this sentence before you read the source? If
  yes, skip it. If no — that's the note.</p>
  <p><b>Returns beat volume.</b> You met this in other sprints as retrieval
  practice, and it governs self-study too: a note you return to after two
  days, then a week, then a month, becomes yours; a notebook filled once and
  never reopened is a diary of things you almost learned. Put the return
  dates IN the plan — they are study sessions, not admin.</p>
  <p><b>The honest two-week plan.</b> Pick the skill. Take your vetted
  sources from week 2. Then plan like the data sprint taught you to claim:
  against your REAL week, not an imaginary one — school, family, the days
  you're wrecked. Each session gets one sitting-sized goal with a visible
  finish ("play the chorus at half speed", "chapter 3's exercises run
  clean"), one source, and a two-line note slot. Build in one catch-up day
  per week, because life. A plan that survives two real weeks beats a
  beautiful plan that dies on day three — and knowing the difference is the
  whole sprint.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Fix the plan</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A two-week self-study plan
    with four planted flaws. Find them.</p>
    <div id="q1"></div>
    <p class="fignote" id="q1sum"></p>
  </div>
''',
 code_h2='Assemble and launch',
 code_intro='Write your real two-week plan — skill, vetted sources, '
      'sitting-sized sessions with visible finishes, return dates, catch-up '
      'days. Then run DAY ONE before the week ends, and log it.',
 try_html='''
  <div class="gd"><b>The plan template:</b> Skill &middot; why now &middot;
  sources (from your week-2 scorecard) &middot; 8–10 sessions, each: day /
  goal with visible finish / source / note slot &middot; two return-date
  sessions &middot; one catch-up day per week.</div>
''',
 deeper_h2='Running mates, if you want them',
 deeper_html='''
  <div class="gd"><b>The science of returns.</b>
  <a href="https://retrievalpractice.org" target="_blank" rel="noopener">retrievalpractice.org</a>
  — the research behind why coming back beats piling on, with student guides.</div>
  <div class="gd"><b>Stretch.</b> Recruit one classmate to run their own
  two-week plan in parallel. Compare day-one logs — and again at the lecture.</div>''',
 quiz=[
  ('The test for whether a note is worth taking:',
   [('is it short enough to copy quickly', 0),
    ('could I have written this before reading — if no, it’s the note', 1),
    ('does it use the source’s exact words', 0)]),
  ('Return dates go IN the plan because…',
   [('plans should look thorough', 0),
    ('returning on a schedule is study, not admin — it’s what makes notes yours', 1),
    ('sources expire', 0)]),
  ('From the data sprint: a plan against an imaginary week is…',
   [('ambitious, which is good', 0),
    ('an overclaim — it dies on contact with your real week', 1),
    ('required for motivation', 0)]),
 ],
 build_h2='The capstone: plan + day one',
 build_html='''
  <p>Turn in the full two-week plan AND the day-one log: what the session’s
  goal was, whether you hit the visible finish, the two-line note in your own
  words, and one adjustment the real day taught you to make to the plan.</p>
  <p><b>Turn-in:</b> plan + day-one log. <b>This completes the sprint</b> —
  your teacher confirms all four weeks, and you are on the lecture list.</p>
''',
 fig_js='''
(function(){
  const FLAWS=[
 ['Day 1: read chapters 1\\u20134 and take full notes on everything',1,
  'Not sitting-sized and no visible finish — "everything" is how day one kills a plan. One chapter, one runnable finish.'],
 ['Day 3: half-speed chorus, from the video course, note slot after',0,
  'Sitting-sized, visible finish, one source, note slot — this is what a session should look like.'],
 ['Notes: copy the tutorial\\u2019s key sentences into my notebook',1,
  'Copied words store nothing. Rewrite as if explaining to a classmate — that\\u2019s the visit to your head.'],
 ['Every single day scheduled, both weeks, no gaps',1,
  'No catch-up days = the first missed day breaks the chain and the plan. Life happens; plan for it.'],
 ['Day 5: return to day-1 notes and re-answer from memory',0,
  'A return session — the thing most plans forget and the thing that makes notes stick.'],
 ['Sources: the top three results from one search, unchecked',1,
  'Week 2 exists for a reason — unvetted sources walk stale or wrong material straight into your plan.']];
  const wrap=document.getElementById('q1');let done=0,score=0;
  FLAWS.forEach(f=>{
    const card=document.createElement('div');card.className='qcard';
    card.innerHTML='<div class="qq" style="font-size:14.5px"></div>';
    card.querySelector('.qq').textContent=f[0];
    ['Solid','Flawed'].forEach((lbl,j)=>{
      const b=document.createElement('button');b.className='choice';b.textContent=lbl;
      b.addEventListener('click',()=>{
        if(card.dataset.done)return;card.dataset.done=1;
        const ok=(j===1)===(f[1]===1);if(ok)score++;done++;
        card.classList.add(ok?'good':'bad');
        [...card.querySelectorAll('.choice')].forEach(x=>x.disabled=true);
        const fb=document.createElement('div');fb.className='qfb';
        fb.innerHTML=(ok?'<b>Caught it.</b> ':'<b>Reveal:</b> ')+f[2];
        card.appendChild(fb);
        if(done===FLAWS.length)document.getElementById('q1sum').innerHTML=
          '<b>'+score+' of '+FLAWS.length+'.</b> A plan that survives reality beats a beautiful one that doesn\\u2019t.';
      });card.appendChild(b);});
    wrap.appendChild(card);});
})();
'''))


if __name__ == '__main__':
    for l in LESSONS:
        key = l['sprint'][2]
        path = os.path.join(SITE, 'lesson-%s-%d.html' % (key, l['n']))
        with open(path, 'w') as f:
            f.write(fill(l))
        print(path)
