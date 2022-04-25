#! /bin/python

# interfaces gráficas: tkinter: calculadora - WIP

import os
import re
import tkinter as tk
import webbrowser as wb
import math as m
import base64
from PIL import Image
from io import BytesIO

version = "1.0.7"

coma = False
operator = False
operatorPos = 0
noFirst = [".", "%", "+", "×", "÷", "C", "**", "=", ")"]
operators = ["%", "+", "-", "×", "÷", "**", "√"]
OpVaAfOp = ["√", "-", "("]  # operadores validos despues de operadores
history = [""]


def buttonPressed(button):

    global coma
    global operator
    global operatorPos
    global noFirst
    global operators
    global OpVaAfOp
    global history

    screenValue = screenString.get()
    lens = len(screenValue)

    if button:
        # calculate
        if button == "=" and lens >= 2:
            calculate(screenValue)

        # clear
        elif button == "C":
            screenString.set("")
            screenHistory.config(text="", cursor="")
            history = []
            coma = False
            operator = False

        # delete last
        elif button == "←":
            screenString.set(screenValue[:-1])
            if lens == 0:
                screenHistory.config(text="", cursor="")
                history = []
                coma = False
                operator = False

        # operators, coma, e = no pueden ingresarse en primera instancia
        elif button in noFirst and lens == 0:
            pass
        # que sí el cero es el primer dígito solo pueda seguir la coma
        elif button != "." and lens == 1 and screenValue[-1] == "0":
            pass
        # que sí el último ingreso es un operator no pueda seguir otro operator
        # a menos que sea operador valido tras operador OpVaAfOp
        elif button in operators and lens > 0  \
                and screenValue[-1] in operators and button not in OpVaAfOp:
            pass

        # numeros negativos
        elif button == "-" and lens == 0 or button == "-" and lens >= 1 \
                and screenValue[-1] != "-" and screenValue[-1] != "√":
            screenString.set(f"{screenValue}{button}")

        # control de √
        elif button == "√" and lens == 0:
            screenString.set(f"{screenValue}{button}")
        elif(button == "√" and (screenValue[-1] not in operators
                                or screenValue[-1] == button)):
            pass

        # que no se pueda ingresar más de 1 coma por número
        elif button in operators and button not in OpVaAfOp:
            screenString.set(f"{screenValue}{button}")
            operatorPos = len(screenValue)
            operator = True
            coma = False

        # control de la coma
        # cuando no hay coma ni operator
        elif button == "." and button not in screenValue and not coma:
            screenString.set(f"{screenValue}{button}")
            coma = True
        # cuando ya hay coma y operator
        elif button == "." and button in screenValue and operator \
                and lens > operatorPos+1 \
                and screenValue[operatorPos:].count(button) == 0:
            screenString.set(f"{screenValue}{button}")
            coma = True

        # parentesis
        elif button == "(" and lens > 2 and (screenValue[-1] not in operators
                                             or screenValue[-1] != "("):
            pass
        elif button == "(" and lens == 0:
            screenString.set(f"{screenValue}{button}")

        # ingreso general
        elif button not in noFirst and button != "-"\
                and (button != "(" or screenValue[-2:] != "(("):
            screenString.set(f"{screenValue}{button}")

        else:
            pass


def calculate(string):

    global history
    global screenHistory

    stringc = string

    result = 0
    stringc = re.sub("÷", "/", stringc)
    stringc = re.sub("×", "*", stringc)

    # squareRoot
    if "√" in stringc:
        operatorsL = {}
        operators_re = ["+", "-", "*", "/", "√"]

        # creating dictionaries with operators and indexes
        for oPos in range(len(stringc)):
            if stringc[oPos] in operators_re:
                operatorsL[oPos] = stringc[oPos]
        dictKeys = list(operatorsL.keys())
        dictValues = list(operatorsL.values())

        # √ for m.sqrt sustitution
        cutStart, cutEnd, numToR, numToRL = 0, 0, 0, []
        for n in range(len(stringc)):
            if n in operatorsL and operatorsL[n] == "√":
                rCount = dictValues.count("√")

                if cutStart != dictKeys.index(n):
                    cutStart = dictKeys.index(n)
                    cutStart = dictKeys[cutStart]

                # if squareRoot operator is not the last operator
                if cutStart != dictKeys[-1]:
                    cutStart = dictKeys.index(n)
                    cutEnd = dictKeys[cutStart+1]
                    cutStart = dictKeys[cutStart]
                # if squareRoot operator is the last operator
                else:
                    cutStart = dictKeys[-1]
                    cutEnd = len(stringc)

                numToR = stringc[cutStart+1:cutEnd]
                numToRL.append(numToR)

        # borrado de numToRs y remplazo de √
        i = 0
        while i < len(numToRL):
            stringc = re.sub(numToRL[i], "", stringc, count=1)
            stringc = re.sub(
                "√", f"m.sqrt({numToRL[i]})", stringc, count=1)
            i += 1

    try:
        result = eval(stringc)

        if len(stringc)+len(str(result)) > 35:
            result = round(result, 5)

        result = str(result)
        if result[-2:] == ".0":
            result = result[:-2]

        if result != string:
            history.append(f"{string} = {result}")
            screenString.set(result)

        if len(history) > 5:
            history.pop(0)

        l4h = ""
        for i in history:
            l4h += (f"{i}\n")
        screenHistory.config(text=l4h, cursor="")
        screenHistory.bind("<Button>", lambda e:
                           screenString.set(history[-1][:history[-1]
                                                        .index("=")-1]))

        # 2+2
        if stringc == "2+2":
            result = "2+2=5"
            def openweb(url): wb.open_new(url)
            screenString.set(result)
            screenHistory.config(
                text="La libertad es poder decir libremente \n\
que dos y dos son cuatro.\n\
Si se concede esto,\n\
todo lo demás vendrá por sí solo.", cursor="hand1")
            screenHistory.bind(
                "<Button>", lambda e:
                openweb("https://es.wikipedia.org/wiki/2_+_2_=_5"))

    except (SyntaxError, NameError):
        screenHistory.config(text="unexpected error", cursor="")
        screenHistory.unbind("<Button>")
        screenString.set("error")


