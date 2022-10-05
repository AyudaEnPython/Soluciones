"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from abc import ABC, abstractmethod


class Transaccion(ABC):

    @abstractmethod
    def ejecutar(self) -> None:
        ...
