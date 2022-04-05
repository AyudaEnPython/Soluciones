"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import Tuple


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/simulador_dado.py
def lanzar(n: int = 2) -> Tuple[str, int]:
    """Lanza 'n' dados al azar. Devuelve un tupla con la representación
    de los dados lanzados y la suma de estos.

    :param n: Número de dados a lanzar, por defecto 2
    :type n: int
    :returns: Tupla (representación, suma)
    :rtype: Tuple(str, int)
    """
    caras = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    dados = [randint(1, 6) for _ in range(n)]
    return " ".join(caras[dado-1] for dado in dados), sum(dados)


def verificar(suma: int, punto: int, i: int) -> Tuple[bool, str]:
    """Verifica la suma de dados.

    :param suma: Suma de los dados
    :type suma: int
    :param punto: Punto
    :type punto: int
    :param i: Número de lanzamientos
    :type i: int
    :returns: Booleano y mensaje
    :rtype: Tuple[bool, str]
    """
    if i == 0:
        if suma in (7, 11):
            return True, "Ganaste!"
        elif suma in (2, 3, 12):
            return True, "Perdiste!"
        return False, ""
    else:
        if suma == 7:
            return True, "Perdiste!"
        if punto == suma:
            return (
                True, f"Ganaste en {i+1} lanzamientos! Tu punto fue {punto}."
            )
        return False, ""


def game() -> None:
    """Juego de dados.

    Si en el primer lanzamiento se obtiene 7 o 11 se gana; si se
    obtiene 2, 3, o 12, se pierde; de lo contrario el resultado
    se guarda como punto y se continúa el juego. Si se obtiene 7
    antes de obtener el punto, pierde; de lo contrario, gana y se
    muestra el número de lanzamientos y el punto.
    """
    punto = i = 0
    while True:
        input("Presionar 'Enter' para lanzar los dados... ")
        dados, suma = lanzar()
        print(f"{dados} = {suma}")
        if i == 0:
            punto = suma
        flag, msg = verificar(suma, punto, i)
        if flag:
            print(msg)
            break
        i += 1


if __name__ == "__main__":
    while True:
        game()
        if input("¿Jugar de nuevo? (s/n): ").lower() != "s":
            break
    print("¡Hasta luego!")
