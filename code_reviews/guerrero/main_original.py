"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

class guerrero :
    def __init__ ( self,nombre,vida,fuerza,precision,velocidad,defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza ; self.precision = precision
        self.velocidad = velocidad ; self.defensa = defensa 
    
    def golpear (self,g) :
    # veo si acierto el golpe
        if( random.random () <= ( self.precision - g.velocidad ) / 100) :
        # en caso de acertar , agrego daño al oponente
            g.vida -= max ([( self.fuerza - g.defensa )+ random.randrange (-10 ,11) ,1])
            print ("Golpe certero de", self.nombre)
        else :
            print (g.nombre, " esquiva el golpe !")
        print(self.nombre,":",self.vida)
        print(g.nombre,":",g.vida)

def simular_batalla(j1,j2):
    # comienza jugador mas veloz
    golpeador,receptor = j1,j2
    if( j1.velocidad < j2.velocidad ) :
        golpeador , receptor = j2 , j1
    # se golpean hasta que alguno tenga vida cero
    while ( j1.vida > 0 and j2.vida > 0) :
        print ("\n" + j1.nombre , j1.vida ,"vs",j2.vida , j2.nombre)
        y=random.randint(1, 2)
        print("golpes: ",y)
        for i in range(0,y):
            golpeador.golpear( receptor )
            i=i+1
        # cambio de turnos
        golpeador,receptor = receptor,golpeador
        # fin
    print ("\n" + j1.nombre , j1.vida ,"vs",j2.vida , j2.nombre)
    print ("Ganador :", receptor.nombre )


# batalla de ejemplo
superman = guerrero ("Superman" ,100 ,50 ,80 ,30 ,20)
goku = guerrero ("Goku" ,100 ,60 ,80 ,40 ,20)
#chuck = guerrero ("Chuck Norris" ,200 ,99 ,99 ,99 ,99)
# simula batalla
#superman.golpear(goku)

simular_batalla (goku,superman)