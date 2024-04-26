"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import RangeDict, text_align

P = RangeDict({
    (0, 0): 10,
    (1, 2): 8,
    (3, 5): 6,
    (6, 9): 4,
    (9, 100): 0,
})
R = {0: 10, 1: 8, 2: 5, 3: 1}
B = RangeDict({
    (0, 11): 2.5,
    (11, 13): 5.,
    (14, 13): 7.5,
    (17, 13): 10.,
    (20, 20): 12.5,
})


def main():
    empleado = {
        "tardanza": 2, 
        "observaciones": 3, 
    }
    p = P[empleado["tardanza"]]
    r = R.get(empleado["observaciones"], 0)
    t = p + r
    b = B[t]
    text_align("Resultados", align="center")
    text_align(f"Puntualidad: {p}")
    text_align(f"Rendimiento: {r}")
    text_align(f"Total: {t}")
    text_align(f"Bonificación: {b}")


if __name__ == "__main__":
    main()
