# Cuestionario Practico

# Pregunta 1

Escriba una función de nombre **promedio_std()**. La función debe recibir una
**lista** de números llamada lista, y debe retornar retornar el promedio de ellos,
junto con su desviación estándar.
<br><br>
_Hint 1_: La desviación estándar corresponde a la raíz de la suma de los cuadrados
de las diferencias de cada elemento respecto al promedio, divididos por la
cantidad de elementos.
<br><br>
_Hint 2_: Recuerda que puedes retonar dos valores x e y utilizando la notación

```python
return (x, y)
```
```python
def ? # debes modificar todos los elementos de la función
# cuidando el retorno, nombre y argumentos
```

# Pregunta 2

Pregunta 2

Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser:
_azul, rojo, verde y amarillo_. Desea saber cual de esos colores es el que más se
repite. Escriba una función _color_frecuente_ que reciba como argumento a una lista
de strings llamada lista y retorne el _string_ más repetido y el número de ocurrencias
del mismo.
<br><br>
Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde',
'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
<br><br>
Debe retornar: "verde", 8
<br><br>
**En caso de que haya varios colores con el máximo número, se retornará con la siguiente
prioridad: azul, rojo, verde, amarillo. Es decir, por ejemplo si la lista es
l = ['rojo', 'rojo', 'azul', azul'], la función debe retornar "azul", 2**

```python
def ? # debes modificar todos los elementos de la función
# cuidando el retorno, nombre y argumentos
```

# Pregunta 3

Un uso muy común de las listas es el de representar tableros con ellas. Para eso se
utilizan listas de listas, de este modo, se puede entender una lista de listas como
una matriz. Así, para acceder a un elemento _i,j_ de la matriz, se debe
acceder a: _matriz[i][j]_. 
<br><br>
Para ese ejercicio se dispone de un tablero de buscaminas especial, donde lo único
que hay es bombas en las distintas posiciones. Este tablero es de la forma:
<br><br>

<table border="1">
<body>
  <tr>
    <td></td>
    <td>x</td>
    <td></td>
    <td>x</td>
  </tr>
  <tr>
    <td>x</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>x</td>
    <td>x</td>
    <td></td>
  </tr>
  <tr>
    <td>x</td>
    <td></td>
    <td></td>
    <td>x</td>
  </tr>
</body>
</table>

Donde las _X_ representan las bombas. Ese tablero, en representación matricial de
Python, donde se utilizan strings con un espacio: " " y "X" para representar
espacios libres y bombas respectivamente, viene dado por:

```python
```

El objetivo de este ejercicio, es que programes una función _buscaminas_ que reciba como
argumento a una matriz _tablero_ y dos coordenadas _i, j_, y que entregue la cantidad de
bombas que rodean a esa posición. 
<br><br>
Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene
dada por _i=0_ y _j=0_, tu función debe retornar el valor 2, ya que hay dos bombas
rodeándola, en (0,1) y (1,0). 
<br><br>
Por otro lado, si el tablero es el mismo, y las coordenadas son _i=1_, _j=1_, tu función
debe retornar 4, pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y
en (2,2).
<br><br>
_Hint_: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir
posiciones más grandes que ese tamaño o menores que 0, tu programa arrojará error.

```python
def ? # debes modificar todos los elementos de la función
# cuidando el retorno, nombre y argumentos
```