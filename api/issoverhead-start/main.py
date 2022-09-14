import requests
from datetime import datetime
import smtplib

MY_LAT = 25.312717 # Your latitude
MY_LONG = 86.490608 # Your longitude
def sendmail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="saurabhpandeyjmp@gmail.com",
            msg=f"Subject:ALERT ISS ABOVE U \n\n LOOK UP"
        )
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
if((iss_latitude-MY_LAT<5 or iss_latitude-MY_LAT>-5 )and (iss_longitude-MY_LONG<5 or iss_longitude-MY_LONG>-5)):
    sendmail()


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
MY_EMAIL="kumarnikhilsaurabh@gmial.com"
password="oasfaqpoujwvnqqx"

# BONUS: run the code every 60 seconds.



