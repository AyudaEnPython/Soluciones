"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


# Pregunta 1
def mezclador(string_a, string_b):
    return string_a[:2] + string_b[-2:]


# Pregunta 2
def intercalar(string_a, string_b):
    t = ""
    for c in string_a:
        t += c + string_b
    return t


# Pregunta 3
def ocurrencias(string):
    return string.count("1") - string.count("0")


# Pregunta 4
def remover_enesimo(s, n):
    return s[:n] + s[n + 1:]


# Pregunta 5
def reemplazo(string):
    s = ""
    for c in string:
        s += "$" if c.isupper() else c
    return s


if __name__ == "__main__":
    assert mezclador("familia", "abrigarse") == "fase"
    assert intercalar("paz", "so") == "psoasozso"
    assert ocurrencias("11000110101") == 1
    assert remover_enesimo("Hasta luego", 3) == "Hasa luego"
    assert reemplazo("Viva la Vida") == "$iva la $ida"
