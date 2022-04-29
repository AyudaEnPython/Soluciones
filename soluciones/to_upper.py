"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def to_upper(s: str) -> str:
    return "".join(chr(ord(c) ^ 0x20) for c in s)
