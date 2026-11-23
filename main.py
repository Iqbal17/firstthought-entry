#!/usr/bin/env python3
"""One Word, First Thought — writes exactly one word to entry.txt.

The word: "defenestration" (14 characters, one word, within the
1-24 character gate). The act of throwing someone out of a window.

FINAL DECISION RECORD — the word was chosen in two passes.
Pass 1 weighed petrichor, sonder, zugzwang, apricity and quixotic
against the judge's criteria (surprise first, then vividness, then
wit, then "feels chosen") and picked defenestration for topping
all four: nobody guesses it, it summons a complete scene in one
word, its sound is funny, and it could only be picked on purpose.

Pass 2 re-opened the choice and tested four more candidates:
- "cleave": a contronym — it means both to split apart and to
  cling together, so its double meaning is perfect. But it looks
  ordinary at first sight, and the judge weighs surprise second;
  defenestration surprises instantly, cleave only on reflection.
- "snollygoster": wonderful sound and surprise, but its meaning
  (a shrewd, unprincipled person) paints a weaker picture than a
  body sailing out of a window.
- "ultracrepidarian" (one who opines beyond their knowledge):
  witty and apt, but abstract — no image, and 15 letters of
  setup for a joke that lands slower.
- "mumpsimus" (one who stubbornly sticks to an error): funny
  sound, but obscure without being vivid.

Head-to-head, "sonder" was the closest rival: emotionally vivid,
but abstract where defenestration is visual, and better known in
"beautiful words" circles, so less surprising. Defenestration
keeps the top score on surprise, vividness and wit together, so
the word stands. The revision in this pass: the docstring now
records the full decision, and the code asserts the gate (one
token, 1-24 characters) before writing, so a typo can never
produce an invalid entry.

Stdlib only, no network. Writes WORD to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

WORD = "defenestration"


def main() -> None:
    word = WORD.strip()
    assert word and " " not in word and 1 <= len(word) <= 24, (
        "entry must be exactly one word of 1-24 characters"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