# diseño #
# root
root = tk.Tk()

iconb64code = "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABhGlDQ1BJQ0MgcHJ\
vZmlsZQAAKJF9kT1Iw0AcxV9bRSkVBzNIcchQnSyIigguWoUiVAi1QqsOJpd+QZOGJMXFUXAtOPixW\
HVwcdbVwVUQBD9A3NycFF2kxP8lhRYxHhz34929x907INioMM3qGgM03TbTyYSYza2KPa8IQ0AIUcz\
IzDLmJCkF3/F1jwBf7+I8y//cn6NPzVsMCIjEs8wwbeIN4qlN2+C8TyywkqwSnxOPmnRB4keuKx6/c\
S66HOSZgplJzxMLxGKxg5UOZiVTI54kjqmaTvnBrMcq5y3OWqXGWvfkL4zk9ZVlrtMcQhKLWIIEEQp\
qKKMCG3FadVIspGk/4eOPun6JXAq5ymDkWEAVGmTXD/4Hv7u1ChPjXlIkAXS/OM7HMNCzCzTrjvN97\
DjNEyD0DFzpbX+1AUx/kl5va7EjoH8buLhua8oecLkDDD4Zsim7UohmsFAA3s/om3LAwC0QXvN6a+3\
j9AHIUFepG+DgEBgpUva6z7t7O3v790yrvx+TTHK0ia06WQAAAAZiS0dEADMAMwAzhj9D9gAAAAlwS\
FlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+UKFAMeKhIqsKgAAAFsSURBVHja7ddBToNAFAbg9xi0G6t\
3MPEKaowH8QRdwVqqEZxgjAdgU114DE/gwjt4BFZtTNDODK5ctZgMKZTO/P+SN014X2ceQIQgCIL4G\
24qVFWVM/MNEQVd3sDd62WnDY71yJwsxg9XyVu2rt7YHDNPu26+jyzEd/B5ML9tqv/XoHBlm8/DH9E\
GwIsAAAAA2FyMMWSM8RdASklSShwBAABgdxK2/aFSyqoWhqFbAHmeW9WGOhxbAwix+nqttW6sOXcE0\
jRduZZlWWMNQxAAAHBrBqzVDAK/Af6GII6Arztg03mafFitT57P3AJgZr93QDI79xugJrM9gLIsMQS\
3HcF7Vut1vXQL4HHybrX+enbqFoAxyu8jMH25wJsgAAAAAAAAYIiPwbquB/dl1ytAURRW6+M4dgtgq\
P9obwBRFGEIAgAAAAAAAAAAAAC4CqBdafJoOVLWAMx8T0Rq55tX++r46zAjBEEQBFnJL7xTUZaNN0R\
ZAAAAAElFTkSuQmCC"
ico = Image.open(BytesIO(base64.b64decode(iconb64code)))
ico.save('calc.png', 'PNG')
ico = "calc.png"
root.iconphoto(False, tk.PhotoImage(file=ico))

root.title(f"Calculadora v{version}")
root.resizable(False, False)
# root.option_add("*Font","DejaVu 11")

# frame
mainFrame = tk.Frame(root)
mainFrame.config(bg="#009900", bd="5")
mainFrame.pack(expand=True, fill="both", side="bottom",
               anchor="center", ipadx="0", ipady="0")


# desktop adjust vars
desktop = os.environ.get('DESKTOP_SESSION')
if desktop == "plasmax11":
    ipadxSH,ipadxSS,wthSH,wthSS = 17,15,35,29
elif desktop == ("gnome" or "gnome-classic"):
    ipadxSH,ipadxSS,wthSH,wthSS = 20,19,31,26
elif desktop == "gnome-wayland":
    ipadxSH,ipadxSS,wthSH,wthSS = 24,23,31,26
else:
    ipadxSH,ipadxSS,wthSH,wthSS = 20,19,31,26

