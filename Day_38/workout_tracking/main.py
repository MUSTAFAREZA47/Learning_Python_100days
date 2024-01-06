import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")


NUTRITION_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")


headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

data = {
    "query": input("What did you exercise today? ")
}

response_nutrition_data = requests.post(url=NUTRITION_API_ENDPOINT, headers=headers, json=data)

data = response_nutrition_data.json()

# exercise_name = [exercise['name'] for exercise in data]
# exercise_duration = [exercise['duration_min'] for exercise in data]
# exercise_calories = [exercise['nf_calories'] for exercise in data]
current_datetime = datetime.now()
date = current_datetime.strftime("%Y-%m-%d")
time = current_datetime.strftime("%X")

for exercise in data["exercises"]:
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response_sheety = requests.post(url=SHEETY_API_ENDPOINT, json=body)
    print(response_sheety.text)

