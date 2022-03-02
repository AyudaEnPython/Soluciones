"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# PROBLEMA 1
print("PROBLEMA 1")
def e1():
    try:
        arr=[];
        wen=[];
        pares=0;
        cont=int(input("Cuantos numeros a capturar? -> "));
        num=[None]*cont;
        for i in range (cont):
            num=float(input("Dame los numeros -> "));
            if num > 0:
                #pares=num;
                m=num;
                #arr.append(m);
                print("Ya son positivos -> ",m);
            elif num < 0 and num%2!=0:
                div=num*-1
                #wen.append(div);
                print("Se convirtieron en positivos ->",div);
    except:
        print("No ingresaste un numero...");

#e1();
#PROBLEMA 2;
def e2():
    try:
        p=0;
        m=0;
        ñ=0;
        mensaje=int(input("Cuantas frutas vas a ingresar -> "));
        frutas=[None]*mensaje;
        for i in range(mensaje):
            frutas[i]=int(input("Selecciona un numero para agregara la canasta correspondiente: [1]PERAS {2}MANZANAS {3}PIÑAS ->"));
            if  (frutas[i]==1):
                p=p+1;
            elif  (frutas[i]==2):
                m=m+1;
            elif  (frutas[i]>3):
                print("He dicho digite un numero entre 1 y 3, intente de nuevo ");
        print("Colocaste en el canasto de peras ->", p);
        print("Colocaste en el canasto de manzanas ->", m);
        print("Colocaste en el canasto de piñas ->", ñ);
    except:
        print("Digite un numero valido ");
        return e2();
#e2();

def esfera():
    ...

def menu():
    try:
        print("Escoge una opcion: ");
        men=int(input("[1]PROBLEMA 1 [2]PROBLEMA 2 {3}PROBLEMA 3 {4}PROBLEMA 4 {5} SALIR-> "));
        for i in range ["[1]PROBLEMA 1", "[2]PROBLEMA 2", "[3]PROBLEMA 3", "{4}PROBLEMA 4", "{5} SALIR"]:
            if men==1:
                print("PROBLEMA 1");
                e1();
            if men==2:
                print("PROBLEMA 2");
                e2();
            if men==3:
                print("PROBLEMA 3");
                esfera();
    except:
        print("Opcion no valida");
#menu();