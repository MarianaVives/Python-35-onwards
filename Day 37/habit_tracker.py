import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN_USER= "abdjeje32"
USERNAME= "devusername"
GRAPH_ID= "test-graph"

now = dt.datetime.now()
yesterday = now - dt.timedelta(days=1)

POST_PARAMS = {
    "token": TOKEN_USER,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

POST_GRAPH = {
    "id": GRAPH_ID,
    "name":"Habit-Tracker",
    "unit":"Programming",
    "type": "int",
    "color":"ajisai"
}
HEADERS = {
    "X-USER-TOKEN": TOKEN_USER
}
POST_VALUE = {
    "date":now.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend programming today?")
}

UPDATE_VALUE = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "20"

}

#STEP 1 - Create a user
create_user = requests.post(url= PIXELA_ENDPOINT, json=POST_PARAMS)
print(create_user.text)
#STEP 2 - Create a graph
create_graph = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=POST_GRAPH,  headers=HEADERS)
print(create_graph.text)
#STEP 3 - Look at graph in https://pixe.la/v1/users/devusername/graphs/test-graph
#STEP 4 - Post a value in the graph
post_value = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", json=POST_VALUE, headers=HEADERS)
print(post_value.text)
#STEP 5 - Update and delete values in the graph
#update_value = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}", json=UPDATE_VALUE, headers=HEADERS)
#print(update_value.text)
#STEP 6 - Delete value in the graph
#delete_value = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}", headers=HEADERS)
#print(delete_value.text)