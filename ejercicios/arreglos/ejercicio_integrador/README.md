# Ejercicio Integrador

- Implemente la función _mostrar_matriz_ que recibe como parámetro una matriz y la muestra de forma matricial (una fila debajo de la otra) escribiendo cada valor en 5 lugares.

- Implemente la función _máximo_matriz_ que recibe como parámetros una matriz de valores numéricos y debe retornar el valor mas grande de la matriz.

- Implemente una función _extrar_columna_ que dada una matriz y un entero `i`, devuelva una lista con todos los valores de la columna i-esima de la matriz.

- Escriba una función, que no reciba parámetros, con nombre _main_ que haga los siguientes pasos:
  - Le pida al usuario que ingrese dos valores enteros `N` y `M`.
  - Cree una matriz de `N` filas y `M` columnas y solicite al usuario valores para cada posición de la matriz.
  - Imprima el mensaje "La matriz ingresada es: " y luego invoque a la función _mostrar_matriz_ para imprimir por pantalla la matriz.
  - Calcule el valor máximo de la matriz, llamando a la función _maximo_matriz_.
  - Por último, por cada columna de la matriz informe si el valor máximo calculado en el tercer punto se encuentra o no en la columna, tal como se muestra en los ejemplos de ejecución.

Por ejemplo:

|Test|Entrada|Resultado|
|----|:-----:|:-------:|
|`main()`|4|La matriz ingresada es:|
||2| 1 2|
||1| 3 1|
||2| 1 2|
