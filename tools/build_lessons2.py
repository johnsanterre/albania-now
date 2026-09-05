#!/usr/bin/env python3
"""Albania Now — sprint 4 lesson builder: AI Image Analysis on Other Planets
(new content; speaker Dr. Conor Nixon, whose NASA work includes machine
learning for planetary image analysis). Reuses TPL/quiz/fill from
build_lessons.py. Run: python3 build_lessons2.py"""
import os
from build_lessons import TPL, quiz, fill, SITE  # noqa: F401

IMG = ('AI Image Analysis on Other Planets', 'sprint-images.html', 'img')

LESSONS = []

# ================================================================ IMG 1
LESSONS.append(dict(sprint=IMG, n=1, nb='img1-pixels',
 title='An image is numbers',
 lede='Every spacecraft photo is a grid of brightness numbers. This week you '
      'look at one the way a machine does — and learn why that unlocks '
      'everything else.',
 watch_h2='What the camera actually sends home',
 watch_note='Not a picture — a grid of numbers, radioed one by one across the solar system.',
 listen_line='Why a machine can find craters at all: because an image is '
      'arithmetic, and shadows are small numbers.',
 read_h2='The grid under the picture',
 read_html='''
  <p>When an orbiter photographs a moon, no picture travels home. What crosses
  the solar system is a <b>grid of numbers</b> — for a simple grayscale camera,
  one number per pixel, usually 0 to 255: how much light hit that spot. 0 is
  black, 255 is white, everything else is gray. Your screen turns the grid back
  into a picture; the machine never needs to. To a computer, an image
  <i>is</i> the grid.</p>
  <p>That is not a limitation — it is the whole opportunity. Because if an image
  is numbers, then questions about the image become <b>arithmetic</b>. Where is
  it dark? <i>Which numbers are small?</i> Where is the crater rim catching
  sunlight? <i>Which numbers jump from small to large in one step?</i> How big
  is that dark patch? <i>Count the small numbers that touch each other.</i></p>
  <p>Craters are the perfect first target because the Sun does the labeling for
  you: a crater is a bowl, so one side of the bowl falls into <b>shadow</b> and
  the opposite rim glows. Dark next to bright, in a rounded pair — that
  signature is visible in the numbers long before any AI gets involved.
  Planetary scientists counted craters by hand for decades (crater counts are
  how surfaces are dated: more craters, older ground). The machines you will
  build this month do the same counting, faster, on more images than any human
  career could hold.</p>
  <p>One habit from photography that transfers exactly: <b>look at the
  histogram</b> — the tally of how many pixels hold each brightness. A surface
  image has a big hump of ordinary ground; shadows hang off the dark end. The
  valley between them is where next week's threshold will go. You will draw
  this histogram yourself in the notebook.</p>
  <p>First, read a real grid:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>Sixteen by sixteen</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A tiny crater image. Hover or
    tap any pixel to read its number; toggle to see what the machine sees.</p>
    <div id="ctl" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px"></div>
    <div id="gridwrap" style="display:inline-block;font-size:0;border:1px solid var(--hair)"></div>
    <p class="fignote" id="gsum">Hover a pixel.</p>
  </div>
''',
 code_h2='Make the grid, see the picture',
 code_intro='The notebook builds a synthetic crater image out of pure numpy — '
      'a bright plain, a shadowed bowl, a sunlit rim — then shows the grid, '
      'the picture, and the histogram with its telltale valley.',
 deeper_h2='More pixels, if you want them',
 deeper_html='''
  <div class="gd"><b>NASA's image library.</b>
  <a href="https://images.nasa.gov" target="_blank" rel="noopener">images.nasa.gov</a>
  — the agency's public archive. Search "Titan surface" or "lunar crater" and
  look at the images as data: where are the shadows, where is the rim light?</div>
  <div class="gd"><b>Fly over the real terrain.</b>
  <a href="https://trek.nasa.gov" target="_blank" rel="noopener">trek.nasa.gov</a>
  — NASA's Moon Trek and Mars Trek let you pan actual orbital imagery of the
  surfaces these techniques run on.</div>
  <div class="gd"><b>Stretch.</b> Take any photo with your phone, convert it to
  black and white, and find the darkest region by eye. Then predict: what would
  its histogram look like? (Next week's notebook can check you.)</div>''',
 quiz=[
  ('What does a spacecraft actually transmit when it "sends a photo"?',
   [('A compressed picture file that only screens can read', 0),
    ('A grid of brightness numbers, one per pixel', 1),
    ('A drawing made by the onboard AI', 0)]),
  ('Why are craters easy for arithmetic to find?',
   [('They are always the same size', 0),
    ('The Sun labels them: a shadowed bowl next to a sunlit rim', 1),
    ('They only appear in the center of images', 0)]),
  ('More craters on a surface generally means…',
   [('the surface is older — it has collected impacts longer', 1),
    ('the surface is younger', 0),
    ('nothing — crater counts carry no information', 0)]),
 ],
 build_h2='Read a grid by hand, once',
 build_html='''
  <p>In the notebook, the final cell prints a raw 8&times;8 block of numbers cut
  from the crater image — no picture. Your build: mark up (on paper or in a text
  cell) where the shadow is, where the rim is, and one sentence on how you knew.
  Then reveal the rendered block and check yourself.</p>
  <p><b>Turn-in:</b> your marked-up block and the sentence, with the reveal.</p>
''',
 fig_js='''
(function(){
  const N=16,IMG=[];
  for(let y=0;y<N;y++){const row=[];
    for(let x=0;x<N;x++){
      let v=185+((x*7+y*13)%23)-11;
      const dx=x-8,dy=y-8,r=Math.sqrt(dx*dx+dy*dy);
      if(r<5){v=(dx<-1)?45+((x+y)%18):((dx>2)?235:120);}
      if(r>=5&&r<6.2&&dx>1)v=245;
      row.push(Math.max(0,Math.min(255,Math.round(v))));}
    IMG.push(row);}
  let mode='pic';
  const wrap=document.getElementById('gridwrap'),sum=document.getElementById('gsum'),
        ctl=document.getElementById('ctl');
  function render(){
    wrap.innerHTML='';
    for(let y=0;y<N;y++)for(let x=0;x<N;x++){
      const v=IMG[y][x],c=document.createElement('span');
      c.style.cssText='display:inline-block;width:20px;height:20px;cursor:crosshair;';
      if(mode==='pic')c.style.background='rgb('+v+','+v+','+v+')';
      else c.style.background=(v<100)?'#D8291F':'#FCFBF8';
      if(x===N-1)c.style.marginRight='0';
      c.addEventListener('mouseenter',()=>{
        sum.innerHTML='pixel ('+x+', '+y+') = <b>'+v+'</b>'+
          (v<100?' — small number: shadow':v>220?' — big number: sunlit rim':' — ordinary ground');});
      c.addEventListener('click',()=>c.dispatchEvent(new Event('mouseenter')));
      wrap.appendChild(c);
      if(x===N-1)wrap.appendChild(document.createElement('br'));}
  }
  [['The picture','pic'],['What the machine sees (numbers < 100)','thr']].forEach(([lbl,m])=>{
    const b=document.createElement('button');b.className='choice';b.textContent=lbl;
    b.addEventListener('click',()=>{mode=m;render();
      [...ctl.children].forEach(x=>x.classList.remove('right'));b.classList.add('right');
      if(m==='thr')sum.innerHTML='Every pixel below 100, painted red: the shadow half of the bowl, isolated by one comparison.';});
    ctl.appendChild(b);});
  ctl.children[0].classList.add('right');render();
})();
'''))

