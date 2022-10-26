"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def pigeonhole(arr):
    min_ = min(arr)
    max_ = max(arr)
    size = max_ - min_ + 1
    holes = [0] * size
    for x in arr:
        holes[x - min_] += 1
    i = 0
    for k in range(size):
        while holes[k] > 0:
            holes[k] -= 1
            arr[i] = k + min_
            i += 1
