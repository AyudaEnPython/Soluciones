"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import smtplib
import re
regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
def sendMail(host,port,email_id,email_pass,message,from_list,to_list):
    try: 
        smtp = smtplib.SMTP(host, port) 
        smtp.starttls() 
        smtp.login(email_id,email_pass)
        smtp.sendmail(from_list, to_list,message) 
        smtp.quit() 
        print ("Correo Enviado Correctamente") 
    except Exception as ex: 
        print("Something went wrong....",ex)
def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        print("Error en el Correo!")
        return False
def run():
    mainLoop=True
    while(mainLoop):
        print("---------------------------------------------------------------------")
        print("Enviar un Correo ")
        from_list = input("Desde : ")
        to_list = input("Para : ")
        message = input("Entre el Mensaje : ")
        if isValid(from_list) and isValid(to_list)  and len(message)>1:
            domain = to_list.split("@")[1]
            if domain=='gmail.com':
                server = 'smtp.gmail.com'
            elif domain=='hotmail.com':
                server = 'smtp-mail.outlook.com'
            sendMail(server,
                     587, 
                     'yourMail', ##su Correo,
                     'yourPass', ##su Contrasena
                     message,
                     from_list,
                     to_list)
        c = input("Desea Enviar Otro Correo (S/N) :") 
        if c == 'S':
            mainLoop=True
        else:
            mainLoop=False
    print("Gracias! por Utilizar nuestros Softwares!!")
run()