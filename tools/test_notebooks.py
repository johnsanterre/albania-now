#!/usr/bin/env python3
"""Albania Now — notebook unit tests (John's ask, 2026-09-04).

Executes every notebook in notebooks/ cell by cell in a fresh namespace:
- ordinary teaching cells MUST run clean;
- cells marked "broken on purpose" MUST raise (that is their job);
- YOUR-TURN / build scaffolds get the reference solution injected from
  SOLUTIONS below (keyed by the scaffold's first line), so the CHECK cells
  that grade students are themselves graded here;
- a scaffold with no solution is skipped, along with nothing else — CHECK
  cells always run, so a missing solution that a CHECK depends on FAILS
  loudly (that is a coverage gap to fix, not to hide).

Run: ./testenv/bin/python test_notebooks.py   (from albania/tools/)
Exit code 1 on any failure.
"""
import glob, io, json, os, sys, traceback

os.environ['MPLBACKEND'] = 'Agg'
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS = {
 'ds1-first-steps': {
  '# your turn': 'print("I am about", 16 * 365, "days old")',
  'emri = ""': 'emri = "Test"\nmosha = 16\nqyteti = "Tirana"\n'
               'print(emri, "is", mosha, "and lives in", qyteti)',
  'line = ""': 'line = "=" * 20\nprint(line)',
  '# lab b': 'artikull1, cmim1 = "byrek", 120\nartikull2, cmim2 = "kafe", 150\n'
             'total = cmim1 + cmim2\nprint("=" * 24)\n'
             'print(artikull1, cmim1, "lek")\nprint(artikull2, cmim2, "lek")\n'
             'print("TOTAL", total, "lek")',
  '# fix me 1': 'pershendetje = "Mirëdita"\nprint(pershendetje)',
  '# fix me 2': 'total_lek = int("100") + 50\nprint(total_lek)',
  '# fix me 3': 'qytet = "Berat"\nprint(qytet)',
  '# part a': 'for i in range(1, 501):\n    print("Tirana is home", i)',
  '# part b': 'emri, mosha, qyteti = "Test", 16, "Tirana"\n'
              'print(emri + ", " + str(mosha) + ", nga " + qyteti)',
  '# stretch': 'for i in range(10, 0, -1):\n    print(i)\nprint("Fest!")',
 },
 'ds2-tables': {
  '# question 1': 'print(df[df["coastal"] == "yes"].sort_values("population").tail(1))',
  '# question 2': 'print(df.groupby("region").size())',
  '# question 3': 'print(df.sort_values("population", ascending=False).head(3))',
 },
 'ds3-charts': {
  '# the build': 'plt.bar(["A", "B"], [96, 100]); plt.ylabel("units"); plt.show()',
 },
 'ds4-capstone': {
  '# your analysis': 'sub = df[df["product"] == "coffee"]\n'
                     'print(len(df), "->", len(sub))\n'
                     'print(sub.groupby("weekday")["revenue_lek"].mean())',
 },
 'space1-spectra': {
  '# your turn': 'seen2 = seen - dip(wl, 4.3, 0.1, 0.35)\n'
                 'order = wl[np.argsort(seen2)[:2]]\nprint(sorted(order.round(1)))',
 },
 'space2-missions': {
  '# your turn': 'mars_rt = 2 * delay_min[2]\nprint(round(mars_rt), "minutes")\n'
                 'print("Huygens descent 150 min; Saturn round trip",\n'
                 '      round(2 * delay_min[4]), "min - no steering possible")',
 },
 'space3-titan': {
  '# your turn': 'print(90.7 <= 92 <= 111.7)\n'
                 'print("moon:", 60 * 1.62, "N vs titan:", 60 * 1.35, "N")',
 },
 'space4-transit': {},
 'img1-pixels': {
  '# your turn': 'my_block = img[0:8, 0:8].astype(int)\nprint(my_block)',
 },
 'img2-craters': {},
 'img3-classifier': {},
 'img4-capstone': {},
 'tiny2-bigram-machine': {},
 'read1-trace-drills': {
  '# predict 1 ': 'pred_1 = 15', '# predict 2 ': 'pred_2 = 8',
  '# predict 3 ': 'pred_3 = "Blerta 6"', '# predict 4 ': 'pred_4 = "555"',
  '# predict 5 ': 'pred_5 = 16', '# predict 6 ': 'pred_6 = "VaVa!"',
  '# predict 7 ': 'pred_7 = 3', '# predict 8 ': 'pred_8 = 10',
  '# predict 9 ': 'pred_9 = 17', '# predict 10 ': 'pred_10 = "33"',
 },
 'read2-shape-drills': {
  '# predict 1 ': 'pred_1 = 13', '# predict 2 ': 'pred_2 = 3',
  '# predict 3 ': 'pred_3 = "jo ende"', '# predict 4 ': 'pred_4 = 18',
  '# predict 5 ': 'pred_5 = "sa mire "', '# predict 6 ': 'pred_6 = 30',
  '# predict 7 ': 'pred_7 = 19', '# predict 8 ': 'pred_8 = 12',
 },
 'read3-three-programs': {
  '# predict — what number': 'pred_1 = 850.5',
  '# predict — the fahrenheit': 'pred_2 = 77.0',
  '# predict — the number it prints': 'pred_3 = 3',
 },
 'read4-traceback-review': {
  '# predict — which line number': 'pred_1 = 2',
  '# predict — the kind of error': 'pred_2 = "ZeroDivisionError"',
 },
}

