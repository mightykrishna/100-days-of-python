from http.client import ResponseNotReady
import requests
from tomlkit import datetime
from datetime import datetime 
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="kumarnikhilsaurabh"
USERNAME="saurabhpandeyjmp"
user_params={
    "token":TOKEN,
    "username":"saurabhpandeyjmp",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"saruabh0008",
    "name":"Meditation",
    "unit":"minutes",
    "type":"int",
    "color":"momiji"
}
headers={
    "X-USER-TOKEN":TOKEN
}
today=datetime(year=2022,month=7,day=30)
post_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":"50",
    
}
post_endpoint=f"{pixela_endpoint}/saurabhpandeyjmp/graphs/saruabh0008"

put_params={
    "quantity":"100"
}
put_endpoint=f"{pixela_endpoint}/saurabhpandeyjmp/graphs/saruabh0008/{today.strftime('%Y%m%d')}"
response=requests.put(url=put_endpoint,json=put_params,headers=headers)
#response=requests.post(url=post_endpoint,json=post_params,headers=headers)
#response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#response=requests.post(url=pixela_endpoint,json=user_params)


print(response.text)