"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
tipos = ['arabe', 'turco', 'cafe latte', 'cappuccino', 'ristretto']
ingredientes = [
    ('cardamomo', 1, 'arabe'),
    ('agua', 2, 'espresso, cappuccino'),
    ('whisly irlandes', 2, 'irlandés'),
    ('agua', 3, 'americano, turco'),
]


def ingredientes_cafe(tipo, ingredientes):
    return [i[:2] for i in ingredientes if tipo in i[2]]


print(ingredientes_cafe('cappuccino', ingredientes))
