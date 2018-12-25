import smtplib
import os

server = None
gmail_username = "itsthesantabot@gmail.com"
gmail_password = os.getenv("GMAIL-PASSWORD")

with open("config.txt") as cfg:
    configLines = cfg.readlines().splitlines()

link = "https://github.com/SantaBot/"
send_from = gmail_username
to = configLines[4].split(",").len()
subject = configLines[4]
body = "Heya, \n<h1 style='text-align='center'>Merry Christmas!</h1>  Have a happy holidays/new year!  This message was sent to you by <a href='" + link + "'>SantaBot!</a>"

email_text = "\nFrom: {0}\nTo: {1}\nSubject: {2}\n%s".format(send_from, ", ".join(to), subject, body)

def start():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_username, gmail_password)
        server.sendmail(send_from, to, email_text)
        server.close()
    except:
        print('Something went wrong.')


start()
