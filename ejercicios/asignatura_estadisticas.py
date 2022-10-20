"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Para la primera prueba de la asignatura, por cada uno de los alumnos
que rindieron la prueba (120 alumnos) se ha recolectado el nombre, su
nota, la sede y el sexo. El ingreso de los datos debe ingresar el
usuario y antes de procesar cualquier información el algoritmo debe
validar:
- Que la nota sea mayor o igual que 10 y menor o igual que 70.
- Que la sede sea un valor desde el 1 hasta 26.
- Que el valor de sexo sea ("F" o "M").

Confeccione un algoritmo que valide la información de acuerdo a las
reglas anteriores y genere las siguientes estadísticas:
- El nombre del alumno que saco la mayor y menor nota.
- Cuantos alumnos de sexo masculino tuvieron una nota superior a 45.
- Cuantos alumnos de las sedes 1 y 22 estuvieron bajo el 30.

NOTE: add typing later...
"""
# pip install prototools
from prototools import int_input, float_input, menu_input

N = 120


def _f(f, data):
    return f(data, key=lambda x: x[1])


def nota_superior(data, x=45, g="M"):
    return sum(1 for _, n, _, s in data if n > x and s == g)


def por_sede_inferior(data, x=30):
    return sum(1 for _, n, s, _ in data if n < x and (s == 1 or s == 22))


def max_min(data):
    return _f(max, data)[0], _f(min, data)[0]


def _ingresar():
    nombre = input("Nombre: ")
    nota = float_input("Nota: ", min=10, max=70)
    sede = int_input("Sede: ", min=1, max=26)
    genero = menu_input(("M", "F"), numbers=True)
    return nombre, nota, sede, genero


def ingresar():
    datos = []
    for _ in range(N):
        datos.append(_ingresar())
    return datos


def main():
    datos = ingresar()
    max_, min_ = max_min(datos)
    print(f"Alumno con mayor nota: {max_}")
    print(f"Alumno con menor nota: {min_}")
    print(f"Varones con nota superior a 45: {nota_superior(datos)}")
    print(f"Debajo de 30 en las sedes 1 y 22: {por_sede_inferior(datos)}")


if __name__ == "__main__":
    main()
