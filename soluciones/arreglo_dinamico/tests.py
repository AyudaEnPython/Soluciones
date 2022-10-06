"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add more tests (private methods)
"""
from unittest import main, TestCase

from main import ArregloDinamico


class Test(TestCase):

    def test_len(self):
        arreglo = ArregloDinamico()
        self.assertEqual(len(arreglo), 0)

    def test_getitem(self):
        arreglo = ArregloDinamico()
        with self.assertRaises(IndexError):
            arreglo[0]

    def test_append(self):
        arreglo = ArregloDinamico()
        arreglo.append(1)
        self.assertEqual(len(arreglo), 1)
        self.assertEqual(arreglo[0], 1)

    def test_insert(self):
        arreglo = ArregloDinamico()
        arreglo.append(1)
        arreglo.insert(0, 2)
        self.assertEqual(len(arreglo), 2)
        self.assertEqual(arreglo[0], 2)
        self.assertEqual(arreglo[1], 1)

    def test_remove(self):
        arreglo = ArregloDinamico()
        arreglo.append(1)
        arreglo.append(2)
        arreglo.remove(1)
        self.assertEqual(len(arreglo), 1)
        self.assertEqual(arreglo[0], 2)

    def test_remove_all(self):
        arreglo = ArregloDinamico()
        arreglo.append(1)
        arreglo.append(2)
        arreglo.append(2)
        arreglo.append(2)
        arreglo.append(2)
        arreglo.append(1)
        arreglo.remove_all(2)
        self.assertEqual(len(arreglo), 2)

    def test_pop(self):
        arreglo = ArregloDinamico()
        arreglo.append(1)
        arreglo.append(2)
        arreglo.append(3)
        self.assertEqual(arreglo.pop(), 3)
        self.assertEqual(len(arreglo), 2)

    def test_crear(self):
        arreglo = ArregloDinamico()
        arr = arreglo._crear(5)
        self.assertEqual(len(arr), 5)


if __name__ == "__main__":
    main()
