Las sumas de Riemann sirven para el cáculo aproximado de áreas y se define como
$$\sum_{i=1}^{n} {\Delta}x.{f(x_{i})}$$

en donde la función $f$ representa la función continua en el intervalo $[a, b]$
que genera una curva,
$n$ representa el número de particiones,
$\Delta x = \frac{b-a}{n}$ representa el tamaño de las particiones y
$x_{i} = a + {\Delta}x.i$ representa un punto en cada partición.

Considere ahora al función $f(x) = x^2 + 6x + 3$ y que se desea calcular el área
bajo la curva en $a {\leq} x {\leq} b$. Escribir un programa con dos funciones:

* `f()` que reciba un número real `x` y devuelva el resultado de evaluar dicho
  número en la función _*f*(x)_ de acuerdo con su definición.

* `Riemann()` que reciba los límites del intervalo `a`, `b` y el número de
  particiones `n`, calcule las sumas de Riemann para la función _*f*(x)_ y devuelva
  el resultado.
