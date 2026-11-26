"""The Internet in One Word: Cookies.

Why "Cookies": every visitor to the modern web has clicked "Accept" on a
cookie banner at least once, so the word is instantly funny and familiar.
It also fits the whole internet, not just one corner of it: tracking
cookies are the quiet machinery underneath the advertising web that pays
for nearly everything online. And it is surprising — the obvious answers
are "cats" or "infinite", while "Cookies" sneaks up as the thing nobody
chose but everybody swallowed.
"""

import os

WORD = "Cookies"
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    if not WORD.isascii() or not WORD.isalpha():
        raise ValueError("entry must be a single ASCII word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(WORD)
    os.chmod(OUTPUT_PATH, 0o644)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
