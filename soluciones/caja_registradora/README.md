# Enunciado Original

El objetivo de este ejercicio es que aprendas a penssar y modelar objetos, 
con sus atributos y métodos.

Abordaremos el problema de modelar una caja registradora básica. Para el
primer ejercicio solamente se te pide que tu caja registradora pueda
calcular el total de los productos comprados. Para ello, considera que en
un supermercado de verdad cada producto tiene un código único llamdo SKU;
es el mismo que aparece en el código de barras. Aquí vamos a usar SKU de
una sola letra: A, B, C, etc.

## Iteración 1: Calcular el total

Tu clase se debe llamar CajaRegistradora y debe tener tres métodos:

- inscribir (sku, precio) sirve para indicarle a la caja registradora que
  un SKU tiene un determinado precio.
- registrar (sku), ocurre cuando el cajero usa el lector de código de barras
  para registrar la compra de un SKU.
- calcular_total() devuelve la suma total de las compras.

Por ejemplo, si yo ejecuto el siguiente código...

```python
caja = CajaRegistradora()
caja.inscribir("A", 62.0)
caja.inscribir("B", 145.5)
caja.inscribir("C", 140.5)
caja.registrar("C")
caja.registrar("A")
caja.registrar("A")
caja.registrar("B")
print(caja.calcular_total())
```

esperaría ver el siguiente resultado: `410.0`

Puede ocurrir que el código de barras esté dañado o no exista dicho SKU en nuestra
tienda, en ese caso tu clase debería de arrojar un KeyError. Ejemplo:

```python
caja = CajaRegistradora()
caja.inscribir("A", 21.0)
caja.registrar("X")
```

    -------------------------------------------------
    KeyError        Traceback (most recent call last)
    ...

    KeyError: 'X'

Es el mismo error que obtendrías haciento esto:

```python
diccionario = {"A": 0, "B": 1}
diccionario["X"]
```