import requests
from datetime import datetime

GENDER = "male"
AGE = 21
WEIGHT_KG = 81
HEIGHT_CM = 197

APP_ID = "YOUR ID"
API_KEY = "YOUR API KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/3f3d332111d28e777785ab213fe05f87/workoutTracking/workouts"

exercise_text = input("Tell me which exercise you did?: ")
# Example:
# exercise_text = "Ran 3 miles and walked for 3Km."

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, headers=headers, json=params)
result = response.json()
print(result)

today = datetime.now()

auth_header = {
        "Authorization": "Bearer YOUR TOKEN"
    }

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": round(float(exercise["duration_min"])),
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_input,
        headers=auth_header)
    print(sheet_response.text)