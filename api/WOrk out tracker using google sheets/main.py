API_ID="c8d814ff"
API_KEY="75373df4a5f755d95940de94a837ae8c"

import requests

GENDER ="Male"
WEIGHT_KG ="80"
HEIGHT_CM ="170"
AGE ="19"



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)