# Indicaciones específicas

- La tarea consiste en desarrollar un programa que pueda procesar un archivo `.CSV`
  y hacer uso de diccionarios para realizar búsquedas y ordenamientos eficientes. Es
  muy importante que lean **las indiciaciones**. (No está permitido utilizar libreriás
  externas para resolver esta tarea).
- Se puede ver la plantilla de código que deberán de seguir para resolver los ejercicios.
- Ustedes deben escribir dentro de la sección y a la misma altura de donde esta escrito
  _"Código comienza aquí"_. Además, no deben modificar nada debajo de _"Código acaba
  aquí"_. Recuerden tener cuidado con las indentaciones.
- Los input del ejercicio se encuentran en la plantilla. Recuerden usar estas variables
  para resolver el ejercicio.
- La respuesta del ejercicio debe ser retornada según especifique la plantilla otorgada.
- Al momento de retornar el resultado que pide el ejercicio utilizar la estructura
  solicitada. En esta tarea se requiere trabajar con la estructura de diccionarios para
  retornar el resultado.
- No se permite el uso de _built-in functions_ que realicen el trabajo por ustedes como
  los siguientes: `sort`, `sorted`, `max`y `min`.
- En la plantilla se utiliza la siguiente función: `sys.setrecursionlimit()`. Se conoce
  que algunos equipos de Windows presentan un error con esta función. Por lo tanto, se
  les recomienda usar Colab o Replit en ese caso.
- Las respuestas tendrán el máximo puntaje si y solo si cumplen con la complejidad
  indicada.
- El archivo _pokemon.csv_ para que puedan realizar sus pruebas.

# Plantilla

```python
import sys
sys.setrecursionlimit()

# FUNCIONES RECURSIVAS EMPIEZAN AQUI

def merge(left, right):
    merged_list = []
    # SU SOLUCION EMPIEZA AQUI



    # SU SOLUCION TERMINA AQUI
    return merged_list

def merge_sort(lista):
    # SU SOLUCION EMPIEZA AQUI
    left = () # debe implementar el valor correcto de left
    right = () # debe implementar el valor correcto de right

    # SU SOLUCION TERMINA AQUI
    return merge(left, right)

# FUNCIONES RECURSIVAS TERMINAN AQUI

class Solution:

    # NO MODIFICAR ABAJO DE ESTA LINEA, ES PARTE DEL AUTOGRADER
    def sort(self, data=[]):
        return "clear"

    def sorted(self, data=[]):
        return "clear"
    # NO MODIFICAR ARRIBA DE ESTA LINEA, ES PARTE DEL AUTOGRADER

    # ============ Pregunta 1 ============

    def crear_diccionario(self, ruta="pokemon.csv"):
        pokemones = {}
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return pokemones

    # ============ Pregunta 2 ============
    def buscar_dato_pokemon(self, pokemones, id, valor):
        result = ""
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 3 ============
    def pokemon_rapido(self, pokemones):
        result = ()
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 4 ============
    def nombre_ascendente(self, pokemones):
        result = []
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 5 ============
    def busqueda_habilidad(self, nombre_a_buscar, nombres_ordenados, pokemones):
        result = {}
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return result
```
<p align = "center">
Listing 3: <b>Template</b> solution.py
</p>

# Laboratorio del Profesor Oak

Te encuentras trabajando como practicante en el laboratorio del Profesor Oak y te ha
asignado la tarea de analizar el inventario de Pokémones. Él tiene un archivo que
contiene los siguientes datos:

* Name: nombre del Pokémon
* id: Número de identificación correspondiente al Pokémon
* sp_attack: Puntos de ataque del Pokémon
* sp_defense: Puntos de defensa del Pokémon
* speed: Puntos de velocidad del Pokémon
* ability: Lista de habilidades del Pokémon

Un ejemplo del contenido del archivo y el orden de las columnas se puede observar en
en el cuadro 1.

