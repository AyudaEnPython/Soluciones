# Creación de funciones

## Pregunta 1

Para la tarea de determinar si un usuario es mayor de edad o no, se dispone de
la función _mayor(edad)_ que recibe como **argumento** un número entero que representa
la edad, y **retorna** True si la persona tiene 18 años o más, y False en caso
contrario.\
<br>
Determina cuál o cuáles de las siguientes alternativas presenta funciones que
realicen lo anterior correctamente.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def mayor(edad):
      if edad >= 18:
          return True
      return False
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def mayor(edad):
      return edad >= 18
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def mayor(edad):
      if edad >= 18:
          return True
      else:
          return False
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def mayor(edad):
      print(edad >= 18)
  ```
  </span>

- [ ] <span>
  ```python
  def mayor(edad):
      if edad >= 18:
          print(True)
      else:
          print(False)
  ```
  </span>

## Pregunta 2

Dada la función _factorial(n)_, que dado un número natural _n_, retorna el valor de
n!, es decir, 1*2*3*4*...*n, se desea que en la variable _resultado_ esté almacenado
el valor de dicho cálculo. Determina cuál de las siguientes alternativas es
correcta para calcular el factorial de 5 y que quede en dicha variable.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  n = 5
  resultado = factorial(n)
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  factorial(5)
  ```
  </span>

- [ ] <span>
  ```python
  resultado = 5
  factorial(resultado)
  ```
  </span>

- [ ] <span>
  ```python
  n = 5
  resultado = 0
  factorial(n, resultado)
  ```
  </span>

- [ ] <span>
  ```python
  resultado = 5
  n = factorial(resultado)
  ```
  </span>

## Pregunta 3

En cuanto al _scope_ de funciones. Determina cuáles de los siguientes códigos termina
en un error de Python.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def sumador(n):
      sumando = 10
      n += sumando
      return n
  sumador(5)
  print(sumando)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  cantidad = 0
  def sumador(n):
      cantidad += 1
      n += 1
      return n
  sumador(5)
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  sumando = 10
  def sumador(n):
      n += sumando
      return n
  sumador(5)
  print(sumando)
  ```
  </span>

- [ ] <span>
  ```python
  def sumador(n):
    sumando = 10
    n += sumando
    return n
  sumador(5)
  ```
  </span>

- [ ] <span>
  ```python
  def sumador(n, sumando):
      sumando += 1
      n += sumando
      return n
  b = 9
  sumador(5, b)
  ```
  </span>

## Pregunta 4

Determina lo que imprimirá el siguiente código:

```python
numero = 10
def operacion(n):
    numero = 100
    return n * numero
operacion(5)
print(numero)
```

- [X] 10
- [ ] 100
- [ ] Depende del valor de n
- [ ] Arrojará error de Python

## Pregunta 5

Si se tiene un módulo de funciones de nombre _modulo.py_, y este contiene las funciones
_multiplicar(a, b)_ y _dividir(a, b)_. Determina cuáles de los siguientes códigos es
correcto.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from modulo import *
  print(multiplicar(2, 3))
  print(dividir(10, 5))
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  import modulo
  print(modulo.multiplicar(2, 3))
  print(modulo.dividir(10, 5))
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from modulo import multiplicar, dividir
  print(multiplicar(2, 3))
  print(dividir(10, 5))
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  from modulo import *
  print(modulo.multiplicar(2, 3))
  print(modulo.dividir(10, 5))
  ```
  </span>

- [ ] <span>
  ```python
  import modulo
  print(multiplicar(2, 3))
  print(dividir(10, 5))
  ```
  </span>

## Pregunta 6

Determina el valor que queda almacenado en las variables _resultado1_ y _resultado2_ tras
la ejecución del siguiente código:

```python
def operacion(n):
    if n > 10:
        return 20
        return 15
    return 10
    return 25

resultado1 = operacion(8)
resultado2 = operacion(12)
```

- [ ] resultado1=8<br>resultado2=12 
- [ ] resultado1=10<br>resultado2=15
- [ ] resultado1=25<br>resultado2=20 
- [ ] resultado1=25<br>resultado2=15 
- [X] resultado1=10<br>resultado2=20 

## Pregunta 7

Considera el siguiente código:

```python
def funcion(x):
    n = 3
    return ?
print(funcion(9))
print(funcion(10))
```

¿Qué debe retornar la función en lugar de ese "?" para que el código imprima True y
False respectivamente?

- [X] `not bool(x % n)`
- [ ] `x != n`
- [ ] `x % n`
- [ ] `x == n`
- [ ] `bool(x % n)`



## Pregunta 8

Considera el siguiente código:

```python
numero = 5
resultado = exponenciacion_aleatoria(numero)

def exponenciacion_aleatoria(n):
    return n ** random.randint(1, 10)
```

Selecciona todas las alternativas que muestren razones por las cuales el código anterior
es **incorrecto**.

- [X] Se llama a la función antes de que se hay definido
- [ ] Se utiliza un operador inválido: **
- [ ] Se realiza una operación en el retorno, en vez de realizarla antes y retornar una variable que almacene el resultado
- [X] No se importa el módulo random
- [ ] Se utiliza un "_" en el nombre de la función 

## Pregunta 9

Selecciona la afirmación **incorrecta** respecto a funciones.

- [ ] Las variables definidas dentro de una función no pueden ser utilizadas fuera de ella.
- [ ] Las variables definidas fuera de una función no pueden ser modificadas dentro de una función.
- [ ] Los llamados a funciones deben hacerse después de la definición de la función.
- [X] Una función no puede tener más de dos retornos.
- [ ] El retorno de una función puede incluir expresiones booleanas.

## Pregunta 10

Considerando el siguiente programa:

```python
def funcion(n):
    a = n ** 3
    b = a ** 2
    c = b + 100
    d = 5 * c
    return print(d)

d = funcion(2)
```

Determina el valor que queda almacenado en _d_ tras la ejecución del programa.

- [] 820
- [X] None
- [ ] 0
- [ ] 2
- [ ] Se genera un error de Python
