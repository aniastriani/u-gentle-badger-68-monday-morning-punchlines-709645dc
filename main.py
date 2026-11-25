"""Monday Morning Punchlines: one joke, at most 200 characters.

A tiny pure-stdlib program. It writes a single joke about Monday
mornings -- no more than 200 characters -- to entry.txt in the output
directory the grader provides, so a judge can compare it two at a time
against the rest of the field.
"""

import os

JOKE = (
    "Monday morning, my alarm clock apologized before ringing -- it had "
    "already read my calendar and refused to be the bearer of bad news."
)


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    assert "\n" not in line, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