| name      | id   | sp_attack | sp_defense | speed | ability      |
|-----------|------|-----------|------------|-------|--------------|
|Bulbasaur1 | 1    |    65     |    65      |  45   | Overgrow     |
|Ivysaur1   | 2    |    80     |    80      |  60   | Overgrow     |
|Venusaur1  | 3    |    122    |    120     |  80   | Overgrow     |
|Charmander1| 4    |    60     |    50      |  65   | Blaze        |
|Charmeleon1| 5    |    80     |    65      |  80   | Blaze        |
|Charizard1 | 6    |    159    |    115     |  100  | Blaze        |
|...        |...   |    ...    |    ...     |  ...  | ...          |
|Baltoy32   |19997 |    40     |    70      |  55   | Levitate     |
|Claydol32  |19998 |    70     |    120     |  75   | Levitate     |
|Lileep32   |19999 |    61     |    87      |  23   | Suction Cups |
|Cradily32  |20000 |    81     |    107     |  43   | Suction Cups |

<p align = "center">
Table 1: Tabla pokemon.csv
</p>


Para trabajar está información el profesor Oak te pide pasar los datos de los
Pokémones a un diccionario que contiene otro diccionario con la siguiente
estructura:

* Clave:ID del Pokémon.
* Valor: Diccionario con la siguiente estructura:
  * Clave: "Nombre"; Valor: Nombre del Pokémon.
  * Clave: "puntos_ataque"; Valor: Sp_attack del Pokémon.
  * Clave: "puntos_defensa"; Valor: Sp_defense del Pokémon.
  * Clave: "puntos_velocidad"; Valor: Speed del Pokémon.
  * Clave: "habilidad"; Valor: Ability del Pokémon.

Los ejemplos de los diccionarios a utilizar se muestra en Listing 1.

    {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
    "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre: "Ivysaur1", "puntos de ataque": 80, "puntos_defensa": 87,
    "puntos_velocidad": 60, "habilidad": "Overgrow"},
    ....,
    19999: {"nombre: "Lileep32", "puntos de ataque": 61, "puntos_defensa": 87,
    "puntos_velocidad": 23, "habilidad": "Suction Cups"},
    20000: {"nombre: "Cradily32", "puntos de ataque": 81, "puntos_defensa": 107,
    "puntos_velocidad": 43, "habilidad": "Suction Cups"},
    }

<p align = "center">
Listing 1: Ejemplo de diccionarios
</p>

**IMPORTANTE**: El ID del Pokémon, los puntos de ataque, puntos de defensa y puntos
de velocidad deben ser un entero. El nombre y habilidad deben estar en formato string.

Se recomienda leer el archivo `pokemon.csv` e iterar línea a línea para llenar el
diccionario de manera eficiente. Para obtener los valores de la línea separada por punto
y coma (;), se recomienda el uso de la función `split()`. Un ejemplo se muestra en
Listing 2.

```python
linea = "Bulbasaur1;1;65;65;45;Overgrow\n"
datos_pokemon = linea.split(";")
print(datos_pokemon)
```
<p align = "center">
Listing 2: Ejemplo de leer líneas
</p>

**TIP**: Tener en cuenta que al final de la línea existe un carácter no visible de
quiebre de línea ("\n"), el valor de la habilidad no debe contener el carácter
mencionado.

## Problema 1

El profesor Oak le solicita que cree el diccionario a partir del archivo `pokemon.csv`.
Recuerde que el diccionario debe tener la siguiente estructura:

- Clave: ID del pokémon.
- Valor: Diccionario con la siguiente estructura:
  - Clave: "nombre"; Valor: Nombre del Pokémon.
  - Clave: "puntos_ataque"; Valor: Sp_attack del Pokémon.
  - Clave: "puntos_defensa"; Valor: Sp_defense del Pokémon.
  - Clave: "puntos_velocidad"; Valor: Speed del Pokémon.
  - Clave: "habilidad"; Valor: Ability del Pokémon.

### Ejemplo 1

#### Input
```python
ruta = "pokemon.csv"
```

| name        | id | sp_attack | sp_defense | speed | abilities   |
|-------------|----|-----------|------------|-------|-------------|
| Bulbasaur1  |  1 |     65    |      65    |   45  | Overgrow    |
| Ivysaur1    |  2 |     80    |      80    |   60  | Overgrow    |
| Venusaur1   |  3 |    122    |     120    |   80  | Overgrow    |
| Charmander1 |  4 |     60    |      50    |   65  | Blaze       |
| Charmeleon1 |  5 |     80    |      65    |   80  | Blaze       |
| Charizard1  |  6 |    159    |     115    |  100  | Blaze       |
| Squirtle1   |  7 |     50    |      64    |   43  | Torrent     |
| Wartortle1  |  8 |     65    |      80    |   58  | Torrent     | 
| Blastoise1  |  9 |    135    |     115    |   78  | Torrent     |
| Caterpie1   | 10 |     20    |      20    |   45  | Shield Dust |

