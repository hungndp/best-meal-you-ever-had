"""The Best Meal You Ever Had — make.fun entry.

One sentence, at most 200 characters, about the best meal ever had.
The program writes it to /output/entry.txt for the judge.
"""

import os

TEXT = "At two in the morning on a Hanoi train platform, I ate instant noodles with a plastic fork that kept bending, and no restaurant meal since has tasted as good as those noodles."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
