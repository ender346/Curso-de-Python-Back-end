class Persona:
    def saludar(self):
        print("Hola!")

persona = Persona()
persona.saludar()

import smtplib

def enviar_correo(destinatario, asunto, cuerpo):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("mi_correo@gmail.com", "mi_contraseña")
        smtp.sendmail("mi_correo@gmail.com", destinatario, f"Asunto: {asunto}\n\n{cuerpo}")

enviar_correo("juan@example.com", "Hola, Juan", "Este es un correo electrónico de prueba.")
