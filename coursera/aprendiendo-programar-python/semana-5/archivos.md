# Archivos

# Pregunta 1

¿Qué carácter especial señala un salto de línea?
- [ ] `"\t"`
- [ ] `"\\"`
- [ ] `"\""`
- [X] `"\n"`

# Pregunta 2

¿Cuál es el orden correcto para realizar estas acciones?
- [ ] Leer archivo - Abrir archivo - Cerrar archivo
- [ ] Abrir archivo - Cerrar archivo - Leer archivo
- [ ] Cerrar archivo - Leer archivo - Abrir archivo
- [X] Abrir archivo - Leer archivo - Cerrar archivo

# Pregunta 3

¿Cuál de estas expresiones indica, como segundo parámetro de la función
open, el modo solo lectura?
- [ ] `""`
- [ ] `"w"`
- [X] `"r"`
- [ ] `"a"`

# Pregunta 4

Si un archivo llamado "ejemplo.txt" contiene lo siguiente:

```terminal
La lengua de la
ballena azul pesa lo mismo
que un elefante
```

¿Qué imprimen las siguientes líneas?

```python
ejemplo = open("ejemplo.txt", "r")
a = ejemplo.readline()
b = ejemplo.readline()
c = ejemplo.readline()
d = a + c
print(d)
```

- [ ] La lengua de la<br>La lengua de la
- [ ] que un elefante
- [ ] La lengua de la<br>ballena azul pesa lo mismo
- [X] La lengua de la<br> que un elefante
- [ ] La lengua de la que un elefante

# Pregunta 5

¿Por qué **NO** es válido el siguiente código?

```python
archivo = open(archivo.txt, "r")
archivo.close()
```

- [ ] Porque el archivo se cerró antes de haberse leído.
- [ ] Porque "r" no es válido como modo para abrir un archivo.
- [ ] Porque la variable archivo tiene el mismo nombre que el archivo.txt 
- [X] Porque el nombre del archivo no está en formato string.

# Pregunta 6

Si tenemos un archivo "mooc.txt" que tiene el siguiente contenido:

```terminal
MOOC 
significa
Massive
Open
Online
Course
```

```python
a = open("mooc.txt")
linea = a.readline()
linea = a.readline()
linea = a.readline()
linea = a.readline()
```

¿Qué contendrá la variable linea al final del código?

- [ ] "MOOC"
- [X] "Open"
- [ ] "Online"
- [ ] No contendrá nada.

# Pregunta 7

¿Qué contendrá la variable linea al final del código?

```python
a = open("mooc.txt", "w")
a.write("1 2 3 4")
a.write("5 6 7 8")
a.close()
```

- [ ] `1 2 3 4 5 6 7 8`
- [X] `1 2 3 45 6 7 8`
- [ ] `1 2 3 4`<br>`5 6 7 8`
- [ ] `1 2 3 4`<br>` 5 6 7 8`


# Pregunta 8

¿Cuál es la instrucción correcta si queremos convertir todo el contenido
de un archivo "direcciones.txt" a un string s?

- [ ] `s = open("direcciones.txt").readline()`
- [ ] `s = open("direcciones.txt")`
- [X] `s = open("direcciones.txt").read()`
- [ ] `s = open("direcciones.txt").readlines()`

# Pregunta 9

¿Por qué no es correcto el siguiente código?

```python
a = open("mi_nombre.txt")
a.write("Me llamo Luis")
a.close()
```

- [ ] Porque no es necesario cerrar un archivo de escritura.
- [X] Porque estamos escribiendo en un archivo solo de lectura.
- [ ] Porque el nombre "mi_nombre.txt" no es un nombre válido para un archivo.
- [ ] Porque la instrucción para escribir en un archivo es print, no write.


# Pregunta 10

¿Cuál es el código correcto para leer (e imprimir en pantalla) un archivo
que sea elegido por el usuario?


- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  s = input("Ingresa nombre archivo: ")
  t = open(s)
  l = t.readline()
  while l != "":
      print(l)
      l = t.readline()
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  s = input("Ingresa nombre archivo: ")
  print(s.read())
  ```
  </span>

- [ ] <span>
  ```python
  s = input("Ingresa nombre archivo: ")
  t = open(s)
  print(t.readline())
  ```
  </span>

- [ ] <span>
  ```python
  s = input("Ingresa nombre archivo: ").open().read()
  print(s)
  ```
  </span>
