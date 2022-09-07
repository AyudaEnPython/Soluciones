"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

... factorial de una lista del 1-20, solo mostrando o filtrando los
números que sean impares por medio de filter. Es decir, de la lista:

lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
]

mapea el factorial pero filtra pero filtra para que solo aparezca el
factorial de 1, 3, 5, 7, 9, 11, 13, 15, 17 y 19.

Nota: Recuerda que la lista1 no la debes recortar, la elección de los
números a los cuales vas a aplicar el factorial lo harás con la función
filter y la función map deberán quedar en una sola línea, aclarando que
para la elección de los números impares usarás la función lambda o
anónima... todo en una sola línea.

NOTE: el enunciado esta incompleto.
"""
# js
# const f = n => n ? n * f(n-1) : 1; console.log(Array.from({length: 20}, (v, k) => k+1).filter((n) => n%2==1).map(f));  # noqa: E501

f = lambda n: 1 if n <= 1 else n*f(n - 1); print(*map(f, filter(lambda x: x % 2, range(1, 21))))  # noqa: E731, E501, E702
