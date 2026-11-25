#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name to /output/entry.txt.

The name: "SheTookTheKidsAndTheRouter" (26 characters).

Why it works as a whole story in one line:
  - Situation: a household split / divorce.
  - Characters: "she" (the ex, who left) and the narrator left behind.
  - Event: she took the kids — and, in the same breath, the router.
  - Punchline: the router is listed alongside the children, as if it
    ranked among the family's most precious possessions. The narrator
    is left with neither kids nor Wi-Fi, and the deadpan inventory
    order is the joke. Fresh — not a recycled stock Wi-Fi gag.
"""

import os

NAME = "SheTookTheKidsAndTheRouter"


def main() -> None:
    assert 1 <= len(NAME) <= 32, f"name is {len(NAME)} chars, must be 1-32"
    assert NAME.strip(), "name must not be whitespace-only"
    # No randomness, no I/O besides the single output file: the same
    # 26 characters are written on every run, byte for byte.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
