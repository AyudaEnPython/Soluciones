# Enunciado Original

Para saber si un número es divisible por 7, hay que restar el número sin
la cifra de las unidaddes y el doble de la cifra de las unidades. Si el
resultado es cero o múltiplo de 7, entonces el número es divisible por 7.
Si el resultado es diferente, el número no es divisible por 7.

Tenga en cuenta que sólo se le permite usar el operador módulo (n%7) si n
es menor que 100.

Se entiende mejor con un ejemplo: ¿1946 es divisible por 7?

Separamos la cifra de las unidades 194, 6. Ahora restamos el número 194
menos el doble de la cifra de las unidades 2*6 = 12 (194 - 12 = 182). Como
182 todavía es un número muy grande, repetimos los pasos:

Separamos la cifra de las unidades 18, 2. Restamos el número 18 menos el
doble de la cifra de las unidades 2*2 = 4 (18 - 4 = 14). 14 ya no es tan
grande y es múlti´lo de 7 (14%7 == 0).

---

Cree un módulo y dentro de el implemente un función de nombre es_modulo_7
que reciba un número de argumento y retorne verdadero (True) o falso (False)
si el número es múltiplo de 7 o no.
Usted debe utilizar obligatoriamente la metodología explicada anteriormente.

Cree otro módulo donde usted le pregunte al usuario cuántos números necesita
verificar, luego pida los números y conteste lo siguiente:

- Cantidad de múltiplos de 7 que encontró.
- El menor de los múltiplos de 7.
- El mayor de los mútliplos de 7.
- El promedio de los múltiplos de 7.

> __**NOTA**__: El enunciado fue modificado para mejorar la legibilidad del mismo.
