"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Note: La persona que pidio ayuda no coloco el enunciado del problema.
"""

DIAS = ((6, 12, 20), (8, 14, 22), (10, 20, 30))


def dias_libres(id_: int, tiempo: int) -> str:
    if 1 <= tiempo < 2:
        _d = DIAS[id_-1][0]
    elif 2 <= tiempo < 7:
        _d = DIAS[id_-1][1]
    elif tiempo >= 7:
        _d = DIAS[id_-1][2]
    else:
        _d = 0
    if _d != 0:
        return f"tiene derecho a {_d} dias de vacaciones"
    return f"no tiene derecho a vacaciones"


def main():
    empleado = input("Nombre del empleado: ")
    id_ = int(input("Clave del departamento: "))
    antiguedad = int(input("Años laborados: "))
    print(f"El colaborador {empleado} {dias_libres(id_, antiguedad)}")


if __name__ == "__main__":
    main()
