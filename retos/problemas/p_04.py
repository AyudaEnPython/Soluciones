"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def solver(words: str) -> int:
    for word in words:
        if word in ",.:-":
            words = words.replace(word, " ")
    return len(words.split())


def main():
    s = "Japón, China NorCorea-Italia: Rusia; EEUU.Inglaterra-Brasil"
    print(solver(s.lower()))


if __name__ == "__main__":
    main()
