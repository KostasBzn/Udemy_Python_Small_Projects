'''
To test and use this tool you have to do the following steps:
1. Sign up at nutritionix.com/business/api
Get your:
APP ID
APP KEY

2. Sign up at sheety.co with your google account
Create a new google sheet (with the same google email)
Create new project and connect Google Sheet
Get your:
Sheety API endpoint (e.g., https://api.sheety.co/{your-api-id}/{project_name}/{sheet_name})
Authorization token (starts with "Bearer") you will find it in the authentication menu.

3. Create a .env and set yout enviroment variables

4. python3 main.py
'''

import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

nutritionix_app_id = os.getenv('NUTRITIONIX_APP_ID')
nutritionix_app_key = os.getenv('NUTRITIONIX_APP_KEY')
sheety_api = os.getenv('SHEETY_API')
sheety_auth = os.getenv('SHEETY_AUTH')

nutritionix_domain = "https://trackapi.nutritionix.com"
project_name = "workoutTracking"
sheet_name = "workouts"

now = datetime.now()

def input_activity():
    try:
        usr_in = input("Tell me which exercises you did: ")
        hdr = {
            'x-app-id' : nutritionix_app_id,
            'x-app-key': nutritionix_app_key
        }
        body = {
            'query' : usr_in,
            'gender': 'male',
            'weight_kg': 82,
            'height_cm': 183,
            'age':41
        }
        endpoint = f"{nutritionix_domain}/v2/natural/exercise"
        print(f"[*] Generating activities with Nutritionix API...")
        res = requests.post(url=endpoint, json=body, headers=hdr)
        res.raise_for_status()
        print(f"[+] Activities generated")
        return res.json()
        
    except ValueError as e:
        print(f"Input error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

def save_activities(activities):
    date_now = now.strftime("%d/%m/%Y")
    time_now = now.strftime("%I:%M %p")
    hdr = {
            'Authorization': sheety_auth
        }
    try:
        print(f"[*] Uploading activities...")
        for actv in activities['exercises']:
            workout = {
                "workout": {
                        "date" : date_now,
                        "time" : time_now,
                        "exercise" : actv['name'].title(),
                        "duration" : actv['duration_min'],
                        "calories" : actv['nf_calories'],

                }
            }
            res = requests.post(url=f"https://api.sheety.co/{sheety_api}/{project_name}/{sheet_name}", json=workout, headers=hdr)
            res.raise_for_status()
        print(f"[+] Activities saved")
        
    except requests.exceptions.RequestException as e:
        print(f"Error saving the activities: {e}")
    


def main():
    try:
        activities = input_activity()
        save_activities(activities)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

