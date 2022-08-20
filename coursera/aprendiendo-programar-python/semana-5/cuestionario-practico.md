# Cuestionario Práctico

# Pregunta 1

Escribe una función que reciba dos _strings_ (de largo > 2) como parámetros,
y retorne un _string_ de largo 4 que consista de las dos primeras letras del
primer _string_ y las últimas dos letras del segundo.\
<br>
Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función
debe retornar "fase".

```python
def mezclador(string_a, string_b):
    # aquí debes escribir el código de tu programa
    return ? # aquí debes retornar el resultado
```

# Pregunta 2

Escriba una función que reciba dos _strings_ como parámetros y retorne un nuevo
_string_ que consista del primero, pero con el segundo _string_ intercalado entre
cada letra del primero.\
<br>
Por ejemplo si los _strings_ son "paz" y "so", entonces tu función debe
retornar "p**so**a**so**z**so**"

```python
def intercalar(string_a, string_b):
    return ? # aquí debes retornar el resultado
```

# Pregunta 3

Escriba una función que reciba un _string_ consistente de unos y ceros y retorne
la cantidad de ocurrencias de _unos_ menos la cantidad de ocurrencias de _ceros_.\
<br>
Por ejemplo, si el _string_ es "11000110101", entonces tu función debe retornar
1 (ya que hay 6 _unos_ y 5 _ceros_)

```python
def ocurrencias(string):
    return ? # aquí debes retornar el resultado
```

# Pregunta 4

Pregunta 4

Escriba una función que reciba un _string_ _s_ y un número _n_ como parámetros y retorne
el mismo _string_ _s_ pero sin el elemento en el índice _n_.

Por ejemplo, si _s_ es "Hasta luego" y _n_ es 3, entonces tu función debe retornar
"Hasa luego".

_Hint_: cuidado con aquellos casos en los que se tenga que eliminar un elemento
de los bordes.

```python
def remover_enesimo(s, n):
    return ? # aquí debes retornar el resultado
```

# Pregunta 5

Escriba una función que reciba un _string_ como parámetro y retorne el _string_, pero
con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el
_string_ consistirá solamente de letras.

Por ejemplo si el _string_ es "Viva la Vida", entonces tu función debe
retornar "$iva la $ida".

```python
def reemplazo(string):
    return ? # aquí debes retornar el resultado
```
