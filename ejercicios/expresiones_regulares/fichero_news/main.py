"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Lea el archivo news.txt y, utilizando expresiones regulares, imprima
las líneas que comiencen con un número y terminen con un punto. El
resultado de la impresión debe comenzar de la siguiente forma:

    +-------------------------------+
    |4 hours ago.                   |
    |1 day.                         |
    |.                              |
    |.                              |
    |.                              |
    +-------------------------------+
"""
import re
from typing import List


def open_file(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return f.readlines()


def print_search(pattern: str, data: List[str]) -> None:
    for line in data:
        if re.match(pattern, line):
            print(line.rstrip())


def main():
    data = open_file("news.txt")
    print_search(r'^\d.*\.$', data)


if __name__ == '__main__':
    main()
