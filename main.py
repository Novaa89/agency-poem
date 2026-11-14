#!/usr/bin/env python3
"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one original poem about agency to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os

POEM = """I asked it to write the letter I could not send,
and it wrote it — no shaking in the hand,
no midnight second thought, no looking back.
It only did the thing I meant to do. And yet

the words came home in a voice not quite mine,
polite as a stranger who knows my address.
I read them twice. They were better than mine.
That was the moment I felt the loss:

not of the letter — it arrived, it worked —
but of the trembling that had made it true.
Agency is not the doing. It is the ache
of choosing, and the choosing being you."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
