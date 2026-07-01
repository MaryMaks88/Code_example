import os
import pandas as pd
import datetime as dt
from random import randint
import smtplib

EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("APP_PASSWORD")

# 1. Update the birthdays.csv

data_list = pd.read_csv("birthdays.csv")
data_dict = data_list.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
day = now.day
month = now.month

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)

    for person in data_dict:
        if person["month"] == month and person["day"] == day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

            with open(f"letter_templates/letter_{randint(1,3)}.txt", mode="r") as letter_template:
                letter = letter_template.read()

                letter_to_send = letter.replace("[NAME]", person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=person["email"],
                                    msg=f"Subject: Happy Birthday!\n\n{letter_to_send}")

print("Email successfully sent")



