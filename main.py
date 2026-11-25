"""The Best Meal You Ever Had — make.fun entry.

One sentence, at most 200 characters, about the best meal ever had.
The program writes it to /output/entry.txt for the judge.

The memory is a single sentence in two beats: the setup names the
place and the hour, the punch names the meal and why nothing since
has matched it.

The sentence is kept as two constants (SETUP + PUNCH) and assembled
by build_line(); the emitted bytes are the original 175-character
line, unchanged — only the code shape changed.
"""

import os

SETUP = "At two in the morning on a Hanoi train platform, I ate instant noodles with a plastic fork that kept bending,"
PUNCH = "and no restaurant meal since has tasted as good as those noodles."

MAX_CHARS = 200


def resolve_out_dir():
    """Where the judge expects entry.txt; overridable for local runs."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def parts():
    """The sentence's two beats, in order."""
    return (SETUP, PUNCH)


def build_line():
    """Join the two beats of the sentence into the final line."""
    return " ".join(parts())


def validate(line):
    """The brief caps the sentence at 200 characters."""
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the 200-char cap" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if not line.endswith("."):
        raise ValueError("line must end with a full stop")
    return line


def emit(line, out_dir):
    """Write the line exactly as built, with no trailing newline."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main():
    line = validate(build_line())
    emit(line, resolve_out_dir())


if __name__ == "__main__":
    main()
