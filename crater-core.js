/* Albania Now — Crater Hunter world generator + detector core.
   Loaded by crater.html AND executed by tools/test_crater.js, so every
   weekly seed's difficulty is machine-verified before students see it. */
function alnowCraterWorld(num){
  const W=96,H=60,NCR=6;
  function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;
    let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;
    return((t^t>>>14)>>>0)/4294967296}}
  const rng=mulberry32(num*2654435761);

  // 6 non-overlapping craters; the first two are FAINT (shadow 102-110,
  // above the default threshold) — the tension the game is made of.
  const CR=[];
  while(CR.length<NCR){
    const r=4+Math.floor(rng()*5),
          cx=r+3+Math.floor(rng()*(W-2*r-6)),
          cy=r+3+Math.floor(rng()*(H-2*r-6));
    if(CR.every(function(c){return Math.hypot(cx-c[0],cy-c[1])>r+c[2]+4}))
      CR.push([cx,cy,r,CR.length<2]);
  }
  const IMG=[];
  for(let y=0;y<H;y++){const row=[];
    for(let x=0;x<W;x++){
      let v=180+Math.floor(rng()*36)-18;
      for(const c of CR){
        const d=Math.hypot(x-c[0],y-c[1]);
        if(d<c[2])v=(x<c[0])?(c[3]?102+Math.floor(rng()*9):50+Math.floor(rng()*22)):225;
        else if(d<c[2]+1.5&&x>c[0])v=240;}
      row.push(v);}
    IMG.push(row);}
  // junk specks (size filter fodder)
  for(let i=0;i<26;i++){
    const x=Math.floor(rng()*W),y=Math.floor(rng()*H);
    if(IMG[y][x]>150)IMG[y][x]=45;}
  // boulder shadows at 116 — 5x4 = 20px, immune to the size filter;
  // only a threshold below 116 keeps them out
  for(let i=0;i<4;i++){
    const bx=2+Math.floor(rng()*(W-8)),by=2+Math.floor(rng()*(H-6));
    let clear=true;
    for(const c of CR)if(Math.hypot(bx-c[0],by-c[1])<c[2]+7)clear=false;
    if(clear)for(let dy=0;dy<4;dy++)for(let dx=0;dx<5;dx++)IMG[by+dy][bx+dx]=116;}

  function blobs(T,minsz){
    const seen=IMG.map(function(r){return r.map(function(){return false})});
    const out=[];
    for(let y=0;y<H;y++)for(let x=0;x<W;x++){
      if(seen[y][x]||IMG[y][x]>=T)continue;
      const q=[[x,y]];seen[y][x]=true;const px=[];
      while(q.length){const p=q.pop(),a=p[0],b=p[1];px.push([a,b]);
        const dirs=[[1,0],[-1,0],[0,1],[0,-1]];
        for(const dd of dirs){
          const nx=a+dd[0],ny=b+dd[1];
          if(nx>=0&&nx<W&&ny>=0&&ny<H&&!seen[ny][nx]&&IMG[ny][nx]<T){
            seen[ny][nx]=true;q.push([nx,ny]);}}}
      if(px.length>=minsz)out.push(px);}
    return out;}
  function score(dets){
    let hits=0;const used=new Set();
    for(const c of CR){
      for(const b of dets){
        if(used.has(b))continue;
        let touch=false;
        for(const p of b)if(Math.hypot(p[0]-c[0],p[1]-c[1])<=c[2]+2){touch=true;break;}
        if(touch){hits++;used.add(b);break;}}}
    return {hits:hits,misses:NCR-hits,fa:dets.filter(function(b){return !used.has(b)}).length};}
  return {IMG:IMG,CR:CR,W:W,H:H,NCR:NCR,blobs:blobs,score:score};
}
if(typeof module!=='undefined')module.exports=alnowCraterWorld;
