import requests
from datetime import datetime
import json
import os

APP_ID = os.environ["APP_ID"]

API_KEY = os.environ["API_KEY"]

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
"Content-Type": "application/json",

}

body = {
 "query": input("What did you do today? "),
 "gender": "male",
 "weight_kg": float(),
 "height_cm": int(),
 "age": int()
}

response = requests.post(url=endpoint, headers=headers, json=body)

dict_response = json.loads(response.text)
print(dict_response)

# ************* Sheety ***********************

sheety_endpoint = "https://api.sheety.co/<sheet_id>/<sheet_name>/<sheet_nr>"

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M")
authorization = os.environ["Authorization"]

for i in range(len(dict_response["exercises"])):
    exercise = dict_response["exercises"][i]["user_input"]
    duration = dict_response["exercises"][i]["duration_min"]
    calories = dict_response["exercises"][i]["nf_calories"]

    header_sheety = {
     "Authorization": authorization,
    }

    sheet_config = {
       "sheet1": {
       "date": today_date,
       "time": today_time,
       "exercise": exercise,
       "duration": duration,
       "calories": calories,
      }
    }

    response_sheet = requests.post(sheety_endpoint, json=sheet_config, headers=header_sheety)
    print(response_sheet.text)
