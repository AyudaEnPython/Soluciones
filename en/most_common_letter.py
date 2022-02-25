"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""
from collections import Counter


def most_common_letter(s: str) -> str:
    """Returns the most common letter in a string."""
    return Counter(s).most_common(1)[0][0]


def main():
    word = input("Enter a word: ")
    print(most_common_letter(word))


if __name__ == '__main__':
    main()
