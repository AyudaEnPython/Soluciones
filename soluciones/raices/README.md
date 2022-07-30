# Enunciado Original

## Cálculo de la raíz cúbica con una fórmula iterativa

La raíz cúbica del número _X_ puede calcularse mediante la fórmula iterativa

$$S_{i+1} = \frac{2}{3}.S_{i} + \frac{1}{3}.\frac{X}{(S_{i})^2}$$

Este procedimiento puede iniciarse dando a $S_{i}$ el valor $1$.

Escriba un programa de computadora para obtener raices cúbicas de esta manera.
Para propósitos informativos, imprímase el valor de $S$ en cada iteración.
Termine el proceso una vez que la diferencia entre dos iteraciones sucesivas
sea menor de 0.01%.
La fórmula es cierta tanto para valores positivos como negativos de $X$. Su
programa debe incluir ambas posibilidades. Utilícelo para $X = 235$ y $X = -91.6$

## Raiz cuadrada con otro método iterativo

Otra manera de formular el método para resolver la raíz cuadrada de un número es
el siguiente. Para calcular la raíz cuadrada de un número $B$ selecciónese
cualquier número $r_{1}$ y con ellos calcúlese $h_{1}$ tal que

$$h_{1} = \frac{b}{r_{1}}$$

A continuación encuéntrese el promedio entre $r_{1}$ y $h_{1}$ y desígnese con $r_{2}$:

$$r_{2} = \frac{r_{1} + h_{1}}{2}$$

El siguiente $h_{2}$ es igual a:

$$h_{2} = \frac{b}{r_{2}}$$

El proceso puede generalizarse mediante las expresiones:

$$h_{i} = \frac{b}{r_{i}}$$

y

$$r_{i+1} = \frac{r_{i} + h_{i}}{2}$$

Ambas sucesiones se aproximan a la raíz cuadrada de $B$. Para detener el proceso,
utilizamos el criterio $| r_{i1} - h_{i}| < \epsilon$ para un $\epsilon$ predeterminado.
Utilice el programa para calcular las raíces cuadradas de $4590$ y $32323$, para un
valor inicial de $r_{1} = 1$ y $\epsilon = 0.000001$.
