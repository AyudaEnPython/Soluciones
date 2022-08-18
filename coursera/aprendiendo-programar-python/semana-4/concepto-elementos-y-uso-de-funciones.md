# Concepto, elementos y uso de funciones

## Pregunta 1

¿Con qué palabra se especifica el valor que queremos que la función nos devuelva?

- [ ] result
- [ ] give
- [X] return
- [ ] def

## Pregunta 2

Dada la siguiente función:

```python
def divis(a, b):
    c = a // b
    d = b // a
    resultado = c + d
    return resultado
```

¿Cuál es/son sus **parámetros**?

- [X] a, b
- [ ] a, b, c, d, resultado
- [ ] resultado
- [ ] c, d

## Pregunta 3

¿Qué retorna la siguiente función, para x = 102, y para x=103?

```python
def funcion_misteriosa(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
```

- [ ] x=102, retorna True<br>x=103, returna True
- [ ] x=102, retorna False<br>x=103, returna False
- [ ] x=102, retorna True<br>x=103, returna False
- [X] x=102, retorna False<br>x=103, returna True

## Pregunta 4

Si queremos importar la función **randint** del módulo **random**, ¿cuál es/son
formas correctas de hacerlo, y de luego utilizar la función?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  import random
  a = random.randint(1, 10)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from random import randint
  a = randint(1, 10)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from random import *
  a = randint(1, 10)
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  from random import *
  a = random.randint(1, 10)
  ```
  </span>

## Pregunta 5

¿Qué hace la siguiente función? 

```python
def funcion_misteriosa(x):
    c = 0
    while x != 0:
        c += 1
        x = x // 10
    return c
```

- [ ] Siempre retorna 0
- [X] Retorna el número de dígitos del número x
- [ ] Retorna el número de x dividido en 10.
- [ ] Retorna un dígito del número x

## Pregunta 6

¿Cuál/es de las siguientes es una definición de función que SÍ es válida?

- [X] `def hola(chao): `
- [X] `def blabla():`
- [X] `def m_90(a, b, c, d, e, f):`
- [ ] `def while(x, y):`

## Pregunta 7

¿Cuál código es correcto para una función que reciba un número N y
entregue 1+2+3+4+...+N?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def suma(N):
    s = 0
    for i in range(N):
        s += i
    return s + N
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def suma(N):
    s = 0
    for i in range(N-1):
            s += i
    return s + N
  ```
  </span>

- [ ] <span>
  ```python
  def suma(N):
    s = 0
    for i in range(N):
            s += i
    return s
  ```
  </span>

- [ ] <span>
  ```python
  def suma(N):
    s = 0
    for i in range(N-1):
        s += i
    return s
  ```
  </span>

## Pregunta 8

Indica cuál es la línea de código **incorrecta** en la siguiente función.

```python
def f(x, y):
    print("Funcion f")
    return x**2 + y**2
    print("Final de la función")
```

- [ ] 1: `def f(x, y):`
- [ ] 2: `print("Funcion f")`
- [ ] 3: `return x**2 + y**2`
- [X] 4: `print("Final de la función")`

## Pregunta 9

Dada la siguiente función:

```python
def funcion(x, y):
    return (x - 8) * (y ** 2)

funcion(16, 1)
```

¿Qué **imprime** el programa?

- [ ] 8
- [X] No imprime nada

## Pregunta 10

¿Cómo hacemos para importar la variable pi del módulo math, pero con el nombre
valor_pi?

- [ ] `from math import pi is valor_pi`
- [ ] `import math, pi as valor_pi`
- [ ] `valor_pi is pi from math import *`
- [X] `from math import pi as valor_pi`
