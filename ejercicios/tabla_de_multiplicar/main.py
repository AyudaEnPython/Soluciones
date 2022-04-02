"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

while True:
    n = int(input("Ingrese un número: "))
    if n == 0:
        break
    print(f"\nTabla de multiplicar del número {n}\n")
    for i in range(1, 13):
        print(f"{n} x {i:02} = {n*i:02}")
    print("\n")
