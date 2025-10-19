# Simulador de Carrera de Caballos

## Inicio

Mostrar descripción breve de la competencia, dibujo ASCII de un caballo y
requisitos de la misma.

## Inscripción del Caballo

Para inscribir un caballo, el sistema solicitará los siguientes datos: 
- ***Nombre del caballo***: Debe comenzar con una letra mayúscula. 
- ***Edad***: Debe estar entre 2 y 15 años. 
- ***Raza***: Debe ser una raza de caballo reconocida. 
- ***Peso***: Debe estar entre 400 kg y 570 kg. 
- ***Nombre completo del dueño***: Tanto el nombre como el apellido deben 
  comenzar con mayúscula. 

Si alguno de los datos ingresados no cumple con los requisitos, la inscripción
será inválida y el proceso se detendrá. 

## Selección de la Carrera

Si la inscripción es válida, se le pedirá al usuario que seleccione una de las 
siguientes carreras para su caballo: 
- ***Cuarto de milla (400 metros)***: Abierta a todos los caballos inscritos. 
- ***Una milla (1600 metros)***: Solo pueden participar caballos con más de 5
  puntos.
- ***Gran Premio (2500 metros)***: Solo pueden participar caballos con más
  de 10 puntos. 

## Asignación Aleatoria y Cálculo de Tiempos

- ***Participantes***: Además del caballo inscrito, se seleccionarán
  aleatoriamente otros siete caballos con nombres generados aleatoriamente para
  cada carrera. 
- ***Velocidad***: A cada caballo se le asignará una velocidad media aleatoria
  entre 45 y 70 km/h. 
- ***Tiempo***: Utilizando la fórmula ```Tiempo total = Distancia total / Velocidad 
media```, se calculará el tiempo que tarda cada caballo en completar la carrera. 
- ***Resultados***: Los resultados se presentarán en una tabla ordenada de mejor 
a peor tiempo, incluyendo el nombre del caballo y su tiempo. 

## Puntuación y Descalificación

### Puestos

- ***Primer lugar***: 15 puntos y mensaje de felicitación. 
- ***Segundo lugar***: 10 puntos y mensaje de felicitación. 
- ***Tercer lugar***: 5 puntos y mensaje de felicitación. 
- ***Último lugar***: Descalificación del caballo y fin del programa. 
- ***Otros puestos***: Se asignarán puntos de acuerdo a la posición (4, 3, 2
  o 1 punto). 

### Acumulación de puntos

Los puntos obtenidos en cada carrera se sumarán al puntaje total del caballo. 

## Continuar o Retirar 

Después de cada carrera, se le preguntará al usuario si desea continuar 
compitiendo o si desea retirarse. Si elige retirarse, el programa finalizará.
Si elige continuar, se volverá a la pantalla de selección de carreras.