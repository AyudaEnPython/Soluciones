"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Hacer un programa que pida al usuario la cantidad de alumnos de un
colegio y que luego pregunta los alumnos que hay en las siguientes
categorías:

- Alumnos de menos de 40 kg.
- Alumnos de 40 a 50 kg.
- Alumnos de más de 50 kg y menos de 60 kg.
- Alumnos de más o igual a 60 kg.

El programa deberá mostrar el porcentaje de alumnos correspondiente a
cada categoría.

NOTE: No es tan claro el enunciado, se opta por implementar dos
    soluciones distintas (sin ingresar pesos e ingresándolos).
"""
from prototools import int_input, float_input


labels = (
    "menos de 40 kg",
    "entre 40 a 50 kg",
    "más de 50 kg y menos de 60 kg",
    "más o igual a 60 kg",
)


def main_sin_ingresar_pesos():
    data = [0, 0, 0, 0]
    n = int_input("Ingrese la cantidad de alumnos: ", min=0)
    for i in range(len(labels)):
        data[i] = float_input(f"Ingresar la cantidad de alumnos de {labels[i]}: ")
    porcentajes = [data[i] / n * 100 for i in range(len(data))]
    for i in range(len(labels)):
        if porcentajes[i] > 0:
            print(f"El {porcentajes[i]:.2f}% pesa {labels[i]}")


def main_ingresando_pesos():
    data = {k:v for k, v in zip(range(4), [0, 0, 0, 0])}
    n = int_input("Ingrese la cantidad de alumnos: ", min=0)
    for _ in range(n):
        peso = float_input("Ingrese el peso del alumno: ")
        if peso < 40:
            data[0] += 1
        elif peso < 50:
            data[1] += 1
        elif peso < 60:
            data[2] += 1
        else:
            data[3] += 1
    for k, v in data.items():
        porcentaje = v / n * 100
        if porcentaje > 0:
            print(f"El {porcentaje:.2f}% pesa {labels[k]}")


if __name__ == "__main__":
    main_sin_ingresar_pesos() # comment/uncomment to switch between 'mains'
    #main_ingresando_pesos()
