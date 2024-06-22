# Prueba Final

## Pregunta 1

¿Cuál es el resultado del siguiente fragmento de código?

```python
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
```

- [ ] `[1, 2, 2, 2]`
- [ ] `[1, 2, 1, 2]`
- [x] `[1, 1, 1, 2]`
- [ ] `[2, 1, 1, 2]`

> Analicemos el programa:
>
> - Línea 1: se crea la lista my_list. La lista almacena los siguientes elementos: [1, 2]
> - Línea 3: la función range() genera una secuencia de dos números (0 y 1), y el bucle for itera sobre esa secuencia. La variable v toma el valor del número dentro de la secuencia en cada iteración y el bucle continúa hasta que se alcanza el último número de la secuencia. Se ingresa el cuerpo del bucle y se realiza dos veces la operación my_list.insert(-1, my_list[v]).
> - Línea 4: después de la primer iteración for del bucle (cuando v = 0), la lista [1, 2] se actualiza: el método insert() inserta un nuevo elemento en la lista (v = 0, entonces my_list[v] = 1) en el índice especificado (-1) . La lista my_list después de la primera iteración del bucle for tiene los siguientes elementos: [1, 1, 2]. Después de la segunda iteración del bucle for (cuando v = 1), la lista [1, 2, 3] se actualiza por segunda vez – el método insert() inserta otro elemento nuevo en la lista (v = 1, por lo que my_list[v] = 1) en el lugar especificado índice (-1). La lista my_list después de la segunda iteración del bucle for contiene los siguientes elementos: [1, 1, 1, 2].
> - Línea 6: la función print() imprime el elemento de la lista en la pantalla.

## Pregunta 2

El significado de un _argumento posicional_ está determinado por:

- [ ] el nombre del argumento especificado junto con su valor
- [x] su posición dentro de la lista de argumentos
- [ ] su conexión con variables existentes
- [ ] su valor

> Los argumentos posicionales se pueden llamar por su posición en una llamada de función y, por lo tanto, deben incluirse en el orden correcto.

## Pregunta 3

¿Cuáles de los siguientes enunciados son **verdaderos** respecto al código? (Selecciona **dos** respuestas)

```python
nums = [1, 2, 3]
vals = nums
```

- [ ] `nums` y `vals` son listas diferentes
- [x] `nums` tiene la misma longitud que `vals`
- [x] `nums` y `vals` son diferentes nombres de la misma lista
- [ ] `vals` es más larga que `nums`

> Asignar nums a vals crea una situación en la que la misma lista (es decir, [1, 2, 3]) tiene dos nombres diferentes. Dar un nuevo nombre a una lista existente, en nuestro caso vals a nums, se llama **aliasing**. Y dado que nums y vals son dos nombres diferentes que se refieren al mismo objeto, también tienen la misma longitud (3).

## Pregunta 4

Un operador capaz de verificar si dos valores **no son iguales** se codifica como:

- [ ] `=/=`
- [ ] `not ==`
- [x] `!=`
- [ ] `<>`

> El operador != comprueba si dos valores no son iguales. Por ejemplo, la siguiente expresión 1 != 2 se evaluará como Verdadero.

## Pregunta 5

El siguiente fragmento de código:

```python
def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)


print(function_2(2))
```

- [ ] dará como salida `2`
- [ ] dará como salida `16`
- [x] provocará un error de ejecución
- [ ] dará como salida `4`

> El objeto None no tiene operadores aritméticos definidos - el programa generará la excepción TypeError, porque el tipo NoneType no puede ser \* operando del operador.

## Pregunta 6

El resultado de la siguiente división:

```python
1 // 2
```

- [ ] es igual a `0.0`
- [x] es igual a `0`
- [ ] es igual `0.5`
- [ ] no se puede predecir

> El operador // divide dos números y redondea el resultado al número entero más cercano. Dado que 1 dividido entre 2 es 0.5, el número resultante se redondea a 0.

## Pregunta 7

El siguiente fragmento de código:

```python
def func(a, b):
    return b ** a


print(func(b=2, 2))
```

- [ ] dará como salida `2`
- [ ] dará como salida `4`
- [ ] dará como salida `None`
- [x] es erróneo

> El programa generará un SyntaxError, porque el argumento posicional en la llamada a la función (2) sigue al argumento de la palabra clave (b=2 ). Cambiar el orden de los argumentos en la invocación de la función func() (es decir, func(2, b=2)) soluciona el problema, en cuyo caso el programa mostraría 4 como resultado.

