# Enunciado Original

- El proyecto debe generar un número entero entre 1 y 100 en forma aleatoria y
  guardarlo.
- El programa solicita el nombre al jugador y lo guarda.
- El jugador ingresa un número que representa un intento de adivinar el número.
  Si el jugador ingresa el número cero el juego termina inmediatamente imprimiendo
  lo siguiente: "No lograste a pesar de tratar N veces. Mas suerte para otra vez".
- El programa lee el número ingresado y genera una de las siguientes respuestas:
  1. Sorry `<nombre>`, ese no es pero estas a una distancia menor a 5.
  2. Sorry `<nombre>`, ese no es pero estas a una distnacia mayor que 5 y menor que 10.
  3. Sorry `<nombre>`, ese no es pero estas a una distancia mayor que 10 y menor que 20.
  4. Sorry `<nombre>`, ese no es pero estas a una distancia mayor que 20.
  5. Felicitaciones `<nombre>`, lo lograste en N intentos.
- En cualquiera de los primeros 4 casos el programa vuelve a pedir un nuevo intento de
  adivinar.
- Observa que debes mantener el registro de los intentos para indicarlo en los mensajes
  cuando el juego termina.