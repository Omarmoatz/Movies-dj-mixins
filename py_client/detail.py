import requests

endpoint = "http://127.0.0.1:8000/meal/1/"

get_request = requests.get(endpoint)
print(get_request.json())