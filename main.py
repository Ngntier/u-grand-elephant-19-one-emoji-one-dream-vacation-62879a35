"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: SUNRISE (U+1F305),
a golden sun rising over the ocean -- pure wanderlust, a postcard
at a glance. Pure stdlib, deterministic, no trailing newline.
"""

import os

EMOJI = "\U0001F305"  # SUNRISE


def main():
    # Gate guard: exactly one character, within the 1-8 char gate,
    # and not only whitespace.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
