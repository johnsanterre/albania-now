/* Albania Now — canvas share card (G1). Draws a 1200x630 result card and
   shares it via the Web Share API (file) or downloads it. */
function alnowShareCard(o){
  // o: {title, grid, line, url, num}
  const cv=document.createElement('canvas');cv.width=1200;cv.height=630;
  const x=cv.getContext('2d');
  const g=x.createLinearGradient(0,0,1200,630);
  g.addColorStop(0,'#C1272D');g.addColorStop(.55,'#D8291F');g.addColorStop(1,'#A31D15');
  x.fillStyle=g;x.fillRect(0,0,1200,630);
  x.fillStyle='#1A1414';x.fillRect(0,600,1200,30);
  // wing mark
  x.fillStyle='#1A1414';
  x.beginPath();
  [[600,60],[480,140],[530,140],[570,180],[600,130],[630,180],[670,140],[720,140]]
    .forEach(([px,py],i)=>i?x.lineTo(px,py):x.moveTo(px,py));
  x.closePath();x.fill();
  x.beginPath();x.moveTo(600,130);x.lineTo(580,210);x.lineTo(600,180);
  x.lineTo(620,210);x.closePath();x.fill();
  x.textAlign='center';x.fillStyle='#FFF';
  x.font='800 30px -apple-system, Segoe UI, sans-serif';
  x.fillText('ALBANIA NOW',600,260);
  x.font='800 64px -apple-system, Segoe UI, sans-serif';
  x.fillText(o.title+(o.num?' #'+o.num:''),600,345);
  x.font='72px sans-serif';
  x.fillText(o.grid,600,440);
  x.fillStyle='#F7D8D4';
  x.font='600 34px -apple-system, Segoe UI, sans-serif';
  x.fillText(o.line,600,505);
  x.fillStyle='#FFF';
  x.font='700 28px -apple-system, Segoe UI, sans-serif';
  x.fillText(o.url,600,570);
  cv.toBlob(function(blob){
    const f=new File([blob],'albania-now.png',{type:'image/png'});
    if(navigator.canShare&&navigator.canShare({files:[f]})){
      navigator.share({files:[f],text:o.line+' '+('https://'+o.url)}).catch(function(){});
    }else{
      const a=document.createElement('a');
      a.href=URL.createObjectURL(blob);a.download='albania-now.png';a.click();
    }
  },'image/png');
}
