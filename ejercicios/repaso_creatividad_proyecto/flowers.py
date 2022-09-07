"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una clase Flowers que tiene tres propiedades, de tipo int, str
y float, que respectivamente representa el nombre de la flor, su
cantidad de pétalos y su precio. La clase debe incluir un método
constructor que inicialice cada variable con su valor apropiado, y la
clase debe incluir métodos para establecer el valor de cada propiedad y
recuperar el valor de cada propiedad.
"""


class Flowers:

    def __init__(self, name: str, petals: int, price: float) -> None:
        self._name = name
        self._petals = petals
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def petals(self) -> int:
        return self._petals

    @petals.setter
    def petals(self, petals) -> None:
        self._petals = petals

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price) -> None:
        self._price = price
