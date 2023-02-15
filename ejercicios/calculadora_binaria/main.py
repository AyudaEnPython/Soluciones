"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calculadora Binaria
-------------------

Diseñar un programa que realice las operaciones básicas de la suma,
resta, multiplicación y división de números reales, de manera binaria
con capacidad máxima de 512 bits, recuerden que el número binario esta
conformado por el bit de signo + los bits de la mantisa o el número a
operar.

Dados lso siguientes números binarios:
A = (110011)_2
B = (0101011)_2
C = (101011.101)_2
D = (001010101.011)_2

Realice las siguientes operaciones:
A + B, A - B, B - A, C + D, -A - B, C - D, A * B, B / A, B * C, D / A
"""
from operator import add, sub, mul, truediv

_T = {"+": add, "-": sub, "*": mul, "/": truediv}
hex2bin = dict('{:x} {:04b}'.format(x, x).split() for x in range(16))
bin2hex = dict('{:b} {:x}'.format(x, x).split() for x in range(16))


def float_dec2bin(d):
    neg = False
    if d < 0:
        d = -d
        neg = True
    hx = float(d).hex()
    p = hx.index('p')
    bn = ''.join(hex2bin.get(char, char) for char in hx[2:p])
    return (('-' if neg else '') + bn.strip('0') + hx[p:p+2]
            + bin(int(hx[p+2:]))[2:])


def float_bin2dec(bn):
    neg = False
    if bn[0] == '-':
        bn = bn[1:]
        neg = True
    dp = bn.index('.')
    extra0 = '0' * (4 - (dp % 4))
    bn2 = extra0 + bn
    dp = bn2.index('.')
    p = bn2.index('p')
    hx = ''.join(
        bin2hex.get(bn2[i:min(i+4, p)].lstrip('0'), bn2[i])
        for i in range(0, dp+1, 4)
    )
    bn3 = bn2[dp+1:p]
    extra0 = '0' * (4 - (len(bn3) % 4))
    bn4 = bn3 + extra0
    hx += ''.join(
        bin2hex.get(bn4[i:i+4].lstrip('0'))
        for i in range(0, len(bn4), 4)
    )
    hx = (
        ('-' if neg else '') + '0x' + hx + bn2[p:p+2]
        + str(int('0b' + bn2[p+2:], 2))
        )
    return float.fromhex(hx)


def _converter(n: int) -> int:
    while n > 1:
        n /= 10
    return n


def bin_to_int(n: str) -> int:
    return int(n, 2)


def int_to_bin(n: int) -> str:
    return bin(n).replace("0b", "")


def bin_to_float(ns: str) -> float:
    n, f = ns.split(".")
    return int(n, 2) + int(f, 2) / 2**len(f)


def float_to_bin(ns, places=3):
    n, f = ns.split(".")
    n, f = int(n), int(f)
    r = bin(n).lstrip("0b") + "."
    for _ in range(places):
        n, f = str((_converter(f))*2).split(".")
        f = int(f)
        r += n
    return r


def f(x, op, y):
    if "." in x:
        x = bin_to_float(x)
    else:
        x = bin_to_int(x)
    if "." in y:
        y = bin_to_float(y)
    else:
        y = bin_to_int(y)
    print(f"x: {x} | y: {y}")
    r = (_T[op](x, y))
    print(r)
    if isinstance(r, float):
        return float_dec2bin(r).replace("p", ".").replace("+", "")
    return int_to_bin(r)


def main():
    a = "110011"
    b = "0101011"
    c = "101011.101"
    d = "001010101.011"
    print(f(a, "+", b))
    print(f(a, "-", b))
    print(f(b, "-", a))
    print(f(c, "-", d))


if __name__ == "__main__":
    main()
