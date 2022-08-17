# Primer Cuestionario Práctico

## Pregunta 1

Esta será la forma de evaluar la escritura de código en este curso. Habrá un
código incompleto (será una función de Python, pero de eso no debes preocuparte
todavía), y tú deberás completarlo.\
<br>
Por ejemplo, aquí escribe en la línea **3** lo siguiente: **suma = a + b**
(cuidando que tenga la misma cantidad de espacios a la izquierda que la
línea anterior).\
<br>
Estas **a** y **b** no deberán ser definidas: uno puede pensarlo como que, todos
los nombres que van entre paréntesis después del nombre de la función, tendrán
el valor correcto.

```python
def sumador(a, b):
  # Acá abajo escribe lo que pedimos
  
  # No cambies esta línea
  return suma
```

## Pregunta 2

Pregunta 2

En esta funciones no buscamos que impriman nada con **print**, sino que retornen
una variable. Por ejemplo, si están pidiendo la suma de dos números, como en la
pregunta pasada, le devolveremos al que preguntó una variable que contenga el
valor de la suma.\
<br>
En esta pregunta, hay cuatro variables definidas, pero solo debes retornar una
(es decir, en la línea **8** poner algo como **return algo**, con **algo** una
opción entre **var1**, **var2**, **var3**, **var4**). En esta pregunta debes
retornar la multiplicación de los dos parámetros (valores dentro de paréntesis
después del nombre de la función) que se pasan a la función. ¿Cuál de las cuatro
variables será?

```python
def multiplicacion(a, b):
  var1 = a + b
  var2 = a + var1
  var3 = a * b
  var4 = a / b
  
  # Después de esta línea pon algo como return nombre_variable, donde nombre_variable es la variable correcta según lo que pide. Ojo: debe escribirse con la misma indentación (cantidad de espacios al principio de la línea) que las líneas 2 a 5.
```
