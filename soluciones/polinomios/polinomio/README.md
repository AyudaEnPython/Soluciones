Un polinomio de una variable tiene la forma siguiente:
<p align="center" width="100%">
<img src="https://render.githubusercontent.com/render/math?math=\color{white}P(x) = a_{n}x^n %2B a_{n-1}x^{n-1} %2B \ldots %2B a_{1}x %2B a_{0}, (a_{n} \gt 0)">
</p>

Si el exponente más grande de <img src="https://render.githubusercontent.com/render/math?math=\color{white}x">
es
<img src="https://render.githubusercontent.com/render/math?math=\color{white}x^n">,
se dice que el polinomio es de grado
<img src="https://render.githubusercontent.com/render/math?math=\color{white}n">.
La representación de un polinomio mediante un arreglo de reales empezando
con el término independiente es:
<img src="https://render.githubusercontent.com/render/math?math=\color{white}[a_{0}, a_{1}, \ldots, a_{n}]">.

Por ejemplo, el polinomio
<img src="https://render.githubusercontent.com/render/math?math=\color{white}P(x) = -3x^4 %2B 2x^3 %2B 10x^2 - 5">
se representa por el arreglo de números <img src="https://render.githubusercontent.com/render/math?math=\color{white}a">:
<p align="center" width="100%">
<img src="https://render.githubusercontent.com/render/math?math=\color{white}a = [-5, 0, 10, 2, -3]">
</p>

Nótese que el número de coeficientes, es decir, la longuitud del arreglo
es <img src="https://render.githubusercontent.com/render/math?math=\color{white}n %2B 1"> (el grado del polinomio más uno)
y que <img src="https://render.githubusercontent.com/render/math?math=\color{white}a_{k}"> es el
cociente de <img src="https://render.githubusercontent.com/render/math?math=\color{white}x^k">.

Escribir un programa que lea el grado del polinomio
<img src="https://render.githubusercontent.com/render/math?math=\color{white}n">,
los coeficientes
<img src="https://render.githubusercontent.com/render/math?math=\color{white}[a_{0}, a_{1}, \ldots, a_{n}]"> y
un real
<img src="https://render.githubusercontent.com/render/math?math=\color{white}t">;
calcule con un ciclo `for` el valor de
<img src="https://render.githubusercontent.com/render/math?math=\color{white}P(t) = \sum_{i=0}^n a_{i}x^i"> y
escriba el resultado.