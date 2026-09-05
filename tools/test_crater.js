/* Crater Hunter difficulty verifier: for every weekly seed in the next two
   years, assert (a) a clean sweep (6 hits, 0 junk) is ACHIEVABLE at some
   threshold, (b) the default setting (T=100) does NOT sweep, so the game
   requires tuning. Run: node test_crater.js */
const world = require('../crater-core.js');
let bad = 0, sweepWidths = [];
for (let num = 30; num <= 140; num++) {
  const w = world(num);
  let sweepTs = [];
  for (let T = 60; T <= 170; T++) {
    const s = w.score(w.blobs(T, 12));
    if (s.hits === 6 && s.fa === 0) sweepTs.push(T);
  }
  const def = w.score(w.blobs(100, 12));
  const defaultSweeps = def.hits === 6 && def.fa === 0;
  if (!sweepTs.length) { console.log('week', num, 'UNSOLVABLE'); bad++; }
  else if (defaultSweeps) { console.log('week', num, 'TRIVIAL (default wins)'); bad++; }
  else sweepWidths.push(sweepTs.length);
}
sweepWidths.sort((a, b) => a - b);
console.log('weeks tested:', 111 - bad, 'ok,', bad, 'bad');
console.log('sweep-window width: min', sweepWidths[0],
            'median', sweepWidths[Math.floor(sweepWidths.length / 2)],
            'max', sweepWidths[sweepWidths.length - 1]);
process.exit(bad ? 1 : 0);
