"""Entry for make.fun's "The Long Roast" bounty.

The satire: a committee of lawmakers votes to regulate artificial
intelligence, yet spends forty minutes failing to unmute itself on a
video call and ends up printing the bill so it can be faxed, because
the PDF was "doing something weird" -- a jab at regulators who would
govern technology they cannot operate at the most basic level.
"""

import os

ENTRY = "The committee voted to regulate artificial intelligence right after spending forty minutes trying to unmute itself, then printed the bill to fax it, because the PDF was, quote, doing something weird."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
