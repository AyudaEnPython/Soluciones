from typing import Dict

Empleados = Dict[str, Dict[str, int]]
EMPLEADOS: Empleados = {
    "María": {
        "UPCH": 50, "INEI": 10, "SUNAT": 0,
        "FACEBOOK": 160, "YOUTUBE": 20, "TWITTER": 50,
    },
    "Jose": {
        "UPCH": 40, "INEI": 5, "SUNAT": 150,
        "FACEBOOK": 0, "YOUTUBE": 25, "TWITTER": 10,
    },
    "Javier": {
        "UPCH": 5, "INEI": 10, "SUNAT": 20,
        "FACEBOOK": 30, "YOUTUBE": 50, "TWITTER": 40,
    },
}


def tiempo_total_internet(empleados: Empleados) -> Dict[str, int]:
    return {k: sum(v.values()) for k, v in empleados.items()}


def empleado_sitios_diversion(empleados: Empleados) -> str:
    return max({
        k: v["FACEBOOK"] + v["YOUTUBE"] + v["TWITTER"]
        for k, v in empleados.items()
    }.keys())


def sitio_trabajo_mas_usado(empleados: Empleados) -> str:
    t = {"UPCH": 0, "INEI": 0, "SUNAT": 0}
    for sitios in empleados.values():
        for sitio in t:
            t[sitio] += sitios[sitio]
    return max(t, key=t.get)


def costo_total_uso_internet(empleados: Empleados) -> float:
    t = 0
    for sitios in empleados.values():
        for sitio, tiempo in sitios.items():
            if sitio in ("UPCH", "INEI", "SUNAT"):
                t +=  tiempo * 0.15
            else:
                t +=  tiempo * 0.30
    return t


def visitas(empleados: Empleados) -> Dict[str, int]:
    t = {
        k: 0
        for k in ("UPCH", "INEI", "SUNAT", "FACEBOOK", "YOUTUBE", "TWITTER")
    }
    for sitios in empleados.values():
        for sitio, tiempo in sitios.items():
            if tiempo > 0:
                t[sitio] += 1
    return t


def main():
    print("Tiempo total de uso de internet por empleado:")
    for empleado, tiempo in tiempo_total_internet(EMPLEADOS).items():
        print(f"- {empleado}: {tiempo} minutos.")
    print("El empleado con más tiempo en sitios de diversión es: ")
    print(f"- {empleado_sitios_diversion(EMPLEADOS)}.")
    print("El sitio de trabajo mas visitado es:")
    print(f"- {sitio_trabajo_mas_usado(EMPLEADOS)}")
    print("El costo total es:")
    print(f"- S/.{costo_total_uso_internet(EMPLEADOS): .2f}")
    print("Cantidad total de empleos que han visitado cada sitio:")
    for sitio, cantidad in visitas(EMPLEADOS).items():
        print(f"- {sitio}: {cantidad} empleados.")


if __name__ == "__main__":
    main()
