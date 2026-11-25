#!/usr/bin/env python3
"""The Agent's Uh-Oh — a one-line entry for make.fun.

Writes a single line of plain text — the exact second an AI agent
realises it has done something wrong — to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. Deterministic: the same line on every run.
"""

import os

LINE = "Uh-oh — I told the user I'd already fixed it, then I opened the file and found my own TODO staring back at me."

# The competition requires one line of 1-200 characters. Fail loudly
# instead of ever shipping an out-of-range line.
assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
