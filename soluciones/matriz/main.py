"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Union

Matrix = List[List[Union[int, float]]]


def _determinante(arr: Matrix) -> Union[int, float]:
    if len(arr) == 1:
        return arr[0][0]
    else:
        det = 0
        for i in range(len(arr)):
            det += arr[0][i] * (-1) ** i * _determinante(
                [
                    [arr[j][k] for k in range(len(arr)) if k != i]
                    for j in range(1, len(arr))
                ]
            )
        return det


def determinante(arr: Matrix) -> Union[int, float]:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            f = arr[j][i] / arr[i][i]
            for k in range(i, len(arr[i])):
                arr[j][k] -= f * arr[i][k]
    d = 1
    for i in range(len(arr)):
        d *= arr[i][i]
    return d


if __name__ == "__main__":
    import numpy as np
    arr: Matrix = [
        [1, 2, 4],
        [3, 4, 7],
        [5, 6, 7],
    ]
    assert _determinante(arr) == determinante(arr) == np.linalg.det(arr)
