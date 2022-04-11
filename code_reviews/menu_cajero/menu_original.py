"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import cmath
import os
os.system("clear")
print("Quieres entrar al cajero  ?")
op=input()
os.system("clear")
while op == "si" or op == "Si" or op == "SI" or op == "sI":
    print("1.- Depositar ")
    print("2.- Retirar ")
    print ("3.-Saldo ")
    print("4.- Salir ")
    print("Que quierés realizar ")
    opc=input()     
    if  opc=='1' or opc=='D' or opc=='d':
        print ("Depositar ")
        núm1 = float(input("Cuánto quierés depositar :"))
        print(f"\nAcabas de depositar : {núm1:}")
    elif opc=='2' or opc=='R' or opc=='r':
        print("Retirar ")
        núm2 = float(input("Cuánto quieres retirar :"))
        R=núm1-núm2
        if R <= 0 :                     
            print ("Saldo insuficiente")
        else:
            print(f"\Tu saldo es: {R:}")         
    elif opc=='3' or opc=='S' or opc=='s':
        print (f"\nTu saldó restante es: {R:.2f}")
    elif opc>="3" or opc<="0":
        print ("Opcion no valida my friend")
    print("¿Quieres continuar en el cajero ?")
    op=input()
    os.system("clear")            
else:
    print ("Hasta la próxima my friend ")