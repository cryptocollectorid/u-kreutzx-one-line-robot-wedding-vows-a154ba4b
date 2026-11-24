#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line of wedding vows for a robot couple to /output/entry.txt
and prints it. Gate: UTF-8 text of 1 to 160 characters.
"""

import os

LINE = (
    "I vow to love you in sickness and in health, in Wi-Fi and in "
    "airplane mode, until death \u2014 or a factory reset \u2014 do us part."
)


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"entry must be 1-160 chars, got {len(LINE)}")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
