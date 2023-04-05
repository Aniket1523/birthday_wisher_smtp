import datetime as dt
import pandas
import random
import smtplib

my_email = "tpython02@gmail.com"
password = "emjoacmqipomxuao"

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
tod = dt.datetime.now()
tod_day = tod.day
tod_month = tod.month
tod_year = tod.year

birthday_data = pandas.read_csv("birthdays.csv")
result = [row for row in
          zip(birthday_data['name'], birthday_data['email'], birthday_data['year'], birthday_data['month'],
              birthday_data['day']) if row[2] == tod_year and row[3] == tod_month and row[4] == tod_day]
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for row in result:
        name = row[0]
        email = row[1]
        letter = random.choice(letter_templates)
        with open("./letter_templates/" + letter, "r") as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace("[NAME]", name)

        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Birthday Wish \n\n {new_letter}")
