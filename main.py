#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt and nothing else:
a single U+1F979 character, 4 UTF-8 bytes, no trailing newline,
no words, no caption, no explanation.

Standard library only. The output directory is created when it
does not exist and is never deleted or recreated.
"""

import os

EMOJI = "\U0001F979"  # U+1F979, exactly 4 UTF-8 bytes (F0 9F A5 B9), nothing else
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
