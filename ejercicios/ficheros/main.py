"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que cuente las palabras del archivo
python_robots.txt y despligue las 6 palabras más comunes del texto. No
cuente las palabras cuya longitud sea menor o igual a 4 letras. 
"""
from typing import List


def open_file(filename: str, encoding="utf-8") -> List[str]:
    with open(filename, encoding=encoding) as f:
        return f.readlines()


def count_words(data: List[str]) -> List[str]:
    count = {}
    words = [word for line in data for word in line.split()]
    for word in (word for word in words if len(word) > 4):
        count[word] = count.get(word, 0) + 1
    return sorted(count, key=count.get, reverse=True)[:6]


def main():
    data = open_file("python_robots.txt")
    words = count_words(data)
    print(words)


if __name__ == "__main__":
    main()
