import os
import smtplib
import datetime as dt
import random

# ------------- DATETIME NOW ------------- #
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
week_day = now.weekday()
print(now)

# ------------- NEW DATETIME OBJECT ------------- #
date_of_birth = dt.datetime(year=1994, month=9, day=26, hour=8)
print(date_of_birth)


# ----------------- CONSTANTS ----------------- #
GMAIL_SMTP = os.getenv("GMAIL_SMTP")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_KEY")
GMAIL_EMAIL_PASSWORD = 'fkI1$7kztG0!y7p)#Qei3zi!e)*0t+W3x3R'
EMAIL = os.getenv("GMAIL_EMAIL")
PORT_NUMBER = os.getenv("PORT_NUMBER")
OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")


# ------------- DATE AND TIME SET UP ------------- #
now = dt.datetime.now()
weekday = now.weekday()

    # ------------- OPENING A FILE ------------- #
with open('quotes.txt', 'r') as quotes:
    all_quotes = quotes.readlines()
    quote = random.choice(all_quotes)

# ----------------- CONNECTION ----------------- #
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=EMAIL,
        password=GMAIL_APP_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=OUTLOOK_EMAIL,
        msg=f'Subject:Motivation'
            f'\n\n{quote}')

