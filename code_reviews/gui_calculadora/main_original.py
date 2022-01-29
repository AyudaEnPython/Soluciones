"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *
from math import *

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x600")

#dimensión de botones
ancho_btn = 6
alto_btn = 2

#variable para función clic
text = StringVar()
operador=""

#función validar clic
def btnClic(num):
    global operador
    operador = operador + str(num)
    text.set(operador)

#función para realizar operaciones
def operacion():
    global operador
    try:
        opera = eval(operador)
    except:
        clear()
        opera="ERROR"
    
    text.set(opera)

def clear():
    global operador
    operador = ""
    text.set(operador)

#crear los botones
btn0 = Button(ventana, text="0", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(0)).place(x=12, y=120)
btn1 = Button(ventana, text="1", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(1)).place(x=92, y=120)
btn2 = Button(ventana, text="2", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(2)).place(x=172, y=120)
btn3 = Button(ventana, text="3", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(3)).place(x=252, y=120)
btn4 = Button(ventana, text="4", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(4)).place(x=12, y=190)
btn5 = Button(ventana, text="5", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(5)).place(x=92, y=190)
btn6 = Button(ventana, text="6", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(6)).place(x=172, y=190)
btn7 = Button(ventana, text="7", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(7)).place(x=252, y=190)
btn8 = Button(ventana, text="8", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(8)).place(x=12, y=260)
btn9 = Button(ventana, text="9", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(9)).place(x=92, y=260)
btnpi = Button(ventana, text="π", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("pi")).place(x=172, y=260)
btnsep = Button(ventana, text=",", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic(",")).place(x=252, y=260)
btnsum = Button(ventana, text="+", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("+")).place(x=12, y=330)
btnres = Button(ventana, text="-", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("-")).place(x=92, y=330)
btnmul = Button(ventana, text="*", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("*")).place(x=172, y=330)
btndiv = Button(ventana, text="/", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("/")).place(x=252, y=330)
btnraiz = Button(ventana, text="R", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("sqrt")).place(x=12, y=400)
btnlimp = Button(ventana, text="C", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=clear).place(x=92, y=400)
btnpor = Button(ventana, text="%", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=lambda:btnClic("%")).place(x=172, y=400)
btnigual = Button(ventana, text="=", font=('Arial', 14), width=ancho_btn, height=alto_btn, command=operacion).place(x=252, y=400)

pantalla = Entry(ventana, font=('Arial', 20, 'bold'), width=23, bd=10, bg="white", textvariable=text, justify="right").place(x=12, y=40)

ventana.mainloop()