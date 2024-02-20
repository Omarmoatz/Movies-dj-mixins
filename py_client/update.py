import requests

endpoint = "http://127.0.0.1:8000/meal/7/update/"

data = {
    "name":"pasta updated",
    "description":"description updated",
    "price":150.88,
    "category":'1',
    "people":2,
    "preperation_time":'0:30:0'
}

get_request = requests.put(endpoint, json=data)
print(get_request.json())