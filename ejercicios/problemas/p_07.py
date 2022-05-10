"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import sin, cos


def solver(r: float, theta: float) -> float:
    return r * cos(theta), r * sin(theta)


def main():
    r = 13
    theta = 0.3944444 # 22.6°
    print(solver(r, theta))


if __name__ == "__main__":
    main()
