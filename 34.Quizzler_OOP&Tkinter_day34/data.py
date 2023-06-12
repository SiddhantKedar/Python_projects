import requests

request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
request.raise_for_status()
data = request.json()
#print(data)

question_data = data["results"]
#print(question_data)
