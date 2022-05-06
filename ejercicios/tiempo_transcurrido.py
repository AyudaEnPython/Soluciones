"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Encontrar el tiempo transcurrido entre la hora inicial y la hora final
de cada usuario los cuales están almacenados en diccionarios tal y como
se puede observar:

u = [
    {'user': 'Ignazio Marino', 'date':'25/02/2022','inicial': '07:29:05 am'},
    {'user': 'Ignazio Marino', 'date':'25/02/2022','final': '04:20:05 pm'},
    {'user': 'Ignazio Marino1', 'date':'25/02/2022','inicial': '01:27:05 pm'},
    {'user': 'Ignazio Marino1', 'date':'25/02/2022','final': '04:27:05 pm'}
]

NOTE: La persona que solicito ayuda no coloco el enunciado original. La
    estructura de los datos no es la óptima, si lo fuese "cleanup" y
    "get_users" no serían necesarias.
"""
from datetime import datetime
from typing import Dict, List

users = [
    {'user': 'Ignazio Marino', 'date':'25/02/2022','inicial': '07:29:05 am'},
    {'user': 'Ignazio Marino', 'date':'25/02/2022','final': '04:20:05 pm'},
    {'user': 'Ignazio Marino1', 'date':'25/02/2022','inicial': '01:27:05 pm'},
    {'user': 'Ignazio Marino1', 'date':'25/02/2022','final': '04:27:05 pm'}
]


def cleanup(users: List[Dict[str, str]], name: str) -> Dict[str, str]:
    data = {}
    for user in [user for user in users if user['user'] == name]:
        data.update(user)
    return data


def get_users(users: List[Dict[str, str]]):
    return tuple(set(user['user'] for user in users))


def tiempo(inicial: str, final: str, format_: str = '%I:%M:%S %p') -> int:
    inicial = datetime.strptime(inicial, format_)
    final = datetime.strptime(final, format_)
    return (final - inicial)


def main():
    users_ = get_users(users)
    for user_ in users_:
        user = cleanup(users, user_)
        print(f"{user_} -> {tiempo(user['inicial'], user['final'])}")


if __name__ == "__main__":
    main()