## Pregunta 8

¿Qué valor se asignará a la variable `x`?

```python
z = 0
y = 10
x = y < z and z > y or y < z and z < y
```

- [x] `False`
- [ ] `True`
- [ ] `0`
- [ ] `1`

> Analicemos el ejemplo:
>
> - 0 se asigna a z, y 10 se asigna a y,
> - el resultado de la siguiente evaluación y < z y z > y o y < z y z < y se asigna a x:
> - y < z se evalúa como Falso,
> - z > y se evalúa como Falso,
> - y < z se evalúa como Falso de nuevo,
> - y z < y se evalúa como Verdadero.
> - Y ahora: Falso and Falso es Falso; Falso or Falso es Falso; y finalmente Falso and Verdadero es Falso.

## Pregunta 9

¿Cuáles de los siguientes nombres de variable son **ilegales** y provocarán una excepción de SyntaxError? (Selecciona **dos** respuestas)

- [x] `in`
- [ ] `In`
- [ ] `print`
- [x] `for`

> Los nombres in y for son palabras reservadas de Python (palabras clave). Estos no se pueden utilizar como nombres de variables. Toma en cuenta que el nombre print no es una palabra reservada de Python y puede usarse como un nombre de variable, en cuyo caso sombreará la función integrada de Python, print().

## Pregunta 10

¿Cuál es el resultado del siguiente fragmento de código?

```python
my_list =  [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))
```

- [ ] `[0, 1, 9, 16]`
- [ ] `[0, 1, 4, 16]`
- [x] `[0, 1, 4, 9]`
- [ ] `[1, 4, 9, 16]`

> Analicemos el ejemplo:
>
> - Línea 1: La lista por comprensión se usa para crear la siguiente lista: [0, 1, 4, 9, 16] , y se asigna a la variable my_list,
> - Líneas 4-6: Se define la función fun(), que toma una lista (lst) como su argumento. En el cuerpo de la función, la instrucción del elimina un elemento específico de la lista y devuelve la lista actualizada,
> - Línea 9: La función print() toma la función fun() como argumento e imprime el valor devuelto en la pantalla. La función fun() toma la lista my_list como argumento y la procesa; la instrucción del elimina el cuarto elemento de la lista (my_list[2] es 4).

## Pregunta 11

¿Cuál es el resultado del siguiente fragmento de código?

```python
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
```

- [ ] `1 2 1`
- [x] `1 1 2`
- [ ] `2 1 2`
- [ ] `1 2 2`

> Analicemos el ejemplo:
>
> - x = 1 y y = 2
> - como resultado de la primera asignación de variable múltiple (Línea 3), x = 1, y = 1 y z = 2
> - como resultado de la segunda asignación de variables múltiples (Línea 4), z = x = 1, y = y = 1 y z = z = 2 (porque la asignación original de la línea anterior ahora sobrescribe la primera asignación z de la línea actual)
> - el resultado en pantalla es por lo tanto 1 1 2

## Pregunta 12

¿Cuál es el resultado del siguiente fragmento de código?

```python
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
```

- [ ] `1 1`
- [ ] `1 0`
- [ ] `0 0`
- [x] `0 1`

> Analicemos el código línea por línea:
>
> - Línea 1: 1 se asigna a la variable a
> - Línea 2: 0 se asigna a la variable b
> - Línea 3: el resultado de la evaluación es 1, entonces a = 1
> - Línea 4: el resultado de la evaluación también es 1, entonces b = 1
> - Línea 5: el resultado de la evaluación a = a ^ b (donde a = 1 y b = 1) es 0, entonces a = 0
> - los nuevos valores asignados a las variables a y b luego se imprimen en la consola.

## Pregunta 13

¿Cuál es el resultado del siguiente fragmento de código?

```python
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))
```

- [ ] `1`
- [ ] `None`
- [ ] el código provocará un error de ejecución
- [x] `2`

> La función print() en la línea 8 toma la función fun() como argumento, que toma otra función fun() como argumento, que a su vez toma el valor 2 como su argumento.
>
> Analicemos las llamadas a funciones, comenzando con las más a la derecha:
>
> - la llamada fun(2): a x se le asigna el valor de 2, por lo que x % 2 = 0, por lo que la comparación 0 == 0 se evalúa como Verdadero, y la función devuelve 1, que se pasa a la función "izquierda" fun() como su argumento,
> - a la llamada fun(1): a x se le asigna el valor de 1, por lo que x % 2 = 1, por lo que la comparación 1 == 0 se evalúa como Falso, lo que significa que la función devuelve 2, que se pasa al función print() como su argumento. Por lo tanto, 2 se imprime en la pantalla.

