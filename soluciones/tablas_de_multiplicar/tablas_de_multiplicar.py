"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import int_input

MIN, MAX = 1, 10
FILENAME = "tabla-{}.txt"


def _linea(n: int, m: int) -> str:
    return f"{n:>02} x {m:>02} = {n * m:>02}"


def _tabla(n: int) -> str:
    return "\n".join([_linea(n, i) for i in range(MIN, MAX+1)])


def write(n: int) -> None:
    with open(FILENAME.format(n), "w") as f:
        f.write(_tabla(n))


def read(n: int, m: int) -> str:
    try:
        with open(FILENAME.format(n), "r") as f:
            for i, line in enumerate(f, 1):
                if i == m:
                    return line.replace("\n", "")
    except FileNotFoundError:
        return "No existe el archivo"


def main():
    tabla = int_input("Tabla del: ", min=MIN, max=MAX)
    linea = int_input("Linea: ", min=MIN, max=MAX)
    print(read(tabla, linea))


if __name__ == "__main__":
    main()
