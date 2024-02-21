import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/auth/"

username = input("Enter your username:\n ")
password = getpass('Enter your password:\n ')

data ={
    "username":username,
    "password":password
}

get_token = requests.post(endpoint, json=data)
print(get_token.json())

if get_token.status_code == 200:
    token = get_token.json()['token']
    endpoint = "http://127.0.0.1:8000/meal/list/"

    headers = {
        "Authorization": f"Token {token}"
    }
    get_request = requests.get(endpoint,headers=headers)
    print(get_request.json())