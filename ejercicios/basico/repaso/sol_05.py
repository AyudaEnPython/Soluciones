"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def main():
    mensaje = "Veo que tu cuenta de correo está registrada en "
    email = input("Ingresar email: ")
    _, domain = email.split("@")
    mail_server, _ = domain.split(".")
    if mail_server == "google":
        mensaje += "Google"
    elif mail_server == "outlook" or mail_server == "hotmail":
        mensaje += "Microsoft"
    elif mail_server == "yahoo":
        mensaje += "Yahoo"
    else:
        mensaje += mail_server.capitalize()
    print(mensaje)


if __name__ == "__main__":
    main()