## Pregunta 14

Observa el fragmento de código y elige la sentencia **verdadera**:

```python
nums = [1, 2, 3]
vals = nums
del vals[:]
```

- [ ] `nums` es más larga que `vals`
- [ ] `vals` es más larga que `nums`
- [ ] el código provocará un error de ejecución
- [x] `nums` y `vals` tienen la misma longitud

> Asignar nums a vals crea una situación en la que la misma lista (es decir, [1, 2, 3]) tiene dos nombres diferentes. Dar un nuevo nombre a una lista existente, en nuestro caso vals a nums, se llama aliasing. Y dado que nums y vals son dos nombres diferentes que se refieren al mismo objeto, también tienen la misma longitud.
>
> La instrucción del vacía la lista a la que apuntan nums y vals, lo que significa que la lista tiene una longitud de cero, lo que a su vez significa que nums y vals tienen la misma longitud.

## Pregunta 15

¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen `3` y `2` respectivamente?

```python
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
```

- [ ] `1`
- [ ] `3`
- [ ] `2`
- [x] `0`

> Analicemos lo que sucede:
>
> - x = 3 y y = 2
> - Línea 3: x = 3 % 2 = 1
> - Línea 4: x = 1 % 2 = 1
> - Línea 5: x = 2 % 1 = 0
> - el resultado se imprime en la pantalla.

## Pregunta 16

¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen `3` y `6` respectivamente?

```python
y = input()
x = input()
print(x + y)
```

- [ ] `6`
- [ ] `36`
- [x] `63`
- [ ] `3`

> Es una pregunta complicada por dos razones:
>
> - Razón uno: la función input() convierte los datos ingresados por el usuario en una cadena, y el resultado de sumar dos cadenas entre sí es pegarlas: "cadena" + "cadena" = "cadena" (concatenación).
> - Razón dos: la primera entrada del usuario se asigna a la variable y, mientras que la segunda a la variable x. Sin embargo, se imprimen en orden inverso.

## Pregunta 17

¿Cuál es el resultado del siguiente fragmento de código?

```python
print("a", "b", "c", sep="sep")
```

- [ ] `asepbsepcsep`
- [ ] `abc`
- [ ] `a b c`
- [x] `asepbsepc`

> La función print() imprime las cadenas "a", "b" y " c" en la pantalla, y los separa con la cadena "sep". El parámetro de palabra clave sep determina el tipo de separador utilizado entre los siguientes argumentos print() mostrados en la pantalla.

## Pregunta 18

¿Cuál es el resultado del siguiente fragmento de código?

```python
x = 1 // 5 + 1 / 5
print(x)
```

- [x] `0.2`
- [ ] `0.4`
- [ ] `0`
- [ ] `0.5`

