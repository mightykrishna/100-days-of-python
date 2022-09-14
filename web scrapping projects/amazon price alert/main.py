import time
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from tkinter import messagebox

messagebox.showinfo('Amazon Price Checker v1.0', "Welcome to Amazon Price Checker v1.0\n"
"Notice:\nYour email should be a Gmail Account\n"
"URL Example: https://www.amazon.com/Elden-Ring-PlayStation-5/dp/B09743F8P6")

message = "Welcome to Amazon Price Checker v1.0\n\n Notice:\n Your email should be a Gmail Account\n "
"URL Example: https://www.amazon.com/Elden-Ring-PlayStation-5/dp/B09743F8P6 "

URL = input("Enter product URL to track price: ")
#class_string = input("Enter URL class string for the item price on the website: ")
#my_email = input("Enter Your Email address: ")
#password = input("Enter Your Emails Password: ")
#receiver = input("Enter the Email address of the receiver: ")
#interval = int(input("Enter time to check price in seconds: "))
#set_price = float(input("Enter the price of the item to notify accepts float number only: "))

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
##def send_mail(): ##Send email function.
 #   global my_email, password, receiver
 #   with smtplib.SMTP("smtp.gmail.com", 587) as connection:
 #       connection.starttls()
 #       connection.login(user=my_email, password=password)
 #       connection.sendmail(from_addr=my_email,
 #       to_addrs=receiver,
 #       msg=f"Subject:Item Price Dropped\n\nYour item price has dropped to: {price}")

#def check_price():
#    global interval, final_price
#    print(f"Checking for price drop, current price is {price}")
#    if final_price <= set_price:
#        send_mail()
#        print("Waiting...")
#        time.sleep(interval)
#    else:
#        print("Waiting...")
#        time.sleep(interval)

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
find_price = soup.find("span", class_="a-offscreen")
price = find_price.getText()
print(price)
if "$" in price:
    pure_price = price.replace('$', '')
    final_price = float(pure_price.replace(",", ""))
    print(final_price)

#is_on = True
#while is_on:
#    check_price()