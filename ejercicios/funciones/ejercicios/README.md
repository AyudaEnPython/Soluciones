# Enunciado Original

## REALICE FUNCIONES EN PYTHON QUE RESUELVAN LOS SIGUIENTES EJERCICIOS

### Ejercicio 1.

Defina una función llamada `hipotenusa` que calcula la longitud de la hipotenusa
de un triángulo recto, cuando se introducen los otros dos lados. Utilice esta
función en un programa que determine la longitud de la hipotenuse para cada uno
de los siguientes triángulos. La función debe tomar dos argumentos de tipo `double`
y devolver la hipotenuse como `double`. Verifique su programa con los valores de los
lados especificados en la figura.

|Triángulo|Lado 1|Lado 2|
|---------|------|------|
|    1    |  3.0 |  4.0 | 
|    2    |  5.0 | 12.0 | 
|    3    |  8.0 | 15.0 |

### Ejercicio 2.

Escriba una función `potenciaInt(base, exponente)` que devuelva el valor de:

     base^exponente

Por ejemplo, `potenciaInt(3, 4) = 3*3*3*3`. Suponga que `exponente` es un entero
positivo diferente de cero, y `base` es un entero. La función `potenciaInt` debe
utilizar for para controlar los cáculos. No utilice las funciones matemáticas de la
biblioteca.

### Ejercicio 3.

Escriba una función `multiplo` que determine para un par de enteros, si el segundo
es múltiplo del primero. La función debe tomar dos argumentos enteros y devolver 1
(verdadero) si el segundo es un mútiplo del primero, y de lo contrario 0 (falso).
Utilice esta función en un programa que introduzca una serie de pares de enteros.

### Ejercicio 4.

Escriba un programa que introduza una serie de enteros y los pase, uno a la vez, a una
función llamada `impar` que utilice el operador módulo para determinar si un entero es
impar. La función debe tomar un argumento entero y devolver 1 si el entero es impar o
0 si no lo es.

### Ejercicio 5.

Escriba una función que despliegue en el margen izquierdo de la pantalla un cuadrado
sólido de asteriscos cuyas medidas se especifiquen mediante el parámetro `lado`. Por
ejemplo, si `lado` es 4, la función despliega:

    ****
    ****
    ****
    ****

### Ejercicio 6.

Modifique la función creada en el ejercicio 5 para formar el cuadrado de cualquier
carácter que especifiquemos en el parámetro `caracterLlenado`. De este modo, si lado
es igual a 5 y `caracterLlenado` es "#", entonces esta función debe imprimir:

    #####
    #####
    #####
    #####
    #####

### Ejercicio 7.

Escriba una función que tome el tiempo en tres argumentos enteros (para horas, minutos
y segundos), y que devuelva el número de segundos desde la última vez que el reloj "marcó
las 12". Utilice esta función para calcular los segundos que existen entre dos horas, las
cuales se miden con el ciclo de 12 horas del reloj.

### Ejercicio 8.

Se dice que un número entero es un _número perfecto_, si la suma de sus factores, incluso
el 1 (pero no el número mismo), arroja el mismo número. Por ejemplo, 6 es número perfecto
debido a que 6 = 1 + 2 + 3. Escriba la función perfecto que determine si el parámetro
numero es un número perfecto. Utilice esta función en un programa que determine e imprima
los números perfectos entre 1 y 100. Imprima los factores de cada número perfecto para
confirmar que el número es realmente perfecto. Rete el poder de su computadora y pruebe
números más grandes que 1000.
