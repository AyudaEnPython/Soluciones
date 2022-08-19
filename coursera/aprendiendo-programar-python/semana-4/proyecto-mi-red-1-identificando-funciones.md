# Proyecto Mi Red: Identificando funciones

# Pregunta 1

Tras ejecutar y hacer los ejercicio en el código "MiRedS4-Funciones.py",
marca las alternativas que describen funcionalidades de este código que
se podrían convertir en función. 
- [ ] Cada instrucción **print**
- [X] Conjunto de instrucciones **print** para mostrar el perfil del usuario
- [X] Mostrar texto de bienvenida
- [X] Código para solicitar todos los datos del perfil de usuario
- [X] Código para que el usuario escoja una opción

# Pregunta 2

Supongamos que queremos encapsular el código que permite al usuario elegir
una opción entre N alternativas numéricas posibles, desde 0 hasta N-1.\
<br>
¿Cuáles de las siguientes opciones permiten efectuar esto?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def opcion_menu(N):
      opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
      while opcion < 0 or opcion > N-1:
          print("Inténtalo otra vez.")
          opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
      return opcion
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def opcion_menu(N):
      opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
      while opcion < 0 or opcion > N-1:
          print("Inténtalo otra vez.")
          opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
  ```
  </span>

- [ ] <span>
  ```python
  def opcion_menu():
      opcion = int(input("Ingresa opción desde 0 a N-1: "))
      while opcion < 0 or opcion > N-1:
          print("Inténtalo otra vez.")
          opcion = int(input("Ingresa opción desde 0 a N-1: "))
      return opcion
  ```
  </span>

- [ ] <span>
  ```python
  def opcion_menu(N):
      opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
      while opcion < 0 or opcion > N-1:
          print("Inténtalo otra vez.")
          opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
      print(opcion)
  ```
  </span>
