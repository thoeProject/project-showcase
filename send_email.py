import smtplib,ssl,os
import secure_pw

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ngoctho.ou.93@gmail.com"
    password = secure_pw.PASSWORD
    receiver = "ngoctho.ou.93@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)