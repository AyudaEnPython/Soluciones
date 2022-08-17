# Instrucciones Cíclicas

## Pregunta 1

Determinar el valor de _x_ al final del siguiente código:

```python
x = 1
i = 0
while i < 4:
    x = x * 2
    i += 1 # es lo mismo que i = i + 1
print(x)
```

- [X] 16
- [ ] 8
- [ ] 1
- [ ] 4


## Pregunta 2

Al final de este código:

```python
x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1
```

El valor de _n_ es:

- [ ] x - y
- [X] x // y
- [ ] x ** y
- [ ] y / x

## Pregunta 3

Considerando las variables del siguiente código:

```python
a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r) 
```

El _output_ del mismo es equivalente a imprimir:

- [ ] a / b
- [ ] b ** a
- [ ] a ** b
- [X] a * b

## Pregunta 4

Determina una opción que entregue el mismo resultado que el código a continuación:

```python
a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)
```

- [X] b ** a
- [ ] a * b
- [ ] a / b
- [ ] a ** b

## Pregunta 5

¿Cuál es el valor de a tras la ejecución de este programa?

```python
a = 3
for i in range(2, 3):
    a = a * i
```

- [ ] 2
- [ ] 18
- [ ] 3
- [X] 6

## Pregunta 6

¿Qué debería ir en lugar de OBJECT en el siguiente código?

```python
a = 2
for i in OBJECT:
    a = i ** a
print(a)
```

Para que ésta imprima _9_

- [ ] range(3)
- [X] range(1, 4)
- [ ] range(1, 3)
- [ ] range(1, 2)

## Pregunta 7

Determine lo que debiese ir en lugar de OBJECT para que el siguiente código

```python
for i in OBJECT:
    print('hola mundo')
```

Imprima 10 veces _'hola mundo'_

- [X] range(10)
- [ ] range(0, 9)
- [ ] range(11)
- [ ] range(3, 12)

## Pregunta 8

Determine lo que imprime este programa

```python
a = 0
for i in range(3):
    a = a + i
print(a)
```

- [ ] 6
- [X] 3
- [ ] 5
- [ ] 4

## Pregunta 9

¿Qué hace el siguiente código?

```python
numero = 1
while numero <= 5:
    print(numero, numero**2)
```

- [ ] Escribe los números del 1 al 5 ("1", "2", "3", "4", "5") y a continuación los números del 1 al 5 al cuadrado. ("1", "4", "9", "16", "25")
- [ ] Escribe los números del 1 al 5 acompañados de ese mismo número al cuadrado ("1 1", "2 4", "3 9", "4 16", "5 25")
- [X] Escribe "1 1" infinitas veces.
- [ ] Escribe los números del 1 al 5 acompañados de ese mismo multiplicado por 2 ("1 2", "2 4", "3 6", "4  8", "5 10")

## Pregunta 10

¿Qué imprime el siguiente código?

```python
for i in range(1,101):
  for j in range(1,101):
    print(i,j)
```

- [ ] Los números del 1 al 100, y luego los números del 1 al 100 nuevamente.
- [ ] Los números del 1 al 10000 (100*100)
- [ ] Por cada número del 1 al 100, imprime el mismo número desde el 1 al 100, por lo tanto imprime 1 1, 2 2, 3 3, 4 4, ..., 100 100
- [X] Para cada número del 1 al 100, imprime los números del 1 al 100, por lo tanto imprime 1 1, 1 2, 1 3, 1 4, ..., 1 100, 2 1, 2 2, 2 3, ..., 100 100
