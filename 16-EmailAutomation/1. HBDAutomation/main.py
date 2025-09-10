import datetime as dt
import pandas as pd
import random
import smtplib
import os

# ----------------- CONSTANTS ----------------- #
GMAIL_SMTP = os.getenv("GMAIL_SMTP")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_KEY")
EMAIL = os.getenv("GMAIL_EMAIL")
RECEIVER_EMAIL = os.getenv("OUTLOOK_EMAIL")

# HINT 1: Create a tuple from today's month and day using datetime. e.g.
today = (dt.datetime.now().month, dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv('birthdays.csv')

# HINT 3: Use dictionary comprehension and dictionary from birthday.csv:
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today] # ['name']
    # print(birthday_person)
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])


# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
    # ----------------- CONNECTION ----------------- #
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=EMAIL,
            password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person['email'],
            msg=f'Subject: Happy Birthday'
                f'\n\n{contents}')

