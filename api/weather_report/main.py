from multiprocessing.connection import Client
from twilio.rest import Client
import requests
account_sid="AC8434c52b1465f2b00bd9b748c9314685"

auth_token="4add51b28284466e0247b7be0f18c36c"
weather_params={"lat" : 8.537981,"lon" : -80.782127,
    "appid":"5ed9a6257eb4af08284eb8758e2e8f9e","exclude":"current,minute,daily"
    
     
}


response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=weather_params)
weather_data=response.json()
response.raise_for_status()

i=0
is_rain=False
while(i<12):
    if weather_data["hourly"][i]["weather"][0]["id"]< 700:
        is_rain=True
    i+=1



if is_rain:
    print("Bring an Umbrella")
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
            body="It's going to raiin today.",
            from_="+12283358548",
            to="+917759923707"
        )
    print(message.status)
