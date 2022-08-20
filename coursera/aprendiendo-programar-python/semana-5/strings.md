# Strings

# Pregunta 1

De estas expresiones, ¿cuál **NO** es un string válido?\
<br>
_Hint_: Recuerda como el computador interpreta que algo es un string o no. 
- [X] Martes 
- [ ] "p(a),a,b"
- [ ] "48"
- [ ] 'La casa verde'

# Pregunta 2

¿Qué imprimiría las siguientes líneas de código?

```python
a = "49" + "10"
print(a)
```

- [X] "4910"
- [ ] Algún error de Python
- [ ] 59
- [ ] "59"


# Pregunta 3

Al ejecutar el siguiente código:

```python
print("MmM" * 4)
```

Se imprime "MmmmmM"

- [X] Falso
- [ ] Verdadero
- [ ] No se puede determinar

# Pregunta 4

Pregunta 4

Si al ejecutar el siguiente código

```python
a = ¿?
b = a.replace("v","n")
print(b)
```
se imprime "notar", determina cuál o cuáles de las siguientes opciones
corresponden a posibles valores de la variable _a_. 

- [X] "notar"
- [ ] True
- [ ] "votan"
- [X] "votar"
- [ ] "notav"

# Pregunta 5

¿Qué imprimiría las siguientes líneas de código?

```python
a = "oso pardo"
b = a.strip("o")
print(b)
```

- [ ] "oso pard"
- [ ] "oso pardo"
- [ ] "s pard"
- [X] "so pard"
- [ ] "so pardo"

# Pregunta 6

¿Cuál de estos métodos retornaría exactamente el _string_ "ANIMALES"?

- [ ] `"ANIMALES".replace("M","m")`
- [ ] `"ANIMALES".strip("A")`
- [X] `"ANIMALES".upper()`
- [ ] `"ANIMALES".lower()`


# Pregunta 7

¿Qué imprimirían las siguientes líneas de código?

```python
a = "Barcelona 92"
print(a[1])
```

- [ ] "B"
- [ ] True
- [X] "a"
- [ ] "Barcelona"

# Pregunta 8

Dado el siguiente código,

```python
s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)
```

¿Qué se imprime? (Escríbelo sin comillas; recuerda usar las mayúsculas y
minúsculas que correspondan)

    aso hubA

# Pregunta 9

¿Qué imprime el siguiente código?

```python
s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i<len(s):
  resultado = resultado + s[len(s)-i-1]
  i = i + 1
print(resultado)
```
- [ ] Imprime la misma palabra que ingresó el usuario
- [X] Imprime la palabra que ingresó el usuario, pero en orden inverso.
- [ ] Imprime la palabra que ingresó el usuario, pero con las letras desordenadas aleatoriamente.
- [ ] Imprime solamente la primera y última letras de la palabra ingresada por el usuario.

# Pregunta 10

Si `s =  "hola que tal"`, ¿cuál es el valor de `len(s)`?

- [ ] 10
- [ ] 11
- [X] 12
- [ ] 13

