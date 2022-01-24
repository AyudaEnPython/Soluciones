"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado el polinomio y=x^4-3x^2+2 calcular el valor de y para valores de x
que varían en el rango -2, +2 con incremento de 0,1.

NOTE: added plot
"""
import matplotlib.pyplot as plt

H = 0.1


def f(x: float) -> float:
    return x**4 - 3*x**2 + 2


def main():
    puntos = [x*H for x in range(-20, 21)]
    for punto in puntos:
        print(f"{punto:.2f} -> {f(punto):.2f}")
    plt.plot(puntos, [f(x) for x in puntos])
    plt.show()


if __name__ == '__main__':
    main()