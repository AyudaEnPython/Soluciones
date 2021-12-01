Las sumas de Riemann sirven para el cáculo aproximado de áreas y se define como

<p align="center" width="100%">
<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} {\Delta}x.{f(x_{i})}">
</p>

en donde la función <img src="https://render.githubusercontent.com/render/math?math=\ f">
representa la función continua en el intervalo
<img src="https://render.githubusercontent.com/render/math?math=\ [a, b]"> que
genera una curva,
<img src="https://render.githubusercontent.com/render/math?math=\ n"> representa
el número de particiones, 
<img src="https://render.githubusercontent.com/render/math?math=\Delta x = \frac{b-a}{n}">representa
el tamaño de las particiones y 
<img src="https://render.githubusercontent.com/render/math?math=\ x_{i} = a + {\Delta}x.i"> representa
un punto en cada partición.

Considere ahora al función
<img src="https://render.githubusercontent.com/render/math?math=\f(x) = x^2 %2B 6x %2B 3"> y
que se desea calcular el área bajo la curva en
<img src="https://render.githubusercontent.com/render/math?math=\ a {\leq} x {\leq} b">. Escribir
un programa con dos funciones:

* `f()` que reciba un número real `x` y devuelva el resultado de evaluar dicho
  número en la función _*f*(x)_ de acuerdo con su definición.

* `Riemann()` que reciba los límites del intervalo `a`, `b` y el número de
  particiones `n`, calcule las sumas de Riemann para la función _*f*(x)_ y devuelva
  el resultado.