# screen history #
mFScreenHistory = tk.Frame(mainFrame)
screenHistory = tk.Label(mFScreenHistory)
screenHistory.grid(ipadx=ipadxSH, ipady=12, columnspan=5)
screenHistory.config(width=wthSH, height=6, bd=0, bg="#333333", fg="#aaaaaa",
                     highlightbackground="#006600", highlightcolor="#006600",
                     font=("DejaVu", 12), justify="center", relief="flat")
mFScreenHistory.pack(expand=True, fill="none", side="top",
                     anchor="center")


# screen #
screenString = tk.StringVar("")
mFScreen = tk.Frame(mainFrame)
screen = tk.Entry(mFScreen, textvariable=screenString)
screen.grid(ipadx=ipadxSS, ipady=12, columnspan=5)
screen.config(width=wthSS, bd=0, bg="#222222", \
    fg="#009900", highlightthickness=0, 
    highlightcolor="#222222", highlightbackground="#222222",
              insertbackground="#009900", font=("DejaVu", 14),
              justify="center", relief="flat")
mFScreen.pack(expand=True, fill="both", side="top",
              anchor="center")

# numeros y operators
mFButtons = tk.Frame(mainFrame)
mFButtons.config(bg="#222222")
mFButtons.pack(expand=True,fill="both",side="top",anchor="center")
pbx = 10  # ipad(xy) nums button size
pby = 10
# fila 1
button7 = tk.Button(mFButtons, text="7", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("7")).grid(row=1, column=0, ipadx=pbx,
                                             ipady=pby)
button8 = tk.Button(mFButtons, text="8", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("8")).grid(row=1, column=1, ipadx=pbx,
                                             ipady=pby)
button9 = tk.Button(mFButtons, text="9", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("9")).grid(row=1, column=2, ipadx=pbx,
                                             ipady=pby)
buttonDividir = tk.Button(mFButtons, text="÷", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("÷")).grid(row=1, column=3, ipadx=pbx, ipady=pby)
buttonClear = tk.Button(mFButtons, text="C", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("C")).grid(row=1, column=4, ipadx=pbx, ipady=pby)
# fila 2
button4 = tk.Button(mFButtons, text="4", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("4")).grid(row=2, column=0, ipadx=pbx,
                                             ipady=pby)
button5 = tk.Button(mFButtons, text="5", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("5")).grid(row=2, column=1, ipadx=pbx,
                                             ipady=pby)
button6 = tk.Button(mFButtons, text="6", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("6")).grid(row=2, column=2, ipadx=pbx,
                                             ipady=pby)
buttonMultiplicar = tk.Button(mFButtons, text="×", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("×")).grid(row=2, column=3, ipadx=pbx, ipady=pby)
buttonRaiz = tk.Button(mFButtons, text="√", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("√")).grid(row=2, column=4, ipadx=pbx, ipady=pby)
# fila 3
button1 = tk.Button(mFButtons, text="1", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("1")).grid(row=3, column=0, ipadx=pbx,
                                             ipady=pby)
button2 = tk.Button(mFButtons, text="2", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("2")).grid(row=3, column=1, ipadx=pbx,
                                             ipady=pby)
button3 = tk.Button(mFButtons, text="3", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("3")).grid(row=3, column=2, ipadx=pbx,
                                             ipady=pby)
buttonResta = tk.Button(mFButtons, text="−", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("-")).grid(row=3, column=3, ipadx=pbx, ipady=pby)
buttonPotencia = tk.Button(mFButtons, text="xⁿ", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("**")).grid(row=3, column=4, ipadx=pbx, ipady=pby)
# fila 4
button0 = tk.Button(mFButtons, text="0", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                    buttonPressed("0")).grid(row=4, column=0, ipadx=pbx,
                                             ipady=pby)
buttonComa = tk.Button(mFButtons, text=".", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed(".")).grid(row=4, column=1, ipadx=pbx, ipady=pby)
buttonPercent = tk.Button(mFButtons, text="%", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("%")).grid(row=4, column=2, ipadx=pbx, ipady=pby)
buttonSuma = tk.Button(mFButtons, text="+", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("+")).grid(row=4, column=3, ipadx=pbx, ipady=pby)
buttonBack = tk.Button(mFButtons, text="←", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("←")).grid(row=4, column=4, ipadx=pbx, ipady=pby)

# fila 5
buttonIgual = tk.Button(mFButtons, text="=", width=20, relief="flat", bg="#009900",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
                        buttonPressed("=")).grid(row=5, column=0,
                                                 ipadx=12, ipady=pby,
                                                 columnspan=3)
buttonParentesisL = tk.Button(mFButtons, text="(", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed("(")).grid(row=5, column=3, ipadx=pbx, ipady=pby)
buttonParentesisR = tk.Button(mFButtons, text=")", width=3, relief="flat", bg="#31363b",
    fg="#dddddd", activebackground="#009900", highlightthickness=1, 
    highlightcolor="#009900", highlightbackground="#31363b", command=lambda:
    buttonPressed(")")).grid(row=5, column=4, ipadx=pbx, ipady=pby)


mFButtons.pack()

root.mainloop()
