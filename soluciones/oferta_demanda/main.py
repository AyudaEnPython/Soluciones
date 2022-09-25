import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

q = sy.symbols('q')


def S(q, b):
    return q**2 + b*10


def D(q):
    return (q - 20)**2


def plot_eq(eq, color, start=0, end=16, alpha=None, label=None):
    x = np.linspace(start, end, 1000)
    y = [eq.subs(q, i) for i in np.linspace(start, end, 1000)]
    plt.plot(x, y, color, alpha=alpha, label=label)


def plot_inter(eq1, eq2):
    ex = sy.solve(eq1 - eq2)[0]
    w = eq1.subs(q, ex)
    plt.scatter([ex], [w], color='red')


def plot_sol(q, start, end):
    for b in range(start, end+1):
        plot_eq(S(q, b), "g", alpha=b*0.1, label=r"$\beta=%d$" % b)
        plot_inter(S(q, b), D(q))
    plot_eq(D(q), "b", label="Demanda")
    plt.legend()
    plt.show()


def main():
    plot_sol(q, 1, 10)


if __name__ == "__main__":
    main()
