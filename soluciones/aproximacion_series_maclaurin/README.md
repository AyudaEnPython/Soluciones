Ejercicio: Muchas veces es importante evaluar una función  sobre 
los $n + 1$ puntos de una partición regular de un intervalo cerrado $[a, b]$. 

Escribir un programa que evalúe las funciones mediante aproximación de
series de Maclaurin en una partición regular del intervalo $[a, b]$ de
tal forma que se programe el siguiente menú de opciones:

    1. Ingrese el valor de a.
    2. Ingrese el valor de b.
    3. Ingrese el valor de n. Cantidad de subintervalos del
      intervalo [a, b].
    4. Evaluación de la función exp(x) en la partición.
    5. Evaluación de la función sen(x) en la partición.
    6. Evaluación de la función arcsen(x) en la partición.
    7. Salir

Elemento a tener en cuenta para escribir (y la evaluación) el programa:

* Se debe inicializar las  variables $a$, $b$ y $n$ con los valores
  -1, 1 y 10 respectivamente. (Todo debe funcionar sin ningún error con
  estos tres valores.)
* Cuando seleccione las opciones 1 o 2  para actualizar el valor
  de _**a**_ o _**b**_ se debe garantizar que dichos valores determinen un
  intervalo cerrado $[a, b]$ bien definido.
* Cuando seleccione la opción 3 para actualizar el valor de la variable
  n se debe garantizar que dicho valor sea positivo.
* Al seleccionar las opciones 4, 5 o 6 el programa debe evaluar la función
  correspondiente en cada uno de los $n + 1$ puntos de la partición regular del
  intervalo $[a, b]$. Esta información debe aparecer en dos columnas, en la
  primera columna el valor de x y en la segunda columna f(x), donde f(x)
  puede ser  _**sen(x)**_, _**cos(x)**_ o _**arcsen(x)**_ dependiendo la
  opción seleccionada.
* Para evaluar las funciones _**exp(x)**_, _**sen(x)**_, _**arcsen(x)**_ se
  debe usar las respectivas fórmulas de series de Maclaurin. 
  Para el _**arcsen**_ tenga en cuenta que el dominio de la función es [-1, 1].
  (ojo con este detalle)
* Use una _**constante**_ para determinar el número sumados para aproximar
  las series, seleccione una cantidad  adecuada. En otras palabras, no se
  debe ingresar el número de sumandos para aproximar las series.
* NO ES PERMITIDO importar exp, sin, arcsen desde el módulo math o usar
  cualquier otra alternativa.