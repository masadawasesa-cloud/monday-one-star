#!/usr/bin/env python3
"""Entry for make.fun's "Monday, Reviewed in One Line" bounty.

The whole entry is one line: a one-star review of my Monday. The
verdict is delivered at the security desk — the guard said I looked
much younger in my ID photo, which sounds like a compliment until
the review's last fact lands: the photo was taken on Friday. Three
days is all Monday needed.

Running this program writes that line, word for word, to entry.txt
in the output directory (/output, or $MAKEFUN_OUTPUT_DIR when set).
"""

import os

REVIEW = "My Monday, one star: security said I looked much younger in my ID photo. It was taken on Friday."


def main():
    # The gate takes UTF-8 text of 1 to 200 characters, nothing else;
    # guard the one thing this program promises before writing it.
    assert 1 <= len(REVIEW) <= 200, "the review must fit the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(REVIEW.encode("utf-8"))


if __name__ == "__main__":
    main()