#### Output
```python
{
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Explicación
Se crea el diccionario desde el archivo `pokemon.csv` según la estructura especificada. 

## Problema 2

El profesor Oak necesita consultar frecuentemente datos de los Pokémon que tiene en su
laboratorio para intercambiar con otros investigadores. Por ese motivo, él le solicita
que genere una función que a partir del ID del Pokémon y un valor de búsqueda devuelva
cómo resultado el dato para el Pokémon.

### Ejemplo 1

#### Input
```python
id = 8
valor = "habilidad"
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```
Torrent
```

#### Explicación
Se busca al Pokémon por su ID y se retorna el valor de la habilidad, en este caso el
Pokémon 8 tiene la habilidad Torrent.

### Ejemplo 2

#### Input
```python
id = 88
valor = "puntos_velocidad"
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```
Pokémon no encontrado
```

#### Explicación
Se busca al Pokémon por su ID, en este caso no se encuentra el ID y se retorna
"Pokémon no encontrado".

### Ejemplo 3

#### Input
```python
id = 3
valor = "puntos_ataque"
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```
122
```

#### Explicación
Se busca al Pokémon por su ID y se retorna el valor de puntos_ataque, en este
caso el Pokémon 3 tiene 122 puntos de ataque.

## Problema 3

El profesor Oak requiere conocer el Pokémon más rápido que tiene en su laboratorio
para enviarlo a una competencia en el torneo Pokémon de la ciudad Johto. Él le solicita
que cree un algoritmo de búsqueda con **Complejidad _O(n)_**, que retorne una tupla
con el nombre del Pokémon y el puntaje de velocidad.

### Ejemplo 1

#### Input
```python
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```python
("Charizard", 100)
```

#### Explicación
La búsqueda en el diccionario de Pokémones permite encontrar que el más rápido
tiene 100 puntos_velocidad y el nombre es Charizard1.

## Problema 4

El profesor Oak necesita ordenar el nombre de los Pokémones de forma ascendente
para publicar la lista en la página web del laboratorio. Él le solicita que cree
un algoritmo de ordenamiento con **Complejidad _O(n log n)_**, que retorne una
lista de tuplas que contengan el nombre del Pokémon y el ID de Pokémon.

**TIP**: Para implementar las funciones de ordenamiento usando recursividad se
le proporciona dos funciones llamadas `merge_sort` y `merge` que debe
implementar en la plantilla Solution. En la plantilla mostrada en el anexo 3, existe
una sección entre las líneas 4 y 23 donde puede editar sus funciones de ordenamiento.

### Ejemplo 1

#### Input
```python
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```python
[("Blastoise1", 9), ("Bulbasaur1", 1), ("Caterpie1", 10), ("Charizard1", 6),
("Charmander1", 4), ("Charmeleon1", 5), ("Ivysaur1", 2), ("Squirtle1", 7),
("Venusaur1", 3), ("Wartortle1", 8),
]
```

#### Explicación
Se crea una lista de tuplas con los valores de nombre e ID del Pokémon. Luego
se realizó el ordenamiento de la lista de forma eficiente con las funciones
recursivas. Como resultado se obtiene el nombre de los Pokémones ordenados
ascendentemente.

## Problema 5

En tres semanas el profesor Oak, necesita entregar Pokémones a los nuevos
entrenadores que llegan a su laboratorio. En esta ocasión va a realizar un sorteo
con los nombres de los Pokémones publicados en la página web del laboratorio. Luego
del sorteo necesita conocer la habilidad que el Pokémon tiene para instruir a los
entrenadores, por ese motivo le solicita que cree un algoritmo de búsqueda binaria
con **Complejidad _O(lg n)_**, que reciba como parámetro el nombre del Pokémon a
buscar y retorne los datos del Pokémon en el diccionario. Si el nombre del Pokémon
no es encontrado debe retornar el valor de "-1" como llave y el texto "No encontrado"
como valor.

**TIP**: Para implementar la busqueda binaria, tiene que trabajar sobre una lista
ordenada. Por ese motivo, uno del los parámetros de entrada es la lista de tuplas
con valores de nombre e ID de Pokémon ordenados ascendentemente por el nombre, similar
al resultado del Problema 4.