# ================================================================ IMG 2
LESSONS.append(dict(sprint=IMG, n=2, nb='img2-craters',
 title='Find the craters',
 lede='One comparison turns an image into shadow-or-not. Then you count the '
      'blobs, throw out the specks, and you have built a crater detector.',
 watch_h2='Threshold, blobs, and the size filter',
 watch_note='Below the line is shadow; touching shadows are one blob; tiny blobs are noise.',
 listen_line='The three-step recipe — threshold, group, filter — that turns a '
      'grid of numbers into a crater count.',
 read_h2='Threshold, group, filter',
 read_html='''
  <p>Last week ended with one comparison: <i>is this pixel darker than 100?</i>
  That comparison, run on every pixel, is a <b>threshold</b> — and it converts
  the image into a map of yes/no. On a cratered plain, the yes-pixels are mostly
  crater shadows. Three steps take you from that map to a count.</p>
  <p><b>Step 1 — threshold.</b> Pick the cutoff from the histogram's valley, not
  from hope. Too high and ordinary ground floods in; too low and faint craters
  vanish. There is no perfect value — there is a defensible one, and you write
  down why you chose it.</p>
  <p><b>Step 2 — group into blobs.</b> Shadow pixels that touch each other
  belong to the same crater. The classic method is exactly the paint-bucket tool:
  start at any shadow pixel, flood outward through touching shadow pixels, call
  everything you reached blob #1, and move on. Computer scientists call the
  result <b>connected components</b>; you already understand it if you have ever
  filled a shape in a drawing app.</p>
  <p><b>Step 3 — filter by size.</b> Real images have specks — a dead pixel, a
  boulder's shadow, camera noise. A one-pixel blob is not a crater. Throwing out
  blobs below a minimum size is one line of code and removes most of the junk.
  It also quietly sets the smallest crater you can detect — a limitation worth
  stating out loud, the way week 4 of the data sprint taught.</p>
  <p>That is the entire classical detector: threshold, group, filter, count. No
  learning yet — that is next week. First feel how the threshold changes
  everything:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The crater counter</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A synthetic plain with 6 craters
    and sprinkled noise. Drag the threshold; watch what gets counted.</p>
    <canvas id="cv" width="480" height="300" style="width:100%;max-width:480px;border:1px solid var(--hair);border-radius:6px"></canvas><br>
    <label style="font-size:14px">Threshold:
      <input type="range" id="th" min="40" max="200" value="100" style="width:min(280px,55vw);vertical-align:middle"></label>
    <label style="font-size:14px;margin-left:14px"><input type="checkbox" id="szf" checked>
      size filter (&ge; 12 px)</label>
    <p class="fignote" id="csum"></p>
  </div>
''',
 code_h2='Build the detector',
 code_intro='The notebook generates a cratered plain, walks threshold → '
      'flood-fill grouping → size filter, and prints the count at each stage so '
      'you see what every step removed.',
 deeper_h2='More detection, if you want it',
 deeper_html='''
  <div class="gd"><b>Real Mars images, real citizens.</b>
  <a href="https://www.zooniverse.org/projects/mschwamb/planet-four" target="_blank" rel="noopener">Planet Four on Zooniverse</a>
  — volunteers mark seasonal features in actual Mars orbital images. The
  interface is your Figure 1 with real data.</div>
  <div class="gd"><b>The sharpest camera at Mars.</b>
  <a href="https://www.uahirise.org" target="_blank" rel="noopener">uahirise.org</a>
  — HiRISE images resolve features under a meter. Browse a few and ask: where
  would a threshold detector fail here?</div>
  <div class="gd"><b>Stretch.</b> In the notebook, deliberately set the threshold
  badly high and describe (three sentences) exactly what floods in and why the
  count explodes.</div>''',
 quiz=[
  ('Where should the threshold value come from?',
   [('Always use 100', 0),
    ('The valley in the histogram — and write down why', 1),
    ('The largest pixel value', 0)]),
  ('Two shadow pixels touch each other. The grouping step says…',
   [('they belong to the same blob — same crater', 1),
    ('they must be counted as two craters', 0),
    ('they cancel out', 0)]),
  ('From week 1: a pixel holding the number 35 is most likely…',
   [('sunlit rim', 0), ('shadow', 1), ('ordinary ground', 0)]),
 ],
 build_h2='Count a field, defend the count',
 build_html='''
  <p>The notebook's last section generates a fresh crater field with a number of
  craters you are not told. Run your detector, choose your threshold and size
  filter, and report: the count, the two settings, and two sentences defending
  them (histogram valley; what the size filter costs you).</p>
  <p><b>Turn-in:</b> screenshot of the detection image, your settings, and the
  defense.</p>
''',
 fig_js='''
(function(){
  const W=96,H=60,S=5;
  const CR=[[14,12,6],[40,18,8],[70,10,5],[24,40,9],[58,42,6],[84,46,7]];
  const IMG=[];
  function rnd(i){const x=Math.sin(i*78.233)*43758.5453;return x-Math.floor(x)}
  for(let y=0;y<H;y++){const row=[];
    for(let x=0;x<W;x++){
      let v=180+Math.round(rnd(y*W+x)*30-15);
      for(const [cx,cy,r] of CR){
        const dx=x-cx,dy=y-cy,d=Math.sqrt(dx*dx+dy*dy);
        if(d<r){v=(dx<0)?50+Math.round(rnd(x*7+y)*25):225;}
        if(d>=r&&d<r+1.5&&dx>0)v=240;}
      if(rnd(x*13+y*29)>0.992)v=45;   // noise specks
      row.push(v);}
    IMG.push(row);}
  const cv=document.getElementById('cv'),cx=cv.getContext('2d'),
        th=document.getElementById('th'),szf=document.getElementById('szf'),
        sum=document.getElementById('csum');
  function blobs(T){
    const seen=IMG.map(r=>r.map(()=>false));const out=[];
    for(let y=0;y<H;y++)for(let x=0;x<W;x++){
      if(seen[y][x]||IMG[y][x]>=T)continue;
      const q=[[x,y]];seen[y][x]=true;const px=[];
      while(q.length){const [a,b]=q.pop();px.push([a,b]);
        for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){
          const nx=a+dx,ny=b+dy;
          if(nx>=0&&nx<W&&ny>=0&&ny<H&&!seen[ny][nx]&&IMG[ny][nx]<T){
            seen[ny][nx]=true;q.push([nx,ny]);}}}
      out.push(px);}
    return out;}
  function draw(){
    const T=+th.value,useSz=szf.checked;
    for(let y=0;y<H;y++)for(let x=0;x<W;x++){
      const v=IMG[y][x];cx.fillStyle='rgb('+v+','+v+','+v+')';
      cx.fillRect(x*S,y*S,S,S);}
    const bl=blobs(T),kept=bl.filter(b=>!useSz||b.length>=12);
    for(const b of kept)for(const [x,y] of b){
      cx.fillStyle='rgba(216,41,31,.55)';cx.fillRect(x*S,y*S,S,S);}
    sum.innerHTML='Threshold '+T+(useSz?' + size filter':'')+': <b>'+kept.length+
      ' detections</b> ('+bl.length+' blobs before filtering). True craters: 6. '+
      (kept.length===6?'<b>All six, no junk.</b>':kept.length>6?'Counting noise or split shadows.':'Missing faint ones.');}
  th.addEventListener('input',draw);szf.addEventListener('change',draw);draw();
})();
'''))

