import requests
from datetime import datetime

USERNAME = "watnick"
TOKEN = "qR:&+2>FB;wxC*R4"
GRAPH_ID = "graph1"

#   Creating pixela user account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#   Creating a graph with all the required json params
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#   Post pixel data on your graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

#   Update exist pixel
update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "2.70",
}
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

#   Delete exist pixel
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
