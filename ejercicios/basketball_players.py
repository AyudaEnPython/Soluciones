"""Dada una lista con la altura de varios jugadores de baloncesto, calcular 
cuantos jugadores estan en el rango de 1 desviación estándar desde el promedio.
.                                              
.                                             +------------------------------+
-4 |*                                         | Fórmulas:                    |
-3 |***                                       | σ = √ (1/N)(∑|x-u|²)      #1 |
-2 |******  «─┐                               | s = √ (1/N-1)(∑|x-u|²)    #2 |
-1 |********  │  «─┐                          |                              |
+0 |********* │    ├─» 1 desviación estándar  | σ, s: Desviación estándar    |
+1 |********  │  «─┘                          | u: media                     |
+2 |******  «─┴──────» 2 desviaciones         | x: valores observados        |
+3 |***                  estándar             |                              |
+4 |*                                         | #1: stdev de una población   |
.                                             | #2: stdev de una muestra     |
.                                             +------------------------------+
Nota: 
    - solucion_a: desviación estándar de una población (usando statistics)
    - solucion_b: desviación estándar de una población (usando un helper)
    - solucion_c: desviación estándar de una muestra (usando statistics)
    - solucion_d: desviación estándar de una muestra (usando un helper)
"""
from statistics import mean, pstdev, stdev
from unittest import main, TestCase

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
dataset = [-2, 0, -1, 4, 0, -1, 3, 0, -2]

def _mean_std_dev(data, sample=True):
    u = sum(data) / len(data)
    return u, (sum(
        (x - u)**2 for x in data)/(len(data)+(-1 if sample else 0))
        )**0.5

def solucion_a(datos):
    u, d = _mean_std_dev(datos, sample=False)
    return len([dato for dato in datos if u - d <= dato <= u + d])

def solucion_b(datos):
    u, d, i = mean(datos), pstdev(datos), 0
    for e in datos:
        if u - d <= e <= u + d:
            i += 1
    return i

def solucion_c(datos):
    u, s = _mean_std_dev(datos, sample=True)
    return len([dato for dato in datos if u - s <= dato <= u + s])

def solucion_d(datos):
    u, s = mean(datos), stdev(datos)
    return len([dato for dato in datos if u - s <= dato <= u + s])


class Test(TestCase):

    def test_solucion_a(self):
        self.assertEqual(solucion_a(players), 6)
        self.assertEqual(solucion_a(dataset), 5)
    
    def test_solucion_b(self):
        self.assertEqual(solucion_b(players), 6)
        self.assertEqual(solucion_b(dataset), 5)
        
    def test_solucion_c(self):
        self.assertEqual(solucion_c(players), 7)
        self.assertEqual(solucion_c(dataset), 5)
    
    def test_solucion_d(self):
        self.assertEqual(solucion_d(players), 7)
        self.assertEqual(solucion_d(dataset), 5)


if __name__ == "__main__":
    main()