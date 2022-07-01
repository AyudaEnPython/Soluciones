"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Taking as base the Mario Kart v1.0 program implement the next improves:

- The start position should be validated between 1 and 12 only.
- The last position must be 12 at the most, if the player is in 12th
    position and is attacked, he can't be in a position higher than 12.
- In each attack there is the possible of a random shortcut, it could
    happened or not, and it will saved 2 places.
- "Surprised effect": In a random way; it could happened or not, if the
    player is in the 5 first places and the "Surprised effect" happens;
    the player will be delay 1 place.

NOTE: There's no code for v1.0.
"""
from random import getrandbits
from typing import Any, Dict, List, Optional, Union
# pip install prototools
from prototools import int_input, menu_input, bool_input

MIN, MAX = 1, 12
ITEMS: Dict[str, int] = {
    "pump": 1,
    "banana": 1,
    "green turtle": 2,
    "red turtle": 3,
}
BONUS: Dict[str, int] = {
    "star": 1,
    "cannon": 2,
}


def _should_happen() -> bool:
    return bool(getrandbits(1))


def _pos_after_attack(pos: int, n: int) -> int:
    t = pos + ITEMS[n]
    if t > MAX:
        return MAX
    return t


def _activate_bonus(pos: int, bonus: str) -> int:
    t = pos - BONUS[bonus]
    if t < MIN:
        return MIN
    return t


def random_shortcut(pos: int) -> int:
    if _should_happen():
        print("You've found a shortcut!")
        return pos - 2
    return pos


def surprise_effect(pos: int) -> int:
    if _should_happen():
        if pos <= 5:
            print("Surprise effect! You will be delay 1 place")
            return pos + 1
    return pos


def attack_phase(pos: int, atk: int) -> int:
    print(f" Attack: {atk} ".center(40, "*"))
    print("\nWhich object attacked you?")
    item = menu_input(tuple(ITEMS.keys()), numbers=True)
    pos = _pos_after_attack(pos, item)
    pos = random_shortcut(pos)
    print(f"You are in position {pos}")
    return pos


def start_game(pos: int, attacks: int) -> int:
    for atk in range(1, attacks+1):
        print()
        pos = attack_phase(pos, atk)
        if bool_input(
            "Do you need help? (y/n): ", true_value="y", false_value="n"
        ):
            print("Which object will help to you?")
            bonus = menu_input(tuple(BONUS.keys()), numbers=True)
            pos = _activate_bonus(pos, bonus)
        print(f"You are in position {pos}")
        pos = surprise_effect(pos)
    return pos


def main():
    pos = int_input("Give me your position: ", min=MIN, max=MAX)
    atk = int_input("Tell me how many attacks will be: ", min=1)
    print(f"You start in position {pos}")
    print(f"You'll have {atk} attacks")
    pos = start_game(pos, atk)
    print(f"Your final position is: {pos}")


if __name__ == "__main__":
    main()
