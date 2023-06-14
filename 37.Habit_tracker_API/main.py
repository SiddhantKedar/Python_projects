import requests
from datetime import datetime

USERNAME = "sidd0automation"
TOKEN = "qazwsxedcrfv1234567890"

api_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": "qazwsxedcrfv1234567890",
    "username": "sidd0automation",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# request = requests.post(url=api_endpoint, json=user_parameters)
# print(request.text)
graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "test",
    "unit": "hour",
    "type": "int",
    "color": "ajisai"
}

today = datetime.now()
headers = {
    "X-USER-TOKEN": TOKEN
}
# request = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(request.text)

add_pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

request = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
print(request.text)
