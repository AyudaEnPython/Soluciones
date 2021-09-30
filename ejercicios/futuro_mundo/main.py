"""
En archivo de texto plano llamado futuro.mundo se encuentra información
acerca de la población de cada país. Cada línea del archivo tiene el
nombre del país, número de androides que hay, el número de cyborgs, el
de superhumanos y el de humanos simples. El siguiente es un ejemplo de
tal archivo:

Croacia> 234003> 54320> 8904> 3045628
Nepal> 45789832> 5396> 3958> 100
Honduras> 9875> 6732> 23056> 21489
...

Haga un programa en Python que tome todos los datos del archivo y los
almacene en un diccionario. Luego, el programa debe imprimir en
pantalla cuántos países hay en cada una de las tres categorías de
acuerdo a lo siguiente. Si el número de androides y cyborgs sumados es
superior al resto, se considera que un país es categoría Nuevo Mundo.
Si no, y si el número de humanos simples es inferior a la suma de los
otros, se considera que es un país categoría Transición. Y si el número
de humanos simples es mayoría, la categoría es Origen.
El programa debe definir al menos una función.
"""

def get_data(file):
    result, countries = {}, []
    with open(file, "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            data = line.replace(" ", "").split(">")
            countries.append(data[0])
            result[data[0]] = dict(
                androides=int(data[1]),
                cyborgs=int(data[2]),
                superhumanos=int(data[3]),
                humanos=int(data[4]),
            )
    return result, countries


def process(data, countries):
    nuevo_mundo, transicion, origen = [], [], []
    classification = ("androides", "cyborgs", "superhumanos", "humanos")
    for country in countries:
        a, c, s, h = [data[country][kind] for kind in classification]
        if c+a > s+h:
            nuevo_mundo.append(country)
        else:
            if c+a+s > h:
                transicion.append(country)
            elif h > c+a+s:
                origen.append(country)
    return [nuevo_mundo, transicion, origen]


def main():
    data = get_data("futuro.mundo") # ejercicios/futuro_mundo/
    results = process(*data)
    categories = ("Nuevo mundo", "Transicion", "Origen")
    for cat, result in zip(categories, results):
        print(f"{cat}: {len(result)}")


if __name__ == "__main__":
    main()