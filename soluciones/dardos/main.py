"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from functools import reduce
from typing import Dict, List, Tuple, Union

CHARS = 3
INITIAL_SCORE = 501
MULTIPLIER = {"DOUBLE BULL": 50, "SINGLE BULL": 25, "NULL": 0}
PlayerData = Dict[str, Union[str, int]]


def prod(iterable): # 3.8 > from math import prod
    return reduce(lambda x, y: x * y, iterable, 1)


def validate(line: str) -> bool:
    if line.replace(" ", "").isalpha() and line in MULTIPLIER.keys():
        return True
    elif line.replace(" ", "").isdigit():
        return True
    return False


def get_names(size: int = 2) -> Tuple[str, str]:
    while True:
        try:
            players = tuple(
                input("Ingrese los nombres de los jugadores: ").split()
            )
            if len(players) == size:
                return players
            else:
                print("Usar espacio en blanco para separar los nombres")
        except ValueError:
            print("Ingrese dos nombres separados por un espacio en blanco")


def set_players(names: Tuple[str, str]) -> PlayerData:
    a, b = names
    suffix = ("", "2") if a[:CHARS] == b[:CHARS] else ("", "") 
    return [
        {"name": n, "nick": n[:CHARS].upper() + s, "score": INITIAL_SCORE}
        for n, s in zip(names, suffix)
    ]


def calculate_score(data: List[int]) -> int:
    return sum(
        prod(map(int, item.split()))
        if item not in MULTIPLIER else MULTIPLIER[item] 
        for item in data
    )


def show_score(players: PlayerData) -> None:
    for player in players:
        print(f"{player['nick']} {player['score']}")
    print()


def read_turn() -> Tuple[bool, List[str]]:
    data = []
    for _ in range(3):
        _data = input()
        if validate(_data):
            data.append(_data)
        else:
            return False, data
    return True, data


def main():
    players = set_players(get_names())
    show_score(players)
    while True:
        for i in range(len(players)):
            ok, data = read_turn()
            if ok:
                players[i]["score"] -= calculate_score(data)
                if players[i]["score"] < 0:
                    players[i]["score"] = players[i]["score"] * -1
            else:
                print("No se pudo calcular el puntaje")
                exit(1)
        print()
        show_score(players)
        if any(player["score"] == 0 for player in players):
            break
    winner = [player for player in players if player["score"] == 0][0]
    print(f"Gana {winner['name']}! Felicitaciones.")


if __name__ == "__main__":
    main()
