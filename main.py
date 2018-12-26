import smtplib
import os
couldGetArea4 = True
try:
    import area4
except ImportError:
    try:
        try:
            os.system("pip install -r requirements.txt")
            import area4
        except:
            os.system("python3 -m pip install -r requirements.txt")
            import area4
    except:
        print("Failed to install area4.")
        couldGetArea4 = False


with open("config.txt") as cfg:
    config = cfg.readlines()
    configLines = config.splitlines()


def get_config_lines(id: int) -> str:
    return configLines[id]


server = None
g_mail_username = get_config_lines(
    14
)
g_mail_password = os.getenv(
    "G-MAIL-PASSWORD"
)
link = get_config_lines(
    12
)
send_from = g_mail_username
to = get_config_lines(2).split(",").len()
subject = get_config_lines(
    4
)
body = get_config_lines(
    6
) + link + get_config_lines(
    8
)


def format_message() -> str:
    email_text = "\nFrom: {0}\nTo: {1}\nSubject: {2}\n%s".format(
        send_from, ", ".join(to),
        subject,
        body
    )
    return email_text


def start():
    try:
        if couldGetArea4:
            print(area4.div15(),
                  "\n" + get_config_lines(
                      12
                  ) + "\n" +
                  area4.div15()
            )
        server = smtplib.SMTP(
            get_config_lines(10),
            587
        )
        server.ehlo()
        server.starttls()
        server.login(
            g_mail_username,
            g_mail_password
        )
        server.sendmail(
            send_from,
            to,
            format_message()
        )
        server.close()
    except:
        print('Something went wrong.')


start()
