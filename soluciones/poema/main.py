"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
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


def analizar(data: Generator[str, None, None]) -> str:
    result = []
    for line in data:
        for word in line.split():
            if len(word) > 6 and word not in result:
                result.append(word)
    return result


def main():
    data = _read_data('poema.txt')
    data = analizar(data)
    _write_data('palabras.txt', data)


if __name__ == '__main__':
    main()