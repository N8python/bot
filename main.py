import smtplib
import os
from typing import List

couldGetArea4 = True
try:
    import area4
except ImportError:
    try:
        try:
            os.system(
                "pip install -r requirements.txt"
            )
            import area4
        except:
            os.system(
                "python3 -m pip install -r requirements.txt"
            )
            import area4
    except:
        print("Failed to install area4.")
        couldGetArea4 = False


with open("config.txt") as cfg:
    configLines = cfg.readlines()


def get_config_lines(given_id: int) -> str:
    return configLines[given_id]


g_mail_username = get_config_lines(
    14
)
g_mail_password = os.getenv(
    "G-MAIL-PASSWORD"
)
link = get_config_lines(
    12
)
people_to = get_config_lines(2).split(",")
send_from = g_mail_username
subject = get_config_lines(4)
body = get_config_lines(6) + link + get_config_lines(8)


def format_message() -> str:
    email_text = "\nFrom: {0}\nTo: {1}\nSubject: {2}\n%s".format(
        send_from, ", ".join(people_to),
        subject,
        body
    )
    return email_text


def start():
    try:
        for i in range(len(people_to)):
            if couldGetArea4:
                print(area4.div15(), "\n" + get_config_lines(12) + "\n" + area4.div15())
            server = smtplib.SMTP(
                get_config_lines(10),
                587
            )
            server.starttls()
            server.login(
                g_mail_username,
                g_mail_password
            )
            server.sendmail(
                send_from,
                people_to[i],
                format_message()
            )
        server.quit()
    except:
        print(
            'Something went wrong.'
        )


start()
