"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
seguir=True


while seguir:
    a=[12]
    x=("--")
    j=("")

# funcion para añadir empleados
    def añadirenpleados():

        nombre = input("Ingrese el nombre: ")
        nombre2= nombre.title()
        i1= True
        while i1:
            try:
                dia=int(input ("Dia: "))
                if dia >=10:
                    dia1= str(dia)
                    i1= False
                else:
                    dia1="0"+str(dia)
                    i1= False

            except:
                print("No ingreses letras.")
        i2= True
        while i2:
            try:
                mes=int(input ("Mes: "))
                if mes >=10:
                    mes1= str(mes)
                    i2= False
                else:
                    mes1= "0"+str(mes)
                    i2= False

            except:
                print("No ingreses letras.")
        i3= True
        while i3:
            try:
                año=int(input("Año: "))
                i3 = False
            except:
                print("No ingreses letras.")
        fecha = (dia1+"/"+mes1+"/"+str(año))

        cargo = input("Ingrese Cargo: ")
        cargo1=cargo.title()

        i4=True
        while i4:
            try:
                sueldo = float(input("Ingrese Sueldo: "))
                i4=False
            except:
                print("No ingreses letras.")

        i5= True
        while i5:
            try:
                sueldo_neto = input("Ingrese Sueldo   neto: ")
                i5= False
            except:
                print("No ingreses letras.")


        if sueldo >= 1800:
            descuento = "10 %"
        else:
            descuento = "0 %"


        archivo1=open("Empleados.txt", "r")
        codigo=["000"]
        texto = archivo1.readlines()
        for linea in texto:
            datos_buscados = linea.split(";")
            codigo3=datos_buscados[0]
            codigo4=codigo3[1:]
            codigo.append(codigo4)



        codigo2 =[]
        for i4 in codigo:
            codigo2.append(int(i4))


        codigo1= max(codigo2)

        if codigo1 >= 1 :
            codigo3= codigo1+1
        else:
            codigo3= 1
        archivo1.close()

        archivo = open("Empleados.txt", "a")


        if codigo3 >=10:
            archivo.write("E0"+str(codigo3)+";"+nombre2 +";"+fecha+";"+cargo1+";"+str(sueldo)+";"  +descuento+";"+str(sueldo_neto)+";"+"null"  +"\n")
        elif codigo3 >= 100:
            archivo.write("E"+str(codigo3)+";"+nombre2+"; "+fecha+";"+cargo1+";"+str(sueldo)+";" +descuento+";"+str(sueldo_neto)+";"+"null" +"\n")
        else:
            archivo.write("E00"+str(codigo3)+";"+nombre2  +";"+fecha+";"+cargo1+";"+str(sueldo)+";" +descuento+";"+str(sueldo_neto)+";"+"null" +"\n")

        print("\nEl Contacto ha sido agregado al  listado")
        archivo.close()





# Para poder dibujar la tabla necesitamos saber cual es la palabra mas extenza
    def contar():
        archivo = open ("Empleados.txt", "r")
        contar= archivo.readlines()
        for linea in contar:
            datos_buscados = linea.split(";")

            a.append(len(datos_buscados[0]))
            a.append(len(datos_buscados[3]))
            a.append(len(datos_buscados[4]))
            a.append(len(datos_buscados[6]))
    contar()

# esta funcion hace solamente tomar la palabra mas grande y añadir espacios para hacer que la tabla quede uniforme y que no salga descuadrada
    def cuantodeespacio(a1,j1):
        c=(max(a1))
        i1=0

        while i1 <c:
            j1=j1+" "
            i1=i1+1
        return j1
    g1=cuantodeespacio(a,j)

# hace lo mismo que la anterior funcion solamente que esta agrega lineas para poder separar
    def cuantodelinea(a1,x1):
        c=(max(a1))

        i=0
        while i <c:
            x1=x1+"-"
            i=i+1
        return x1
    g2=cuantodelinea(a,x)

