import requests

meal_id = input('enter the meal id you want to delete : ')
endpoint = f"http://127.0.0.1:8000/meal/{meal_id}/delete/"

get_request = requests.delete(endpoint)
if get_request.status_code == 404:
    print('Meal not found')
else:
    print(get_request.status_code)
