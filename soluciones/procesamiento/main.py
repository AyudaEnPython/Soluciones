"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Tuple

Data = List[Tuple[str, ...]]


def get_data(filename: str) -> Data:
    with open(filename, 'r') as f:
        return [tuple(line.strip().split(';')) for line in f]


def main():
    d: Data = get_data('data.csv')

    # Ejercicio 1:
    print(f"{sum(int(col[1]) for col in d)}")

    # Ejercicio 2:
    print("\n".join(f"{s},{[col[0] for col in d].count(s)}" for s in "ABCDE"))

    # Ejercicio 3:
    d_ = {k: 0 for k in "ABCDE"}
    for k, v in [(col[0], int(col[1])) for col in d]:
        d_[k] += v
    print("\n".join(f"{k},{d_[k]}" for k in d_))
    
    # Ejercicio 4:
    m = sorted(col[2][5:-3] for col in d)
    d_ = dict((x, m.count(x)) for x in m)
    print("\n".join(f"{k},{d_[k]}" for k in d_))

    # Ejercicio 5:
    d_ = {k: [] for k in "ABCDE"}
    for k, v in [(col[0], col[1]) for col in d]:
        d_[k].append(int(v))
    print("\n".join(f"{k},{max(d_[k])},{min(d_[k])}" for k in d_))

    # Ejercicio 6:
    d_ = {k: [] for k in (k*3 for k in "abcdefghij")}
    for ss in [col[-1].split(",") for col in d]:
        for s in ss:
            k, v = s.split(":")
            d_[k].append(int(v))
    print("\n".join(f"{k},{min(d_[k])},{max(d_[k])}" for k in d_))

    # Ejercicio 7:
    d_ = {str(k): [] for k in range(10)}
    for k, v in [(col[1], col[0]) for col in d]:
        d_[k].append(v)
    print("\n".join(f"{i}" for i in list(d_.items())))
    
    # Ejercicio 8:
    d_ = {str(k): [] for k in range(10)}
    for k, v in [(col[1], col[0]) for col in d]:
        d_[k].append((v))
        d_[k] = sorted(list(set(d_[k])))
    print("\n".join(f"{i}" for i in list(d_.items())))

    # Ejercicio 9:
    d_ = {k: [] for k in (k*3 for k in "abcdefghij")}
    for s in [col[-1].split(",") for col in d]:
        for i in s:
            k, v = i.split(":")
            d_[k].append(int(v))
    print("\n".join(f"{k},{len(d_[k])}" for k in d_))

    # Ejercicio 10:
    print("\n".join([
        f"{e[0]},{len(e[-2].split(','))},{len(e[-1].split(','))}"
        for e in d
    ]))
    
    # Ejercicio 11:
    d_ = {k: [] for k in "abcdefg"}
    for v in [{s:int(col[1]) for s in col[3].split(',')} for col in d]:
        for k in v:
            d_[k].append(v[k])
    print("\n".join(f"{k},{sum(d_[k])}" for k in d_))

    # Ejercicio 12:
    print("\n".join([
        f"{s},{sum(int(s.split(':')[1]) for s in ss.split(','))}"
        for s, ss in [(col[0], col[-1]) for col in d]
    ]))


if __name__ == "__main__":
    main()
