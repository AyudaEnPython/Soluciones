"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solución completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/aprobados_desaprobados.py

Escribir un programa que solicite ingresar la nota de 10 alumnos, el
programa debe informar cuantos han aprobado, reprobado, nota promedio,
la mayor y la menor.
"""
UMBRAL, DESTACADO = 4, 7


def ingresar_notas(n=10, min_=0, max_=10):
    notas, i = [], 0
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
    print(f'Aprobados: {len(list(filter(lambda x: x >= UMBRAL, notas)))}')
    print(f'Desaprobados: {len(list(filter(lambda x: x < UMBRAL, notas)))}')
    print(f'Notables: {len(list(filter(lambda x: x > DESTACADO, notas)))}')
    print(f'Promedio: {sum(notas) / len(notas)}')


if __name__ == '__main__':
    main()