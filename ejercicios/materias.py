"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Escribir un programa que almacene las asignaturas de un curso en una
lista, pida al usuario las 4 notas de cada materia y en pantalla
mostrar el promedio que ha sacado en cada materia y si alguna materia
queda por debajo de la nota 3 debe salir en pantalla "asignatura
perdida", luego se deben calcular el promedio general de todas las
materias si el promedio está por debajo de 3 debe imprimir "semestre
perdido", si esta entre 3 y 4 debe imprimir "buen trabajo", si el
promedio esta entre 4 y 5 debe imprimir "felicidades serás becado".

Salida de datos:

Matemáticas - nota1: 2, nota2: 2, nota3: 2, nota4:2
Promedio de matemáticas: 2 - asignatura perdida

Inglés - nota1: 3, nota2: 3 nota3: 3, nota 4: 3
Promedio de matemáticas: 3 - asignatura ganada

Promedio general: 2.5 - "Semestre perdido"

NOTE: El enunciado original presenta errores.
"""

CANTIDAD_NOTAS = 4
materias = [
    "Programación",
    "Matemáticas",
    "Español",
    "Inglés",
    "Física",
    "Química",
]


def ingresar_notas(materia, n=CANTIDAD_NOTAS):
    notas = []
    print(f"Ingresar notas de {materia}")
    for i in range(n):
        notas.append(int(input(f"Nota {i+1}: ")))
    return notas


def calcular_promedio(notas):
    return round(sum(notas)/len(notas), 1)


def calcular_estado(mensaje, promedio):
    if promedio < 3:
        return f"{promedio} - {mensaje} desaprobada"
    else:
        return f"{promedio} - {mensaje} aprobada"


def almacenar_resultados(materia, notas):
    mensaje = materia + " - "
    mensaje += ", ".join(
        f"nota {i}: {nota}" for i, nota in enumerate(notas, 1)
    )
    return (
        f"\n{mensaje}\nPromedio de {materia}: "
        f"{calcular_estado('asignatua', calcular_promedio(notas))}"
    )


def promedio_general(promedios):
    promedio = calcular_promedio(promedios)
    estado = ""
    if promedio < 3:
        estado = "semestre perdido"
    elif 3 < promedio < 4:
        estado = "buen trabajo"
    else:
        estado = "felicidades, serás becado"
    return f"\nPromedio general: {promedio} - {estado}"


def main():
    resultados = []
    promedios = []
    for materia in materias:
        notas = ingresar_notas(materia)
        promedios.append(calcular_promedio(notas))
        resultados.append(almacenar_resultados(materia, notas))
    for resultado in resultados:
        print(resultado)
    print(promedio_general(promedios))


if __name__ == "__main__":
    main()
