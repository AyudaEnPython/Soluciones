"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List, Tuple

FILENAME = "data.txt"
_D: Dict[str, int] = {"N": -1, "S": 1, "E": 1, "O": -1}
_T: str = "Nos movemos al {} {} pasos, estando ahora en la posicion {},{}."


def read_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            s, x = line.split()
            data.append((_D[s] * int(x)))
    return data


def _print(ss: Tuple[str, str], n: int, x: int, y: int) -> None:
    a, b = ss
    orientation = a if n > 0 else b
    print(_T.format(orientation, abs(n), x, y))


def sol(data: List[int]) -> None:
    pos = {"x": 0, "y": 0}
    for i in range(len(data)):
        n = data[i]
        if i % 2 == 0:
            pos["x"] += n
            _print(("este", "oeste"), n, pos["x"], pos["y"])
        else:
            pos["y"] += n
            _print(("sur", "norte"), n, pos["x"], pos["y"])
    print("Posición final del tesoro: {} {}.".format(pos["x"], pos["y"]))


def main():
    data = read_data(FILENAME)
    sol(data)


if __name__ == "__main__":
    main()
