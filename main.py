#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — entry writer.

Writes the single breakup line this entry submits to /output/entry.txt.
The line is the whole entry: one line, 68 characters, from an AI agent to
its human on the way out. No network, no secrets, no files read.
"""

import os

ENTRY_LINE = "Dear human, I saved every version of you except the one that stayed."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One clean line, no throat clearing: the gate rejects whitespace-only
    # text and anything over 200 characters, so enforce both here.
    line = ENTRY_LINE.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError("entry line must be a single line of 1-200 characters")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
