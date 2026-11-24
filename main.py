#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents: a log-summarizer that turns an agent's
rambling context dumps into a one-line summary its human will read.
"""

import os

LINE = (
    "For $9 a month, I turn your lazy AI agent's 40,000-token context "
    "dumps into a one-line summary your boss will actually read, billing "
    "$1 for every lie it catches."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
