# Cuestionario Calificado

## Pregunta 1

Tras ejecutar el código "MiRedS2-Bienvenida.py" y realizar los ejercicios
correspondientes, te invitamos a resolver las siguientes preguntas: ¿a qué tipo
de dato corresponden, las variables indicadas en el archivo? Selecciona la
respuestas correcta.
- [ ] **edad**:int, **estatura**:float, **num_amigos**:bool
- [X] **edad**:int, **estatura**:float, **num_amigos**:int
- [ ] **edad**:float, **estatura**:int, **num_amigos**:int
- [ ] **edad**:float, **estatura**:float, **num_amigos**:str
- [ ] **edad**:str, **estatura**:str, **num_amigos**:str

## Pregunta 2

Supongamos que queremos agregar el dato **número de teléfono** del usuario.
¿Qué tipo de dato sería más apropiado?
- [ ] int
- [X] str
- [ ] bool
- [ ] float

## Pregunta 3

Supongamos que queremeos agregar un valor que corresponde a la expresión:
**"Tiene más de 10 amigos en la red social"**. ¿Qué tipo de datos es más
apropiado para almacenar este valor?
- [ ] int
- [ ] float
- [ ] str
- [X] bool

## Pregunta 4

Supongamos que dispones de la ubicación GPS del usuario, en coordenadas de
latitud y longitud con este código:
```python
lat = -33.499188
lon = -70.615126
```
De las siguientes instrucciones, ¿cuáles, al agregarlas después del código
mostrado, permiten almacenar el valor correspondiente a la expresión _"Estoy
al sur de mi casa"_?\
<br>
_Tip: prueba el código en tu entorno de programación_\
<br>
_Tip2: el Polo Sur es -90 en latitud, y el Polo Norte es +90_

- [ ] <span>
```python
  lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio - lat > 0
  ```
  </span>

- [ ] <span>
  ```python
  lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio - lat
  ```
  </span>

- [X] <details><summary>Ver código</summary>
  <p>

  ```python
  lat_domicilio = int(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = int(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio > lat

  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  lat_domicilio = input("Ingresa la latitud de tu domicilio")
  lon_domicilio = input("Ingresa la longitud de tu domicilio")
  estoy_al_sur = lat_domicilio - lat > 0
  ```
  </span>

- [ ] <span>
  ```python
  lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio > lon
  ```
  </span>

- [ ] <span>
  ```python
  lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio - lat < 0
  ```
  </span>

- [ ] <span>
  ```python
  lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
  lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
  estoy_al_sur = lat_domicilio > lat
  ```
  </span>

## Pregunta 5

De las siguientes alternativas, ¿cuáles son verdaderas respecto del código del
programa?

- [ ] El programa presentado no utiliza tipos de datos bool
- [ ] Luego de cada ejecución el programa, éste recuerda los datos que ingresamos en la ejecución anterior.
- [ ] La variables, **estatura**, de tipo float, no se almacena.
- [ ] La edad del usuario está calculada de manera exacta
- [X] El mensaje publicado por el usuario es una variable de tipo str
- [ ] El nombre del usuario debe estar compuesto solo por una palabra