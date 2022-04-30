"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as MessageBox
from usuarios import usuario

root = Tk()

nombreUsuario = StringVar()
contraUsuario = StringVar()
usuarios = []

def createGUI():
    # ventana principal
    #root = Tk()
    root.title("Login Usuario")

    # mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320)#,bg="lightblue")

    # textos y titulos
    titulo = Label(mainFrame,text="Login de Usuario con Python",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    nombreLabel = Label(mainFrame,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)
    passLabel = Label(mainFrame,text="Contraseña: ")
    passLabel.grid(column=0,row=2)

    # entradas de texto
    # nombreUsuario = StringVar()
    nombreUsuario.set("")
    nombreEntry = Entry(mainFrame,textvariable=nombreUsuario)
    nombreEntry.grid(column=1,row=1)

    # contraUsuario = StringVar()
    contraUsuario.set("")
    contraEntry = Entry(mainFrame,textvariable=contraUsuario,show="*")
    contraEntry.grid(column=1,row=2)

    # botones
    iniciarSesionButton = ttk.Button(mainFrame,text="Iniciar Sesion",command=iniciarSesion)
    iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    cerrarSesionButton = ttk.Button(mainFrame,text="Cerrar Sesion",command=cerrarSesion)

    registrarButton = ttk.Button(mainFrame,text="Registrar",command=registrarUsuario)
    registrarButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)
    
    root.mainloop()


def iniciarSesion():
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            test = user.conectar(contraUsuario.get())
            if test:
                MessageBox.showinfo("Conectado",f"Se inicio sesion en [{user.nombre}] con EXITO!!!")
            else:
                MessageBox.showerror("Error","Contraseña incorrecta")
            break
    else:
        MessageBox.showerror("Error","No existen usuarios con ese nombre")

def cerrarSesion():
    pass

def registrarUsuario():
    name = nombreUsuario.get()
    passwd = contraUsuario.get()
    newUser = usuario(name,passwd)
    usuarios.append(newUser)
    MessageBox.showinfo("Resgistro Exitoso",f"Se registro el usuario [{name}] con EXITO!!!")
    nombreUsuario.set("")
    contraUsuario.set("")

if __name__=="__main__":
    # user1 = usuario(input("Ingrese un nombre: "),input("Igrese una contraseña: "))
    user1 = usuario("lucas","1234")
    usuarios.append(user1)
    createGUI()