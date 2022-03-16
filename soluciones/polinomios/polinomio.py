"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class Termino:

    def __init__(self, coeficiente, exponente) -> None:
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __str__(self) -> str:
        if self.exponente == 0:
            return f"{self.coeficiente}"
        elif self.exponente == 1:
            return f"{self.coeficiente}x"
        else:
            return f"{self.coeficiente}x^{self.exponente}"


class Poliniomio:

    def __init__(self, *terminos) -> None:
        if len(terminos) < 2:
            self.terminos = [terminos]
        else:
            for termino in terminos:
                if not isinstance(termino, Termino):
                    raise TypeError("El argumento no es un termino")
        self.terminos = list(terminos)

    def __str__(self) -> str:
        return " + ".join(map(str, self.terminos))


class Polinomio_:

    def __init__(self, coeficientes) -> None:
        self.coeeficientes = coeficientes
        self.grado = len(coeficientes) - 1


    def __str__(self) -> str:
        s = ""
        for i, c in enumerate(self.coeeficientes):
            if c != 0 and i != self.grado:
                if i == self.grado - 1:
                    s += f"{c}x"
                else:
                    s += f"{c}x^{self.grado - i}"
            elif i == self.grado:
                s += f"{c}"
            if i != self.grado:
                s += " + "
        return s


if __name__ == "__main__":
    p = Poliniomio(Termino(2, 2), Termino(3, 1), Termino(4, 0))
    print(p)

    p_ = Polinomio_([2, 3, 4])
    print(p_)