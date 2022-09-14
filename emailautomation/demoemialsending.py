
from multiprocessing import connection
import smtplib
from sqlite3 import connect
my_email="kumarnikhilsaurabh@gmail.com"
password="oasfaqpoujwvnqqx"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="saurabhpandeyjmp@gmail.com",msg="Subject:HELLO\n\nThis is the body of my email")
connection.close()


"""
import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()

date_of_birth=dt.datetime(year=2003,month=12,day=8)
print(date_of_birth)
"""