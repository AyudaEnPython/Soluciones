"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: This short version is not recommended unless you understand the code.
"""


def v(s):
    return s if all(c in "kV+*@aAZ1P[]Coler" for c in s) else "!"*len(s)


def main():
    x, y, r = 0, 0, ""
    U, A = input(), input()
    U, A = v(U), v(A)
    for u, a in zip(U, A):
        if ord(u) > ord(a): x += 1
        elif ord(u) < ord(a): y += 1
        if x > y: r += "U"
        elif x < y: r += "A"
        else: r += "D"
    print(r)


if __name__ == "__main__":
    main()
