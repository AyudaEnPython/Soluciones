"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import timedelta
from typing import List
# pip install prototools
from prototools.validators import validate_time  # noqa: F401


def sumar_tiempos_1(tiempos: List[str]) -> str:
    t = timedelta()
    for tiempo in tiempos:
        (h, m, s) = tiempo.split(":")
        t += timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    return str(t)


def sumar_tiempos_2(tiempos):
    t = timedelta()
    for tiempo in tiempos:
        h, m, s = [int(s) for s in tiempo.split(":")]
        t += timedelta(hours=h, minutes=m, seconds=s)
    return str(t)


def sumar_tiempos_3(tiempos: List[str]) -> str:
    return str(sum(map(
        lambda hms: timedelta(
            hours=int(hms.split(":")[0]),
            minutes=int(hms.split(":")[1]),
            seconds=int(hms.split(":")[2]),
        ),
        tiempos,
    ), timedelta()))


def sumar_tiempos_4(tiempos: List[str]) -> str:
    return str(sum([
        timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        for tiempo in tiempos for h, m, s in [tiempo.split(":")]
    ], timedelta()))


def sumar_tiempos_5(tiempos: List[str]) -> str:  # using prototools
    return sum([
        timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        for t in tiempos
    ], timedelta())


def sumar_tiempos_6(tiempos: List[str]) -> str:  # no days
    ss = 0
    for tiempo in tiempos:
        h, m, s = [int(s) for s in tiempo.split(":")]
        ss += (h * 3600) + (m * 60) + s
    ss, s = divmod(ss, 60)
    h, m = divmod(ss, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    tiempos = ["18:30:58", "14:32:04"]
    print(sumar_tiempos_1(tiempos))
    # print(sumar_tiempos_2(tiempos))
    # print(sumar_tiempos_3(tiempos))
    # print(sumar_tiempos_4(tiempos))
    # print(sumar_tiempos_5([validate_time(t) for t in tiempos]))
    # print(sumar_tiempos_6(tiempos))


if __name__ == "__main__":
    main()
