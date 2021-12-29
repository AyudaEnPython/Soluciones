"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add more features later when I have time
"""
from ctypes import py_object, POINTER
from typing import List


class ArregloDinamico:
    """Implementación de un arreglo dinámico.

    :param _n: número de elementos en el arreglo
    :_n type: int
    :param _capacidad: capacidad del arreglo
    :_capacidad type: int
    :param _factor: factor de redimensionamiento
    :_factor type: int
    :param _A: arreglo 
    :_A type: POINTER(py_object)
    """

    def __init__(self, factor: int = 2) -> None:
        self._n = 0
        self._capacidad = 1
        self._factor = max(2, factor)
        self._A = self._crear(self._capacidad)

    def __len__(self) -> int:
        """Devuelve el tamaño del arreglo"""
        return self._n

    def __getitem__(self, k: int) -> py_object:
        """Devuelve el elemento en la posición k

        :param k: posición del elemento
        :k type: int
        :return: elemento en la posición k
        :rtype: py_object
        """
        if 0 <= k < self._n:
            return self._A[k]
        elif k < 0 and self._n + k >= 0:
            return self._A[self._n + k]
        raise IndexError("El indice esta fuera de rango")

    def append(self, obj: py_object) -> None:
        """Agrega un elemento al final del arreglo
        
        :param obj: elemento a agregar
        :obj type: py_object
        """
        if self._n == self._capacidad:
            self._incrementar()
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k: int, obj: py_object) -> None:
        """Inserta un elemento en la posición k
        
        :param k: posición del elemento
        :k type: int
        :param obj: elemento a insertar
        :obj type: py_object
        """
        if k < 0 or k > self._n:
            raise IndexError("El indice esta fuera de rango")
        if self._n == self._capacidad:
            B = self._crear(self._capacidad * self._factor)
            for i in range(self._n + 1):
                if i < k:
                    B[i] = self._A[i]
                elif i == k:
                    B[i] = obj
                else:
                    B[i] = self._A[i - 1]
            self._A = B
            self._capacidad *= self._factor
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i - 1]
            self._A[k] = obj
        self._n += 1

    def remove(self, obj: py_object) -> None:
        """Remueve la primera ocurrencia de un elemento del arreglo

        :param obj: elemento a remover
        :obj type: py_object
        """
        for k in range(self._n):
            if self._A[k] == obj:
                for i in range(k, self._n - 1):
                    self._A[i] = self._A[i + 1]
                self._n -= 1
                self._reducir()
                return
        raise ValueError("El elemento no existe")

    def remove_all(self, obj: py_object) -> None:
        """Remueve todas las ocurrencias de un elemento del arreglo

        :param obj: elemento a remover
        :obj type: py_object
        """
        B = self._crear(self._n)
        i = 0
        for k in range(self._n):
            if self._A[k] != obj:
                B[i] = self._A[k]
                i += 1
        self._n = i
        self._A = B

    def pop(self) -> py_object:
        """Remueve el ultimo elemento del arreglo

        :return: el ultimo elemento del arreglo
        """
        if self._n < 1:
            return None
        r = self._A[self._n - 1]
        for i in range(self._n - 1):
            self._A[i] = self._A[i + 1]
        self._n -= 1
        self._reducir()
        return r

    def _reducir(self) -> None:
        """Reduce la capacidad del arreglo si es necesario"""
        if self._n < self._capacidad // self._factor ** 2:
            self._redimensionar(self._capacidad // self._factor)

    def _incrementar(self) -> None:
        """Incrementa la capacidad del arreglo"""
        self._redimensionar(self._capacidad * self._factor)

    def _redimensionar(self, c: int) -> None:
        """Redimensiona el arreglo

        :param c: nueva capacidad del arreglo
        :c type: int
        """
        B = self._crear(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacidad = c

    @staticmethod
    def sumar_for(arr: List[List[int]]) -> int:
        """Suma los elementos de un arreglo

        :param arr: arreglo
        :arr type: List[List[int]]
        :return: suma de los elementos del arreglo
        :rtype: int
        """
        suma = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                suma += arr[i][j]
        return suma

    @staticmethod
    def sumar_lc(arr: List[List[int]]) -> int:
        """Suma los elementos de un arreglo

        :param arr: arreglo
        :arr type: List[List[int]]
        :return: suma de los elementos del arreglo
        :rtype: int
        """
        return sum([sum(i) for i in arr])

    @staticmethod
    def _crear(c: int) -> POINTER(py_object):
        """ Crea un arreglo dinamico de capacidad `c`

        :param c: capacidad del arreglo
        :c type: int
        :return: arreglo dinamico
        :rtype: POINTER(py_object)
        """
        return (c * py_object)()

    def __str__(self) -> str:
        return str(self._A[:self._n])