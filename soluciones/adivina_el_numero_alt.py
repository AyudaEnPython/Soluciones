"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import sample

LIMITE, MIN, MAX, SIZE, tries = 20, 1, 21, 4, 0
rnd_numbers = sample(range(MIN, MAX), SIZE)


while tries < LIMITE:
    print(f"¡Guess the numbers! {tries + 1}° try!")
    guessed_n = int(input("> "))
    tries += 1
    if guessed_n in rnd_numbers:
        rnd_numbers.pop()
        if len(rnd_numbers) == 0:
            print("¡You win! You've guessed all the numbers!")
            break
        print(f"You guessed one number! {len(rnd_numbers)} left.")
    else:
        print("You didn't guessed any number!.")
else:
    print(f"You lost! The numbers were: {', '.join(map(str, rnd_numbers))}.")
