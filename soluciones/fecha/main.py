"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from fecha import escribir, comparar, es_fecha


def _f(fecha: int) -> int:
    if not es_fecha(fecha):
        print("Fecha incorrecta")
        exit(1)
    return fecha


def main():
    a = _f(int(input("Ingresar primera fecha: ")))
    escribir(a)
    b = _f(int(input("Ingresar segunda fecha: ")))
    escribir(b)
    fechas = [None, a, b]
    print("Menor fecha")
    menor = comparar(a, b)
    if menor == 0:
        print("Las fechas son iguales")
    else:
        escribir(fechas[menor])


if __name__ == "__main__":
    main()
