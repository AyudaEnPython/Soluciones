from typing import Dict, List

Data = Dict[str, set]
TENDENCIAS: Data = {
    "08-22-2019": {"#Rio2019", "#BSC", "#ECU"},
    "08-25-2019": {"#GYE", "#BSC"},
    "08-27-2019": {"#BRA", "#YoSoyUpch", "#GYE", "#BSC"},
}
FECHAS: List[str] = ["08-22-2019", "08-25-2019", "08-27-2019"]


def cuenta_etiquetas(tendencias: Data, fechas: List[str]) -> Dict[str, int]:
    t = {}
    for fecha in fechas:
        for etiqueta in tendencias[fecha]:
            if etiqueta not in t:
                t.setdefault(etiqueta, 1)
            else:
                t[etiqueta] += 1
    return t 


def reporta_tendencias(tendencias: Data, fechas: List[str]) -> None:
    todas_las_fechas = set(
        tendencias[fechas[0]]
    ) if fechas[0] in tendencias else set()
    al_menos_una_fecha = set()
    for fecha in fechas:
        if fecha in tendencias:
            al_menos_una_fecha.update(tendencias[fecha])
            todas_las_fechas.intersection_update(tendencias[fecha])
    print(f"Etiquetas que fueron tendencia en todas las fechas:")
    for etiqueta in todas_las_fechas:
        print(etiqueta)
    print(f"Etiquetas que fueron tendencia al menos en un fecha:")
    for etiqueta in al_menos_una_fecha:
        print(etiqueta)


def main():
    print(cuenta_etiquetas(TENDENCIAS, FECHAS))
    reporta_tendencias(TENDENCIAS, FECHAS)


if __name__ == "__main__":
    main()
