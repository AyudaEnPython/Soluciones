Un polinomio de grado $n$
es una función matemática de la forma:
$$p(x) = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3} + \ldots + a_{n}x^{n}$$

Donde $x$ es el parámetro y $a_{0}, a_{1}, \ldots, a_{n}$ son números reales dados.

Algunos ejemplos de polinomios son:
* $p(x) = 1 + 2x + x^2$
* $q(x) = 4 - 17x$
* $r(x) = -1 -5x^3 + 3x^5$
* $s(x) = 5x^{40} + 2x^{80}$

Los grados de estos polinomios son, respectivamente 2, 1, 5 y 80.

Evaluar un polinomio significa reemplazar $x$ por un valor y obtener el resultado.
Por ejemplo, si evaluamos el polinomio $p$ en el valor $x=3$, obtenemos el resultado:
$$p(3) = 1 + (2\cdot3) + 3^2 = 16$$


Un polinomio puede ser representado como una lista con los valores $a_{0}, a_{1}, \ldots, a_{n}$.
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