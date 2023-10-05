"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.

output:
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
"""
from prototools import time_functions


def f(n, s=""):
    k = -1
    for i in range(1, n):
        s += str(i)
        if i % 2 != 0:
            k += 1
            print(s[k-i:])


def g(n):
    print("",*[col if col<(2*lin) else "\n" for lin in range(1,6) for col in range(lin,2*lin+1) ])


if __name__ == "__main__":
    fs = {"f": f, "g": g}
    time_functions(fs, args=(10), globals=globals(), number=100)
