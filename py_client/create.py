import requests

endpoint = "http://127.0.0.1:8000/meal/create/"

data = {
    "name":"pasta",
    "description":None,
    "price":150.88,
    "category":'1',
    "people":2,
    "preperation_time":'0:30:0'
}

get_request = requests.post(endpoint, json=data)
print(get_request.json())