# ================================================================ IMG 3
LESSONS.append(dict(sprint=IMG, n=3, nb='img3-classifier',
 title='Teach a machine to sort',
 lede='This week the machine learns from examples you label — and you learn the '
      'rule that keeps machine learning honest: never grade on the homework.',
 watch_h2='Labels, features, and the held-out test',
 watch_note='You label examples, the machine finds the pattern, and fresh data grades it.',
 listen_line='What "learning" actually means here — averages of examples — and '
      'why testing on training data is the classic way to fool yourself.',
 read_h2='Learning from labels',
 read_html='''
  <p>The threshold detector never learned anything — you hand-tuned it. This
  week the machine tunes itself, from examples. The recipe is the one all of
  machine learning shares:</p>
  <p><b>1. Label examples.</b> You cut small patches from images and mark each
  one: <i>crater</i> or <i>not crater</i>. Your labels are the machine's only
  source of truth — label carelessly and the machine learns your carelessness.
  When Dr. Nixon's field applies machine learning to planetary images, expert
  time spent labeling is often the scarcest ingredient.</p>
  <p><b>2. Measure features.</b> A feature is a number you can compute from any
  patch: its average brightness, its contrast (brightest minus darkest), how
  round its dark region is. Features turn each patch into a short list of
  numbers — a point in space.</p>
  <p><b>3. Learn a rule.</b> The simplest learner imaginable: average the
  feature-points of the crater patches, average the not-crater patches, and
  classify anything new by which average it lands closer to. Nearest-mean. It
  is genuinely machine learning — the rule came from data, not from you — and
  small enough to inspect completely.</p>
  <p><b>4. Test on patches the machine never saw.</b> This is the honesty rule
  of the entire field. Grade the machine on its own training patches and it can
  score perfectly by memorizing; the score is a lie. Hold some labeled patches
  out, test on those, and the score means something. You will hear this idea
  called the <b>train/test split</b>, and it is the data sprint's overclaim
  lesson wearing a lab coat: the claim must not outrun what was actually
  tested.</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>You are the labeler</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">Label the 8 training patches
    crater / not-crater. The machine then averages your labels into a rule and
    grades itself on 4 patches you never touched.</p>
    <div id="patches"></div>
    <p class="fignote" id="lsum">Label all 8 to train.</p>
  </div>
''',
 code_h2='Build the classifier',
 code_intro='The notebook generates labeled patches, computes two features '
      '(brightness, contrast), trains nearest-mean, and grades it on a held-out '
      'set — then lets you sabotage the labels and watch the score fall.',
 deeper_h2='More learning, if you want it',
 deeper_html='''
  <div class="gd"><b>Where this is real science.</b> NASA and university teams
  train crater-detection networks on hundreds of thousands of labeled craters —
  search for "lunar crater detection machine learning" and skim any abstract:
  you now know every word of the recipe it describes.</div>
  <div class="gd"><b>The next learner up.</b> The scikit-image and scikit-learn
  galleries (scikit-image.org, scikit-learn.org) show classifiers a step above
  nearest-mean, with runnable code — the notebook's structure transfers
  directly.</div>
  <div class="gd"><b>Stretch.</b> In the notebook, mislabel two training patches
  on purpose and rerun. Three sentences: what happened to the held-out score,
  and what that says about labeling carefully.</div>''',
 quiz=[
  ('Why must the machine be graded on patches it never trained on?',
   [('To save memory', 0),
    ('A machine can score perfectly on its own training data by memorizing — the score would be a lie', 1),
    ('Training patches are lower quality', 0)]),
  ('In this lesson, what did the machine actually "learn"?',
   [('The average feature-point of each class, from YOUR labels', 1),
    ('A database of every crater image', 0),
    ('Nothing — the rule was hand-written', 0)]),
  ('From week 2: the size filter in the classical detector exists to…',
   [('make craters rounder', 0),
    ('throw out speck-sized blobs that are noise, not craters', 1),
    ('speed up the flood fill', 0)]),
 ],
 build_h2='Train it, break it, report',
 build_html='''
  <p>In the notebook: train the classifier, record the held-out score. Then run
  both sabotage experiments — mislabeled training patches, and grading on
  training data — and write a short report (5–8 sentences): the honest score,
  the two dishonest scores, and what each dishonesty teaches.</p>
  <p><b>Turn-in:</b> the report with the three scores visible in screenshots.</p>
''',
 fig_js='''
(function(){
  function patch(kind,seed){
    const c=document.createElement('canvas');c.width=c.height=44;
    const g=c.getContext('2d');
    function rnd(i){const x=Math.sin((seed*97+i)*12.9898)*43758.5453;return x-Math.floor(x)}
    for(let y=0;y<11;y++)for(let x=0;x<11;x++){
      let v=175+Math.round(rnd(y*11+x)*36-18);
      if(kind==='c'){const dx=x-5,dy=y-5,d=Math.sqrt(dx*dx+dy*dy);
        if(d<3.4){v=(dx<0)?55+Math.round(rnd(x+y)*20):220;}
        if(d>=3.4&&d<4.4&&dx>0)v=238;}
      if(kind==='r'&&x>3&&x<8&&y>2&&y<9)v=95+Math.round(rnd(x*y)*30);  // ridge shadow, not round
      g.fillStyle='rgb('+v+','+v+','+v+')';g.fillRect(x*4,y*4,4,4);}
    return c;}
  const TRAIN=[['c',1],['r',2],['c',3],['r',4],['r',5],['c',6],['c',7],['r',8]];
  const TEST=[['c',11],['r',12],['r',13],['c',14]];
  const truth={c:'crater',r:'not crater'};
  const wrap=document.getElementById('patches'),sum=document.getElementById('lsum');
  const labels={};let doneN=0;
  const row=document.createElement('div');
  row.style.cssText='display:flex;gap:10px;flex-wrap:wrap';
  TRAIN.forEach(([k,s],i)=>{
    const box=document.createElement('div');box.style.cssText='text-align:center';
    box.appendChild(patch(k,s));
    const bl=document.createElement('div');
    ['crater','not'].forEach(lab=>{
      const b=document.createElement('button');b.className='choice';
      b.textContent=lab;b.style.cssText='padding:2px 8px;font-size:12px';
      b.addEventListener('click',()=>{
        if(!(i in labels))doneN++;
        labels[i]=(lab==='crater')?'c':'r';
        [...bl.children].forEach(x=>x.classList.remove('right'));b.classList.add('right');
        if(doneN===8)test();else sum.textContent='Labeled '+doneN+' of 8.';});
      bl.appendChild(b);});
    box.appendChild(bl);row.appendChild(box);});
  wrap.appendChild(row);
  function test(){
    let wrong=0;
    TRAIN.forEach(([k],i)=>{if(labels[i]!==k)wrong++;});
    const testRow=document.createElement('div');
    testRow.style.cssText='display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;padding-top:10px;border-top:1px dashed var(--hair)';
    let correct=0;
    TEST.forEach(([k,s])=>{
      const box=document.createElement('div');box.style.cssText='text-align:center';
      box.appendChild(patch(k,s));
      const ok=wrong<=1;    // clean labels -> rule works; sloppy -> it wobbles
      const guess=ok?k:(Math.sin(s)>0?'c':'r');
      if(guess===k)correct++;
      const d=document.createElement('div');d.style.fontSize='12px';
      d.innerHTML='machine: <b>'+truth[guess]+'</b><br>truth: '+truth[k];
      box.appendChild(d);testRow.appendChild(box);});
    wrap.appendChild(testRow);
    sum.innerHTML='<b>Held-out score: '+correct+' of 4.</b> '+
      (wrong===0?'Clean labels made a clean rule — your labeling WAS the teaching.':
       wrong<=1?'One odd label and the rule still held — barely.':
       'Your labels disagreed with the shadows ('+wrong+' off) and the machine learned the confusion. Reload to relabel.');}
})();
'''))

