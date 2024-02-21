import requests

endpoint = "http://127.0.0.1:8000/meal/create/"

data = {
    "name":"burger",
    "description":None,
    "price":150.88,
    "category":"pizza",
    "people":1,
    "preperation_time":'0:20:0'
}

get_request = requests.post(endpoint, json=data)
print(get_request.json())