### Ejemplo 1

#### Input
```python
nombre_a_buscar = "Squirtle1"
nombres_ordenados = [
  ("Blastoise1", 9), ("Bulbasaur1", 1), ("Caterpie1", 10),
  ("Charizard1", 6), ("Charmander1", 4), ("Charmeleon1", 5),
  ("Ivysaur1", 2), ("Squirtle1", 7), ("Venusaur1", 3), ("Wartortle1", 8),
]
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```python
{7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
    "puntos_velocidad": 43, "habilidad": "Torrent"}}
```

#### Explicación
El nombre del Pokémon a buscar es Squirtle1, para obtener el ID del Pokémon se
tiene que realizar la búsqueda binaria en la lista nombres_ordenados. Luego de
encontrarlo, tiene que retornar todos los valores del diccionario para ese Pokémon.
En el ejemplo obtenemos:

- Clave: 7.
- Valor: Diccionario con la siguiente estructura:
  - Clave: "nombre"; Valor: Squirtle1.
  - Clave: "puntos_ataque"; Valor: 50.
  - Clave: "puntos_defensa"; Valor: 64.
  - Clave: "puntos_velocidad"; Valor: 43.
  - Clave: "habilidad"; Valor: Torrent.

### Ejemplo 2

#### Input
```python
nombre_a_buscar = "Squirtle5"
Pokemones = {
    1: {"nombre": "Bulbasaur1", "puntos_ataque": 65, "puntos_defensa": 65,
        "puntos_velocidad": 45, "habilidad": "Overgrow"},
    2: {"nombre": "Ivysaur1", "puntos_ataque": 80, "puntos_defensa": 80,
        "puntos_velocidad": 60, "habilidad": "Overgrow"},
    3: {"nombre": "Venusaur1", "puntos_ataque": 122, "puntos_defensa": 120,
        "puntos_velocidad": 80, "habilidad": "Overgrow"},
    4: {"nombre": "Charmander1", "puntos_ataque": 60, "puntos_defensa": 50,
        "puntos_velocidad": 65, "habilidad": "Blaze"},
    5: {"nombre": "Charmeleon1", "puntos_ataque": 80, "puntos_defensa": 65,
        "puntos_velocidad": 80, "habilidad": "Blaze"},
    6: {"nombre": "Charizard1", "puntos_ataque": 159, "puntos_defensa": 115,
        "puntos_velocidad": 100, "habilidad": "Blaze"},
    7: {"nombre": "Squirtle1", "puntos_ataque": 50, "puntos_defensa": 64,
        "puntos_velocidad": 43, "habilidad": "Torrent"},
    8: {"nombre": "Wartortle1", "puntos_ataque": 65, "puntos_defensa": 80,
        "puntos_velocidad": 58, "habilidad": "Torrent"},
    9: {"nombre": "Blastoise1", "puntos_ataque": 135, "puntos_defensa": 115,
        "puntos_velocidad": 78, "habilidad": "Torrent"},
    10: {"nombre": "Caterpie1", "puntos_ataque": 20, "puntos_defensa": 20,
        "puntos_velocidad": 45, "habilidad": "Shield Dust"},
}
```

#### Output
```python
{-1: "No encontrado"}
```

#### Explicación
El nombre del Pokémon a buscar es Squirtle5, para obtener el ID del Pokémon se
tiene que realizar la búsqueda binaria en la lista nombres_ordenados. Debido a que no
se encontró al Pokémon se devuelve -1 como clave y "No encontrado" como valor.

- Clave: 7.
- Valor: Diccionario con la siguiente estructura:
  - Clave: "nombre"; Valor: Squirtle1.
  - Clave: "puntos_ataque"; Valor: 50.
  - Clave: "puntos_defensa"; Valor: 64.
  - Clave: "puntos_velocidad"; Valor: 43.
  - Clave: "habilidad"; Valor: Torrent.

> _**NOTA**_: Segun el enunciado original una de las llaves es "Nombre" pero
> al ser evaluado en un _grader_ (de la institución) este realiza tests
> esperando la llave "nombre".
> El instructor debería corredir el enunciado original o modificar los tests
> del grader.
>
> Se opta por modificar la llave en la solución.
