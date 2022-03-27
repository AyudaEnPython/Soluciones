"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] == x:
            return mid
        elif arr[mid][0] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
