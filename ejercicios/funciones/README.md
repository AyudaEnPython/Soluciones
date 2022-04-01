# Enunciado Original

## Ejercicios

1. Función que devuelve una lista de números enteros, recibe dos argumentos:\
    `inicio`: Número entero donde inicia la lista.\
    `tamanio`: Cantidad de números enteros consecutivos.

    Ejemplo: `ListaEnteros(10,5)` debe retornar `[10,11,12,13,14]`

2. Función que devuelve dos valores, la parte entera de la división y su resto,
  recibe dos argumentos:\
  `dividendo`: El número que va a ser dividido.\
  `divisor`: El número que va a dividir.

    Ejemplo: `DividirDosNumeros(10,3)` debe retornar `3,1`

3. Función que devuelve el valor booleano True si el número es capicúa, de lo
  contrario devuelve el valor booleano False.
  En caso de que el parámetro no sea de tipo entero, debe retornar nulo; recibe
  un argumento:\
  `numero`: Será el número sobre el que se evaluará si es capicúa o no lo es.

    Ejemplo:\
    `NumeroCapicua(787)` debe retornar `True`\
    `NumeroCapicua(108)` debe retornar `False`

4. Función que devuelve el factorial del número pasado como parámetro, en caso de no
  ser de tipo entero y/o sea menor que 1, debe retornar nulo; recibe un argumento:\
  `numero`: Será el número con el que se calcule el factorial.

    Ejemplo:\
    `Factorial(4)` debe retornar 24\
    `Factorial(-2)` debe retornar nulo

5. Función que devuelve el número primo siguiente al enviado como parámetro, en caso
  de que el parámetro no sea de tipo entero y/o sea un número primo, debe retornar
  nulo; recibe un argumento:\
  `actual_primo`: Será el número primo a partir del cual debo buscar el siguiente.

    Ejemplo:\
    `ProximoPrimo(7)` debe retornar 11\
    `ProximoPrimo(8)` debe retornar nulo

6. Función que recibe como parámetro un número entero mayor a cero y devuelva dos listas,
  una con cada factor común y otra con su exponente, esas dos listas tiene que estar
  contenidas en otra lista. En caso de que el parámetro no sea de tipo entero y/o mayor
  a cero debe retornar nulo; recibe un argumento:\
  `numero`: Será el número sobre el que se hará la factorización.

    Ejemplo:\
    `factorizar_numero(12)` debe retornar `[[2,3],[2,1]]`\
    `factorizar_numero(13)` debe retornar `[[13],[1]]`\
    `factorizar_numero(14)` debe retornar `[[2,7],[1,1]]`

7. Función que devuelve un objeto instanciado de la clase Animal, la cual debe tener los
  siguientes atributos:\
  `Edad` (Un valor de tipo de dato entero, que debe inicializarse en cero).
  `Especie` (Un valor de tipo de dato string).
  `Color` (Un valor de tipo de dato string).\
  y debe tener el siguiente método:\
  `CumplirAnios` (este método debe sumar uno al atributo Edad y debe devolver ese valor)\
  Recibe dos argumentos:
  `especie`: dato que se asignará al atributo Especie del objeto de la clase Animal.
  `color`: dato que se asignará al atributo Color del objeto de la clase Animal.\

    Ejemplo:\
    a = ClaseAnimal('perro','blanco')\
    a.CumpliAnios() -> debe devolver 1.\
    a.CumpliAnios() -> debe devolver 2.\
    a.CumpliAnios() -> debe devolver 3.

8. Función recibe como parámetro un número entero mayor o igual a cero y lo devuelve en
  su representación binaria. Debe recibir y devolver un valor de tipo entero. En caso de
  que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo; recibe un
  argumento:\

    Ejemplo:\
    `NumeroBinario(12)` debe retornar 1100. 
    `NumeroBinario(2)` debe retornar 10. 

