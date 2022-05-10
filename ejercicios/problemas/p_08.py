"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def solver(n: int) -> int:
    return sum([(-1)**(i+1) * (i/2**i) for i in range(1, n+1)])


def main():
    print(solver(200)) # 0.2222...


if __name__ == "__main__":
    main()
