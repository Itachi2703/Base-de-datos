import smtplib

class sendmailclass:
    
    def sendmailnow():
        print("Solo falta configurar el usuario y contrasena y ya se puede usar")
        try:
            message = str(input("Mensaje: "))
            destintario = str(input("destintario: "))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("Your mail", "Your password")
            server.sendmail("addressee", destintario, message)
            server.quit()
            print("Finish")
        except:
            print("Error en sendmailnow")


