# Instrucciones Condicionales

## Pregunta 1

¿De las siguientes opciones, cuál es una manera inválida de implementar una
condición en un programa Python?
- [ ] if sin else
- [X] else sin if
- [ ] if con else
- [ ] if, con varios elif, sin else al final

## Pregunta 2

En una competencia de cantantes, si las tres personas del jurado le dan una "X"
al participante, éste queda eliminado. De las siguientes, ¿cuál sería una
manera de escribir esa condición?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  if jurado1 =="X" and jurado2 =="X" and jurado3 == "X":
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  if jurado1, jurado2, jurado3 == "X":
  ```
  </span>

- [ ] <span>
  ```python
  if jurado1 and  jurado2 and jurado3 == "X":
  ```
  </span>

- [ ] <span>
  ```python
  if jurado1 == "X" or jurado2 == "X" or jurado3 == "X":
  ```
  </span>

## Pregunta 3

En algunos países, la mayoría de edad se cumple a los 18 años. ¿Cúal es el código
correcto para escribir un programa que determine si un usuario es mayor de edad
o no?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>
  ```python
  edad = int(input("Ingresa tu edad: "))
  if edad > 18:
      print("Eres mayor de edad")
  else:
      print("Eres menor de edad")
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  edad = int(input("Ingresa tu edad: "))
  if edad >= 18:
      print("Eres mayor de edad")
  print("Eres menor de edad")
  ```
  </span>

- [ ] <span>
  ```python
  edad = int(input("Ingresa tu edad: "))
  if edad > 18:
      print("Eres mayor de edad")
  else:
      print("Eres menor de edad")
  ```
  </span>

- [ ] <span>
  ```python
  edad = int(input("Ingresa tu edad: "))
  if edad >= 18:
      print("Eres mayor de edad")
  else:
      print("Eres menor de edad")
  ```
  </span>

## Pregunta 4

¿Qué imprime el siguiente código?

```python
a = 15
b = 10
if a == b:
    print("Son iguales")
    print("Adiós")
else:
    print("Son distintos")
    print("Adiós")
print("a y b son dos números")
```

- [ ] <p>Son distintos<br>Adios<p>
- [ ] <p>Son distintos<br>a y b son dos números<p>
- [ ] <p>Son iguales<br>Adios<br>a y b son dos números<p>
- [X] <p>Son distions<br>Adios<br>a y b son dos números<p>

## Pregunta 5

¿Cuál es el error que presenta el siguiente código?

```python
c = float(input("Ingrese temperatura del agua"))
if c <= 0:
    print("Su agua está congelada")
elif c >= 0 and c < 100:
    print("Su agua está líquida") 
elif:
    print("Su agua está hirviendo")
```

- [ ] No hay else
- [X] Existe un elif sin condición.
- [ ] Se utilizan dos elif en vez de uno.
- [ ] Se compara un número que es float(real) con números enteros dentro de las condiciones.

## Pregunta 6

¿Qué imprime el siguiente código?

```python
n = 20
if (n <= 100 and n % 2 == 0) or (n < 5):
    if n != 21:
        print("1")
    else:
        print("2")
else:
    if n == 20:
        print("3")
    else:
        print("4")
```

- [X] 1
- [ ] 2
- [ ] 3
- [ ] 4

## Pregunta 7

Para definir la calidad del aire se hace una medición de partículas presentes en
este. Dependiendo de su valor se definen 5 posibles estados de calidad de aire:\
<br>
**Bueno**: 0-99\
<br>
**Regular**: 100-199\
<br>
**Alerta**: 200-299\
<br>
**Premergencia**: 300-499\
<br>
**Emergencia**: 500-Superior\
<br>
Esto quiere decir si la medición es de menos de 99, la calidad es **buena**, si la
medición es de menos de 199, pero más de 100 es **regular**, etc.\
<br>
(Fuente: http://portal.mma.gob.cl/pronostico-rm/)\
<br>
Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del
aire:

```python
numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
    print("Bueno")
elif numero >= 100 and numero <= 199:
    print("Regular")
elif numero >= 200 and numero <= 299:
    print("Alerta")
elif numero >= 300 and numero <= 499:
    print("Preemergencia")
else:
    print("Emergencia")
```

¿Qué imprime el código anterior si el usuario ingresa un valor menor a 0?

- [ ] No imprime nada
- [ ] El programa señala que hay un error
- [X] Emergencia
- [ ] Bueno, Regular, Alerta, Preemergencia y Emergencia

## Pregunta 8

Para definir la calidad del aire se hace una medición de partículas presentes en
este. Dependiendo de su valor se definen 5 posibles estados de calidad de aire:\
<br>
**Bueno**: 0-99\
<br>
**Regular**: 100-199\
<br>
**Alerta**: 200-299\
<br>
**Premergencia**: 300-499\
<br>
**Emergencia**: 500-Superior\
<br>
Esto quiere decir si la medición es de menos de 99, la calidad es **buena**, si la
medición es de menos de 199, pero más de 100 es **regular**, etc.\
<br>
(Fuente: http://portal.mma.gob.cl/pronostico-rm/)\
<br>
Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del
aire:

```python
numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
    print("Bueno")
if numero >= 100 and numero <= 199:
    print("Regular")
if numero >= 200 and numero <= 299:
    print("Alerta")
if numero >= 300 and numero <= 499:
    print("Preemergencia")
else:
    print("Emergencia")
```

¿Qué imprime el código anterior si el usuario ingresa el valor 163?

- [ ] Bueno
- [ ] Regular
- [X] Regular<br>Emergencia
- [ ] Bueno<br>Regular<br>Alerta<br>Emergencia

## Pregunta 9

Queremos escribir un programa que imprima "par" si un número es par, y nada en
otro caso. ¿Cuál es el código correcto para esto?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>
  ```python
  numero = int(input("Ingrese numero"))
  if numero % 2 == 0:
      print("Es par")
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  numero = int(input("Ingrese numero"))
  if numero/2==0:
      print("Es par")
  ```
  </span>

- [ ] <span>
  ```python
  numero = int(input("Ingrese numero"))
  if numero//2==0:
      print("Es par")
  ```
  </span>

- [ ] <span>
  ```python
  numero = int(input("Ingrese numero"))
  if numero%2==0:
      print("Es par")
  else:
      print("Es impar")
  ```
  </span>

## Pregunta 10

Se conoce como año bisiesto a un año que tiene un día extra. Todo año bisiesto
debe cumplir alguna de las siguientes condiciones:

1. Debe ser divisible por 4, pero no por 100.
2. Debe ser divisible por 100, pero no por 400.

Por ejemplo, 1996 es año bisiesto porque cumple la condición uno. Por otro lado
1900 no lo es, ya que no cumple ninguna de las condiciones.\
<br>
¿Cuál de las siguientes condiciones es la que permite determinar si un año A es bisiesto?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>
  ```python
  if (A % 4 == 0 and A % 100 != 0) or (A % 100 == 0 and A % 400 == 0):
      print("Es bisiesto")
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  if A % 400 == 0:
      print("Es bisiesto")
  ```
  </span>

- [ ] <span>
  ```python
  if A % 4 or (A % 100 and A % 400):
      print("Es bisiesto")
  ```
  </span>

- [ ] <span>
  ```python
  if A % 100 == 0 and A % 4 == 0 and A % 400 ==0:
      print("Es bisiesto")
  ```
  </span>
