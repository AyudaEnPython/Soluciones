Un polinomio de grado <img src="https://render.githubusercontent.com/render/math?math=n">
es una función matemática de la forma:

<p align="center" width="100%">
<img src="https://render.githubusercontent.com/render/math?math=p(x) = a_{0} %2B a_{1}x %2B a_{2}x^{2} %2B a_{3}x^{3} %2B \ldots %2B a_{n}x^{n}">
</p>

Donde <img src="https://render.githubusercontent.com/render/math?math=x"> es
el parámetro y <img src="https://render.githubusercontent.com/render/math?math=a_{0}, a_{1}, \ldots, a_{n}">
son números reales dados.

Algunos ejemplos de polinomios son:
* <img src="https://render.githubusercontent.com/render/math?math=p(x) = 1 %2B 2x %2B x^2">
* <img src="https://render.githubusercontent.com/render/math?math=q(x) = 4 - 17x">
* <img src="https://render.githubusercontent.com/render/math?math=r(x) = -1 -5x^3 %2B 3x^5">
* <img src="https://render.githubusercontent.com/render/math?math=s(x) = 5x^40 %2B 2x^80">

Los grados de estos polinomios son, respectivamente 2, 1, 5 y 80.

Evaluar un polinomio significa reemplazar <img src="https://render.githubusercontent.com/render/math?math=x"> por
un valor y obtener el resultado. Por ejemplo, si evaluamos el polinomio <img src="https://render.githubusercontent.com/render/math?math=p">
en el valor <img src="https://render.githubusercontent.com/render/math?math=x=3">,
obtenemos el resultado:

<p align="center" width="100%">
<img src="https://render.githubusercontent.com/render/math?math=p(3) = 1 %2B (2\cdot3) %2B 3^2 = 16">
</p>

Un polinomio puede ser representado como una lista con los valores
<img src="https://render.githubusercontent.com/render/math?math=a_{0}, a_{1}, \ldots, a_{n}">.
Por ejemplo, los polinomios anteriores pueden ser representados así en un programa:

```python
>>> p = [1, 2, 1]
>>> q = [4, -17]
>>> r = [-1, 0, 0, -5, 0, 3]
>>> s = [0]*40 + [5] + [0]*39 + [2]
```

a) Escriba la función `grado(p)` que entregue el grado de un polinomio:
```python
>>> grado(r)
5
>>> grado(s)
80
```

b) Escriba la función `evaluar(p, x)` que evalúe el polinomio `p` (representado
como una lista) en el valor `x`:
```python
>>> evaluar(p, 3)
16
>>> evaluar(q, 0.0)
4.0
>>> evaluar(r, 1.1)
-2.82347
>>> evaluar([4, 3, 1], 3.14)
23.2796
```

c) Escriba la función `sumar_polinomios(p, q)` que entregue la suma de dos polinomios:
```python
>>> sumar_polinomios(p, r)
[0, 2, 1, -5, 0, 3]
```

d) Escriba la función `derivar_polinomio(p)` que entregue la derivada de un polinomio:
```python
>>> derivar_polinomio(p)
[0, 0, -15, 0, 15]
```

e) Escriba la función `multiplicar_polinomios(p, q)` que entregue el producto de dos polinomios:
```python
>>> multiplicar_polinomios(p, q)
[4, -9, -30, -17]
```