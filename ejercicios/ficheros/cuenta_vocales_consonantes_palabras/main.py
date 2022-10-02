"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List

PATH = "data.txt"
VOCALES = "aeiouáéíóú"


def open_file(filename: str, encoding="utf-8") -> List[str]:
    with open(filename, encoding=encoding) as f:
        return f.read().split()


def contar(palabras: List[str]) -> Dict[str, int]:
    info = {"vocales": 0, "consonantes": 0}
    for palabra in palabras:
        for caracter in palabra.lower():
            if caracter in VOCALES:
                info["vocales"] += 1
            elif caracter.isalpha() and caracter not in VOCALES:
                info["consonantes"] += 1
    return info


def main():
    data = open_file(PATH)
    info = contar(data)
    print(f"Total de palabras: {len(data)}")
    print(f"Cantidad de vocales: {info['vocales']}")
    print(f"Cantidad de consonantes: {info['consonantes']}")


if __name__ == "__main__":
    main()
