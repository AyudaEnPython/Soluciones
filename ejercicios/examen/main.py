import json
from prototools import int_input, menu_input


def max_level(data, class_=None):
    _d = sorted(data, key=lambda x: x[-2], reverse=True)
    if not class_:
        return _d[0][0]
    for n, _, k, *_ in _d:
        if class_ == k:
            return n


def increment(data, name):
    for i, (n, *before, lvl, w) in enumerate(data):
        if name == n:
            data[i] = (n, *before, lvl+1, w)
            return


def find_character(data):
    character = menu_input([n for n, *_ in data], prompt="Ingresar nombre: \n", numbers=True)
    for n, age, *_ in data:
        if n == character:
            return n, age


def guess_game(name, age):
    while True:
        user_guess = int_input("Edad: ")
        if user_guess == age:
            print(f"Exacto! {name} tiene {age}")
            return
        print(f"{name} es {'menor' if user_guess > age else 'mayor'}")


def main():
    with open("./data/db.json") as f:
        data = json.load(f)
    level = sum(level for (*_, level, _) in data) // len(data)
    players = [name for name, *_, in_game in data if in_game]
    classes = set(k for _, _, k, *_ in data)
    players_by_race = {k:[k for _, _, _, k, *_ in data].count(k) for _, _, _, k, *_ in data }
    print(f"{level}")
    verify = lambda x: x in [k for _, _, _, k, *_ in data]
    print(f"{players}")
    print(f"{classes}")
    print(f"{players_by_race}")
    print(f"{verify('Human')}")
    print(f"{verify('Gnome')}")
    print(max_level(data))
    print(max_level(data, "Druid"))
    print(data)
    increment(data, "Gale")
    print(data)
    # guess_game(*find_character(data))


if __name__ == "__main__":
    main()
