"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from utils import get_data, es_multiplo_7


def main():
    numeros = get_data()
    multiplos_7 = [n for n in numeros if es_multiplo_7(n)]
    print(f"Cantidad de números multiplos de 7: {len(multiplos_7)}")
    print(f"Menor número multiplo de 7: {min(multiplos_7)}")
    print(f"Mayor número multiplo de 7: {max(multiplos_7)}")
    print(
        f"Promedio de los números multiplos de 7: "
        f"{sum(multiplos_7)/len(multiplos_7)}"
    )


if __name__ == "__main__":
    main()
