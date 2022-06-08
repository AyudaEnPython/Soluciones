"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realiza un programa que sume los números primos que se encuentran en
una colección de números del 1 - 100 utilizando Reduce. La colección
del 1 - 100 debe ser una lista creada a partir de un iterable o un
ciclo for, no manualmente.

Nota: Debes crear la lista completa del 1 al 100 y después filtrarla
con Filter para obtener los números primos. Toda esa maniobra en una
sola línea.
""" 

# js
# console.log(Array.from({length: 100}, (v, k) => k+1).filter((n) => ![...Array(n).keys()].slice(2).map(i => !(n%i)).includes(true) && ![0,1].includes(n)).reduce((x, y) => x + y));

# python
from functools import reduce; print(reduce(lambda x, y: x + y, list(filter(lambda x: all(x % i != 0 for i in range(2, x)), list(range(1, 101))[1:]))))
