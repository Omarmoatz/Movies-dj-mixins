import requests

endpoint = "http://127.0.0.1:8000/meal/7/update/"

data = {
    "name":"pasta updated",
    "description":None,
    "price":150.88,
    "category":"pizza",
    "people":2,
    "preperation_time":'0:19:0'
}

get_request = requests.put(endpoint, json=data)
print(get_request.json())