> Recuerda el principio de precedencia de operadores y la diferencia entre los dos operadores de división en Python: // (división entera) y / (división de punto flotante). Analicemos la expresión en la primera línea:
>
> Debido a que los operadores de división tienen una prioridad más alta que el operador de suma, podemos agregar corchetes para facilitar la lectura y evaluar la expresión de la siguiente manera: (1 // 5) + (1 / 5) da 0 + 0.2, que a su vez se evalúa como 0.2.

## Pregunta 19

Suponiendo que `my_tuple` es una tupla creada correctamente, el hecho de que las tuplas sean inmutables significa que la siguiente instrucción:

```python
my_tuple[1] = my_tuple[1] + my_tuple[0]
```

- [ ] se puede ejecutar si y solo si la tupla contiene al menos dos elementos
- [ ] puede ser ilegal si la tupla contiene cadenas
- [ ] es completamente correcta
- [x] es ilegal

> Las tuplas son secuencias inmutables, lo que significa que no puede actualizarlas directamente - agregar, cambiar o eliminar elementos de tupla requiere que se realicen diferentes tipos de operaciones, por ejemplo, convertir la tupla en una lista, actualizar la lista y volver a convertirla a una tupla.

## Pregunta 20

¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen `2` y `4` respectivamente?

```python
x = float(input())
y = float(input())
print(y ** (1 / x))
```

- [x] `2.0`
- [ ] `1.0`
- [ ] `4.2`
- [ ] `0.0`

> Analicemos lo que sucede:
>
> - el usuario ingresa 2, que se convierte en un flotante, y se asigna a la variable x
> - el usuario ingresa 4, que se convierte en un flotante, y se asigna a la variable y
> - el resultado de la siguiente evaluación se imprime en la pantalla: 4 ** (1 / 2) = 4 ** 0.5 = 2.0

## Pregunta 21

¿Cuál es el resultado del siguiente fragmento de código?

```python
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)
```

- [ ] `('one', 'two', 'three')`
- [x] `one`
- [ ] `two`
- [ ] `three`

> Analicemos el código:
>
> - Línea 1: se crea el diccionario dct que contiene tres pares clave:valor
> - Línea 2: se crea la variable v y se le asigna el valor del diccionario asociado con la clave 'three', que es la cadena "one"
> - Líneas 4-5: el bucle for realiza tres iteraciones (la longitud del diccionario dct es 3):
> - después de k = 0 v = "two"
> - después de k = 1 v = "three"
> - después de k = 2 v = "one"
> - la cadena "one" asignada a la variable v luego se imprime en la pantalla.

## Pregunta 22

¿Cuántos elementos contiene la lista `lst`?

```python
lst = [i for i in range(-1, -2)]
```

- [x] `cero`
- [ ] `dos`
- [ ] `tres`
- [ ] `uno`

> La lista lst está vacía, porque la función range(), que consiste en la comprensión de la lista, establece el parámetro inicial con el valor de -1 y el parámetro final con el valor de -2 (el parámetro final tiene un valor más bajo que el parámetro inicial, lo que hace que sea imposible crear una secuencia).

## Pregunta 23

¿Cuáles de las siguientes líneas **correctamente** invocan la función definida a continuación? (Selecciona **dos** respuestas)

```python
def fun(a, b, c=0):
    # Cuerpo de la función.
```

- [ ] `fun()`
- [ ] `fun(b=1)`
- [x] `fun(0, 1, 2)`
- [x] `fun(b=0, a=0)`

> Debido a que el argumento c es un argumento de palabra clave con un valor predeterminado especificado, basta con llamar a la función especificando valores predeterminados para los dos argumentos de palabra clave restantes, a y b. También es posible reemplazar el valor predeterminado de un parámetro de palabra clave con una llamada de función con argumentos posicionales: fun(0, 1, 2). En ambos casos, es importante que se sirvan todos los parámetros de la función.
>
> La llamada fun(b=1) es incorrecta porque no especifica un valor para un argumento requerido en la definición de la función. La llamada fun() es incorrecta porque no especifica los valores para los argumentos a y b requeridos en la definición de la función.

## Pregunta 24

¿Cuál es el resultado del siguiente fragmento de código?

```python
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))
```

- [x] `0`
- [ ] el código provocará un error de ejecución
- [ ] `2`
- [ ] `1`

> El siguiente fragmento es un ejemplo de una función recursiva.
>
> Los siguientes dos argumentos se envían a la función fun(x, y): 0 y 3. El resultado de la comparación x == y es Falso, por lo que se activa el bloque else:.
>
> En el else:, se devuelve la llamada a la función fun(x, y-1), y esta vez se envían los siguientes dos argumentos: x = 0, y y = 3 - 1 = 2. El proceso se repite (x = 0, y = 2 – 1 = 1 y x = 0, y = 1 – 1 = 0) hasta que el valor asignado a la variable y sea igual a 0, en cuyo caso el resultado de la comparación x == y es Verdadero, y la función devuelve el valor x de 0.

## Pregunta 25

¿Cuántos (`*`) imprimirá el siguiente fragmento de código en la consola?

```python
i = 0
while i < i + 2 :
    i += 1
    print("*")
else:
    print("*")
```

- [x] el fragmento entrará en un bucle infinito, imprimiendo un `*` por línea
- [ ] `2`
- [ ] `0`
- [ ] `1`

> Debido a que i = 0, el resultado de la siguiente comparación: i < 1 +2 es Verdadero, entonces el programa ingresa en el bucle while. Sin embargo, en el cuerpo del bucle, i se incrementa, no se reduce, lo que significa que el resultado de la comparación i < 1 +2 siempre se evaluará como True, lo que significa el bucle realizará un número infinito de iteraciones, ejecutando la función print("\*") con todas y cada una de las iteraciones.

## Pregunta 26

¿Cuál es el resultado del siguiente fragmento de código?

```python
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
```

- [x] `4`
- [ ] `(4, )`
- [ ] `(4)`
- [ ] `44`

> Analicemos el código línea por línea:
>
> - Línea 1: se crea la tupla tup de cuatro elementos
> - Línea 2: las tuplas se puede dividir, por lo que el siguiente resultado de división se asigna a tup: (4,)
> - Línea 3: dado que la tupla tup es una tupla de un elemento ahora (4,), indexar el último y único elemento lo extraerá de la tupla y lo asignará a la variable tup como un valor entero.
> - el valor 4 se imprimirá en la pantalla.

## Pregunta 27

¿Cuál es el resultado del siguiente fragmento de código?

```python
dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")
```

- [ ] `0 0`
- [ ] `0 1`
- [x] el código es erróneo (el objeto `dict` no contiene el método `vals()`)
- [ ] `1 0`

> El siguiente fragmento generará la excepción AttributeError, porque el objeto dict no tiene un atributo llamado vals. Reemplazar vals con values debería funcionar.

## Pregunta 28

¿Cuál es el resultado del siguiente fragmento de código?

```python
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
```

- [ ] `(1, 2)`
- [ ] `12`
- [x] `21`
- [ ] `(2, 1)`

> Analicemos el código:
>
> - Línea 1: se crea un diccionario vacío
> - Líneas 2-3: se crean los pares clave:valor y se agregan al diccionario dct:
> - dct = {'1': (1, 2), '2': (2, 1)}
> - Línea 5-6: se realizan dos iteraciones del bucle for (itera a través de las claves dct) e imprime los valores del diccionario (elementos de tupla) indexados en la función print(): x = 1 2, x = 2 1
> - el parámetro end="" une las dos líneas impresas.

## Pregunta 29

¿Cuál es el resultado del siguiente fragmento de código?

```python
def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))
```

- [ ] `2`
- [ ] el fragmento de código es erróneo y provocará un SyntaxError
- [ ] `6`
- [x] `4`

> El valor predeterminado (3) asignado al argumento out de la definición de la función fun() se ha cambiado a 2 en la llamada a la función fun() pasada como argumento a la función print(). De esta forma el resultado de la evaluación (inp = 2) \* (out = 2) es igual a 4.

## Pregunta 30

¿Cuántos (`#`) imprimirá el siguiente fragmento de código en la consola?

```python
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
```

- [ ] `seis`
- [ ] `cero`
- [x] `tres`
- [ ] `nueve`

> Analicemos el código:
>
> - Línea 1: estamos usando una lista por comprensión para crear la siguiente arreglo bidimensional:
> - [[0, 1, 2 ], [0, 1, 2], [0, 1, 2]]
> - el programa entra en el primer bucle for con la variable de iteración r que toma el valor del primer elemento dentro de la secuencia generada por la función range(3), que es 0. Luego, el programa ingresa al segundo bucle (anidado) for con la variable de iteración c tomando el valor del primer elemento dentro de la secuencia generada por la función range(3), que es 0. Se verifica la siguiente condición:
> - if lst[0][0] % 2 != 0, luego se imprime un # en la pantalla. El valor devuelto de la lista lst almacenada en los índices [0][0] es 0, por lo que la condición se evalúa como falsa (0 % 2 != 0 → False), lo que significa que no se imprime un # en la pantalla en este momento, y la ejecución del programa vuelve al bucle exterior. Las iteraciones se repiten para los siguientes pares de índices: [0][1], [0][2], [1][2], [1][0], [1][1], [1][2], [2][2], [2][0], [2][1] y [2][2].
> - la función print() imprimirá un # cuando los siguientes pares de índices formen parte de la comprobación condicional:
> - [0][1] → 1 porque if 1 % 2 != 0 se evalúa como Verdadero
> - [1][1] → 1 porque if 1 % 2 != 0 se evalúa como Verdadero
> - [2][1] → 1 porque if 1 % 2 != 0 se evalúa como Verdadero
> - Por lo tanto, la función print() generará tres # en la pantalla.

## Pregunta 31

¿Cuál es el comportamiento esperado del siguiente programa si el usuario ingresa `0`?

```python
try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")
```

- [ ] `Entrada incorrecta...`
- [ ] `1.0`
- [x] `0.0`
- [ ] `Entrada errónea..`
- [ ] `Entrada muy errónea..`
- [ ] `¡Buuu!`

> El programa imprimirá 0.0 porque la siguiente expresión int(0) / len("0") se evalúa como 0.0 (0 / 1 → 0.0), por lo que el flujo del programa no entra en ninguna de las ramas except y no se genera ninguna excepción.

## Pregunta 32

¿Cuál es el comportamiento esperado del siguiente programa?

```python
try:
    print(5/0)
    break
except:
    print("Lo siento, algo salió mal...")
except (ValueError, ZeroDivisionError):
    print("Mala suerte...")
```

- [ ] El programa generará una excepción `ValueError` y dará como salida el siguiente mensaje: `Mala suerte...`
- [ ] El programa generará una excepción `ZeroDivisionError` y dará como salida el siguiente mensaje: `Mala suerte...`
- [ ] El programa generará una excepción `ZeroDivisionError` y dará como salida un mensaje de error predeterminado.
- [ ] El programa generará una excepción `ValueError` y dará como salida un mensaje de error predeterminado.
- [ ] El programa generará una excepción y será manejada por el primer bloque `except`.
- [x] El programa generará una excepción `SyntaxError`.

> El programa generará una excepción SyntaxError, porque la sentencia break utilizada en el bloque try viola las reglas gramaticales de Python (la instrucción break debe usarse en un bucle). Cuando se ejecuta el código, antes de que se ejecute, el intérprete de Python primero lo analiza y lo convierte en código de bytes de Python. Si el analizador encuentra un error de sintaxis que tiene un efecto fatal en el programa, no podrá analizar el código correctamente y generará un SyntaxError.
>
> Recuerda que el analizador analiza el programa antes de su ejecución, por lo que si encuentra un error de sintaxis, el programa no se ejecutará. Si tu código no tiene errores de sintaxis, el programa se ejecuta y puede generar otros tipos de excepciones.

## Pregunta 33

¿Cuál es el comportamiento esperado del siguiente programa?

```python
foo = (1, 2, 3)
foo.index(0)
```

- [ ] El programa provocará una excepción `TypeError`.
- [ ] El programa dará como salida un `1` en la pantalla.
- [ ] El programa provocará una excepción `SyntaxError`.
- [x] El programa provocará una excepción `ValueError`.
- [ ] El programa provocará una excepción `AttributeError`.

> El programa generará una excepción ValueError, porque el método de tupla index() devuelve el índice de un elemento dado en una tupla, y la tupla foo no tiene el elemento 0.
>
> Mensaje de error completo: ValueError: tuple.index(x): x not in tuple.

## Pregunta 34

¿Cuál de los siguientes fragmentos muestra la forma correcta de manejar múltiples excepciones en una sola cláusula _except_?

```python
# A:
except (TypeError, ValueError, ZeroDivisionError):
    # Algo de código.

# B:
except TypeError, ValueError, ZeroDivisionError:
    # Algo de código.

# C:
except: (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.

# D:
except: TypeError, ValueError, ZeroDivisionError
    # Algo de código.

# E:
except (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.

# F:
except TypeError, ValueError, ZeroDivisionError
    # Algo de código.
```

- [ ] A y F
- [ ] D y E
- [ ] A, C y D
- [x] A solamente
- [ ] A y B
- [ ] F solamente
- [ ] B y C

> La siguiente sintaxis:
>
> `except (TypeError, ValueError, ZeroDivisionError):`
>
> es la única opción correcta para manejar múltiples excepciones integradas dentro de una única cláusula _except_.

## Pregunta 35

¿Qué pasará cuando intentes ejecutar el siguiente código?

```python
print(¡Hola, Mundo!)
```

- [ ] El código generará la excepción _ValueError_.
- [x] El código generará la excepción _SyntaxError_.
- [ ] El código imprimirá `¡Hola, Mundo!` en la consola.
- [ ] El código generará la excepción _AttributeError_.
- [ ] El código generará la excepción _TypeError_.

> El código generará una excepción SyntaxError, porque el argumento de cadena pasado a la función print() debe estar delimitado por comillas.
>
> El programa no genera una excepción NameError, porque ¡Hola contiene un carácter ilegal: ¡, y ¡Hola y Mundo! no pueden considerarse nombres de variables que no hayan sido reconocidos por Python.
