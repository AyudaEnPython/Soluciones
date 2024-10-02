import re
from random import randint
from typing import List


def _generar_linea() -> List[str]:
    return [
        str(randint(1, 100)).rjust(3, "0") + " " for _ in range(1, 11)
    ]


def generar_archivo(fichero: str) -> None:
    with open(fichero, "w") as f:
        for _ in range(10):
            f.writelines(_generar_linea())
            f.write("\n")


def respaldar_archivo(origen: str, destino: str) -> None:
    with open(origen, "r") as f_origen:
        with open(destino, "w") as f_destino:
            for line in f_origen:
                f_destino.write(line)


def modificar_archivo(fichero: str) -> None:
    np = []
    with open(fichero, "r") as f:
        for line in f:
            for n in line.split():
                if int(n) % 2 == 0:
                    np.append(n.rjust(3, "0"))
    with open(fichero, "r+") as f:
        line = f.read()
        for n in np:
            line = re.sub(str(n), "000", line)
        f.seek(0)
        f.write(line)
        f.truncate()


def mostrar_archivo(fichero) -> None:
    with open(fichero, "r") as f:
        for line in f:
            for n in sorted(int(n) for n in line.split()):
                print(f"{n:03}", sep=" ", end=" ")
            print()


def main():
    generar_archivo("data/numeros.txt")
    mostrar_archivo("data/numeros.txt")
    respaldar_archivo("data/numeros.txt", "data/numeros.bkp")
    modificar_archivo("data/numeros.txt")


if __name__ == "__main__":
    main()
