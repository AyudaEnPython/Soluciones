"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import sin, cos, pi


def solver() -> float:
    return (1 - sin(pi/4) * cos(pi)**4) / (1 + cos(pi)**2)


def main():
    print(f"{solver():.4f}")


if __name__ == "__main__":
    main()
