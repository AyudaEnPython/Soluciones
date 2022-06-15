"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una pista de Kart permite 10 vueltas por cada uno de los 6 corredores.
Implemente un programa que lea todos los tiempos en segundos y los
almacene en un diccionario, donde la clave sea el nombre del corredor.
Al final, diga quién fue la mejor vuelta de la carrera y en qué vuelta;
y la clasificación final en orden (1° el campeón). El campeón es el que
tiene el promdeio de tiempos más bajo.
"""
from typing import Dict, List, Tuple

CORREDORES, VUELTAS = 6, 10


def get_data() -> Dict[str, List[int]]:
    data = {}
    for _ in range(CORREDORES):
        name = input("Nombre del corredor: ")
        data[name] = [
            float(input(f"[{i+1}] Tiempo en segundos: "))
            for i in range(VUELTAS)
        ]
    return data


def _min_time(times: List[int]) -> Tuple[int, int]:
    min_ = min(times)
    return min_, times.index(min_)


def best_lap(data: Dict[str, List[int]]) -> Tuple[int, str, int]:
    mins = [_min_time(times) for times in data.values()]
    best_lap, i = min(mins, key=lambda x: x[0])
    best_lap_name = list(data.keys())[mins.index((best_lap, i))]
    return best_lap, best_lap_name, i+1


def final_time(data: Dict[str, List[int]]) -> Dict[str, float]:
    return {
        name: sum(times)/len(times) for name, times
        in sorted(data.items(), key=lambda x: x[1])
    }


def main():
    data = get_data()
    sec, name, lap = best_lap(data)
    print("\nResultados:")
    print(
        f"La mejor vuelta es de {sec} segundos, en la vuelta "
        f"{lap} del corredor {name}"
    )
    print("\nClassificación final:")
    for i, (name, time) in enumerate(final_time(data).items(), 1):
        print(f"{i}° Lugar -> {name}: {time:.2f} segundos")


if __name__ == "__main__":
    main()
