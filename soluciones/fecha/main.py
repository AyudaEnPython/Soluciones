"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from fecha import escribir, comparar, es_fecha


def _validate(fecha: int) -> int:
    if not es_fecha(fecha):
        print("Fecha incorrecta")
        exit(1)
    return fecha


def main():
    a = _validate(int(input("Ingresar primera fecha: ")))
    escribir(a)
    b = _validate(int(input("Ingresar segunda fecha: ")))
    escribir(b)
    print("Menor fecha")
    menor = comparar(a, b)
    if menor == 0:
        print("Las fechas son iguales")
    elif menor == -1:
        escribir(a)
    else:
        escribir(b)


if __name__ == "__main__":
    main()
