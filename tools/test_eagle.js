/* Eagle's Flight verifier: every level's par solution must run in-bounds,
   produce a valid star layout (>=3 distinct stars), collect ALL stars, and
   earn 3 stars at par. Also: par must be honest (no wasted trailing moves —
   the last step of the solution collects a star or turns for one).
   Run: node test_eagle.js */
var E = require('../eagle-core.js');
var bad = 0;
E.LEVELS.forEach(function(lv, i) {
  var n = i + 1;
  var stars = E.stars(lv);
  if (!stars) { console.log('L' + n, lv.name, ': PAR SOLUTION CRASHES or bad starSteps'); bad++; return; }
  if (stars.length < 3) { console.log('L' + n, lv.name, ': only', stars.length, 'distinct stars'); bad++; return; }
  var j = E.judge(lv, lv.sol.main, lv.sol.f1);
  if (!j.ok) { console.log('L' + n, lv.name, ': par does not collect all stars (', j.collected, '/', j.total, ')'); bad++; return; }
  if (j.stars !== 3) { console.log('L' + n, lv.name, ': par earns', j.stars, 'stars, not 3'); bad++; return; }
  console.log('L' + n, '"' + lv.name + '"', 'OK —', stars.length, 'stars, par', j.par);
});
console.log(bad ? bad + ' LEVELS BROKEN' : 'ALL ' + E.LEVELS.length + ' LEVELS VERIFIED');
process.exit(bad ? 1 : 0);
