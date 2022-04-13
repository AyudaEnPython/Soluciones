"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import smtplib
from email.mime.text import MIMEText
# pip install prototools
from prototools import email_input, password_input, str_input, main_loop
from soluciones.caesar import encrypt


def send_mail(
    host: str,
    port: int,
    sender: str,
    password: str,
    receiver: str,
    subject: str,
    message: str,
) -> None:
    msg = MIMEText(encrypt(message, 3))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


def main():
    sender = email_input("Desde: ")
    receiver = email_input("Para: ")
    subject = str_input("Asunto: ")
    message = str_input("Mensaje: ")
    password = password_input("Password: ")
    host = "smtp.gmail.com" if "gmail" in sender else "smtp-mail.outlook.com"
    send_mail(
        host,
        587,
        sender,
        password,
        receiver,
        subject,
        message,
    )


if __name__ == "__main__":
    main_loop(main)
