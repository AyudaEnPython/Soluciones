"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""
from random import choice

TRIES = 5
WORDS = "rainbow computer science programming python mathematics \
player condition reverse water board geeks".split()


def show_word(word, guesses):
    return " ".join(letter if letter in guesses else "_" for letter in word)


def user_input(word, guessed):
    while True:
        guess = input("Enter a guess: ").lower()
        if guess == word:
            return True, guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter!")
        elif guess in guessed:
            print("You've already guessed that guess!")
        else:
            return False, guess


def check(word, guesses):
    return all(letter in guesses for letter in word)


def play(word):
    tries, guessed = TRIES, ""
    while tries != 0:
        print(f"Remaining attempts: {tries}")
        print(show_word(word, guessed))
        won, guess = user_input(word, guessed)
        if won:
            print("You win!")
            return
        if guess in word:
            guessed += guess
            if check(word, guessed):
                print("You win!")
                return
        else:
            tries -= 1
    print("You lose!")
    print(f"The word was: {word}")


def main():
    while True:
        play(choice(WORDS))
        print("Do you want to play again? (y/n): ")
        if not input().lower().startswith("y"):
            return


if __name__ == "__main__":
    main()
