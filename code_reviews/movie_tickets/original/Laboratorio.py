from tkinter import *
from io import open
from tkinter import ttk
from tkinter import messagebox


bill = open("Registro.txt", "a")



def agregar():
    id = cajaid.get()
    tickets = int(cajacantidad.get())
    dia = opt_dias.get()
    pelicula = opt_peliculas.get()

    if(dia == "Lunes" or dia == "Martes"):
        cop = (tickets*20000)

    elif(dia == "Miercoles" or dia == "Jueves"):
        cop = (tickets*15000)

    elif(dia == "Viernes" or dia == "Sabado"):
        cop = (tickets*30000)

    elif(dia == "Domingo"):
        cop = (tickets*35000)

    elif(dia == ""):
        messagebox.showerror(message="Debe ingresar todos los campos primero", title="Alerta")

    elif(id == ""):
        messagebox.showerror(message="Debe ingresar una identificación valida", title="Alerta")

    elif(tickets == ""):
        messagebox.showerror(message="Debe ingresar la cantidad de tiquetes que desea comprar", title="Alerta")

    messagebox.showinfo(
    message=f"El total a pagar es:  ${cop} COP.", title="Factura")

    if(dia != "", tickets != "" and id != ""):
        bill = open("Registro.txt", "a")
        dia = str(dia)
        id = str(id)
        cantidad = str(tickets)
        pelicula = str(pelicula)
        cop = str(cop)
        bill.write(f"Dia: {dia} Identificación: {id} Cantidad: {cantidad} Pelicula: {pelicula} Precio: {cop} COP")
        bill.write("\n")
        bill.close()


def agregarDos():
    id = cajaid.get()
    tickets = int(cajacantidad.get())
    dia = opt_dias.get()
    pelicula = opt_peliculas.get()

    if(dia == ""):
        messagebox.showerror(message="Por favor complete todos los campos", title="Alerta")

    elif id == "":
        messagebox.showerror(message="Por favor ingrese un número de identificación valido", title="Alerta")

    elif(tickets == ""):
        messagebox.showerror(message="Por favor ingrese la cantidad de tiquetes que desea comprar", title="Alerta")

    elif dia == "Lunes" or dia == "Martes":
        cop = (tickets*20000)
        dolar = (cop/3800)

    elif dia == "Miercoles" or dia == "Jueves":
        cop = (tickets*15000)
        dolar = (cop/3800)

    elif dia == "Viernes" or dia == "Sabado":
        cop = (tickets*30000)
        dolar = (cop/3800)

    elif dia == "Domingo":
        cop = (tickets*35000)
        dolar = (cop/3800)

    messagebox.showinfo(
    message=f"El total a pagar es: ${dolar} USD.", title="Factura")

    if (dia != ""and tickets != "" and id != ""):
        bill = open("Registro.txt", "a")
        dia = str(dia)
        id = str(id)
        cantidad = str(tickets)
        pelicula = str(pelicula)
        cop = str(cop)
        bill.write(
            f"Dia: {dia} Identificación: {id} Cantidad: {cantidad} Pelicula: {pelicula} Precio: {cop} COP/ {dolar} USD")

        bill.write("\n")
        bill.close()


def registro():
    consulta = cajaconsulta.get()
    if consulta == "":
        messagebox.showerror(
            message="Por favor ingrese su consulta", title="Error")
    else:
        bill = open("Registro.txt", "r")
        fact = bill.readlines()
        for linea in fact:
            if consulta in linea:
                messagebox.showinfo(
                    message=f" {linea}", title="Mensaje")
        bill.close()


def mostrar():
    archivo = open("Peliculas.txt", "r")
    messagebox.showinfo("Registro", archivo.read())
    archivo.close()


