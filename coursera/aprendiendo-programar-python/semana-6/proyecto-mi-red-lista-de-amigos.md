# Proyecto Mi Red: Lista de amigos

# Pregunta 1

Tras ejecutar y extender los ficheros "MiRedS6-Listas.py" y "S6Red.py",
contesta a las siguientes preguntas. Marca las alternativas verdaderas. 

- [X] El programa utiliza archivos para simular la interacción entre los usuarios

- [X] Las relaciones entre amigos en este programa pueden ser unidireccionales.
  Esto significa que si A es amigo de B, no necesariamente B es también amigo de A

- [ ] El archivo original no permite que la lista de amigos de un usuario cambie
  durante la ejecución del programa.

- [X] El muro de un usuario, se guarda en una lista de _strings_.

- [ ] Dado que el usuario no ingresa el valor **num_amigos**, no es posible saber
  cuántos amigos tiene un usuario.

- [X] En el programa presentado es posible que un usuario escriba el nombre de un
  amigo dos veces.

# Pregunta 2

De las siguientes alternativas de código, ¿cuáles permiten que, al ejecutar el
siguiente código, se agregue correctamente un nuevo amigo a la lista de amigos
del usuario?

```python
nuevo = input("Indica el nombre de tu nuevo amigo o amiga: ")
agregar_amigo(lista_amigos, nuevo)
```

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def agregar_amigo(lista_amigos, nuevo_amigo):
      lista_amigos.append(nuevo_amigo)
      return lista_amigos
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def agregar_amigo(lista_amigos, nuevo_amigo):
      lista_amigos.append(nuevo_amigo)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def agregar_amigo(lista_amigos, nuevo_amigo):
      lista_amigos.extend([nuevo_amigo])
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def agregar_amigo(lista_amigos, nuevo_amigo):
      lista_amigos.extend(nuevo_amigo)
  ```
  </span>

- [ ] <span>
  ```python
  def agregar_amigo(lista_amigos, nuevo_amigo):
      lista_amigos = lista_amigos + nuevo_amigo
      return lista_amigos
  ```
  </span>


# Pregunta 3

Se desea agregar una opción que permita mostrar el estado de todos los amigos.
Suponiendo que todos los amigos existen en el sistema (por lo tanto existe un
archivo **.user** para cada uno de ellos). ¿Cuáles de los siguientes códigos
permiten implementar este llamado correctamente?

```python
mostrar_estados_amigos(amigos)
```

Considere que el estado de un usuario se almacena en la séptima línea de su archivo.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def mostrar_estados_amigos(lista_amigos):
      for k in range(len(lista_amigos)):
          archivo = open(lista_amigos[k]+".user", "r")
          for i in range(7):
              linea = archivo.readline().rstrip()
          print(lista_amigos[k]+":", linea)
          archivo.close()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def mostrar_estados_amigos(lista_amigos):
      for amigo in lista_amigos:
          archivo = open(amigo+".user", "r")
          for i in range(7):
              linea = archivo.readline().rstrip()
          print(amigo+":", linea)
          archivo.close()
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def mostrar_estados_amigos(lista_amigos):
      archivo = open(amigo+".user", "r")
      for amigo in lista_amigos:
          for i in range(7):
              linea = archivo.readline().rstrip()
          print(amigo+":", linea)
      archivo.close()
  ```
  </span>

- [ ] <span>
  ```python
  def mostrar_estados_amigos(lista_amigos):
      for amigo in lista_amigos:
          archivo = open(amigo+".user", "r")
          linea = archivo.readline().rstrip()
          print(amigo+":", linea)
          archivo.close()
  ```
  </span>

- [ ] <span>
  ```python
  def mostrar_estados_amigos(lista_amigos):
      for amigo in lista_amigos:
          archivo = open(amigo+".user", "r")
          for i in range(7):
              linea = archivo.readline().rstrip()
              print(amigo+":", linea)
          archivo.close()
  ```
  </span>
