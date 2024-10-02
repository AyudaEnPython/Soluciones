

def traducir(frase: str) -> str:
    t = {
        "a": "ka", "b": "tu", "c": "mi", "d": "te", "e": "ku",
        "f": "lu", "g": "ji", "h": "ri", "i": "ki", "j": "zu",
        "k": "me", "l": "ta", "m": "rin", "n": "to", "o": "mo",
        "p": "no", "q": "ke", "r": "shi", "s": "ari", "t": "chi",
        "u": "do", "v": "ru", "w": "mei", "x": "na", "y": "fu",
        "z": "ra", " ": " ",
    }
    return "".join(t[letra] for letra in frase.lower())


def main():
    frase = input("Ingrese una frase: ")
    print(f"La pronunciación en japonés es: {traducir(frase)}")


if __name__ == "__main__":
    main()
