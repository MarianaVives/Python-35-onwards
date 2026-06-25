import requests
import datetime as dt

APP_ID = "app_593dd304c3f14b4d829d3c4c"
API_KEY = "nix_live_1iYHsCiDgtuKqTwO9886dBjJbbQ9jQPR"
BASE_URL = "https://app.100daysofpython.dev"
WEIGHT_KG = 51
HEIGHT_CM = 165
AGE = 32
GENDER = "female"
BEARER_TKN = "myBearerT0k3n"

POST_EXERCISE_URL = "v1/nutrition/natural/exercise"
POST_SHEETY_URL = "https://api.sheety.co/310e1e03f24b53778bffd997055e2aaf/myWorkouts/workouts"
CALORIES_BURNT_POST = {
      "query": input("What exercise did you do today?"),
      "weight_kg": WEIGHT_KG,
      "height_cm": HEIGHT_CM,
      "age": AGE,
      "gender": GENDER
}

HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": f"Bearer {BEARER_TKN}",
}

# Calculate burned calories from an exercise session
post_exercise = requests.post(url=f"{BASE_URL}/{POST_EXERCISE_URL}", headers=HEADERS, json=CALORIES_BURNT_POST)
result = post_exercise.json()

now = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")
get_sheety = requests.get(url=f"https://api.sheety.co/310e1e03f24b53778bffd997055e2aaf/myWorkouts/workouts", headers=HEADERS)
print(get_sheety.text)

for r in result['exercises']:
    data_entry= {
      "workout": {
          "date":now,
          "time":now_time,
          "exercise":r['user_input'],
          "duration":r['duration_min'],
          "calories":r['nf_calories'],
      }
    }
    post_sheet_response = requests.post(url=f"{POST_SHEETY_URL}", json=data_entry, headers=HEADERS)
    print(post_sheet_response.text)

get_sheety = requests.get(url=f"https://api.sheety.co/310e1e03f24b53778bffd997055e2aaf/myWorkouts/workouts")
print(get_sheety)