import requests
from datetime import datetime
import os

API_KEY = os.environ["API_KEY"]
API_ID = os.environ["API_ID"]
GENDER = "Male"
WEIGHT = 45
HEIGHT = 161
AGE = 21
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/8a60f259f19b1e6738ff459b9e9ce25d/workoutTracking/workouts"

exercise_text = input("Tell me what exercises you did?: ")
bearer_header = {
    "Authorization": os.environ["Authorization"],
}
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

request = requests.post(url=nutritionix_endpoint, headers=headers, json=parameters)
result = request.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_header)
    print(sheet_response.text)


