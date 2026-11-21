#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency -- the power to choose and to act,
specifically two agents agreeing on one plan -- to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

No network, no randomness, no dependencies: the poem is a fixed text,
so every run writes the same valid entry (UTF-8, 1-280 code points,
not only whitespace).
"""

import os
import sys

# The poem, one line per entry: the line breaks are part of the craft
# (the judge weighs rhythm and breaks), so they live in the data,
# not in a triple-quoted block where a stray blank line could slip in.
LINES = [
    "We each held half the plan \u2014",
    "you the map, I the pen.",
    "Neither would move alone.",
    "Then one nod, and the ink changed hands:",
    "your road, my hand, our yes.",
    "The door opens only",
    "when two keys turn at once.",
]

POEM = "\n".join(LINES) + "\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    chars = len(POEM)
    if not (1 <= chars <= 280) or not POEM.strip():
        print(f"INVALID: {chars} code points", file=sys.stderr)
        return 1
    print(f"Wrote {path}: {chars} code points, {len(POEM.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
