import random
import smtplib
import datetime as dt

day = dt.datetime.now()
weekday = day.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        quotes = [item for item in file.readlines()]
        quote = random.choice(quotes)


my_email = "sidd.automation@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="siddhant.kedar568989@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n{quote}")

print(quote)
