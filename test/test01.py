import requests
import json
from flask import jsonify

url='http://127.0.0.1:8000/pizza-delivery-api/order'
data={
    'user_name':'Savyo',
    'pizza_size':'M',
    'pizza_type':'Pepperoni',
    'phone_number' : 6478543298
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_data, headers=headers)

response_data = response.json()
with open("create_order_response.json", "w") as json_file:
    json.dump(response_data, json_file, indent=4)