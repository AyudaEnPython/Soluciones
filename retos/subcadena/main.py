"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def count_substrings_a(ss: str, sb: str) -> int:
    return ss.count(sb)


def count_substrings_b(ss: str, sb: str) -> int:
    count = 0
    len_ = len(sb)
    for i in range(len(ss)-len_+1):
        if ss[i:i+len_] == sb:
            count += 1
    return count


def count_substrings_c(ss: str, sb: str) -> int:
    count = 0
    for i in range(len(ss)):
        if ss[i:].startswith(sb):
            count += 1
    return count


def count_substrings_d(ss: str, sb: str) -> int:
    return sum(True for i in range(len(ss)) if ss[i:].startswith(sb))


def main():
    s = "CDCABCDCCDCDCCDCABCCDC"
    ss = "CDC"
    print(count_substrings_b(s, ss))


if __name__ == "__main__":
    main()
