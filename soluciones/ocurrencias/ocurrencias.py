"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import Counter
from typing import List, Generator


def _read_data(file: str) -> Generator[str, None, None]:
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def _write_data(file: str, data: List[str]) -> None:
    with open(file, 'w', encoding="utf-8") as f:
        for line in data:
            f.write(line)
            f.write('\n')


def contar_vocales(data: Generator[str, None, None]) -> Counter:
    resultado = Counter()
    for line in data:
        resultado += Counter(c for c in line if c in "aeiou")
    return resultado


def _sort(result: Counter) -> List[str]:
    return sorted([f"{k} {v}" for k, v in result.items()])


def main():
    data = _read_data("soluciones/ocurrencias/origen.txt")
    resultado = contar_vocales(data)
    data = _sort(resultado)
    _write_data("soluciones/ocurrencias/destino.txt", data)


if __name__ == '__main__':
    main()
