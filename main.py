"""Famous Last Words at 1 Percent — the funny last words of a phone at 1% battery.

Writes one line (98 characters) to /output/entry.txt.
"""

import os

LINE = "The charger is three feet away. I can see it. I have watched it all day and said nothing. Goodbye."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
