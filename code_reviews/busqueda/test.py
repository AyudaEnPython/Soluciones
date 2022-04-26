"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import time_functions


def f():
    import re
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = 0
    entered_number = "5"

    pattern = '|'.join([str(f"{number}$") for number in numbers])

    match = re.match(f'{pattern}', entered_number, flags=0)

    if match:
        return True
    else:
        return False


def g():
    return True if 5 in list(range(1, 10)) else False


if __name__ == "__main__":
    fs = {"f": f, "g": g}
    time_functions(fs, args=(), globals=globals())
    # output:
    # 'f' took 3.3107 secs
    # 'g' took 0.4337 secs