SKIP_PREFIXES = ('# your turn', '# the build', '# part', '# question',
                 '# stretch', '# your analysis', '# your detector',
                 '# your', '# quest')


def run_notebook(path):
    name = os.path.basename(path)[:-6]
    doc = json.load(open(path))
    sols = SOLUTIONS.get(name, {})
    ns = {'__name__': '__main__'}
    fails, ran, injected, skipped, xfail = [], 0, 0, 0, 0
    for idx, cell in enumerate(doc['cells']):
        if cell['cell_type'] != 'code':
            continue
        src = ''.join(cell['source'])
        stripped = src.strip()
        if not stripped:
            continue
        first = stripped.splitlines()[0].strip().lower()
        expect_raise = 'broken on purpose' in src
        sol = None
        if not expect_raise and not first.startswith('# check'):
            for key, code in sols.items():
                if first.startswith(key.lower()):
                    sol = code
                    break
        if sol is not None:
            src = sol
            injected += 1
        elif not expect_raise and first.startswith(SKIP_PREFIXES) and not first.startswith('# check'):
            skipped += 1
            continue
        try:
            code_obj = compile(src, '%s[cell %d]' % (name, idx), 'exec')
            old = sys.stdout
            sys.stdout = io.StringIO()
            try:
                exec(code_obj, ns)
            finally:
                sys.stdout = old
            if expect_raise:
                fails.append('cell %d: marked broken on purpose but ran CLEAN' % idx)
            else:
                ran += 1
        except SyntaxError:
            if expect_raise:
                xfail += 1
            else:
                fails.append('cell %d SyntaxError:\n%s' % (idx, traceback.format_exc(limit=0)))
        except Exception:
            if expect_raise:
                xfail += 1
            else:
                fails.append('cell %d raised:\n%s' % (idx, traceback.format_exc(limit=1)))
    return ran, injected, skipped, xfail, fails


def main():
    paths = sorted(glob.glob(os.path.join(SITE, 'notebooks', '*.ipynb')))
    bad = 0
    for p in paths:
        ran, inj, skip, xfail, fails = run_notebook(p)
        status = 'PASS' if not fails else 'FAIL'
        if fails:
            bad += 1
        print('%s  %-28s ran %2d · solutions %d · skipped %d · expected-raise %d'
              % (status, os.path.basename(p), ran, inj, skip, xfail))
        for f in fails:
            print('      ' + f.replace('\n', '\n      '))
    print('%d/%d notebooks pass' % (len(paths) - bad, len(paths)))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
