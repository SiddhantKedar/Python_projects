import pandas
import datetime as dt
import random
import smtplib

time = dt.datetime.now()
today = (time.month, time.day)
MY_EMAIL = "sidd.automation@gmail.com"
MY_PASS = "password"

data = pandas.read_csv("birthdays.csv")
birthday_dates = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today in birthday_dates:
    birthday_person = birthday_dates[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        final_letter = content.replace(f"[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n{final_letter}")


