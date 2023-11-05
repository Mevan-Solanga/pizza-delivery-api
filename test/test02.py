import requests
import json
from flask import jsonify

url='http://127.0.0.1:8000/pizza-delivery-api/order/4f064844-b7df-4f3e-880a-3252e719d151'
data = {
    "order_status" : "In Kitchen",
    "pizza_size" : 'L',
    "pizza_type" : None
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.put(url, data=json_data, headers=headers)

response_data = response.json()
with open("retrieve_order_response.json", "w") as json_file:
    json.dump(response_data, json_file, indent=4)