"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Diseñe un algoritmo que cargue una lista, con las notas de los alumnos
que en total son 10 se pide:
- Unos métodos para cargar las listas necesarias (No recibe en
parámetros, devuelve un valor es decir la lista)
- Un método para cantidad de personas que sacaron 10 (Como desee)
- Un método para cantidad de regulares (Como desee)
- Un método para el promedio general (Como desee)
- Un método para indicar cual es el porcentaje de alumnos excelentes (
    Como desee)

* Para estar regular el alumno deberá cumplir que la nota sea mayor o
    igual a 5
* Al probar el código, cambie por cantidad menor

NOTE: el enunciado original presenta errores.
TODO: add typing later...
"""

CANTIDAD_ALUMNOS = 10
MAXIMA_NOTA = 10
UMBRAL_REGULAR = 5


def ingresar_datos(n=CANTIDAD_ALUMNOS):
    notas = []
    for i in range(n):
        notas.append(int(input(f"Ingresar nota del alumno N°{i+1:02}: ")))
    return notas


def notas_maxima(notas):
    return sum(1 for nota in notas if nota == MAXIMA_NOTA)


def regulares(notas):
    return sum(1 for nota in notas if nota > UMBRAL_REGULAR)


def promedio(notas):
    return sum(notas)/len(notas)


def porcentaje(notas):
    return notas_maxima(notas)*(100/CANTIDAD_ALUMNOS)


def main():
    notas = ingresar_datos()
    print("\nResultados:")
    print(f"Personas que sacaron 10: {notas_maxima(notas)}")
    print(f"Cantidad de regulares: {regulares(notas)}")
    print(f"Promedio general: {promedio(notas)}")
    print(f"Porcentaje de alumnos excelentes: {porcentaje(notas)}%")


if __name__ == "__main__":
    main()
