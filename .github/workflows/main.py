import os

import pandas as pd
import smtplib
import datetime as dt



email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month


birthday = pd.read_csv('birthdays.csv')

birth_day = birthday[birthday.day == day]
birth_month = birthday[birthday.month == month]
day_b = birth_day.day
day_month = birth_month.month
name = birth_day.name[0]
email = birth_day.email[0]

print(name)
place_holder = "[NAME]"
name_to_replace = name

if day == day_b.item() and month == day_month.item():

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open("./letter_templates/letter_3.txt", "r") as f:
        letter_3 = f.read()
    letter_3 = letter_3.replace(f"{place_holder}",f"{name}")
    with open("./letter_templates/letter_3.txt", "w") as f:
        f.write(letter_3)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com", 587) as send:
    send.starttls()
    send.login(my_email, password)
    send.sendmail(my_email, f"{email}", f"Subject: A king was born today\n\n{letter_3}")


