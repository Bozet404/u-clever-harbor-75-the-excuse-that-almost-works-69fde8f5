#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt.

The excuse is one line of plain text, at most 20 words, written like a
real text a gamer sends the boss in a hurry to skip work on GTA 6
launch week: a specific, boring, believable detail, no setup, no
explanation, no signature.
"""

import os

EXCUSE = "My root canal got moved to 9am today, I'll be drooling till lunch then catch up from home."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
