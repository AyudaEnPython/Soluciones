"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Dada la siguiente matriz de números compuestos:

    +-------------------------------------------------------+
    | compues = [[8 , 9, 14, 15, 16, 18, 4, 6, 10, 12 ],    |
    |            [21 , 22, 25, 26, 27, 20, 24] ,            |
    |            [34 , 28, 32, 33, 30, ],                   |
    |            [38 , 39, 42, 44, 35, 36, 40] ,            |
    |            [52 , 54, 45, 48, 49, 50, 51, 46 ]]        |
    +-------------------------------------------------------+

Escribe un programa que realice lo siguiente:
- Ordenar los números de cada lista en forma ascendente.
- Imprimir las listas ordenadas.
- Imprimir el máximo número de cada lista.

Para ordenar los números de cada lista, en forma ascendente, implemente
y use la siguiente función:
- ordenar_matriz recibe como parámetro una matriz compues, e implemente
    un algoritmo para ordenar las listas en forma ascendente.

Restricciones: No puede utilizar las funciones sort, min y max.

El resultado de la ejecución del programa es el siguiente:

    +-------------------------------------------------------+
    | [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]                  |
    | [20 , 21, 22, 24, 26, 27]                             |
    | [28 , 30, 32, 33, 34]                                 |
    | [35 , 36, 38, 39, 40, 42, 44]                         |
    | [45 , 46, 48, 49, 50, 51, 52, 54]                     |
    | 18                                                    |
    | 27                                                    |
    | 34                                                    |
    | 44                                                    |
    | 54                                                    |
    +-------------------------------------------------------+

# ---------------------------------------------------------------------
NOTE: El enunciado original tiene varios errores y contiene partes
    redundantes.
"""
# Algoritmo de ordenación merge
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_merge.py


def merge(left, right):
    merged_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list


def merge_sort(lista):
    length = len(lista)
    if length <= 1:
        return lista
    mid = length // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)


def ordenar_matriz(matriz):
    return [merge_sort(fila) for fila in matriz]


def main():
    compuesto = [
        [8, 9, 14, 15, 16, 18, 4, 6, 10, 12],
        [21, 22, 25, 26, 27, 20, 24],
        [34, 28, 32, 33, 30],
        [38, 39, 42, 44, 35, 36, 40],
        [52, 54, 45, 48, 49, 50, 51, 46]
    ]
    ordenado = ordenar_matriz(compuesto)
    for fila in ordenado:
        print(fila)
    for fila in ordenado:
        print(fila[-1])


if __name__ == '__main__':
    main()
