"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os


def continuar():
    print("Presione cualquier tecla para continuar...")
    input()
    os.system("cls" if os.name == "nt" else "clear")


def depositar(balance):
    n = float(input("Cuánto quieres depositar: "))
    if n < 0:
        print("No puedes depositar una cantidad negativa")
    else:
        balance += n
        print(f"Acabas de depositar: {n:.2f}")
    return balance


def retirar(balance):
    n = float(input("Cuánto quieres retirar: "))
    if n > balance:
        print ("Saldo insuficiente")
    else:
        balance -= n
        print(f"Acabas de retirar: {n:.2f}")
    return balance


def saldo(balance):
    print(f"Saldo restante: {balance:.2f}")


def cajero():
    balance = 0
    while True:
        print("1.- Depositar")
        print("2.- Retirar")
        print("3.- Saldo")
        print("4.- Salir\n")
        print("Ingrese la opción que desea realizar:")
        opcion = input("> ")
        os.system("cls" if os.name == "nt" else "clear")
        if opcion == "4":
            print("Hasta la próxima")
            break
        elif opcion == "1":
            balance = depositar(balance)
        elif opcion == "2":
            balance = retirar(balance)
        elif opcion == "3":
            saldo(balance)
        else:
            print("Opción no válida")
        continuar()


def main():
    print("Quieres entrar al cajero? (s)i o (n)o?")
    if input("> ").lower() in "si":
        cajero()
    else:
        print("Hasta la próxima")


if __name__ == "__main__":
    main()
