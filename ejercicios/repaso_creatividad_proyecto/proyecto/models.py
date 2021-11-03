from abc import ABC, abstractmethod


class Poligono(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base * 3


class Cuadrilatero(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2


class Pentagono(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (5 * (self.lado ** 2)) / (4 * (3 ** 0.5))

    def perimetro(self):
        return self.lado * 5


class Hexagono(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (6 * (self.lado ** 2)) / (4 * (2 ** 0.5))

    def perimetro(self):
        return self.lado * 6


class Octagono(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (8 * (self.lado ** 2)) / (4 * (3 ** 0.5))

    def perimetro(self):
        return self.lado * 8


class TrianguloIsoceles(Triangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def perimetro(self):
        return self.base * 2 + self.altura * 2


class TrianguloEquilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.lado = lado

    def perimetro(self):
        return self.lado * 3


class Rectangulo(Cuadrilatero):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def perimetro(self):
        return self.base * 2 + self.altura * 2


class Cuadrado(Cuadrilatero):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4