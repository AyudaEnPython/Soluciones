"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


# Pregunta 1
def promedio_std(lista):
    mean_ = sum(lista) / len(lista)
    std_ = (sum((x - mean_) ** 2 for x in lista) / len(lista)) ** 0.5
    return mean_, round(std_, 3)


# Pregunta 2
def color_frecuente(lista):
    _p = ["azul", "rojo", "verde", "amarillo"]
    d = {}
    for c in lista:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return max(
        sorted(list(d.items()), key=lambda x: (_p.index(x[0]))),
        key=lambda x: x[1],
    )


# Pregunta 3
def buscaminas(tablero, i, j):
    bombas = 0
    for x, y in (
        (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)
    ):
        if 0 <= i + x < len(tablero) and 0 <= j + y < len(tablero[0]):
            if tablero[i + x][j + y] == "X":
                bombas += 1
    return bombas


if __name__ == "__main__":
    numeros = [
        69, 43, 17, 4, 31, 10, 6, 52, 67, 8, 25, 2, 50, 75, 24, 89, 44, 5
    ]
    colores_1 = ['rojo', 'rojo', 'azul', 'azul']
    colores_2 =  [
        'verde', 'rojo', 'azul', 'amarillo', 'verde', 'verde', 'azul',
        'rojo', 'azul', 'rojo', 'azul', 'verde', 'verde', 'azul',
        'amarillo', 'azul', 'amarillo', 'rojo', 'rojo', 'azul',
        'verde', 'azul', 'verde', 'verde', 'azul', 'verde', 'rojo'
    ]
    colores_3 = [
        'rojo', 'azul', 'verde', 'verde', 'amarillo', 'amarillo', 'verde',
        'rojo', 'amarillo', 'rojo', 'verde', 'amarillo', 'rojo', 'amarillo',
        'rojo', 'rojo', 'verde', 'amarillo', 'verde'
    ]
    tablero = [
        [' ', 'X', ' ', 'X'],
        ['X', ' ', ' ', ' '],
        [' ', 'X', 'X', ' '],
        ['X', ' ', ' ', 'X']
    ]
    assert promedio_std(numeros) == (34.5, 26.933)
    assert color_frecuente(colores_1) == ("azul", 2)
    assert color_frecuente(colores_2) == ("azul", 9)
    assert color_frecuente(colores_3) == ("rojo", 6)
    assert buscaminas(tablero, 0, 0) == 2
