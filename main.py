import requests
from datetime import datetime
import os

APP_ID = os.environ.get('Your App ID')
APIKEY = s.environ.get('Your APIKEY')

exersise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input("Tell me which exersise did you did?")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APIKEY
  }
parameters = {
    "query" : query
}

response = requests.post(url=exersise_endpoint, json=parameters, headers=headers)
result = response.json()

BEARER_TOKEN = os.environ.get("Bearer <token>")

today =datetime.now()

for response in result["exercises"]:
    date = today.strftime("%m/%d/%Y")
    time = today.strftime("%H:%M")
    exercise = response['name'].title()
    duration = response['duration_min']
    calories = response['nf_calories']

    #psoting data to sheets
    google_sheets_api = f"https://api.sheety.co/1c296835569c77d1fcd715ee9a2f3d83/myWorkouts/workouts"

    user_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': BEARER_TOKEN
        }

    posting_workouts = requests.post(url=google_sheets_api, json=user_params, headers=headers)

