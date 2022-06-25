"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List


def read_file(filename: str) -> List[str]:
    with open(f"{filename}.txt", "r") as f:
        return f.read().splitlines()


def cleanup(data: List[str]) -> List[str]:
    t = []
    for line in data:
        for c in line.split(" "):
            try:
                c = float(c)
                t.append(c)
            except ValueError:
                pass
    return t


def main():
    filename = input("> ")
    try:
        data = read_file(filename)
        data = cleanup(data)
        print(f"Suma de puntos {sum(data)}")
    except FileNotFoundError:
        print("Archivo no encontrado!")
        return


if __name__ == "__main__":
    main()
