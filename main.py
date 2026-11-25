#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the moon's one-line comeback to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no environment reads.
The line is a fixed constant below; the program only writes it out.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "You wish on me every night. I'm a rock. I don't grant wishes. "
    "I just sit here, glowing, judging your life choices in silence."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
