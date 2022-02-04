"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Generar las notas de 5 estudiantes, en 6 asignaturas, durante 4 cursos.
Mostrar en pantalla los datos de forma que seleccionando un elemento
lo muestre según su curso, asignatura o compañeros.

NOTA: cursos se refiere a un periodo académico (por ejemplo bimestre o 
    semestre) y asignaturas a una materia.
    Las calificaciones pueden variar (0 a 10, 0 a 20, 0 a 100, etc.).
    No se precisa con exactitud el como mostrar los datos.
"""
from random import randint
from typing import Dict, List, Tuple
# pip install prototools
from prototools import Menu, int_input, choice_input

Data = List[Dict[str, Dict[str, int]]]
PERIODO = 4
RANGO = 0, 10
ASIGNATURAS = "Arte", "Historia", "Lenguaje", "Matemáticas", "Química"
ESTUDIANTES = "Jason", "Joe", "Paul", "Steve", "Yngwie"


def generar_notas() -> Data:
    return [
        {estudiante:
            {asignatura:randint(*RANGO) for asignatura in ASIGNATURAS}
            for estudiante in ESTUDIANTES}
        for _ in range(PERIODO)
    ]


def _helper(msg: str, data: Tuple[str]) -> Tuple[int, str]:
    int_value = int_input(msg, min=1, max=PERIODO)
    str_value = choice_input(data)
    return int_value, str_value


def por_periodo(notas: Data) -> None:
    periodo = int_input("Periodo: ")
    print(f"\nNotas del periodo {periodo}:")
    notas = notas[periodo - 1]
    for estudiante, asignaturas in notas.items():
        print(f"{estudiante:>8} -> ", end="")
        for asignatura, calificacion in asignaturas.items():
            print(f"{asignatura}: {calificacion:2d}", end="| ")
        print()


def por_asignatura(notas: Data) -> None:
    periodo, asignatura = _helper("Periodo: ", ASIGNATURAS)
    print(f"\nNotas de la asignatura {asignatura} en el periodo {periodo}:")
    notas = notas[periodo - 1]
    for estudiante, calificacion in notas.items():
        print(f"{estudiante}: {calificacion[asignatura]}", end="| ")
    print()


def por_estudiante(notas: Data) -> None:
    periodo, estudiante = _helper("Periodo: ", ESTUDIANTES)
    print(f"\nNotas del estudiante {estudiante} en el periodo {periodo}:")
    notas = notas[periodo - 1]
    for asignatura, calificacion in notas[estudiante].items():
        print(f"{asignatura}: {calificacion}", end="| ")
    print()


def main():
    notas = generar_notas()
    menu = Menu()
    menu.add_options(
        ("Mostrar notas por periodo", lambda: por_periodo(notas)),
        ("Mostrar notas de una asignatura", lambda: por_asignatura(notas)),
        ("Mostrar notas de un estudiante", lambda: por_estudiante(notas)),
    )
    menu.run()


if __name__ == "__main__":
    main()
