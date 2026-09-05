#!/usr/bin/env python3
"""Albania Now — ds-1 worked-example video (second Watch video, 4x expansion).
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_ds1b.py"""
from vidlib import s_title, s_notebook, s_code, s_bullets, build_all, GREEN

L = {}

L["alnow-ds-1b"] = [
 (s_title("Week 1 · Worked example", "A first session, errors included",
          "Watch a real notebook run — mistakes and all."),
  "This is a worked example: a first Colab session, played out cell by cell — "
  "including the mistakes, because reading the mistakes is the skill."),
 (s_notebook("The session", "Three cells, one surprise", [
   (['print("Hello from Tirana")'], [("Hello from Tirana", "ok")]),
   (['emri = "Drita"', 'print(emri)'], [("Drita", "ok")]),
   (['print("age: " + 16)'],
    [("TypeError: can only concatenate str (not \"int\") to str", "err")]),
  ], note="Red text. Now we read it, not fear it."),
  "Cell one: print runs on a Google computer and the text comes back. Cell "
  "two: a variable — the name emri stores Drita, and print looks it up. Cell "
  "three: we glue text to the number sixteen, and Python refuses. Type error: "
  "can only concatenate str, not int, to str. That report names both sides of "
  "the problem — text met a number."),
 (s_code("The fix", "Two honest repairs",
   ['print("age: " + str(16))   # bridge: str turns 16 into text',
    '',
    'print("age:", 16)          # or a comma — print joins them itself'],
   console=[("age: 16", GREEN), ("age: 16", GREEN)],
   note="Same result, two idioms. Both count."),
  "Two repairs, both honest. Bridge the number into text with str — now plus "
  "glues two texts. Or hand print two things with a comma and let it join "
  "them. Run, green, done. That loop — write, read the report, repair, rerun "
  "— is the entire working life of a programmer, and you just watched all of "
  "it in ninety seconds."),
 (s_bullets("Now you", "The notebook is waiting", [
   "Run every teaching cell",
   "Fill the YOUR TURN cells",
   "Make the CHECK cells say PASSED",
   "Then the three-part build"], closing=True),
  "Now it is your turn. Run the teaching cells, fill in the your-turn cells, "
  "and make every check cell say passed. Then the three-part build: scale, "
  "the mad-lib, and your own error safari. Two to four hours, honestly spent."),
]

if __name__ == "__main__":
    build_all(L, "Data Science")