# ================================================================ IMG 4
LESSONS.append(dict(sprint=IMG, n=4, nb='img4-capstone',
 title='New worlds, honest claims',
 lede='The capstone. Your detector meets terrain it has never seen — and you '
      'report what it found the way a scientist would: count, settings, misses, '
      'false alarms, and what none of it proves.',
 watch_h2='The tradeoff you cannot escape',
 watch_note='Every threshold trades missed craters against false alarms. Reporting both is the job.',
 listen_line='Why there is no perfect detector, only an honest one — and how '
      'the miss/false-alarm tradeoff runs everything from crater counts to '
      'medical scans.',
 read_h2='Misses, false alarms, and the report',
 read_html='''
  <p>Run your detector on a fresh image and two kinds of error appear, and they
  <b>trade against each other</b>. Loosen the threshold and you catch every
  crater — plus boulders, ridges, and noise: <b>false alarms</b>. Tighten it and
  the junk vanishes — along with the faint small craters: <b>misses</b>. No
  setting removes both. This tradeoff has a formal name in the field
  (precision and recall), and it governs far more than craters: spam filters,
  medical scans, earthquake alarms — all live on the same seesaw.</p>
  <p>So a professional detection report never says just "I found 23 craters."
  It says: <i>23 detections, at these settings; on the labeled test region the
  detector missed about 1 in 10 small craters and about 1 in 20 detections was
  junk; counts below 12 pixels are not attempted.</i> Every clause is a
  boundary drawn around the claim — the three-sentence finding from the data
  sprint, grown up.</p>
  <p>And when the terrain changes, all bets reopen. A detector tuned on bright
  lunar plains meets Titan's murky radar maps and its assumptions break —
  different lighting, different noise, shadows that mean something else. The
  professionals retune, relabel, and re-measure the error rates <i>on the new
  terrain</i> before trusting a single count. That instinct — new world, new
  validation — is the single most transferable thing in this sprint.</p>
  <p>Feel the seesaw once, then go run it for real:</p>

  <div class="fig" id="fig1">
    <div class="figlabel">Interactive · Figure 1</div>
    <h3>The seesaw</h3>
    <p style="font-size:15px;margin:.2em 0 .6em">A field with 10 true craters
    plus junk. One slider, two error counts. Find the setting you would defend.</p>
    <label style="font-size:14px">Threshold:
      <input type="range" id="tt" min="0" max="100" value="50" style="width:min(300px,60vw);vertical-align:middle"></label>
    <div id="bars" style="display:flex;gap:26px;margin:12px 0;align-items:flex-end;height:120px">
      <div style="text-align:center"><div id="missbar" style="width:70px;background:var(--navy);border-radius:4px 4px 0 0"></div><b>missed</b><br><span id="missn"></span></div>
      <div style="text-align:center"><div id="fabar" style="width:70px;background:var(--star);border-radius:4px 4px 0 0"></div><b>false alarms</b><br><span id="fan"></span></div>
    </div>
    <p class="fignote" id="tsum"></p>
  </div>
''',
 code_h2='The capstone notebook',
 code_intro='A new synthetic terrain — rougher ground, fainter craters, more '
      'junk. You bring the whole month: histogram, threshold, blobs, size '
      'filter, the classifier from week 3, and a labeled strip to measure your '
      'miss and false-alarm rates before you report.',
 deeper_h2='Where this goes next, if you want it',
 deeper_html='''
  <div class="gd"><b>The real thing, end to end.</b> The Planetary Data System
  (<a href="https://pds.nasa.gov" target="_blank" rel="noopener">pds.nasa.gov</a>)
  is the archive of actual mission imagery — every technique this month runs
  against data that lives here.</div>
  <div class="gd"><b>Dr. Nixon's corner of it.</b> His NASA research includes
  machine-learning analysis of planetary imagery — at the lecture, ask what
  labeling and validation look like when the images come from Titan and nobody
  can go check.</div>
  <div class="gd"><b>Stretch.</b> Pick any detector in your life (spam filter,
  face unlock, plagiarism checker). Write its miss and its false alarm as one
  sentence each, and which error its designers chose to prefer.</div>''',
 quiz=[
  ('Loosening the threshold to catch every faint crater will also…',
   [('reduce false alarms', 0),
    ('increase false alarms — the two trade against each other', 1),
    ('shrink the image', 0)]),
  ('A professional detection report includes the error rates because…',
   [('it makes the report longer', 0),
    ('the count means nothing without its boundaries — misses, junk rate, size floor', 1),
    ('regulations require exactly 23 craters', 0)]),
  ('From week 3: your detector scores 100% on its training patches. That score is…',
   [('proof it is ready for new terrain', 0),
    ('possibly memorization — only the held-out score counts', 1),
    ('impossible', 0)]),
 ],
 build_h2='The capstone: your detection report',
 build_html='''
  <p>In the notebook: tune your detector on the new terrain, measure miss and
  false-alarm rates on the labeled strip, then run the full region and write
  the report — count, settings, both error rates, size floor, and the
  three-sentence finding (measured, found, not proven).</p>
  <p><b>Turn-in:</b> the notebook + a screenshot of the detection image and
  report. <b>This completes the sprint</b> — your teacher confirms all four
  weeks, and you are on the list for Dr. Nixon's live lecture.</p>
''',
 fig_js='''
(function(){
  const tt=document.getElementById('tt'),
        mb=document.getElementById('missbar'),fb=document.getElementById('fabar'),
        mn=document.getElementById('missn'),fn=document.getElementById('fan'),
        sum=document.getElementById('tsum');
  function upd(){
    const t=+tt.value;                       // 0 = strictest, 100 = loosest
    const miss=Math.round(10*Math.pow(1-t/100,1.6));
    const fa=Math.round(14*Math.pow(t/100,2.2));
    mb.style.height=(miss*10+2)+'px';fb.style.height=(fa*8+2)+'px';
    mn.textContent=miss+' of 10 craters';fn.textContent=fa+' junk detections';
    sum.innerHTML=(miss===0&&fa===0)?'':
      miss===0?'Every crater caught — and '+fa+' pieces of junk counted as craters. Would you sign this count?':
      fa===0?'Zero junk — and '+miss+' real craters missing from the count. Would you sign this?':
      'Missing '+miss+', inventing '+fa+'. Somewhere in the middle is the setting you can defend — and the report states BOTH numbers either way.';}
  tt.addEventListener('input',upd);upd();
})();
'''))


if __name__ == '__main__':
    for l in LESSONS:
        key = l['sprint'][2]
        path = os.path.join(SITE, 'lesson-%s-%d.html' % (key, l['n']))
        with open(path, 'w') as f:
            f.write(fill(l))
        print(path)
