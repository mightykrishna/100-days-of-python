##################### Extra Hard Starting Project ######################
from email import iterators
import pandas
import datetime as dt
import random
import smtplib
MY_EMAIL = "kumarnikhilsaurabh@gmail.com"
MY_PASSWORD = "oasfaqpoujwvnqqx"


today=dt.datetime.now()
today_tuple=(today.month,today.day)
# 1. Update the birthdays.csv



data=pandas.read_csv("list_of_birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for(index,data_row)in data.iterators()}

# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="saurabhpandeyjmp@gmail.com",
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




