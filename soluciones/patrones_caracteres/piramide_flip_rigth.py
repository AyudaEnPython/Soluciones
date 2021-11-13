"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Imprimir el patrón siguiente usando bucles:

    +---------------+
    | *             |
    | * *           |
    | * * *         |
    | * * * *       |
    | * * * * *     |
    | * * * *       |
    | * * *         |
    | * *           |
    | *             |
    +---------------+

NOTE: add more implementations
"""
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")
