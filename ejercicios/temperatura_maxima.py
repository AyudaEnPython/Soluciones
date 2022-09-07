"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Las temperaturas mínimas y máximas de algunas ciudades de la V región
están almacenadas en una cadena con el siguiente formato:

"ciudad1:min1:max1,ciudad2:min2:max2, ...,ciudadN:minN:maxN"

Se necesita un programa que muestre por pantalla solamente la
información de las ciudades en donde hubo más de 25 grados de
temperatura máxima.
"""


def oneliner():
    ciudades = (
        "Viña del Mar:9:26,Valparaiso:10:24,Quilpe:7:30,Olmue:5:29,"
        "Limache:9:23,Villa Alemana:9:22"
    )
    print(
        "\n".join(
            f"{s[0]} min {s[1]}, max {s[2]}"
            for s in (c.split(":") for c in ciudades.split(","))
            if int(s[2]) > 25
        )
    )


def main():
    ciudades = (
        "Viña del Mar:9:26,Valparaiso:10:24,Quilpe:7:30,Olmue:5:29,"
        "Limache:9:23,Villa Alemana:9:22"
    )
    for ciudad in ciudades.split(","):
        nombre, min_, max_ = ciudad.split(":")
        if int(max_) > 25:
            print(f"{nombre}: min {min_}, max {max_}")


if __name__ == "__main__":
    # oneliner()
    main()
