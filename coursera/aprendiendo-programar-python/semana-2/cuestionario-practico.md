# Cuestionario Práctico

## Pregunta 1

Una Una conocida medida de la masa en relación a la estatura de las personas
es el IMC (Índice de Masa Corporal). Para su   cálculo se utiliza la masa del
individuo y su estatura. La ecuación que las relaciona es:\
<br>
IMC = masa / (estatura ^ 2)\
<br>
Donde la masa se expresa en kilogramos, y la estatura en metros.\
<br>
Para poder resolver este problema y los siguientes, debes escribir el código
que falta en el espacio que lo señala. Asume que ya existen variables con los
nombres **masa** y **peso**, que ya contienen los valores requeridos (no debes
pedírselos al usuario), haz los cálculos que necesites, y luego deja el
resultado en una variable llamada **imc**.

```python
def imc(masa, estatura):
    imc = 0
    # desde aquí hacia abajo debes modificar el programa
    # modifica la variable imc
    # recuerda que los datos están en las variables masa y estatura
    return imc
```

## Pregunta 2
Para obtener ciertas estadísticas de un recorrido, se pide realizar un programa
que dada una distancia, entregue la velocidad en kilómetros por hora y en metros
por segundo. Para esto, existen dos variables _tiempo_ y _distancia_ que vienen en
segundos y kilómetros respectivamente. Tu programa debe guardar en la variable
resultado un _string_, por ejemplo, para el siguiente caso:\
<br>
_tiempo = 1_\
<br>
_distancia = 0.01_\
<br>
La variable resultado debería tener lo siguiente:\
<br>
"La velocidad es 36.0 km/h o 10.0 m/s"\
<br>
Para poder resolver este problema , debes escribir el código que falta en el
espacio que lo señala. Asume que ya existen variables con los nombres **tiempo** y
**distancia**, que ya contienen los valores requeridos (no debes pedírselos al
usuario), haz los cálculos que necesites, y luego deja el resultado en una
variable llamada **resultado**.

```python
def velocidad(distancia, tiempo):
    resultado = ""
    # desde aquí hacia abajo debes modificar el programa
    # modifica la variable resultado
    # recuerda que los datos están en las variables distancia y tiempo
    return resultado
```

## Pregunta 3

Considerando que las variables pueden almacenar cualquier tipo de dato, en
este ejercicio se utilizaran variables de tipo _booleanas_. En computación un
operador muy conocido es el operador lógico XOR (exclusive OR), el que dadas
dos expresiones a y b _booleanas_, entrega verdadero únicamente si una de ellas
es verdadera, y falso en cualquier otro caso.\
<br>
Por ejemplo si se tiene\
<br>
_resultado = True XOR False_\
<br>
en resultado estará almacenado el valor True, en cambio si se tiene\
<br>
&nbsp;&nbsp;_resultado = True XOR True    o     resultado = False XOR False_\
<br>
en _resultado_ estará almacenado el valor False.\
<br>
La tabla de verdad para todos los valores posibles de a y b, es la siguiente:
<table border="1">
  <thead>
    <tr>
      <th>a</th>
      <th>b</th>
      <th>a XOR b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
Así, utilizando los conocimientos de _booleanos_ adquiridos en el curso, y los
conocimientos de operadores lógicos, modifica el código de más abajo, para
que en la variable _xor_ quede almacenado el valor de hacer XOR entre las
variables a y b.\
<br>
Para poder resolver este problema , debes escribir el código que falta en el
espacio que lo señala. Asume que ya existen variables con los nombres **a** y
**b**, que ya contienen los valores requeridos (no debes pedírselos al usuario),
haz los cálculos que necesites, y luego deja el resultado en una variable
llamada **xor**.

```python
def xor(a, b):
    xor = False
    # desde aquí hacia abajo debes modificar el programa
    # modifica la variable xor
    # recuerda que los datos están en las variables a y b
    return xor
```