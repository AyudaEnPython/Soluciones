Un polinomio de una variable tiene la forma siguiente:
$$P(x) = a_{n}x^n + a_{n-1}x^{n-1} + \ldots + a_{1}x + a_{0}, (a_{n} \gt 0)$$

Si el exponente más grande de $x$ es $x^n$, se dice que el polinomio es de
grado $n$.
La representación de un polinomio mediante un arreglo de reales empezando
con el término independiente es: $[a_{0}, a_{1}, \ldots, a_{n}]$.

Por ejemplo, el polinomio $P(x) = -3x^4 + 2x^3 + 10x^2 - 5$ se representa por el
arreglo de números $a$: $$a = [-5, 0, 10, 2, -3]$$

Nótese que el número de coeficientes, es decir, la longuitud del arreglo
es $n + 1$ (el grado del polinomio más uno) y que $a_{k}$ es el cociente de $x^k$.

Escribir un programa que lea el grado del polinomio $n$, los coeficientes
$[a_{0}, a_{1}, \ldots, a_{n}]$ y un real $t$; calcule con un cicle `for` el valor
de $P(t) = \sum_{i=0}^n a_{i}x^i$ y escriba el resultado.