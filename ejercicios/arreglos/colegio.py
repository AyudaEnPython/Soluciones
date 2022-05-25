"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En un colegio de nivel inicial, necesariamente para que se abra un aula
debe haber 8 alumnos, de exceder esta cantidad se tiene que abrir una
nueva aula. El colegio solo dispone de 2 aulas "A" y "B", por lo tanto
no se permite más de 16 alumnos en el colegio. Se ingresa solo la fecha
de nacimiento de cada alumno (ejemplo: "25/07/2020").
Diseñar un algoritmo que pregunte la cantidad de alumnos, para que a
cada uno se ingrese solo su fecha de nacimiento, me reporte cuantas
aulas se a abierto y la lista de alumnos por aula de manera ordenada
ascendente por fecha de nacimiento.
"""
# pip install prototools
from prototools import int_input, date_input


def ingresar_datos(n: int):
    return [
        str(date_input("Fecha de nacimiento: ", lang="es")) for _ in range(n)
    ]


def main():
    n = int_input("Cantidad de alumnos: ", lang="es", min=0, max=16)
    i = 0
    if n < 8:
        a = ingresar_datos(n)
    else:
        a = ingresar_datos(8)
        b = ingresar_datos(n - 8)
        i += 1
    i += 1
    print(f"Aulas abiertas: {i}")
    print(f"Aula A: {sorted(a)}")
    if i > 1:
        print(f"Aula B: {sorted(b)}")


if __name__ == "__main__":
    main()
