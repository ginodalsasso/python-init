import smtplib

to = input("Enter the email of the recipient: \n")

message = input("Enter the message you want to send: \n")

def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587) # Serveur SMTP de Gmail sur le port 587
    server.starttls() # Démarre le chiffrement
    server.login("senderEmail", "password")
    server.sendmail("senderEmail", to, message)
    server.close()

sendEmail(to, message)