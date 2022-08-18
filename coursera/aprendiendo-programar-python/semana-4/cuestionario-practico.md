# Cuestionario Práctico

# Pregunta 1

Existen múltiples formas de calcular el máximo común divisor de un conjunto de
números, escriba una función de nombre _mcd_ que reciba dos números **n1** y
**n2** como argumentos, y **retorne** el máximo común divisor. Por ejemplo
para los argumentos 10 y 15 debe retornar 5.

```python
def # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
```

# Pregunta 2

Para muchas aplicaciones matemáticas, conocer la potencia de 2 más grande que
es menor o igual a cierto número, es muy útil. Escribe una función _exponente_,
que dado un número _n_, **retorne** el exponente de dicha potencia de 2 más grande.
Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶  = 64.

```python
def # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
```

# Pregunta 3

Considere que existen los números primos y los números pandigitales. Los números
pandigitales son aquellos que contienen todos los dígitos del 0 al 9 al menos una
vez, como el 1023478695. Escribe una función _panprimo_ que determine si un número
_n_ es pandigital y si al mismo tiempo, sus últimos 3 dígitos conforman un número
primo, **retornando** _True_ o _False_ según corresponda. Por ejemplo:

1) El número 2424643 cumple que sus últimos 3 dígitos conforman un número primo (643),
  pero no es pandigital por lo tu función que debería retornar _False_.

2) El número 1234567890 cumple que es pandigital, pero sus últimos 3 dígitos no
  conforman un primo (890), por lo que tu función debería retornar _False_.

3) El número 10123485769 cumple que es pandigital y además el número conformado por
  sus 3 últimos dígitos (769) es primo, por lo que debería retornar _True_.

_Tip1: Puedes convertir un entero a una cadena de texto con el método _**str(numero)**_, y
puedes verificar si alguna letra está en el esta cadena de texto haciendo _**if letra in string: ...**__

_Tip2: Un número es primo si solo es divisible por 1 y por sí mismo. Para obtener
los últimos tres dígitos, puedes obtener el resto del número en su división con **100**._

```python
def # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
```
