#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """Open, write and return number character to stdout"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
