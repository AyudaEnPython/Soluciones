"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que solicite ingresar la nota de 10 alumnos, el
programa debe informar cuantos han aprobado, reprobado, nota promedio,
la mayor y la menor.
"""
from typing import List

UMBRAL = 4
DESTACADO = 7


def ingresar_notas(n: int = 10, min_: int = 0, max_: int = 10) -> List[int]:
    """Solicita las notas de 'n' alumnos.

    :param n: Cantidad de alumnos.
    :param min_: Valor mínimo de la nota.
    :param max_: Valor máximo de la nota.
    :n type: int
    :min_ type: int
    :max_ type: int
    :return: Lista con las notas de los alumnos.
    :rtype: list
    """
    notas = []
    i = 0
    while i < n:
        nota = input(f'[{i+1}] Ingrese la nota: ')
        try:
            nota = int(nota)
        except ValueError:
            print('La nota debe ser un número.')
            continue
        if min_ <= nota <= max_:
            notas.append(nota)
            i += 1
        else:
            print('Nota fuera de rango')
    return notas


def main():
    notas = ingresar_notas()
    aprobados = list(filter(lambda x: x >= UMBRAL, notas))
    desaprobados = list(filter(lambda x: x < UMBRAL, notas))
    notables = list(filter(lambda x: x > DESTACADO, notas))
    promedio = sum(notas) / len(notas)
    print(f'Aprobados: {len(aprobados)}')
    print(f'Desaprobados: {len(desaprobados)}')
    print(f'Notables: {len(notables)}')
    print(f'Promedio: {promedio}')


def main_alt(): # hardcoded
    aprobados = desaprobados = notables = 0
    promedio = i = 0
    while i < 10:
        nota = input(f'[{i+1}] Ingrese la nota: ')
        try:
            nota = int(nota)
            if 0 <= nota <= 10:
                if nota >= 4:
                    aprobados += 1
                else:
                    desaprobados += 1
                if nota > 7:
                    notables += 1
                promedio += nota
                i += 1
            else:
                print('Nota fuera de rango')
        except ValueError:
            print('La nota debe ser un número.')
            continue
    promedio /= 10
    print(f'Aprobados: {aprobados}')
    print(f'Desaprobados: {desaprobados}')
    print(f'Notables: {notables}')
    print(f'Promedio: {promedio}')


if __name__ == '__main__':
    # main()
    main_alt()
