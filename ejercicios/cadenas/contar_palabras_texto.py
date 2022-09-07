"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Contar la cantidad de palabras del texto

NOTA: No es necesario recorrer cada palabra del texto y reemplazar los
    caracteres como el . , ; ! etc. Basta con usar split() para separar
    las palabras (espacio en blanco) y convertirlas en conjunto (set)
    para eliminar los duplicados. Luego, usar len() para devolver el
    tamaño del conjunto.
"""

texto = """Puck ve a Nick Bottom y los otros jugadores ensayando en el
bosque, y convierte la cabeza de Nick Bottom en cabeza de burro,
asustando a los otros jugadores. Titania se despierta con la poción en
sus ojos y instantáneamente se enamora del Bottom de cabeza de burro.
Oberon toma su changeling y arregla Puck para invertir la poción y
convencer a todo el mundo que sólo estaban soñando. Demetrius ama a
Helena ahora, así que Hermia es libre de casarse con Lysander. El rey
Theseus decide que todas las parejas deben casarse. Puck termina la
obra sugiriendo a la audiencia que la obra pudo haber sido un sueño.
"""

print(len(set(texto.split())))  # output: 73
