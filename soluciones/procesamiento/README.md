# Procesamiento de datos (Enunciado Original)

## Ejercicio 1

Imprima la suma de la segunda columna.

    214

## Ejercicio 2

Imprima la cantidad de registros por letra para la primera
ordenados alfabéticamente por la letra de la columna 1.

    A,8
    B,7
    C,5
    D,6
    E,14

## Ejercicio 3

Imprima la suma de la columna 2 por cada letra de la primera
columna, ordenados alfabéticamente.

    A,53
    B,36
    C,27
    D,31
    E,67

## Ejercicio 4:

La columna 3 contiene una fecha en formato 'YYYY-MM-DD'. Imprima la
cantidad de registros por cada mes separados por comas, tal como se
muestra a continuación.

    01,3
    02,4
    03,2
    04,4
    05,3
    06,3
    07,5
    08,6
    09,3
    10,2
    11,2
    12,3

## Ejercicio 5:

Imprima el valor máximo y el mínimo de la columna 2 por cada letra de la
columna 1.

    A,9,2
    B,9,1
    C,9,0
    D,8,3
    E,9,1

## Ejercicio 6:

La columna 5 codifica un diccionario donde cada cadena de tres letras
corresponde a una clave y el valor despues del caracter `:` corresponde
al valor asociado a la clave. Por cada clave, obtenga el valor asociado
mas pequeño y el valor asociado mas grande computados sobre todo el
archivo.

    aaa,1,9
    bbb,1,9
    ccc,1,10
    ddd,0,9
    eee,1,7
    fff,0,9
    ggg,3,10
    hhh,0,9
    iii,0,9
    jjj,5,17

## Ejercicio 7:

Genera una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
contiene un valor posible de la columna 2 y una lista con todas las
letras asociadas (columna 1) a dicho valor de la columna 2.

    ('0', ['C'])
    ('1', ['E', 'B', 'E'])
    ('2', ['A', 'E'])
    ('3', ['A', 'B', 'D', 'E', 'E', 'D'])
    ('4', ['E', 'B'])
    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
    ('6', ['C', 'E', 'A', 'B'])
    ('7', ['A', 'C', 'E', 'D'])
    ('8', ['E', 'D', 'E', 'A', 'B'])
    ('9', ['A', 'B', 'E', 'A', 'A', 'C'])

## Ejercicio 8:

Genere una lista de tuplas, donde cada tupla contiene en la primera posicion,
el valor de la segunda columna; la segunda parte de la tupla es una lista con
las letras (ordenadas y sin repetir letra) de la primera  columna que
aparecen asociadas a dicho valor de la segunda columna. Esto es:

    ('0', ['C'])
    ('1', ['E', 'B'])
    ('2', ['A', 'E'])
    ('3', ['E', 'A', 'D', 'B'])
    ('4', ['E', 'B'])
    ('5', ['E', 'D', 'C', 'B'])
    ('6', ['A', 'E', 'C', 'B'])
    ('7', ['A', 'E', 'C', 'D'])
    ('8', ['A', 'E', 'D', 'B'])
    ('9', ['A', 'E', 'C', 'B'])

## Ejercicio 9:

Imprima una tabla en formato CSV que contenga la cantidad de registros en que
aparece cada clave de la columna 5.

    aaa,13
    bbb,16
    ccc,23
    ddd,23
    eee,15
    fff,20
    ggg,13
    hhh,16
    iii,18
    jjj,18

## Ejercicio 10:

Imprima una tabla en formato CSV que contenga por registro, la letra de la
columna 1 y la cantidad de elementos de las columnas 4 y 5.

    E,3,5
    A,3,4
    B,4,4
    A,2,4
    C,4,4
    A,2,5
    A,3,6
    B,2,3
    E,4,6
    B,4,6
    C,4,5
    C,4,3
    D,4,5
    E,2,3
    B,2,5
    D,2,4
    E,3,6
    D,2,3
    E,4,3
    E,2,3
    E,2,3
    E,3,3
    D,3,3
    A,3,5
    E,2,6
    E,3,6
    A,3,3
    E,3,5
    A,2,5
    C,4,6
    A,2,5
    D,2,6
    E,2,4
    B,3,6
    B,3,5
    D,2,3
    B,2,5
    C,4,3
    E,2,3
    E,3,3

## Ejercicio 11:

Imprima la suma de la columna 2 para cada letra de la columna 4,
ordenados alfabeticamente.

    a,122
    b,49
    c,91
    d,73
    e,86
    f,134
    g,35

## Ejercicio 12:

Imprima por cada fila, la columna 1 y la suma de los valores de la
columna 5.

    E,34
    A,14
    B,25
    A,22
    C,27
    A,14
    A,23
    B,6
    E,33
    B,31
    C,24
    C,22
    D,24
    E,25
    B,25
    D,26
    E,29
    D,18
    E,16
    E,13
    E,15
    E,20
    D,27
    A,38
    E,35
    E,25
    A,9
    E,35
    A,34
    C,30
    A,23
    D,32
    E,12
    B,24
    B,33
    D,9
    B,43
    C,11
    E,16
    E,16
