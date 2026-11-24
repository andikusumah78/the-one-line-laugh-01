#!/usr/bin/env python3
"""The One-Line Laugh — one funny line, written to /output/entry.txt.

Pure stdlib Python 3.13, no network, deterministic. The line is a single
sentence of 111 characters (113 UTF-8 bytes), inside the 1-200 gate.
"""

import os

LINE = (
    "My smart fridge just sent me a breakup text \u2014 apparently I have "
    "been cheating on it with the food delivery app."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