def nuevaVentana():
    global cajaid
    global cajacantidad
    global opt_peliculas
    global opt_dias
    global cajaconsulta
    ventana = Tk()
    ventana.title("MundoCine")
    ventana.geometry("800x250")
    ventana.resizable(0, 0)
    ventana.iconbitmap("cine.ico")
    cajaid = Entry(ventana)
    cajaid.grid(pady=5, padx=5, row=0, column=1)

    cajaconsulta = Entry(ventana)
    cajaconsulta.grid(pady=5, row=5, column=2)
    label_id = Label(ventana, text="Identificación: ")
    label_id.grid(row=0, column=0)
    label_cantidad = Label(ventana, text="Cantidad de tiquetes: ")
    label_cantidad.grid(row=1, column=0)
    cajacantidad = Entry(ventana)
    cajacantidad.grid(pady=5, padx=5, row=3, column=1)
    label_cantidad.grid(row=3, column=0)
    label_box_dia = Label(ventana, text="Lista de dias disponibles:")
    label_box_dia.grid(row=4, column=0)
    label_box_pelicula = Label(ventana, text="Lista de peliculas disponibles:")
    label_box_pelicula.grid(row=4, column=1)
    label_consulta = Label(ventana, text="Ingrese su consulta: ")
    label_consulta.grid(row=4, column=2)

    opt_dias = ttk.Combobox(ventana, state="readonly")
    opt_dias["values"] = ["Lunes", "Martes", "Miercoles",
                        "Jueves", "Viernes", "Sábado", "Domingo"]
    opt_dias.grid(pady=5, row=5, column=0, padx=5)
    opt_peliculas = ttk.Combobox(ventana, state="readonly")
    opt_peliculas["values"] = ["El conjuro", "La noche del demonio", "Ouija", "Interestelar", "Cuando las luces se apagan",
                            "La huerfana", "Hereditary", "Annabelle", "Cadaver", "El silencio", "Verdad o reto", "Doctor sueño", "Mamá", "Ma", "Descendientes","El privilegio","Sin respiro","Perdona nuestras ofensas"]
    opt_peliculas.grid(pady=5, padx=5, row=5, column=1)

    pagar_btn = Button(ventana, text="Pagar en COP", command=agregar)
    pagar_btn.grid(row=6, column=0)
    pagar_btn2 = Button(ventana, text="Pagar en USD", command=agregarDos)
    pagar_btn2.grid(row=6, column=1)
    registro_id_btn = Button(ventana, text="Ver registro", command=registro)
    registro_id_btn.grid(row=6, column=2)
    label_info = Label(
        ventana, text="Nota: Para ver el registro de consultas puede ingresar su número de identificación\n o dia de facturación ")
    label_info.grid(row=8, column=0)
    ventana.mainloop()

def cerrar():

    login.destroy()


def user_password():
    
    archivo = open("user.txt","r")
    usuario = str(caja1.get())
    archivo2 = open("password.txt","r")
    contra = str(caja2.get())
    if usuario == archivo.readline() and contra == archivo2.readline():
        cerrar()
        nuevaVentana()
        
    else:
        messagebox.showerror(
        message="Usuario o contraseña incorrecta", title="Alerta")
    
def verificar():
    cantickets = cajacantidad.get()
    if cantickets == "": 
        messagebox.showerror(
        message="Por favor ingrese la cantidad de tiquetes a comprar", title="Alerta")
        
    

login = Tk()
login.title("Login")
login.geometry("250x150")
login.resizable(0,0)
login.iconbitmap("loginico.ico")
label1=Label(login, text="Usuario")
label1.grid(pady=5, row=0, column=0)
caja1 = Entry(login)
caja1.grid(pady=5, row=0, column=1)
label2=Label(login, text="Contraseña")
label2.grid(pady=5, row=2, column=0)
caja2=Entry(login, show="*")
caja2.grid(pady=5, row=2, column=1)
boton1 = Button(login, text="Iniciar sesión",command=user_password)
boton1.grid(padx= 5, pady=5, row=3, column=0)
boton2= Button(login, text="Cerrar",command=cerrar)
boton2.grid(pady=5, row=3, column=1)

login.mainloop()