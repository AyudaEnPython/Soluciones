"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

¿Por qué el 6174 es el número más misterioso del mundo?

Vamos a hacer magia con los números. Tan solo tienes que realizar los
siguientes pasos:

- Elige un número de 4 cifras que esté formado por al menos dos dígitos
    diferentes. Por ejemplo: 1324.
- Ordena las cifras de forma descendente. En nuestro ejemplo anterior
    sería: 4321.
- Ahora ordena las cifras de forma ascendente, es decir, de menor a
    mayor: 1234.
- Resta al número mayor el más pequeño: 4321 - 1234 = 3087.

Ahora te toca repetir los tres últimos pasos con la cifra que nos ha
dado:

Ordenamos de forma ascendente: 0378
Hacemos lo mismo de forma descendente: 8730
Realizamos la resta: 8730 - 378 = 8352
Repetimos la operacíon y:
    
    8532 - 2358 = 6174

¡Magia! Siempre vamos a acabar llegando a la misma cifra. Podemos
hacerlo en bucle con distintos números que la operación se va a
repetir.
"""
from random import sample


def _f(xs):
    return "".join(str(x) for x in xs)


def get_ns():
    return _f(sample(range(10), k=4))


def f(xs):
    return int(_f(sorted(xs, reverse=True))), int(_f(sorted(xs)))


def show(i, x, y, xs):
    print(f"{i}: {x} - {y} = {xs}")


def main():
    xs = get_ns()
    k = 0
    while True:
        k += 1
        x, y = f(xs)
        xs = str(x - y)
        show(k, x, y, xs)
        if xs == "6174":
            break


if __name__ == "__main__":
    main()