# esta funcion toma todo lo anterior y dibuja la tabla
    def dibujartodo(x3,j2):
        c1=(max(a))
        archivo = open ("Empleados.txt", "r")
        dibuja= archivo.readlines()

        print("-"+x3+x3+x3+x3+x3+x3+x3)
        print('|',("Codigo"+j2)[:c1]+'|',("Nombre"+j2)  [:c1]+'|',("Fecha"+j2)[:c1]+'|',("Cargo"+j2)[:c1] +'|',("Sueldo"+j2)[:c1]+'|',("Descuento"+j2)[:c1]  +'|',("Sueldo neto"+j2)[:c1]+'|')
        print("-"+x3+x3+x3+x3+x3+x3+x3)
        for linea in dibuja:
            datos_buscados = linea.split(";")
            print('|',(datos_buscados[0]+j2)[:c1]+'|',  (datos_buscados[1]+j2)[:c1]+'|',  (datos_buscados[2]+j2)[:c1]+'|',  (datos_buscados[3]+j2)[:c1]+'|',  (datos_buscados[4]+j2)[:c1]+'|',  (datos_buscados[5]+j2)[:c1]+'|',  (datos_buscados[6]+j2)[:c1]+'|')
            print("-"+x3+x3+x3+x3+x3+x3+x3) 
        archivo.close()


# solamente busca y dibuja igual que dibujar todo
    def buscarempleado(x3,j2):
        c1=(max(a))
        archivo= open ("Empleados.txt", "r")
        print("Buscar.\n1:Por nombre.\n2:Por fecha")
        o= True
        while o:
            try:
                opcion = int(input("Opcion: "))
                o=False
            except:
                print("No ingreses letras.")

        if opcion == 1:
            nombre = input("Que nombre desea buscar: ")
            print()
            texto = archivo.readlines()
            print("-"+x3+x3+x3+x3+x3+x3+x3)
            print('|',("Codigo"+j2)[:c1]+'|',("Nombre"  +j2)[:c1]+'|',("Fecha"+j2)[:c1]+'|',("Cargo"  +j2)[:c1]+'|',("Sueldo"+j2)[:c1]+'|', ("Descuento"+j2)[:c1]+'|',("Sueldo neto"+j2) [:c1]+'|')
            print("-"+x3+x3+x3+x3+x3+x3+x3)
            for linea in texto:
                if nombre in linea.lower():
                    datos_buscados = linea.split(";")
                    print('|',(datos_buscados[0]+j2)[:c1]+'|',(datos_buscados[1]+j2)[:c1]+'|',(datos_buscados[2]+j2)[:c1]+'|',(datos_buscados[3]+j2)[:c1]+'|',(datos_buscados[4]+j2)[:c1]+'|',(datos_buscados[5]+j2)[:c1]+'|',(datos_buscados[6]+j2)[:c1]+'|')
                    print("-"+x3+x3+x3+x3+x3+x3+x3)

        if opcion == 2:
            i1= True
            while i1:
                try:
                    dia=int(input ("Dia: "))
                    if dia >=10:
                        dia1= str(dia)
                        i1= False
                    else:
                        dia1="0"+str(dia)
                        i1= False

                except:
                    print("No ingreses letras.")
            i2= True
            while i2:
                try:
                    mes=int(input ("Mes: "))
                    if mes >=10:
                        mes1= str(mes)
                        i2= False
                    else:
                        mes1= "0"+str(mes)
                        i2= False

                except:
                    print("No ingreses letras.")
            i3= True
            while i3:
                try:
                    año=int(input("Año: "))
                    i3 = False
                except:
                    print("No ingreses letras.")
            fecha = (dia1+"/"+mes1+"/"+str(año))
            print()
            texto = archivo.readlines()
            print("-"+x3+x3+x3+x3+x3+x3+x3)
            print('|',("Codigo"+j2)[:c1]+'|',("Nombre"  +j2)[:c1]+'|',("Fecha"+j2)[:c1]+'|',("Cargo"  +j2)[:c1]+'|',("Sueldo"+j2)[:c1]+'|', ("Descuento"+j2)[:c1]+'|',("Sueldo neto"+j2) [:c1]+'|')
            print("-"+x3+x3+x3+x3+x3+x3+x3)
            for linea in texto:
                if fecha in linea.lower():
                    datos_buscados = linea.split(";")
                    print('|',(datos_buscados[0]+j2)[:c1]+'|  ',(datos_buscados[1]+j2)[:c1]+'|',  (datos_buscados[2]+j2)[:c1]+'|',  (datos_buscados[3]+j2)[:c1]+'|',  (datos_buscados[4]+j2)[:c1]+'|',  (datos_buscados[5]+j2)[:c1]+'|',  (datos_buscados[6]+j2)[:c1]+'|')
                    print("-"+x3+x3+x3+x3+x3+x3+x3)


    respuesta=input("\nQue deseas hacer.\n1:Agregar.\n2:Buscar.\n3:Ver todo\n4:Salir del programa.\nEleccion: ")
    print()
    if respuesta=="1":
        añadirenpleados()
    elif respuesta == "2":
        buscarempleado(g2,g1)
    elif respuesta=="3":
        dibujartodo(g2,g1)
    else:
        seguir=False