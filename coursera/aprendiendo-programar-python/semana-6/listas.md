# Listas

# Pregunta 1

Daniel no entendió muy bien qué era un objeto de tipo _list_. Ayúdalo marcando
cuál de las siguientes es una variable de tipo _list_.

```python
lista = "[en un momento]"
saludo = ["s", "a", "l", "u", "4"]
coordenada = (3, 5)
edad = 90
```

- [X] `fecha = [2, "Julio", 2017]`
- [X] `saludo = ["s", "a", "l", "u", "4"]`
- [ ] `lista = "[en un momento]"]`
- [ ] `edad = 90`
- [ ] `coordenada = (3, 5)`

# Pregunta 2

Sea la variable **lista_espera** que contiene la lista de espera de un restaurante.
¿Cuál, de las siguientes alternativas, permite almacenar en la variable
**siguiente_cliente** el nombre del siguiente cliente a ser atendido?. El siguiente
cliente es el primero en la lista de espera, de izquierda a derecha.

```python
lista_espera = ["Mar", "Jorge", "Cristian", "Valeria"]
siguiente_cliente =  ¿?
```

- [ ] `lista_espera[0:1]`
- [X] `lista_espera[0]`
- [ ] `lista_espera.index(0)`
- [ ] `lista_espera.insert(0)`
- [ ] `lista_espera.append(0)`

# Pregunta 3

¿Cómo queda la lista **lista_compras** después de ejecutar este código? Doña Rosa ya
no sabe qué comprar y qué no comprar.

```python
lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"];
lista_compras.append("maní");
lista_compras.remove("arroz");
lista_compras.insert(2,"leche");
```

- [X] `["pan", "huevo", "leche", "queso", "jamon", "maní"]`
- [ ] `["pan", "huevo", "queso", "arroz", "jamon"]`
- [ ] `["pan", "leche", "huevo", "queso", "jamon", "maní"]`
- [ ] `["pan", "huevo", "leche", "queso", "jamon"]`
- [ ] `["pan", "huevo", "queso", "jamon", "maní"]`

# Pregunta 4

¿Cuál es el valor de la variable **trozo** después de ejecutar el siguiente código?

```python
datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
```

- [X] `[2017, "Final", 14.5, "Chile"]`
- [ ] `[2017, "Final", 14.5, "Chile", 0]`
- [ ] `[2, "Julio", 2017, "Final"]`
- [ ] `[2017, "Final", 14.5, "Chile", 0, "Alemania", 1]`
- [ ] `["Julio", 2017, "Final", 14.5]`

# Pregunta 5

¿Cuál es el valor de la variable trozo después de ejecutar el siguiente código?

```python
datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
```

- [X] `[500, 2, 4100, "bitcoin"]`
- [ ] `["semillas", "cerveza", "despacho", "pago"]`
- [ ] `[500, 2, 4100, "bitcoin", 95.4]`
- [ ] `[500, "despacho", "bitcoin", ]`
- [ ] `[500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza"]`

# Pregunta 6

En el siguiente código:

```python
unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = ¿?
```

De las siguientes expresiones, marque aquellas que permiten que el valor de
la variable **muestra** sea

```python
[49, 2, 55, 300]
```

- [X] `unidades[2:4] + unidades[6:8]`
- [X] `unidades[2:3] + unidades[3:7:3] + unidades[7:8]`
- [ ] `unidades[2] + unidades[3:7:3] + unidades[7]`
- [ ] `unidades[2:8] - unidades[4:6]`
- [ ] `unidades[2:8:2]`

# Pregunta 7

Considere la lista **votos**, que contiene listas con los resultados de una votación

```python
resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]
mayoria = ganador(resultados)
```

De las siguientes funciones, ¿cuáles retornan correctamente el _**string**_ asociado al valor más grande? 

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def ganador(votos):
      mayor = votos[0]
      for cand in votos:
          if cand[1] > mayor[1]:
              mayor = cand
      return mayor[0]
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def ganador(votos):
      mayor = votos[0]
      for cand in votos:
          if cand[1] > mayor[1]:
              mayor = cand
      return mayor
  ```
  </span>

- [ ] <span>
  ```python
  def ganador(votos):
      mayor = votos[0]
      for cand in votos:
          if cand[1] < mayor[1]:
              mayor = cand
      return mayor[0]
  ```
  </span>

- [ ] <span>
  ```python
  def ganador(votos):
      mayor = votos[0]
      for cand in votos:
          if cand[1] > mayor[1]:
              mayor = cand
      return mayor[1]
  ```
  </span>

- [ ] <span>
  ```python
  def ganador(votos):
      mayor = votos[len(votos)-1]
      for cand in votos:
          if cand[1] >= mayor[1]:
              mayor = cand
      return mayor
  ```
  </span>


# Pregunta 8

Considera un tablero de 3x3 posiciones, donde cada una de ella está numerada
desde el número 1 al 9. El tablero está definido de la siguiente manera:

```python
tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
```

De los siguientes códigos, marque aquellos que permiten recorrer el tablero por
orden de columnas. Esto significa que la salida debe escribir los valores:

```python
1 4 7 2 5 8 3 6 9
```

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  for i in range(3):
      for j in range(3):
          print(tablero[j][i],end=" ")
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  for j in range(3):
      for i in range(3):
          print(tablero[i][j],end=" ")
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  for i in range(9):
      print(tablero[i%3][i//3],end=" ")
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  for i in range(3):
      for j in range(3):
          print(tablero[i][j],end=" ")
  ```
  </span>

- [ ] <span>
  ```python
  for j in range(3):
      for i in range(3):
          print(tablero[j][i],end=" ")
  ```
  </span>


# Pregunta 9

De las siguientes funciones, indique cuál o cuáles permiten obtener la cantidad
de veces que un elemento **elem** se encuentra dentro de la lista **conjunto**.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def cuantas(elem, conjunto):
      contador = 0
      for e in conjunto:
          if e == elem:
              contador += 1
      return contador
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def cuantas(elem, conjunto):
      contador = 0
      for k in range(len(conjunto)):
          if conjunto[k] == elem:
              contador += 1
      return contador
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def cuantas(elem, conjunto):
      return len(conjunto)
  ```
  </span>

- [ ] <span>
  ```python
  def cuantas(elem, conjunto):
      for e in conjunto:
          if e == elem:
              return e
  ```
  </span>

- [ ] <span>
  ```python
  def cuantas(elem, conjunto):
      contador = 0
      for k in range(len(conjunto)):
          contador += 1
      return contador
  ```
  </span>

# Pregunta 10

¿Cuál es el valor de la variable **splitted** luego de ejecutar el siguiente código?

```python
contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
```

- [X] `['Marcelo, Alvaro', ' Elena, Karen', ' Jaime', ' Carmen']`
- [ ] `['Marcelo, Alvaro;', ' Elena, Karen;', ' Jaime;', ' Carmen']`
- [ ] `['Marcelo, Alvaro, Elena, Karen, Jaime, Carmen']`
- [ ] `['Marcelo, Alvaro', 'Elena, Karen', 'Jaime', 'Carmen']`
- [ ] `['Marcelo', ' Alvaro', ' Elena', ' Karen', ' Jaime', ' Carmen']`
