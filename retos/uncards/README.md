# UNCards

En las universidades de Colombia se ha creado un juego, donde dos
equipos se enfrentan utilizando un conjunto de caracteres, para
determinar el ganador en cada turno se hace a través del peso (el
código ASCII) de cada uno de los caracteres.

En la final del torneo para este juego se esta enfrentando la
Universidad Nacional de Colombia y la Universidad de los Andes, tu
debes desarrollar un programa que ayude a decidir que equipo va
ganando en cada uno de los turnos:

## Reglas

1. Ambos equipos arrancan con 0 puntos.
2. Los puntos se van acumulando en cada turno.
3. El ganador de cada turno es el que más puntaje lleve acumulado hasta
  el momento.
4. Un equipo obtiene un punto si un carácter elegido en el turno `i` es
  mayor al de su oponente.
5. Si la Universidad Nacional de Colombia va ganando se debe usar la U,
  si los Andes va ganando se debe usar A y si hay empate se debe usar
  la D.

Cada equipo puede formar una secuenci de caracteres de los siguientes
caracteres validos para la final:
k V + * @ a A Z 1 P [ ] C o l e r

## Ejemplos

Se recibirá dos entradas, la primera corresponde a los caracteres
usados por la Universidad Nacional de Colombia y la segunda por los
caracteres usados por la Universidad de los Andes en cada turno, la
salida debe ser una cadena de caracteres indicando que equipo va
ganando en cada turno.

|Entrada           |Salida |
|------------------|-------|
| P1[@]<br>CZ*[ol  | UDUDA |  
| ro1<br>]cP       | UUU   |
