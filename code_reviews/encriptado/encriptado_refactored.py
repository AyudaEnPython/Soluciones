"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

KEYS = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}


def get_data(filename):
    with open(filename) as f:
        return f.read()


def decrypt(data):
    result = ""
    for word in data.split():
        result += f'{"".join([KEYS.get(c, c) for c in word[::-1]])} '
    return result


def longest_word(data):
    return max(data.split(), key=len)


def main():
    data = get_data('code_reviews/encriptado/mensaje.txt')
    print("Mensaje cifrado:", data)
    print(data)
    decrypted = decrypt(data)
    longest = longest_word(decrypted)
    print(f"\nPalabra con mayor numero de caracteres: {longest}")
    print(f"Numero de caracteres: {len(longest)}")
    print("\nMensaje descifrado:")
    print(decrypted)


if __name__ == "__main__":
    main()
